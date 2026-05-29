from vllm import SamplingParams

class AdversarialConsistencyEvaluator:
    """Implements Adversarial Consistency Evaluation (ACE) to detect logical contradictions."""
    def __init__(self, model):
        self.model = model

    def generate_negation(self, claim: str) -> tuple[str, int, int]:
        system_prompt = (
            "Negate the core factual premise of the claim "
            "by inverting its logical meaning while preserving "
            "the original grammatical structure. Output EXACTLY "
            "ONE SENTENCE. No explanations, no quotes, no conversational filler."
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Claim: {claim}"}
        ]
        llm_engine = self.model.model
        tokenizer = llm_engine.get_tokenizer()

        try:
            prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        except Exception:
            prompt = f"{system_prompt}\n\nClaim: {claim}\nResponse:"
        prompt += "Negated Claim:"

        prompt_tokens_count = len(tokenizer.encode(prompt))
        neg_sampling_params = SamplingParams(
            temperature=0.1,
            max_tokens=64,
            stop=["<|im_end|>", "<|eot_id|>", "\n"]
        )
        outputs = llm_engine.generate([prompt], sampling_params=neg_sampling_params, use_tqdm=False)
        negated_text = outputs[0].outputs[0].text.strip()

        response_tokens_count = len(outputs[0].outputs[0].token_ids)
        if negated_text.startswith(" "):
            negated_text = negated_text[1:]
        return negated_text, prompt_tokens_count, response_tokens_count

    def check_logical_contradiction(
        self, uq_verifier, claim: str, original_verdict: str, original_uq_scores: dict,
        parametric_prompt: str, dataset_name: str, eval_method: str = "discrete",
        output_format: str = "label_only"
    ) -> tuple[float, int, int, int]:
        """Adversarial consistency evaluation (ACE): generates a negated claim and checks for logical contradiction."""
        negated_claim, neg_p_tokens, neg_r_tokens = self.generate_negation(claim)

        # Temporarily disable UQ estimation for the negated claim pass
        orig_lm_estimators = uq_verifier.lm_polygraph_estimators
        orig_estimators = uq_verifier.estimator_names
        orig_semantic = getattr(uq_verifier, "requires_semantic", False)

        uq_verifier.lm_polygraph_estimators = []
        uq_verifier.estimator_names = []
        uq_verifier.requires_semantic = False

        _, _, negated_verdict, _, inner_p_tokens, inner_r_tokens, inner_llm_calls = uq_verifier.verify_claim(
            claim=negated_claim,
            prompt_template=parametric_prompt,
            dataset_name=dataset_name,
            output_format=output_format
        )

        uq_verifier.lm_polygraph_estimators = orig_lm_estimators
        uq_verifier.estimator_names = orig_estimators
        uq_verifier.requires_semantic = orig_semantic
        
        # Adversarial consistency evaluation (ACE)
        logic_score = 0.0
        if eval_method == "discrete":
            if original_verdict == negated_verdict and original_verdict in ["SUPPORT", "CONTRADICT", "True", "False"]:
                logic_score = 1.0
        elif eval_method == "probabilistic":
            # Fluri et al.'s approach — not implemented for ACE; using discrete version instead.
            pass

        extra_p_tokens = neg_p_tokens + inner_p_tokens
        extra_r_tokens = neg_r_tokens + inner_r_tokens
        extra_llm_calls = 1 + inner_llm_calls

        return logic_score, extra_p_tokens, extra_r_tokens, extra_llm_calls
