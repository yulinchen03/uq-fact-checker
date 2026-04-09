# Quantemp Decomposition Comparison

## Sample ID: quantemp_0
**Original Claim**: Image shows train abadoned in Sri Lanka's hillcountry in 1927

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Image shows train abandoned in Sri Lanka's hillcountry in 1927 | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An image shows a train abandoned in Sri Lanka's hill country in 1927. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Sri Lanka<br>2. 1927 | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An image shows a train abandoned in Sri Lanka's hillcountry in 1927. | 1 |
| google/gemma-3-1b-it | 1. Image shows a train abandoned in Sri Lanka’s hillcountry in 1927. | 1 |
| google/gemma-3-4b-it | 1. The image shows a train.<br>2. The train is abandoned.<br>3. The train is in Sri Lanka.<br>4. The train is in Sri Lanka's hillcountry.<br>5. The train was in 1927. | 5 |
| gpt-3.5-turbo-0125 | 1. The image shows a train abandoned in Sri Lanka's hill country in 1927. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The image shows a train abandoned in Sri Lanka's hillcountry in 1927. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Image shows train abadoned in Sri Lanka's hillcountry in 1927 | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Image shows train abadoned in Sri Lanka's hillcountry in 1927. | 1 |

---

## Sample ID: quantemp_1
**Original Claim**: Says Ted Strickland supported giving $150 billion to Iranian regime that persecutes women, Christians and gays.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Ted Strickland supported giving $150 billion to the Iranian regime.<br>2. The Iranian regime persecutes women, Christians, and gays. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Ted Strickland supported giving $150 billion to the Iranian regime.<br>2. The Iranian regime persecutes women, Christians, and gays. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Ted Strickland is a U.S. politician.<br>2. He supported giving $150 billion to the Iranian regime.<br>3. The Iranian regime persecutes women, Christians, and gays. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Ted Strickland supported giving $150 billion to the Iranian regime.<br>2. The Iranian regime persecutes women.<br>3. The Iranian regime persecutes Christians.<br>4. The Iranian regime persecutes gays. | 4 |
| google/gemma-3-1b-it | 1. Ted Strickland supported giving $150 billion to Iranian regime that persecutes women, Christians and gays. | 1 |
| google/gemma-3-4b-it | 1. Ted Strickland says he supported giving $150 billion to Iranian regime.<br>2. The Iranian regime persecutes women.<br>3. The Iranian regime persecutes Christians.<br>4. The Iranian regime persecutes gays. | 4 |
| gpt-3.5-turbo-0125 | 1. Ted Strickland supported giving $150 billion to Iranian regime.<br>2. Iranian regime persecutes women.<br>3. Iranian regime persecutes Christians.<br>4. Iranian regime persecutes gays. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Ted Strickland supported giving $150 billion to the Iranian regime.<br>2. The Iranian regime persecutes women.<br>3. The Iranian regime persecutes Christians.<br>4. The Iranian regime persecutes gays. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Says Ted Strickland supported giving $150 billion to Iranian regime that persecutes women, Christians and gays. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Ted Strickland supported giving $150 billion to Iranian regime.<br>2. Iranian regime persecutes women.<br>3. Iranian regime persecutes Christians.<br>4. Iranian regime persecutes gays. | 4 |

---

## Sample ID: quantemp_2
**Original Claim**: Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Rosie O'Donnell bribed two senators.<br>2. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill.<br>3. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill.<br>2. The bribery occurred via Twitter. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Rosie O'Donnell is a U.S. politician.<br>2. Rosie O'Donnell is a U.S. politician.<br>3. Rosie O'Donnell is a U.S. politician.<br>4. Rosie O'Donnell is a U.S. politician.<br>5. Rosie O'Donnell is a U.S. politician.<br>6. Rosie O'Donnell is a U.S. politician.<br>7. Rosie O'Donnell is a U.S. politician.<br>8. Rosie O'Donnell is a U.S. politician.<br>9. Rosie O'Donnell is a U.S. politician.<br>10. Rosie O'Donnell is a U.S. politician.<br>11. Rosie O'Donnell is a U.S. politician.<br>12. Rosie O'Donnell is a U.S. politician.<br>13. Rosie O'Donnell is a U.S. politician.<br>14. Rosie O'Donnell is a U.S. politician.<br>15. Rosie O'Donnell is a U.S. politician.<br>16. Rosie O'Donnell is a U.S. politician.<br>17. Rosie O'Donnell is a U.S. politician.<br>18. Rosie O'Donnell is a U.S. politician.<br>19. Rosie O'Donnell is a U.S. politician.<br>20. Rosie O'Donnell is a U | 20 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter.<br>2. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill.<br>3. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill in the United States. | 3 |
| google/gemma-3-1b-it | 1. Rosie O’Donnell bribed two senators to vote “no” on the GOP tax bill via Twitter. | 1 |
| google/gemma-3-4b-it | 1. Rosie O'Donnell bribed two senators.<br>2. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill.<br>3. Rosie O'Donnell bribed two senators via Twitter. | 3 |
| gpt-3.5-turbo-0125 | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Rosie O'Donnell bribed two senators to vote "no" on the GOP tax bill via Twitter. | 1 |

---

## Sample ID: quantemp_3
**Original Claim**: The City of Atlanta has invited residents to watch the implosion of Stone Mountain on 5 August 2018.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The City of Atlanta invited residents to watch the implosion of Stone Mountain.<br>2. The implosion of Stone Mountain occurred on 5 August 2018.<br>3. The City of Atlanta invited residents to watch the implosion of Stone Mountain on 5 August 2018. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain.<br>2. The implosion of Stone Mountain is scheduled for 5 August 2018. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain on 5 August 2018.<br>2. Stone Mountain is a 1,300-acre park in Atlanta.<br>3. Stone Mountain is located in the state of Georgia.<br>4. Stone Mountain is a popular tourist destination.<br>5. Stone Mountain is a prominent landmark in Atlanta.<br>6. Stone Mountain is a site of historical significance.<br>7. Stone Mountain is a location in the state of Georgia.<br>8. Stone Mountain is a prominent landmark in Atlanta.<br>9. Stone Mountain is a site of historical significance.<br>10. Stone Mountain is a location in the state of Georgia. | 10 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The City of Atlanta is the location of the event.<br>2. The implosion of Stone Mountain occurred in the City of Atlanta.<br>3. The implosion of Stone Mountain occurred on 5 August 2018.<br>4. The City of Atlanta invited residents to watch the implosion of Stone Mountain. | 4 |
| google/gemma-3-1b-it | 1. The City of Atlanta invited residents to watch the implosion of Stone Mountain on August 5, 2018.<br>2. The City of Atlanta invited residents to watch the implosion of Stone Mountain. | 2 |
| google/gemma-3-4b-it | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain.<br>2. The implosion of Stone Mountain is scheduled for 5 August 2018. | 2 |
| gpt-3.5-turbo-0125 | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain on 5 August 2018. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The City of Atlanta invited residents to watch the implosion of Stone Mountain on 5 August 2018. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain on 5 August 2018. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The City of Atlanta has invited residents to watch the implosion of Stone Mountain on 5 August 2018. | 1 |

---

## Sample ID: quantemp_4
**Original Claim**: In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives, asking them to fire Whoopi Goldberg and Joy Behar as hosts.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. The petition was signed by more than 1 million fans of "The View".<br>3. The petition was sent to ABC executives.<br>4. The petition asked ABC executives to fire Whoopi Goldberg as a host.<br>5. The petition asked ABC executives to fire Joy Behar as a host. | 5 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In July 2023, a petition was signed by more than 1 million fans of "The View".<br>2. The petition was sent to ABC executives, asking them to fire Whoopi Goldberg and Joy Behar as hosts. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. ABC executives<br>2. July<br>3. 2023<br>4. Whoopi Goldberg<br>5. Joy Behar<br>6. The View | 6 |
| meta-llama/Llama-3.2-3B-Instruct | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. The petition was signed by fans of "The View".<br>3. The petition was sent to ABC executives.<br>4. ABC executives were asked to fire Whoopi Goldberg and Joy Behar as hosts. | 4 |
| google/gemma-3-1b-it | 1. A petition signed by more than 1 million fans of “The View” was sent to ABC executives.<br>2. The petition was sent in July 2023.<br>3. A petition signed by more than 1 million fans of “The View” was sent to ABC executives.<br>4. The petition asked ABC executives to fire Whoopi Goldberg and Joy Behar. | 4 |
| google/gemma-3-4b-it | 1. In July 2023, a petition was sent to ABC executives.<br>2. The petition was signed by more than 1 million fans of "The View."<br>3. The petition was sent to ABC executives.<br>4. "The View" is a television program.<br>5. Whoopi Goldberg was asked to be fired.<br>6. Joy Behar was asked to be fired. | 6 |
| gpt-3.5-turbo-0125 | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. The petition asked ABC executives to fire Whoopi Goldberg as a host of "The View."<br>3. The petition asked ABC executives to fire Joy Behar as a host of "The View." | 3 |
| gpt-4.1-mini-2025-04-14 | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. The petition sent to ABC executives in July 2023 asked ABC executives to fire Whoopi Goldberg as a host of "The View."<br>3. The petition sent to ABC executives in July 2023 asked ABC executives to fire Joy Behar as a host of "The View." | 3 |
| gpt-5.4-nano-2026-03-17 | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. In July 2023, the petition signed by more than 1 million fans of "The View" asked ABC executives to fire Whoopi Goldberg as a host.<br>3. In July 2023, the petition signed by more than 1 million fans of "The View" asked ABC executives to fire Joy Behar as a host. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. In July 2023, a petition signed by more than 1 million fans of "The View" was sent to ABC executives.<br>2. In July 2023, a petition signed by more than 1 million fans of "The View" asked ABC executives to fire Whoopi Goldberg as a host.<br>3. In July 2023, a petition signed by more than 1 million fans of "The View" asked ABC executives to fire Joy Behar as a host. | 3 |

---

## Sample ID: quantemp_5
**Original Claim**: "A cashier earning $20,000 per year pays the same (Virginia) income tax rate as a hedge fund manager earning $20 million per year."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A cashier earning $20,000 per year pays the same income tax rate as a hedge fund manager earning $20 million per year in Virginia. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A cashier earning $20,000 per year pays the same Virginia income tax rate as a hedge fund manager earning $20 million per year. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A cashier earning $20,000 per year pays the same income tax rate as a hedge fund manager earning $20 million per year.<br>2. The income tax rate for a cashier earning $20,000 per year is 0.01%.<br>3. The income tax rate for a hedge fund manager earning $20 million per year is 0.01%. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A cashier earning $20,000 per year pays the same income tax rate as a hedge fund manager earning $20 million per year in Virginia.<br>2. The cashier earning $20,000 per year pays the same income tax rate as the hedge fund manager earning $20 million per year in Virginia. | 2 |
| google/gemma-3-1b-it | 1. A cashier earning $20,000 per year pays the same (Virginia) income tax rate as a hedge fund manager earning $20 million per year. | 1 |
| google/gemma-3-4b-it | 1. A cashier earns $20,000 per year.<br>2. The cashier lives in Virginia.<br>3. A hedge fund manager earns $20 million per year.<br>4. The hedge fund manager lives in Virginia.<br>5. The cashier pays the same (Virginia) income tax rate as the hedge fund manager. | 5 |
| gpt-3.5-turbo-0125 | 1. A cashier earning $20,000 per year pays the same (Virginia) income tax rate as a hedge fund manager earning $20 million per year. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A cashier earning $20,000 per year pays the same Virginia income tax rate as a hedge fund manager earning $20 million per year. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A cashier earning $20,000 per year pays the same (Virginia) income tax rate as a hedge fund manager earning $20 million per year. | 1 |

---

## Sample ID: quantemp_6
**Original Claim**: Bundeswirtschaftsminister Robert Habeck habe am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe und damit große Spekulationsgewinne erziele. Deutschland müsse dann einfach darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Bundeswirtschaftsminister Robert Habeck hat am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe.<br>2. Bundeswirtschaftsminister Robert Habeck hat am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland derzeit große Spekulationsgewinne erziele.<br>3. Deutschland müsse dann einfach darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Robert Habeck, the Bundeswirtschaftsminister, confirmed on July 29, 2022, at 19:00, that Germany is currently exporting natural gas abroad.<br>2. Germany is currently exporting natural gas abroad.<br>3. Germany must ensure that the natural gas storage is at least 90% full by October 2022. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Bundeswirtschaftsminister Robert Habeck confirmed on July 29, 2022, at 19 Uhr on ZDF, that Germany is currently exporting gas to the outside and thereby generating significant speculative gains.<br>2. Germany must therefore focus on ensuring that its gas storage facilities are at least 90% full by October 2022. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Bundeswirtschaftsminister Robert Habeck confirmed on 29 July 2022 at 19:00 in ZDF Heute that Germany is currently selling Erdgas abroad and thus earning large speculative profits.<br>2. Germany must ensure that its gas storage facilities are at least 90 percent full by October 2022. | 2 |
| google/gemma-3-1b-it | 1. Robert Habeck confirmed that Germany is currently selling gas abroad and has generated large speculative gains.<br>2. Germany must ensure that the gas reserves in Germany are at least 90 percent full in October 2022. | 2 |
| google/gemma-3-4b-it | 1. Bundeswirtschaftsminister Robert Habeck habe am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt.<br>2. Deutschland derzeit Erdgas ins Ausland weiterverkaufe.<br>3. Deutschland große Spekulationsgewinne erziele.<br>4. Deutschland müsse dann einfach darauf achten.<br>5. Die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent seien. | 5 |
| gpt-3.5-turbo-0125 | 1. Bundeswirtschaftsminister Robert Habeck bestätigte am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe und damit große Spekulationsgewinne erziele.<br>2. Deutschland müsse dann einfach darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Bundeswirtschaftsminister Robert Habeck hat am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe.<br>2. Bundeswirtschaftsminister Robert Habeck hat am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland mit dem Weiterverkauf von Erdgas ins Ausland große Spekulationsgewinne erziele.<br>3. Deutschland müsse am 29. Juli 2022 einfach darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Bundeswirtschaftsminister Robert Habeck bestätigte am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe.<br>2. Bundeswirtschaftsminister Robert Habeck bestätigte am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera, dass Deutschland damit große Spekulationsgewinne erziele.<br>3. Deutschland müsse darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Bundeswirtschaftsminister Robert Habeck habe am 29. Juli 2022 um 19 Uhr in ZDF Heute vor laufender Kamera bestätigt, dass Deutschland derzeit Erdgas ins Ausland weiterverkaufe und damit große Spekulationsgewinne erziele.<br>2. Deutschland müsse dann einfach darauf achten, dass die Gasspeicher im Oktober 2022 zu mindestens 90 Prozent voll seien. | 2 |

---

## Sample ID: quantemp_7
**Original Claim**: Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this.<br>2. Imran Khan is a Pakistani politician.<br>3. Imran Khan is a Pakistani politician.<br>4. Imran Khan is a Pakistani politician.<br>5. Imran Khan is a Pakistani politician.<br>6. Imran Khan is a Pakistani politician.<br>7. Imran Khan is a Pakistani politician.<br>8. Imran Khan is a Pakistani politician.<br>9. Imran Khan is a Pakistani politician.<br>10. Imran Khan is a Pakistani politician.<br>11. Imran Khan is a Pakistani politician.<br>12. Imran Khan is a Pakistani politician.<br>13. Imran Khan is a Pakistani politician.<br>14. Imran Khan is a Pakistani politician.<br>15. Imran Khan is a Pakistani politician.<br>16. Imran Khan is a Pakistani politician.<br>17. Imran Khan is a Pakistani politician.<br>18. Imran Khan is a Pakistani politician.<br>19. Imran Khan is a Pakistani politician.<br>20. Imran Khan is a Pakistani politician.<br>21. Imran Khan is a Pakistani politician.<br>22. Imran Khan is a Pakistani politician.<br>23. Imran Khan is a Pakistani politician.<br>24. Imran Khan is a Pakistani politician.<br>25. Imran Khan is a Pakistani politician.<br>26. Imran Khan is a Pakistani politician.<br>27. Imran Khan is | 27 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Imran Khan publicly admitted that in 73 years India had a government as strong and iron-willed as this. | 1 |
| google/gemma-3-1b-it | 1. Imran Khan publicly admitted that in 73 years India had never had a government as strong and iron-willed as this. | 1 |
| google/gemma-3-4b-it | 1. Imran Khan publicly admits that in 73 years India had never had a government.<br>2. The government was as strong and iron-willed as this. | 2 |
| gpt-3.5-turbo-0125 | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this government. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Imran Khan publicly admits that in 73 years India had never had a government as strong and iron-willed as this. | 1 |

---

## Sample ID: quantemp_8
**Original Claim**: An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An image was taken during the French occupation of Congo in 1955.<br>2. The image shows two white children sitting between a black child inside a cage. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The French occupation of Congo in 1955 was taken by an image of two white children sitting between a black child inside a cage.<br>2. The French occupation of Congo in 1955 was taken by an image of two white children sitting between a black child inside a cage.<br>3. The French occupation of Congo in 1955 was taken by an image of two white children sitting between a black child inside a cage. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An image of two white children was taken inside a cage.<br>2. Two white children were taken inside a cage.<br>3. A black child was taken inside a cage.<br>4. An image of a black child was taken inside a cage.<br>5. Two white children were sitting between a black child.<br>6. A black child was sitting between two white children.<br>7. An image of two white children was taken between a black child.<br>8. A black child was sitting between two white children. | 8 |
| google/gemma-3-1b-it | 1. An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955. | 1 |
| google/gemma-3-4b-it | 1. An image of two white children sitting between a black child inside a cage was taken.<br>2. The image was taken during the French occupation of Congo.<br>3. The French occupation of Congo occurred in 1955. | 3 |
| gpt-3.5-turbo-0125 | 1. The image was taken during the French occupation of Congo in 1955.<br>2. The image shows two white children sitting between a black child inside a cage. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. An image of two white children sitting between a black child inside a cage was taken during the French occupation of Congo in 1955. | 1 |

---

## Sample ID: quantemp_9
**Original Claim**: Lawsuit about Detroit voter rolls affected 2020 vote

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A lawsuit about Detroit voter rolls affected the 2020 vote in Detroit. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A lawsuit about Detroit voter rolls affected the 2020 vote. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Lawsuit about Detroit voter rolls affected 2020 vote.<br>2. Lawsuit about Detroit voter rolls was filed in 2020.<br>3. Lawsuit about Detroit voter rolls was filed in 2020.<br>4. Lawsuit about Detroit voter rolls was filed in 2020. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Lawsuit about Detroit voter rolls affected the 2020 vote. | 1 |
| google/gemma-3-1b-it | 1. Lawsuit about Detroit voter rolls affected 2020 vote. | 1 |
| google/gemma-3-4b-it | 1. There is a lawsuit about Detroit voter rolls.<br>2. The lawsuit affected the 2020 vote. | 2 |
| gpt-3.5-turbo-0125 | 1. The lawsuit was about Detroit voter rolls.<br>2. The lawsuit affected the 2020 vote. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A lawsuit about Detroit voter rolls affected the 2020 vote. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Lawsuit about Detroit voter rolls affected the 2020 vote. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Lawsuit about Detroit voter rolls affected 2020 vote. | 1 |

---

## Sample ID: quantemp_10
**Original Claim**: Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache ähnliche oder gar schlimmere Symptome als Covid-19. Der Impfstoff sei zudem laut der U.S. Food and Drug Administration (FDA) nicht zugelassen.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A comparison with the symptoms of a Covid-19 infection creates the impression that the Biontech/Pfizer vaccination causes symptoms similar to or worse than Covid-19.<br>2. The Biontech/Pfizer vaccine is additionally stated to be not approved according to the U.S. Food and Drug Administration (FDA). | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A comparison with the symptoms of a Covid-19 infection creates the impression that the Biontech/Pfizer vaccine causes similar or even worse symptoms than Covid-19.<br>2. The U.S. Food and Drug Administration (FDA) has not approved the vaccine. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer ähnliche oder gar schlimmere Symptome als Covid-19 zu verursachen.<br>2. Der Impfstoff von Biontech/Pfizer ist laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A comparison with the symptoms of a Covid-19 infection leads to the impression that the Biontech/Pfizer vaccine causes similar or even more severe symptoms than Covid-19.<br>2. The Biontech/Pfizer vaccine causes similar or even more severe symptoms than Covid-19.<br>3. The Biontech/Pfizer vaccine is not approved by the U.S. Food and Drug Administration (FDA). | 3 |
| google/gemma-3-1b-it | 1. A comparison with symptoms of a Covid-19 infection leads to the impression that the vaccination of Biontech/Pfizer causes similar or more severe symptoms as Covid-19.<br>2. The vaccine is reportedly not approved by the U.S. Food and Drug Administration (FDA). | 2 |
| google/gemma-3-4b-it | 1. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck.<br>2. Die Impfung von Biontech/Pfizer verursache ähnliche oder gar schlimmere Symptome als Covid-19.<br>3. Der Impfstoff sei zudem laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 3 |
| gpt-3.5-turbo-0125 | 1. Ein Vergleich mit den Symptomen einer Covid-19-Erkrankung lässt den Eindruck entstehen, dass die Impfung von Biontech/Pfizer ähnliche oder sogar schlimmere Symptome als Covid-19 verursacht.<br>2. Der Impfstoff von Biontech/Pfizer ist laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache ähnliche Symptome wie Covid-19.<br>2. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache gar schlimmere Symptome als Covid-19.<br>3. Der Impfstoff von Biontech/Pfizer sei laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache ähnliche Symptome wie Covid-19.<br>2. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache gar schlimmere Symptome als Covid-19.<br>3. Der Impfstoff von Biontech/Pfizer sei laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache ähnliche Symptome als Covid-19.<br>2. Durch einen Vergleich mit den Symptomen einer Covid-19-Erkrankung entsteht der Eindruck, die Impfung von Biontech/Pfizer verursache gar schlimmere Symptome als Covid-19.<br>3. Der Impfstoff von Biontech/Pfizer sei zudem laut der U.S. Food and Drug Administration (FDA) nicht zugelassen. | 3 |

---

## Sample ID: quantemp_11
**Original Claim**: Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicates a scam by the UPA government.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicate a scam by the UPA government. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The UPA government is suspected of a scam.<br>2. The 500-rupee currency notes are suspected of being fake.<br>3. The serial numbers on the 500-rupee currency notes are suspected of being fake.<br>4. The signatures on the 500-rupee currency notes are suspected of being fake. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The RBI (Reserve Bank of India) is the central bank of India.<br>2. The UPA (United Progressive Alliance) is a political party in India.<br>3. The 500-rupee currency note is a type of Indian currency.<br>4. The serial number is a unique identifier for a currency note.<br>5. The signatures of two different RBI governors are different.<br>6. A scam is an act that is done dishonestly. | 6 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The RBI issued 500-rupee currency notes.<br>2. The RBI issued currency notes with the same serial number as the RBI.<br>3. The RBI governors signed the 500-rupee currency notes.<br>4. The UPA government issued the 500-rupee currency notes.<br>5. The UPA government issued currency notes with the same serial number as the RBI.<br>6. The UPA government issued currency notes signed by the RBI governors. | 6 |
| google/gemma-3-1b-it | 1. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicate a scam.<br>2. The currency notes are of a certain value.<br>3. The currency notes are old. | 3 |
| google/gemma-3-4b-it | 1. Old 500-rupee currency notes exist.<br>2. Those currency notes have the same serial number.<br>3. Those currency notes have the signatures of two different RBI governors.<br>4. That indicates a scam by the UPA government. | 4 |
| gpt-3.5-turbo-0125 | 1. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors were found.<br>2. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicate a scam by the UPA government. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Old 500-rupee currency notes have the same serial number.<br>2. Old 500-rupee currency notes have the signatures of two different RBI governors.<br>3. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicates a scam by the UPA government. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicate a scam by the UPA government. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Old 500-rupee currency notes having the same serial number but with the signatures of two different RBI governors indicates a scam by the UPA government. | 1 |

---

## Sample ID: quantemp_12
**Original Claim**: There are no scientific studies that prove SARS-CoV-2, which causes COVID-19, exists

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. There are no scientific studies that prove SARS-CoV-2 exists.<br>2. SARS-CoV-2 causes COVID-19. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There are no scientific studies that prove SARS-CoV-2, which causes COVID-19, exists. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. SARS-CoV-2 is a virus.<br>2. SARS-CoV-2 causes COVID-19.<br>3. There are no scientific studies that prove SARS-CoV-2 exists. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. There are no scientific studies that prove SARS-CoV-2 exists.<br>2. SARS-CoV-2 causes COVID-19.<br>3. There are no scientific studies that prove COVID-19 exists. | 3 |
| google/gemma-3-1b-it | 1. There are no scientific studies that prove SARS-CoV-2 exists. | 1 |
| google/gemma-3-4b-it | 1. There are no scientific studies that prove SARS-CoV-2 exists. | 1 |
| gpt-3.5-turbo-0125 | 1. There are no scientific studies that prove SARS-CoV-2 exists.<br>2. SARS-CoV-2 causes COVID-19. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. There are no scientific studies that prove SARS-CoV-2 exists.<br>2. SARS-CoV-2 causes COVID-19. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. There are no scientific studies that prove SARS-CoV-2 exists. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. There are no scientific studies that prove SARS-CoV-2 exists.<br>2. SARS-CoV-2 causes COVID-19. | 2 |

---

## Sample ID: quantemp_13
**Original Claim**: During the 2008 presidential campaign, VP candidate Sarah Palin said: "I can see Russia from my house."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. During the 2008 presidential campaign, VP candidate Sarah Palin said: "I can see Russia from my house." | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Sarah Palin was the Vice President during the 2008 presidential campaign.<br>2. Sarah Palin said, "I can see Russia from my house." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. During the 2008 presidential campaign, Sarah Palin said: "I can see Russia from my house."<br>2. Sarah Palin is the VP of the United States.<br>3. The United States is a country.<br>4. The United States is located in North America.<br>5. North America is a continent.<br>6. The continent of North America is home to the United States.<br>7. The United States is a republic.<br>8. The United States is a republic with a presidential system of government.<br>9. The presidential system of government is a form of government.<br>10. The presidential system of government is used in the United States.<br>11. The United States is a major world power.<br>12. The United States is a major world power with significant influence in international affairs.<br>13. The United States is a major world power with significant influence in international affairs.<br>14. The United States is a major world power with significant influence in international affairs.<br>15. The United States is a major world power with significant influence in international affairs.<br>16. The United States is a major world power with significant influence in international affairs.<br>17. The United States is a major world power with significant influence in international affairs.<br>18. The United States is a major world power with significant influence in international affairs.<br>19. The United States is a major world power with significant influence in international affairs. | 19 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Sarah Palin was the vice presidential candidate in the 2008 presidential campaign.<br>2. The 2008 presidential campaign was in the United States.<br>3. Sarah Palin said: "I can see Russia from my house" during the 2008 presidential campaign. | 3 |
| google/gemma-3-1b-it | 1. Sarah Palin stated that she could see Russia from her house during the 2008 presidential campaign. | 1 |
| google/gemma-3-4b-it | 1. During the 2008 presidential campaign, VP candidate Sarah Palin said: "I can see Russia from my house." | 1 |
| gpt-3.5-turbo-0125 | 1. VP candidate Sarah Palin said: "I can see Russia from my house." | 1 |
| gpt-4.1-mini-2025-04-14 | 1. During the 2008 presidential campaign, VP candidate Sarah Palin said: "I can see Russia from my house." | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. During the 2008 presidential campaign, VP candidate Sarah Palin said: "I can see Russia from my house." | 1 |

---

## Sample ID: quantemp_14
**Original Claim**: While Manmohan Singh was seen hiding his face at G20 summit gathering in 2011, PM Modi interacted face to face with world leaders at the recent summit

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Manmohan Singh was seen hiding his face at the G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent G20 summit. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Manmohan Singh was seen hiding his face at the G20 summit in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Manmohan Singh was seen hiding his face at the G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Manmohan Singh was seen hiding his face at the G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the G20 summit gathering in 2011. | 2 |
| google/gemma-3-1b-it | 1. Manmohan Singh was seen hiding his face at a G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at a recent summit. | 2 |
| google/gemma-3-4b-it | 1. Manmohan Singh was seen hiding his face at the G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |
| gpt-3.5-turbo-0125 | 1. Manmohan Singh was seen hiding his face at G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Manmohan Singh was seen hiding his face at G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. While Manmohan Singh was seen hiding his face at G20 summit gathering in 2011, PM Modi interacted face to face with world leaders at the recent summit. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Manmohan Singh was seen hiding his face at G20 summit gathering in 2011.<br>2. PM Modi interacted face to face with world leaders at the recent summit. | 2 |

---

## Sample ID: quantemp_15
**Original Claim**: This video of two people trying to save a deer which has its face completely frozen is from the recent blizzard in the United States.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This video is of two people trying to save a deer.<br>2. The deer in the video has its face completely frozen.<br>3. The video is from the recent blizzard in the United States. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. This video is from the recent blizzard in the United States.<br>2. Two people are trying to save a deer in the video. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The video is from the recent blizzard in the United States.<br>2. It is from a video of two people trying to save a deer.<br>3. The deer is from the recent blizzard in the United States. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. This video is of two people trying to save a deer.<br>2. The deer has its face completely frozen.<br>3. The video is from the recent blizzard in the United States. | 3 |
| google/gemma-3-1b-it | 1. This video depicts a deer with its face frozen during a recent blizzard in the United States. | 1 |
| google/gemma-3-4b-it | 1. This video of two people trying to save a deer which has its face completely frozen is from the recent blizzard in the United States. | 1 |
| gpt-3.5-turbo-0125 | 1. The video is of two people trying to save a deer.<br>2. The deer has its face completely frozen.<br>3. The recent blizzard in the United States is the context of the video. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. This video of two people trying to save a deer which has its face completely frozen is from the recent blizzard in the United States. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. This video of two people trying to save a deer which has its face completely frozen is from the recent blizzard in the United States. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The video is from the recent blizzard in the United States.<br>2. The video shows two people trying to save a deer.<br>3. The deer has its face completely frozen. | 3 |

---

## Sample ID: quantemp_16
**Original Claim**: Says Jeff Wentworth, bending the rules, "has used $211,743.96 in campaign contributions to lease luxury cars."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Jeff Wentworth says bending the rules has used $211,743.96 in campaign contributions to lease luxury cars. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Jeff Wentworth has used $211,743.96 in campaign contributions to lease luxury cars.<br>2. Jeff Wentworth has used $211,743.96 in campaign contributions. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Jeff Wentworth is a person.<br>2. Bending the rules is a campaign contribution.<br>3. $211,743.96 is the amount of money used in campaign contributions. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Jeff Wentworth has used $211,743.96 in campaign contributions to lease luxury cars. | 1 |
| google/gemma-3-1b-it | 1. Jeff Wentworth has used $211,743.96 in campaign contributions to lease luxury cars.<br>2. The amount of campaign contributions is $211,743.96.<br>3. The amount of campaign contributions is used to lease luxury cars. | 3 |
| google/gemma-3-4b-it | 1. Jeff Wentworth says bending the rules.<br>2. $211,743.96 in campaign contributions has been used by Jeff Wentworth.<br>3. Jeff Wentworth has used $211,743.96 in campaign contributions to lease luxury cars. | 3 |
| gpt-3.5-turbo-0125 | 1. Jeff Wentworth has used $211,743.96 in campaign contributions to lease luxury cars. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Jeff Wentworth says bending the rules has used $211,743.96 in campaign contributions to lease luxury cars. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Jeff Wentworth says that bending the rules has used $211,743.96 in campaign contributions to lease luxury cars. | 1 |

---

## Sample ID: quantemp_17
**Original Claim**: Says, "In the last four years we’ve cut $36 million in ongoing revenue."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In the last four years, ongoing revenue was cut by $36 million. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "In the last four years, the company has cut $36 million in ongoing revenue." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In the last four years, the company cut $36 million in ongoing revenue.<br>2. The company cut $36 million in ongoing revenue.<br>3. The company cut $36 million in ongoing revenue. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The speaker says, "In the last four years we've cut $36 million in ongoing revenue." | 1 |
| google/gemma-3-1b-it | 1. “In the last four years” refers to the period from 2020 to 2024.<br>2. “We’ve cut $36 million” refers to the action of cutting $36 million.<br>3. “Ongoing revenue” refers to the revenue generated over the past four years. | 3 |
| google/gemma-3-4b-it | 1. Says, "In the last four years we’ve cut $36 million in ongoing revenue." | 1 |
| gpt-3.5-turbo-0125 | 1. In the last four years $36 million in ongoing revenue was cut. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. In the last four years, we have cut $36 million in ongoing revenue. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "In the last four years we’ve cut $36 million in ongoing revenue." | 1 |

---

## Sample ID: quantemp_18
**Original Claim**: This video shows Indians trying to block China’s border construction in June 2020

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This video shows Indians trying to block China’s border construction in June 2020. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. This video shows Indians trying to block China’s border construction.<br>2. The video was taken in June 2020. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. This video shows Indians trying to block China's border construction in June 2020.<br>2. The video shows Indians trying to block China's border construction in June 2020.<br>3. The video shows Indians trying to block China's border construction in June 2020. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. This video shows Indians.<br>2. This video is about China's border construction.<br>3. This video was released in June 2020. | 3 |
| google/gemma-3-1b-it | 1. This video shows Indians attempting to block China’s border construction in June 2020. | 1 |
| google/gemma-3-4b-it | 1. This video shows Indians.<br>2. This video shows China’s border construction.<br>3. The border construction occurred in June 2020.<br>4. The Indians are attempting to block the border construction. | 4 |
| gpt-3.5-turbo-0125 | 1. The video shows Indians trying to block China’s border construction in June 2020. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. This video shows Indians trying to block China’s border construction in June 2020. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The video shows Indians trying to block China’s border construction in June 2020. | 1 |

---

## Sample ID: quantemp_19
**Original Claim**: "Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Creating 25 jobs in Umatilla County has the same impact as creating 500 jobs in the metro region. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Umatilla County<br>2. 25 jobs<br>3. 500 jobs<br>4. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| google/gemma-3-1b-it | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| google/gemma-3-4b-it | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| gpt-3.5-turbo-0125 | 1. 25 jobs were created in Umatilla County.<br>2. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Creating 25 jobs in Umatilla County has the same impact as 500 jobs in the metro region. | 1 |

---

## Sample ID: quantemp_20
**Original Claim**: Graphic shows ABP News questioned Conress for Chandrayaan-2 setback

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Graphic shows ABP News questioned Congress for Chandrayaan-2 setback | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. ABP News questioned Congress for Chandrayaan-2 setback. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Graphic shows the question asked by ABP News to Congress regarding Chandrayaan-2 setback.<br>2. ABP News questioned Congress for Chandrayaan-2 setback.<br>3. ABP News asked Congress for Chandrayaan-2 setback.<br>4. ABP News asked Congress for Chandrayaan-2 setback.<br>5. ABP News asked Congress for Chandrayaan-2 setback.<br>6. ABP News asked Congress for Chandrayaan-2 setback.<br>7. ABP News asked Congress for Chandrayaan-2 setback.<br>8. ABP News asked Congress for Chandrayaan-2 setback.<br>9. ABP News asked Congress for Chandrayaan-2 setback.<br>10. ABP News asked Congress for Chandrayaan-2 setback.<br>11. ABP News asked Congress for Chandrayaan-2 setback.<br>12. ABP News asked Congress for Chandrayaan-2 setback.<br>13. ABP News asked Congress for Chandrayaan-2 setback.<br>14. ABP News asked Congress for Chandrayaan-2 setback.<br>15. ABP News asked Congress for Chandrayaan-2 setback.<br>16. ABP News asked Congress for Chandrayaan-2 setback.<br>17. ABP News asked Congress for Chandrayaan-2 setback.<br>18. ABP News asked Congress for Chandrayaan-2 | 18 |
| meta-llama/Llama-3.2-3B-Instruct | 1. ABP News questioned Congress about Chandrayaan-2.<br>2. Chandrayaan-2 was a setback. | 2 |
| google/gemma-3-1b-it | 1. Graphic shows ABP News questioned Chandrayaan-2 setback.<br>2. ABP News was questioned by Chandrayaan-2.<br>3. Chandrayaan-2 setback is a setback. | 3 |
| google/gemma-3-4b-it | 1. Graphic shows ABP News questioned Congress.<br>2. ABP News questioned Congress for Chandrayaan-2 setback. | 2 |
| gpt-3.5-turbo-0125 | 1. ABP News questioned Congress for Chandrayaan-2 setback. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. ABP News questioned Conress for Chandrayaan-2 setback. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Graphic shows ABP News questioned Conress for Chandrayaan-2 setback. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Graphic shows ABP News questioned Conress for Chandrayaan-2 setback. | 1 |

---

## Sample ID: quantemp_21
**Original Claim**: California "cut about $1.3 billion in child care (during the recession). We’ve only reinvested about $300 million."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. California cut about $1.3 billion in child care during the recession.<br>2. California reinvested about $300 million in child care. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. California cut about $1.3 billion in child care during the recession.<br>2. California has only reinvested about $300 million. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. California cut about $1.3 billion in child care during the recession.<br>2. We’ve only reinvested about $300 million in child care. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. California cut about $1.3 billion in child care during the recession.<br>2. California cut about $300 million in child care. | 2 |
| google/gemma-3-1b-it | 1. California cut approximately $1.3 billion in child care during the recession.<br>2. We’ve only reinvested about $300 million in child care. | 2 |
| google/gemma-3-4b-it | 1. California cut about $1.3 billion in child care during the recession.<br>2. We’ve only reinvested about $300 million. | 2 |
| gpt-3.5-turbo-0125 | 1. California cut about $1.3 billion in child care during the recession.<br>2. California has only reinvested about $300 million in child care. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. California cut about $1.3 billion in child care during the recession.<br>2. California has only reinvested about $300 million in child care. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. California cut about $1.3 billion in child care (during the recession).<br>2. California has only reinvested about $300 million. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. California cut about $1.3 billion in child care during the recession.<br>2. California has only reinvested about $300 million. | 2 |

---

## Sample ID: quantemp_22
**Original Claim**: Says "92 percent of the people agree on DACA."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 92 percent of the people agree on DACA. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "92 percent of the people agree on DACA" is a statement. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States Congress passed the Deferred Action for Childhood Arrivals (DACA) Act in 2012.<br>2. DACA was signed into law by President Barack Obama.<br>3. The DACA Act was enacted on June 15, 2012.<br>4. The DACA Act was signed into law by President Barack Obama.<br>5. The DACA Act was signed into law by President Barack Obama.<br>6. The DACA Act was signed into law by President Barack Obama.<br>7. The DACA Act was signed into law by President Barack Obama.<br>8. The DACA Act was signed into law by President Barack Obama.<br>9. The DACA Act was signed into law by President Barack Obama.<br>10. The DACA Act was signed into law by President Barack Obama.<br>11. The DACA Act was signed into law by President Barack Obama.<br>12. The DACA Act was signed into law by President Barack Obama.<br>13. The DACA Act was signed into law by President Barack Obama.<br>14. The DACA Act was signed into law by President Barack Obama.<br>15. The DACA Act was signed into law by President Barack Obama.<br>16. The DACA Act was signed into law by President Barack Obama.<br>17. The DACA Act was signed into law by President Barack Obama.<br>18. The DACA Act was signed into law by President Barack Obama.<br>19. The DACA Act was signed into law by President Barack Obama | 19 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The people agree on 92 percent of DACA. | 1 |
| google/gemma-3-1b-it | 1. “92 percent of the people” refers to the people who agree on DACA.<br>2. DACA is a program that provides temporary protection from deportation to certain immigrants. | 2 |
| google/gemma-3-4b-it | 1. “92 percent of the people agree on DACA.” | 1 |
| gpt-3.5-turbo-0125 | 1. 92 percent of the people agree on DACA. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 92 percent of the people agree on DACA. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "92 percent of the people agree on DACA." | 1 |

---

## Sample ID: quantemp_23
**Original Claim**: Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Rahul Gandhi made a promise to farmers' loan waiver.<br>2. 24 hours after the election results, Rahul Gandhi went back on his promise to farmers' loan waiver. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results.<br>2. Rahul Gandhi was elected to the Lok Sabha.<br>3. Rahul Gandhi was elected to the Lok Sabha 24 hours after election results. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Rahul Gandhi went back on the farmers' loan waiver promise 24 hours after the election results. | 1 |
| google/gemma-3-1b-it | 1. Rahul Gandhi made a promise to waive farmers’ loans.<br>2. Rahul Gandhi went back on the promise 24 hours after election results.<br>3. The promise of farmers’ loan waiver was revoked. | 3 |
| google/gemma-3-4b-it | 1. Rahul Gandhi goes back on farmers’ loan waiver promise.<br>2. The going back on farmers’ loan waiver promise occurred 24 hours after election results. | 2 |
| gpt-3.5-turbo-0125 | 1. Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Rahul Gandhi went back on farmers' loan waiver promise 24 hours after election results. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Rahul Gandhi goes back on farmers' loan waiver promise 24 hours after election results. | 1 |

---

## Sample ID: quantemp_24
**Original Claim**: 40 percent of illegal immigrants "had a visa and then became illegal," mostly because "they changed jobs."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 40 percent of illegal immigrants had a visa and then became illegal.<br>2. 40 percent of illegal immigrants became illegal mostly because they changed jobs. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 40 percent of illegal immigrants "had a visa and then became illegal."<br>2. They changed jobs. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 40 percent of illegal immigrants had a visa and then became illegal.<br>2. They changed jobs. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. 40 percent of illegal immigrants had a visa.<br>2. Illegal immigrants had a visa.<br>3. They changed jobs.<br>4. They were illegal immigrants. | 4 |
| google/gemma-3-1b-it | 1. 40 percent of illegal immigrants “had a visa”<br>2. Became illegal “because” they changed jobs. | 2 |
| google/gemma-3-4b-it | 1. 40 percent of illegal immigrants had a visa.<br>2. The illegal immigrants "changed jobs." | 2 |
| gpt-3.5-turbo-0125 | 1. 40 percent of illegal immigrants had a visa and then became illegal.<br>2. Mostly because they changed jobs. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. 40 percent of illegal immigrants had a visa and then became illegal.<br>2. 40 percent of illegal immigrants became illegal mostly because they changed jobs. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. 40 percent of illegal immigrants had a visa and then became illegal.<br>2. 40 percent of illegal immigrants became illegal mostly because they changed jobs. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. 40 percent of illegal immigrants "had a visa and then became illegal."<br>2. 40 percent of illegal immigrants became illegal mostly because "they changed jobs." | 2 |

---

## Sample ID: quantemp_25
**Original Claim**: A 2022 photograph shows a crowded train station as thousands of Ukrainians attempted to flee after Russia's invasion of the country.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A 2022 photograph shows a crowded train station.<br>2. A 2022 photograph shows thousands of Ukrainians.<br>3. A 2022 photograph shows thousands of Ukrainians attempting to flee.<br>4. A 2022 photograph shows thousands of Ukrainians attempting to flee after Russia's invasion of the country. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photograph was taken in 2022.<br>2. The photograph shows a crowded train station.<br>3. Thousands of Ukrainians attempted to flee after Russia's invasion of the country. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Ukraine<br>2. Russia<br>3. Russia's invasion of Ukraine<br>4. 2022<br>5. Thousands of Ukrainians<br>6. Flew | 6 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A photograph taken in 2022 shows a crowded train station.<br>2. The train station is in Ukraine.<br>3. Thousands of people attempted to flee after Russia's invasion of Ukraine in 2022. | 3 |
| google/gemma-3-1b-it | 1. A crowded train station was photographed in Russia.<br>2. Thousands of Ukrainians attempted to flee after Russia’s invasion of the country. | 2 |
| google/gemma-3-4b-it | 1. A 2022 photograph shows a crowded train station.<br>2. Thousands of Ukrainians attempted to flee after Russia’s invasion of the country.<br>3. Russia’s invasion occurred in 2022. | 3 |
| gpt-3.5-turbo-0125 | 1. The photograph was taken in 2022.<br>2. The photograph shows a crowded train station.<br>3. Thousands of Ukrainians attempted to flee after Russia's invasion of the country. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. A 2022 photograph shows a crowded train station.<br>2. Thousands of Ukrainians attempted to flee after Russia's invasion of the country. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A 2022 photograph shows a crowded train station.<br>2. Thousands of Ukrainians attempted to flee after Russia's invasion of the country. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A 2022 photograph shows a crowded train station.<br>2. Thousands of Ukrainians attempted to flee after Russia's invasion of the country. | 2 |

---

## Sample ID: quantemp_26
**Original Claim**: About 400 mosques and madrasas have been identified in Rampur which were operating without electricity connection

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. About 400 mosques and madrasas in Rampur were operating without electricity connection. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. These mosques and madrasas were operating without electricity connection. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Rampur is a city in India.<br>2. About 400 mosques and madrasas have been identified in Rampur.<br>3. Rampur is a city in India.<br>4. About 400 mosques and madrasas were operating in Rampur. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. The mosques and madrasas in Rampur were operating without electricity connection. | 2 |
| google/gemma-3-1b-it | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. The number of mosques and madrasas in Rampur has been identified.<br>3. The number of mosques and madrasas in Rampur has been identified.<br>4. The number of mosques and madrasas in Rampur has been identified. | 4 |
| google/gemma-3-4b-it | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. These mosques and madrasas were operating without electricity connection. | 2 |
| gpt-3.5-turbo-0125 | 1. 400 mosques and madrasas have been identified in Rampur.<br>2. The 400 mosques and madrasas were operating without electricity connection in Rampur. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. About 400 mosques have been identified in Rampur which were operating without electricity connection.<br>2. About 400 madrasas have been identified in Rampur which were operating without electricity connection. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. About 400 mosques and madrasas in Rampur were operating without electricity connection. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. About 400 mosques and madrasas have been identified in Rampur.<br>2. About 400 mosques and madrasas in Rampur were operating without electricity connection. | 2 |

---

## Sample ID: quantemp_27
**Original Claim**: Government officials, law enforcement, billionaires, or antifa groups nefariously placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Government officials placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>2. Law enforcement placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>3. Billionaires placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>4. Antifa groups placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Government officials, law enforcement, billionaires, or antifa groups nefariously placed pallets of bricks at protest sites in U.S. cities.<br>2. Stoking violence during June 2020 demonstrations against police brutality was the goal of the nefariously placed pallets of bricks. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Government officials<br>2. Law enforcement<br>3. Billionaires<br>4. Antifa groups<br>5. Pallets of bricks<br>6. U.S. cities<br>7. June 2020 | 7 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Government officials, law enforcement, billionaires, or antifa groups placed pallets of bricks at protest sites in U.S. cities.<br>2. Government officials, law enforcement, billionaires, or antifa groups placed pallets of bricks at protest sites in U.S. cities in June 2020.<br>3. Government officials, law enforcement, billionaires, or antifa groups placed pallets of bricks at protest sites in U.S. cities. | 3 |
| google/gemma-3-1b-it | 1. Government officials, law enforcement, billionaires, or antifa groups were nefariously placed pallets of bricks at protest sites in U.S. cities.<br>2. During June 2020 demonstrations against police brutality, pallets of bricks were placed at protest sites in U.S. cities. | 2 |
| google/gemma-3-4b-it | 1. Government officials placed pallets of bricks at protest sites in U.S. cities.<br>2. Law enforcement placed pallets of bricks at protest sites in U.S. cities.<br>3. Billionaires placed pallets of bricks at protest sites in U.S. cities.<br>4. Antifa groups placed pallets of bricks at protest sites in U.S. cities.<br>5. The placement of pallets of bricks occurred during June 2020 demonstrations.<br>6. The demonstrations occurred against police brutality.<br>7. The demonstrations occurred in U.S. cities. | 7 |
| gpt-3.5-turbo-0125 | 1. Government officials nefariously placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>2. Law enforcement nefariously placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>3. Billionaires nefariously placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>4. Antifa groups nefariously placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Government officials placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality to stoke violence.<br>2. Law enforcement placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality to stoke violence.<br>3. Billionaires placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality to stoke violence.<br>4. Antifa groups placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality to stoke violence. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Government officials placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>2. Law enforcement placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>3. Billionaires placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>4. Antifa groups placed pallets of bricks at protest sites in U.S. cities during June 2020 demonstrations against police brutality.<br>5. Government officials, law enforcement, billionaires, or antifa groups placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality. | 5 |
| gpt-5.4-mini-2026-03-17 | 1. Government officials nefariously placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality.<br>2. Law enforcement nefariously placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality.<br>3. Billionaires nefariously placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality.<br>4. Antifa groups nefariously placed pallets of bricks at protest sites in U.S. cities to stoke violence during June 2020 demonstrations against police brutality. | 4 |

---

## Sample ID: quantemp_28
**Original Claim**: "It has been estimated that nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. It has been estimated that nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers.<br>2. Nearly 40 percent of all guns sold in America are sold online.<br>3. Nearly 40 percent of all guns sold in America are sold at gun shows.<br>4. Private, unlicensed sellers sell nearly 40 percent of all guns sold in America. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. It has been estimated that nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows.<br>2. Private, unlicensed sellers either online or through gun shows are estimated to sell nearly 40 percent of all guns sold in America. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The guns sold in America are primarily sold by private, unlicensed sellers either online or through gun shows.<br>2. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 2 |
| google/gemma-3-1b-it | 1. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers.<br>2. Approximately 40 percent of all guns sold in America are sold by private, unlicensed sellers. | 2 |
| google/gemma-3-4b-it | 1. It has been estimated that nearly 40 percent of all guns sold in America are sold.<br>2. The guns sold are sold by private, unlicensed sellers.<br>3. The private, unlicensed sellers sell guns either online.<br>4. The private, unlicensed sellers sell guns through gun shows. | 4 |
| gpt-3.5-turbo-0125 | 1. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. It has been estimated that nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Nearly 40 percent of all guns sold in America are sold by private, unlicensed sellers either online or through gun shows. | 1 |

---

## Sample ID: quantemp_29
**Original Claim**: A 2013 study found that coconut oil kills 93 percent of colon cancer cells.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells.<br>2. Coconut oil is a 2013 study.<br>3. Coconut oil is a 2013 study.<br>4. Coconut oil is a 2013 study. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| google/gemma-3-1b-it | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| google/gemma-3-4b-it | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| gpt-3.5-turbo-0125 | 1. The study was conducted in 2013.<br>2. The study found that coconut oil kills 93 percent of colon cancer cells. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A 2013 study found that coconut oil kills 93 percent of colon cancer cells. | 1 |

---

## Sample ID: quantemp_30
**Original Claim**: An Illinois couple who received five vote-by-mail applications can vote five times.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An Illinois couple received five vote-by-mail applications.<br>2. The Illinois couple can vote five times. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An Illinois couple can receive five vote-by-mail applications.<br>2. The couple can use these applications to vote five times. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. An Illinois couple who received five vote-by-mail applications can vote five times.<br>2. The couple who received five vote-by-mail applications in Illinois received five applications.<br>3. The couple who received five vote-by-mail applications in Illinois received five applications.<br>4. The couple who received five vote-by-mail applications in Illinois received five applications. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An Illinois couple voted five times.<br>2. The couple received five vote-by-mail applications.<br>3. The couple is an Illinois couple.<br>4. The couple is referred to as "an Illinois couple". | 4 |
| google/gemma-3-1b-it | 1. A couple received five vote-by-mail applications in Illinois.<br>2. Five vote-by-mail applications can be voted on. | 2 |
| google/gemma-3-4b-it | 1. An Illinois couple received five vote-by-mail applications.<br>2. The Illinois couple can vote five times. | 2 |
| gpt-3.5-turbo-0125 | 1. An Illinois couple received five vote-by-mail applications.<br>2. The Illinois couple can vote five times. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. An Illinois couple received five vote-by-mail applications.<br>2. An Illinois couple who received five vote-by-mail applications can vote five times. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. An Illinois couple who received five vote-by-mail applications can vote five times. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. An Illinois couple received five vote-by-mail applications.<br>2. An Illinois couple can vote five times. | 2 |

---

## Sample ID: quantemp_31
**Original Claim**: Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have jumped over 250 percent.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Florida passed the "stand your ground" law in 2005.<br>2. Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have increased by over 250 percent. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Florida passed the "stand your ground" law in 2005.<br>2. Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have jumped over 250 percent. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Florida passed the "stand your ground" law in 2005.<br>2. Deaths due to self-defense have jumped over 250 percent since Florida passed the "stand your ground" law in 2005. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Florida passed the "stand your ground" law in 2005.<br>2. Deaths due to self-defense have jumped over 250 percent since Florida passed the "stand your ground" law in 2005. | 2 |
| google/gemma-3-1b-it | 1. Florida passed the “stand your ground” law in 2005.<br>2. Deaths due to self-defense have jumped over 250 percent since 2005. | 2 |
| google/gemma-3-4b-it | 1. Florida passed the "stand your ground" law in 2005.<br>2. Deaths due to self-defense have jumped over 250 percent since Florida passed the "stand your ground" law in 2005. | 2 |
| gpt-3.5-turbo-0125 | 1. Florida passed the "stand your ground" law in 2005.<br>2. Deaths due to self-defense have jumped over 250 percent since Florida passed the "stand your ground" law in 2005. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Florida passed the "stand your ground" law in 2005.<br>2. Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have jumped over 250 percent. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have jumped over 250 percent. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Florida passed the "stand your ground" law in 2005.<br>2. Since Florida passed the "stand your ground" law in 2005, deaths due to self-defense have jumped over 250 percent. | 2 |

---

## Sample ID: quantemp_32
**Original Claim**: Says "74 percent of small-business people believe that Obamacare is a bad idea."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 74 percent of small-business people believe that Obamacare is a bad idea. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 74 percent of small-business people believe that Obamacare is a bad idea. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 74 percent of small-business people believe that Obamacare is a bad idea.<br>2. The United States Senate voted to repeal the Affordable Care Act (ACA) in 2017.<br>3. The ACA was signed into law by President Barack Obama.<br>4. The ACA was enacted in 2010.<br>5. The ACA was signed into law by President Barack Obama.<br>6. The ACA was enacted in 2010.<br>7. The ACA was signed into law by President Barack Obama.<br>8. The ACA was enacted in 2010.<br>9. The ACA was signed into law by President Barack Obama.<br>10. The ACA was enacted in 2010.<br>11. The ACA was signed into law by President Barack Obama.<br>12. The ACA was enacted in 2010.<br>13. The ACA was signed into law by President Barack Obama.<br>14. The ACA was enacted in 2010.<br>15. The ACA was signed into law by President Barack Obama.<br>16. The ACA was enacted in 2010.<br>17. The ACA was signed into law by President Barack Obama.<br>18. The ACA was enacted in 2010.<br>19. The ACA was signed into law by President Barack Obama.<br>20. The ACA was enacted in 2010.<br>21. The ACA was signed into law by President Barack Obama.<br>22. The ACA was enacted in 2010. | 22 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The phrase "74 percent of small-business people" refers to "people who own small businesses".<br>2. The phrase "believe that Obamacare is a bad idea" refers to "Obamacare".<br>3. Obamacare is a health insurance reform law passed in 2010. | 3 |
| google/gemma-3-1b-it | 1. “74 percent” of small-business people believe that Obamacare is a bad idea. | 1 |
| google/gemma-3-4b-it | 1. “74 percent of small-business people believe that Obamacare is a bad idea.” | 1 |
| gpt-3.5-turbo-0125 | 1. 74 percent of small-business people believe that Obamacare is a bad idea. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 74 percent of small-business people believe that Obamacare is a bad idea. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "74 percent of small-business people believe that Obamacare is a bad idea." | 1 |

---

## Sample ID: quantemp_33
**Original Claim**: Canadians can be fined $1,000 for eating while driving.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Canadians can be fined $1,000 for eating while driving.<br>2. Eating while driving is illegal in Canada.<br>3. Canadians can be fined $1,000 for eating while driving in Canada. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| google/gemma-3-1b-it | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| google/gemma-3-4b-it | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| gpt-3.5-turbo-0125 | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Canadians can be fined $1,000 for eating while driving. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Canadians can be fined $1,000 for eating while driving. | 1 |

---

## Sample ID: quantemp_34
**Original Claim**: In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us"; and "I shall not avoid person or place but will go freely."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us".<br>2. In 1527, Martin Luther wrote of the Black Death: "I shall not avoid person or place but will go freely". | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Martin Luther wrote of the Black Death in 1527.<br>2. Martin Luther wrote "I shall ask God to mercifully protect us" in 1527.<br>3. Martin Luther wrote "I shall not avoid person or place but will go freely" in 1527. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Martin Luther wrote of the Black Death.<br>2. Martin Luther wrote of the Black Death in 1527.<br>3. Martin Luther wrote "I shall ask God to mercifully protect us" in 1527.<br>4. Martin Luther wrote "I shall ask God to mercifully protect us" in 1527. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Martin Luther wrote of the Black Death in 1527: "I shall ask God to mercifully protect us".<br>2. Martin Luther wrote of the Black Death in 1527: "I shall not avoid person or place but will go freely". | 2 |
| google/gemma-3-1b-it | 1. Martin Luther wrote of the Black Death in 1527.<br>2. The Black Death occurred in 1527.<br>3. God was asked to mercifully protect us.<br>4. God was asked to not avoid person or place.<br>5. God was asked to go freely. | 5 |
| google/gemma-3-4b-it | 1. In 1527, Martin Luther wrote of the Black Death.<br>2. Martin Luther wrote “I shall ask God to mercifully protect us” in 1527.<br>3. Martin Luther wrote “I shall not avoid person or place but will go freely” in 1527. | 3 |
| gpt-3.5-turbo-0125 | 1. In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us".<br>2. In 1527, Martin Luther wrote of the Black Death: "I shall not avoid person or place but will go freely". | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us."<br>2. In 1527, Martin Luther wrote of the Black Death: "I shall not avoid person or place but will go freely." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us".<br>2. In 1527, Martin Luther wrote of the Black Death: "I shall not avoid person or place but will go freely". | 2 |
| gpt-5.4-mini-2026-03-17 | 1. In 1527, Martin Luther wrote of the Black Death: "I shall ask God to mercifully protect us".<br>2. In 1527, Martin Luther wrote of the Black Death: "I shall not avoid person or place but will go freely". | 2 |

---

## Sample ID: quantemp_35
**Original Claim**: Many advocates of reproductive rights say bans do not prevent the procedure but instead can lead to life-threatening abortions "The abortion ban does not stop abortion" aTikTokuser says (archived claimhere) "It just stops safe abortions"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. The abortion ban does not stop abortion.<br>3. The abortion ban just stops safe abortions. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. Bans can lead to life-threatening abortions.<br>3. The abortion ban does not stop abortion.<br>4. The abortion ban just stops safe abortions. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Many advocates of reproductive rights say bans do not prevent the procedure but instead can lead to life-threatening abortions.<br>2. The abortion ban does not stop abortion.<br>3. The abortion ban does not stop safe abortions. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Many advocates of reproductive rights say that the abortion ban does not stop abortion.<br>2. The abortion ban does not stop safe abortions.<br>3. A TikTok user says that the abortion ban does not stop abortion.<br>4. A TikTok user says that the abortion ban stops safe abortions. | 4 |
| google/gemma-3-1b-it | 1. Bans do not prevent the procedure.<br>2. The abortion ban does not stop abortion.<br>3. A TikTokuser states that the abortion ban does not prevent safe abortions. | 3 |
| google/gemma-3-4b-it | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. TikTokuser says (archived claim here) "The abortion ban does not stop abortion."<br>3. TikTokuser says (archived claim here) "It just stops safe abortions." | 3 |
| gpt-3.5-turbo-0125 | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. Many advocates of reproductive rights say bans can lead to life-threatening abortions.<br>3. "The abortion ban does not stop abortion" aTikTokuser says.<br>4. "The abortion ban just stops safe abortions" aTikTokuser says. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. Many advocates of reproductive rights say bans can lead to life-threatening abortions.<br>3. A TikTok user says "The abortion ban does not stop abortion."<br>4. A TikTok user says "The abortion ban just stops safe abortions." | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. Many advocates of reproductive rights say bans can lead to life-threatening abortions.<br>3. “The abortion ban does not stop abortion” aTikTokuser says (archived claimhere).<br>4. “It just stops safe abortions” aTikTokuser says (archived claimhere). | 4 |
| gpt-5.4-mini-2026-03-17 | 1. Many advocates of reproductive rights say bans do not prevent the procedure.<br>2. Many advocates of reproductive rights say bans can lead to life-threatening abortions.<br>3. "The abortion ban does not stop abortion" aTikTokuser says.<br>4. "It just stops safe abortions" aTikTokuser says. | 4 |

---

## Sample ID: quantemp_36
**Original Claim**: "When a car is sent to the United States from China, there is a Tariff to be paid of 2 1/2%. When a car is sent to China from the United States, there is a Tariff to be paid of 25%."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2 1/2%.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25%. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2.5%.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25%. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States is a country.<br>2. A car is a vehicle.<br>3. A vehicle is sent to the United States from China.<br>4. A car is sent from China to the United States.<br>5. A Tariff is a tax on imported goods.<br>6. A Tariff is paid when a car is sent to the United States from China.<br>7. A Tariff is paid when a car is sent from China to the United States. | 7 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A car sent to the United States from China incurs a Tariff of 2 1/2%.<br>2. A car sent to China from the United States incurs a Tariff of 25%. | 2 |
| google/gemma-3-1b-it | 1. A Tariff to be paid of 2.5% is charged when a car is sent to the United States from China.<br>2. A Tariff to be paid of 25% is charged when a car is sent to China from the United States. | 2 |
| google/gemma-3-4b-it | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2 and a half percent.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25 percent. | 2 |
| gpt-3.5-turbo-0125 | 1. A car sent to the United States from China incurs a Tariff of 2 1/2%.<br>2. A car sent to China from the United States incurs a Tariff of 25%. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2 1/2%.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25%. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2 1/2%.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25%. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. When a car is sent to the United States from China, there is a Tariff to be paid of 2 1/2%.<br>2. When a car is sent to China from the United States, there is a Tariff to be paid of 25%. | 2 |

---

## Sample ID: quantemp_37
**Original Claim**: "More than 70 percent of American adults have committed a crime that could lead to imprisonment."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. More than 70 percent of American adults have committed a crime.<br>2. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment.<br>2. More than 70 percent of American adults have committed a crime that could lead to imprisonment.<br>3. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| google/gemma-3-1b-it | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| google/gemma-3-4b-it | 1. More than 70 percent of American adults have committed a crime.<br>2. That crime could lead to imprisonment. | 2 |
| gpt-3.5-turbo-0125 | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. More than 70 percent of American adults have committed a crime that could lead to imprisonment. | 1 |

---

## Sample ID: quantemp_38
**Original Claim**: Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks, three of which are being sold for Rs 999.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks.<br>2. Three face masks are being sold by Khadi India for Rs 999. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi.<br>2. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks.<br>3. Three face masks are being sold for Rs 999. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Khadi India replaced Mahatma Gandhi's picture with that of PM Modi in its advertisement for face masks.<br>2. Three of the face masks being sold for Rs 999 are being produced in India.<br>3. Khadi India is a brand of face masks. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Khadi India has replaced the picture of Mahatma Gandhi with the picture of PM Modi in its advertisement for face masks.<br>2. Khadi India is selling three face masks with the picture of PM Modi.<br>3. The face masks being sold by Khadi India have the picture of PM Modi.<br>4. The advertisement for face masks by Khadi India features the picture of PM Modi. | 4 |
| google/gemma-3-1b-it | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi.<br>2. Three of the advertisements are being sold for Rs 999. | 2 |
| google/gemma-3-4b-it | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi.<br>2. This replacement is in advertisements for face masks.<br>3. Three of these face masks are being sold for Rs 999. | 3 |
| gpt-3.5-turbo-0125 | 1. Khadi India has replaced Mahatma Gandhi’s picture with PM Modi's picture in its advertisement for face masks.<br>2. Three face masks are being sold for Rs 999 in the advertisement. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks.<br>2. Three face masks are being sold for Rs 999 in the advertisement by Khadi India. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks.<br>2. Three face masks are being sold for Rs 999 in Khadi India’s advertisement. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Khadi India has replaced Mahatma Gandhi’s picture with that of PM Modi in its advertisement for face masks.<br>2. Three face masks are being sold for Rs 999. | 2 |

---

## Sample ID: quantemp_39
**Original Claim**: A photograph shows President Obama posing next to a 69 or 420 mile marker.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photograph shows President Obama posing next to a 69 or 420 mile marker. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photograph shows President Obama posing.<br>2. President Obama is next to a 69 or 420 mile marker. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The photograph shows President Obama posing next to a 69 or 420 mile marker.<br>2. The photograph shows President Obama posing next to a 69 or 420 mile marker.<br>3. The photograph shows President Obama posing next to a 69 or 420 mile marker. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A photograph shows President Obama posing next to a 69 mile marker.<br>2. A photograph shows President Obama posing next to a 420 mile marker. | 2 |
| google/gemma-3-1b-it | 1. A photograph shows President Obama posing next to a 69 mile marker. | 1 |
| google/gemma-3-4b-it | 1. A photograph shows President Obama.<br>2. The photograph shows President Obama posing next to a 69 mile marker.<br>3. The photograph shows President Obama posing next to a 420 mile marker. | 3 |
| gpt-3.5-turbo-0125 | 1. The photograph shows President Obama posing next to a 69 mile marker.<br>2. The photograph shows President Obama posing next to a 420 mile marker. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A photograph shows President Obama posing next to a 69 mile marker.<br>2. A photograph shows President Obama posing next to a 420 mile marker. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Please provide the claim text to break down into atomic facts. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A photograph shows President Obama posing next to a 69 or 420 mile marker. | 1 |

---

## Sample ID: quantemp_40
**Original Claim**: An 8-year-old Yemeni girl was forced to marry a 40-year-old man and then died of vaginal injuries on their wedding night.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The 8-year-old Yemeni girl died of vaginal injuries on their wedding night. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The girl died of vaginal injuries on their wedding night. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I can't fulfill this request | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The 8-year-old Yemeni girl died of vaginal injuries on their wedding night. | 2 |
| google/gemma-3-1b-it | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The girl died of vaginal injuries.<br>3. The wedding night was a death event. | 3 |
| google/gemma-3-4b-it | 1. An 8-year-old girl was forced to marry a 40-year-old man.<br>2. The girl died of vaginal injuries.<br>3. The injuries occurred on their wedding night.<br>4. The girl was from Yemen. | 4 |
| gpt-3.5-turbo-0125 | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. An 8-year-old Yemeni girl died of vaginal injuries on her wedding night. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The 8-year-old Yemeni girl died of vaginal injuries on their wedding night. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. The 8-year-old Yemeni girl died of vaginal injuries on their wedding night. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. An 8-year-old Yemeni girl was forced to marry a 40-year-old man.<br>2. An 8-year-old Yemeni girl died of vaginal injuries on their wedding night. | 2 |

---

## Sample ID: quantemp_41
**Original Claim**: This photo shows four female ministers of the recently formed government of Finland

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This photo shows four female ministers.<br>2. This photo shows ministers of the government of Finland.<br>3. The government of Finland is recently formed. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. This photo shows four female ministers.<br>2. The recently formed government of Finland is led by four female ministers. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The photo shows four female ministers of the recently formed government of Finland.<br>2. The photo shows four female ministers of the government of Finland.<br>3. The photo shows four female ministers of the government of Finland.<br>4. The photo shows four female ministers of the government of Finland.<br>5. The photo shows four female ministers of the government of Finland. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. This photo shows the female ministers of the government of Finland.<br>2. The female ministers of the government of Finland are four. | 2 |
| google/gemma-3-1b-it | 1. This photo shows four female ministers.<br>2. The recently formed government of Finland. | 2 |
| google/gemma-3-4b-it | 1. This photo shows four female ministers.<br>2. This photo shows the government of Finland.<br>3. The government of Finland is recently formed. | 3 |
| gpt-3.5-turbo-0125 | 1. The photo shows four female ministers.<br>2. The ministers are part of the recently formed government of Finland. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. This photo shows four female ministers of the recently formed government of Finland. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. This photo shows four female ministers of the recently formed government of Finland. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The photo shows four female ministers of the recently formed government of Finland. | 1 |

---

## Sample ID: quantemp_42
**Original Claim**: Brazil’s defence ministry has not declared 2022 election fraudulent and congress has not been temporarily suspended

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Brazil's defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Brazil's defence ministry has not declared the 2022 election fraudulent.<br>2. Brazil's defence ministry has not declared 2022 election fraudulent.<br>3. Congress has not been temporarily suspended.<br>4. Congress has not been suspended. | 4 |
| google/gemma-3-1b-it | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| google/gemma-3-4b-it | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| gpt-3.5-turbo-0125 | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended in Brazil. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Brazil’s defence ministry has not declared the 2022 election fraudulent.<br>2. Brazil’s congress has not been temporarily suspended. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. Congress has not been temporarily suspended. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Brazil’s defence ministry has not declared 2022 election fraudulent.<br>2. congress has not been temporarily suspended. | 2 |

---

## Sample ID: quantemp_43
**Original Claim**: Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Dainik Bhaskar has reported that Shah Rukh Khan will donate Rs 5 crore for the Ram temple at Ayodhya.<br>2. Shah Rukh Khan will donate Rs 5 crore for the Ram temple at Ayodhya. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Dainik Bhaskar is a newspaper.<br>2. According to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya.<br>3. Dainik Bhaskar is a newspaper.<br>4. According to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for the construction of the Ram temple at Ayodhya. | 1 |
| google/gemma-3-1b-it | 1. Dainik Bhaskar has reported that Shah Rukh Khan will donate Rs 5 crore for the construction of the Ram temple at Ayodhya.<br>2. Red Chillies Entertainment reported that Shah Rukh Khan will donate Rs 5 crore for the construction of the Ram temple at Ayodhya. | 2 |
| google/gemma-3-4b-it | 1. Dainik Bhaskar has reported that.<br>2. According to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore.<br>3. The donation is for construction of the Ram temple.<br>4. The Ram temple is located at Ayodhya. | 4 |
| gpt-3.5-turbo-0125 | 1. Dainik Bhaskar has reported that Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya according to Red Chillies Entertainment. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Dainik Bhaskar has reported that according to Red Chillies Entertainment, Shah Rukh Khan will donate Rs 5 crore for construction of the Ram temple at Ayodhya. | 1 |

---

## Sample ID: quantemp_44
**Original Claim**: Says President Barack Obama’s homeland security budget had "$16 million to fight climate change" but "didn't have a line item to fight violent extremism."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. President Barack Obama’s homeland security budget had "$16 million to fight climate change".<br>2. President Barack Obama’s homeland security budget did not have a line item to fight violent extremism. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. President Barack Obama's homeland security budget had "$16 million to fight climate change."<br>2. President Barack Obama's homeland security budget did not have a line item to fight violent extremism. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States homeland security budget had $16 million to fight climate change.<br>2. President Barack Obama's homeland security budget had "$16 million to fight climate change" but didn't have a line item to fight violent extremism. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. President Barack Obama's homeland security budget had "$16 million to fight climate change".<br>2. President Barack Obama's homeland security budget did not have a line item to fight violent extremism. | 2 |
| google/gemma-3-1b-it | 1. President Barack Obama’s homeland security budget had "$16 million to fight climate change".<br>2. $16 million to fight climate change was allocated to combat.<br>3. “Didn’t have a line item to fight violent extremism.” was a lack of funding. | 3 |
| google/gemma-3-4b-it | 1. President Barack Obama’s homeland security budget had $16 million.<br>2. The $16 million was for fighting climate change.<br>3. The homeland security budget did not have a line item for fighting violent extremism. | 3 |
| gpt-3.5-turbo-0125 | 1. President Barack Obama's homeland security budget had "$16 million to fight climate change".<br>2. President Barack Obama's homeland security budget didn't have a line item to fight violent extremism. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. President Barack Obama’s homeland security budget had "$16 million to fight climate change."<br>2. President Barack Obama’s homeland security budget did not have a line item to fight violent extremism. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. President Barack Obama’s homeland security budget had "$16 million to fight climate change."<br>2. President Barack Obama’s homeland security budget didn't have a line item to fight violent extremism. | 2 |

---

## Sample ID: quantemp_45
**Original Claim**: "I saved the taxpayers $2-billion on a bogus Air Force Boeing tanker deal where people went to jail."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. I saved the taxpayers $2-billion.<br>2. The Air Force Boeing tanker deal was bogus.<br>3. People went to jail in connection with the Air Force Boeing tanker deal. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. I saved the taxpayers $2-billion on a bogus Air Force Boeing tanker deal.<br>2. People went to jail in the Air Force Boeing tanker deal. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Air Force Boeing tanker deal was a $2-billion contract.<br>2. People went to jail.<br>3. The taxpayers were saved. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Air Force entered into a $2-billion deal with Boeing.<br>2. People were jailed as a result of the Air Force's $2-billion deal with Boeing. | 2 |
| google/gemma-3-1b-it | 1. A bogus Air Force Boeing tanker deal occurred where people went to jail.<br>2. Saving taxpayers $2-billion on a bogus Air Force Boeing tanker deal. | 2 |
| google/gemma-3-4b-it | 1. I saved the taxpayers $2-billion.<br>2. The saving occurred on a bogus Air Force Boeing tanker deal.<br>3. People went to jail. | 3 |
| gpt-3.5-turbo-0125 | 1. The speaker saved the taxpayers $2-billion on a bogus Air Force Boeing tanker deal.<br>2. People went to jail in the bogus Air Force Boeing tanker deal. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The speaker saved the taxpayers $2-billion on a bogus Air Force Boeing tanker deal.<br>2. People went to jail in relation to the bogus Air Force Boeing tanker deal. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "I saved the taxpayers $2-billion on a bogus Air Force Boeing tanker deal where people went to jail." | 1 |

---

## Sample ID: quantemp_46
**Original Claim**: Congressman Robert Hurt has a plan to cut education by 40 percent.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Congressman Robert Hurt has a plan to cut education. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Congressman Robert Hurt has a plan to cut education.<br>2. Congressman Robert Hurt's plan to cut education by 40 percent. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Congressman Robert Hurt<br>2. A plan to cut education by 40 percent<br>3. A plan to cut education by 40 percent in the United States | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Congressman Robert Hurt has a plan.<br>2. Congressman Robert Hurt has a plan to cut education.<br>3. Congressman Robert Hurt has a plan to cut education by 40 percent. | 3 |
| google/gemma-3-1b-it | 1. Congressman Robert Hurt has a plan to cut education by 40 percent. | 1 |
| google/gemma-3-4b-it | 1. Congressman Robert Hurt has a plan.<br>2. The plan is to cut education by 40 percent. | 2 |
| gpt-3.5-turbo-0125 | 1. Congressman Robert Hurt has a plan to cut education by 40 percent. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Congressman Robert Hurt has a plan to cut education by 40 percent. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Congressman Robert Hurt has a plan to cut education by 40 percent. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Congressman Robert Hurt has a plan to cut education by 40 percent. | 1 |

---

## Sample ID: quantemp_47
**Original Claim**: A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup, adding, "They've lost their audience."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup, adding, "They've lost their audience." | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. The executive added, "They've lost their audience." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Country Music Television (CMT) is a television network.<br>2. Country Music Television (CMT) is a television network.<br>3. Country Music Television (CMT) is a television network.<br>4. Country Music Television (CMT) is a television network.<br>5. Country Music Television (CMT) is a television network.<br>6. Country Music Television (CMT) is a television network.<br>7. Country Music Television (CMT) is a television network.<br>8. Country Music Television (CMT) is a television network.<br>9. Country Music Television (CMT) is a television network.<br>10. Country Music Television (CMT) is a television network.<br>11. Country Music Television (CMT) is a television network.<br>12. Country Music Television (CMT) is a television network.<br>13. Country Music Television (CMT) is a television network.<br>14. Country Music Television (CMT) is a television network.<br>15. Country Music Television (CMT) is a television network.<br>16. Country Music Television (CMT) is a television network.<br>17. Country Music Television (CMT) is a television network.<br>18. Country Music Television (CMT) is a television network.<br>19. Country Music Television (CMT) is a television network.<br>20. Country Music Television (CMT) is | 20 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. A Paramount executive said in July 2023 that they have lost the audience of Country Music Television (CMT). | 2 |
| google/gemma-3-1b-it | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be “cut” from its channel lineup.<br>2. Country Music Television (CMT) might be “cut” from its channel lineup. | 2 |
| google/gemma-3-4b-it | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. The executive added, "They've lost their audience." | 2 |
| gpt-3.5-turbo-0125 | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from Paramount's channel lineup.<br>2. A Paramount executive said in July 2023 that Country Music Television (CMT) has lost its audience. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. A Paramount executive said in July 2023, "They've lost their audience." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. A Paramount executive said in July 2023, "They've lost their audience." | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A Paramount executive said in July 2023 that Country Music Television (CMT) might be "cut" from its channel lineup.<br>2. A Paramount executive said in July 2023, "They've lost their audience." | 2 |

---

## Sample ID: quantemp_48
**Original Claim**: As a student at Occidental College in Los Angeles from 1979 to 1981, "there were days where folks couldn't go outside. … because of all the pollution in the air."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. As a student at Occidental College in Los Angeles from 1979 to 1981, there were days where folks couldn't go outside because of all the pollution in the air. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. As a student at Occidental College in Los Angeles from 1979 to 1981, "there were days where folks couldn't go outside."<br>2. Because of all the pollution in the air, "there were days where folks couldn't go outside." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Occidental College<br>2. Los Angeles<br>3. 1979<br>4. 1981 | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The student was at Occidental College in Los Angeles.<br>2. The student was a student at Occidental College in Los Angeles from 1979 to 1981.<br>3. There were days where folks could not go outside at Occidental College in Los Angeles.<br>4. There were days where folks could not go outside because of the pollution in the air at Occidental College in Los Angeles. | 4 |
| google/gemma-3-1b-it | 1. As a student at Occidental College in Los Angeles from 1979 to 1981, there were days where folks couldn’t go outside.<br>2. Because of all the pollution in the air, there were days where folks couldn’t go outside. | 2 |
| google/gemma-3-4b-it | 1. There were days where folks couldn't go outside.<br>2. The student was at Occidental College in Los Angeles.<br>3. The student's time at Occidental College in Los Angeles was from 1979 to 1981.<br>4. There was pollution in the air. | 4 |
| gpt-3.5-turbo-0125 | 1. The speaker was a student at Occidental College in Los Angeles from 1979 to 1981.<br>2. There were days where folks couldn't go outside at Occidental College in Los Angeles from 1979 to 1981.<br>3. The reason folks couldn't go outside was because of all the pollution in the air at Occidental College in Los Angeles from 1979 to 1981. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. The person was a student at Occidental College in Los Angeles from 1979 to 1981.<br>2. There were days from 1979 to 1981 when people at Occidental College in Los Angeles could not go outside because of all the pollution in the air. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. As a student at Occidental College in Los Angeles from 1979 to 1981, there were days where folks couldn't go outside because of all the pollution in the air. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. As a student at Occidental College in Los Angeles from 1979 to 1981, "there were days where folks couldn't go outside."<br>2. As a student at Occidental College in Los Angeles from 1979 to 1981, "because of all the pollution in the air." | 2 |

---

## Sample ID: quantemp_49
**Original Claim**: Anambra State has a combined debt profile of over N200 billion.Former Governor Peter Obi handed over N72 billion in cash and $150 million to Governor Willie Obiano.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash and $150 million to Governor Willie Obiano. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| google/gemma-3-1b-it | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano. | 2 |
| google/gemma-3-4b-it | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| gpt-3.5-turbo-0125 | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash and $150 million to Governor Willie Obiano. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Anambra State has a combined debt profile of over N200 billion.<br>2. Former Governor Peter Obi handed over N72 billion in cash to Governor Willie Obiano.<br>3. Former Governor Peter Obi handed over $150 million to Governor Willie Obiano. | 3 |

---

## Sample ID: quantemp_50
**Original Claim**: Says D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Michael Fanone is a D.C. police officer.<br>2. Michael Fanone was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6.<br>2. Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6.<br>3. Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Michael Fanone is a D.C. police officer.<br>2. Michael Fanone was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6.<br>3. Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 3 |
| google/gemma-3-1b-it | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |
| google/gemma-3-4b-it | 1. D.C. police officer Michael Fanone is the same person who was arrested.<br>2. The arrest occurred after carrying a Confederate flag through the U.S. Capitol.<br>3. The event occurred on Jan. 6. | 3 |
| gpt-3.5-turbo-0125 | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Says D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. D.C. police officer Michael Fanone is the same person who was arrested after carrying a Confederate flag through the U.S. Capitol on Jan. 6. | 1 |

---

## Sample ID: quantemp_51
**Original Claim**: A video authentically shows U.S. President Joe Biden tumbling down airplane stairs as he disembarked from Air Force One on a trip to Poland in February 2023.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. U.S. President Joe Biden tumbling down airplane stairs occurs as he disembarks from Air Force One.<br>3. U.S. President Joe Biden disembarks from Air Force One on a trip to Poland.<br>4. The event of U.S. President Joe Biden tumbling down airplane stairs happens in February 2023. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs as he disembarked from Air Force One on a trip to Poland in February 2023. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. U.S. President Joe Biden<br>2. Air Force One<br>3. February<br>4. Poland | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs as he disembarked from Air Force One.<br>2. The airplane was Air Force One.<br>3. The trip was to Poland.<br>4. The trip occurred in February 2023. | 4 |
| google/gemma-3-1b-it | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. The video occurred on a trip to Poland in February 2023.<br>3. The video shows Biden disembarking from Air Force One. | 3 |
| google/gemma-3-4b-it | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. The video shows Joe Biden disembarking from Air Force One.<br>3. The trip was to Poland.<br>4. The trip occurred in February 2023. | 4 |
| gpt-3.5-turbo-0125 | 1. The video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. U.S. President Joe Biden tumbled down airplane stairs as he disembarked from Air Force One on a trip to Poland in February 2023. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. U.S. President Joe Biden tumbled down airplane stairs as he disembarked from Air Force One.<br>3. U.S. President Joe Biden disembarked from Air Force One on a trip to Poland in February 2023. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs as he disembarked from Air Force One on a trip to Poland in February 2023. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A video authentically shows U.S. President Joe Biden tumbling down airplane stairs.<br>2. U.S. President Joe Biden disembarked from Air Force One on a trip to Poland in February 2023. | 2 |

---

## Sample ID: quantemp_52
**Original Claim**: Photos show the site of the Manipur ambush by militants that killed Colonel Viplav Tripathi, his family, and four other soldiers.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Photos show the site of the Manipur ambush by militants.<br>2. The Manipur ambush by militants killed Colonel Viplav Tripathi.<br>3. The Manipur ambush by militants killed Viplav Tripathi's family.<br>4. The Manipur ambush by militants killed four other soldiers. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Photos show the site of the Manipur ambush.<br>2. The ambush killed Colonel Viplav Tripathi, his family, and four other soldiers. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The site of the Manipur ambush by militants that killed Colonel Viplav Tripathi, his family, and four other soldiers is located in Manipur.<br>2. The ambush was carried out by militants in Manipur.<br>3. Colonel Viplav Tripathi was killed in the ambush.<br>4. The ambush was in Manipur. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Photos show the site of the Manipur ambush.<br>2. The Manipur ambush was carried out by militants.<br>3. The Manipur ambush killed Colonel Viplav Tripathi.<br>4. The Manipur ambush killed Colonel Viplav Tripathi's family.<br>5. The Manipur ambush killed four other soldiers.<br>6. Colonel Viplav Tripathi was killed in the Manipur ambush.<br>7. Colonel Viplav Tripathi's family was killed in the Manipur ambush. | 7 |
| google/gemma-3-1b-it | 1. Photos show the site of the Manipur ambush by militants.<br>2. The site of the Manipur ambush by militants that killed Colonel Viplav Tripathi, his family, and four other soldiers. | 2 |
| google/gemma-3-4b-it | 1. Photos show the site of the Manipur ambush.<br>2. The Manipur ambush was carried out by militants.<br>3. The Manipur ambush killed Colonel Viplav Tripathi.<br>4. The Manipur ambush killed his family.<br>5. The Manipur ambush killed four other soldiers. | 5 |
| gpt-3.5-turbo-0125 | 1. Photos show the site of the Manipur ambush by militants.<br>2. The Manipur ambush by militants killed Colonel Viplav Tripathi.<br>3. The Manipur ambush by militants killed Colonel Viplav Tripathi's family.<br>4. The Manipur ambush by militants killed four other soldiers. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Photos show the site of the Manipur ambush by militants.<br>2. The Manipur ambush by militants killed Colonel Viplav Tripathi.<br>3. The Manipur ambush by militants killed the family of Colonel Viplav Tripathi.<br>4. The Manipur ambush by militants killed four other soldiers. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Photos show the site of the Manipur ambush by militants that killed Colonel Viplav Tripathi, his family, and four other soldiers. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photos show the site of the Manipur ambush by militants.<br>2. The Manipur ambush by militants killed Colonel Viplav Tripathi.<br>3. The Manipur ambush by militants killed Colonel Viplav Tripathi's family.<br>4. The Manipur ambush by militants killed four other soldiers. | 4 |

---

## Sample ID: quantemp_53
**Original Claim**: NPR published an article that described pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol hours before the riot took place.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. NPR published an article.<br>2. The article described pro-Trump supporters.<br>3. The pro-Trump supporters decried the 2020 election results.<br>4. The pro-Trump supporters stormed the U.S. Capitol hours before the riot took place. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. NPR published an article.<br>2. The article described pro-Trump supporters.<br>3. The article described the 2020 election results.<br>4. The article described the storming of the U.S. Capitol.<br>5. The article described the riot that took place. | 5 |
| meta-llama/Llama-3.2-1B-Instruct | 1. NPR published an article.<br>2. The 2020 election results were announced.<br>3. The U.S. Capitol was stormed. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. NPR published an article.<br>2. The article described pro-Trump supporters.<br>3. The article described pro-Trump supporters storming the U.S. Capitol.<br>4. The article described pro-Trump supporters storming the U.S. Capitol hours before the 2020 election results. | 4 |
| google/gemma-3-1b-it | 1. NPR published an article describing pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol.<br>2. The article described pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol.<br>3. The article described pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol. | 3 |
| google/gemma-3-4b-it | 1. NPR published an article.<br>2. The article described pro-Trump supporters.<br>3. Pro-Trump supporters decried the 2020 election results.<br>4. The 2020 election results were stormed.<br>5. Pro-Trump supporters stormed the U.S. Capitol.<br>6. The storming occurred hours before the riot took place. | 6 |
| gpt-3.5-turbo-0125 | 1. NPR published an article.<br>2. The article described pro-Trump supporters.<br>3. The pro-Trump supporters decried the 2020 election results.<br>4. The pro-Trump supporters stormed the U.S. Capitol.<br>5. The storming took place hours before the riot. | 5 |
| gpt-4.1-mini-2025-04-14 | 1. NPR published an article.<br>2. The article published by NPR described pro-Trump supporters who decried the 2020 election results.<br>3. The article published by NPR described pro-Trump supporters storming the U.S. Capitol hours before the riot took place. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. NPR published an article that described pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol hours before the riot took place. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. NPR published an article.<br>2. NPR published an article that described pro-Trump supporters storming the U.S. Capitol.<br>3. NPR published an article that described pro-Trump supporters who decried the 2020 election results storming the U.S. Capitol hours before the riot took place. | 3 |

---

## Sample ID: quantemp_54
**Original Claim**: The Indian Government is considering a 30% salary cut for employees.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Indian Government is considering a 30% salary cut for employees.<br>2. The Indian Government is considering a 30% salary cut for employees.<br>3. The Indian Government is considering a 30% salary cut for employees.<br>4. The Indian Government is considering a 30% salary cut for employees.<br>5. The Indian Government is considering a 30% salary cut for employees.<br>6. The Indian Government is considering a 30% salary cut for employees.<br>7. The Indian Government is considering a 30% salary cut for employees.<br>8. The Indian Government is considering a 30% salary cut for employees.<br>9. The Indian Government is considering a 30% salary cut for employees.<br>10. The Indian Government is considering a 30% salary cut for employees.<br>11. The Indian Government is considering a 30% salary cut for employees.<br>12. The Indian Government is considering a 30% salary cut for employees.<br>13. The Indian Government is considering a 30% salary cut for employees.<br>14. The Indian Government is considering a 30% salary cut for employees.<br>15. The Indian Government is considering a 30% salary cut for employees.<br>16. The Indian Government is considering a 30% salary cut for employees.<br>17. The Indian Government is considering a 30% salary cut for employees. | 17 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| google/gemma-3-1b-it | 1. The Indian Government is considering a 30% salary cut for employees.<br>2. The Indian Government is considering a 30% salary cut. | 2 |
| google/gemma-3-4b-it | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| gpt-3.5-turbo-0125 | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The Indian Government is considering a 30% salary cut for employees. | 1 |

---

## Sample ID: quantemp_55
**Original Claim**: Using ginger can regrow your hair in 21 days

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Using ginger can regrow your hair in 21 days. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Using ginger can regrow your hair.<br>2. Using ginger can regrow your hair in 21 days. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Using ginger can regrow your hair in 21 days.<br>2. The effectiveness of using ginger for hair regrowth is not well established.<br>3. There is limited scientific evidence supporting the use of ginger for hair regrowth.<br>4. Some studies have shown that ginger can stimulate hair growth, but the results are inconsistent.<br>5. More research is needed to confirm the effectiveness of using ginger for hair regrowth.<br>6. There is currently no standard treatment for hair regrowth using ginger.<br>7. Hair regrowth is a complex process that involves multiple factors, including genetics, nutrition, and overall health.<br>8. The use of ginger for hair regrowth is not a proven treatment.<br>9. The use of ginger for hair regrowth is not supported by current medical evidence. | 9 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Using ginger can regrow hair in 21 days. | 1 |
| google/gemma-3-1b-it | 1. Ginger can regrow hair.<br>2. Regrowing your hair in 21 days using ginger. | 2 |
| google/gemma-3-4b-it | 1. Using ginger can regrow hair in 21 days. | 1 |
| gpt-3.5-turbo-0125 | 1. Using ginger can regrow your hair in 21 days. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Using ginger can regrow your hair in 21 days. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Using ginger can regrow your hair in 21 days. | 1 |

---

## Sample ID: quantemp_56
**Original Claim**: Says his proposed payroll tax cut "will mean an extra $1,500 in your pocket compared to if we do nothing."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. His proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The speaker proposes a payroll tax cut.<br>2. The speaker claims that the payroll tax cut will mean an extra $1,500 in the pocket compared to if no action is taken. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing.<br>2. The proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing.<br>3. The proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The person making the claim says his proposed payroll tax cut "will mean an extra $1,500 in your pocket compared to if we do nothing." | 1 |
| google/gemma-3-1b-it | 1. His proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing. | 1 |
| google/gemma-3-4b-it | 1. He says his proposed payroll tax cut will mean an extra $1,500 in your pocket.<br>2. He says this will mean an extra $1,500 in your pocket compared to if we do nothing. | 2 |
| gpt-3.5-turbo-0125 | 1. His proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The proposed payroll tax cut will mean an extra $1,500 in your pocket compared to if we do nothing. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. His proposed payroll tax cut "will mean an extra $1,500 in your pocket compared to if we do nothing." | 1 |

---

## Sample ID: quantemp_57
**Original Claim**: AIDS was transmitted to humans because "one guy" had sex with "a monkey" and then started "having sex with men."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. AIDS was transmitted to humans because one guy had sex with a monkey.<br>2. One guy had sex with a monkey and then started having sex with men. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. AIDS was transmitted to humans.<br>2. "One guy" had sex with "a monkey" and then started "having sex with men." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I can't fulfill this request | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. AIDS was transmitted to humans because one guy had sex with a monkey.<br>2. One guy had sex with a monkey.<br>3. One guy had sex with men.<br>4. A monkey. | 4 |
| google/gemma-3-1b-it | 1. AIDS was transmitted to humans because “one guy” had sex with “a monkey.”<br>2. AIDS was transmitted to humans.<br>3. The transmission of AIDS occurred due to a specific sexual act. | 3 |
| google/gemma-3-4b-it | 1. AIDS was transmitted to humans.<br>2. “one guy” had sex with “a monkey”.<br>3. “one guy” started “having sex with men”. | 3 |
| gpt-3.5-turbo-0125 | 1. AIDS was transmitted to humans.<br>2. "One guy" had sex with "a monkey."<br>3. "One guy" started "having sex with men." | 3 |
| gpt-4.1-mini-2025-04-14 | 1. AIDS was transmitted to humans because one guy had sex with a monkey.<br>2. AIDS was transmitted to humans because one guy then started having sex with men. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. AIDS was transmitted to humans because "one guy" had sex with "a monkey".<br>2. AIDS was transmitted to humans because "one guy" then started "having sex with men." | 2 |

---

## Sample ID: quantemp_58
**Original Claim**: Florida Agriculture Commissioner Nikki Fried “suspended gun rights — no due process — just because she says these people were merely ‘involved’ in January 6.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. Florida Agriculture Commissioner Nikki Fried suspended gun rights without due process.<br>3. Florida Agriculture Commissioner Nikki Fried suspended gun rights because she says these people were merely ‘involved’ in January 6. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nikki Fried is the Florida Agriculture Commissioner.<br>2. Nikki Fried suspended gun rights.<br>3. Nikki Fried said these people were merely 'involved' in January 6.<br>4. Due process was not followed in the suspension of gun rights. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Florida Agriculture Commissioner Nikki Fried<br>2. Suspended gun rights<br>3. No due process<br>4. Just because | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nikki Fried was the Florida Agriculture Commissioner.<br>2. She suspended gun rights in Florida.<br>3. The suspension of gun rights in Florida was without due process.<br>4. The people involved in January 6 were involved in the January 6 incident.<br>5. Nikki Fried said the people involved in January 6 were merely 'involved' in the January 6 incident. | 5 |
| google/gemma-3-1b-it | 1. Nikki Fried was suspended as Florida Agriculture Commissioner.<br>2. Gun rights — no due process — was suspended by Nikki Fried.<br>3. January 6th was a political event. | 3 |
| google/gemma-3-4b-it | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. The suspension of gun rights occurred without due process.<br>3. The suspension of gun rights was stated by Florida Agriculture Commissioner Nikki Fried.<br>4. These people were merely “involved” in January 6.<br>5. Florida Agriculture Commissioner Nikki Fried said these people were merely “involved” in January 6. | 5 |
| gpt-3.5-turbo-0125 | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. The suspension of gun rights by Florida Agriculture Commissioner Nikki Fried had no due process.<br>3. The suspension of gun rights by Florida Agriculture Commissioner Nikki Fried was based on people merely 'involved' in January 6. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. Florida Agriculture Commissioner Nikki Fried suspended gun rights without due process.<br>3. Florida Agriculture Commissioner Nikki Fried suspended gun rights just because Florida Agriculture Commissioner Nikki Fried says these people were merely "involved" in January 6. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. Florida Agriculture Commissioner Nikki Fried suspended gun rights “no due process.”<br>3. Florida Agriculture Commissioner Nikki Fried suspended gun rights “just because she says these people were merely ‘involved’ in January 6.” | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Florida Agriculture Commissioner Nikki Fried suspended gun rights.<br>2. Florida Agriculture Commissioner Nikki Fried suspended gun rights with no due process.<br>3. Florida Agriculture Commissioner Nikki Fried suspended gun rights just because she says these people were merely involved in January 6. | 3 |

---

## Sample ID: quantemp_59
**Original Claim**: Starting in 2011, "you will be required to pay taxes" on "the value of whatever health insurance you are given by the company."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Starting in 2011, you will be required to pay taxes on the value of whatever health insurance you are given by the company. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Starting in 2011, "you will be required to pay taxes" on "the value of whatever health insurance you are given by the company."<br>2. Starting in 2011, "you will be required to pay taxes" on "the value of whatever health insurance you are given by the company" has been in effect since 2011. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Starting in 2011, "you will be required to pay taxes" on "the value of whatever health insurance you are given by the company."<br>2. The value of whatever health insurance you are given by the company is required to be paid taxes.<br>3. The value of whatever health insurance you are given by the company is required to be paid taxes in 2011. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The year 2011 began.<br>2. You will be required to pay taxes on the value of health insurance given by the company starting in 2011.<br>3. The value of health insurance given by the company is subject to taxation. | 3 |
| google/gemma-3-1b-it | 1. “you will be required to pay taxes” on the value of whatever health insurance you are given by the company.<br>2. Starting in 2011, “you will be required to pay taxes” on the value of whatever health insurance you are given by the company. | 2 |
| google/gemma-3-4b-it | 1. Starting in 2011, you will be required to pay taxes.<br>2. The taxes are on the value of whatever health insurance you are given by the company. | 2 |
| gpt-3.5-turbo-0125 | 1. The requirement to pay taxes on the value of health insurance given by the company started in 2011.<br>2. "You will be required to pay taxes" on "the value of whatever health insurance you are given by the company" started in 2011. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Starting in 2011, you will be required to pay taxes on the value of whatever health insurance you are given by the company. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Starting in 2011, “you will be required to pay taxes” on “the value of whatever health insurance you are given by the company.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Starting in 2011, "you will be required to pay taxes" on "the value of whatever health insurance you are given by the company." | 1 |

---

## Sample ID: quantemp_60
**Original Claim**: Viral image shows 66 EVMs that were seized from the house of a BJP leader in West Bengal

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A viral image shows 66 EVMs.<br>2. 66 EVMs were seized from the house of a BJP leader in West Bengal. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A viral image shows 66 EVMs (Emergency Withdrawal Machines) that were seized from the house of a BJP leader in West Bengal. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The house of a BJP leader in West Bengal was seized.<br>2. Viral images show 66 EVMs seized from the house of a BJP leader in West Bengal. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A viral image shows 66 EVMs that were seized from the house of a BJP leader in West Bengal. | 1 |
| google/gemma-3-1b-it | 1. Viral image shows 66 EVMs seized from the house of a BJP leader in West Bengal. | 1 |
| google/gemma-3-4b-it | 1. There is a viral image.<br>2. The image shows 66 EVMs.<br>3. The 66 EVMs were seized.<br>4. The seizure occurred from the house.<br>5. The house belongs to a BJP leader.<br>6. The location is West Bengal. | 6 |
| gpt-3.5-turbo-0125 | 1. Viral image shows 66 EVMs that were seized from the house of a BJP leader in West Bengal. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A viral image shows 66 EVMs.<br>2. The 66 EVMs were seized from the house of a BJP leader in West Bengal. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Viral image shows 66 EVMs.<br>2. 66 EVMs were seized from the house of a BJP leader in West Bengal. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Viral image shows 66 EVMs.<br>2. 66 EVMs were seized from the house of a BJP leader in West Bengal. | 2 |

---

## Sample ID: quantemp_61
**Original Claim**: While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection.” | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Senate Majority Leader Chuck Schumer (D-NY) spoke on the Senate floor on Jan. 22, 2021.<br>2. Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection.” | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Senate Majority Leader Chuck Schumer (D-NY) spoke on the Senate floor on Jan. 22, 2021.<br>2. Schumer accidentally said “erection” instead of “insurrection” during a speech. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Senate Majority Leader Chuck Schumer (D-NY) was speaking on the Senate floor on Jan. 22, 2021.<br>2. Senate Majority Leader Chuck Schumer (D-NY) said "erection" instead of "insurrection". | 2 |
| google/gemma-3-1b-it | 1. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection”. | 1 |
| google/gemma-3-4b-it | 1. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) said “erection.”<br>2. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) said “insurrection.” | 2 |
| gpt-3.5-turbo-0125 | 1. Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection” while speaking on the Senate floor on Jan. 22, 2021. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Senate Majority Leader Chuck Schumer (D-NY) spoke on the Senate floor on Jan. 22, 2021.<br>2. Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection” while speaking on the Senate floor on Jan. 22, 2021. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. While speaking on the Senate floor on Jan. 22, 2021, Senate Majority Leader Chuck Schumer (D-NY) accidentally said “erection” instead of “insurrection.” | 1 |

---

## Sample ID: quantemp_62
**Original Claim**: Yogi Adityanath called for a Bharat Band on January 1, 2023, demanding that India be declared a Hindu nation

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation on January 1, 2023. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation. | 2 |
| google/gemma-3-1b-it | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Bharat Band was demanded by Yogi Adityanath in India. | 2 |
| google/gemma-3-4b-it | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. The Bharat Band was demanded that India be declared a Hindu nation. | 2 |
| gpt-3.5-turbo-0125 | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath called for a Bharat Band demanding that India be declared a Hindu nation. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation on January 1, 2023. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Yogi Adityanath called for a Bharat Band on January 1, 2023.<br>2. Yogi Adityanath demanded that India be declared a Hindu nation. | 2 |

---

## Sample ID: quantemp_63
**Original Claim**: ACTRESS SANDRA BULLOCK: ‘DONALD TRUMP IS DOING EVERYTHING TO IMPROVE OUR NATION, IF YOU DON’T LIKE HIM JUST…’ – New News 40

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. ACTRESS SANDRA BULLOCK made a statement about DONALD TRUMP.<br>2. ACTRESS SANDRA BULLOCK said that DONALD TRUMP is doing everything to improve our nation.<br>3. ACTRESS SANDRA BULLOCK added that if you don’t like him, just…<br>4. The statement was reported by New News 40. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Sandra Bullock is an actress.<br>2. Donald Trump is a political figure.<br>3. Sandra Bullock made a statement about Donald Trump.<br>4. The statement was on a news show. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. ACTRESS SANDRA BULLOCK<br>2. ‘DONALD TRUMP IS DOING EVERYTHING TO IMPROVE OUR NATION, IF YOU DON'T LIKE HIM JUST DON'T’<br>3. New News 40 | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Sandra Bullock is an actress.<br>2. Donald Trump is a person.<br>3. Sandra Bullock said 'Donald Trump is doing everything to improve our nation, if you don’t like him just…' | 3 |
| google/gemma-3-1b-it | 1. Sandra Bullock is an actress.<br>2. Donald Trump is doing everything to improve our nation.<br>3. If you do not like Donald Trump, then…<br>4. New News 40 is a news source. | 4 |
| google/gemma-3-4b-it | 1. SANDRA BULLOCK is an ACTRESS.<br>2. DONALD TRUMP is doing everything to improve our nation.<br>3. New News 40 reported that SANDRA BULLOCK said DONALD TRUMP is doing everything to improve our nation. | 3 |
| gpt-3.5-turbo-0125 | 1. Sandra Bullock said that Donald Trump is doing everything to improve our nation.<br>2. Sandra Bullock said that if you don't like Donald Trump, just... | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Actress Sandra Bullock said, "Donald Trump is doing everything to improve our nation."<br>2. Actress Sandra Bullock said, "If you don’t like Donald Trump just…" | 2 |
| gpt-5.4-nano-2026-03-17 | 1. ACTRESS SANDRA BULLOCK said “DONALD TRUMP IS DOING EVERYTHING TO IMPROVE OUR NATION, IF YOU DON’T LIKE HIM JUST…”.<br>2. The statement “DONALD TRUMP IS DOING EVERYTHING TO IMPROVE OUR NATION, IF YOU DON’T LIKE HIM JUST…” is associated with New News 40. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. ACTRESS SANDRA BULLOCK said, “DONALD TRUMP IS DOING EVERYTHING TO IMPROVE OUR NATION, IF YOU DON’T LIKE HIM JUST…” – New News 40. | 1 |

---

## Sample ID: quantemp_64
**Original Claim**: Russia And China Roll Out 100% Gold-Backed Currency

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Russia rolled out a 100% gold-backed currency.<br>2. China rolled out a 100% gold-backed currency. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Russia and China are rolling out 100% gold-backed currency.<br>2. Russia and China are introducing 100% gold-backed currency. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Russia<br>2. China<br>3. Rolled<br>4. Out<br>5. 100% | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Russia and China rolled out 100% gold-backed currency.<br>2. Russia and China rolled out a currency backed 100% by gold. | 2 |
| google/gemma-3-1b-it | 1. Russia and China are both countries.<br>2. Russia and China are rolling out a new currency.<br>3. Russia and China are rolling out a 100% gold-backed currency. | 3 |
| google/gemma-3-4b-it | 1. Russia and China are rolling out 100% gold-backed currency. | 1 |
| gpt-3.5-turbo-0125 | 1. Russia rolled out 100% gold-backed currency.<br>2. China rolled out 100% gold-backed currency. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Russia rolled out a 100% gold-backed currency.<br>2. China rolled out a 100% gold-backed currency. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Russia and China rolled out 100% gold-backed currency. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Russia and China roll out 100% gold-backed currency. | 1 |

---

## Sample ID: quantemp_65
**Original Claim**: A Dominion Voting Systems employee named Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An employee named Eric Coomer of Dominion Voting Systems said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!” | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Eric Coomer is a Dominion Voting Systems employee.<br>2. Eric Coomer made a statement about the 2020 election.<br>3. Eric Coomer said, "Don't worry about the election, Trump's not gonna win. I made f-----g sure of that!" | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Dominion Voting Systems employee Eric Coomer made a statement on an "antifa conference call" prior to the 2020 election.<br>2. Eric Coomer is a Dominion Voting Systems employee.<br>3. Eric Coomer made a statement on an "antifa conference call" prior to the 2020 election.<br>4. Eric Coomer is a Dominion Voting Systems employee.<br>5. Eric Coomer made a statement on an "antifa conference call" prior to the 2020 election. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Eric Coomer was a Dominion Voting Systems employee.<br>2. Eric Coomer said something on an “antifa conference call.<br>3. The “antifa conference call” was prior to the 2020 election.<br>4. Eric Coomer said “Don’t worry about the election, Trump’s not gonna win.<br>5. Eric Coomer said “I made f-----g sure of that!” | 5 |
| google/gemma-3-1b-it | 1. Eric Coomer was a Dominion Voting Systems employee.<br>2. On an “antifa conference call,” Eric Coomer stated that Donald Trump would not win the 2020 election.<br>3. Donald Trump’s actions prior to the 2020 election were a concern. | 3 |
| google/gemma-3-4b-it | 1. A Dominion Voting Systems employee named Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win.”<br>2. Eric Coomer is a Dominion Voting Systems employee.<br>3. The statement was made on an “antifa conference call”.<br>4. The conference call occurred prior to the 2020 election.<br>5. Eric Coomer said, “Don’t worry about the election, Trump’s not gonna win.”<br>6. Trump is a political candidate. | 6 |
| gpt-3.5-turbo-0125 | 1. A Dominion Voting Systems employee named Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!” | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Eric Coomer is a Dominion Voting Systems employee.<br>2. Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!” | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A Dominion Voting Systems employee named Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A Dominion Voting Systems employee named Eric Coomer said on an “antifa conference call” prior to the 2020 election, “Don’t worry about the election, Trump’s not gonna win. I made f-----g sure of that!” | 1 |

---

## Sample ID: quantemp_66
**Original Claim**: Image shows a Google statement informing user of a 10-year ban

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Image shows a Google statement informing user of a 10-year ban | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Image shows a Google statement.<br>2. The statement informs the user of a 10-year ban. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Google<br>2. a 10-year ban<br>3. on image shows a Google statement informing users of | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Image shows a Google statement informing a user of a 10-year ban. | 1 |
| google/gemma-3-1b-it | 1. Google stated a 10-year ban.<br>2. Image shows a Google statement informing user of a 10-year ban. | 2 |
| google/gemma-3-4b-it | 1. The image shows a Google statement.<br>2. The Google statement informs the user.<br>3. The Google statement informs the user of a 10-year ban. | 3 |
| gpt-3.5-turbo-0125 | 1. The image shows a Google statement.<br>2. The Google statement informs the user of a 10-year ban. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The image shows a Google statement informing the user of a 10-year ban. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Image shows a Google statement informing user of a 10-year ban. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Image shows a Google statement informing user of a 10-year ban. | 1 |

---

## Sample ID: quantemp_67
**Original Claim**: Actor-politician Mithun Chakroborty has tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Actor-politician Mithun Chakroborty has tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Mithun Chakroborty is an actor-politician.<br>2. Mithun Chakroborty has tweeted.<br>3. Doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Mithun Chakroborty is an actor.<br>2. Mithun Chakroborty is a politician.<br>3. Mithun Chakroborty is a doctor.<br>4. Mithun Chakroborty is a West Bengal chief minister.<br>5. Mithun Chakroborty advised Mamata Banerjee to rest for five years. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Mithun Chakroborty is an actor-politician.<br>2. Mithun Chakroborty has tweeted that doctors have advised Mamata Banerjee to rest.<br>3. Doctors have advised Mamata Banerjee to rest for five years.<br>4. Mamata Banerjee is the chief minister of West Bengal. | 4 |
| google/gemma-3-1b-it | 1. Mithun Chakroborty is an actor.<br>2. Actor-politician Mithun Chakroborty tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 2 |
| google/gemma-3-4b-it | 1. Actor-politician Mithun Chakroborty has tweeted.<br>2. Doctors have advised West Bengal chief minister Mamata Banerjee to rest.<br>3. The period of rest advised is five years. | 3 |
| gpt-3.5-turbo-0125 | 1. Mithun Chakroborty has tweeted that doctors have advised Mamata Banerjee to rest for five years. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Actor-politician Mithun Chakroborty has tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Actor-politician Mithun Chakroborty has tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Actor-politician Mithun Chakroborty has tweeted that doctors have advised West Bengal chief minister Mamata Banerjee to rest for five years. | 1 |

---

## Sample ID: quantemp_68
**Original Claim**: In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States occurred.<br>2. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Michele Bachmann told Fox News in August 2014.<br>2. In August 2014, Michele Bachmann said banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation.<br>2. Michele Bachmann is a U.S. politician.<br>3. Michele Bachmann is a U.S. politician.<br>4. Michele Bachmann is a U.S. politician.<br>5. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Michele Bachmann told Fox News in August 2014 that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 1 |
| google/gemma-3-1b-it | 1. Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 1 |
| google/gemma-3-4b-it | 1. In August 2014, Michele Bachmann told Fox News.<br>2. August 2014 was the date when Michele Bachmann told Fox News.<br>3. Banning Mexican food in the United States would stop Mexicans from entering the country without documentation, according to Michele Bachmann. | 3 |
| gpt-3.5-turbo-0125 | 1. Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation.<br>2. Michele Bachmann told Fox News this in August 2014. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In August 2014, Michele Bachmann told Fox News that banning Mexican food in the United States would stop Mexicans from entering the country without documentation. | 1 |

---

## Sample ID: quantemp_69
**Original Claim**: Says Mike Gallagher’s plan "would cut Social Security benefits for two-thirds of seniors."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Mike Gallagher’s plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Mike Gallagher's plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Mike Gallagher's plan would cut Social Security benefits for two-thirds of seniors.<br>2. The plan was proposed by Mike Gallagher.<br>3. Mike Gallagher is a U.S. Representative from Maryland.<br>4. The plan was proposed by Mike Gallagher.<br>5. Mike Gallagher is a U.S. Representative from Maryland. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Mike Gallagher's plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| google/gemma-3-1b-it | 1. Mike Gallagher’s plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| google/gemma-3-4b-it | 1. Mike Gallagher’s plan would cut Social Security benefits.<br>2. The Social Security benefits would be cut for two-thirds of seniors. | 2 |
| gpt-3.5-turbo-0125 | 1. Mike Gallagher has a plan.<br>2. Mike Gallagher's plan would cut Social Security benefits for two-thirds of seniors. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Mike Gallagher’s plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Says Mike Gallagher’s plan would cut Social Security benefits for two-thirds of seniors. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Mike Gallagher’s plan "would cut Social Security benefits for two-thirds of seniors." | 1 |

---

## Sample ID: quantemp_70
**Original Claim**: A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A Democrat-sponsored bill proposes a "1,000% gun tax on most firearms." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.”<br>2. The bill was proposed by a Democrat.<br>3. The bill proposes a “1,000% gun tax on most firearms.” | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A Democrat-sponsored bill proposes a "1,000% gun tax on most firearms." | 1 |
| google/gemma-3-1b-it | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| google/gemma-3-4b-it | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| gpt-3.5-turbo-0125 | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| gpt-5.4-nano-2026-03-17 | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A Democrat-sponsored bill proposes a “1,000% gun tax on most firearms.” | 1 |

---

## Sample ID: quantemp_71
**Original Claim**: "Migrants DEMAND $50,000 each to go home, or else …"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Migrants demand $50,000 each to go home, or else. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Migrants DEMAND $50,000 each to go home.<br>2. Otherwise, they will not go home. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Migrants<br>2. DEMAND<br>3. $50,000<br>4. each<br>5. to<br>6. go<br>7. home<br>8. or<br>9. else | 9 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Migrants demand $50,000 each to go home.<br>2. The entity demanding $50,000 each to go home is migrants.<br>3. The entity that migrants demand $50,000 each to go home is … | 3 |
| google/gemma-3-1b-it | 1. Migrants demand $50,000 each to go home.<br>2. Or else… (This is a threat/instruction). | 2 |
| google/gemma-3-4b-it | 1. Migrants DEMAND $50,000 each to go home.<br>2. Migrants DEMAND $50,000 each to go home, or else… | 2 |
| gpt-3.5-turbo-0125 | 1. Migrants demand $50,000 each to go home. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Migrants demand $50,000 each to go home. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Migrants DEMAND $50,000 each to go home, or else … | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "Migrants DEMAND $50,000 each to go home, or else …" | 1 |

---

## Sample ID: quantemp_72
**Original Claim**: Says the 2014-15 Texas budget increases spending by less than the rate of inflation and population growth.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>2. The 2014-15 Texas budget increases spending by less than the rate of population growth. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The 2014-15 Texas budget increases spending.<br>2. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>3. The 2014-15 Texas budget increases spending by less than population growth. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>2. The 2014-15 Texas budget increases spending by less than the rate of population growth. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The 2014-15 Texas budget increased spending.<br>2. The 2014-15 Texas budget increased spending by less than the rate of inflation.<br>3. The 2014-15 Texas budget increased spending by less than the rate of population growth. | 3 |
| google/gemma-3-1b-it | 1. The 2014-15 Texas budget increased spending by less than the rate of inflation and population growth.<br>2. Says the 2014-15 Texas budget increases spending by less than the rate of inflation and population growth. | 2 |
| google/gemma-3-4b-it | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>2. The 2014-15 Texas budget increases spending by less than the rate of population growth. | 2 |
| gpt-3.5-turbo-0125 | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation and population growth. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>2. The 2014-15 Texas budget increases spending by less than the rate of population growth. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The 2014-15 Texas budget increases spending by less than the rate of inflation.<br>2. The 2014-15 Texas budget increases spending by less than the rate of population growth. | 2 |

---

## Sample ID: quantemp_73
**Original Claim**: Viral image shows two children 'paying their respect' to Ukrainian troops amid the ongoing Russia Ukraine troops.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A viral image shows two children paying their respect to Ukrainian troops.<br>2. The image shows two children paying their respect to Ukrainian troops amid the ongoing Russia Ukraine conflict. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A viral image shows two children paying respect to Ukrainian troops.<br>2. The image is being shared amid the ongoing Russia-Ukraine conflict. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The viral image shows two children paying their respect to Ukrainian troops amid the ongoing Russia-Ukraine conflict.<br>2. The conflict between Russia and Ukraine began in 2022.<br>3. The conflict between Russia and Ukraine began in 2022.<br>4. The conflict between Russia and Ukraine began in 2022. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A viral image shows two children paying their respect to Ukrainian troops.<br>2. A viral image shows two children paying their respect to Russian troops.<br>3. A viral image shows two children paying their respect to Russia troops. | 3 |
| google/gemma-3-1b-it | 1. Viral image shows two children paying respect to Ukrainian troops.<br>2. Two children are paying respect to Ukrainian troops.<br>3. The image shows two children. | 3 |
| google/gemma-3-4b-it | 1. A viral image shows two children.<br>2. The two children are paying their respect.<br>3. The children are paying their respect to Ukrainian troops.<br>4. The troops are Ukrainian troops.<br>5. The troops are part of the ongoing Russia Ukraine troops. | 5 |
| gpt-3.5-turbo-0125 | 1. Viral image shows two children 'paying their respect' to Ukrainian troops.<br>2. The ongoing Russia Ukraine conflict involves Ukrainian troops. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The viral image shows two children paying their respect to Ukrainian troops.<br>2. The viral image shows two children paying their respect to Ukrainian troops amid the ongoing Russia Ukraine troops. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Viral image shows two children paying their respect to Ukrainian troops amid the ongoing Russia Ukraine troops. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Viral image shows two children 'paying their respect' to Ukrainian troops amid the ongoing Russia Ukraine troops. | 1 |

---

## Sample ID: quantemp_74
**Original Claim**: “More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. More people have been killed by the COVID vaccines in the last 20 months.<br>2. All other vaccines in the world have not been killed by the COVID vaccines in the last 20 months. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The COVID vaccines have killed more people in the last 20 months than all other vaccines in the world over the last thirty years combined. | 1 |
| google/gemma-3-1b-it | 1. “More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined.” | 1 |
| google/gemma-3-4b-it | 1. More people have been killed in the last 20 months.<br>2. The COVID vaccines were involved in the deaths.<br>3. The deaths occurred in the last 20 months.<br>4. All other vaccines in the world were involved in the deaths.<br>5. The deaths occurred over the last thirty years.<br>6. The deaths occurred combined. | 6 |
| gpt-3.5-turbo-0125 | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. More people have been killed by the COVID vaccines in the last 20 months than all the other vaccines in the world over the last thirty years combined. | 1 |

---

## Sample ID: quantemp_75
**Original Claim**: "It costs $10,000 a year to keep a child in school; it costs $30,000 a year to keep someone in prison."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Keeping a child in school costs $10,000 a year.<br>2. Keeping someone in prison costs $30,000 a year. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| google/gemma-3-1b-it | 1. A child in school costs $10,000 a year.<br>2. A child in school costs $30,000 a year. | 2 |
| google/gemma-3-4b-it | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| gpt-3.5-turbo-0125 | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. It costs $10,000 a year to keep a child in school.<br>2. It costs $30,000 a year to keep someone in prison. | 2 |

---

## Sample ID: quantemp_76
**Original Claim**: The caption with the video claims a six year old girl was raped and buried alive in Hyderabad

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The caption with the video claims a six year old girl was raped and buried alive in Hyderabad. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The caption with the video claims a six-year-old girl was raped.<br>2. The caption with the video claims a six-year-old girl was buried alive.<br>3. The caption with the video claims a six-year-old girl was raped and buried alive. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I can't fulfill this request | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. I can't fulfill this request<br>2. I can't create content that describes the graphic details of a violent crime<br>3. Can I help you with something else? | 3 |
| google/gemma-3-1b-it | 1. The caption with the video claims a six-year-old girl was raped and buried alive in Hyderabad. | 1 |
| google/gemma-3-4b-it | 1. The caption with the video claims a six year old girl was raped.<br>2. The caption with the video claims a six year old girl was buried alive.<br>3. The claim is located in Hyderabad. | 3 |
| gpt-3.5-turbo-0125 | 1. The caption with the video claims a six year old girl was raped and buried alive in Hyderabad. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The caption with the video claims a six year old girl was raped in Hyderabad.<br>2. The caption with the video claims a six year old girl was buried alive in Hyderabad. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The caption with the video claims a six year old girl was raped and buried alive in Hyderabad. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The caption with the video claims a six year old girl was raped and buried alive in Hyderabad. | 1 |

---

## Sample ID: quantemp_77
**Original Claim**: "In 1950, corporations paid $3 in taxes for every $1 by a worker. Today, they pay 22 cents for every $1 by a worker."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents in taxes for every $1 by a worker. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents for every $1 by a worker. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents for every $1 by a worker. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Corporations paid $3 in taxes for every $1 by a worker in 1950.<br>2. Corporations paid 22 cents in taxes for every $1 by a worker today. | 2 |
| google/gemma-3-1b-it | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents for every $1 by a worker. | 2 |
| google/gemma-3-4b-it | 1. In 1950, corporations paid $3 for every $1 by a worker.<br>2. Today, corporations pay 22 cents for every $1 by a worker. | 2 |
| gpt-3.5-turbo-0125 | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents for every $1 by a worker. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In 1950, corporations paid $3 in taxes for every $1 paid in taxes by a worker.<br>2. Today, corporations pay 22 cents in taxes for every $1 paid in taxes by a worker. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. In 1950, corporations paid $3 in taxes for every $1 by a worker.<br>2. Today, corporations pay 22 cents in taxes for every $1 by a worker. | 2 |

---

## Sample ID: quantemp_78
**Original Claim**: Bank of Ghana issues 500 cedi notes

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Bank of Ghana issues 500 cedi notes | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Bank of Ghana issues 500 cedi notes. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Bank of Ghana issues 500 cedi notes.<br>2. The Bank of Ghana is a central bank.<br>3. The Bank of Ghana is located in Accra.<br>4. The Bank of Ghana is a financial institution.<br>5. The Bank of Ghana is headquartered in Accra.<br>6. The Bank of Ghana is a major financial institution in Ghana.<br>7. The Bank of Ghana is a major financial institution in Ghana.<br>8. The Bank of Ghana is a major financial institution in Ghana.<br>9. The Bank of Ghana is a major financial institution in Ghana.<br>10. The Bank of Ghana is a major financial institution in Ghana.<br>11. The Bank of Ghana is a major financial institution in Ghana.<br>12. The Bank of Ghana is a major financial institution in Ghana.<br>13. The Bank of Ghana is a major financial institution in Ghana.<br>14. The Bank of Ghana is a major financial institution in Ghana.<br>15. The Bank of Ghana is a major financial institution in Ghana.<br>16. The Bank of Ghana is a major financial institution in Ghana.<br>17. The Bank of Ghana is a major financial institution in Ghana.<br>18. The Bank of Ghana is a major financial institution in Ghana.<br>19. The Bank of Ghana is a major financial institution in Ghana.<br>20. The Bank of Ghana is a major financial institution in Ghana.<br>21. The Bank of Ghana is a major | 21 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Bank of Ghana issues 500 cedi notes. | 1 |
| google/gemma-3-1b-it | 1. Bank of Ghana issued 500 cedi notes.<br>2. 500 cedi notes were issued by Bank of Ghana. | 2 |
| google/gemma-3-4b-it | 1. The Bank of Ghana issued 500 cedi notes. | 1 |
| gpt-3.5-turbo-0125 | 1. Bank of Ghana issued 500 cedi notes. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Bank of Ghana issues 500 cedi notes. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Bank of Ghana issues 500 cedi notes. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Bank of Ghana issues 500 cedi notes | 1 |

---

## Sample ID: quantemp_79
**Original Claim**: Says over 90 percent of Travis County’s eligible residents have registered to vote.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Travis County’s eligible residents have registered to vote.<br>2. Over 90 percent of Travis County’s eligible residents have registered to vote. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Travis County, Texas<br>2. over 90 percent of eligible residents have registered to vote. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Travis County is eligible for voting registration.<br>2. Over 90 percent of Travis County's eligible residents have registered to vote. | 2 |
| google/gemma-3-1b-it | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |
| google/gemma-3-4b-it | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |
| gpt-3.5-turbo-0125 | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Please provide the claim text to break down into atomic facts. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Over 90 percent of Travis County’s eligible residents have registered to vote. | 1 |

---

## Sample ID: quantemp_80
**Original Claim**: A 1922 report disproves human-caused global warming

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A 1922 report disproves human-caused global warming. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A 1922 report disproves human-caused global warming. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A 1922 report disproves human-caused global warming. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A report was published in 1922.<br>2. The report disproves human-caused global warming. | 2 |
| google/gemma-3-1b-it | 1. A 1922 report disproves human-caused global warming. | 1 |
| google/gemma-3-4b-it | 1. A 1922 report disproves human-caused global warming. | 1 |
| gpt-3.5-turbo-0125 | 1. A 1922 report disproves human-caused global warming. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A 1922 report exists.<br>2. The 1922 report disproves human-caused global warming. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A 1922 report disproves human-caused global warming. | 1 |

---

## Sample ID: quantemp_81
**Original Claim**: "For the first time in 35 years, we have more businesses closing than starting."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. For the first time in 35 years, more businesses closed than started. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The number of businesses closing has increased.<br>2. The number of businesses starting has decreased. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States has more businesses closing than starting.<br>2. The United States has more businesses closing than starting for the first time in 35 years.<br>3. The United States has more businesses closing than starting for the first time in 35 years. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The year was 1987.<br>2. Businesses were closing more than businesses were starting. | 2 |
| google/gemma-3-1b-it | 1. We have more businesses closing than starting.<br>2. For the first time in 35 years, we have more businesses closing than starting. | 2 |
| google/gemma-3-4b-it | 1. For the first time in 35 years, there have been more businesses closing.<br>2. There have been more businesses closing.<br>3. For the first time in 35 years, there have been more businesses starting.<br>4. There have been more businesses starting.<br>5. This has occurred for the first time in 35 years. | 5 |
| gpt-3.5-turbo-0125 | 1. For the first time in 35 years, there are more businesses closing than starting. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. For the first time in 35 years, there are more businesses closing than starting. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. For the first time in 35 years, we have more businesses closing than starting. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. For the first time in 35 years, we have more businesses closing than starting. | 1 |

---

## Sample ID: quantemp_82
**Original Claim**: Altered photo falsely links judge to Epstein partner Ghislaine Maxwell

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Altered photo is falsely linked to judge.<br>2. Altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Altered photo falsely links judge to Epstein partner Ghislaine Maxwell.<br>2. Ghislaine Maxwell is a British socialite and convicted sex offender.<br>3. Ghislaine Maxwell was convicted of sex trafficking and abuse.<br>4. Ghislaine Maxwell was sentenced to prison for sex trafficking and abuse.<br>5. Ghislaine Maxwell was sentenced to prison for sex trafficking and abuse in 2021.<br>6. Ghislaine Maxwell was sentenced to prison for sex trafficking and abuse in 2021 in the United States.<br>7. Ghislaine Maxwell was sentenced to prison for sex trafficking and abuse in the United States in 2021. | 7 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Altered photo falsely links Ghislaine Maxwell to Epstein.<br>2. Altered photo falsely links judge to Ghislaine Maxwell.<br>3. Altered photo falsely links Epstein's partner to Ghislaine Maxwell. | 3 |
| google/gemma-3-1b-it | 1. Altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 1 |
| google/gemma-3-4b-it | 1. An altered photo links judge to Epstein partner Ghislaine Maxwell. | 1 |
| gpt-3.5-turbo-0125 | 1. The altered photo falsely links a judge to Epstein partner Ghislaine Maxwell. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. An altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Altered photo falsely links judge to Epstein partner Ghislaine Maxwell. | 1 |

---

## Sample ID: quantemp_83
**Original Claim**: The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein, lipids, sucrose, and salts.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. Lipids<br>3. Sucrose<br>4. Salts | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| google/gemma-3-1b-it | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains salts. | 3 |
| google/gemma-3-4b-it | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| gpt-3.5-turbo-0125 | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |
| gpt-5.4-mini-2026-03-17 | 1. The Pfizer/BioNTech vaccine contains mRNA encoding the SARS-CoV-2 spike protein.<br>2. The Pfizer/BioNTech vaccine contains lipids.<br>3. The Pfizer/BioNTech vaccine contains sucrose.<br>4. The Pfizer/BioNTech vaccine contains salts. | 4 |

---

## Sample ID: quantemp_84
**Original Claim**: A story of a leopard that went under an elephant’s trunk and a fable of a fight that erupted between two elephants in Kerala

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A story of a leopard that went under an elephant’s trunk occurred in Kerala.<br>2. A fable of a fight that erupted between two elephants occurred in Kerala. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A story of a leopard that went under an elephant’s trunk.<br>2. A fable of a fight that erupted between two elephants in Kerala. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A story of a leopard went under an elephant’s trunk.<br>2. A fable of a fight erupted between two elephants in Kerala. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A leopard went under an elephant's trunk.<br>2. A story about a leopard going under an elephant's trunk is a fable.<br>3. A fable about a leopard going under an elephant's trunk is set in Kerala.<br>4. A fight erupted between two elephants in Kerala. | 4 |
| google/gemma-3-1b-it | 1. A story of a leopard that went under an elephant’s trunk.<br>2. A fable of a fight that erupted between two elephants in Kerala. | 2 |
| google/gemma-3-4b-it | 1. There is a story of a leopard.<br>2. The leopard went under an elephant’s trunk.<br>3. There is a fable.<br>4. The fable is of a fight.<br>5. The fight erupted between two elephants.<br>6. The location is Kerala. | 6 |
| gpt-3.5-turbo-0125 | 1. A story of a leopard that went under an elephant’s trunk occurred in Kerala.<br>2. A fable of a fight that erupted between two elephants occurred in Kerala. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A story of a leopard that went under an elephant’s trunk exists.<br>2. A fable of a fight that erupted between two elephants in Kerala exists. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A story of a leopard went under an elephant’s trunk.<br>2. A fable of a fight erupted between two elephants in Kerala. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A story of a leopard went under an elephant’s trunk.<br>2. A fable of a fight erupted between two elephants in Kerala. | 2 |

---

## Sample ID: quantemp_85
**Original Claim**: Drinking cold water closes four heart veins and cause heart attacks

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Drinking cold water can close four heart veins.<br>2. Drinking cold water can cause heart attacks. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Cold water is associated with closing four heart veins.<br>2. Cold water causes heart attacks. | 2 |
| google/gemma-3-1b-it | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| google/gemma-3-4b-it | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| gpt-3.5-turbo-0125 | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Drinking cold water closes four heart veins.<br>2. Drinking cold water causes heart attacks. | 2 |

---

## Sample ID: quantemp_86
**Original Claim**: On Sandra Day O'Connor: "I think one reason she was a good judge is she had no judicial experience" before she joined the Supreme Court.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. On Sandra Day O'Connor: "I think one reason she was a good judge is she had no judicial experience" before she joined the Supreme Court. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Sandra Day O'Connor joined the Supreme Court.<br>2. Sandra Day O'Connor was a good judge.<br>3. Sandra Day O'Connor had no judicial experience before joining the Supreme Court. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Sandra Day O'Connor was a judge.<br>2. She had no judicial experience.<br>3. She joined the Supreme Court. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Sandra Day O'Connor was a judge before she joined the Supreme Court.<br>2. She had no judicial experience before she joined the Supreme Court.<br>3. She thinks one reason she was a good judge is she had no judicial experience. | 3 |
| google/gemma-3-1b-it | 1. Sandra Day O’Connor was a judge before joining the Supreme Court.<br>2. “I think she was a good judge” was a statement made by Sandra Day O’Connor before she joined the Supreme Court. | 2 |
| google/gemma-3-4b-it | 1. On Sandra Day O'Connor, it was stated: "I think one reason she was a good judge is she had no judicial experience" before she joined the Supreme Court. | 1 |
| gpt-3.5-turbo-0125 | 1. Sandra Day O'Connor had no judicial experience before she joined the Supreme Court.<br>2. Sandra Day O'Connor was a good judge. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Sandra Day O'Connor had no judicial experience before she joined the Supreme Court.<br>2. One reason Sandra Day O'Connor was a good judge is that Sandra Day O'Connor had no judicial experience before she joined the Supreme Court. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. On Sandra Day O'Connor, “I think one reason she was a good judge is she had no judicial experience” was stated before she joined the Supreme Court. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. On Sandra Day O'Connor, "I think one reason Sandra Day O'Connor was a good judge is Sandra Day O'Connor had no judicial experience" before Sandra Day O'Connor joined the Supreme Court. | 1 |

---

## Sample ID: quantemp_87
**Original Claim**: Says NC Senate leader "expressed disdain" for the NC House budget vote on Sept. 11.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The NC Senate leader expressed disdain for the NC House budget vote on Sept. 11. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. NC Senate leader expressed disdain for the NC House budget vote on Sept. 11. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The NC Senate leader expressed disdain for the NC House budget vote on Sept. 11.<br>2. The NC Senate leader voted against the NC House budget vote on Sept. 11.<br>3. The NC Senate leader voted against the NC House budget vote on September 11. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The NC Senate leader expressed disdain for the NC House budget vote on Sept. 11. | 1 |
| google/gemma-3-1b-it | 1. NC Senate leader expressed disdain for the NC House budget vote on Sept. 11. | 1 |
| google/gemma-3-4b-it | 1. The NC Senate leader expressed disdain for the NC House budget vote.<br>2. The NC House budget vote occurred on Sept. 11. | 2 |
| gpt-3.5-turbo-0125 | 1. NC Senate leader "expressed disdain" for the NC House budget vote on Sept. 11. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. NC Senate leader expressed disdain for the NC House budget vote on Sept. 11. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. NC Senate leader "expressed disdain" for the NC House budget vote on Sept. 11. | 1 |

---

## Sample ID: quantemp_88
**Original Claim**: Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. The lawsuit was over a decision by Sheriff David A. Clarke Jr.<br>3. Sheriff David A. Clarke Jr. used "untrained corrections officers" rather than deputies to patrol the lakefront. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. Milwaukee County taxpayers settled a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront.<br>2. The decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront was made in Milwaukee County.<br>3. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over the decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" to patrol the lakefront.<br>2. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 2 |
| google/gemma-3-1b-it | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. A decision by Sheriff David A. Clarke Jr. to use “untrained corrections officers” resulted in a lawsuit.<br>3. The lawsuit involved a decision by Sheriff David A. Clarke Jr. to use “untrained corrections officers” rather than deputies. | 3 |
| google/gemma-3-4b-it | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. The lawsuit was over a decision by Sheriff David A. Clarke Jr.<br>3. Sheriff David A. Clarke Jr. used “untrained corrections officers” rather than deputies to patrol the lakefront. | 3 |
| gpt-3.5-turbo-0125 | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. The lawsuit was over a decision by Sheriff David A. Clarke Jr.<br>3. The decision was to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit.<br>2. The lawsuit was over a decision by Sheriff David A. Clarke Jr.<br>3. Sheriff David A. Clarke Jr. used "untrained corrections officers" rather than deputies to patrol the lakefront. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Milwaukee County taxpayers paid $370,000 to settle a lawsuit over a decision by Sheriff David A. Clarke Jr. to use "untrained corrections officers" rather than deputies to patrol the lakefront. | 1 |

---

## Sample ID: quantemp_89
**Original Claim**: "At $587 apiece, USA would need to bring home about 33.1 BILLION gold medals to pay off our national debt."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. At $587 apiece, the USA would need to bring home about 33.1 BILLION gold medals to pay off its national debt. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. USA would need to bring home about 33.1 billion gold medals to pay off its national debt.<br>2. At $587 apiece, USA would need to bring home about 33.1 billion gold medals to pay off its national debt. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States would need to bring home about 33.1 billion gold medals to pay off its national debt.<br>2. The national debt of the United States is approximately 33.1 billion gold medals.<br>3. The national debt of the United States is approximately 33.1 billion gold medals. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The United States would need to bring home 33.1 billion gold medals at $587 apiece to pay off its national debt. | 1 |
| google/gemma-3-1b-it | 1. USA would need to bring home about 33.1 billion gold medals to pay off our national debt. | 1 |
| google/gemma-3-4b-it | 1. At $587 apiece, USA would need to bring home about 33.1 BILLION gold medals.<br>2. USA would need to bring home about 33.1 BILLION gold medals to pay off our national debt. | 2 |
| gpt-3.5-turbo-0125 | 1. USA would need to bring home about 33.1 BILLION gold medals to pay off our national debt. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. At $587 apiece, USA would need to bring home about 33.1 BILLION gold medals to pay off our national debt. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. At $587 apiece, USA would need to bring home about 33.1 BILLION gold medals to pay off our national debt. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. At $587 apiece, USA would need to bring home about 33.1 BILLION gold medals to pay off USA's national debt. | 1 |

---

## Sample ID: quantemp_90
**Original Claim**: “At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. At a top robotics company in Japan this week, four robots were being developed for military applications.<br>2. These robots killed 29 humans in the lab. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab.<br>2. The company is located in Japan.<br>3. The company is a top robotics company.<br>4. The company is located in Japan.<br>5. The company is a top robotics company.<br>6. The company is located in Japan.<br>7. The company is a top robotics company.<br>8. The company is located in Japan.<br>9. The company is a top robotics company.<br>10. The company is located in Japan.<br>11. The company is a top robotics company.<br>12. The company is located in Japan.<br>13. The company is a top robotics company.<br>14. The company is located in Japan.<br>15. The company is a top robotics company.<br>16. The company is located in Japan.<br>17. The company is a top robotics company.<br>18. The company is located in Japan.<br>19. The company is a top robotics company.<br>20. The company is located in Japan.<br>21. The company is a top robotics company. | 21 |
| meta-llama/Llama-3.2-3B-Instruct | 1. At a top robotics company in Japan, four robots being developed for military applications killed 29 humans in the lab. | 1 |
| google/gemma-3-1b-it | 1. “At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab.” | 1 |
| google/gemma-3-4b-it | 1. At a top robotics company in Japan this week, four robots were being developed for military applications.<br>2. Four robots being developed for military applications killed 29 humans in the lab. | 2 |
| gpt-3.5-turbo-0125 | 1. Four robots being developed for military applications killed 29 humans in the lab at a top robotics company in Japan this week. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Four robots being developed for military applications killed 29 humans in the lab at a top robotics company in Japan this week. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. At a top robotics company in Japan this week, four robots being developed for military applications killed 29 humans in the lab. | 1 |

---

## Sample ID: quantemp_91
**Original Claim**: The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention, which was thereafter popularly known as the "Klanbake."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The 1924 Democratic National Convention was thereafter popularly known as the "Klanbake". | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The march and rally was thereafter popularly known as the "Klanbake." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The Ku Klux Klan held a march and rally at the Democratic National Convention.<br>3. The Ku Klux Klan held a march and rally at the Democratic National Convention in 1924. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The 1924 Democratic National Convention was popularly known as the "Klanbake". | 2 |
| google/gemma-3-1b-it | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The Klanbake was popularly known as the 1924 Democratic National Convention. | 2 |
| google/gemma-3-4b-it | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The 1924 Democratic National Convention was thereafter popularly known as the "Klanbake." | 2 |
| gpt-3.5-turbo-0125 | 1. The Ku Klux Klan held a march and rally at the 1924 Democratic National Convention.<br>2. The 1924 Democratic National Convention was popularly known as the "Klanbake." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The Ku Klux Klan held a march at the 1924 Democratic National Convention.<br>2. The Ku Klux Klan held a rally at the 1924 Democratic National Convention.<br>3. The 1924 Democratic National Convention was thereafter popularly known as the "Klanbake." | 3 |
| gpt-5.4-nano-2026-03-17 | 1. The Ku Klux Klan held a march at the 1924 Democratic National Convention.<br>2. The Ku Klux Klan held a rally at the 1924 Democratic National Convention.<br>3. The 1924 Democratic National Convention was thereafter popularly known as the "Klanbake." | 3 |
| gpt-5.4-mini-2026-03-17 | 1. The Ku Klux Klan held a march at the 1924 Democratic National Convention.<br>2. The Ku Klux Klan held a rally at the 1924 Democratic National Convention.<br>3. The 1924 Democratic National Convention was thereafter popularly known as the "Klanbake." | 3 |

---

## Sample ID: quantemp_92
**Original Claim**: In den „letzten vier Monaten“ seien in Deutschland nur 427 Menschen an Covid-19 gestorben, aber zehntausende an Krebs oder Herz-Kreislauf-Krankheiten.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In the last four months in Germany, only 427 people died of Covid-19.<br>2. In the last four months in Germany, ten thousand people died of cancer or heart and circulatory diseases. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In the last four months, 427 people in Germany have died from Covid-19.<br>2. In the last four months, tens of thousands of people in Germany have died from cancer or heart-circulation diseases. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In den letzten vier Monaten seien in Deutschland nur 427 Menschen an COVID-19 gestorben.<br>2. Zehntausende an Krebs oder Herz-Kreislauf-Krankheiten sind in Deutschland jedoch zehntausende an COVID-19 gestorben. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. In the last four months, in Germany, 427 people died from Covid-19.<br>2. In the last four months, in Germany, 10,000 people died from cancer or heart and circulatory diseases. | 2 |
| google/gemma-3-1b-it | 1. In den letzten vier Monaten waren 427 Menschen in Deutschland an Covid-19 gestorben.<br>2. Thousands of people in Germany died from cancer or heart-related illnesses. | 2 |
| google/gemma-3-4b-it | 1. In the “last four months”, 427 people died from Covid-19 in Germany.<br>2. Zehntausende people died from cancer or heart-circulatory diseases in Germany. | 2 |
| gpt-3.5-turbo-0125 | 1. In the last four months, only 427 people have died from Covid-19 in Germany.<br>2. In the last four months, tens of thousands of people have died from cancer or cardiovascular diseases in Germany. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In den „letzten vier Monaten“ sind in Deutschland nur 427 Menschen an Covid-19 gestorben.<br>2. In den „letzten vier Monaten“ sind in Deutschland zehntausende Menschen an Krebs gestorben.<br>3. In den „letzten vier Monaten“ sind in Deutschland zehntausende Menschen an Herz-Kreislauf-Krankheiten gestorben. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. In den „letzten vier Monaten“ seien in Deutschland nur 427 Menschen an Covid-19 gestorben.<br>2. In den „letzten vier Monaten“ seien in Deutschland zehntausende an Krebs oder Herz-Kreislauf-Krankheiten gestorben. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. In den „letzten vier Monaten“ seien in Deutschland nur 427 Menschen an Covid-19 gestorben.<br>2. In den „letzten vier Monaten“ seien in Deutschland zehntausende an Krebs gestorben.<br>3. In den „letzten vier Monaten“ seien in Deutschland zehntausende an Herz-Kreislauf-Krankheiten gestorben. | 3 |

---

## Sample ID: quantemp_93
**Original Claim**: "For the last 10 years, our economy has grown at less than 2 percent on average every single year for 10 years. We have not had a decade like that in a century in America."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. For the last 10 years, the economy has grown at less than 2 percent on average every single year.<br>2. For the last 10 years, the economy has grown at less than 2 percent on average every single year for 10 years.<br>3. America has not had a decade like that in a century. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. For the last 10 years, our economy has grown at less than 2 percent on average every single year.<br>2. We have not had a decade like that in a century in America. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The last 10 years have seen an average annual economic growth of less than 2 percent.<br>2. The economy has grown at less than 2 percent on average every single year for 10 years.<br>3. The economy has grown at less than 2 percent on average for 10 years.<br>4. The economy has grown at less than 2 percent on average for 10 years.<br>5. The economy has grown at less than 2 percent on average for 10 years. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The economy of America has grown at less than 2 percent on average for 10 years.<br>2. The economy of America has not had a decade of less than 2 percent growth for 10 years.<br>3. For the last 10 years, the economy of America has grown at less than 2 percent on average every single year. | 3 |
| google/gemma-3-1b-it | 1. For the last 10 years, our economy has grown at less than 2 percent on average every single year for 10 years.<br>2. We have not had a decade like that in a century in America. | 2 |
| google/gemma-3-4b-it | 1. For the last 10 years, the economy has grown at less than 2 percent on average every single year for 10 years.<br>2. We have not had a decade like that in America. | 2 |
| gpt-3.5-turbo-0125 | 1. The economy has grown at less than 2 percent on average every single year for the last 10 years.<br>2. The economy has not had a decade like the last 10 years in a century in America. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. For the last 10 years, the economy has grown at less than 2 percent on average every single year for 10 years.<br>2. The United States has not had a decade like that in a century. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. For the last 10 years, our economy has grown at less than 2 percent on average every single year for 10 years.<br>2. We have not had a decade like that in a century in America. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. For the last 10 years, our economy has grown at less than 2 percent on average every single year for 10 years.<br>2. We have not had a decade like that in a century in America. | 2 |

---

## Sample ID: quantemp_94
**Original Claim**: "I have already saved more than $700 million when I got involved in the negotiation on the F-35."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. I saved more than $700 million when I got involved in the negotiation on the F-35. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The person has saved more than $700 million.<br>2. The person got involved in the negotiation on the F-35. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I have already saved more than $700 million when I got involved in the negotiation on the F-35. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The person involved in the negotiation on the F-35 has already saved more than $700 million.<br>2. The person involved in the negotiation on the F-35 is a male.<br>3. The person involved in the negotiation on the F-35 is female.<br>4. The person involved in the negotiation on the F-35 is they.<br>5. The person involved in the negotiation on the F-35 is that. | 5 |
| google/gemma-3-1b-it | 1. I have saved more than $700 million.<br>2. I got involved in the negotiation on the F-35. | 2 |
| google/gemma-3-4b-it | 1. I have already saved more than $700 million.<br>2. I got involved in the negotiation on the F-35. | 2 |
| gpt-3.5-turbo-0125 | 1. The speaker saved more than $700 million when they got involved in the negotiation on the F-35. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. I have already saved more than $700 million when I got involved in the negotiation on the F-35. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "I have already saved more than $700 million when I got involved in the negotiation on the F-35." | 1 |

---

## Sample ID: quantemp_95
**Original Claim**: “This week liberal Bill White faced an ethics complaint about more than $83,000 he failed to report to the state Ethics Commission.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This week liberal Bill White faced an ethics complaint.<br>2. Liberal Bill White faced an ethics complaint about more than $83,000.<br>3. Liberal Bill White failed to report more than $83,000 to the state Ethics Commission. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Bill White faced an ethics complaint.<br>2. The complaint involved more than $83,000.<br>3. Bill White failed to report the money to the state Ethics Commission. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. This week liberal Bill White faced an ethics complaint about more than $83,000 he failed to report to the state Ethics Commission.<br>2. Bill White is a liberal politician.<br>3. Bill White is a politician.<br>4. Bill White is a politician.<br>5. Bill White is a politician.<br>6. Bill White is a politician.<br>7. Bill White is a politician.<br>8. Bill White is a politician.<br>9. Bill White is a politician.<br>10. Bill White is a politician.<br>11. Bill White is a politician.<br>12. Bill White is a politician.<br>13. Bill White is a politician.<br>14. Bill White is a politician.<br>15. Bill White is a politician.<br>16. Bill White is a politician.<br>17. Bill White is a politician.<br>18. Bill White is a politician.<br>19. Bill White is a politician.<br>20. Bill White is a politician.<br>21. Bill White is a politician.<br>22. Bill White is a politician.<br>23. Bill White is a politician.<br>24. Bill White is a politician.<br>25. Bill White is a politician.<br>26. Bill White is a politician.<br>27. Bill White is a politician.<br>28. Bill White is a politician.<br>29. Bill White is a politician.<br>30. Bill White is a politician.<br>31. Bill White is a politician.<br>32. Bill White is a politician.<br>33. Bill White is a politician.<br>34. Bill White is | 34 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Bill White faced an ethics complaint about more than $83,000 he failed to report to the state Ethics Commission this week.<br>2. The state Ethics Commission is located in Rhode Island.<br>3. Bill White is a liberal. | 3 |
| google/gemma-3-1b-it | 1. “This week liberal Bill White faced an ethics complaint about more than $83,000.”<br>2. “Bill White failed to report $83,000 to the state Ethics Commission.” | 2 |
| google/gemma-3-4b-it | 1. This week liberal Bill White faced an ethics complaint.<br>2. The ethics complaint was about more than $83,000.<br>3. Bill White failed to report more than $83,000 to the state Ethics Commission.<br>4. The state Ethics Commission is a state entity.<br>5. Bill White is a liberal. | 5 |
| gpt-3.5-turbo-0125 | 1. Bill White faced an ethics complaint this week.<br>2. Bill White failed to report more than $83,000 to the state Ethics Commission. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. This week liberal Bill White faced an ethics complaint about more than $83,000 he failed to report to the state Ethics Commission. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. This week liberal Bill White faced an ethics complaint about more than $83,000 Bill White failed to report to the state Ethics Commission. | 1 |

---

## Sample ID: quantemp_96
**Original Claim**: Some 700-plus undocumented migrants, including sex offenders, were apprehended by the U.S. Border Patrol overnight.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. Some sex offenders were apprehended by the U.S. Border Patrol overnight. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Some undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. The apprehensions included some sex offenders. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The U.S. Border Patrol apprehended some 700-plus undocumented migrants, including sex offenders.<br>2. Some 700-plus undocumented migrants, including sex offenders, were apprehended by the U.S. Border Patrol overnight.<br>3. The U.S. Border Patrol apprehended some 700-plus undocumented migrants, including sex offenders.<br>4. Some 700-plus undocumented migrants, including sex offenders, were apprehended by the U.S. Border Patrol overnight. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The U.S. Border Patrol apprehended some 700-plus undocumented migrants overnight.<br>2. The U.S. Border Patrol apprehended some undocumented migrants who were sex offenders overnight. | 2 |
| google/gemma-3-1b-it | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight. | 1 |
| google/gemma-3-4b-it | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. The apprehended migrants are undocumented migrants.<br>3. The apprehended migrants include sex offenders.<br>4. The U.S. Border Patrol apprehended the migrants overnight. | 4 |
| gpt-3.5-turbo-0125 | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. Some 700-plus undocumented migrants, including sex offenders, were apprehended by the U.S. Border Patrol overnight. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. Some sex offenders were apprehended by the U.S. Border Patrol overnight. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Some 700-plus undocumented migrants, including sex offenders, were apprehended by the U.S. Border Patrol overnight. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Some 700-plus undocumented migrants were apprehended by the U.S. Border Patrol overnight.<br>2. Some 700-plus undocumented migrants included sex offenders. | 2 |

---

## Sample ID: quantemp_97
**Original Claim**: The viral image shows Hindus attacked in Bangladesh in 2022

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The viral image shows Hindus in Bangladesh.<br>2. The viral image shows Hindus attacked in Bangladesh in 2022. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The viral image shows Hindus attacked in Bangladesh in 2022.<br>2. The image shows Hindus attacked in Bangladesh in 2022.<br>3. The image shows Hindus attacked in Bangladesh in 2022. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The image is of Hindus.<br>2. The image shows Hindus attacked in Bangladesh in 2022. | 2 |
| google/gemma-3-1b-it | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |
| google/gemma-3-4b-it | 1. The viral image shows Hindus attacked in Bangladesh.<br>2. The attack occurred in Bangladesh in 2022. | 2 |
| gpt-3.5-turbo-0125 | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The viral image shows Hindus attacked in Bangladesh in 2022. | 1 |

---

## Sample ID: quantemp_98
**Original Claim**: No, photo shows India-made chopper, not one built in Tanzania

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The photo shows an India-made chopper.<br>2. The photo does not show a chopper built in Tanzania. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The photo shows an India-made chopper.<br>2. The photo does not show a chopper built in Tanzania. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. India is a country.<br>2. The photo shows a chopper built in India.<br>3. The photo shows a chopper built in Tanzania. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The photo shows an India-made chopper.<br>2. The photo shows a chopper built in Tanzania. | 2 |
| google/gemma-3-1b-it | 1. Photo depicts India-made chopper.<br>2. India-made chopper is not one built in Tanzania. | 2 |
| google/gemma-3-4b-it | 1. The photo shows India-made chopper.<br>2. The photo does not show one built in Tanzania. | 2 |
| gpt-3.5-turbo-0125 | 1. The photo shows an India-made chopper.<br>2. The photo does not show a chopper built in Tanzania. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The photo shows an India-made chopper.<br>2. The photo does not show a chopper built in Tanzania. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. No, photo shows India-made chopper.<br>2. No, photo shows not one built in Tanzania. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The photo shows India-made chopper.<br>2. The photo does not show one built in Tanzania. | 2 |

---

## Sample ID: quantemp_99
**Original Claim**: Former President Barack Obama took 30 million documents, many of them classified, to Chicago upon leaving the White House.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Former President Barack Obama took 30 million documents to Chicago upon leaving the White House.<br>2. Many of the documents taken by former President Barack Obama to Chicago upon leaving the White House were classified. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Former President Barack Obama left the White House.<br>2. 30 million documents were taken from the White House.<br>3. Many of the documents were classified. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Former President Barack Obama took 30 million documents, many of them classified, to Chicago upon leaving the White House. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Former President Barack Obama took 30 million documents, many of them classified, to Chicago.<br>2. Former President Barack Obama took documents, many of them classified, to the White House.<br>3. Former President Barack Obama took documents, many of them classified, from the White House to Chicago. | 3 |
| google/gemma-3-1b-it | 1. Former President Barack Obama took 30 million documents.<br>2. Many of the documents were classified.<br>3. The documents were taken to Chicago by Former President Barack Obama.<br>4. The documents were classified. | 4 |
| google/gemma-3-4b-it | 1. Former President Barack Obama took 30 million documents to Chicago.<br>2. The documents were many of them classified.<br>3. The documents were taken upon leaving the White House. | 3 |
| gpt-3.5-turbo-0125 | 1. Former President Barack Obama took 30 million documents to Chicago upon leaving the White House.<br>2. Many of the documents taken by Former President Barack Obama to Chicago upon leaving the White House were classified. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Former President Barack Obama took 30 million documents to Chicago upon leaving the White House.<br>2. Many of the 30 million documents that Former President Barack Obama took to Chicago upon leaving the White House were classified. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Former President Barack Obama took 30 million documents to Chicago upon leaving the White House.<br>2. Former President Barack Obama took many of the 30 million documents classified to Chicago upon leaving the White House. | 2 |

---

## Sample ID: quantemp_100
**Original Claim**: Post claims that a temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A temple priest was brutally attacked in Vrindavan, Matura.<br>2. The attack on the temple priest occurred in Vrindavan, Matura.<br>3. The attackers were two Bangladeshi Muslims. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A temple priest was brutally attacked.<br>2. The attack occurred in Vrindavan.<br>3. The attacker was two Bangladeshi Muslims. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan.<br>2. The temple priest was brutally attacked by two Bangladeshi Muslims in Matura.<br>3. The temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan.<br>4. The temple priest was brutally attacked by two Bangladeshi Muslims in Matura. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A temple priest was attacked by two Bangladeshi Muslims in Vrindavan.<br>2. The temple priest was attacked by two Muslims in Vrindavan.<br>3. Two Bangladeshi Muslims attacked the temple priest in Vrindavan.<br>4. Two Muslims attacked the temple priest in Vrindavan. | 4 |
| google/gemma-3-1b-it | 1. A temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura. | 1 |
| google/gemma-3-4b-it | 1. A temple priest was brutally attacked.<br>2. The attacker was two Bangladeshi Muslims.<br>3. The attack occurred in Vrindavan.<br>4. The attack occurred in Matura. | 4 |
| gpt-3.5-turbo-0125 | 1. A temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura.<br>2. Post claims that a temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A post claims that a temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Post claims that a temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Post claims that a temple priest was brutally attacked by two Bangladeshi Muslims in Vrindavan, Matura. | 1 |

---

## Sample ID: quantemp_101
**Original Claim**: In the UK on 1 July 2021, 66% had had their first vaccination, 49% had had their second, and there were 27,989 new cases of Covid-19.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second vaccination.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. On 1 July 2021, 66% of people in the UK had their first vaccination.<br>2. On 1 July 2021, 49% of people in the UK had their second vaccination.<br>3. On 1 July 2021, there were 27,989 new cases of Covid-19 in the UK. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The UK had 66% of its population vaccinated on 1 July 2021.<br>2. 49% of the UK population had had their second vaccination on 1 July 2021.<br>3. 27,989 new cases of Covid-19 occurred in the UK on 1 July 2021. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The first vaccination was administered in the UK on 1 July 2021 to 66% of the population.<br>2. The second vaccination was administered in the UK on 1 July 2021 to 49% of the population.<br>3. There were 27,989 new cases of Covid-19 in the UK on 1 July 2021. | 3 |
| google/gemma-3-1b-it | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second vaccination.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |
| google/gemma-3-4b-it | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second.<br>3. There were 27,989 new cases of Covid-19. | 3 |
| gpt-3.5-turbo-0125 | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second vaccination.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second vaccination.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. In the UK on 1 July 2021, 66% had had their first vaccination.<br>2. In the UK on 1 July 2021, 49% had had their second vaccination.<br>3. In the UK on 1 July 2021, there were 27,989 new cases of Covid-19. | 3 |

---

## Sample ID: quantemp_102
**Original Claim**: CDC said cigarette smoking doesn't cause cancer in 1958

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. CDC said cigarette smoking doesn't cause cancer in 1958 | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The CDC said cigarette smoking doesn't cause cancer in 1958. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Centers for Disease Control and Prevention (CDC) said cigarette smoking doesn't cause cancer in 1958.<br>2. The statement is a claim.<br>3. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>4. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>5. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>6. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>7. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>8. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>9. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>10. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>11. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>12. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>13. The claim is about the CDC saying that cigarette smoking doesn't cause cancer in 1958.<br>14. The claim is about the | 14 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Centers for Disease Control and Prevention (CDC) made the statement that cigarette smoking does not cause cancer in 1958. | 1 |
| google/gemma-3-1b-it | 1. CDC stated cigarette smoking does not cause cancer in 1958. | 1 |
| google/gemma-3-4b-it | 1. The CDC said cigarette smoking doesn't cause cancer in 1958. | 1 |
| gpt-3.5-turbo-0125 | 1. CDC said cigarette smoking doesn't cause cancer in 1958. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. CDC said cigarette smoking doesn't cause cancer in 1958. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. CDC said cigarette smoking doesn't cause cancer in 1958. | 1 |

---

## Sample ID: quantemp_103
**Original Claim**: "You (Hillary Clinton) get a subpoena, and after getting the subpoena you delete 33,000 emails."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. You get a subpoena (Hillary Clinton).<br>2. Hillary Clinton gets a subpoena.<br>3. After getting the subpoena, Hillary Clinton deletes 33,000 emails. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Hillary Clinton received a subpoena.<br>2. After receiving the subpoena, Hillary Clinton deleted 33,000 emails. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. You<br>2. Hillary Clinton<br>3. gets<br>4. a<br>5. subpoena<br>6. and<br>7. after<br>8. getting<br>9. the<br>10. subpoena<br>11. you<br>12. delete<br>13. 33,000<br>14. emails | 14 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Hillary Clinton received a subpoena.<br>2. After receiving a subpoena, Hillary Clinton deleted 33,000 emails. | 2 |
| google/gemma-3-1b-it | 1. Hillary Clinton received a subpoena.<br>2. A subpoena led to the deletion of 33,000 emails. | 2 |
| google/gemma-3-4b-it | 1. Hillary Clinton gets a subpoena.<br>2. After getting the subpoena, Hillary Clinton deletes 33,000 emails. | 2 |
| gpt-3.5-turbo-0125 | 1. Hillary Clinton got a subpoena.<br>2. After getting the subpoena, Hillary Clinton deleted 33,000 emails. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Hillary Clinton got a subpoena.<br>2. After Hillary Clinton got the subpoena, Hillary Clinton deleted 33,000 emails. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Hillary Clinton gets a subpoena.<br>2. After Hillary Clinton gets the subpoena, Hillary Clinton deletes 33,000 emails. | 2 |

---

## Sample ID: quantemp_104
**Original Claim**: The elderly will now be given P25,000 as they reach the ages of 80, 85, 90 and 95, under an amended Centenarians Act of 2016 or Republic Act 10868.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The elderly will now be given P25,000 as they reach the ages of 80, 85, 90 and 95.<br>2. The P25,000 is given to the elderly as they reach the ages of 80, 85, 90 and 95.<br>3. The amended Centenarians Act of 2016 or Republic Act 10868 provides for the elderly to be given P25,000 as they reach the ages of 80, 85, 90 and 95. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The elderly will now be given P25,000.<br>2. The elderly will now be given P25,000 as they reach the ages of 80, 85, 90, and 95.<br>3. The elderly will now be given P25,000 under an amended Centenarians Act of 2016 or Republic Act 10868. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The elderly will be given P25,000 as they reach the ages of 80, 85, 90, and 95.<br>2. The Centenarians Act of 2016 or Republic Act 10868 is an amended law. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The elderly will now be given P25,000.<br>2. The elderly will now be given P25,000 when they reach the age of 80.<br>3. The elderly will now be given P25,000 when they reach the age of 85.<br>4. The elderly will now be given P25,000 when they reach the age of 90.<br>5. The elderly will now be given P25,000 when they reach the age of 95.<br>6. The Centenarians Act of 2016 is Republic Act 10868. | 6 |
| google/gemma-3-1b-it | 1. The elderly will be given P25,000 as they reach the ages of 80, 85, 90, and 95.<br>2. P25,000 is an amendment to the Centenarians Act of 2016.<br>3. The Centenarians Act of 2016 is Republic Act 10868. | 3 |
| google/gemma-3-4b-it | 1. The elderly will be given P25,000.<br>2. The elderly will be given P25,000 as they reach the ages of 80.<br>3. The elderly will be given P25,000 as they reach the ages of 85.<br>4. The elderly will be given P25,000 as they reach the ages of 90.<br>5. The elderly will be given P25,000 as they reach the ages of 95.<br>6. The giving of P25,000 is under an amended Centenarians Act of 2016.<br>7. The giving of P25,000 is under Republic Act 10868. | 7 |
| gpt-3.5-turbo-0125 | 1. The elderly will now be given P25,000 as they reach the ages of 80 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>2. The elderly will now be given P25,000 as they reach the ages of 85 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>3. The elderly will now be given P25,000 as they reach the ages of 90 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>4. The elderly will now be given P25,000 as they reach the ages of 95 under an amended Centenarians Act of 2016 or Republic Act 10868. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. The elderly will be given P25,000 as they reach the age of 80 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>2. The elderly will be given P25,000 as they reach the age of 85 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>3. The elderly will be given P25,000 as they reach the age of 90 under an amended Centenarians Act of 2016 or Republic Act 10868.<br>4. The elderly will be given P25,000 as they reach the age of 95 under an amended Centenarians Act of 2016 or Republic Act 10868. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. The elderly will now be given P25,000 as they reach the ages of 80, 85, 90 and 95.<br>2. The elderly will now be given P25,000 under an amended Centenarians Act of 2016.<br>3. The elderly will now be given P25,000 under Republic Act 10868. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. The elderly will now be given P25,000 as they reach the age of 80, under an amended Centenarians Act of 2016 or Republic Act 10868.<br>2. The elderly will now be given P25,000 as they reach the age of 85, under an amended Centenarians Act of 2016 or Republic Act 10868.<br>3. The elderly will now be given P25,000 as they reach the age of 90, under an amended Centenarians Act of 2016 or Republic Act 10868.<br>4. The elderly will now be given P25,000 as they reach the age of 95, under an amended Centenarians Act of 2016 or Republic Act 10868. | 4 |

---

## Sample ID: quantemp_105
**Original Claim**: The image claims that an IAF woman pilot killed 300 people in an air strike

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The image claims that an IAF woman pilot killed 300 people in an air strike.<br>2. The image is an IAF woman pilot.<br>3. The image is a woman pilot.<br>4. The image is an IAF woman pilot.<br>5. The image is an IAF woman pilot. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The image claims that an IAF woman pilot killed 300 people in an air strike.<br>2. The IAF woman pilot killed 300 people in an air strike. | 2 |
| google/gemma-3-1b-it | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| google/gemma-3-4b-it | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| gpt-3.5-turbo-0125 | 1. An IAF woman pilot killed 300 people in an air strike. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The image claims that an IAF woman pilot killed 300 people in an air strike. | 1 |

---

## Sample ID: quantemp_106
**Original Claim**: People can only see 1% of the visible light spectrum? No, it's VISIBLE – we can see all of it

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. People can only see 1% of the visible light spectrum.<br>2. It is not true that people can only see 1% of the visible light spectrum.<br>3. People can see all of the visible light spectrum. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The visible light spectrum is 100% of the visible light spectrum. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. People can only see 1% of the visible light spectrum.<br>2. No, it's VISIBLE – we can see all of it. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. People can see 100% of the visible light spectrum.<br>2. The visible light spectrum is visible. | 2 |
| google/gemma-3-1b-it | 1. People can only see 1% of the visible light spectrum.<br>2. Visible light is not limited to a specific portion of the spectrum.<br>3. We can see all of the visible light. | 3 |
| google/gemma-3-4b-it | 1. People can only see 1% of the visible light spectrum.<br>2. It is VISIBLE.<br>3. We can see all of it. | 3 |
| gpt-3.5-turbo-0125 | 1. People can only see 1% of the visible light spectrum.<br>2. People can see all of the visible light spectrum. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. People can only see 1% of the visible light spectrum.<br>2. People can see all of the visible light spectrum. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. People can only see 1% of the visible light spectrum. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. People can only see 1% of the visible light spectrum.<br>2. People can see all of the visible light spectrum. | 2 |

---

## Sample ID: quantemp_107
**Original Claim**: Azam Khan calls Lord Krishna and Ram his ideals after he got out of jail after 27 months.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Azam Khan calls Lord Krishna and Ram his ideals.<br>2. Azam Khan got out of jail after 27 months. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Azam Khan was released from jail.<br>2. Azam Khan called Lord Krishna.<br>3. Azam Khan called Ram. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Azam Khan calls Lord Krishna and Ram his ideals after he got out of jail after 27 months.<br>2. Azam Khan is a person.<br>3. Azam Khan is a person.<br>4. Azam Khan is a person.<br>5. Azam Khan is a person.<br>6. Azam Khan is a person.<br>7. Azam Khan is a person.<br>8. Azam Khan is a person.<br>9. Azam Khan is a person.<br>10. Azam Khan is a person.<br>11. Azam Khan is a person.<br>12. Azam Khan is a person.<br>13. Azam Khan is a person.<br>14. Azam Khan is a person.<br>15. Azam Khan is a person.<br>16. Azam Khan is a person.<br>17. Azam Khan is a person.<br>18. Azam Khan is a person.<br>19. Azam Khan is a person.<br>20. Azam Khan is a person.<br>21. Azam Khan is a person.<br>22. Azam Khan is a person.<br>23. Azam Khan is a person.<br>24. Azam Khan is a person.<br>25. Azam Khan is a person.<br>26. Azam Khan is a person.<br>27. Azam Khan is a person.<br>28. Azam Khan is a person.<br>29. Azam Khan is a person.<br>30. Azam Khan is a person.<br>31. Az | 31 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Azam Khan called Lord Krishna after he got out of jail.<br>2. Azam Khan called Lord Krishna after he was released from jail.<br>3. Azam Khan called Lord Krishna after 27 months of being in jail.<br>4. Azam Khan called Lord Krishna after he was released from jail. | 4 |
| google/gemma-3-1b-it | 1. Azam Khan called Lord Krishna and Ram his ideals.<br>2. Azam Khan got out of jail after 27 months. | 2 |
| google/gemma-3-4b-it | 1. Azam Khan calls Lord Krishna his ideals.<br>2. Azam Khan calls Ram his ideals.<br>3. Azam Khan got out of jail.<br>4. Azam Khan was in jail for 27 months. | 4 |
| gpt-3.5-turbo-0125 | 1. Azam Khan calls Lord Krishna his ideals after he got out of jail after 27 months.<br>2. Azam Khan calls Ram his ideals after he got out of jail after 27 months. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Azam Khan calls Lord Krishna his ideal after Azam Khan got out of jail after 27 months.<br>2. Azam Khan calls Ram his ideal after Azam Khan got out of jail after 27 months. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Azam Khan called Lord Krishna and Ram his ideals after he got out of jail after 27 months. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Azam Khan calls Lord Krishna and Ram his ideals.<br>2. Azam Khan got out of jail after 27 months. | 2 |

---

## Sample ID: quantemp_108
**Original Claim**: All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Safdarjung hospital is located in New Delhi.<br>2. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 1 |
| google/gemma-3-1b-it | 1. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 1 |
| google/gemma-3-4b-it | 1. All seven patients who were getting treated for Covid-19 were at Safdarjung hospital.<br>2. All seven patients who were getting treated for Covid-19 in New Delhi have recovered. | 2 |
| gpt-3.5-turbo-0125 | 1. All seven patients were getting treated for Covid-19 at Safdarjung hospital in New Delhi.<br>2. All seven patients have recovered. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Seven patients were getting treated for Covid-19 at Safdarjung hospital in New Delhi.<br>2. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. All seven patients were getting treated for Covid-19 at Safdarjung hospital in New Delhi.<br>2. All seven patients who were getting treated for Covid-19 at Safdarjung hospital in New Delhi have recovered. | 2 |

---

## Sample ID: quantemp_109
**Original Claim**: Photograph of 8-year-old girl allegedly raped and murdered in Kolkata

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Photograph of 8-year-old girl allegedly raped and murdered in Kolkata | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photograph of an 8-year-old girl was allegedly raped and murdered in Kolkata. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I can't fulfill this request | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. I can't fulfill this request | 1 |
| google/gemma-3-1b-it | 1. Photograph of 8-year-old girl allegedly raped and murdered in Kolkata. | 1 |
| google/gemma-3-4b-it | 1. There is a photograph of an 8-year-old girl.<br>2. The photograph is allegedly of a girl who was raped.<br>3. The photograph is allegedly of a girl who was murdered.<br>4. The location is Kolkata. | 4 |
| gpt-3.5-turbo-0125 | 1. An 8-year-old girl was allegedly raped and murdered in Kolkata.<br>2. The 8-year-old girl was photographed. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The photograph is of an 8-year-old girl.<br>2. The 8-year-old girl was allegedly raped in Kolkata.<br>3. The 8-year-old girl was allegedly murdered in Kolkata. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Photograph of 8-year-old girl allegedly raped and murdered in Kolkata | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photograph of 8-year-old girl allegedly raped and murdered in Kolkata | 1 |

---

## Sample ID: quantemp_110
**Original Claim**: Under the GOP tax law, "if you live in Hinsdale, Illinois … you are now being double-taxed to the tune of $35,000."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Under the GOP tax law, if you live in Hinsdale, Illinois, you are now being double-taxed.<br>2. Under the GOP tax law, living in Hinsdale, Illinois results in being double-taxed to the tune of $35,000. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The GOP tax law has been implemented.<br>2. Under the GOP tax law, "if you live in Hinsdale, Illinois, you are now being double-taxed to the tune of $35,000." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The GOP tax law applies to Hinsdale, Illinois.<br>2. If you live in Hinsdale, Illinois, you are being double-taxed to the tune of $35,000.<br>3. The GOP tax law applies to Hinsdale, Illinois.<br>4. If you live in Hinsdale, Illinois, you are being double-taxed to the tune of $35,000. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The GOP tax law was enacted.<br>2. You live in Hinsdale, Illinois.<br>3. Under the GOP tax law, you are being double-taxed to the tune of $35,000. | 3 |
| google/gemma-3-1b-it | 1. Under the GOP tax law, “if you live in Hinsdale, Illinois, you are now being double-taxed to the tune of $35,000.” | 1 |
| google/gemma-3-4b-it | 1. Under the GOP tax law, if you live in Hinsdale, Illinois, you are being double-taxed.<br>2. The GOP tax law is being applied to people who live in Hinsdale, Illinois.<br>3. The double-taxation is to the tune of $35,000.<br>4. The location is Hinsdale, Illinois. | 4 |
| gpt-3.5-turbo-0125 | 1. The GOP tax law applies to residents of Hinsdale, Illinois.<br>2. Residents of Hinsdale, Illinois are being double-taxed to the tune of $35,000 under the GOP tax law. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Under the GOP tax law, if you live in Hinsdale, Illinois, you are now being double-taxed to the tune of $35,000. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Under the GOP tax law, if you live in Hinsdale, Illinois, you are now being double-taxed to the tune of $35,000. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Under the GOP tax law, if you live in Hinsdale, Illinois, you are now being double-taxed to the tune of $35,000. | 1 |

---

## Sample ID: quantemp_111
**Original Claim**: The purported website of Amazon that is selling unclaimed packages of Amazon for $19.99

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The purported website of Amazon is selling unclaimed packages of Amazon.<br>2. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Amazon is the purported website of Amazon.<br>2. Amazon is selling unclaimed packages of Amazon for $19.99. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The purported website of Amazon is selling unclaimed packages of Amazon.<br>2. The purported website is selling unclaimed packages of Amazon for $19.99. | 2 |
| google/gemma-3-1b-it | 1. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 1 |
| google/gemma-3-4b-it | 1. The purported website is selling unclaimed packages of Amazon.<br>2. The website is selling these packages for $19.99. | 2 |
| gpt-3.5-turbo-0125 | 1. The website of Amazon is purported to be selling unclaimed packages of Amazon for $19.99. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The purported website of Amazon is selling unclaimed packages of Amazon for $19.99. | 1 |

---

## Sample ID: quantemp_112
**Original Claim**: Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur, who was convicted in the murder of a police officer.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Colin Kaepernick made a $25,000 donation to an activist group.<br>2. The activist group is named after Assata Shakur.<br>3. Assata Shakur was convicted in the murder of a police officer. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer.<br>3. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Colin Kaepernick made a $25,000 donation to an activist group named Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer. | 2 |
| google/gemma-3-1b-it | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. The donation was to an activist group. | 2 |
| google/gemma-3-4b-it | 1. Colin Kaepernick made a $25,000 donation.<br>2. The donation was made to an activist group named after Assata Shakur.<br>3. Assata Shakur was convicted in the murder of a police officer. | 3 |
| gpt-3.5-turbo-0125 | 1. Colin Kaepernick made a $25,000 donation.<br>2. The donation was made to an activist group.<br>3. The activist group is named after Assata Shakur.<br>4. Assata Shakur was convicted in the murder of a police officer. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Colin Kaepernick made a $25,000 donation to an activist group named after Assata Shakur.<br>2. Assata Shakur was convicted in the murder of a police officer. | 2 |

---

## Sample ID: quantemp_113
**Original Claim**: "You had more women getting computer sciences degrees in the '80s by a factor of 2-plus than you do now."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In the '80s, there were more women getting computer sciences degrees than there are now.<br>2. The number of women getting computer sciences degrees in the '80s was 2-plus times greater than the number of women getting computer sciences degrees now. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In the '80s, more women got computer science degrees than they do now.<br>2. The '80s had a factor of 2-plus more women getting computer science degrees than they do now. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. You had more women getting computer sciences degrees in the '80s by a factor of 2-plus than you do now.<br>2. The '80s saw a significant increase in women pursuing computer sciences degrees.<br>3. The increase in women pursuing computer sciences degrees in the '80s was by a factor of 2-plus. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. You had more women getting computer sciences degrees in the '80s by a factor of 2-plus than you do now. | 1 |
| google/gemma-3-1b-it | 1. More women getting computer sciences degrees in the ‘80s by a factor of 2-plus than now. | 1 |
| google/gemma-3-4b-it | 1. You had more women getting computer sciences degrees in the '80s.<br>2. You had more women getting computer sciences degrees than you do now.<br>3. The '80s were a time period. | 3 |
| gpt-3.5-turbo-0125 | 1. More women were getting computer sciences degrees in the '80s by a factor of 2-plus than they do now. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. More women were getting computer sciences degrees in the 1980s by a factor of 2-plus than the number of women getting computer sciences degrees now. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. You had more women getting computer sciences degrees in the '80s by a factor of 2-plus than you do now. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. More women were getting computer sciences degrees in the '80s by a factor of 2-plus than now. | 1 |

---

## Sample ID: quantemp_114
**Original Claim**: Photo shows U.S. Rep. Lauren Boebert with two scantily dressed men.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Photo shows U.S. Rep. Lauren Boebert with two scantily dressed men. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photo shows U.S. Rep. Lauren Boebert.<br>2. Lauren Boebert is with two scantily dressed men. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. U.S. Rep. Lauren Boebert<br>2. Two scantily dressed men | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Photo shows U.S. Rep. Lauren Boebert with two men.<br>2. Photo shows U.S. Rep. Lauren Boebert with men. | 2 |
| google/gemma-3-1b-it | 1. Photo depicts U.S. Representative Lauren Boebert.<br>2. U.S. Representative Lauren Boebert is dressed scantily.<br>3. Two scantily dressed men are depicted in the photo. | 3 |
| google/gemma-3-4b-it | 1. A photo shows U.S. Rep. Lauren Boebert with two scantily dressed men. | 1 |
| gpt-3.5-turbo-0125 | 1. The photo shows U.S. Rep. Lauren Boebert with two scantily dressed men. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The photo shows U.S. Rep. Lauren Boebert with two scantily dressed men. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photo shows U.S. Rep. Lauren Boebert with two scantily dressed men. | 1 |

---

## Sample ID: quantemp_115
**Original Claim**: "The $3.6 billion deficit we inherited has turned into more than a half-billion-dollar surplus."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The $3.6 billion deficit was inherited.<br>2. The $3.6 billion deficit inherited has turned into more than a half-billion-dollar surplus. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The $3.6 billion deficit we inherited has turned into more than a half-billion-dollar surplus. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The $3.6 billion deficit we inherited has turned into more than a half-billion-dollar surplus.<br>2. The $3.6 billion deficit we inherited has turned into a surplus of more than $500 million.<br>3. The $3.6 billion deficit we inherited has turned into a surplus of more than $500 million in the United States. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The deficit inherited by the United States was $3.6 billion.<br>2. The deficit inherited by the United States has turned into a surplus of more than $500,000,000,000. | 2 |
| google/gemma-3-1b-it | 1. The deficit is $3.6 billion.<br>2. The deficit has turned into a surplus.<br>3. More than a half-billion-dollar surplus. | 3 |
| google/gemma-3-4b-it | 1. The deficit was $3.6 billion.<br>2. The deficit was inherited.<br>3. The deficit has turned into more than a half-billion-dollar surplus. | 3 |
| gpt-3.5-turbo-0125 | 1. The $3.6 billion deficit was inherited.<br>2. The $3.6 billion deficit has turned into more than a half-billion-dollar surplus. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The $3.6 billion deficit was inherited.<br>2. The $3.6 billion deficit that was inherited has turned into more than a half-billion-dollar surplus. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The $3.6 billion deficit we inherited has turned into more than a half-billion-dollar surplus. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The $3.6 billion deficit we inherited has turned into more than a half-billion-dollar surplus. | 1 |

---

## Sample ID: quantemp_116
**Original Claim**: CDC data says only 6% people died for only Covid-19

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. CDC data says only 6% of people died from Covid-19. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The CDC data says that only 6% of people died from only Covid-19. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The CDC data says only 6% people died for Covid-19.<br>2. CDC data says only 6% of people died for Covid-19. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Centers for Disease Control and Prevention (CDC) released data.<br>2. Only 6% of people died from Covid-19 according to CDC data. | 2 |
| google/gemma-3-1b-it | 1. CDC data states that only 6% of people died for COVID-19. | 1 |
| google/gemma-3-4b-it | 1. CDC data says only 6% people died for only Covid-19. | 1 |
| gpt-3.5-turbo-0125 | 1. CDC data says only 6% of people died from only Covid-19. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. CDC data says only 6% people died for only Covid-19. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. CDC data says only 6% people died for only Covid-19 | 1 |
| gpt-5.4-mini-2026-03-17 | 1. CDC data says only 6% people died for only Covid-19. | 1 |

---

## Sample ID: quantemp_117
**Original Claim**: Says "New Jersey’s $1 billion horse racing industry … employs 13,000 individuals and ensures the preservation of 176,000 acres of horse farmland."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. New Jersey's $1 billion horse racing industry employs 13,000 individuals.<br>2. The preservation of 176,000 acres of horse farmland is ensured by New Jersey's $1 billion horse racing industry. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. New Jersey's $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey's $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| google/gemma-3-1b-it | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. The horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| google/gemma-3-4b-it | 1. New Jersey’s horse racing industry says something.<br>2. New Jersey’s horse racing industry employs 13,000 individuals.<br>3. New Jersey’s horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 3 |
| gpt-3.5-turbo-0125 | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. New Jersey’s $1 billion horse racing industry employs 13,000 individuals.<br>2. New Jersey’s $1 billion horse racing industry ensures the preservation of 176,000 acres of horse farmland. | 2 |

---

## Sample ID: quantemp_118
**Original Claim**: "Over the last several months, there was a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering, who investigated every element of" the Benghazi incident.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Over the last several months, a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering, investigated every element of the Benghazi incident. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There was a review board headed by Mike Mullen and Tom Pickering.<br>2. Mike Mullen and Tom Pickering investigated every element of the Benghazi incident. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Benghazi incident was investigated by a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering.<br>2. Mike Mullen and Tom Pickering were two distinguished Americans.<br>3. Mike Mullen and Tom Pickering were two Americans.<br>4. Mike Mullen and Tom Pickering were Americans.<br>5. Mike Mullen and Tom Pickering were Americans. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Benghazi incident was reviewed by a review board headed by Mike Mullen and Tom Pickering.<br>2. The review board headed by Mike Mullen and Tom Pickering was composed of Americans.<br>3. The review board headed by Mike Mullen and Tom Pickering was active for several months.<br>4. The review board headed by Mike Mullen and Tom Pickering investigated every element of the Benghazi incident. | 4 |
| google/gemma-3-1b-it | 1. A review board headed by two distinguished Americans, Mike Mullen and Tom Pickering, investigated the Benghazi incident.<br>2. The Benghazi incident was a review board investigation. | 2 |
| google/gemma-3-4b-it | 1. Over the last several months, there was a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering.<br>2. The review board headed by two distinguished Americans, Mike Mullen and Tom Pickering investigated every element of the Benghazi incident. | 2 |
| gpt-3.5-turbo-0125 | 1. The review board was headed by two distinguished Americans.<br>2. The review board was headed by Mike Mullen.<br>3. The review board was headed by Tom Pickering.<br>4. The review board investigated every element of the Benghazi incident. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Over the last several months, there was a review board that investigated every element of the Benghazi incident.<br>2. The review board was headed by two distinguished Americans, Mike Mullen and Tom Pickering. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Over the last several months, there was a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering.<br>2. Mike Mullen and Tom Pickering investigated every element of the Benghazi incident. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Over the last several months, there was a review board headed by two distinguished Americans, Mike Mullen and Tom Pickering.<br>2. Over the last several months, the review board headed by two distinguished Americans, Mike Mullen and Tom Pickering, investigated every element of the Benghazi incident. | 2 |

---

## Sample ID: quantemp_119
**Original Claim**: "Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Since the election, 2.4 million new jobs have been created.<br>2. Since the election, 200,000 new jobs in manufacturing have been created. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Since the election, we have created 2.4 million new jobs.<br>2. Since the election, we have created 200,000 new jobs in manufacturing alone. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Since the election, we have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone.<br>2. The election has created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone.<br>3. We have created 2.4 million new jobs, including 200,000 new jobs in manufacturing alone. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The election took place.<br>2. We have created 2.4 million new jobs since the election.<br>3. We have created 200,000 new jobs in manufacturing since the election. | 3 |
| google/gemma-3-1b-it | 1. We have created 2.4 million new jobs.<br>2. 200,000 new jobs in manufacturing alone have been created. | 2 |
| google/gemma-3-4b-it | 1. Since the election, 2.4 million new jobs have been created.<br>2. 200,000 new jobs have been created in manufacturing alone. | 2 |
| gpt-3.5-turbo-0125 | 1. Since the election, "we" have created 2.4 million new jobs.<br>2. Since the election, "we" have created 200,000 new jobs in manufacturing alone. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Since the election, 2.4 million new jobs have been created.<br>2. Since the election, 200,000 new jobs in manufacturing have been created. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Since the election, we have created 2.4 million new jobs.<br>2. Since the election, we have created 200,000 new jobs in manufacturing alone. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Since the election, we have created 2.4 million new jobs.<br>2. Since the election, we have created 200,000 new jobs in manufacturing alone. | 2 |

---

## Sample ID: quantemp_120
**Original Claim**: Nein, Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft/nEine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist. Sie wird seit 2010 immer wieder zitiert. Sie fußt nicht nur auf falschen Annahmen sondern ist auch unlogisch.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Nein, Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt nicht nur auf falschen Annahmen, sondern ist auch unlogisch. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nein, Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Sie wird seit 2010 immer wieder zitiert.<br>4. Sie fußt nicht nur auf falschen Annahmen sondern ist auch unlogisch. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nein, Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Sie wird seit 2010 immer wieder zitiert.<br>4. Sie fußt nicht nur auf falschen Annahmen sondern ist auch unlogisch. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nein, Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Diese Rechnung wird seit 2010 immer wieder zitiert.<br>4. Diese Rechnung fußt nicht nur auf falschen Annahmen.<br>5. Diese Rechnung ist unlogisch. | 5 |
| google/gemma-3-1b-it | 1. Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt nicht nur auf falschen Annahmen sondern ist auch unlogisch. | 4 |
| google/gemma-3-4b-it | 1. Nein, Deutschland beeinflusst 0.00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt nicht nur auf falschen Annahmen.<br>5. Die Rechnung ist auch unlogisch. | 5 |
| gpt-3.5-turbo-0125 | 1. Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt nicht nur auf falschen Annahmen.<br>5. Die Rechnung ist auch unlogisch. | 5 |
| gpt-4.1-mini-2025-04-14 | 1. Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt auf falschen Annahmen.<br>5. Die Rechnung ist unlogisch. | 5 |
| gpt-5.4-nano-2026-03-17 | 1. Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Die Rechnung wird seit 2010 immer wieder zitiert.<br>4. Die Rechnung fußt nicht nur auf falschen Annahmen.<br>5. Die Rechnung ist auch unlogisch. | 5 |
| gpt-5.4-mini-2026-03-17 | 1. Deutschland beeinflusst nicht 0,00004712 Prozent des CO2-Anteils in der Luft.<br>2. Eine Rechnung soll zeigen, wie gering der Beitrag des Menschen zum Klimawandel angeblich ist.<br>3. Eine Rechnung wird seit 2010 immer wieder zitiert.<br>4. Eine Rechnung fußt nicht nur auf falschen Annahmen.<br>5. Eine Rechnung ist auch unlogisch. | 5 |

---

## Sample ID: quantemp_121
**Original Claim**: The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during Ukraine-Russia war

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one.<br>2. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during the Ukraine-Russia war. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one.<br>2. The picture is from the Ukraine-Russia war. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one.<br>2. It is a recent one.<br>3. During Ukraine-Russia war. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one.<br>2. The man draped in the Ukrainian flag is embracing a woman wearing the Russian flag.<br>3. The woman wearing the Russian flag is being embraced by a man draped in the Ukrainian flag.<br>4. The Ukrainian flag is being draped on a man.<br>5. The woman wearing the Russian flag is being embraced by a man wearing the Ukrainian flag.<br>6. The Russian flag is being worn by a woman.<br>7. The man is draped in the Ukrainian flag.<br>8. The woman is wearing the Russian flag. | 8 |
| google/gemma-3-1b-it | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during the Ukraine-Russia war. | 1 |
| google/gemma-3-4b-it | 1. The picture showing a man draped in the Ukrainian flag is a recent one.<br>2. The picture showing a man draped in the Ukrainian flag is embracing a woman.<br>3. The woman is wearing the Russian flag.<br>4. The picture is during Ukraine-Russia war. | 4 |
| gpt-3.5-turbo-0125 | 1. The picture is recent.<br>2. The picture shows a man draped in the Ukrainian flag embracing a woman wearing the Russian flag.<br>3. The picture was taken during the Ukraine-Russia war. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. The picture shows a man draped in the Ukrainian flag embracing a woman wearing the Russian flag.<br>2. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during the Ukraine-Russia war. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during Ukraine-Russia war. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The picture showing a man draped in the Ukrainian flag embracing a woman wearing the Russian flag is a recent one during Ukraine-Russia war. | 1 |

---

## Sample ID: quantemp_122
**Original Claim**: Apple will give $700 to anyone whose iPhone was slowed down

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Apple will give $700 to anyone whose iPhone was slowed down.<br>2. Apple is giving $700 to anyone whose iPhone was slowed down.<br>3. Apple is giving $700 to anyone whose iPhone was slowed down. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| google/gemma-3-1b-it | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| google/gemma-3-4b-it | 1. Apple will give $700 to anyone.<br>2. The person’s iPhone was slowed down. | 2 |
| gpt-3.5-turbo-0125 | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Apple will give $700 to anyone whose iPhone was slowed down. | 1 |

---

## Sample ID: quantemp_123
**Original Claim**: Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy, and "that's a loss for you."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, "that's a loss for you" is a statement. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. That's a loss for you. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. That's a loss for you. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. John McCain's health care plan provided a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy, and that's a loss for you. | 2 |
| google/gemma-3-1b-it | 1. John McCain’s health care plan provides a $5,000 tax credit for a $12,000 health care policy.<br>2. A loss for you is a statement expressing dissatisfaction with the tax credit. | 2 |
| google/gemma-3-4b-it | 1. Under John McCain's health care plan, people get a $5,000 tax credit.<br>2. People get a $5,000 tax credit to buy a $12,000 health care policy.<br>3. "That's a loss for you." | 3 |
| gpt-3.5-turbo-0125 | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, that is a loss for you. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, "that's a loss for you." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, "that's a loss for you." | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Under John McCain's health care plan, people get a $5,000 tax credit to buy a $12,000 health care policy.<br>2. Under John McCain's health care plan, "that's a loss for you." | 2 |

---

## Sample ID: quantemp_124
**Original Claim**: Video shows French president Macron dancing with his wife 30 years ago

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Video shows French president Macron dancing with his wife 30 years ago. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Video shows French president Macron dancing with his wife.<br>2. The video is from 30 years ago. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. French president Macron<br>2. Macron<br>3. Macron<br>4. Macron<br>5. Macron<br>6. Macron<br>7. Macron<br>8. Macron<br>9. Macron<br>10. Macron<br>11. Macron<br>12. Macron<br>13. Macron<br>14. Macron<br>15. Macron<br>16. Macron<br>17. Macron<br>18. Macron<br>19. Macron<br>20. Macron<br>21. Macron<br>22. Macron<br>23. Macron<br>24. Macron<br>25. Macron<br>26. Macron<br>27. Macron<br>28. Macron<br>29. Macron<br>30. Macron<br>31. Macron<br>32. Macron<br>33. Macron<br>34. Macron<br>35. Macron<br>36. Macron<br>37. Macron<br>38. Macron<br>39. Macron<br>40. Macron<br>41. Macron<br>42. Macron<br>43. Macron<br>44. Macron<br>45. Macron<br>46. Macron<br>47. Macron<br>48. Macron<br>49. Macron<br>50. Macron<br>51. Macron<br>52. Macron<br>53. Macron<br>54. Macron<br>55. Macron<br>56. Macron<br>57. Macron<br>58. Macron<br>59. Macron<br>60. Macron<br>61. Macron<br>62. Macron<br>63. Macron<br>64. Macron<br>65. Macron<br>66. Macron<br>67. Macron<br>68. Macron<br>69. Macron<br>70. Macron<br>71. Macron<br>72. Macron<br>73. Macron<br>74. Macron<br>75. Macron<br>76. Macron<br>77. Macron<br>78. Macron<br>79. Macron<br>80. Macron<br>81. Macron<br>82. Macron<br>83. Macron<br>84. Macron<br>85. Macron | 85 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Video shows French president Emmanuel Macron dancing with his wife Brigitte Macron 30 years ago. | 1 |
| google/gemma-3-1b-it | 1. Video shows French president Macron dancing with his wife.<br>2. French president Macron danced with his wife 30 years ago. | 2 |
| google/gemma-3-4b-it | 1. Video shows French president Macron.<br>2. Video shows Macron dancing with his wife.<br>3. The dancing occurred 30 years ago. | 3 |
| gpt-3.5-turbo-0125 | 1. Video shows French president Macron dancing with his wife 30 years ago. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The video shows French president Macron dancing with his wife 30 years ago. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows French president Macron dancing with French president Macron's wife 30 years ago. | 1 |

---

## Sample ID: quantemp_125
**Original Claim**: In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25 to include dozens of frozen shrimp products due to concerns over possible salmonella contamination.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25.<br>2. The voluntary recall initially issued on June 25 was expanded by Avanti Frozen Foods distributor in August 2021.<br>3. The expanded recall in August 2021 included dozens of frozen shrimp products.<br>4. The expansion of the voluntary recall in August 2021 was due to concerns over possible salmonella contamination. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In August 2021, Avanti Frozen Foods expanded its voluntary recall.<br>2. The voluntary recall initially issued on June 25 was expanded.<br>3. The expanded recall included dozens of frozen shrimp products.<br>4. The expanded recall was due to concerns over possible salmonella contamination. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25 to include dozens of frozen shrimp products due to concerns over possible salmonella contamination.<br>2. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25 to include dozens of frozen shrimp products due to concerns over possible salmonella contamination.<br>3. Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25 to include dozens of frozen shrimp products due to concerns over possible salmonella contamination. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25 to include dozens of frozen shrimp products in August 2021.<br>2. The recall was initially issued on June 25.<br>3. The recall was expanded in August 2021.<br>4. The recall included dozens of frozen shrimp products in August 2021.<br>5. Avanti Frozen Foods distributor was involved in the recall.<br>6. Avanti Frozen Foods distributor was the distributor of the frozen shrimp products included in the recall. | 6 |
| google/gemma-3-1b-it | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall.<br>2. Initially issued on June 25, the recall included dozens of frozen shrimp products.<br>3. The recall was due to concerns over possible salmonella contamination. | 3 |
| google/gemma-3-4b-it | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall.<br>2. The voluntary recall was initially issued on June 25.<br>3. The voluntary recall includes dozens of frozen shrimp products.<br>4. The recall is due to concerns over possible salmonella contamination. | 4 |
| gpt-3.5-turbo-0125 | 1. Avanti Frozen Foods distributor expanded its voluntary recall in August 2021.<br>2. The voluntary recall was initially issued on June 25.<br>3. The voluntary recall was expanded to include dozens of frozen shrimp products.<br>4. The expansion was due to concerns over possible salmonella contamination. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25.<br>2. The voluntary recall initially issued on June 25 included dozens of frozen shrimp products.<br>3. The voluntary recall expansion in August 2021 included dozens of frozen shrimp products.<br>4. The voluntary recall expansion in August 2021 was due to concerns over possible salmonella contamination. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall initially issued on June 25.<br>2. The voluntary recall initially issued on June 25 was expanded in August 2021 to include dozens of frozen shrimp products.<br>3. The expansion to include dozens of frozen shrimp products was due to concerns over possible salmonella contamination. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall.<br>2. Avanti Frozen Foods distributor initially issued its voluntary recall on June 25.<br>3. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall to include dozens of frozen shrimp products.<br>4. In August 2021, Avanti Frozen Foods distributor expanded its voluntary recall due to concerns over possible salmonella contamination. | 4 |

---

## Sample ID: quantemp_126
**Original Claim**: 77% of working mothers endure some kind of discrimination.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Working mothers endure some kind of discrimination.<br>2. 77% of working mothers endure some kind of discrimination.<br>3. 77% of working mothers endure some kind of discrimination. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The term "working mothers" refers to mothers who are employed.<br>2. 77% of mothers who are employed endure some kind of discrimination. | 2 |
| google/gemma-3-1b-it | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| google/gemma-3-4b-it | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| gpt-3.5-turbo-0125 | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 77% of working mothers endure some kind of discrimination. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 77% of working mothers endure some kind of discrimination. | 1 |

---

## Sample ID: quantemp_127
**Original Claim**: An asteroid had been expected to hit earth in mid-February 2020.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An asteroid was expected to hit Earth in mid-February 2020. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An asteroid was expected to hit Earth in mid-February 2020. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. An asteroid was expected to hit Earth in mid-February 2020.<br>2. The asteroid was expected to hit Earth in mid-February 2020.<br>3. The asteroid was expected to hit Earth in February 2020. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An asteroid was expected to hit earth in mid-February 2020. | 1 |
| google/gemma-3-1b-it | 1. An asteroid was expected to hit earth in mid-February 2020. | 1 |
| google/gemma-3-4b-it | 1. An asteroid had been expected to hit earth in mid-February 2020. | 1 |
| gpt-3.5-turbo-0125 | 1. An asteroid had been expected to hit earth in mid-February 2020. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. An asteroid had been expected to hit earth in mid-February 2020. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. An asteroid had been expected to hit earth in mid-February 2020. | 1 |

---

## Sample ID: quantemp_128
**Original Claim**: Photo shows Sri Lankan shaman who claimed he had a miracle cure for Covid-19 receiving the Covid-19 vaccine

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photo shows a Sri Lankan shaman.<br>2. The Sri Lankan shaman claimed he had a miracle cure for Covid-19.<br>3. The Sri Lankan shaman received the Covid-19 vaccine. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photo shows a Sri Lankan shaman.<br>2. The shaman claimed he had a miracle cure for Covid-19.<br>3. The shaman is receiving the Covid-19 vaccine. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Sri Lankan shaman<br>2. He<br>3. Covid-19<br>4. Vaccine | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A photo exists showing a Sri Lankan shaman.<br>2. The Sri Lankan shaman claimed to have a miracle cure for Covid-19.<br>3. The Sri Lankan shaman received the Covid-19 vaccine. | 3 |
| google/gemma-3-1b-it | 1. Photo shows Sri Lankan shaman.<br>2. The shaman claimed he had a miracle cure for Covid-19.<br>3. The shaman received the Covid-19 vaccine. | 3 |
| google/gemma-3-4b-it | 1. A photo shows Sri Lankan shaman.<br>2. The Sri Lankan shaman claimed he had a miracle cure for Covid-19.<br>3. The Sri Lankan shaman received the Covid-19 vaccine. | 3 |
| gpt-3.5-turbo-0125 | 1. The photo shows Sri Lankan shaman.<br>2. The Sri Lankan shaman claimed he had a miracle cure for Covid-19.<br>3. The Sri Lankan shaman is receiving the Covid-19 vaccine. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. The photo shows a Sri Lankan shaman.<br>2. The Sri Lankan shaman claimed he had a miracle cure for Covid-19.<br>3. The Sri Lankan shaman is receiving the Covid-19 vaccine. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Photo shows Sri Lankan shaman who claimed he had a miracle cure for Covid-19 receiving the Covid-19 vaccine. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photo shows Sri Lankan shaman receiving the Covid-19 vaccine.<br>2. Sri Lankan shaman claimed he had a miracle cure for Covid-19. | 2 |

---

## Sample ID: quantemp_129
**Original Claim**: Says"Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills!"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Patrick Murphy's "Pay More" energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Patrick Murphy's 'Pay More' energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Patrick Murphy's 'Pay More' energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| google/gemma-3-1b-it | 1. Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| google/gemma-3-4b-it | 1. Patrick Murphy’s ‘Pay More’ energy agenda is being said.<br>2. You could pay another $500 a year for your utility bills. | 2 |
| gpt-3.5-turbo-0125 | 1. Patrick Murphy has a 'Pay More' energy agenda.<br>2. Patrick Murphy's 'Pay More' energy agenda means you could pay another $500 a year for your utility bills. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Says "Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills!" | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Patrick Murphy’s ‘Pay More’ energy agenda means you could pay another $500 a year for your utility bills. | 1 |

---

## Sample ID: quantemp_130
**Original Claim**: Says "if you are shot in the city of Newark, you have over an 80 percent chance that you've been arrested before an average of 10 times."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. If a person is shot in the city of Newark, that person has over an 80 percent chance of having been arrested before an average of 10 times. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "if you are shot in the city of Newark" is a statement.<br>2. "you have over an 80 percent chance that you've been arrested" is a statement.<br>3. "you have over an 80 percent chance that you've been arrested before an average of 10 times" is a statement. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The city of Newark.<br>2. You have over an 80 percent chance that you've been arrested before an average of 10 times.<br>3. You are shot in the city of Newark. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The city of Newark is a place where if you are shot, you have over an 80 percent chance that you've been arrested before an average of 10 times. | 1 |
| google/gemma-3-1b-it | 1. If you are shot in the city of Newark, you have over an 80 percent chance that you’ve been arrested before an average of 10 times. | 1 |
| google/gemma-3-4b-it | 1. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>2. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>3. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>4. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>5. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>6. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>7. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>8. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>9. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>10. It says “if you are shot in the city of Newark, you have over an 80 percent chance.”<br>11. It says “if you | 11 |
| gpt-3.5-turbo-0125 | 1. If you are shot in the city of Newark, you have over an 80 percent chance that you've been arrested before an average of 10 times. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. If a person is shot in the city of Newark, the person has over an 80 percent chance that the person has been arrested before an average of 10 times. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Says "if you are shot in the city of Newark, you have over an 80 percent chance that you've been arrested before an average of 10 times." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. If you are shot in the city of Newark, you have over an 80 percent chance that you have been arrested before an average of 10 times. | 1 |

---

## Sample ID: quantemp_131
**Original Claim**: Photos show protest against electronic vote machine tampering in India in May 2019

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Photos show a protest against electronic vote machine tampering in India.<br>2. The protest took place in May 2019. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Photos show protest against electronic vote machine tampering in India in May 2019.<br>2. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>3. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>4. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>5. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>6. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>7. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>8. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>9. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>10. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>11. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>12. The protest against electronic vote machine tampering in India in May 2019 was shown in photos.<br>13. The protest against electronic vote machine | 13 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |
| google/gemma-3-1b-it | 1. Photos show protest against electronic vote machine tampering in India.<br>2. Protest against electronic vote machine tampering in India occurred in May 2019. | 2 |
| google/gemma-3-4b-it | 1. Photos show protest against electronic vote machine tampering in India occurred in May 2019. | 1 |
| gpt-3.5-turbo-0125 | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photos show protest against electronic vote machine tampering in India in May 2019. | 1 |

---

## Sample ID: quantemp_132
**Original Claim**: Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Budweiser has acknowledged that its employee has urinated in beer tanks. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Budweiser has acknowledged that its employee has urinated in beer tanks.<br>2. The employee has urinated in beer tanks for 12 years. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Budweiser<br>2. acknowledged<br>3. that<br>4. its<br>5. employee<br>6. has<br>7. urinated<br>8. in<br>9. beer<br>10. tanks<br>11. for<br>12. 12<br>13. years | 13 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An employee of Budweiser has urinated in beer tanks for 12 years.<br>2. Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years. | 2 |
| google/gemma-3-1b-it | 1. Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years. | 1 |
| google/gemma-3-4b-it | 1. Budweiser has acknowledged that its employee has urinated in beer tanks.<br>2. This employee has urinated in beer tanks for 12 years. | 2 |
| gpt-3.5-turbo-0125 | 1. Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Budweiser has acknowledged that its employee has urinated in beer tanks for 12 years. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Budweiser has acknowledged that Budweiser's employee has urinated in beer tanks for 12 years. | 1 |

---

## Sample ID: quantemp_133
**Original Claim**: "While fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year, teachers in Georgia are getting paid half of that."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of $102,000 a year. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of that. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Department of Education is a federal agency.<br>2. Fat-cat bureaucrats are employees of the Department of Education.<br>3. The Department of Education is located in Washington D.C.<br>4. Georgia is a state in the United States.<br>5. Teachers in Georgia are paid an average salary of $102,000 a year. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Department of Education is a federal executive department.<br>2. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>3. Teachers in Georgia are getting paid half of $102,000 a year. | 3 |
| google/gemma-3-1b-it | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| google/gemma-3-4b-it | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of $102,000 a year. | 2 |
| gpt-3.5-turbo-0125 | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of $102,000 a year. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of $102,000 a year. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. While fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year, teachers in Georgia are getting paid half of that. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Fat-cat bureaucrats at the Department of Education are getting paid an average salary of $102,000 a year.<br>2. Teachers in Georgia are getting paid half of that. | 2 |

---

## Sample ID: quantemp_134
**Original Claim**: The UK would pay 62% more into the EU budget than it gets back in spending by 2022 if it stays in the EU.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022 if it stays in the EU. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022.<br>2. If the UK stays in the EU, it would pay 62% more into the EU budget than it gets back in spending. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022 if it stays in the EU.<br>2. The UK's spending by 2022 would be 62% more than the amount it pays into the EU budget.<br>3. The UK's spending by 2022 would be 62% more than the amount it pays into the EU budget.<br>4. The UK's spending by 2022 would be 62% more than the amount it pays into the EU budget. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The UK would pay 62% more into the EU budget than it gets back in spending in 2022.<br>2. The UK would pay into the EU budget and get back in spending in 2022.<br>3. The UK would get back in spending from the EU budget in 2022. | 3 |
| google/gemma-3-1b-it | 1. The UK would pay 62% more into the EU budget.<br>2. The UK would get back 2022 in spending.<br>3. The UK would pay 62% more into the EU budget in 2022.<br>4. The UK would get back 2022 in spending. | 4 |
| google/gemma-3-4b-it | 1. The UK would pay 62% more into the EU budget.<br>2. The EU budget is being paid by the UK.<br>3. This payment would occur by 2022.<br>4. The UK would get back in spending by 2022 if it stays in the EU.<br>5. The UK is staying in the EU. | 5 |
| gpt-3.5-turbo-0125 | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022.<br>2. The UK would pay 62% more into the EU budget than it gets back in spending if it stays in the EU. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The UK would pay 62% more into the EU budget than the UK gets back in spending by 2022 if the UK stays in the EU. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022 if the UK stays in the EU. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The UK would pay 62% more into the EU budget than it gets back in spending by 2022 if the UK stays in the EU. | 1 |

---

## Sample ID: quantemp_135
**Original Claim**: Simulation with fictional virus shows ‘“what they're preparing for us" in 2025.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Simulation with fictional virus shows “what they're preparing for us” in 2025. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A simulation with a fictional virus shows "what they're preparing for us" in 2025. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Simulation with fictional virus shows “what they're preparing for us” in 2025.<br>2. The simulation with fictional virus shows “what they're preparing for us” in 2025.<br>3. The simulation with fictional virus shows “what they're preparing for us” in 2025. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The simulation was of a fictional virus.<br>2. The simulation with the fictional virus shows “what they're preparing for us" in 2025. | 2 |
| google/gemma-3-1b-it | 1. Simulation with fictional virus shows “what they’re preparing for us” in 2025. | 1 |
| google/gemma-3-4b-it | 1. Simulation with a fictional virus shows ““what they're preparing for us” in 2025. | 1 |
| gpt-3.5-turbo-0125 | 1. The simulation was conducted with a fictional virus.<br>2. The simulation shows "what they're preparing for us" in 2025. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Simulation with fictional virus shows “what they are preparing for us" in 2025. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Simulation with fictional virus shows “what they’re preparing for us” in 2025. | 1 |

---

## Sample ID: quantemp_136
**Original Claim**: Says CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. CNN's Wolf Blitzer said that the wealthiest Americans pay the most in taxes already.<br>2. CNN's Wolf Blitzer said that 50 percent of Americans don't even pay any federal income tax. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. CNN's Wolf Blitzer said that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax."<br>2. Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax."<br>2. The wealthiest Americans pay the most in taxes already.<br>3. 50 percent of Americans do not even pay any federal income tax. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. CNN's Wolf Blitzer said that the wealthiest Americans pay the most in taxes already.<br>2. The wealthiest Americans pay 50 percent of the federal income tax.<br>3. 50 percent of Americans do not pay any federal income tax. | 3 |
| google/gemma-3-1b-it | 1. CNN’s Wolf Blitzer was wrong to say that “the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don’t even pay any federal income tax.” | 1 |
| google/gemma-3-4b-it | 1. CNN's Wolf Blitzer said that "the wealthiest Americans, they pay the most in taxes already."<br>2. 50 percent of Americans don't even pay any federal income tax. | 2 |
| gpt-3.5-turbo-0125 | 1. CNN's Wolf Blitzer said "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax."<br>2. CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. CNN's Wolf Blitzer said that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax."<br>2. The claim says that CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. CNN's Wolf Blitzer was wrong to say that "the wealthiest Americans, they pay the most in taxes already -- 50 percent of Americans don't even pay any federal income tax." | 1 |

---

## Sample ID: quantemp_137
**Original Claim**: "At least 10 ISIS fighters have been caught coming across the Mexican border in Texas" and there are "dozens more that did not get caught by the Border Patrol."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more ISIS fighters that did not get caught by the Border Patrol coming across the Mexican border in Texas. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more ISIS fighters that did not get caught by the Border Patrol. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. Dozens more than 10 ISIS fighters have been caught coming across the Mexican border in Texas. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. Dozens of ISIS fighters coming across the Mexican border in Texas did not get caught by the Border Patrol. | 2 |
| google/gemma-3-1b-it | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more ISIS fighters that did not get caught by the Border Patrol. | 2 |
| google/gemma-3-4b-it | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more that did not get caught by the Border Patrol. | 2 |
| gpt-3.5-turbo-0125 | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. Dozens more ISIS fighters did not get caught by the Border Patrol coming across the Mexican border in Texas. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more ISIS fighters that did not get caught by the Border Patrol coming across the Mexican border in Texas. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. Dozens more ISIS fighters did not get caught by the Border Patrol. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. At least 10 ISIS fighters have been caught coming across the Mexican border in Texas.<br>2. There are dozens more ISIS fighters that did not get caught by the Border Patrol. | 2 |

---

## Sample ID: quantemp_138
**Original Claim**: "The CBO, the Congressional Budget Office has said that Obamacare will kill 800,000 jobs."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Congressional Budget Office has said that Obamacare will kill 800,000 jobs. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The CBO, the Congressional Budget Office, has said that Obamacare will kill 800,000 jobs. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The CBO, the Congressional Budget Office, has said that Obamacare will kill 800,000 jobs.<br>2. The Congressional Budget Office has said that Obamacare will kill 800,000 jobs.<br>3. The Congressional Budget Office has said that Obamacare will kill 800,000 jobs. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Congressional Budget Office (CBO) has said that Obamacare will kill 800,000 jobs. | 1 |
| google/gemma-3-1b-it | 1. The CBO has stated that Obamacare will kill 800,000 jobs. | 1 |
| google/gemma-3-4b-it | 1. The Congressional Budget Office (CBO) has said that Obamacare will kill 800,000 jobs. | 1 |
| gpt-3.5-turbo-0125 | 1. The Congressional Budget Office (CBO) has said that Obamacare will kill 800,000 jobs. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The Congressional Budget Office has said that Obamacare will kill 800,000 jobs. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The CBO, the Congressional Budget Office has said that Obamacare will kill 800,000 jobs. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The Congressional Budget Office has said that Obamacare will kill 800,000 jobs. | 1 |

---

## Sample ID: quantemp_139
**Original Claim**: Clip of Canada’s former Minister for Health discussing quarantine centers is not recent and dates to March 2021

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. The clip of Canada’s former Minister for Health discussing quarantine centers dates to March 2021. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. The clip dates to March 2021. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Canada's former Minister for Health<br>2. Discussing quarantine centers is not recent<br>3. Dates to March 2021 | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Clip of Canada's former Minister for Health discussing quarantine centers is not recent.<br>2. Clip of Canada's former Minister for Health discussing quarantine centers dates to March 2021. | 2 |
| google/gemma-3-1b-it | 1. Clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. Dates to March 2021. | 2 |
| google/gemma-3-4b-it | 1. A clip of Canada’s former Minister for Health is being discussed.<br>2. The clip dates to March 2021.<br>3. The clip pertains to quarantine centers. | 3 |
| gpt-3.5-turbo-0125 | 1. The clip is of Canada’s former Minister for Health.<br>2. The clip discussing quarantine centers is not recent.<br>3. The clip dates to March 2021. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. The clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. The clip of Canada’s former Minister for Health discussing quarantine centers dates to March 2021. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. A clip of Canada’s former Minister for Health discussing quarantine centers dates to March 2021. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Clip of Canada’s former Minister for Health discussing quarantine centers is not recent.<br>2. Clip of Canada’s former Minister for Health discussing quarantine centers dates to March 2021. | 2 |

---

## Sample ID: quantemp_140
**Original Claim**: US Government is giving out $185,000 to US homeowners through a secret stimulus program and users need to enter their details in the accompanying website to get the money

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money from the US Government. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The US Government is giving out $185,000 to US homeowners.<br>2. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>3. Users need to enter their details in the accompanying website to get the money. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The US Government is giving out $185,000 to US homeowners.<br>2. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>3. Users need to enter their details in the accompanying website to get the money. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The US Government is giving out $185,000 to US homeowners.<br>2. The US Government is giving out a secret stimulus program.<br>3. US homeowners need to enter their details in the accompanying website. | 3 |
| google/gemma-3-1b-it | 1. US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money. | 2 |
| google/gemma-3-4b-it | 1. The US Government is giving out $185,000 to US homeowners.<br>2. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>3. Users need to enter their details in the accompanying website to get the money. | 3 |
| gpt-3.5-turbo-0125 | 1. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. US Government is giving out $185,000 to US homeowners through a secret stimulus program.<br>2. Users need to enter their details in the accompanying website to get the money. | 2 |

---

## Sample ID: quantemp_141
**Original Claim**: "Russ Feingold got a memo in 2009 that outlined veteran harm" at a Wisconsin VA facility "and nothing was done."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Russ Feingold got a memo in 2009.<br>2. The memo outlined veteran harm.<br>3. The memo was received at a Wisconsin VA facility.<br>4. Nothing was done after Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Russ Feingold received a memo in 2009.<br>2. The memo outlined veteran harm at a Wisconsin VA facility.<br>3. Nothing was done regarding the memo. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. A memo in 2009 outlining veteran harm at a Wisconsin VA facility was written by Russ Feingold. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Russ Feingold received a memo in 2009.<br>2. The memo received by Russ Feingold outlined veteran harm at a Wisconsin VA facility.<br>3. Nothing was done at a Wisconsin VA facility. | 3 |
| google/gemma-3-1b-it | 1. A memo outlining veteran harm was issued in 2009 at a Wisconsin VA facility.<br>2. Russ Feingold received a memo detailing veteran harm at a Wisconsin VA facility. | 2 |
| google/gemma-3-4b-it | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. Nothing was done at a Wisconsin VA facility. | 2 |
| gpt-3.5-turbo-0125 | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. Nothing was done about the memo Russ Feingold got in 2009 that outlined veteran harm at a Wisconsin VA facility. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. Nothing was done about the memo that Russ Feingold got in 2009 that outlined veteran harm at a Wisconsin VA facility. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. Nothing was done. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Russ Feingold got a memo in 2009 that outlined veteran harm at a Wisconsin VA facility.<br>2. Nothing was done at a Wisconsin VA facility. | 2 |

---

## Sample ID: quantemp_142
**Original Claim**: Says Clackamas County Measure 3-401 "will hurt our county, cripple economic growth, and increase our taxes with excessive special elections."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Clackamas County Measure 3-401 will hurt Clackamas County.<br>2. Clackamas County Measure 3-401 will cripple economic growth in Clackamas County.<br>3. Clackamas County Measure 3-401 will increase taxes in Clackamas County.<br>4. Clackamas County Measure 3-401 will increase special elections in Clackamas County. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Clackamas County Measure 3-401 says "will hurt our county."<br>2. Clackamas County Measure 3-401 says "will cripple economic growth."<br>3. Clackamas County Measure 3-401 says "will increase our taxes."<br>4. Clackamas County Measure 3-401 says "will have excessive special elections." | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Clackamas County Measure 3-401 is a measure.<br>2. It is a special election.<br>3. It will hurt our county.<br>4. It will cripple economic growth.<br>5. It will increase our taxes. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Clackamas County Measure 3-401 says "will hurt our county, cripple economic growth, and increase our taxes with excessive special elections."<br>2. "our county" refers to Clackamas County.<br>3. "our" refers to Clackamas County.<br>4. "it" does not refer to anything in this claim.<br>5. "excessive special elections" refers to special elections.<br>6. "hurt" refers to Clackamas County.<br>7. "cripple economic growth" refers to Clackamas County.<br>8. "increase" refers to Clackamas County.<br>9. "our taxes" refers to taxes in Clackamas County. | 9 |
| google/gemma-3-1b-it | 1. Clackamas County Measure 3-401 is a measure.<br>2. “Will hurt our county” refers to Clackamas County.<br>3. “Cripple economic growth” refers to economic growth.<br>4. “Increase our taxes with excessive special elections” refers to taxes and special elections. | 4 |
| google/gemma-3-4b-it | 1. Clackamas County Measure 3-401 says “will hurt our county.”<br>2. Clackamas County Measure 3-401 says “will cripple economic growth.”<br>3. Clackamas County Measure 3-401 says “will increase our taxes.”<br>4. Clackamas County Measure 3-401 says “with excessive special elections.” | 4 |
| gpt-3.5-turbo-0125 | 1. Clackamas County Measure 3-401 "will hurt" the county.<br>2. Clackamas County Measure 3-401 "will cripple economic growth" in the county.<br>3. Clackamas County Measure 3-401 "will increase" taxes in the county with excessive special elections. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Clackamas County Measure 3-401 "will hurt our county."<br>2. Clackamas County Measure 3-401 "will cripple economic growth."<br>3. Clackamas County Measure 3-401 "will increase our taxes with excessive special elections." | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Clackamas County Measure 3-401 will hurt our county.<br>2. Clackamas County Measure 3-401 will cripple economic growth.<br>3. Clackamas County Measure 3-401 will increase our taxes with excessive special elections. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Clackamas County Measure 3-401 will hurt our county.<br>2. Clackamas County Measure 3-401 will cripple economic growth.<br>3. Clackamas County Measure 3-401 will increase our taxes with excessive special elections. | 3 |

---

## Sample ID: quantemp_143
**Original Claim**: "Two days of interest we pay to China is enough to buy one joint strike fighter [jet]."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Two days of interest paid to China is enough to buy one joint strike fighter. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "Two days of interest we pay to China" is enough to buy one joint strike fighter [jet]. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Two days of interest in China is enough to buy one joint strike fighter jet. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The interest paid to China is two days.<br>2. Two days of interest paid to China is enough to buy one joint strike fighter. | 2 |
| google/gemma-3-1b-it | 1. Two days of interest to China is enough to buy one joint strike fighter [jet]. | 1 |
| google/gemma-3-4b-it | 1. Two days of interest we pay to China is enough.<br>2. That is enough to buy one joint strike fighter [jet]. | 2 |
| gpt-3.5-turbo-0125 | 1. Two days of interest the US pays to China is enough to buy one joint strike fighter [jet]. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Two days of interest we pay to China is enough to buy one joint strike fighter [jet]. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Two days of interest we pay to China is enough to buy one joint strike fighter [jet]. | 1 |

---

## Sample ID: quantemp_144
**Original Claim**: Sir Gangaram built horse train in Pakistan's Punjab to transport men, machinery in 1898

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Sir Gangaram built a horse train in Punjab, Pakistan in 1898. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Sir Gangaram built a horse train in Pakistan's Punjab in 1898.<br>2. Sir Gangaram built a horse train to transport men and machinery in 1898. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Sir Gangaram built a horse train in Pakistan's Punjab in 1898.<br>2. The horse train was built by Sir Gangaram.<br>3. Sir Gangaram built the horse train in Punjab in 1898. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Sir Gangaram built a horse train in Pakistan's Punjab in 1898.<br>2. Sir Gangaram built a train in Pakistan's Punjab to transport men.<br>3. Sir Gangaram built a train in Pakistan's Punjab to transport machinery. | 3 |
| google/gemma-3-1b-it | 1. Sir Gangaram built a horse train in Pakistan’s Punjab.<br>2. In 1898, Sir Gangaram built a horse train in Pakistan’s Punjab. | 2 |
| google/gemma-3-4b-it | 1. Sir Gangaram built a horse train in Pakistan's Punjab.<br>2. The horse train was built in Pakistan's Punjab.<br>3. The horse train was built in 1898.<br>4. The horse train transported men.<br>5. The horse train transported machinery. | 5 |
| gpt-3.5-turbo-0125 | 1. Sir Gangaram built horse train in Pakistan's Punjab in 1898.<br>2. The horse train was built by Sir Gangaram in Pakistan's Punjab in 1898 to transport men and machinery. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Sir Gangaram built horse train in Pakistan's Punjab in 1898.<br>2. Sir Gangaram built horse train in Pakistan's Punjab to transport men.<br>3. Sir Gangaram built horse train in Pakistan's Punjab to transport machinery. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Sir Gangaram built horse train in Pakistan's Punjab to transport men, machinery in 1898. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Sir Gangaram built horse train in Pakistan's Punjab in 1898.<br>2. Sir Gangaram built horse train in Pakistan's Punjab to transport men.<br>3. Sir Gangaram built horse train in Pakistan's Punjab to transport machinery. | 3 |

---

## Sample ID: quantemp_145
**Original Claim**: Microsoft and Bill Gates created a video game titled “Omicron” in 1999

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Microsoft and Bill Gates created a video game titled “Omicron” in 1999. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Microsoft and Bill Gates created a video game titled "Omicron" in 1999. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Microsoft<br>2. Bill Gates<br>3. created<br>4. a<br>5. video<br>6. game<br>7. titled<br>8. “Omicron”<br>9. in<br>10. 1999 | 10 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Microsoft and Bill Gates created a video game titled “Omicron” in 1999. | 1 |
| google/gemma-3-1b-it | 1. Microsoft and Bill Gates created a video game titled “Omicron” in 1999. | 1 |
| google/gemma-3-4b-it | 1. Microsoft created a video game titled “Omicron” in 1999.<br>2. Bill Gates created a video game titled “Omicron” in 1999. | 2 |
| gpt-3.5-turbo-0125 | 1. Microsoft created a video game titled “Omicron” in 1999.<br>2. Bill Gates created a video game titled “Omicron” in 1999. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Microsoft created a video game titled “Omicron” in 1999.<br>2. Bill Gates created a video game titled “Omicron” in 1999. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Microsoft and Bill Gates created a video game titled “Omicron” in 1999. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Microsoft created a video game titled “Omicron” in 1999.<br>2. Bill Gates created a video game titled “Omicron” in 1999. | 2 |

---

## Sample ID: quantemp_146
**Original Claim**: SP president Akhilesh Yadav said 2000 will be build in western UP

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. SP president Akhilesh Yadav said 2000 will be built in western UP. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. SP president Akhilesh Yadav said 2000 will be built in western UP. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The President of India, Akhilesh Yadav, said 2000 will be built in western UP.<br>2. Akhilesh Yadav is the President of India.<br>3. Akhilesh Yadav is the President of India.<br>4. Akhilesh Yadav is the President of India. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The president of SP is Akhilesh Yadav.<br>2. Akhilesh Yadav said 2000 will be built in western UP. | 2 |
| google/gemma-3-1b-it | 1. Akhilesh Yadav was the SP president.<br>2. 2000 will be built in western Uttar Pradesh. | 2 |
| google/gemma-3-4b-it | 1. SP president Akhilesh Yadav said 2000 will be built in western UP. | 1 |
| gpt-3.5-turbo-0125 | 1. 2000 will be built in western UP.<br>2. Akhilesh Yadav said 2000 will be built in western UP. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. SP president Akhilesh Yadav said 2000 will be build in western UP. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. SP president Akhilesh Yadav said 2000 will be build in western UP. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. SP president Akhilesh Yadav said 2000 will be build in western UP. | 1 |

---

## Sample ID: quantemp_147
**Original Claim**: Melania Trump ripped out cherry trees, crabapple trees, and roses from 1913 when redoing the White House Rose Garden

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Melania Trump ripped out cherry trees from the White House Rose Garden in 1913.<br>2. Melania Trump ripped out crabapple trees from the White House Rose Garden in 1913.<br>3. Melania Trump ripped out roses from the White House Rose Garden in 1913. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Melania Trump ripped out cherry trees, crabapple trees, and roses from the White House Rose Garden.<br>2. Melania Trump redid the White House Rose Garden in 1913. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The White House Rose Garden was renovated in 1913.<br>2. Melania Trump ripped out cherry trees, crabapple trees, and roses from the White House Rose Garden in 1913.<br>3. The White House Rose Garden was renovated in 1913 by Melania Trump. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Melania Trump ripped out cherry trees from the White House.<br>2. Melania Trump ripped out crabapple trees from the White House.<br>3. Melania Trump ripped out roses from the White House. | 3 |
| google/gemma-3-1b-it | 1. Melania Trump ripped out cherry trees from the White House Rose Garden in 1913.<br>2. The White House Rose Garden was redone by Melania Trump in 1913. | 2 |
| google/gemma-3-4b-it | 1. Melania Trump ripped out cherry trees.<br>2. Melania Trump ripped out crabapple trees.<br>3. Melania Trump ripped out roses.<br>4. The ripping out of cherry trees, crabapple trees, and roses occurred in 1913.<br>5. The ripping out of cherry trees, crabapple trees, and roses occurred when redoing the White House Rose Garden. | 5 |
| gpt-3.5-turbo-0125 | 1. Melania Trump ripped out cherry trees from 1913 when redoing the White House Rose Garden.<br>2. Melania Trump ripped out crabapple trees from 1913 when redoing the White House Rose Garden.<br>3. Melania Trump ripped out roses from 1913 when redoing the White House Rose Garden. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Melania Trump ripped out cherry trees from 1913 when redoing the White House Rose Garden.<br>2. Melania Trump ripped out crabapple trees from 1913 when redoing the White House Rose Garden.<br>3. Melania Trump ripped out roses from 1913 when redoing the White House Rose Garden. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Melania Trump ripped out cherry trees from 1913 when redoing the White House Rose Garden.<br>2. Melania Trump ripped out crabapple trees from 1913 when redoing the White House Rose Garden.<br>3. Melania Trump ripped out roses from 1913 when redoing the White House Rose Garden. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Melania Trump ripped out cherry trees from 1913 when redoing the White House Rose Garden.<br>2. Melania Trump ripped out crabapple trees from 1913 when redoing the White House Rose Garden.<br>3. Melania Trump ripped out roses from 1913 when redoing the White House Rose Garden. | 3 |

---

## Sample ID: quantemp_148
**Original Claim**: "Again today (Ahmadinejad) made light of 9/11, and said that he's not even sure it happened and that people actually died."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Again today Ahmadinejad made light of 9/11.<br>2. Ahmadinejad said that he is not even sure 9/11 happened.<br>3. Ahmadinejad said that people actually died. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Ahmadinejad made a statement about 9/11.<br>2. Ahmadinejad said he is not sure if 9/11 happened.<br>3. Ahmadinejad said people actually died on 9/11. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Ahmadinejad made light of 9/11.<br>2. Ahmadinejad said that he's not even sure it happened.<br>3. Ahmadinejad made light of 9/11. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Ahmadinejad made light of 9/11.<br>2. Ahmadinejad said that he's not even sure 9/11 happened.<br>3. Ahmadinejad said that people actually died at 9/11. | 3 |
| google/gemma-3-1b-it | 1. Ahmadinejad made light of 9/11.<br>2. He said that he’s not even sure it happened.<br>3. People actually died. | 3 |
| google/gemma-3-4b-it | 1. Ahmadinejad made light of 9/11 today.<br>2. Ahmadinejad said that he's not even sure that 9/11 happened.<br>3. Ahmadinejad said that people actually died. | 3 |
| gpt-3.5-turbo-0125 | 1. Ahmadinejad made light of 9/11.<br>2. Ahmadinejad said he's not even sure 9/11 happened.<br>3. Ahmadinejad said people actually died in 9/11. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Ahmadinejad made light of 9/11 again today.<br>2. Ahmadinejad said that Ahmadinejad is not even sure 9/11 happened.<br>3. Ahmadinejad said that people actually died in 9/11. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Again today (Ahmadinejad) made light of 9/11.<br>2. Again today (Ahmadinejad) said that he is not even sure it happened.<br>3. Again today (Ahmadinejad) said that people actually died. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Ahmadinejad made light of 9/11 again today.<br>2. Ahmadinejad said that Ahmadinejad is not even sure that 9/11 happened.<br>3. Ahmadinejad said that people actually died. | 3 |

---

## Sample ID: quantemp_149
**Original Claim**: "We've had examples like in Yuma County, where we've been able to stop 97 percent of the illegal (immigration) flow, and those programs, they abolish."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In Yuma County, examples of stopping 97 percent of the illegal immigration flow have been observed.<br>2. The programs in Yuma County abolish illegal immigration flow. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. We've had examples like in Yuma County.<br>2. In Yuma County, we've been able to stop 97 percent of the illegal immigration flow.<br>3. Those programs, they abolish. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Yuma County<br>2. We've had examples like in Yuma County<br>3. Those programs abolish | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The claim "We've had examples like in Yuma County, where we've been able to stop 97 percent of the illegal (immigration) flow, and those programs, they abolish" refers to Yuma County.<br>2. We have had examples in Yuma County where we have been able to stop 97 percent of the illegal immigration flow.<br>3. Those programs in Yuma County abolish illegal immigration. | 3 |
| google/gemma-3-1b-it | 1. We’ve had examples like in Yuma County, where we’ve been able to stop 97 percent of the illegal (immigration) flow.<br>2. Those programs, they abolish. | 2 |
| google/gemma-3-4b-it | 1. We have had examples like in Yuma County.<br>2. We have been able to stop 97 percent of the illegal (immigration) flow in Yuma County.<br>3. Those programs abolish. | 3 |
| gpt-3.5-turbo-0125 | 1. Examples like in Yuma County have been able to stop 97 percent of the illegal immigration flow.<br>2. Those programs in Yuma County abolish. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In Yuma County, 97 percent of the illegal (immigration) flow has been stopped.<br>2. The programs that stopped 97 percent of the illegal (immigration) flow in Yuma County abolish. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. We've had examples like in Yuma County.<br>2. In Yuma County, we've been able to stop 97 percent of the illegal (immigration) flow.<br>3. Those programs abolish. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. "We've had examples like in Yuma County, where we've been able to stop 97 percent of the illegal (immigration) flow."<br>2. "Those programs abolish." | 2 |

---

## Sample ID: quantemp_150
**Original Claim**: A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter that read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The deleted 2018 tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody."<br>3. The tweet was deleted from the account of CNN correspondent Brian Stelter. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. CNN correspondent Brian Stelter was deleted from the account.<br>2. The Handmaid's Tale is a book.<br>3. The Handmaid's Tale is a book.<br>4. The Handmaid's Tale is a book.<br>5. CNN is a news organization.<br>6. CNN correspondent Brian Stelter is a person. | 6 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A tweet was deleted from the account of CNN correspondent Brian Stelter in 2018.<br>2. The deleted tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |
| google/gemma-3-1b-it | 1. A tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don’t think this kind of fear-mongering helps anybody." | 2 |
| google/gemma-3-4b-it | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The tweet read: "We are not 'a few steps from The Handmaid's Tale.'".<br>3. The tweet read: "I don't think this kind of fear-mongering helps anybody." | 3 |
| gpt-3.5-turbo-0125 | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The deleted tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The 2018 tweet from the account of CNN correspondent Brian Stelter read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The deleted 2018 tweet read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A 2018 tweet was deleted from the account of CNN correspondent Brian Stelter.<br>2. The 2018 tweet from the account of CNN correspondent Brian Stelter read: "We are not 'a few steps from The Handmaid's Tale.' I don't think this kind of fear-mongering helps anybody." | 2 |

---

## Sample ID: quantemp_151
**Original Claim**: "People show up in the emergency room with a sprained ankle, 25 percent get an opioid prescription."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. People show up in the emergency room with a sprained ankle.<br>2. Twenty-five percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of those who arrive in the emergency room get an opioid prescription. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people show up in the emergency room with a sprained ankle.<br>3. People show up in the emergency room with a sprained ankle. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| google/gemma-3-1b-it | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people get an opioid prescription. | 2 |
| google/gemma-3-4b-it | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| gpt-3.5-turbo-0125 | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. People show up in the emergency room with a sprained ankle.<br>2. 25 percent of people who show up in the emergency room with a sprained ankle get an opioid prescription. | 2 |

---

## Sample ID: quantemp_152
**Original Claim**: With the goal to preserve 30% of the earth’s land and water by 2030, “300 million people stand to lose their land and livelihood, most of them tribal and indigenous peoples.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The goal is to preserve 30% of the earth’s land and water by 2030.<br>2. 300 million people stand to lose their land and livelihood.<br>3. Most of the 300 million people who stand to lose their land and livelihood are tribal and indigenous peoples. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The goal is to preserve 30% of the earth’s land and water by 2030.<br>2. “300 million people stand to lose their land and livelihood, most of them tribal and indigenous peoples.” | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The goal to preserve 30% of the earth’s land and water by 2030.<br>2. 300 million people stand to lose their land and livelihood, most of them tribal and indigenous peoples. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The earth's land and water were to be preserved at 30% by 2030.<br>2. 300 million people stand to lose their land and livelihood by 2030.<br>3. 300 million people who are tribal and indigenous stand to lose their land and livelihood by 2030. | 3 |
| google/gemma-3-1b-it | 1. “300 million people stand to lose their land and livelihood”<br>2. “300 million people”<br>3. “2030”<br>4. “land and livelihood” | 4 |
| google/gemma-3-4b-it | 1. With the goal to preserve 30% of the earth’s land and water by 2030, 300 million people stand to lose their land and livelihood.<br>2. Most of the 300 million people stand to lose their land and livelihood are tribal peoples.<br>3. Most of the 300 million people stand to lose their land and livelihood are indigenous peoples. | 3 |
| gpt-3.5-turbo-0125 | 1. The goal is to preserve 30% of the earth’s land and water by 2030.<br>2. 300 million people stand to lose their land and livelihood, most of them tribal and indigenous peoples. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The goal is to preserve 30% of the earth’s land and water by 2030.<br>2. 300 million people stand to lose their land and livelihood with the goal to preserve 30% of the earth’s land and water by 2030.<br>3. Most of the 300 million people who stand to lose their land and livelihood with the goal to preserve 30% of the earth’s land and water by 2030 are tribal and indigenous peoples. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. With the goal to preserve 30% of the earth’s land and water by 2030, “300 million people stand to lose their land and livelihood, most of them tribal and indigenous peoples.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The goal is to preserve 30% of the earth’s land and water by 2030.<br>2. 300 million people stand to lose their land and livelihood.<br>3. Most of the 300 million people are tribal and indigenous peoples. | 3 |

---

## Sample ID: quantemp_153
**Original Claim**: Kejriwal was distributing masks during the pandemic without wearing one

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was not wearing a mask while distributing masks during the pandemic. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Arvind Kejriwal was distributing masks during the pandemic.<br>2. Arvind Kejriwal was not wearing a mask while distributing masks during the pandemic. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Kejriwal was distributing masks during the pandemic without wearing one.<br>2. Kejriwal was the leader of the Indian state of Delhi.<br>3. Kejriwal was the leader of the Indian state of Delhi.<br>4. Kejriwal was the leader of the Indian state of Delhi. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was not wearing a mask during the pandemic. | 2 |
| google/gemma-3-1b-it | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal distributed masks during the pandemic. | 2 |
| google/gemma-3-4b-it | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was distributing masks during the pandemic.<br>3. Kejriwal did not wear one. | 3 |
| gpt-3.5-turbo-0125 | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was distributing masks during the pandemic without wearing one. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was not wearing a mask while distributing masks during the pandemic. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Kejriwal was distributing masks during the pandemic without wearing one. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Kejriwal was distributing masks during the pandemic.<br>2. Kejriwal was not wearing a mask during the pandemic. | 2 |

---

## Sample ID: quantemp_154
**Original Claim**: "For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. For every dollar spent on actual peace creation, over $1,000 is spent on ways to prepare for war. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The entity referred to as "we" spent a dollar on actual peace creation.<br>2. The entity referred to as "we" spent over $1,000 on ways to prepare for war. | 2 |
| google/gemma-3-1b-it | 1. For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war. | 1 |
| google/gemma-3-4b-it | 1. For every dollar we spend on actual peace creation, we spend over $1,000.<br>2. We spend over $1,000 on ways to prepare for war. | 2 |
| gpt-3.5-turbo-0125 | 1. Every dollar spent on actual peace creation is over $1,000 spent on ways to prepare for war. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. For every dollar spent on actual peace creation, over $1,000 is spent on ways to prepare for war. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. For every dollar we spend on actual peace creation, we spend over $1,000 on ways to prepare for war. | 1 |

---

## Sample ID: quantemp_155
**Original Claim**: The New Zealand government plans to lock down schools for 72 hours with children inside.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The New Zealand government plans to lock down schools.<br>2. The New Zealand government plans to lock down schools for 72 hours.<br>3. The New Zealand government plans to have children inside schools during the lock down. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The New Zealand government plans to lock down schools.<br>2. The New Zealand government plans to lock down schools for 72 hours.<br>3. Children will be inside the schools during the lockdown. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The New Zealand government plans to lock down schools for 72 hours with children inside.<br>2. The New Zealand government plans to lock down schools for 72 hours.<br>3. The New Zealand government plans to lock down schools for 72 hours. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The New Zealand government plans to lock down schools for 72 hours.<br>2. The lockdown of schools in New Zealand will involve children. | 2 |
| google/gemma-3-1b-it | 1. The New Zealand government plans to lock down schools for 72 hours.<br>2. Schools in New Zealand are being locked down.<br>3. The New Zealand government plans to lock down schools for 72 hours. | 3 |
| google/gemma-3-4b-it | 1. The New Zealand government plans to lock down schools.<br>2. The lockdown of schools will be for 72 hours.<br>3. Children will be inside the schools during the lockdown. | 3 |
| gpt-3.5-turbo-0125 | 1. The New Zealand government plans to lock down schools for 72 hours.<br>2. Children will be inside the schools during the lockdown. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The New Zealand government plans to lock down schools for 72 hours with children inside. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The New Zealand government plans to lock down schools for 72 hours with children inside. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The New Zealand government plans to lock down schools for 72 hours with children inside. | 1 |

---

## Sample ID: quantemp_156
**Original Claim**: "There are 4.7 percent of Virginians who are minimum wage earners who are over 25 years of age working full-time and trying to raise a family."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 4.7 percent of Virginians who are minimum wage earners and over 25 years of age working full-time are trying to raise a family. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There are 4.7 percent of Virginians who are minimum wage earners.<br>2. These minimum wage earners are over 25 years of age.<br>3. These minimum wage earners are working full-time.<br>4. These minimum wage earners are trying to raise a family. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Virginians<br>2. 4.7 percent<br>3. of<br>4. are<br>5. minimum<br>6. wage<br>7. earners<br>8. who<br>9. are<br>10. over<br>11. 25<br>12. years<br>13. of<br>14. age<br>15. working<br>16. full-time<br>17. and<br>18. trying<br>19. to<br>20. raise<br>21. a<br>22. family | 22 |
| meta-llama/Llama-3.2-3B-Instruct | 1. There are 4.7 percent of Virginians who are minimum wage earners.<br>2. There are 25 years old Virginians who are minimum wage earners.<br>3. There are Virginians who are over 25 years old.<br>4. There are Virginians who are full-time workers.<br>5. There are Virginians who are trying to raise a family. | 5 |
| google/gemma-3-1b-it | 1. There are 4.7 percent of Virginians who are minimum wage earners.<br>2. There are 25 years of age or older Virginians who are working full-time.<br>3. There are Virginians who are over 25 years of age working full-time.<br>4. There are Virginians who are minimum wage earners working full-time.<br>5. There are Virginians who are minimum wage earners over 25 years of age working full-time. | 5 |
| google/gemma-3-4b-it | 1. There are 4.7 percent of Virginians.<br>2. Those Virginians are minimum wage earners.<br>3. Those Virginians are over 25 years of age.<br>4. Those Virginians are working full-time.<br>5. Those Virginians are trying to raise a family. | 5 |
| gpt-3.5-turbo-0125 | 1. 4.7 percent of Virginians who are minimum wage earners are over 25 years of age.<br>2. 4.7 percent of Virginians who are minimum wage earners are working full-time.<br>3. 4.7 percent of Virginians who are minimum wage earners are trying to raise a family. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. There are 4.7 percent of Virginians who are minimum wage earners.<br>2. The 4.7 percent of Virginians who are minimum wage earners are over 25 years of age.<br>3. The 4.7 percent of Virginians who are minimum wage earners are working full-time.<br>4. The 4.7 percent of Virginians who are minimum wage earners are trying to raise a family. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. There are 4.7 percent of Virginians who are minimum wage earners who are over 25 years of age working full-time and trying to raise a family. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 4.7 percent of Virginians are minimum wage earners.<br>2. 4.7 percent of Virginians are over 25 years of age.<br>3. 4.7 percent of Virginians are working full-time.<br>4. 4.7 percent of Virginians are trying to raise a family. | 4 |

---

## Sample ID: quantemp_157
**Original Claim**: 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. July<br>2. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July 2020. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| google/gemma-3-1b-it | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| google/gemma-3-4b-it | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| gpt-3.5-turbo-0125 | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 409,152 indictments for child pedophilia offenses were coming to the surface in July, 2020.<br>2. 409,152 indictments for trafficking offenses were coming to the surface in July, 2020. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 409,152 indictments for child pedophilia and trafficking offenses were coming to the surface in July, 2020. | 1 |

---

## Sample ID: quantemp_158
**Original Claim**: "Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes.<br>2. The United States is the only country in the world where 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes.<br>3. The United States is the only country in the world where 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The licensed dealers are 1 percent of the total licensed dealers.<br>2. The 1 percent of licensed dealers supply 57 percent of the guns that are recovered in crimes. | 2 |
| google/gemma-3-1b-it | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns recovered in crimes. | 1 |
| google/gemma-3-4b-it | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 1 |
| gpt-3.5-turbo-0125 | 1. 1 percent of licensed dealers supply 57 percent of the guns that are recovered in crimes.<br>2. Research shows this. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. 1 percent of licensed dealers supply 57 percent of the guns that are recovered in crimes. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Research shows that 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 1 percent of licensed dealers supply a whopping 57 percent of the guns that are recovered in crimes. | 1 |

---

## Sample ID: quantemp_159
**Original Claim**: Says the U.S. fleet of attack submarines is scheduled to fall below the 48 boats that Navy says it needs to carry out current missions.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The U.S. fleet of attack submarines is scheduled to fall below 48 boats.<br>2. The Navy says it needs 48 boats to carry out current missions. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that Navy says it needs to carry out current missions.<br>2. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that Navy says it needs to carry out current missions.<br>2. The U.S. fleet of attack submarines is scheduled to fall below 48 boats.<br>3. The U.S. fleet of attack submarines is scheduled to fall below 48 boats. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that the U.S. Navy says it needs to carry out current missions. | 1 |
| google/gemma-3-1b-it | 1. The U.S. fleet of attack submarines is scheduled to fall below 48 boats.<br>2. The Navy says it needs to carry out current missions. | 2 |
| google/gemma-3-4b-it | 1. The U.S. fleet of attack submarines is scheduled to fall below 48 boats.<br>2. The Navy says the U.S. fleet of attack submarines is scheduled to fall below 48 boats.<br>3. The Navy says it needs to carry out current missions. | 3 |
| gpt-3.5-turbo-0125 | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats.<br>2. Navy says the U.S. fleet of attack submarines needs 48 boats to carry out current missions. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that the Navy says it needs to carry out current missions. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that Navy says it needs to carry out current missions. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The U.S. fleet of attack submarines is scheduled to fall below the 48 boats that Navy says it needs to carry out current missions. | 1 |

---

## Sample ID: quantemp_160
**Original Claim**: In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "tamed" and "no longer to be feared."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "tamed" and "no longer to be feared". | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "tamed" and "no longer to be feared." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The New York Times reported that Adolf Hitler's imprisonment had left him "tamed" and "no longer to be feared" in December 1924. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Adolf Hitler was imprisoned in December 1924.<br>2. The New York Times reported in December 1924 that Adolf Hitler's short term of imprisonment had left him "tamed".<br>3. The New York Times reported in December 1924 that Adolf Hitler's short term of imprisonment had left him "no longer to be feared". | 3 |
| google/gemma-3-1b-it | 1. In December 1924, the New York Times reported that Adolf Hitler’s short term of imprisonment had left him “tamed” and “no longer to be feared.” | 1 |
| google/gemma-3-4b-it | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "tamed".<br>2. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "no longer to be feared". | 2 |
| gpt-3.5-turbo-0125 | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left him "tamed" and "no longer to be feared." | 1 |
| gpt-4.1-mini-2025-04-14 | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left Adolf Hitler "tamed."<br>2. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left Adolf Hitler "no longer to be feared." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left Adolf Hitler "tamed" and "no longer to be feared." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left Adolf Hitler "tamed".<br>2. In December 1924, the New York Times reported that Adolf Hitler's short term of imprisonment had left Adolf Hitler "no longer to be feared". | 2 |

---

## Sample ID: quantemp_161
**Original Claim**: Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019.<br>2. Moderna is a company.<br>3. Moderna is a biotechnology company.<br>4. Moderna is a biotechnology company that produced 100,000 Covid-19 vaccines in 2019. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| google/gemma-3-1b-it | 1. Moderna’s CEO stated that the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| google/gemma-3-4b-it | 1. Moderna’s CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| gpt-3.5-turbo-0125 | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Moderna's CEO said the company produced 100,000 Covid-19 vaccines in 2019. | 1 |

---

## Sample ID: quantemp_162
**Original Claim**: Video shows former President Donald Trump attacking the Clintons in 2023.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Video shows former President Donald Trump attacking the Clintons in 2023. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Video shows former President Donald Trump attacking the Clintons.<br>2. Former President Donald Trump attacked the Clintons in the video. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The former President of the United States is Donald Trump.<br>2. The Clintons are former President Donald Trump.<br>3. The former President of the United States is Donald Trump.<br>4. The Clintons are former President Donald Trump. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Video shows former President Donald Trump attacking the Clintons in 2023.<br>2. The Clintons were attacked by former President Donald Trump in 2023. | 2 |
| google/gemma-3-1b-it | 1. Video shows former President Donald Trump attacking the Clintons in 2023. | 1 |
| google/gemma-3-4b-it | 1. Video shows former President Donald Trump attacking the Clintons in 2023. | 1 |
| gpt-3.5-turbo-0125 | 1. The video shows former President Donald Trump attacking the Clintons in 2023. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A video shows former President Donald Trump attacking the Clintons in 2023. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows former President Donald Trump attacking the Clintons in 2023. | 1 |

---

## Sample ID: quantemp_163
**Original Claim**: "We are $20 trillion in debt. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The United States is $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. We are $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years.<br>2. The Congressional Budget Office is a US government agency.<br>3. The Congressional Budget Office is a US government agency.<br>4. The Congressional Budget Office is a US government agency.<br>5. The Congressional Budget Office is a US government agency.<br>6. The Congressional Budget Office is a US government agency.<br>7. The Congressional Budget Office is a US government agency.<br>8. The Congressional Budget Office is a US government agency.<br>9. The Congressional Budget Office is a US government agency.<br>10. The Congressional Budget Office is a US government agency.<br>11. The Congressional Budget Office is a US government agency.<br>12. The Congressional Budget Office is a US government agency.<br>13. The Congressional Budget Office is a US government agency.<br>14. The Congressional Budget Office is a US government agency.<br>15. The Congressional Budget Office is a US government agency.<br>16. The Congressional Budget Office is a US government agency.<br>17. The Congressional Budget Office is a US government agency.<br>18. The Congressional Budget Office is a US government agency.<br>19. The Congressional Budget Office is a US government agency.<br>20. The Congressional Budget Office is a US government agency.<br>21. The Congressional Budget Office is a US government agency.<br>22. The Congressional Budget Office is a US government agency.<br>23. The Congressional Budget | 23 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The United States is $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| google/gemma-3-1b-it | 1. We are $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| google/gemma-3-4b-it | 1. We are $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| gpt-3.5-turbo-0125 | 1. The United States is $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The United States is $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. We are $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. We are $20 trillion in debt.<br>2. The Congressional Budget Office projects an additional $129 trillion of accumulated deficits over the next 30 years. | 2 |

---

## Sample ID: quantemp_164
**Original Claim**: In late June 2021, a statue of George Floyd in New York City was vandalized with a label representing a white nationalist group.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In late June 2021, a statue of George Floyd in New York City was vandalized.<br>2. In late June 2021, a label representing a white nationalist group was applied to the statue of George Floyd in New York City. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In late June 2021, a statue of George Floyd in New York City was vandalized.<br>2. The statue of George Floyd in New York City was vandalized.<br>3. A statue of George Floyd in New York City was vandalized.<br>4. A statue of George Floyd in New York City was vandalized with a label representing a white nationalist group. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. New York City<br>2. George Floyd<br>3. June<br>4. 2021<br>5. A statue<br>6. New York City<br>7. George Floyd<br>8. Vandalized<br>9. A label<br>10. Representing<br>11. A white nationalist group | 11 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A statue of George Floyd was vandalized in New York City in late June 2021.<br>2. The vandalization of a statue of George Floyd in New York City in late June 2021 was with a label representing a white nationalist group. | 2 |
| google/gemma-3-1b-it | 1. A statue of George Floyd was vandalized in New York City.<br>2. A label representing a white nationalist group was placed on the statue in late June 2021. | 2 |
| google/gemma-3-4b-it | 1. In late June 2021, a statue of George Floyd was vandalized.<br>2. The statue of George Floyd was located in New York City.<br>3. The vandalism involved a label representing a white nationalist group. | 3 |
| gpt-3.5-turbo-0125 | 1. A statue of George Floyd was vandalized in New York City.<br>2. The vandalism occurred in late June 2021.<br>3. The label on the statue represented a white nationalist group. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. In late June 2021, a statue of George Floyd in New York City was vandalized.<br>2. In late June 2021, a statue of George Floyd in New York City was vandalized with a label representing a white nationalist group. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. In late June 2021, a statue of George Floyd in New York City was vandalized with a label representing a white nationalist group. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In late June 2021, a statue of George Floyd in New York City was vandalized.<br>2. In late June 2021, a statue of George Floyd in New York City was vandalized with a label representing a white nationalist group. | 2 |

---

## Sample ID: quantemp_165
**Original Claim**: Some 8.1 million of the estimated 11 million to 12 million people "in this country illegally are working."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Some 8.1 million of the estimated 11 million to 12 million people in this country illegally are working. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Some 8.1 million people "in this country illegally" are working.<br>2. The estimated number of people "in this country illegally" is 11 million to 12 million. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The estimated 11 million to 12 million people are working.<br>2. Some 8.1 million of the estimated 11 million to 12 million people are working. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The people in this country are estimated to be 11 million to 12 million.<br>2. Some of the people in this country are 8.1 million.<br>3. The people in this country are 11 million.<br>4. The people in this country are 12 million. | 4 |
| google/gemma-3-1b-it | 1. Some 8.1 million people are estimated to be working in this country.<br>2. The estimated number of people working in this country is 11 million to 12 million.<br>3. The estimated number of people working in this country is 8.1 million. | 3 |
| google/gemma-3-4b-it | 1. Some 8.1 million of the estimated 11 million to 12 million people “in this country illegally” are working. | 1 |
| gpt-3.5-turbo-0125 | 1. 8.1 million of the estimated 11 million to 12 million people in this country illegally are working. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Some 8.1 million of the estimated 11 million to 12 million people in this country illegally are working. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Some 8.1 million of the estimated 11 million to 12 million people "in this country illegally are working." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Some 8.1 million of the estimated 11 million to 12 million people in this country illegally are working. | 1 |

---

## Sample ID: quantemp_166
**Original Claim**: Photos show a 1,000-bed advance hospital has been constructed in days at Rajasthan to tackle the Coronavirus outbreak.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Photos show a 1,000-bed advance hospital has been constructed in Rajasthan.<br>2. The 1,000-bed advance hospital was constructed in Rajasthan.<br>3. The 1,000-bed advance hospital was constructed in Rajasthan to tackle the Coronavirus outbreak. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A 1,000-bed advance hospital has been constructed in Rajasthan.<br>2. The hospital has been constructed in days to tackle the Coronavirus outbreak. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The 1,000-bed advance hospital in Rajasthan has been constructed in days.<br>2. A 1,000-bed advance hospital in Rajasthan has been constructed.<br>3. A 1,000-bed advance hospital in Rajasthan has been constructed in days. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A 1,000-bed advance hospital has been constructed in Rajasthan.<br>2. The hospital was constructed in days.<br>3. The hospital was constructed to tackle the Coronavirus outbreak in Rajasthan. | 3 |
| google/gemma-3-1b-it | 1. A 1,000-bed advance hospital has been constructed in days in Rajasthan.<br>2. The construction of a 1,000-bed advance hospital in Rajasthan to tackle the Coronavirus outbreak has been shown in photos. | 2 |
| google/gemma-3-4b-it | 1. Photos show a 1,000-bed advance hospital has been constructed.<br>2. The construction of the 1,000-bed advance hospital occurred in days at Rajasthan.<br>3. The construction of the 1,000-bed advance hospital occurred to tackle the Coronavirus outbreak. | 3 |
| gpt-3.5-turbo-0125 | 1. Photos show a 1,000-bed advance hospital has been constructed in days at Rajasthan.<br>2. The advance hospital was constructed in days at Rajasthan to tackle the Coronavirus outbreak. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Photos show a 1,000-bed advance hospital has been constructed in Rajasthan.<br>2. The 1,000-bed advance hospital was constructed in days.<br>3. The 1,000-bed advance hospital in Rajasthan has been constructed to tackle the Coronavirus outbreak. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Photos show a 1,000-bed advance hospital has been constructed in days at Rajasthan to tackle the Coronavirus outbreak. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photos show a 1,000-bed advance hospital has been constructed in days at Rajasthan.<br>2. Photos show a 1,000-bed advance hospital has been constructed in days at Rajasthan to tackle the Coronavirus outbreak. | 2 |

---

## Sample ID: quantemp_167
**Original Claim**: A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods that the Quezon City government procured in 2020.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A Commission on Audit report was issued in 2020.<br>2. The Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods.<br>3. The Commission on Audit report questioned the validity of COVID-19 relief goods procured by the Quezon City government.<br>4. The Commission on Audit report questioned the validity of COVID-19 relief goods procured by the Quezon City government in 2020. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods that the Quezon City government procured in 2020. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Quezon City government procured P479-million worth of COVID-19 relief goods in 2020.<br>2. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods that the Quezon City government procured in 2020. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A Commission on Audit issued a report questioning the validity of P479-million worth of COVID-19 relief goods procured by the Quezon City government in 2020.<br>2. The Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods procured by the Quezon City government in 2020.<br>3. The Commission on Audit report questioned the validity of COVID-19 relief goods worth P479-million procured by the Quezon City government in 2020. | 3 |
| google/gemma-3-1b-it | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods.<br>2. The Quezon City government procured COVID-19 relief goods worth P479-million.<br>3. The validity of the COVID-19 relief goods is questioned. | 3 |
| google/gemma-3-4b-it | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods was procured.<br>2. The Quezon City government procured the COVID-19 relief goods in 2020. | 2 |
| gpt-3.5-turbo-0125 | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods.<br>2. The COVID-19 relief goods were procured by the Quezon City government in 2020. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods.<br>2. The Quezon City government procured P479-million worth of COVID-19 relief goods in 2020. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods that the Quezon City government procured in 2020. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A new Commission on Audit report questioned the validity of P479-million worth of COVID-19 relief goods.<br>2. The Quezon City government procured P479-million worth of COVID-19 relief goods in 2020. | 2 |

---

## Sample ID: quantemp_168
**Original Claim**: California’s registered independent voters “will not be able to vote republican come 2020.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. California’s registered independent voters will not be able to vote Republican come 2020. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. California’s registered independent voters will not be able to vote Republican in 2020. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. California's registered independent voters will not be able to vote Republican in 2020. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. California has registered independent voters.<br>2. California's registered independent voters will not vote for the Republican party in 2020. | 2 |
| google/gemma-3-1b-it | 1. California’s registered independent voters will not be able to vote republican come 2020. | 1 |
| google/gemma-3-4b-it | 1. California’s registered independent voters will not be able to vote republican come 2020. | 1 |
| gpt-3.5-turbo-0125 | 1. California’s registered independent voters “will not be able to vote republican come 2020.” | 1 |
| gpt-4.1-mini-2025-04-14 | 1. California’s registered independent voters will not be able to vote republican come 2020. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. California’s registered independent voters will not be able to vote republican come 2020. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. California’s registered independent voters will not be able to vote republican come 2020. | 1 |

---

## Sample ID: quantemp_169
**Original Claim**: "President Trump has lifted the prospect of voters across Vermont, overseeing a 11,742 decline of Vermont residents on food stamps."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. President Trump has lifted the prospect of voters in Vermont.<br>2. Vermont residents have experienced an 11,742 decline in food stamp recipients under President Trump's action.<br>3. President Trump is overseeing the decline of Vermont residents on food stamps. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. A 11,742 decline of Vermont residents on food stamps has occurred. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. Vermont residents on food stamps have declined by 11,742. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. President Trump has lifted the prospect of voters across Vermont.<br>3. Vermont residents have declined by 11,742 due to the lifting of the prospect of voters across Vermont. | 3 |
| google/gemma-3-1b-it | 1. President Trump lifted the prospect of voters across Vermont.<br>2. A 11,742 decline of Vermont residents on food stamps occurred. | 2 |
| google/gemma-3-4b-it | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. There has been a 11,742 decline of Vermont residents on food stamps. | 2 |
| gpt-3.5-turbo-0125 | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. President Trump oversaw an 11,742 decline of Vermont residents on food stamps. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. President Trump has overseen a 11,742 decline of Vermont residents on food stamps. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. President Trump has overseen a 11,742 decline of Vermont residents on food stamps. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. President Trump has lifted the prospect of voters across Vermont.<br>2. President Trump has overseen a 11,742 decline of Vermont residents on food stamps. | 2 |

---

## Sample ID: quantemp_170
**Original Claim**: "Elaine Chao BUSTED Sending $97 Million Contract To Help Mitch McConnell Win Reelection."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Elaine Chao was accused of sending a $97 million contract to help Mitch McConnell win re-election. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Elaine Chao sent a $97 million contract to help Mitch McConnell win reelection. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Elaine Chao was the Secretary of Labor.<br>2. BUSTED is a verb.<br>3. Sending is a verb.<br>4. $97 Million is a monetary unit.<br>5. Contract is a noun.<br>6. To is a preposition.<br>7. Help is a verb.<br>8. Mitch McConnell is a person.<br>9. Win is a verb.<br>10. Reelection is a noun.<br>11. Is a linking verb.<br>12. Is a linking verb.<br>13. Is a linking verb. | 13 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Elaine Chao sent a $97 million contract to help Mitch McConnell win reelection. | 1 |
| google/gemma-3-1b-it | 1. Elaine Chao BUSTED Sending $97 Million Contract To Help Mitch McConnell Win Reelection. | 1 |
| google/gemma-3-4b-it | 1. Elaine Chao BUSTED<br>2. Sending $97 million contract to help Mitch McConnell win reelection. | 2 |
| gpt-3.5-turbo-0125 | 1. Elaine Chao was busted sending a $97 million contract to help Mitch McConnell win reelection. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Elaine Chao sent a $97 million contract to help Mitch McConnell win reelection. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Elaine Chao BUSTED Sending $97 Million Contract To Help Mitch McConnell Win Reelection. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Elaine Chao BUSTED Sending $97 Million Contract To Help Mitch McConnell Win Reelection. | 1 |

---

## Sample ID: quantemp_171
**Original Claim**: Did Jim Jordan Say In A Congressional Hearing That The 2020 Election Was Stolen?

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Did Jim Jordan say in a congressional hearing that the 2020 election was stolen? | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Jim Jordan gave a statement in a Congressional hearing.<br>2. Jim Jordan stated that the 2020 election was stolen. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Jim Jordan did not say in a congressional hearing that the 2020 election was stolen.<br>2. The 2020 election was not stolen.<br>3. The 2020 United States presidential election was not stolen. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Jim Jordan made a statement in a congressional hearing.<br>2. The 2020 election was the subject of Jim Jordan's statement in a congressional hearing. | 2 |
| google/gemma-3-1b-it | 1. Jim Jordan stated that the 2020 election was not accurate.<br>2. The 2020 election was not accurate. | 2 |
| google/gemma-3-4b-it | 1. Jim Jordan said in a congressional hearing that the 2020 election was stolen. | 1 |
| gpt-3.5-turbo-0125 | 1. Jim Jordan said in a congressional hearing that the 2020 Election was stolen. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Jim Jordan spoke in a Congressional hearing.<br>2. Jim Jordan said that the 2020 election was stolen in the Congressional hearing. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Did Jim Jordan say in a Congressional hearing that the 2020 Election was stolen? | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Jim Jordan said in a congressional hearing that the 2020 election was stolen. | 1 |

---

## Sample ID: quantemp_172
**Original Claim**: The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers to make journey safer, faster and more convenient.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey to the CharDham pilgrimage centers safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey to the CharDham pilgrimage centers faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey to the CharDham pilgrimage centers more convenient. | 5 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched to make journey safer, faster, and more convenient. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The CharDham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers.<br>3. The CharDham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers to make journey safer, faster and more convenient. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched to make the CharDham pilgrimage journey safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched to make the CharDham pilgrimage journey faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched to make the CharDham pilgrimage journey more convenient. | 5 |
| google/gemma-3-1b-it | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. To improve connectivity to the CharDham pilgrimage centers, the Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>3. To make journey safer, faster, and more convenient, the Chardham Mahamarg Vikas Pariyojna was launched in 2016. | 3 |
| google/gemma-3-4b-it | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched to make the journey to the CharDham pilgrimage centers safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched to make the journey to the CharDham pilgrimage centers faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched to make the journey to the CharDham pilgrimage centers more convenient. | 5 |
| gpt-3.5-turbo-0125 | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna aims to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna aims to make the journey safer.<br>4. The Chardham Mahamarg Vikas Pariyojna aims to make the journey faster.<br>5. The Chardham Mahamarg Vikas Pariyojna aims to make the journey more convenient. | 5 |
| gpt-4.1-mini-2025-04-14 | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey more convenient. | 5 |
| gpt-5.4-nano-2026-03-17 | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey more convenient. | 5 |
| gpt-5.4-mini-2026-03-17 | 1. The Chardham Mahamarg Vikas Pariyojna was launched in 2016.<br>2. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to improve connectivity to the CharDham pilgrimage centers.<br>3. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey safer.<br>4. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey faster.<br>5. The Chardham Mahamarg Vikas Pariyojna was launched in 2016 to make journey more convenient. | 5 |

---

## Sample ID: quantemp_173
**Original Claim**: "Mass shootings went up 200 percent in the decade after the assault weapons ban expired."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "Mass shootings went up 200 percent in the decade after the assault weapons ban expired." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired.<br>2. The assault weapons ban expired in the United States.<br>3. Mass shootings in the United States increased by 200 percent in the decade following the ban's expiration. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The assault weapons ban expired.<br>2. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 2 |
| google/gemma-3-1b-it | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |
| google/gemma-3-4b-it | 1. Mass shootings went up 200 percent.<br>2. The increase occurred in the decade after the assault weapons ban expired. | 2 |
| gpt-3.5-turbo-0125 | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Mass shootings went up 200 percent in the decade after the assault weapons ban expired. | 1 |

---

## Sample ID: quantemp_174
**Original Claim**: An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An Indian flag was waved among the crowd.<br>2. The crowd stormed the U.S. Capitol on Jan. 6, 2021. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021.<br>2. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021.<br>3. The U.S. Capitol was stormed by a crowd of people on Jan. 6, 2021.<br>4. The crowd of people that stormed the U.S. Capitol on Jan. 6, 2021, waved an Indian flag. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |
| google/gemma-3-1b-it | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on January 6, 2021. | 1 |
| google/gemma-3-4b-it | 1. An Indian flag was waved among the crowd of people.<br>2. The crowd of people stormed the U.S. Capitol.<br>3. The event occurred on Jan. 6, 2021. | 3 |
| gpt-3.5-turbo-0125 | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. An Indian flag was waved among the crowd of people that stormed the U.S. Capitol on Jan. 6, 2021. | 1 |

---

## Sample ID: quantemp_175
**Original Claim**: Hungarian-American billionaire George Soros bribed three Democratic senators to vote for a shutdown of the U.S. federal government.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Hungarian-American billionaire George Soros bribed three Democratic senators.<br>2. Three Democratic senators were bribed by Hungarian-American billionaire George Soros.<br>3. Hungarian-American billionaire George Soros bribed three Democratic senators to vote for a shutdown of the U.S. federal government. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. George Soros is a Hungarian-American billionaire.<br>2. George Soros bribed three Democratic senators.<br>3. The senators voted for a shutdown of the U.S. federal government. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Hungarian-American billionaire George Soros<br>2. Bribed three Democratic senators<br>3. Voted for a shutdown of the U.S. federal government | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. George Soros is a Hungarian-American.<br>2. George Soros is a billionaire.<br>3. George Soros bribed three Democratic senators.<br>4. The U.S. federal government was shut down.<br>5. The three Democratic senators voted for the shutdown of the U.S. federal government. | 5 |
| google/gemma-3-1b-it | 1. George Soros was a Hungarian-American billionaire.<br>2. Three Democratic senators were bribed by George Soros.<br>3. The shutdown of the U.S. federal government occurred. | 3 |
| google/gemma-3-4b-it | 1. Hungarian-American billionaire George Soros bribed three Democratic senators.<br>2. The bribery occurred for a shutdown of the U.S. federal government. | 2 |
| gpt-3.5-turbo-0125 | 1. Hungarian-American billionaire George Soros bribed three Democratic senators.<br>2. The three Democratic senators voted for a shutdown of the U.S. federal government. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Hungarian-American billionaire George Soros bribed three Democratic senators.<br>2. Hungarian-American billionaire George Soros bribed three Democratic senators to vote for a shutdown of the U.S. federal government. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Hungarian-American billionaire George Soros bribed three Democratic senators to vote for a shutdown of the U.S. federal government. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Hungarian-American billionaire George Soros bribed three Democratic senators.<br>2. Hungarian-American billionaire George Soros bribed three Democratic senators to vote for a shutdown of the U.S. federal government. | 2 |

---

## Sample ID: quantemp_176
**Original Claim**: "Ivermectin sterilizes the majority (85%) of the men who take it."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Ivermectin is an antiparasitic drug.<br>2. Ivermectin is also used for treating certain skin conditions.<br>3. Ivermectin is not known to sterilize men who take it. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Ivermectin is a medication.<br>2. Ivermectin is used to treat parasitic infections.<br>3. Ivermectin is used to treat parasitic infections in humans.<br>4. Ivermectin is used to treat parasitic infections in humans.<br>5. Ivermectin is used to treat parasitic infections in humans. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| google/gemma-3-1b-it | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| google/gemma-3-4b-it | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| gpt-3.5-turbo-0125 | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Ivermectin sterilizes the majority (85%) of the men who take it. | 1 |

---

## Sample ID: quantemp_177
**Original Claim**: Video shows Priyanka Gandhi Vadra's security personnel threatens a Journalist when she was asked questions on Article 370

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Video shows Priyanka Gandhi Vadra's security personnel threatening a journalist.<br>2. Priyanka Gandhi Vadra was asked questions on Article 370. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Video shows Priyanka Gandhi Vadra's security personnel threatening a journalist.<br>2. Journalist was asked questions on Article 370.<br>3. Security personnel threatened journalist when asked questions on Article 370. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Priyanka Gandhi Vadra was asked questions on Article 370.<br>2. Video shows Priyanka Gandhi Vadra's security personnel threatening a Journalist.<br>3. Priyanka Gandhi Vadra was asked questions on Article 370 by a Journalist. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Video shows Priyanka Gandhi Vadra's security personnel threatening a journalist.<br>2. Priyanka Gandhi Vadra's security personnel threatened a journalist.<br>3. Priyanka Gandhi Vadra's security personnel threatened a journalist when she was asked questions on Article 370. | 3 |
| google/gemma-3-1b-it | 1. Video shows Priyanka Gandhi Vadra’s security personnel threatened a Journalist.<br>2. Security personnel threatens a Journalist.<br>3. Priyanka Gandhi Vadra’s security personnel threatens a Journalist. | 3 |
| google/gemma-3-4b-it | 1. Video shows Priyanka Gandhi Vadra's security personnel.<br>2. Priyanka Gandhi Vadra's security personnel threatens a Journalist.<br>3. The threat occurred when she was asked questions on Article 370. | 3 |
| gpt-3.5-turbo-0125 | 1. Video shows Priyanka Gandhi Vadra's security personnel threatens a Journalist.<br>2. Priyanka Gandhi Vadra was asked questions on Article 370. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Video shows Priyanka Gandhi Vadra's security personnel threatens a Journalist.<br>2. Priyanka Gandhi Vadra's security personnel threatened a Journalist when the Journalist was asked questions on Article 370. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Video shows Priyanka Gandhi Vadra's security personnel threatens a Journalist. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows Priyanka Gandhi Vadra's security personnel threatens a Journalist when Priyanka Gandhi Vadra was asked questions on Article 370. | 1 |

---

## Sample ID: quantemp_178
**Original Claim**: Video shows military helicopter shot down by rebels in Myanmar in May 2021

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A video shows a military helicopter being shot down by rebels in Myanmar in May 2021. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A military helicopter was shot down by rebels in Myanmar in May 2021. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Video shows<br>2. military<br>3. helicopter<br>4. shot<br>5. down<br>6. by<br>7. rebels<br>8. in<br>9. Myanmar<br>10. in<br>11. May<br>12. 2021 | 12 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A military helicopter was shot down by rebels in Myanmar in May 2021.<br>2. Video shows a military helicopter being shot down by rebels in Myanmar in May 2021. | 2 |
| google/gemma-3-1b-it | 1. Video shows military helicopter shot down by rebels in Myanmar in May 2021. | 1 |
| google/gemma-3-4b-it | 1. Video shows military helicopter shot down by rebels in Myanmar.<br>2. The video was from May 2021. | 2 |
| gpt-3.5-turbo-0125 | 1. The video shows a military helicopter being shot down by rebels in Myanmar in May 2021. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A video shows a military helicopter shot down by rebels in Myanmar in May 2021. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Video shows military helicopter shot down by rebels in Myanmar in May 2021. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows military helicopter shot down by rebels in Myanmar in May 2021. | 1 |

---

## Sample ID: quantemp_179
**Original Claim**: Says"76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States is a country.<br>2. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The presidential debates are in the United States.<br>2. 76 percent of all voters in the United States say Johnson-Weld in the presidential debates. | 2 |
| google/gemma-3-1b-it | 1. “76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates.” | 1 |
| google/gemma-3-4b-it | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| gpt-3.5-turbo-0125 | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 76 percent of all voters in the United States say they want Johnson-Weld, by name, in the presidential debates. | 1 |

---

## Sample ID: quantemp_180
**Original Claim**: "According to the latest statistics 121,000 [teen] pregnancies were experienced in our country in 2019 …"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. According to the latest statistics, 121,000 teen pregnancies were experienced in our country in 2019. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. According to the latest statistics, 121,000 pregnancies were experienced in our country in 2019. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 2019 was the year in which 121,000 [teen] pregnancies were experienced in the country.<br>2. According to the latest statistics, 121,000 [teen] pregnancies were experienced in the country in 2019. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. According to the latest statistics, 121,000 teenage pregnancies were experienced in our country in 2019. | 1 |
| google/gemma-3-1b-it | 1. 121,000 teenage pregnancies were experienced in our country in 2019. | 1 |
| google/gemma-3-4b-it | 1. According to the latest statistics, 121,000 teen pregnancies were experienced in our country in 2019. | 1 |
| gpt-3.5-turbo-0125 | 1. 121,000 teen pregnancies were experienced in the country in 2019. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 121,000 teen pregnancies were experienced in our country in 2019. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 121,000 [teen] pregnancies were experienced in our country in 2019. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. According to the latest statistics, 121,000 teen pregnancies were experienced in our country in 2019. | 1 |

---

## Sample ID: quantemp_181
**Original Claim**: Says Joe Biden “wants to put a 3% annual federal tax on your home.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Joe Biden says he wants to put a 3% annual federal tax on your home. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Joe Biden says he wants to put a 3% annual federal tax on your home. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Joe Biden wants to put a 3% annual federal tax on your home. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Joe Biden says a 3% annual federal tax on homes.<br>2. Joe Biden wants to put a 3% annual federal tax on homes. | 2 |
| google/gemma-3-1b-it | 1. Joe Biden stated that he wants to put a 3% annual federal tax on your home. | 1 |
| google/gemma-3-4b-it | 1. Joe Biden said “wants to put a 3% annual federal tax on your home.” | 1 |
| gpt-3.5-turbo-0125 | 1. Joe Biden wants to put a 3% annual federal tax on your home. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Joe Biden wants to put a 3% annual federal tax on your home. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Joe Biden “wants to put a 3% annual federal tax on your home.” | 1 |

---

## Sample ID: quantemp_182
**Original Claim**: "We have a system now where in 40 states, the highest-paid public employee is the state university’s head football or basketball coach."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In 40 states, the highest-paid public employee is the state university’s head football coach.<br>2. In 40 states, the highest-paid public employee is the state university’s head basketball coach. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. We have a system where in 40 states, the highest-paid public employee is the state university’s head football or basketball coach. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The highest-paid public employee in the United States is the state university's head football coach.<br>2. The highest-paid public employee in the United States is the state university's head football coach in 40 states.<br>3. The highest-paid public employee in the United States is the state university's head football coach in 40 states. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The highest-paid public employee is the head football coach in 40 states.<br>2. The highest-paid public employee is the head basketball coach in 40 states. | 2 |
| google/gemma-3-1b-it | 1. We have a system where the highest-paid public employee is the state university’s head football or basketball coach. | 1 |
| google/gemma-3-4b-it | 1. We have a system now.<br>2. In 40 states, the highest-paid public employee is the state university’s head football or basketball coach. | 2 |
| gpt-3.5-turbo-0125 | 1. In 40 states, the highest-paid public employee is the state university’s head football coach.<br>2. In 40 states, the highest-paid public employee is the state university’s head basketball coach. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In 40 states, the highest-paid public employee is the state university’s head football coach.<br>2. In 40 states, the highest-paid public employee is the state university’s head basketball coach. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. We have a system now where in 40 states, the highest-paid public employee is the state university’s head football or basketball coach. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "We have a system now where in 40 states, the highest-paid public employee is the state university’s head football or basketball coach." | 1 |

---

## Sample ID: quantemp_183
**Original Claim**: Since he took office as Milwaukee County executive, "we have never raised" bus fares and "this year there’ll be a million route-miles more than there were five years ago."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Since he took office as Milwaukee County executive, there has been no increase in bus fares.<br>2. Since he took office as Milwaukee County executive, this year there will be a million route-miles more than there were five years ago. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Since he took office as Milwaukee County executive, "we have never raised" bus fares.<br>2. "This year there’ll be a million route-miles more than there were five years ago." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Milwaukee County executive took office.<br>2. "we" is a pronoun referring to Milwaukee County executive.<br>3. "have" is a verb.<br>4. "raised" is a verb.<br>5. "bus" is a noun.<br>6. "fare" is a noun.<br>7. "there" is a demonstrative.<br>8. "there" is a demonstrative.<br>9. "were" is a verb.<br>10. "five" is a number.<br>11. "years" is a noun.<br>12. "more" is a determiner.<br>13. "there" is a demonstrative.<br>14. "a million" is a number.<br>15. "route-miles" is a noun.<br>16. "there" is a demonstrative.<br>17. "this year" is a demonstrative.<br>18. "there" is a demonstrative.<br>19. "there" is a demonstrative.<br>20. "there" is a demonstrative.<br>21. "there" is a demonstrative.<br>22. "there" is a demonstrative.<br>23. "there" is a demonstrative.<br>24. "there" is a demonstrative.<br>25. "this" is a demonstrative.<br>26. "year" is a noun.<br>27. "five" is a number.<br>28. "there" is a demonstrative.<br>29. "there" is a demonstrative | 29 |
| meta-llama/Llama-3.2-3B-Instruct | 1. He took office as Milwaukee County executive.<br>2. We have never raised bus fares in Milwaukee County.<br>3. This year there'll be a million route-miles more than there were five years ago in Milwaukee County. | 3 |
| google/gemma-3-1b-it | 1. “We have never raised” bus fares in Milwaukee County.<br>2. “This year there’ll be a million route-miles more than there were five years ago.” | 2 |
| google/gemma-3-4b-it | 1. He took office as Milwaukee County executive.<br>2. “We have never raised” bus fares.<br>3. “This year there’ll be a million route-miles more than there were five years ago.” | 3 |
| gpt-3.5-turbo-0125 | 1. He took office as Milwaukee County executive.<br>2. "We have never raised" bus fares since he took office as Milwaukee County executive.<br>3. "This year there’ll be a million route-miles more than there were five years ago" since he took office as Milwaukee County executive. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Since he took office as Milwaukee County executive, bus fares have never been raised.<br>2. Since he took office as Milwaukee County executive, there will be a million route-miles more this year than there were five years ago. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Since Milwaukee County executive took office, “we have never raised” bus fares.<br>2. Since Milwaukee County executive took office, “this year there’ll be a million route-miles more than there were five years ago.” | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Since the Milwaukee County executive took office, bus fares have never been raised.<br>2. Since the Milwaukee County executive took office, there will be a million route-miles more this year than there were five years ago. | 2 |

---

## Sample ID: quantemp_184
**Original Claim**: "Fred's never had a 100 percent record on right-to-life in his Senate career. The records reflect that. And he doesn't support the human life amendment, which is most amazing because that's been a part of the Republican platform since 1980."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Fred has never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred has never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Fred has never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred has never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Fred's never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that.<br>3. The human life amendment is a part of the Republican platform since 1980. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Fred never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment has been part of the Republican platform since 1980. | 4 |
| google/gemma-3-1b-it | 1. Fred’s never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred does not support the human life amendment.<br>3. The human life amendment is a part of the Republican platform since 1980. | 3 |
| google/gemma-3-4b-it | 1. Fred has never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred has never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |
| gpt-3.5-turbo-0125 | 1. Fred has never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred has never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred doesn't support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Fred has never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that Fred has never had a 100 percent record on right-to-life in his Senate career.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Fred had never had a 100 percent record on right-to-life in his Senate career.<br>2. The records reflect that.<br>3. Fred does not support the human life amendment.<br>4. The human life amendment is most amazing because that has been a part of the Republican platform since 1980. | 4 |
| gpt-5.4-mini-2026-03-17 | 1. Fred's never had a 100 percent record on right-to-life in Fred's Senate career.<br>2. The records reflect that Fred's never had a 100 percent record on right-to-life in Fred's Senate career.<br>3. Fred doesn't support the human life amendment.<br>4. The human life amendment has been a part of the Republican platform since 1980. | 4 |

---

## Sample ID: quantemp_185
**Original Claim**: Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Akhilesh Yadav was one of the 302 people who signed a petition.<br>2. The petition was for stopping the death sentence of Kasab. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Akhilesh Yadav signed a petition for stopping the death sentence of Kasab.<br>2. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab.<br>2. Kasab was a person who was sentenced to death.<br>3. Kasab was a person who was sentenced to death. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 1 |
| google/gemma-3-1b-it | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 1 |
| google/gemma-3-4b-it | 1. Akhilesh Yadav was one of the 302 people.<br>2. The 302 people signed a petition.<br>3. The petition was for stopping the death sentence.<br>4. The death sentence was for Kasab. | 4 |
| gpt-3.5-turbo-0125 | 1. Akhilesh Yadav signed a petition for stopping the death sentence of Kasab. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Akhilesh Yadav was one of the 302 people who signed a petition for stopping the death sentence of Kasab. | 1 |

---

## Sample ID: quantemp_186
**Original Claim**: A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt.<br>2. The Chevrolet Volt is a car model.<br>3. A Florida car dealer is a business entity.<br>4. A car dealer is a business entity.<br>5. A car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |
| google/gemma-3-1b-it | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt.<br>2. The quote was for a battery. | 2 |
| google/gemma-3-4b-it | 1. A Florida car dealer quoted $30,000.<br>2. The Florida car dealer quoted $30,000 to replace the battery.<br>3. The battery is on a Chevrolet Volt. | 3 |
| gpt-3.5-turbo-0125 | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A Florida car dealer quoted $30,000 to replace the battery on a Chevrolet Volt. | 1 |

---

## Sample ID: quantemp_187
**Original Claim**: HMRC employs 300 people to investigate tax fraud.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. HMRC employs 300 people.<br>2. HMRC employs 300 people to investigate tax fraud. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. HMRC employs 300 people to investigate tax fraud. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. HMRC employs 300 people to investigate tax fraud. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. HMRC employs 300 people.<br>2. HMRC investigates tax fraud. | 2 |
| google/gemma-3-1b-it | 1. HMRC employs 300 people to investigate tax fraud.<br>2. HMRC investigates tax fraud. | 2 |
| google/gemma-3-4b-it | 1. HMRC employs 300 people.<br>2. HMRC employs 300 people to investigate tax fraud. | 2 |
| gpt-3.5-turbo-0125 | 1. HMRC employs 300 people to investigate tax fraud. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. HMRC employs 300 people to investigate tax fraud. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. HMRC employs 300 people to investigate tax fraud. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. HMRC employs 300 people to investigate tax fraud. | 1 |

---

## Sample ID: quantemp_188
**Original Claim**: IPS Officer Roopa Yadav refused to take an award from the Modi government as one of its MP has insulted martyr Hemant Karkare

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of the MPs of the Modi government insulted martyr Hemant Karkare. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of its MPs has insulted martyr Hemant Karkare. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of its MP has insulted martyr Hemant Karkare. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. IPS Officer Roopa Yadav refused an award from the Modi government.<br>2. IPS Officer Roopa Yadav was refused an award by the Modi government.<br>3. One of the MPs of the Modi government insulted martyr Hemant Karkare.<br>4. The MP of the Modi government insulted martyr Hemant Karkare. | 4 |
| google/gemma-3-1b-it | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. The award was refused by the Modi government.<br>3. The MP insulted martyr Hemant Karkare. | 3 |
| google/gemma-3-4b-it | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of its MP insulted martyr Hemant Karkare. | 2 |
| gpt-3.5-turbo-0125 | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of Modi government's MP insulted martyr Hemant Karkare. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. IPS Officer Roopa Yadav refused to take an award from the Modi government because one of the Modi government's MPs has insulted martyr Hemant Karkare. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of the Modi government’s MP has insulted martyr Hemant Karkare. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. IPS Officer Roopa Yadav refused to take an award from the Modi government.<br>2. One of the Modi government’s MP has insulted martyr Hemant Karkare. | 2 |

---

## Sample ID: quantemp_189
**Original Claim**: A 71-year-old Florida man was arrested on suspicion of grand theft after tying a downed power pole to the roof of his vehicle.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A 71-year-old Florida man was arrested.<br>2. A 71-year-old Florida man was arrested on suspicion of grand theft.<br>3. A 71-year-old Florida man tied a downed power pole to the roof of his vehicle. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A 71-year-old man was arrested in Florida.<br>2. The man tied a downed power pole to the roof of his vehicle.<br>3. The arrest is suspected of being related to grand theft. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The man was arrested on suspicion of grand theft.<br>2. A 71-year-old man was arrested on suspicion of grand theft.<br>3. The man was tied down to the roof of his vehicle. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A 71-year-old man was arrested on suspicion of grand theft after tying a downed power pole to the roof of his vehicle in Florida. | 1 |
| google/gemma-3-1b-it | 1. A 71-year-old Florida man was arrested on suspicion of grand theft.<br>2. The man was arrested in Florida.<br>3. The man was arrested on suspicion of grand theft.<br>4. The man was arrested after tying a downed power pole to the roof of his vehicle. | 4 |
| google/gemma-3-4b-it | 1. A 71-year-old man was arrested.<br>2. The man is from Florida.<br>3. The man was arrested on suspicion of grand theft.<br>4. The man tied a downed power pole to the roof of his vehicle. | 4 |
| gpt-3.5-turbo-0125 | 1. A 71-year-old Florida man was arrested on suspicion of grand theft.<br>2. The Florida man tied a downed power pole to the roof of his vehicle. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A 71-year-old Florida man was arrested on suspicion of grand theft.<br>2. The 71-year-old Florida man tied a downed power pole to the roof of his vehicle. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A 71-year-old Florida man was arrested on suspicion of grand theft.<br>2. A 71-year-old Florida man tied a downed power pole to the roof of his vehicle. | 2 |

---

## Sample ID: quantemp_190
**Original Claim**: ﻿﻿"Since Mayor Kennedy O’Brien took office Sayreville has issued 22,081 building permits! Now O’Brien is holding secret meetings with big developers."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits since Mayor Kennedy O’Brien took office.<br>3. Mayor Kennedy O’Brien is holding secret meetings with big developers. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits since Mayor Kennedy O’Brien took office.<br>3. Mayor Kennedy O’Brien is holding secret meetings with big developers. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Mayor Kennedy O'Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits.<br>3. Mayor Kennedy O'Brien is holding secret meetings with big developers. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Mayor Kennedy O'Brien took office in Sayreville.<br>2. Sayreville issued 22,081 building permits since Mayor Kennedy O'Brien took office.<br>3. Mayor Kennedy O'Brien is holding secret meetings with big developers in Sayreville. | 3 |
| google/gemma-3-1b-it | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits.<br>3. O’Brien is holding secret meetings with big developers. | 3 |
| google/gemma-3-4b-it | 1. Mayor Kennedy O’Brien took office.<br>2. Since Mayor Kennedy O’Brien took office, Sayreville has issued 22,081 building permits.<br>3. Now, Mayor Kennedy O’Brien is holding secret meetings with big developers. | 3 |
| gpt-3.5-turbo-0125 | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits since Mayor Kennedy O’Brien took office.<br>3. Mayor Kennedy O’Brien is holding secret meetings with big developers. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Since Mayor Kennedy O’Brien took office, Sayreville has issued 22,081 building permits.<br>2. Mayor Kennedy O’Brien is holding secret meetings with big developers. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Since Mayor Kennedy O’Brien took office, Sayreville has issued 22,081 building permits.<br>3. Now O’Brien is holding secret meetings with big developers. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Mayor Kennedy O’Brien took office in Sayreville.<br>2. Sayreville has issued 22,081 building permits since Mayor Kennedy O’Brien took office.<br>3. O’Brien is holding secret meetings with big developers. | 3 |

---

## Sample ID: quantemp_191
**Original Claim**: Two white men were doused in gasoline and set on fire by Black Lives Matter members, and the story was "censored" by the media.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was "censored" by the media. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was "censored" by the media. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was "censored" by the media. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was censored by the media. | 2 |
| google/gemma-3-1b-it | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was “censored” by the media. | 2 |
| google/gemma-3-4b-it | 1. Two white men were doused in gasoline.<br>2. The gasoline was poured on the two white men.<br>3. The two white men were set on fire.<br>4. Black Lives Matter members doused the two white men in gasoline.<br>5. Black Lives Matter members set the two white men on fire.<br>6. The story was censored by the media. | 6 |
| gpt-3.5-turbo-0125 | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story of two white men being doused in gasoline and set on fire by Black Lives Matter members was "censored" by the media. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Two white men were doused in gasoline by Black Lives Matter members.<br>2. Two white men were set on fire by Black Lives Matter members.<br>3. The story about two white men being doused in gasoline and set on fire by Black Lives Matter members was "censored" by the media. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was "censored" by the media. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Two white men were doused in gasoline and set on fire by Black Lives Matter members.<br>2. The story was "censored" by the media. | 2 |

---

## Sample ID: quantemp_192
**Original Claim**: Says Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| google/gemma-3-1b-it | 1. Bill Murray said “The best way to teach your kids about taxes is by eating 30% of their ice cream.” | 1 |
| google/gemma-3-4b-it | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| gpt-3.5-turbo-0125 | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Bill Murray said "The best way to teach your kids about taxes is by eating 30% of their ice cream." | 1 |

---

## Sample ID: quantemp_193
**Original Claim**: "If you took every penny of the 1 percent, including their dog, you wouldn't even begin to balance the budget."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. If you took every penny of the 1 percent, including their dog, the budget would not be balanced. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. If you took every penny of the 1 percent, including their dog, you wouldn't even begin to balance the budget. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The 1 percent refers to the United States.<br>2. The United States refers to the country.<br>3. You refers to the person.<br>4. You refers to the individual.<br>5. Every penny refers to the United States.<br>6. Every penny of the 1 percent includes their dog.<br>7. You wouldn't even begin to balance the budget if you took every penny of the 1 percent, including their dog. | 7 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The 1 percent refers to the 1 percent of the federal budget.<br>2. You refers to the United States government.<br>3. You refers to the United States government.<br>4. If you took every penny of the 1 percent, including their dog, you wouldn't even begin to balance the budget. | 4 |
| google/gemma-3-1b-it | 1. Every penny of the 1 percent was taken.<br>2. You wouldn’t even begin to balance the budget. | 2 |
| google/gemma-3-4b-it | 1. If you took every penny of the 1 percent.<br>2. Including their dog.<br>3. You wouldn't even begin to balance the budget. | 3 |
| gpt-3.5-turbo-0125 | 1. Every penny of the 1 percent was taken, including their dog.<br>2. Taking every penny of the 1 percent, including their dog, wouldn't even begin to balance the budget. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Taking every penny of the 1 percent, including their dog, would not even begin to balance the budget. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "If you took every penny of the 1 percent, including their dog, you wouldn't even begin to balance the budget." | 1 |

---

## Sample ID: quantemp_194
**Original Claim**: Video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A bridge in Labis, Malaysia's Johor state, was swept away by flood in March 2023. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The bridge in Labis, Malaysia's Johor state, was swept away by flood in March 2023.<br>2. Video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023.<br>3. The bridge in Labis, Malaysia's Johor state, was swept away by flood in March 2023. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A bridge in Labis, Malaysia's Johor state, was swept away by flood in March 2023.<br>2. Video shows a bridge in Labis, Malaysia's Johor state. | 2 |
| google/gemma-3-1b-it | 1. A bridge in Labis, Malaysia’s Johor state, was swept away by flood in March 2023. | 1 |
| google/gemma-3-4b-it | 1. There is a bridge in Labis, Malaysia.<br>2. Labis is in Johor state, Malaysia.<br>3. The bridge was swept away by flood.<br>4. The flood occurred in March 2023. | 4 |
| gpt-3.5-turbo-0125 | 1. The video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. A bridge in Labis, Malaysia's Johor state, was swept away by flood in March 2023. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows a bridge in Labis, Malaysia's Johor state, swept away by flood in March 2023. | 1 |

---

## Sample ID: quantemp_195
**Original Claim**: Fabric masks sanitize them by microwaving it for 2-3 minutes

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Fabric masks are sanitized by microwaving them for 2-3 minutes. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Fabric masks sanitize them by microwaving them for 2-3 minutes. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Fabric masks sanitize them by microwaving for 2-3 minutes.<br>2. Fabric masks sanitize them by microwaving for 2-3 minutes.<br>3. Fabric masks sanitize them by microwaving for 2-3 minutes.<br>4. Fabric masks sanitize them by microwaving for 2-3 minutes. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Fabric masks are sanitized by microwaving them for 2-3 minutes. | 1 |
| google/gemma-3-1b-it | 1. Fabric masks sanitize when microwaved for 2-3 minutes.<br>2. Microwaving fabric masks for 2-3 minutes sanitizes them. | 2 |
| google/gemma-3-4b-it | 1. Fabric masks sanitize it by microwaving it for 2-3 minutes. | 1 |
| gpt-3.5-turbo-0125 | 1. Fabric masks can be sanitized by microwaving them for 2-3 minutes. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Fabric masks can be sanitized by microwaving fabric masks for 2-3 minutes. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Fabric masks sanitize them by microwaving it for 2-3 minutes. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Fabric masks sanitize them by microwaving it for 2-3 minutes. | 1 |

---

## Sample ID: quantemp_196
**Original Claim**: In 1989, a senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In 1989, a senior U.N. environmental official said that entire nations could be wiped off the face of the Earth by rising sea levels.<br>2. In 1989, a senior U.N. environmental official said that rising sea levels could wipe entire nations off the face of the Earth.<br>3. In 1989, a senior U.N. environmental official said that entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In 1989, a senior U.N. environmental official said, "Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In 1989, a senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.” | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. In 1989, a senior U.N. environmental official said that entire nations could be wiped off the face of the Earth.<br>2. Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000. | 2 |
| google/gemma-3-1b-it | 1. A senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.” | 1 |
| google/gemma-3-4b-it | 1. In 1989, a senior U.N. environmental official said that.<br>2. Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000. | 2 |
| gpt-3.5-turbo-0125 | 1. In 1989, a senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.” | 1 |
| gpt-4.1-mini-2025-04-14 | 1. In 1989, a senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.” | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 1989, a senior U.N. environmental official said that entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In 1989, a senior U.N. environmental official said, “Entire nations could be wiped off the face of the Earth by rising sea levels if the global warming trend is not reversed by the year 2000.” | 1 |

---

## Sample ID: quantemp_197
**Original Claim**: The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move and was only for “photo ops.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite.<br>2. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move.<br>3. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite was only for “photo ops.” | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Leni Robredo rode a motorcycle pillion to get to her campaign rally.<br>2. The rally was in Cavite.<br>3. The rally was on March 4.<br>4. The rally was for photo ops. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite.<br>2. The motorcycle did not actually move.<br>3. The motorcycle was only for "photo ops." | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The motorcycle ridden by Vice President Leni Robredo was not moved to her campaign rally on March 4 in Cavite.<br>2. The motorcycle ridden by Vice President Leni Robredo was only for "photo ops."<br>3. The motorcycle ridden by Vice President Leni Robredo was ridden by her to her campaign rally on March 4 in Cavite. | 3 |
| google/gemma-3-1b-it | 1. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move.<br>2. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite.<br>3. The motorcycle Vice President Leni Robredo did not move.<br>4. The motorcycle Vice President Leni Robredo was only for photo ops. | 4 |
| google/gemma-3-4b-it | 1. The motorcycle Vice President Leni Robredo rode pillion.<br>2. The motorcycle ride was to get to her March 4 campaign rally.<br>3. The motorcycle ride was in Cavite.<br>4. The motorcycle did not actually move.<br>5. The motorcycle ride was only for “photo ops.” | 5 |
| gpt-3.5-turbo-0125 | 1. Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite.<br>2. The motorcycle Vice President Leni Robredo rode did not actually move.<br>3. The motorcycle Vice President Leni Robredo rode was only for "photo ops." | 3 |
| gpt-4.1-mini-2025-04-14 | 1. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move.<br>2. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite was only for “photo ops.” | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move.<br>2. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite was only for “photo ops.” | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite did not actually move.<br>2. The motorcycle Vice President Leni Robredo rode pillion to get to her March 4 campaign rally in Cavite was only for “photo ops.” | 2 |

---

## Sample ID: quantemp_198
**Original Claim**: “Overall, the economy is estimated to have expanded by 7.6% in 2021, a much stronger level from the contraction of 0.3% in 2020.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The economy expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020.<br>3. The expansion of the economy in 2021 was a much stronger level than the contraction in 2020. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. The economy is estimated to have contracted by 0.3% in 2020. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The economy expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |
| google/gemma-3-1b-it | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. A much stronger level of economic expansion occurred in 2021 compared to the contraction of 0.3% in 2020. | 2 |
| google/gemma-3-4b-it | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |
| gpt-3.5-turbo-0125 | 1. The economy expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Overall, the economy is estimated to have expanded by 7.6% in 2021.<br>2. Overall, the economy is estimated to have contracted by 0.3% in 2020.<br>3. The economy’s 7.6% expansion in 2021 is described as a much stronger level from the contraction of 0.3% in 2020. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. The economy is estimated to have expanded by 7.6% in 2021.<br>2. The economy contracted by 0.3% in 2020. | 2 |

---

## Sample ID: quantemp_199
**Original Claim**: The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis in 2021.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The photo does not show a Buddhist monk-shaped cloud in Taiwan during the Covid-19 crisis in 2021. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The photo does not show a Buddhist monk-shaped cloud.<br>2. The photo was taken in Taiwan.<br>3. The photo was taken during the Covid-19 crisis in 2021. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The photo does not show a Buddhist monk-shaped cloud in Taiwan during the Covid-19 crisis in 2021.<br>2. The photo shows a cloud in Taiwan during the Covid-19 crisis in 2021.<br>3. The photo shows a cloud in Taiwan during the Covid-19 crisis in 2021. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The photo does not show a Buddhist monk.<br>2. The photo does not show a cloud.<br>3. The photo does not show in Taiwan.<br>4. The photo does not show during the Covid-19 crisis.<br>5. The photo does not show in 2021. | 5 |
| google/gemma-3-1b-it | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis.<br>2. The photo does not show Buddhist monk-shaped cloud.<br>3. Covid-19 crisis in 2021. | 3 |
| google/gemma-3-4b-it | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan.<br>2. The photo does not show Buddhist monk-shaped cloud during Covid-19 crisis.<br>3. The photo does not show Buddhist monk-shaped cloud in Taiwan during 2021. | 3 |
| gpt-3.5-turbo-0125 | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis in 2021. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis in 2021. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis in 2021. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The photo does not show Buddhist monk-shaped cloud in Taiwan during Covid-19 crisis in 2021. | 1 |

---

## Sample ID: quantemp_200
**Original Claim**: Steve Mnuchin Said Americans Can Live on $1,200 for 10 Weeks?

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Steve Mnuchin is an American businessman.<br>2. Americans can live on $1,200 for 10 weeks. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| google/gemma-3-1b-it | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| google/gemma-3-4b-it | 1. Steve Mnuchin said Americans can live on $1,200.<br>2. The stated period for this is 10 weeks. | 2 |
| gpt-3.5-turbo-0125 | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Steve Mnuchin said Americans can live on $1,200 for 10 weeks. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Steve Mnuchin Said Americans Can Live on $1,200 for 10 Weeks? | 1 |

---

## Sample ID: quantemp_201
**Original Claim**: Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are single, childless adults. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are single, childless adults.<br>2. The United States has 4,000 counties.<br>3. The United States has 4,000 counties.<br>4. The United States has 4,000 counties.<br>5. The United States has 4,000 counties.<br>6. The United States has 4,000 counties.<br>7. The United States has 4,000 counties.<br>8. The United States has 4,000 counties.<br>9. The United States has 4,000 counties.<br>10. The United States has 4,000 counties.<br>11. The United States has 4,000 counties.<br>12. The United States has 4,000 counties.<br>13. The United States has 4,000 counties.<br>14. The United States has 4,000 counties.<br>15. The United States has 4,000 counties.<br>16. The United States has 4,000 counties.<br>17. The United States has 4,000 counties.<br>18. The United States has 4,000 counties.<br>19. The United States has 4,000 counties.<br>20. The United States has 4,000 counties.<br>21. The United States has 4,000 counties.<br>22. The United States has 4,000 counties.<br>23. The United | 23 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Eighty-five percent of single, childless adults in Florida will benefit from expanding Medicaid. | 1 |
| google/gemma-3-1b-it | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are “single, childless adults.” | 1 |
| google/gemma-3-4b-it | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults." | 1 |
| gpt-3.5-turbo-0125 | 1. Floridians who will benefit from expanding Medicaid are "single, childless adults."<br>2. Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults." | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Eighty-five percent of Floridians who will benefit from expanding Medicaid are "single, childless adults." | 1 |

---

## Sample ID: quantemp_202
**Original Claim**: On 9/11, BBC reported building collapse 26 minutes early; it was a pre-rigged demolition

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. On 9/11, BBC reported building collapse 26 minutes early.<br>2. BBC reported building collapse 26 minutes early; it was a pre-rigged demolition. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. On September 11, 2001, the BBC reported a building collapse 26 minutes early.<br>2. The BBC reported a building collapse 26 minutes early on September 11, 2001.<br>3. It was a pre-rigged demolition on September 11, 2001. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. On 9/11<br>2. BBC reported building collapse 26 minutes early<br>3. It was a pre-rigged demolition | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The BBC reported building collapse on 9/11.<br>2. BBC reported building collapse 26 minutes early on 9/11.<br>3. It was a pre-rigged demolition on 9/11. | 3 |
| google/gemma-3-1b-it | 1. BBC reported building collapse at 26 minutes.<br>2. On 9/11, BBC reported building collapse.<br>3. Building collapse occurred at 26 minutes. | 3 |
| google/gemma-3-4b-it | 1. On 9/11, BBC reported building collapse.<br>2. The collapse was reported 26 minutes early.<br>3. The collapse was a pre-rigged demolition. | 3 |
| gpt-3.5-turbo-0125 | 1. On 9/11, BBC reported building collapse 26 minutes early.<br>2. The building collapse on 9/11 was a pre-rigged demolition. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. On 9/11, BBC reported building collapse 26 minutes early.<br>2. The building collapse on 9/11 was a pre-rigged demolition. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. On 9/11, BBC reported building collapse 26 minutes early.<br>2. On 9/11, BBC reported that the building collapse was a pre-rigged demolition. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. On 9/11, BBC reported building collapse 26 minutes early.<br>2. On 9/11, BBC reported building collapse was a pre-rigged demolition. | 2 |

---

## Sample ID: quantemp_203
**Original Claim**: The United States accounted for 26 percent of worldwide military spending during the Cold War, but now accounts for 41 percent.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States accounted for 41 percent of worldwide military spending. | 2 |
| google/gemma-3-1b-it | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| google/gemma-3-4b-it | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States accounts for 41 percent of worldwide military spending now. | 2 |
| gpt-3.5-turbo-0125 | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States accounts for 41 percent of worldwide military spending now. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The United States accounted for 26 percent of worldwide military spending during the Cold War.<br>2. The United States now accounts for 41 percent of worldwide military spending. | 2 |

---

## Sample ID: quantemp_204
**Original Claim**: Image of a dead mother being carried by her son and husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Image of a dead mother being carried by her son and husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related oxygen crisis. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A dead mother is being carried by her son and husband on a bike.<br>2. The mother is dead.<br>3. The son and husband are carrying the mother.<br>4. The ambulance is unavailable.<br>5. India is experiencing a COVID-19 related oxygen crisis. | 5 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Image of a dead mother being carried by her son and husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis.<br>2. India’s COVID-19 related Oxygen crisis.<br>3. The unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An image of a dead mother was being carried by her son and husband on a bike in India.<br>2. The image was taken during India's COVID-19 related Oxygen crisis.<br>3. The image was taken amid India's COVID-19 related Oxygen crisis. | 3 |
| google/gemma-3-1b-it | 1. Image of a dead mother being carried by her son and husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis. | 1 |
| google/gemma-3-4b-it | 1. There is an image of a dead mother.<br>2. The mother is being carried by her son.<br>3. The mother is being carried by her husband.<br>4. The carrying is occurring on a bike.<br>5. The carrying is due to unavailability of an ambulance.<br>6. The unavailability of an ambulance is amid India’s COVID-19 related Oxygen crisis. | 6 |
| gpt-3.5-turbo-0125 | 1. An image of a dead mother being carried by her son and husband on a bike exists.<br>2. The dead mother was being carried by her son and husband on a bike due to unavailability of an ambulance.<br>3. The unavailability of an ambulance was amid India's COVID-19 related Oxygen crisis. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. A dead mother was carried by her son on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis.<br>2. A dead mother was carried by her husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. An image of a dead mother was carried by her son on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis.<br>2. An image of a dead mother was carried by her husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Image of a dead mother being carried by her son and husband on a bike due to unavailability of an ambulance amid India’s COVID-19 related Oxygen crisis. | 1 |

---

## Sample ID: quantemp_205
**Original Claim**: “There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach in what can only be considered a manufactured supply-chain halt.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. There are now 56 cargo freighters anchored off the coast of California.<br>2. The cargo freighters are anchored from Oakland to Long Beach.<br>3. The anchoring of 56 cargo freighters off the coast of California from Oakland to Long Beach can only be considered a manufactured supply-chain halt. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There are now 56 cargo freighters anchored off the coast of California.<br>2. The anchoring of these freighters is from Oakland to Long Beach.<br>3. This anchoring is considered a supply-chain halt. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. California<br>2. Oakland<br>3. Long Beach<br>4. Cargo freighters<br>5. Manufactured supply-chain | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. There are 56 cargo freighters anchored off the coast of California.<br>2. The cargo freighters are anchored off the coast of California.<br>3. The cargo freighters are from Oakland.<br>4. The cargo freighters are from Long Beach.<br>5. There is a manufactured supply-chain halt from Oakland to Long Beach. | 5 |
| google/gemma-3-1b-it | 1. There are now 56 cargo freighters anchored off the coast of California.<br>2. Cargo freighters are anchored off the coast of California.<br>3. The location is off the coast of California.<br>4. The location is Oakland to Long Beach.<br>5. A manufactured supply-chain halt is occurring. | 5 |
| google/gemma-3-4b-it | 1. There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach.<br>2. This is considered a manufactured supply-chain halt. | 2 |
| gpt-3.5-turbo-0125 | 1. There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach.<br>2. The situation can only be considered a manufactured supply-chain halt. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. There are 56 cargo freighters anchored off the coast of California from Oakland to Long Beach.<br>2. The 56 cargo freighters anchored off the coast of California from Oakland to Long Beach are in what can only be considered a manufactured supply-chain halt. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. “There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach in what can only be considered a manufactured supply-chain halt.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach.<br>2. There are now 56 cargo freighters anchored off the coast of California from Oakland to Long Beach in what can only be considered a manufactured supply-chain halt. | 2 |

---

## Sample ID: quantemp_206
**Original Claim**: Says the Florida House of Representatives allocated $24 billion, "the greatest investment in education in Florida history!"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives allocated $24 billion, "the greatest investment in education in Florida history!" | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives allocated "the greatest investment in education in Florida history!" | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Florida House of Representatives allocated $24 billion.<br>2. "The greatest investment in education in Florida history!" | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives allocated "the greatest investment in education in Florida history!" | 2 |
| google/gemma-3-1b-it | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives invested in education in Florida history. | 2 |
| google/gemma-3-4b-it | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives stated that $24 billion was "the greatest investment in education in Florida history!" | 2 |
| gpt-3.5-turbo-0125 | 1. The Florida House of Representatives allocated $24 billion.<br>2. The allocation is the greatest investment in education in Florida history. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives said that $24 billion is "the greatest investment in education in Florida history!" | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Says the Florida House of Representatives allocated $24 billion, "the greatest investment in education in Florida history!" | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The Florida House of Representatives allocated $24 billion.<br>2. The Florida House of Representatives allocated $24 billion is "the greatest investment in education in Florida history!" | 2 |

---

## Sample ID: quantemp_207
**Original Claim**: “This means 12.5 million additional Nigerians now have direct access to potable water.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This means 12.5 million additional Nigerians now have direct access to potable water. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 12.5 million Nigerians now have direct access to potable water. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nigerians now have direct access to potable water.<br>2. This means 12.5 million additional Nigerians now have direct access to potable water. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The statement was made by the President of Nigeria.<br>2. "This" refers to the President of Nigeria.<br>3. The President of Nigeria means 12.5 million additional Nigerians now have direct access to potable water. | 3 |
| google/gemma-3-1b-it | 1. “This means 12.5 million additional Nigerians now have direct access to potable water.” | 1 |
| google/gemma-3-4b-it | 1. This means 12.5 million additional Nigerians now have direct access to potable water. | 1 |
| gpt-3.5-turbo-0125 | 1. 12.5 million additional Nigerians now have direct access to potable water. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 12.5 million additional Nigerians now have direct access to potable water. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. “This means 12.5 million additional Nigerians now have direct access to potable water.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 12.5 million additional Nigerians now have direct access to potable water. | 1 |

---

## Sample ID: quantemp_208
**Original Claim**: SP/BJP bribing voters using Rs 500 in envelope

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. SP/BJP bribed voters using Rs 500 in envelope. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. SP/BJP is a political party.<br>2. SP/BJP is known for bribing voters.<br>3. SP/BJP is using Rs 500 in envelopes as a bribe. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Supreme Court of India.<br>2. The Bharat Janata Party.<br>3. Rs 500. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. SP/BJP bribed voters using Rs 500 in envelopes. | 1 |
| google/gemma-3-1b-it | 1. SP/BJP bribed voters with Rs 500 in envelopes.<br>2. Bribing voters with Rs 500 in envelopes is a fact. | 2 |
| google/gemma-3-4b-it | 1. SP is bribing voters.<br>2. BJP is bribing voters.<br>3. The bribery is using Rs 500.<br>4. The bribery is using envelopes. | 4 |
| gpt-3.5-turbo-0125 | 1. SP/BJP is bribing voters using Rs 500 in envelope. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. SP/BJP bribed voters using Rs 500 in envelope. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. SP/BJP bribing voters using Rs 500 in envelope | 1 |
| gpt-5.4-mini-2026-03-17 | 1. SP/BJP bribing voters using Rs 500 in envelope | 1 |

---

## Sample ID: quantemp_209
**Original Claim**: “According to the latest statistics 121,000 [teen] pregnancies were experienced in our country in 2019 …”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. According to the latest statistics, 121,000 teen pregnancies were experienced in our country in 2019. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. According to the latest statistics, 121,000 [teen] pregnancies were experienced in our country in 2019. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 121,000<br>2. Teen<br>3. 2019 | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. According to the latest statistics, 121,000 teenage pregnancies were experienced in our country in 2019. | 1 |
| google/gemma-3-1b-it | 1. 121,000 teenage pregnancies were experienced in our country in 2019. | 1 |
| google/gemma-3-4b-it | 1. 121,000 [teen] pregnancies were experienced in our country in 2019. | 1 |
| gpt-3.5-turbo-0125 | 1. 121,000 teen pregnancies were experienced in the country in 2019. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 121,000 teen pregnancies were experienced in our country in 2019. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. According to the latest statistics, 121,000 teen pregnancies were experienced in our country in 2019. | 1 |

---

## Sample ID: quantemp_210
**Original Claim**: "One of the reasons that Budweiser stayed in New Jersey is the money they got from RGGI to put solar on their roof to save on their energy costs."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. One of the reasons that Budweiser stayed in New Jersey is the money they got from RGGI.<br>2. Budweiser got money from RGGI.<br>3. The money Budweiser got from RGGI was used to put solar on their roof.<br>4. Putting solar on their roof saved Budweiser energy costs. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Budweiser stayed in New Jersey.<br>2. Budweiser received money from RGGI.<br>3. Budweiser put solar panels on their roof.<br>4. Budweiser saved on energy costs. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Budweiser stayed in New Jersey.<br>2. The money they got from RGGI to put solar on their roof to save on their energy costs. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Budweiser stayed in New Jersey.<br>2. One of the reasons Budweiser stayed in New Jersey is the money they got from RGGI.<br>3. Budweiser stayed in New Jersey to save on their energy costs.<br>4. Budweiser stayed in New Jersey to put solar on their roof. | 4 |
| google/gemma-3-1b-it | 1. Budweiser stayed in New Jersey due to money received from RGGI to install solar panels.<br>2. The money received from RGGI was used to put solar panels on the roof.<br>3. The solar panels saved on energy costs. | 3 |
| google/gemma-3-4b-it | 1. One of the reasons that Budweiser stayed in New Jersey is the money they got.<br>2. The money they got was from RGGI.<br>3. They put solar on their roof.<br>4. They did this to save on their energy costs. | 4 |
| gpt-3.5-turbo-0125 | 1. Budweiser stayed in New Jersey.<br>2. Budweiser got money from RGGI.<br>3. Budweiser used the money to put solar on their roof.<br>4. Putting solar on their roof helped Budweiser save on their energy costs. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Budweiser stayed in New Jersey.<br>2. Budweiser got money from RGGI to put solar on their roof to save on their energy costs.<br>3. One of the reasons that Budweiser stayed in New Jersey is the money Budweiser got from RGGI to put solar on their roof to save on their energy costs. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. One of the reasons that Budweiser stayed in New Jersey is the money they got from RGGI to put solar on their roof to save on their energy costs. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Budweiser stayed in New Jersey.<br>2. Budweiser got money from RGGI to put solar on Budweiser's roof.<br>3. Budweiser got money from RGGI to put solar on Budweiser's roof to save on Budweiser's energy costs. | 3 |

---

## Sample ID: quantemp_211
**Original Claim**: “But from 2013, and in only 7 years of my presidency, we have connected close to 3.5 million households, bringing the number of households connected close to 8 million.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. From 2013, and in only 7 years of my presidency, close to 3.5 million households were connected.<br>2. From 2013, and in only 7 years of my presidency, the number of households connected reached close to 8 million. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. From 2013, in only 7 years of my presidency, we have connected close to 3.5 million households.<br>2. In only 7 years of my presidency, we have connected close to 8 million households. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States has connected close to 3.5 million households since 2013.<br>2. The United States has connected close to 8 million households since 2013. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The year was 2013.<br>2. The number of years of the presidency was 7.<br>3. The president was Barack Obama.<br>4. We connected close to 3.5 million households.<br>5. We connected close to 8 million households. | 5 |
| google/gemma-3-1b-it | 1. “But from 2013, and in only 7 years of my presidency, we have connected close to 3.5 million households.”<br>2. “We have connected close to 3.5 million households.”<br>3. “The number of households connected close to 8 million has increased.” | 3 |
| google/gemma-3-4b-it | 1. From 2013, and in only 7 years of my presidency, we have connected close to 3.5 million households.<br>2. Bringing the number of households connected close to 8 million. | 2 |
| gpt-3.5-turbo-0125 | 1. The speaker's presidency started in 2013.<br>2. In only 7 years of the speaker's presidency, close to 3.5 million households have been connected.<br>3. The number of households connected is close to 8 million. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. From 2013, and in only 7 years of the presidency, close to 3.5 million households have been connected.<br>2. From 2013, and in only 7 years of the presidency, the number of households connected has been brought close to 8 million. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. From 2013, and in only 7 years of my presidency, we have connected close to 3.5 million households.<br>2. From 2013, and in only 7 years of my presidency, connecting close to 3.5 million households has brought the number of households connected close to 8 million. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. From 2013, and in only 7 years of my presidency, we have connected close to 3.5 million households.<br>2. From 2013, and in only 7 years of my presidency, the number of households connected is close to 8 million. | 2 |

---

## Sample ID: quantemp_212
**Original Claim**: “Nearly 80,000 land claims, totalling 3.4 million hectares, have been settled. 1.8 million people have benefited.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Nearly 80,000 land claims have been settled.<br>2. Nearly 80,000 land claims totalling 3.4 million hectares have been settled.<br>3. 1.8 million people have benefited from settled land claims. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nearly 80,000 land claims have been settled.<br>2. 3.4 million hectares of land have been settled.<br>3. 1.8 million people have benefited from the land claims. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nearly 80,000 land claims have been settled.<br>2. 3.4 million hectares have been settled.<br>3. 1.8 million people have been benefited. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. "Nearly 80,000 land claims have been settled.<br>2. The land claims were settled for 3.4 million hectares.<br>3. Nearly 80,000 land claims have benefited 1.8 million people. | 3 |
| google/gemma-3-1b-it | 1. Nearly 80,000 land claims have been settled.<br>2. A total of 3.4 million hectares has been settled.<br>3. 1.8 million people have benefited from the land claims. | 3 |
| google/gemma-3-4b-it | 1. Nearly 80,000 land claims have been settled.<br>2. The land claims total 3.4 million hectares.<br>3. 1.8 million people have benefited. | 3 |
| gpt-3.5-turbo-0125 | 1. Nearly 80,000 land claims have been settled.<br>2. The land claims total 3.4 million hectares.<br>3. 1.8 million people have benefited from the settled land claims. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Nearly 80,000 land claims have been settled.<br>2. Nearly 80,000 land claims total 3.4 million hectares.<br>3. 1.8 million people have benefited from the settlement of nearly 80,000 land claims. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Nearly 80,000 land claims have been settled.<br>2. Nearly 80,000 land claims totalling 3.4 million hectares have been settled.<br>3. 1.8 million people have benefited. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Nearly 80,000 land claims have been settled.<br>2. The nearly 80,000 land claims total 3.4 million hectares.<br>3. 1.8 million people have benefited. | 3 |

---

## Sample ID: quantemp_213
**Original Claim**: "When you look at the nearly 150 men and women who have served us on the Texas Supreme Court, more than half of them had zero prior judicial experience."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. When you look at the nearly 150 men and women who have served on the Texas Supreme Court, more than half of them had zero prior judicial experience. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. More than half of the individuals who have served on the Texas Supreme Court had zero prior judicial experience.<br>2. The Texas Supreme Court has approximately 150 individuals who have served on it. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Texas Supreme Court has nearly 150 members.<br>2. More than half of the nearly 150 members of the Texas Supreme Court had zero prior judicial experience. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The men who served on the Texas Supreme Court are 150.<br>2. The women who served on the Texas Supreme Court are 150.<br>3. The men who served on the Texas Supreme Court had zero prior judicial experience.<br>4. The women who served on the Texas Supreme Court had zero prior judicial experience. | 4 |
| google/gemma-3-1b-it | 1. The Texas Supreme Court has served approximately 150 men and women.<br>2. More than half of the men and women who have served on the Texas Supreme Court had zero prior judicial experience. | 2 |
| google/gemma-3-4b-it | 1. When you look at the nearly 150 men and women who have served on the Texas Supreme Court,<br>2. more than half of them had zero prior judicial experience. | 2 |
| gpt-3.5-turbo-0125 | 1. Nearly 150 men and women have served on the Texas Supreme Court.<br>2. More than half of the nearly 150 men and women who have served on the Texas Supreme Court had zero prior judicial experience. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Nearly 150 men and women have served on the Texas Supreme Court.<br>2. More than half of the nearly 150 men and women who have served on the Texas Supreme Court had zero prior judicial experience. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. When you look at the nearly 150 men and women who have served us on the Texas Supreme Court, more than half of them had zero prior judicial experience. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. When you look at the nearly 150 men and women who have served us on the Texas Supreme Court, more than half of the nearly 150 men and women who have served us on the Texas Supreme Court had zero prior judicial experience. | 1 |

---

## Sample ID: quantemp_214
**Original Claim**: A man was released from jail in Texas after outliving his 99-year prison sentence for horse theft.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A man was released from jail in Texas.<br>2. The man outlived his 99-year prison sentence for horse theft in Texas. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A man was released from jail in Texas.<br>2. The man was released after outliving his 99-year prison sentence for horse theft. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A man was released from jail in Texas after outliving his 99-year prison sentence for horse theft.<br>2. The man was released from jail in Texas after outliving his 99-year prison sentence for horse theft.<br>3. The man was released from jail in Texas after outliving his 99-year prison sentence for horse theft. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A man was released from jail in Texas.<br>2. A man was released from jail in Texas after outliving his 99-year prison sentence.<br>3. The man who was released from jail in Texas was released from jail in Texas after outliving his 99-year prison sentence for horse theft. | 3 |
| google/gemma-3-1b-it | 1. A man was released from jail in Texas.<br>2. A man was released from jail in Texas after outliving his 99-year prison sentence for horse theft. | 2 |
| google/gemma-3-4b-it | 1. A man was released from jail in Texas.<br>2. The man was released from jail after outliving his 99-year prison sentence.<br>3. The 99-year prison sentence was for horse theft. | 3 |
| gpt-3.5-turbo-0125 | 1. A man was released from jail in Texas.<br>2. The man outlived his 99-year prison sentence for horse theft. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A man was released from jail in Texas.<br>2. The man was released from jail in Texas after outliving his 99-year prison sentence for horse theft. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A man was released from jail in Texas.<br>2. A man outlived his 99-year prison sentence for horse theft. | 2 |

---

## Sample ID: quantemp_215
**Original Claim**: When Rick Scott "was deposed in lawsuits about his company, he took the Fifth 75 times."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. When Rick Scott was deposed in lawsuits about his company, he took the Fifth Amendment 75 times. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Rick Scott was deposed in lawsuits about his company.<br>2. Rick Scott took the Fifth 75 times. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Rick Scott was deposed in lawsuits about his company.<br>2. He took the Fifth 75 times. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Rick Scott was deposed in lawsuits about his company.<br>2. He took the Fifth 75 times. | 2 |
| google/gemma-3-1b-it | 1. Rick Scott was deposed in lawsuits about his company.<br>2. Rick Scott took the Fifth 75 times. | 2 |
| google/gemma-3-4b-it | 1. Rick Scott was deposed in lawsuits about his company.<br>2. He took the Fifth 75 times. | 2 |
| gpt-3.5-turbo-0125 | 1. Rick Scott was deposed in lawsuits about his company.<br>2. Rick Scott took the Fifth 75 times when he was deposed in lawsuits about his company. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Rick Scott was deposed in lawsuits about his company.<br>2. Rick Scott took the Fifth 75 times when Rick Scott was deposed in lawsuits about his company. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. When Rick Scott was deposed in lawsuits about his company, Rick Scott took the Fifth 75 times. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. When Rick Scott was deposed in lawsuits about his company, Rick Scott took the Fifth 75 times. | 1 |

---

## Sample ID: quantemp_216
**Original Claim**: Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam and caused losses worth 12,000 crores.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Dravida Munnetra Kazhagam (DMK) is a political party in India.<br>2. A. Raja is a member of the DMK political party.<br>3. A. Raja engaged in the 2G Scam.<br>4. The 2G Scam is a fraudulent scheme in India.<br>5. The 2G Scam caused losses worth 12,000 crores. | 5 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. A. Raja was involved in the 2G Scam.<br>3. A. Raja caused losses worth 12,000 crores. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |
| google/gemma-3-1b-it | 1. Dravida Munnetra Kazhagam’s (DMK) A. Raja engaged in the 2G Scam.<br>2. The 2G Scam caused losses worth 12,000 crores. | 2 |
| google/gemma-3-4b-it | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. A. Raja caused losses worth 12,000 crores. | 2 |
| gpt-3.5-turbo-0125 | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Dravida Munnetra Kazhagam's (DMK) A. Raja engaged in the 2G Scam.<br>2. Dravida Munnetra Kazhagam's (DMK) A. Raja caused losses worth 12,000 crores. | 2 |

---

## Sample ID: quantemp_217
**Original Claim**: "The laws governing Agenda 2030 land development allows the government to seize polluted lands and move their residents to … smart cities.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The laws governing Agenda 2030 land development allow the government to move residents of polluted lands to smart cities. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Agenda 2030 land development allows the government to seize polluted lands.<br>2. The government can move residents to smart cities from seized lands. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The laws governing Agenda 2030 allow the government to seize polluted lands.<br>2. The government can seize polluted lands.<br>3. The government can seize polluted lands to move residents to smart cities. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The laws governing Agenda 2030 land development allow the government to move the residents of polluted lands to smart cities. | 2 |
| google/gemma-3-1b-it | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The government can seize polluted lands.<br>3. The government allows the government to move residents to smart cities. | 3 |
| google/gemma-3-4b-it | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The government can move their residents to … smart cities. | 2 |
| gpt-3.5-turbo-0125 | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The laws governing Agenda 2030 land development allow the government to move residents to smart cities. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands.<br>2. The laws governing Agenda 2030 land development allow the government to move the residents of polluted lands to smart cities. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The laws governing Agenda 2030 land development allow the government to seize polluted lands and move their residents to … smart cities. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The laws governing Agenda 2030 land development allows the government to seize polluted lands.<br>2. The laws governing Agenda 2030 land development allows the government to move the residents of polluted lands to smart cities. | 2 |

---

## Sample ID: quantemp_218
**Original Claim**: Kola Abiola claimed National Security Council (NSC) has not met since 1999

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Kola Abiola claimed the National Security Council (NSC) has not met since 1999. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Kola Abiola claimed that the National Security Council (NSC) has not met since 1999. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| google/gemma-3-1b-it | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| google/gemma-3-4b-it | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| gpt-3.5-turbo-0125 | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Kola Abiola claimed that the National Security Council (NSC) has not met since 1999. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Kola Abiola claimed National Security Council (NSC) has not met since 1999. | 1 |

---

## Sample ID: quantemp_219
**Original Claim**: "About 80 percent of (the manufacturing and agriculture) tax credit goes to claimants who are making $1 million or more."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more.<br>2. The manufacturing and agriculture tax credit is a government program that provides financial assistance to businesses. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The manufacturing and agriculture tax credit goes to claimants who are making $1 million or more.<br>2. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The manufacturing and agriculture tax credit is 80 percent.<br>2. The manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 2 |
| google/gemma-3-1b-it | 1. About 80 percent of (the manufacturing and agriculture) tax credit goes to claimants who are making $1 million or more. | 1 |
| google/gemma-3-4b-it | 1. About 80 percent of (the manufacturing and agriculture) tax credit goes to claimants.<br>2. The claimants are making $1 million or more. | 2 |
| gpt-3.5-turbo-0125 | 1. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. About 80 percent of the (manufacturing and agriculture) tax credit goes to claimants who are making $1 million or more. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. About 80 percent of the manufacturing and agriculture tax credit goes to claimants who are making $1 million or more. | 1 |

---

## Sample ID: quantemp_220
**Original Claim**: Newspaper clipping about UP BJP government introducing 6% GST on Sunday Church Mass offertory money

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A newspaper clipping about the UP BJP government introducing 6% GST on Sunday Church Mass offertory money exists. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A newspaper clipping is about the UP BJP government introducing 6% GST on Sunday Church Mass offertory money. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United Progressive BJP government introduced 6% GST on Sunday Church Mass offertory money.<br>2. Newspaper clipping about UP BJP government introducing 6% GST on Sunday Church Mass offertory money. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Newspaper clipping exists.<br>2. The UP BJP government introduced a 6% GST on Sunday Church Mass offertory money. | 2 |
| google/gemma-3-1b-it | 1. Newspaper clipping about the UP BJP government introducing a 6% GST on Sunday Church Mass offertory money. | 1 |
| google/gemma-3-4b-it | 1. There is a newspaper clipping.<br>2. The UP BJP government introduced 6% GST on Sunday Church Mass offertory money. | 2 |
| gpt-3.5-turbo-0125 | 1. The UP BJP government introduced 6% GST on Sunday Church Mass offertory money. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The UP BJP government introduced 6% GST on Sunday Church Mass offertory money. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Newspaper clipping about UP BJP government introducing 6% GST on Sunday Church Mass offertory money | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Newspaper clipping about UP BJP government introducing 6% GST on Sunday Church Mass offertory money | 1 |

---

## Sample ID: quantemp_221
**Original Claim**: The United States has "10,000 IRS agents making sure that you don't take an improper charity deduction," but to fight terrorism, it has "less than two dozen people focusing on countering violent extremism at home."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The United States has 10,000 IRS agents making sure that you don't take an improper charity deduction.<br>2. The United States has less than two dozen people focusing on countering violent extremism at home. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The United States has "10,000 IRS agents making sure that you don't take an improper charity deduction."<br>2. The United States has "less than two dozen people focusing on countering violent extremism at home." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States has 10,000 IRS agents.<br>2. The United States has less than two dozen people focusing on countering violent extremism at home. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The United States has 10,000 IRS agents.<br>2. The United States has less than two dozen people.<br>3. The United States has agents focusing on countering violent extremism at home. | 3 |
| google/gemma-3-1b-it | 1. The United States has “10,000 IRS agents” making sure that you don’t take an improper charity deduction.<br>2. The United States has “less than two dozen people” focusing on countering violent extremism at home. | 2 |
| google/gemma-3-4b-it | 1. The United States has 10,000 IRS agents.<br>2. The IRS agents are making sure that you don't take an improper charity deduction.<br>3. The United States has less than two dozen people.<br>4. The people are focusing on countering violent extremism at home. | 4 |
| gpt-3.5-turbo-0125 | 1. The United States has "10,000 IRS agents making sure that you don't take an improper charity deduction."<br>2. The United States has "less than two dozen people focusing on countering violent extremism at home." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The United States has 10,000 IRS agents making sure that you don't take an improper charity deduction.<br>2. The United States has less than two dozen people focusing on countering violent extremism at home to fight terrorism. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The United States has "10,000 IRS agents making sure that you don't take an improper charity deduction."<br>2. The United States has "less than two dozen people focusing on countering violent extremism at home." | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The United States has "10,000 IRS agents making sure that you don't take an improper charity deduction."<br>2. The United States has "less than two dozen people focusing on countering violent extremism at home." | 2 |

---

## Sample ID: quantemp_222
**Original Claim**: There is "more oil produced at home than we buy from the rest of the world – the first time that’s happened in nearly 20 years."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. More oil is produced at home than is bought from the rest of the world.<br>2. The first time that more oil is produced at home than is bought from the rest of the world occurred in nearly 20 years. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There is "more oil produced at home than we buy from the rest of the world."<br>2. The first time that's happened in nearly 20 years. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States is the world's largest oil producer.<br>2. The United States is the world's largest oil producer.<br>3. The United States is the world's largest oil producer.<br>4. The United States is the world's largest oil producer.<br>5. The United States is the world's largest oil producer.<br>6. The United States is the world's largest oil producer.<br>7. The United States is the world's largest oil producer.<br>8. The United States is the world's largest oil producer.<br>9. The United States is the world's largest oil producer.<br>10. The United States is the world's largest oil producer.<br>11. The United States is the world's largest oil producer.<br>12. The United States is the world's largest oil producer.<br>13. The United States is the world's largest oil producer.<br>14. The United States is the world's largest oil producer.<br>15. The United States is the world's largest oil producer.<br>16. The United States is the world's largest oil producer.<br>17. The United States is the world's largest oil producer.<br>18. The United States is the world's largest oil producer.<br>19. The United States is the world's largest oil producer.<br>20. The United States is the world's largest oil producer.<br>21. The United States is the world's largest oil producer.<br>22. The United States | 22 |
| meta-llama/Llama-3.2-3B-Instruct | 1. There is more oil produced at home than is bought from the rest of the world.<br>2. The first time that's happened is in nearly 20 years. | 2 |
| google/gemma-3-1b-it | 1. There is more oil produced at home than the rest of the world.<br>2. There is a record of increased oil production at home in nearly 20 years. | 2 |
| google/gemma-3-4b-it | 1. There is more oil produced at home.<br>2. That happened in the rest of the world.<br>3. That happened in nearly 20 years. | 3 |
| gpt-3.5-turbo-0125 | 1. More oil is produced at home than is bought from the rest of the world.<br>2. More oil is produced at home than is bought from the rest of the world for the first time in nearly 20 years. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. More oil is produced at home than is bought from the rest of the world.<br>2. More oil is produced at home than is bought from the rest of the world for the first time in nearly 20 years. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. There is more oil produced at home than we buy from the rest of the world.<br>2. The first time that more oil produced at home than we buy from the rest of the world has happened is nearly 20 years. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. There is more oil produced at home than we buy from the rest of the world.<br>2. There is more oil produced at home than we buy from the rest of the world for the first time in nearly 20 years. | 2 |

---

## Sample ID: quantemp_223
**Original Claim**: Every year here in the rain a 15 feet snake covers the statue of Lord Buddha. Watch this video to believe its truth.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Every year in the rain a 15 feet snake covers the statue of Lord Buddha. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Every year, a 15-foot snake covers the statue of Lord Buddha.<br>2. Watch this video to believe its truth. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The statue of Lord Buddha is located in the city of Bangkok.<br>2. Every year, a 15 feet snake covers the statue of Lord Buddha.<br>3. The statue of Lord Buddha is located in the city of Bangkok. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The statue of Lord Buddha is located here.<br>2. Every year here in the rain a 15 feet snake covers the statue of Lord Buddha.<br>3. There is a snake that covers the statue of Lord Buddha here.<br>4. A 15 feet snake covers the statue of Lord Buddha here. | 4 |
| google/gemma-3-1b-it | 1. Every year here in the rain a 15 feet snake covers the statue of Lord Buddha.<br>2. Watching this video will likely confirm the truth. | 2 |
| google/gemma-3-4b-it | 1. Every year here in the rain a 15 feet snake covers the statue of Lord Buddha.<br>2. Watch this video to believe its truth. | 2 |
| gpt-3.5-turbo-0125 | 1. Every year in the rain, a 15 feet snake covers the statue of Lord Buddha. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Every year in the rain, a 15 feet snake covers the statue of Lord Buddha. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Every year here in the rain a 15 feet snake covers the statue of Lord Buddha. | 1 |

---

## Sample ID: quantemp_224
**Original Claim**: Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government".<br>2. Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first". | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government."<br>2. Thomas Jefferson wrote that "let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first."<br>2. Thomas Jefferson is a 3rd U.S. President.<br>3. Thomas Jefferson is a 3rd U.S. President.<br>4. Thomas Jefferson is a U.S. President.<br>5. Thomas Jefferson is a U.S. President.<br>6. Thomas Jefferson is a U.S. President.<br>7. Thomas Jefferson is a U.S. President.<br>8. Thomas Jefferson is a U.S. President.<br>9. Thomas Jefferson is a U.S. President.<br>10. Thomas Jefferson is a U.S. President.<br>11. Thomas Jefferson is a U.S. President.<br>12. Thomas Jefferson is a U.S. President.<br>13. Thomas Jefferson is a U.S. President.<br>14. Thomas Jefferson is a U.S. President.<br>15. Thomas Jefferson is a U.S. President.<br>16. Thomas Jefferson is a U.S. President.<br>17. Thomas Jefferson is a U.S. President.<br>18. Thomas Jefferson is a U.S. President.<br>19. Thomas Jefferson is a U.S. President.<br>20. Thomas Jefferson is a U.S. President.<br>21. Thomas Jefferson is a U.S. President.<br>22. Thomas Jefferson is a U.S | 22 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Thomas Jefferson wrote that.<br>2. The two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first. | 2 |
| google/gemma-3-1b-it | 1. Thomas Jefferson wrote that “the two enemies of the people are criminals and government.”<br>2. Thomas Jefferson wrote that “the two enemies of the people are criminals and government.”<br>3. Let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first. | 3 |
| google/gemma-3-4b-it | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government".<br>2. Thomas Jefferson wrote that "so let us tie the second down with the chains of the constitution".<br>3. Thomas Jefferson wrote that "so the second will not become the legalized version of the first". | 3 |
| gpt-3.5-turbo-0125 | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government."<br>2. Thomas Jefferson wrote that "let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first." | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Thomas Jefferson wrote that "the two enemies of the people are criminals and government, so let us tie the second down with the chains of the constitution so the second will not become the legalized version of the first." | 1 |

---

## Sample ID: quantemp_225
**Original Claim**: Joe Biden is offereing undocumented immigrants free six-month motels stays and $1,100 of Greyhound bus vouchers.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Joe Biden is offering undocumented immigrants free six-month motel stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Joe Biden is offering undocumented immigrants free six-month motels stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Joe Biden is offering undocumented immigrants free six-month motels stays and $1,100 of Greyhound bus vouchers. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Joe Biden is offering undocumented immigrants free six-month motel stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 in Greyhound bus vouchers. | 2 |
| google/gemma-3-1b-it | 1. Joe Biden is offering undocumented immigrants free six-month motels stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| google/gemma-3-4b-it | 1. Joe Biden is offering undocumented immigrants free six-month motel stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| gpt-3.5-turbo-0125 | 1. Joe Biden is offering undocumented immigrants free six-month motel stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Joe Biden is offering undocumented immigrants free six-month motel stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Joe Biden is offering undocumented immigrants free six-month motels stays.<br>2. Joe Biden is offering undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Joe Biden is offereing undocumented immigrants free six-month motels stays.<br>2. Joe Biden is offereing undocumented immigrants $1,100 of Greyhound bus vouchers. | 2 |

---

## Sample ID: quantemp_226
**Original Claim**: The Prime Minister may not have had Covid-19 and when he was admitted to hospital staff were asked to sign the Official Secrets Act and two who refused were dismissed.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. Two staff members who refused to sign the Official Secrets Act were dismissed. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. Two staff members who refused to sign the Official Secrets Act were dismissed. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Prime Minister may not have had Covid-19.<br>2. The Prime Minister was admitted to hospital.<br>3. The Prime Minister was asked to sign the Official Secrets Act.<br>4. Two staff members were dismissed. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Prime Minister may not have had Covid-19.<br>2. The Prime Minister was admitted to hospital.<br>3. Staff were asked to sign the Official Secrets Act when the Prime Minister was admitted to hospital.<br>4. Two staff who refused to sign the Official Secrets Act were dismissed. | 4 |
| google/gemma-3-1b-it | 1. The Prime Minister may not have had Covid-19.<br>2. The official secrets act was signed by the Prime Minister.<br>3. The Official Secrets Act was signed by the Prime Minister.<br>4. Two individuals were dismissed as a result of refusing to sign the official secrets act. | 4 |
| google/gemma-3-4b-it | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. Two who refused to sign the Official Secrets Act were dismissed. | 3 |
| gpt-3.5-turbo-0125 | 1. The Prime Minister may not have had Covid-19.<br>2. The Prime Minister was admitted to hospital.<br>3. Staff were asked to sign the Official Secrets Act when the Prime Minister was admitted to hospital.<br>4. Two staff members who refused to sign the Official Secrets Act were dismissed. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. Two staff who refused to sign the Official Secrets Act when the Prime Minister was admitted to hospital were dismissed. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. When staff were asked to sign the Official Secrets Act, two who refused were dismissed. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. The Prime Minister may not have had Covid-19.<br>2. When the Prime Minister was admitted to hospital, staff were asked to sign the Official Secrets Act.<br>3. When the Prime Minister was admitted to hospital, two staff who refused to sign the Official Secrets Act were dismissed. | 3 |

---

## Sample ID: quantemp_227
**Original Claim**: Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“, weil 2014 beschlossen worden sei, Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“.<br>2. 2014 wurde beschlossen, Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Bundesregierung provided financial assistance to the affected individuals.<br>2. The financial assistance provided by the Bundesregierung was insufficient.<br>3. The financial assistance provided by the Bundesregierung was insufficient because 2014 was the year when the funds from the Flood Relief Fund were allocated to refugees. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Bundesregierung (German government) provided financial assistance to affected people in 2014.<br>2. Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben (Financial assistance from the Fluthilfe-Fonds for refugees) was provided by the Bundesregierung. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Hilfen der Bundesregierung für die Betroffenen des Hochwassers were "so gering" in 2014.<br>2. 2014 was decided to distribute Geld aus dem Fluthilfe-Fonds für Geflüchtete.<br>3. The Hilfen der Bundesregierung für die Betroffenen des Hochwassers were for the refugees. | 3 |
| google/gemma-3-1b-it | 1. Die Bundesregierung hat für die Betroffenen des Hochwassers Geld aus dem Fluthilfe-Fonds für Geflüchtete ausgegeben.<br>2. Die Summe des Geldes aus dem Fluthilfe-Fonds für Geflüchtete ist gering.<br>3. Die Entscheidung wurde 2014 getroffen. | 3 |
| google/gemma-3-4b-it | 1. The aids of the Federal Government for the affected persons of the flood were “so small”.<br>2. The aids of the Federal Government for the affected persons of the flood were decided in 2014.<br>3. The money from the flood aid fund was being spent for refugees from 2014. | 3 |
| gpt-3.5-turbo-0125 | 1. The Bundesregierung's aid for the flood victims is "so low".<br>2. The decision to spend money from the Fluthilfe-Fonds on refugees was made in 2014. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“.<br>2. Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“, weil 2014 beschlossen worden sei, Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“.<br>2. Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“, weil 2014 beschlossen worden sei, Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Die Hilfen der Bundesregierung für die Betroffenen des Hochwassers seien „so gering“.<br>2. 2014 beschlossen worden sei, Geld aus dem Fluthilfe-Fonds für Geflüchtete auszugeben. | 2 |

---

## Sample ID: quantemp_228
**Original Claim**: "One in three people who’s receiving treatment for (opioid) drug problems gets some help from Medicaid to pay for that."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. One in three people who is receiving treatment for opioid drug problems gets some help from Medicaid to pay for that treatment. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "One in three people who’s receiving treatment for (opioid) drug problems gets some help from Medicaid to pay for that." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. One in three people who are receiving treatment for opioid drug problems gets some help from Medicaid to pay for that. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. One person out of three who is receiving treatment for opioid drug problems gets some help from Medicaid to pay for that. | 1 |
| google/gemma-3-1b-it | 1. One in three people who’s receiving treatment for (opioid) drug problems gets some help from Medicaid to pay for that. | 1 |
| google/gemma-3-4b-it | 1. One in three people who’s receiving treatment for (opioid) drug problems gets some help.<br>2. That help is from Medicaid.<br>3. Medicaid is used to pay for that. | 3 |
| gpt-3.5-turbo-0125 | 1. One in three people who are receiving treatment for opioid drug problems gets some help from Medicaid to pay for that. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. One in three people who is receiving treatment for (opioid) drug problems gets some help from Medicaid to pay for that. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 40mg/day dosage of folic acid does not affect chronic kidney disease (CKD) progression.<br>2. 2mg/day dosage of vitamin B12 does not affect chronic kidney disease (CKD) progression. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. One in three people who’s receiving treatment for (opioid) drug problems gets some help from Medicaid to pay for that. | 1 |

---

## Sample ID: quantemp_229
**Original Claim**: The Civics Secures Democracy Act “would allow the Biden administration to buy off states with $6 billion” if they adopt critical race theory.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion.<br>2. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion if they adopt critical race theory. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion.<br>2. If states adopt critical race theory, the Biden administration would be able to buy off the states with $6 billion. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion if they adopt critical race theory.<br>2. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>3. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>4. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>5. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>6. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>7. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>8. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>9. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off states with $6 billion.<br>10. The Biden administration has the authority to use the Civil Rights Act of 1964 to buy off | 10 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion.<br>2. The Biden administration would allow states to buy off with $6 billion if they adopt critical race theory. | 2 |
| google/gemma-3-1b-it | 1. The Civics Secures Democracy Act “would allow the Biden administration to buy off states with $6 billion”<br>2. The Biden administration is currently engaging in critical race theory. | 2 |
| google/gemma-3-4b-it | 1. The Civics Secures Democracy Act “would allow” the Biden administration to buy off states.<br>2. The Civics Secures Democracy Act “would allow” the Biden administration to buy off states with $6 billion.<br>3. The Biden administration “would allow” the purchase of states.<br>4. The purchase of states would be dependent on states adopting critical race theory. | 4 |
| gpt-3.5-turbo-0125 | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion if they adopt critical race theory. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion if the states adopt critical race theory. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. The Civics Secures Democracy Act would allow the Biden administration to buy off states with $6 billion if they adopt critical race theory. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The Civics Secures Democracy Act “would allow the Biden administration to buy off states with $6 billion” if states adopt critical race theory. | 1 |

---

## Sample ID: quantemp_230
**Original Claim**: Visuals of a woman flashing at FIFA world cup 2022 held in Qatar

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Visuals of a woman flashing at the FIFA World Cup 2022 held in Qatar. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A woman is flashing.<br>2. The FIFA World Cup 2022 is held in Qatar.<br>3. The visuals show a woman flashing at the FIFA World Cup 2022. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The FIFA World Cup 2022 was held in Qatar.<br>2. A woman flashed at the FIFA World Cup 2022.<br>3. The woman flashed at the FIFA World Cup 2022 was held in Qatar. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The FIFA World Cup 2022 was held in Qatar.<br>2. The FIFA World Cup 2022 featured visuals of a woman.<br>3. A woman flashed at the FIFA World Cup 2022 in Qatar. | 3 |
| google/gemma-3-1b-it | 1. Visuals of a woman flashing at FIFA World Cup 2022 held in Qatar. | 1 |
| google/gemma-3-4b-it | 1. There are visuals of a woman flashing at FIFA world cup 2022.<br>2. The FIFA world cup 2022 was held in Qatar. | 2 |
| gpt-3.5-turbo-0125 | 1. A woman flashed at FIFA World Cup 2022.<br>2. FIFA World Cup 2022 was held in Qatar. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Visuals of a woman flashing were recorded at FIFA world cup 2022 held in Qatar. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Visuals of a woman flashing at FIFA world cup 2022 were held in Qatar. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Visuals of a woman flashing at FIFA world cup 2022 held in Qatar. | 1 |

---

## Sample ID: quantemp_231
**Original Claim**: President Trump's losing the election despite receiving millions more votes in 2020 than in 2016 is indicative of a "rigged election."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. President Trump lost the election in 2020.<br>2. President Trump received millions more votes in 2020 than in 2016.<br>3. President Trump's losing the election in 2020 despite receiving millions more votes than in 2016 is indicative of a "rigged election." | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. President Trump's losing the election in 2020 is indicative of a "rigged election." | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. President Trump lost the election in 2020 despite receiving more votes than in 2016.<br>2. The United States presidential election in 2020 was lost by President Trump.<br>3. The United States presidential election in 2020 was lost by President Trump despite receiving more votes than in 2016. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. President Trump lost the 2020 US presidential election.<br>2. President Trump received more votes in the 2020 US presidential election than in the 2016 US presidential election.<br>3. The 2020 US presidential election was not rigged. | 3 |
| google/gemma-3-1b-it | 1. President Trump’s losing the election.<br>2. Receiving millions more votes in 2020 than in 2016 is indicative of a “rigged election.” | 2 |
| google/gemma-3-4b-it | 1. President Trump lost the election in 2020.<br>2. President Trump received millions more votes in 2020 than in 2016.<br>3. The statement “rigged election” is being used. | 3 |
| gpt-3.5-turbo-0125 | 1. President Trump lost the election in 2020.<br>2. President Trump received millions more votes in 2020 than in 2016.<br>3. President Trump losing the election despite receiving millions more votes in 2020 than in 2016 is indicative of a "rigged election." | 3 |
| gpt-4.1-mini-2025-04-14 | 1. President Trump lost the election in 2020.<br>2. President Trump received millions more votes in 2020 than in 2016.<br>3. President Trump's losing the election in 2020 despite receiving millions more votes in 2020 than in 2016 is indicative of a "rigged election." | 3 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. President Trump's losing the election in 2020 is indicative of a "rigged election."<br>2. President Trump received millions more votes in 2020 than in 2016. | 2 |

---

## Sample ID: quantemp_232
**Original Claim**: “Nancy Pelosi (purchased) 10,000 shares of Amgen, manufacturer of Nplate, a drug used to treat radiation sickness.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is a manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate, a drug used to treat radiation sickness. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is a drug used to treat radiation sickness.<br>3. Nancy Pelosi is a politician. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| google/gemma-3-1b-it | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is a manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| google/gemma-3-4b-it | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| gpt-3.5-turbo-0125 | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate, a drug used to treat radiation sickness. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Nancy Pelosi purchased 10,000 shares of Amgen.<br>2. Amgen is the manufacturer of Nplate.<br>3. Nplate is a drug used to treat radiation sickness. | 3 |

---

## Sample ID: quantemp_233
**Original Claim**: As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times "higher" than Tokyo's — and growing with time.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo's.<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo's and growing with time. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo's.<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo's. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. New York City<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo's — and growing with time.<br>3. Tokyo | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The COVID-19 coronavirus disease was prevalent in New York City as of April 25, 2020.<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than in Tokyo as of April 25, 2020.<br>3. The rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time as of April 25, 2020. | 3 |
| google/gemma-3-1b-it | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo’s.<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than Tokyo’s.<br>3. The rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time. | 3 |
| google/gemma-3-4b-it | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times "higher".<br>2. Tokyo's rate of people dying from the COVID-19 coronavirus disease was lower than New York City's rate of people dying from the COVID-19 coronavirus disease.<br>3. The rate of people dying from the COVID-19 coronavirus disease was growing with time in New York City. | 3 |
| gpt-3.5-turbo-0125 | 1. The rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times "higher" than Tokyo's as of April 25, 2020.<br>2. The rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time as of April 25, 2020. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times higher than the rate of people dying from the COVID-19 coronavirus disease in Tokyo.<br>2. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times "higher" than Tokyo's.<br>2. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was at least 250 times "higher" than Tokyo's.<br>2. As of April 25, 2020, the rate of people dying from the COVID-19 coronavirus disease in New York City was growing with time. | 2 |

---

## Sample ID: quantemp_234
**Original Claim**: Says Rep. Charles Bass "supports privatizing Social Security, risking trillions more on Wall Street."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Rep. Charles Bass supports privatizing Social Security.<br>2. Rep. Charles Bass risks trillions more on Wall Street. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Rep. Charles Bass says "supports privatizing Social Security."<br>2. Privatizing Social Security risks trillions more on Wall Street. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Says Rep. Charles Bass supports privatizing Social Security.<br>2. Rep. Charles Bass supports privatizing Social Security.<br>3. Rep. Charles Bass is a U.S. Representative for the state of Rhode Island.<br>4. Rep. Charles Bass is a U.S. Representative for the state of Rhode Island.<br>5. Rep. Charles Bass is a U.S. Representative for the state of Rhode Island. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Rep. Charles Bass says "supports privatizing Social Security, risking trillions more on Wall Street." | 1 |
| google/gemma-3-1b-it | 1. Rep. Charles Bass supports privatizing Social Security.<br>2. Risking trillions more on Wall Street is a consequence of privatizing Social Security. | 2 |
| google/gemma-3-4b-it | 1. Rep. Charles Bass says supports privatizing Social Security.<br>2. Privatizing Social Security is being risked.<br>3. Wall Street is receiving trillions more. | 3 |
| gpt-3.5-turbo-0125 | 1. Rep. Charles Bass supports privatizing Social Security.<br>2. Rep. Charles Bass is risking trillions more on Wall Street. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Rep. Charles Bass supports privatizing Social Security.<br>2. Rep. Charles Bass supports privatizing Social Security, risking trillions more on Wall Street. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Says Rep. Charles Bass supports privatizing Social Security, risking trillions more on Wall Street. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Rep. Charles Bass supports privatizing Social Security.<br>2. Rep. Charles Bass is risking trillions more on Wall Street. | 2 |

---

## Sample ID: quantemp_235
**Original Claim**: Daten aus Großbritannien würden zeigen, dass Geimpfte ein 885 Prozent höheres Risiko hätten, an Covid-19 zu sterben.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Daten aus Großbritannien würden zeigen, dass geimpfte Personen ein 885 Prozent höheres Risiko hätten, an Covid-19 zu sterben. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Daten aus Großbritannien würden zeigen, dass Geimpfte ein 885 Prozent höheres Risiko haben, an Covid-19 zu sterben. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United Kingdom is a country.<br>2. The UK is located in Europe.<br>3. The UK is a member of the European Union.<br>4. The UK is a member of the European Economic Area.<br>5. The UK is a member of the Schengen Area.<br>6. The UK is a member of the European Free Trade Association.<br>7. The UK is a member of the European Free Trade Association.<br>8. The UK is a member of the European Economic Area.<br>9. The UK is a member of the Schengen Area.<br>10. The UK is a member of the Schengen Area.<br>11. The UK is a member of the Schengen Area.<br>12. The UK is a member of the Schengen Area.<br>13. The UK is a member of the Schengen Area.<br>14. The UK is a member of the Schengen Area.<br>15. The UK is a member of the Schengen Area.<br>16. The UK is a member of the Schengen Area.<br>17. The UK is a member of the Schengen Area.<br>18. The UK is a member of the Schengen Area.<br>19. The UK is a member of the Schengen Area.<br>20. The UK is a member of the Schengen Area.<br>21. The UK is a member of the Scheng | 21 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Vaccines from the United Kingdom will show that unvaccinated individuals have an 885 percent higher risk of dying from Covid-19. | 1 |
| google/gemma-3-1b-it | 1. Daten aus Großbritannien würden zeigen, dass Geimpfte ein höheres Risiko haben, an Covid-19 zu sterben. | 1 |
| google/gemma-3-4b-it | 1. Daten from Großbritannien would show that the vaccinated would have an 885 percent higher risk of dying from Covid-19. | 1 |
| gpt-3.5-turbo-0125 | 1. Daten aus Großbritannien zeigen, dass Geimpfte ein 885 Prozent höheres Risiko haben, an Covid-19 zu sterben. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Daten aus Großbritannien würden zeigen, dass Geimpfte ein 885 Prozent höheres Risiko hätten, an Covid-19 zu sterben. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Daten aus Großbritannien würden zeigen, dass Geimpfte ein 885 Prozent höheres Risiko hätten, an Covid-19 zu sterben. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Daten aus Großbritannien würden zeigen, dass Geimpfte ein 885 Prozent höheres Risiko hätten, an Covid-19 zu sterben. | 1 |

---

## Sample ID: quantemp_236
**Original Claim**: A photograph captures a rare seven-headed snake found in Honduras.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photograph captures a rare seven-headed snake.<br>2. The seven-headed snake is found in Honduras. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photograph captures a rare seven-headed snake.<br>2. The photograph was taken in Honduras. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Honduras<br>2. A photograph captures a rare seven-headed snake found in Honduras<br>3. The photograph was taken in Honduras | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A photograph captures a seven-headed snake in Honduras.<br>2. A photograph captures a rare seven-headed snake in Honduras. | 2 |
| google/gemma-3-1b-it | 1. A photograph captures a rare seven-headed snake found in Honduras. | 1 |
| google/gemma-3-4b-it | 1. A photograph captures a rare seven-headed snake.<br>2. The snake was found in Honduras. | 2 |
| gpt-3.5-turbo-0125 | 1. A photograph captures a rare seven-headed snake found in Honduras. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A photograph captures a rare seven-headed snake found in Honduras. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A photograph captures a rare seven-headed snake found in Honduras. | 1 |

---

## Sample ID: quantemp_237
**Original Claim**: Any country joining the European Union must have a fiscal deficit at three per cent or below.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below.<br>2. The European Union is a country.<br>3. The European Union is a member of the European Economic Area (EEA).<br>4. The EEA is a part of the European Union.<br>5. The European Union is a member of the European Economic Area (EEA).<br>6. The European Union is a member of the European Economic Area (EEA).<br>7. The European Union is a member of the European Economic Area (EEA).<br>8. The European Union is a member of the European Economic Area (EEA).<br>9. The European Union is a member of the European Economic Area (EEA).<br>10. The European Union is a member of the European Economic Area (EEA).<br>11. The European Union is a member of the European Economic Area (EEA).<br>12. The European Union is a member of the European Economic Area (EEA).<br>13. The European Union is a member of the European Economic Area (EEA).<br>14. The European Union is a member of the European Economic Area (EEA).<br>15. The European Union is a member of the European Economic Area (EEA).<br>16. The European Union is a member of the European Economic Area (EEA).<br>17. The European Union is a member of the | 17 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| google/gemma-3-1b-it | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below.<br>2. A fiscal deficit must be at three per cent or below. | 2 |
| google/gemma-3-4b-it | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| gpt-3.5-turbo-0125 | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Any country joining the European Union must have a fiscal deficit at three per cent or below. | 1 |

---

## Sample ID: quantemp_238
**Original Claim**: “They say the ocean will rise one eighth of an inch over the next two hundred to three hundred years.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. They say the ocean will rise one eighth of an inch.<br>2. The ocean will rise one eighth of an inch over the next two hundred years.<br>3. The ocean will rise one eighth of an inch over the next three hundred years. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The ocean will rise one eighth of an inch over the next two hundred to three hundred years. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The ocean will rise one eighth of an inch over the next two hundred to three hundred years.<br>2. They say the ocean will rise one eighth of an inch over the next two hundred to three hundred years. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The ocean will rise one eighth of an inch over the next two hundred years.<br>2. They say the ocean will rise one eighth of an inch over the next three hundred years. | 2 |
| google/gemma-3-1b-it | 1. “They say the ocean will rise one eighth of an inch over the next two hundred to three hundred years.” | 1 |
| google/gemma-3-4b-it | 1. They say the ocean will rise one eighth of an inch over the next two hundred years.<br>2. They say the ocean will rise one eighth of an inch over the next three hundred years. | 2 |
| gpt-3.5-turbo-0125 | 1. The ocean will rise one eighth of an inch over the next two hundred to three hundred years. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The ocean will rise one eighth of an inch over the next two hundred to three hundred years. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The ocean will rise one eighth of an inch over the next two hundred to three hundred years. | 1 |

---

## Sample ID: quantemp_239
**Original Claim**: A list shows over 14,000 dead people voted in Wayne County, Michigan.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A list shows over 14,000 dead people in Wayne County, Michigan.<br>2. Over 14,000 dead people have been voted in Wayne County, Michigan. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Wayne County, Michigan<br>2. Over 14,000 dead people voted in Wayne County, Michigan | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan.<br>2. The people on the list are deceased.<br>3. The list is in Wayne County, Michigan.<br>4. The people on the list voted. | 4 |
| google/gemma-3-1b-it | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |
| google/gemma-3-4b-it | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |
| gpt-3.5-turbo-0125 | 1. The list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A list shows over 14,000 dead people voted in Wayne County, Michigan. | 1 |

---

## Sample ID: quantemp_240
**Original Claim**: On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump," and then quickly corrected himself.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump".<br>2. On June 16, 2021, U.S. President Joe Biden quickly corrected himself after mistakenly referring to Russian President Vladimir Putin as "President Trump". | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. U.S. President Joe Biden quickly corrected himself. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. U.S. President Joe Biden<br>2. June 16, 2021<br>3. Russian President Vladimir Putin<br>4. President Trump | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. On June 16, 2021, U.S. President Joe Biden referred to Russian President Vladimir Putin as "President Trump".<br>2. On June 16, 2021, U.S. President Joe Biden quickly corrected himself after referring to Russian President Vladimir Putin as "President Trump". | 2 |
| google/gemma-3-1b-it | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as “President Trump.”<br>2. U.S. President Joe Biden corrected himself. | 2 |
| google/gemma-3-4b-it | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. U.S. President Joe Biden quickly corrected himself after referring to Russian President Vladimir Putin as "President Trump." | 2 |
| gpt-3.5-turbo-0125 | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. U.S. President Joe Biden quickly corrected himself after referring to Russian President Vladimir Putin as "President Trump." | 2 |
| gpt-4.1-mini-2025-04-14 | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. On June 16, 2021, U.S. President Joe Biden quickly corrected himself after mistakenly referring to Russian President Vladimir Putin as "President Trump." | 2 |
| gpt-5.4-nano-2026-03-17 | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. On June 16, 2021, U.S. President Joe Biden quickly corrected himself after mistakenly referring to Russian President Vladimir Putin as "President Trump." | 2 |
| gpt-5.4-mini-2026-03-17 | 1. On June 16, 2021, U.S. President Joe Biden mistakenly referred to Russian President Vladimir Putin as "President Trump."<br>2. On June 16, 2021, U.S. President Joe Biden quickly corrected himself. | 2 |

---

## Sample ID: quantemp_241
**Original Claim**: A photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden and an ISIS flag.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photograph shows four Democratic congresswomen posing.<br>2. A photograph shows a portrait of Osama bin Laden.<br>3. A photograph shows an ISIS flag. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photograph shows four Democratic congresswomen.<br>2. The photograph shows the four Democratic congresswomen posing.<br>3. The photograph shows the four Democratic congresswomen with a portrait of Osama bin Laden.<br>4. The photograph shows the four Democratic congresswomen with an ISIS flag. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Democratic congresswomen<br>2. Osama bin Laden<br>3. ISIS | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden.<br>2. A photograph shows four Democratic congresswomen posing with an ISIS flag. | 2 |
| google/gemma-3-1b-it | 1. A photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden and an ISIS flag. | 1 |
| google/gemma-3-4b-it | 1. A photograph shows four Democratic congresswomen.<br>2. The photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden.<br>3. The photograph shows four Democratic congresswomen posing with an ISIS flag. | 3 |
| gpt-3.5-turbo-0125 | 1. The photograph shows four Democratic congresswomen.<br>2. The photograph shows the four Democratic congresswomen posing with a portrait of Osama bin Laden.<br>3. The photograph shows the four Democratic congresswomen posing with an ISIS flag. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. A photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden.<br>2. A photograph shows four Democratic congresswomen posing with an ISIS flag. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A photograph shows four Democratic congresswomen posing with a portrait of Osama bin Laden.<br>2. A photograph shows four Democratic congresswomen posing with an ISIS flag. | 2 |

---

## Sample ID: quantemp_242
**Original Claim**: The World Economic Forum “bans natural conception” because “all babies must be lab-grown by 2030.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The World Economic Forum bans natural conception.<br>2. The World Economic Forum states that all babies must be lab-grown by 2030. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The World Economic Forum bans natural conception.<br>2. All babies must be lab-grown by 2030. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The World Economic Forum bans natural conception.<br>2. All babies must be lab-grown by 2030. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The World Economic Forum has banned natural conception.<br>2. The World Economic Forum claims that all babies must be lab-grown by 2030.<br>3. The World Economic Forum has stated that babies must be lab-grown by 2030. | 3 |
| google/gemma-3-1b-it | 1. The World Economic Forum has banned natural conception.<br>2. The World Economic Forum has proposed that all babies must be lab-grown by 2030. | 2 |
| google/gemma-3-4b-it | 1. The World Economic Forum bans natural conception.<br>2. All babies must be lab-grown by 2030. | 2 |
| gpt-3.5-turbo-0125 | 1. The World Economic Forum bans natural conception.<br>2. All babies must be lab-grown by 2030 according to the World Economic Forum. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The World Economic Forum bans natural conception.<br>2. The World Economic Forum requires that all babies must be lab-grown by 2030. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The World Economic Forum “bans natural conception” because “all babies must be lab-grown by 2030.” | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The World Economic Forum “bans natural conception”.<br>2. “all babies must be lab-grown by 2030.” | 2 |

---

## Sample ID: quantemp_243
**Original Claim**: Farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The target for farm credit has been raised to a record high of 11 lakh crore rupees for the fiscal year 2018-19. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19.<br>2. The farm credit target has been raised to a record high of 11 lakh crore rupees.<br>3. The farm credit target has been raised to a record high of 11 lakh crore rupees. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Farm credit target was raised to a record high of 11 lakh crore rupees in 2018-19. | 1 |
| google/gemma-3-1b-it | 1. Farm credit target has been raised to a record high of 11 lakh crore rupees.<br>2. The farm credit target has been raised in 2018-19. | 2 |
| google/gemma-3-4b-it | 1. Farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |
| gpt-3.5-turbo-0125 | 1. The farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Farm credit target has been raised to a record high of 11 lakh crore rupees for 2018-19. | 1 |

---

## Sample ID: quantemp_244
**Original Claim**: Video shows Sen. John Kennedy presenting proof of '2020 fraud'

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Sen. John Kennedy presented proof of '2020 fraud'.<br>2. Sen. John Kennedy is a U.S. Senator.<br>3. Sen. John Kennedy is a U.S. Senator in the United States.<br>4. Sen. John Kennedy is a U.S. Senator in the United States.<br>5. Sen. John Kennedy is a U.S. Senator in the United States. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud' | 1 |
| google/gemma-3-1b-it | 1. Video shows Sen. John Kennedy presenting proof of ‘2020 fraud’. | 1 |
| google/gemma-3-4b-it | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |
| gpt-3.5-turbo-0125 | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows Sen. John Kennedy presenting proof of '2020 fraud'. | 1 |

---

## Sample ID: quantemp_245
**Original Claim**: Boris Johnson's address on 4 January was filmed before 8pm and not live as claimed, and you can tell from the time on his watch.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Boris Johnson's address on 4 January was filmed before 8pm.<br>2. Boris Johnson's address on 4 January was not live as claimed.<br>3. The time on Boris Johnson's watch indicates that his address on 4 January was filmed before 8pm. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Boris Johnson's address on 4 January was filmed before 8pm.<br>2. The address was not live as claimed.<br>3. The time on Boris Johnson's watch was not accurate. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Boris Johnson's address was filmed before 8pm on 4 January.<br>2. The time on Boris Johnson's watch was not 8pm. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Boris Johnson's address was filmed on 4 January.<br>2. The time on Boris Johnson's watch was before 8pm.<br>3. The filming of Boris Johnson's address was not live.<br>4. The filming of Boris Johnson's address was before 8pm. | 4 |
| google/gemma-3-1b-it | 1. Boris Johnson’s address on 4 January was filmed before 8pm.<br>2. The time on his watch indicates the recording occurred before 8pm. | 2 |
| google/gemma-3-4b-it | 1. Boris Johnson's address on 4 January was filmed.<br>2. The time on his watch can be seen before 8pm.<br>3. The address on 4 January was not live as claimed. | 3 |
| gpt-3.5-turbo-0125 | 1. Boris Johnson's address on 4 January was filmed before 8pm.<br>2. Boris Johnson's address on 4 January was not live as claimed.<br>3. You can tell Boris Johnson's address on 4 January was filmed before 8pm from the time on his watch. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Boris Johnson's address on 4 January was filmed before 8pm.<br>2. Boris Johnson's address on 4 January was not live as claimed.<br>3. You can tell that Boris Johnson's address on 4 January was filmed before 8pm from the time on Boris Johnson's watch. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Boris Johnson's address on 4 January was filmed before 8pm.<br>2. Boris Johnson's address on 4 January was not live as claimed.<br>3. You can tell from the time on Boris Johnson's watch. | 3 |

---

## Sample ID: quantemp_246
**Original Claim**: Is Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Automatically Counted As A COVID-19 Death?

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Is any death that occurs within 20 days of a positive COVID-19 test automatically counted as a COVID-19 death? | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Is Automatically Counted As A COVID-19 Death. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Any death that occurs within 20 days of a positive COVID-19 test is automatically counted as a COVID-19 death.<br>2. The COVID-19 test is a positive test.<br>3. A positive test indicates a death.<br>4. A death is a death.<br>5. A death is counted as a COVID-19 death. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The claim "Is Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Automatically Counted As A COVID-19 Death?" was made by the Centers for Disease Control and Prevention (CDC).<br>2. The claim "Is Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Automatically Counted As A COVID-19 Death?" was made on 2020.<br>3. The claim "Is Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Automatically Counted As A COVID-19 Death?" was made in the United States.<br>4. The claim "Is Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test Automatically Counted As A COVID-19 Death?" was made by the World Health Organization (WHO). | 4 |
| google/gemma-3-1b-it | 1. Is any death that occurs within 20 days of a positive COVID-19 test automatically counted as a COVID-19 death? | 1 |
| google/gemma-3-4b-it | 1. Any death that occurs within 20 days of a positive COVID-19 test is automatically counted as a COVID-19 death. | 1 |
| gpt-3.5-turbo-0125 | 1. Any death that occurs within 20 days of a positive COVID-19 test is automatically counted as a COVID-19 death. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Any death that occurs within 20 days of a positive COVID-19 test is automatically counted as a COVID-19 death. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Any Death That Occurs Within 20 Days Of A Positive COVID-19 Test is not automatically counted as a COVID-19 death. | 1 |

---

## Sample ID: quantemp_247
**Original Claim**: Kamala Harris jailed 1,500 Black men for possession of weed and withheld EVIDENCE on two Black men that were on death row

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld evidence on two Black men that were on death row. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld evidence on two Black men that were on death row. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. I can't fulfill this request | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris jailed 1,500 Black men.<br>3. Kamala Harris withheld EVIDENCE on two Black men that were on death row.<br>4. Kamala Harris withheld EVIDENCE on two men that were on death row. | 4 |
| google/gemma-3-1b-it | 1. Kamala Harris was jailed for arresting 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld evidence on two Black men that were on death row. | 2 |
| google/gemma-3-4b-it | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld EVIDENCE on two Black men that were on death row. | 2 |
| gpt-3.5-turbo-0125 | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld evidence on two Black men that were on death row. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld EVIDENCE on two Black men that were on death row. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld EVIDENCE on two Black men that were on death row. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Kamala Harris jailed 1,500 Black men for possession of weed.<br>2. Kamala Harris withheld EVIDENCE on two Black men that were on death row. | 2 |

---

## Sample ID: quantemp_248
**Original Claim**: Video shows a baby born with three eyes.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A baby was born with three eyes. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A video shows a baby born with three eyes. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A baby born with three eyes is a rare congenital condition.<br>2. The condition is known as trisomy 13.<br>3. Trisomy 13 is a genetic disorder.<br>4. It is a rare condition that affects the development of the fetus.<br>5. Trisomy 13 is a serious condition that can lead to severe health problems.<br>6. The condition is usually fatal in utero.<br>7. Trisomy 13 is a rare genetic disorder that affects the development of the fetus.<br>8. It is a serious condition that can lead to severe health problems.<br>9. The condition is usually fatal in utero.<br>10. Trisomy 13 is a rare genetic disorder that affects the development of the fetus. | 10 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A baby was born with three eyes.<br>2. Video shows a baby. | 2 |
| google/gemma-3-1b-it | 1. Video shows a baby born with three eyes. | 1 |
| google/gemma-3-4b-it | 1. Video shows a baby born with three eyes. | 1 |
| gpt-3.5-turbo-0125 | 1. A baby was born with three eyes in the video. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A video shows a baby born with three eyes. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows a baby born with three eyes. | 1 |

---

## Sample ID: quantemp_249
**Original Claim**: Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits and retirement income.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits and retirement income. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits and retirement income. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |
| google/gemma-3-1b-it | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>3. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits. | 3 |
| google/gemma-3-4b-it | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |
| gpt-3.5-turbo-0125 | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits and retirement income. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Nancy Pelosi advocated implementing a 100% windfall tax on stock market profits.<br>2. Nancy Pelosi advocated implementing a 100% windfall tax on retirement income. | 2 |

---

## Sample ID: quantemp_250
**Original Claim**: Says Mitt Romney raised business taxes 20 percent in Massachusetts.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Mitt Romney raised business taxes 20 percent in Massachusetts.<br>2. Romney was the Governor of Massachusetts.<br>3. Romney was elected Governor of Massachusetts in 2002.<br>4. Romney served as Governor of Massachusetts from 2002 to 2007.<br>5. Romney was elected President of the United States in 2008.<br>6. Romney served as President of the United States from 2009 to 2011.<br>7. Romney was elected President of the United States in 2012.<br>8. Romney served as President of the United States from 2013 to 2017.<br>9. Romney was elected President of the United States in 2016.<br>10. Romney served as President of the United States from 2017 to 2021.<br>11. Romney was elected President of the United States in 2020. | 11 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Mitt Romney raised business taxes by 20 percent in Massachusetts. | 1 |
| google/gemma-3-1b-it | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| google/gemma-3-4b-it | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| gpt-3.5-turbo-0125 | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Mitt Romney raised business taxes 20 percent in Massachusetts. | 1 |

---

## Sample ID: quantemp_251
**Original Claim**: $50,000. That's what every child owes today because Washington politicians have run up a huge spending tab and left our kids the bill."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. $50,000 is what every child owes today.<br>2. Washington politicians have run up a huge spending tab.<br>3. Washington politicians have left our kids the bill. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Washington politicians have run up a huge spending tab.<br>2. Our kids owe $50,000 today. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. $50,000<br>2. Every child owes $50,000<br>3. Washington politicians have run up a huge spending tab<br>4. Left our kids the bill | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The spending tab was run up by politicians in Washington.<br>2. Every child owes $50,000.<br>3. The spending tab was left by politicians in Washington for children. | 3 |
| google/gemma-3-1b-it | 1. $50,000 is the amount that every child owes today due to Washington politicians’ spending.<br>2. Washington politicians have run up a huge spending tab. | 2 |
| google/gemma-3-4b-it | 1. $50,000 is what every child owes.<br>2. Washington politicians have run up a huge spending tab.<br>3. Washington politicians have left our kids the bill. | 3 |
| gpt-3.5-turbo-0125 | 1. Every child owes $50,000 today.<br>2. Washington politicians have run up a huge spending tab.<br>3. Washington politicians have left our kids the bill. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Every child owes $50,000 today.<br>2. Washington politicians have run up a huge spending tab.<br>3. Washington politicians have left our kids the bill for the huge spending tab. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Every child owes $50,000 today.<br>2. Washington politicians have run up a huge spending tab.<br>3. Washington politicians have left our kids the bill. | 3 |

---

## Sample ID: quantemp_252
**Original Claim**: Georgia has lost more than 124,000 jobs and the unemployment rate has increased since the stimulus passed

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Georgia has lost more than 124,000 jobs since the stimulus passed.<br>2. The unemployment rate in Georgia has increased since the stimulus passed. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate in Georgia has increased since the stimulus passed. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate in Georgia has increased since the stimulus passed. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate has increased since the stimulus passed in Georgia. | 2 |
| google/gemma-3-1b-it | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate has increased since the stimulus passed. | 2 |
| google/gemma-3-4b-it | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate has increased since the stimulus passed. | 2 |
| gpt-3.5-turbo-0125 | 1. Georgia has lost more than 124,000 jobs since the stimulus passed.<br>2. The unemployment rate in Georgia has increased since the stimulus passed. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Georgia has lost more than 124,000 jobs since the stimulus passed.<br>2. The unemployment rate in Georgia has increased since the stimulus passed. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Georgia has lost more than 124,000 jobs.<br>2. The unemployment rate has increased since the stimulus passed. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Georgia has lost more than 124,000 jobs since the stimulus passed.<br>2. The unemployment rate has increased since the stimulus passed. | 2 |

---

## Sample ID: quantemp_253
**Original Claim**: unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century, not the 1 degree usually claimed

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. The claim suggests that temperatures in Australia have increased by 1 degree over the past century. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Australia<br>2. Temperatures in Australia have increased by 0.3 degrees over the past century.<br>3. Temperatures in Australia have increased by 1 degree. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. The claim that temperatures in Australia have increased by 1 degree is not supported by unadjusted data.<br>3. The claim that temperatures in Australia have increased by 1 degree over the past century is not supported by unadjusted data. | 3 |
| google/gemma-3-1b-it | 1. Unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. Temperatures in Australia have only increased by 0.3 degrees over the past century.<br>3. The temperature increase in Australia has not been the 1 degree usually claimed. | 3 |
| google/gemma-3-4b-it | 1. Unadjusted data suggests that temperatures in Australia have increased by 0.3 degrees.<br>2. The increase in temperatures in Australia occurred over the past century.<br>3. The increase in temperatures in Australia was not the 1 degree usually claimed. | 3 |
| gpt-3.5-turbo-0125 | 1. Temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. The increase in temperatures in Australia is not the 1 degree usually claimed. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Unadjusted data suggests that temperatures in Australia have increased by 0.3 degrees over the past century.<br>2. Unadjusted data suggests that temperatures in Australia have not increased by 1 degree over the past century. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. Unadjusted data suggests that temperatures in Australia have not increased by 1 degree over the past century.<br>3. The 1 degree increase is usually claimed. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. unadjusted data suggests that temperatures in Australia have only increased by 0.3 degrees over the past century.<br>2. unadjusted data suggests that temperatures in Australia have not increased by 1 degree over the past century. | 2 |

---

## Sample ID: quantemp_254
**Original Claim**: Says the Georgia Dome would need up to $350 million in work over the next five to seven years.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The Georgia Dome would need up to $350 million in work.<br>2. The Georgia Dome would need up to $350 million in work over the next five years.<br>3. The Georgia Dome would need up to $350 million in work over the next seven years. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Georgia Dome is located in Atlanta, Georgia.<br>2. The Georgia Dome would need up to $350 million in work over the next five years.<br>3. The Georgia Dome would need up to $350 million in work over the next seven years. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Georgia Dome would need up to $350 million in work over the next five years.<br>2. The Georgia Dome would need up to $350 million in work over the next seven years. | 2 |
| google/gemma-3-1b-it | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |
| google/gemma-3-4b-it | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |
| gpt-3.5-turbo-0125 | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The Georgia Dome would need up to $350 million in work over the next five to seven years. | 1 |

---

## Sample ID: quantemp_255
**Original Claim**: "The number of new businesses started per year has dropped by 100,000 during this president’s term."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term.<br>2. The president’s term is 100,000. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The term "this president" refers to Barack Obama.<br>2. The number of new businesses started per year has dropped by 100,000 during Barack Obama's term. | 2 |
| google/gemma-3-1b-it | 1. The number of new businesses started per year has dropped by 100,000.<br>2. During this president’s term, the number of new businesses started per year has dropped by 100,000. | 2 |
| google/gemma-3-4b-it | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |
| gpt-3.5-turbo-0125 | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Please provide the claim text you want broken down into atomic facts. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The number of new businesses started per year has dropped by 100,000 during this president’s term. | 1 |

---

## Sample ID: quantemp_256
**Original Claim**: 18 nations including USA and UK want PM Modi to lead a coronavirus task force

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 18 nations want PM Modi to lead a coronavirus task force.<br>2. USA wants PM Modi to lead a coronavirus task force.<br>3. UK wants PM Modi to lead a coronavirus task force. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 18 nations want PM Modi to lead a coronavirus task force.<br>2. The USA and the UK are among the 18 nations. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 18 nations including USA and UK want PM Modi to lead a coronavirus task force.<br>2. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>3. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>4. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>5. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>6. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>7. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>8. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>9. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>10. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>11. The United States and United Kingdom are among 18 nations that want PM Modi to lead a coronavirus task force.<br>12. The United States and United Kingdom are | 12 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The USA and the UK are 18 nations.<br>2. 18 nations including the USA and the UK want PM Modi to lead a coronavirus task force. | 2 |
| google/gemma-3-1b-it | 1. 18 nations including the USA and UK want PM Modi to lead a coronavirus task force. | 1 |
| google/gemma-3-4b-it | 1. 18 nations including USA and UK want PM Modi to lead a coronavirus task force. | 1 |
| gpt-3.5-turbo-0125 | 1. 18 nations want PM Modi to lead a coronavirus task force.<br>2. USA wants PM Modi to lead a coronavirus task force.<br>3. UK wants PM Modi to lead a coronavirus task force. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. 18 nations want PM Modi to lead a coronavirus task force.<br>2. The USA is one of the 18 nations that want PM Modi to lead a coronavirus task force.<br>3. The UK is one of the 18 nations that want PM Modi to lead a coronavirus task force. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. 18 nations including USA and UK want PM Modi to lead a coronavirus task force | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 18 nations including USA and UK want PM Modi to lead a coronavirus task force. | 1 |

---

## Sample ID: quantemp_257
**Original Claim**: "With three months remaining in the Fiscal Year, (the border patrol) has already encountered more illegal immigrants along the Southwest border" than in any previous fiscal year.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. With three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The border patrol has encountered more illegal immigrants along the Southwest border than in any previous fiscal year.<br>2. Three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year.<br>2. The border patrol has encountered more illegal immigrants along the Southwest border than in any previous fiscal year.<br>3. The border patrol has encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Fiscal Year had three months remaining.<br>2. (The border patrol) has already encountered more illegal immigrants along the Southwest border than in any previous Fiscal Year.<br>3. (The border patrol) has already encountered more illegal immigrants along the Southwest border than in the Fiscal Year. | 3 |
| google/gemma-3-1b-it | 1. Three months remaining in the Fiscal Year have been encountered by the border patrol more illegally immigrants than in any previous fiscal year. | 1 |
| google/gemma-3-4b-it | 1. With three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border.<br>2. The border patrol has encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 2 |
| gpt-3.5-turbo-0125 | 1. Three months remain in the Fiscal Year.<br>2. The border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. With three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. With three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. With three months remaining in the Fiscal Year, the border patrol has already encountered more illegal immigrants along the Southwest border than in any previous fiscal year. | 1 |

---

## Sample ID: quantemp_258
**Original Claim**: Says "$3 trillion in offshore money... is coming back into the economy" because of the GOP tax bills.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. "$3 trillion in offshore money" is coming back into the economy because of the GOP tax bills. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The GOP tax bills are causing offshore money to come back into the economy.<br>2. The GOP tax bills are causing $3 trillion in offshore money to come back into the economy. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The United States is a republic.<br>2. The United States is a republic.<br>3. The United States is a republic.<br>4. The United States is a republic.<br>5. The United States is a republic.<br>6. The United States is a republic.<br>7. The United States is a republic.<br>8. The United States is a republic.<br>9. The United States is a republic.<br>10. The United States is a republic.<br>11. The United States is a republic.<br>12. The United States is a republic.<br>13. The United States is a republic.<br>14. The United States is a republic.<br>15. The United States is a republic.<br>16. The United States is a republic.<br>17. The United States is a republic.<br>18. The United States is a republic.<br>19. The United States is a republic.<br>20. The United States is a republic.<br>21. The United States is a republic.<br>22. The United States is a republic.<br>23. The United States is a republic.<br>24. The United States is a republic.<br>25. The United States is a republic.<br>26. The United States is a republic.<br>27. The United States is a republic.<br>28. The United States is a republic.<br>29. The United States is a republic.<br>30. The United States is a republic.<br>31. The United States is a republic.<br>32. The United States is a republic. | 32 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The GOP passed tax bills.<br>2. $3 trillion in offshore money is coming back into the economy.<br>3. The GOP tax bills are attributed to $3 trillion in offshore money coming back into the economy. | 3 |
| google/gemma-3-1b-it | 1. $3 trillion in offshore money is coming back into the economy.<br>2. The GOP tax bills are causing the money to come back into the economy. | 2 |
| google/gemma-3-4b-it | 1. The statement "$3 trillion in offshore money" is being made.<br>2. The offshore money is being described as coming back into the economy.<br>3. The statement is being made because of the GOP tax bills. | 3 |
| gpt-3.5-turbo-0125 | 1. $3 trillion in offshore money is coming back into the economy because of the GOP tax bills. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. "$3 trillion in offshore money is coming back into the economy" because of the GOP tax bills. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. "$3 trillion in offshore money... is coming back into the economy" because of the GOP tax bills. | 1 |

---

## Sample ID: quantemp_259
**Original Claim**: “Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional. Today, there was a mass shooting in Boulder.”

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. A mass shooting occurred in Boulder. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Colorado Supreme Court declared that Boulder's AR-15 ban was unconstitutional.<br>2. Boulder's AR-15 ban was declared unconstitutional by the Colorado Supreme Court.<br>3. Boulder's AR-15 ban was declared unconstitutional by the Colorado Supreme Court last week.<br>4. Boulder's AR-15 ban was declared unconstitutional by the Colorado Supreme Court last week. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Colorado Supreme Court declared that Boulder's AR-15 ban was unconstitutional last week.<br>2. There was a mass shooting in Boulder today. | 2 |
| google/gemma-3-1b-it | 1. “Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.”<br>2. “Today, there was a mass shooting in Boulder.” | 2 |
| google/gemma-3-4b-it | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |
| gpt-3.5-turbo-0125 | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Last week, the Colorado Supreme Court declared that Boulder’s AR-15 ban was unconstitutional.<br>2. Today, there was a mass shooting in Boulder. | 2 |

---

## Sample ID: quantemp_260
**Original Claim**: Says U.S. Sen. Ron Johnson "voted to cut $700m from Medicare."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. U.S. Sen. Ron Johnson voted to cut $700 million from Medicare. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare.<br>2. Ron Johnson is a U.S. Senator.<br>3. Ron Johnson voted to cut $700m from Medicare. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| google/gemma-3-1b-it | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| google/gemma-3-4b-it | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| gpt-3.5-turbo-0125 | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. U.S. Sen. Ron Johnson voted to cut $700m from Medicare. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Says U.S. Sen. Ron Johnson "voted to cut $700m from Medicare." | 1 |
| gpt-5.4-mini-2026-03-17 | 1. U.S. Sen. Ron Johnson "voted to cut $700m from Medicare." | 1 |

---

## Sample ID: quantemp_261
**Original Claim**: A cheque of Rs 35 crore signed by Vijay Mallya before he fled to London has been deposited in BJP's fund.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A cheque of Rs 35 crore signed by Vijay Mallya before he fled to London was deposited in BJP's fund. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A cheque of Rs 35 crore was signed by Vijay Mallya.<br>2. The cheque has been deposited in BJP's fund. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The cheque of Rs 35 crore signed by Vijay Mallya before he fled to London has been deposited in BJP's fund.<br>2. Vijay Mallya signed the cheque before he fled to London.<br>3. The cheque of Rs 35 crore was signed by Vijay Mallya.<br>4. Vijay Mallya signed the cheque in London.<br>5. Vijay Mallya fled to London. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A cheque of Rs 35 crore was signed by Vijay Mallya.<br>2. The cheque of Rs 35 crore was deposited in London.<br>3. Vijay Mallya fled to London.<br>4. The cheque of Rs 35 crore was deposited in BJP's fund. | 4 |
| google/gemma-3-1b-it | 1. A cheque of Rs 35 crore was signed by Vijay Mallya.<br>2. The cheque was deposited in the BJP’s fund. | 2 |
| google/gemma-3-4b-it | 1. A cheque of Rs 35 crore was signed by Vijay Mallya.<br>2. The cheque was signed by Vijay Mallya before he fled to London.<br>3. The cheque was deposited in BJP's fund. | 3 |
| gpt-3.5-turbo-0125 | 1. A cheque of Rs 35 crore signed by Vijay Mallya before he fled to London has been deposited in BJP's fund. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A cheque of Rs 35 crore was signed by Vijay Mallya before Vijay Mallya fled to London.<br>2. The cheque of Rs 35 crore signed by Vijay Mallya before Vijay Mallya fled to London has been deposited in BJP's fund. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A cheque of Rs 35 crore was signed by Vijay Mallya before he fled to London.<br>2. The cheque of Rs 35 crore was deposited in BJP's fund. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A cheque of Rs 35 crore signed by Vijay Mallya before Vijay Mallya fled to London has been deposited in BJP's fund. | 1 |

---

## Sample ID: quantemp_262
**Original Claim**: Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Nickelodeon, the children's network, went off air.<br>2. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds.<br>3. Nickelodeon, the children's network, went off air to protest police brutality. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Nickelodeon went off air for eight minutes and 46 seconds.<br>2. Nickelodeon went off air to protest police brutality. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds.<br>2. The protest against police brutality was conducted by Nickelodeon, the children's network. | 2 |
| google/gemma-3-1b-it | 1. Nickelodeon went off air for eight minutes and 46 seconds to protest police brutality.<br>2. Nickelodeon is a children’s network.<br>3. Nickelodeon went off air for eight minutes and 46 seconds. | 3 |
| google/gemma-3-4b-it | 1. Nickelodeon, the children's network, went off air.<br>2. The going off air occurred for eight minutes and 46 seconds.<br>3. The purpose of the going off air was to protest police brutality. | 3 |
| gpt-3.5-turbo-0125 | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds.<br>2. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds.<br>2. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds.<br>2. Nickelodeon, the children's network, went off air for eight minutes and 46 seconds to protest police brutality. | 2 |

---

## Sample ID: quantemp_263
**Original Claim**: Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen. Das Sozialamt bezahle für den Besuch, habe sie behauptet. Polizisten, die dann gerufen worden seien, hätten das bestätigt.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A Ukrainian woman refused to pay a bill of 200 euros during a hairdresser visit.<br>2. The social office paid for the visit, she claimed.<br>3. Police officers who were then called confirmed that the social office paid for the visit. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An Ukrainerin has refused to pay a 200 Euro bill at a hair salon.<br>2. The Sozialamt has been paying for the salon visit.<br>3. Police have been called to confirm the claim. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen.<br>2. Das Sozialamt bezahle für den Besuch, habe sie behauptet.<br>3. Polizisten, die dann gerufen worden seien, hätten das bestätigt. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Eine Ukrainerin went to a haircut.<br>2. The Ukrainerin refused to pay the 200 Euro bill.<br>3. The Ukrainerin claimed the Social Office would pay for the visit.<br>4. Social Office paid for the visit.<br>5. Police officers were called.<br>6. Police officers confirmed the payment. | 6 |
| google/gemma-3-1b-it | 1. Eine Ukrainerin geweigert sich bei einem Friseurbesuch, die Rechnung von 200 Euro zu bezahlen.<br>2. Das Sozialamt bezahle für den Besuch.<br>3. Polizisten, die dann gerufen worden seien, hätten das bestätigt. | 3 |
| google/gemma-3-4b-it | 1. Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert.<br>2. Die Ukrainerin habe die Rechnung von 200 Euro nicht bezahlen wollen.<br>3. Das Sozialamt habe für den Besuch bezahlt.<br>4. Die Ukrainerin habe das behauptet.<br>5. Polizisten seien gerufen worden.<br>6. Die Polizisten hätten das bestätigt. | 6 |
| gpt-3.5-turbo-0125 | 1. Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen.<br>2. Das Sozialamt bezahle für den Besuch, habe die Ukrainerin behauptet.<br>3. Polizisten, die dann gerufen worden seien, hätten das bestätigt. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Eine Ukrainerin hat sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen.<br>2. Die Ukrainerin hat behauptet, das Sozialamt bezahle für den Friseurbesuch.<br>3. Polizisten, die dann gerufen worden sind, haben die Behauptung der Ukrainerin bestätigt. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen.<br>2. Die Ukrainerin habe behauptet, dass das Sozialamt für den Besuch bezahle.<br>3. Polizisten, die dann gerufen worden seien, hätten das bestätigt. | 3 |
| gpt-5.4-mini-2026-03-17 | 1. Eine Ukrainerin habe sich bei einem Friseurbesuch geweigert, die Rechnung von 200 Euro zu bezahlen.<br>2. Das Sozialamt bezahle für den Besuch, habe eine Ukrainerin behauptet.<br>3. Polizisten, die dann gerufen worden seien, hätten das bestätigt. | 3 |

---

## Sample ID: quantemp_264
**Original Claim**: "Under those eight years before (Barack)Obama came along, we didn’t have any successful radical Islamic terrorist attack in the United States" since Sept. 11, 2001.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Under the eight years before Barack Obama came along, there were no successful radical Islamic terrorist attacks in the United States since Sept. 11, 2001. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. "Under those eight years before (Barack)Obama came along, we didn’t have any successful radical Islamic terrorist attack in the United States" since Sept. 11, 2001. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Barack Obama<br>2. came along<br>3. the United States<br>4. Sept. 11, 2001 | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Barack Obama was the President of the United States from 2009 to 2017.<br>2. The year 2001 is after the presidency of George W. Bush.<br>3. There were no successful radical Islamic terrorist attacks in the United States since September 11, 2001, under the presidency of George W. Bush. | 3 |
| google/gemma-3-1b-it | 1. Under those eight years before (Barack) Obama came along, there were no successful radical Islamic terrorist attacks in the United States.<br>2. Since Sept. 11, 2001, we didn’t have any successful radical Islamic terrorist attacks in the United States. | 2 |
| google/gemma-3-4b-it | 1. Under those eight years before (Barack) Obama came along, there were no successful radical Islamic terrorist attacks in the United States.<br>2. This occurred since Sept. 11, 2001. | 2 |
| gpt-3.5-turbo-0125 | 1. Under those eight years before Barack Obama came along, there was no successful radical Islamic terrorist attack in the United States since Sept. 11, 2001. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Under the eight years before Barack Obama came along, the United States did not have any successful radical Islamic terrorist attack since Sept. 11, 2001. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Under those eight years before (Barack)Obama came along, there were no successful radical Islamic terrorist attack in the United States since Sept. 11, 2001. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Under those eight years before Barack Obama came along, we didn’t have any successful radical Islamic terrorist attack in the United States since Sept. 11, 2001. | 1 |

---

## Sample ID: quantemp_265
**Original Claim**: This photo shows vegetable shops vandalized during Indian farmers protest in December 2020.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This photo shows vegetable shops vandalized during the Indian farmers protest in December 2020. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. This photo shows a vegetable shop.<br>2. The vegetable shop was vandalized.<br>3. The vegetable shop was vandalized during the Indian farmers protest.<br>4. The vegetable shop was vandalized in December 2020. | 4 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The photo shows vegetable shops vandalized during Indian farmers protest in December 2020.<br>2. Indian farmers protest in December 2020.<br>3. Indian farmers protest.<br>4. Indian farmers. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. This photo shows vegetable shops.<br>2. The protest was by Indian farmers.<br>3. The photo was taken in December 2020.<br>4. The protest was in India. | 4 |
| google/gemma-3-1b-it | 1. This photo shows vegetable shops vandalized during Indian farmers protest in December 2020. | 1 |
| google/gemma-3-4b-it | 1. This photo shows vegetable shops.<br>2. Vegetable shops were vandalized.<br>3. The vandalism occurred during Indian farmers protest.<br>4. The Indian farmers protest occurred in December 2020. | 4 |
| gpt-3.5-turbo-0125 | 1. The photo shows vegetable shops vandalized during Indian farmers protest in December 2020. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. This photo shows vegetable shops vandalized during Indian farmers protest in December 2020. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The photo shows vegetable shops vandalized during Indian farmers protest in December 2020. | 1 |

---

## Sample ID: quantemp_266
**Original Claim**: "David Dewhurst currently owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. David Dewhurst currently owes more than $1 million to vendors.<br>2. The vendors provided services to David Dewhurst's 2012 U.S. Senate campaign. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. David Dewhurst owes more than $1 million to vendors.<br>2. David Dewhurst owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. David Dewhurst owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign.<br>2. He currently owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign.<br>3. He owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. David Dewhurst currently owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 1 |
| google/gemma-3-1b-it | 1. David Dewhurst owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 1 |
| google/gemma-3-4b-it | 1. David Dewhurst currently owes more than $1 million to vendors.<br>2. The vendors owe the services to his 2012 U.S. Senate campaign. | 2 |
| gpt-3.5-turbo-0125 | 1. David Dewhurst currently owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. David Dewhurst currently owes more than $1 million to vendors for services provided to David Dewhurst's 2012 U.S. Senate campaign. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. David Dewhurst currently owes more than $1 million to vendors for services provided to his 2012 U.S. Senate campaign. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. David Dewhurst currently owes more than $1 million to vendors for services provided to David Dewhurst's 2012 U.S. Senate campaign. | 1 |

---

## Sample ID: quantemp_267
**Original Claim**: Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Whoopi Goldberg said that military widows love their 15 minutes in the spotlight. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Whoopi Goldberg made a statement about military widows.<br>2. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |
| google/gemma-3-1b-it | 1. Whoopi Goldberg stated that “military widows love their 15 minutes in the spotlight.” | 1 |
| google/gemma-3-4b-it | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |
| gpt-3.5-turbo-0125 | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Whoopi Goldberg said that "military widows love their 15 minutes in the spotlight." | 1 |

---

## Sample ID: quantemp_268
**Original Claim**: Shows a photo of two similar Wall Street Journal newspapers with different headlines about President Donald Trump, and describes the editions as, "Same paper, same dates, different markets. What did you just learn? Feeling manipulated yet?"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photo shows two similar Wall Street Journal newspapers.<br>2. The two Wall Street Journal newspapers have different headlines.<br>3. The two Wall Street Journal newspapers are about President Donald Trump.<br>4. The two Wall Street Journal newspapers are the same paper.<br>5. The two Wall Street Journal newspapers are the same date.<br>6. The two Wall Street Journal newspapers are from different markets.<br>7. The editions are described as "Same paper, same dates, different markets."<br>8. The editions are described as "What did you just learn? Feeling manipulated yet?" | 8 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photo of two similar Wall Street Journal newspapers with different headlines about President Donald Trump is shown.<br>2. The editions are described as "Same paper, same dates, different markets. What did you just learn? Feeling manipulated yet?" | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Shows a photo of two similar Wall Street Journal newspapers with different headlines about President Donald Trump.<br>2. The two Wall Street Journal newspapers have different headlines about President Donald Trump.<br>3. The two Wall Street Journal newspapers have different editions.<br>4. The two Wall Street Journal newspapers have different dates.<br>5. The two Wall Street Journal newspapers have different markets.<br>6. The two Wall Street Journal newspapers have different headlines.<br>7. The two Wall Street Journal newspapers have different subjects.<br>8. The two Wall Street Journal newspapers have different authors.<br>9. The two Wall Street Journal newspapers have different publication dates.<br>10. The two Wall Street Journal newspapers have different editions.<br>11. The two Wall Street Journal newspapers have different content.<br>12. The two Wall Street Journal newspapers have different topics.<br>13. The two Wall Street Journal newspapers have different sources.<br>14. The two Wall Street Journal newspapers have different circulation.<br>15. The two Wall Street Journal newspapers have different readers.<br>16. The two Wall Street Journal newspapers have different readership.<br>17. The two Wall Street Journal newspapers have different readers.<br>18. The two Wall Street Journal newspapers have different circulation.<br>19. The two Wall Street Journal newspapers have different readers.<br>20. The two Wall Street Journal newspapers have different readership.<br>21. The two Wall Street Journal newspapers have different readers.<br>22. The two Wall Street Journal newspapers have different circulation | 22 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Wall Street Journal published two editions.<br>2. The Wall Street Journal published two editions with different headlines about President Donald Trump.<br>3. The Wall Street Journal published two editions with different headlines about President Donald Trump on the same dates.<br>4. The Wall Street Journal published two editions with different headlines about President Donald Trump in different markets. | 4 |
| google/gemma-3-1b-it | 1. A photo of two similar Wall Street Journal newspapers with different headlines about President Donald Trump was shown.<br>2. The editions of the newspapers were “Same paper, same dates, different markets.”<br>3. The editions were described as manipulating the user. | 3 |
| google/gemma-3-4b-it | 1. There is a photo of two similar Wall Street Journal newspapers.<br>2. The two newspapers have different headlines.<br>3. The newspapers are about President Donald Trump.<br>4. The editions are described as, "Same paper, same dates, different markets."<br>5. The description states, "What did you just learn?"<br>6. The description asks if the person feels manipulated.<br>7. The person feels manipulated. | 7 |
| gpt-3.5-turbo-0125 | 1. The editions of the Wall Street Journal newspapers are the same.<br>2. The editions of the Wall Street Journal newspapers have the same dates.<br>3. The editions of the Wall Street Journal newspapers are for different markets.<br>4. The editions of the Wall Street Journal newspapers have different headlines about President Donald Trump.<br>5. The editions of the Wall Street Journal newspapers prompt the question, "What did you just learn?"<br>6. The editions of the Wall Street Journal newspapers prompt the feeling of being manipulated. | 6 |
| gpt-4.1-mini-2025-04-14 | 1. The photo shows two similar Wall Street Journal newspapers with different headlines about President Donald Trump.<br>2. The editions are described as "Same paper, same dates, different markets."<br>3. The description asks, "What did you just learn? Feeling manipulated yet?" | 3 |
| gpt-5.4-nano-2026-03-17 | 1. A photo shows two similar Wall Street Journal newspapers with different headlines about President Donald Trump.<br>2. The editions are described as, "Same paper, same dates, different markets. What did you just learn? Feeling manipulated yet?" | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A photo shows two similar Wall Street Journal newspapers with different headlines about President Donald Trump.<br>2. The editions are described as, "Same paper, same dates, different markets. What did you just learn? Feeling manipulated yet?" | 2 |

---

## Sample ID: quantemp_269
**Original Claim**: Farmers want article 370 and 35A to be restored in Kashmir

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Farmers want article 370 to be restored in Kashmir.<br>2. Farmers want article 35A to be restored in Kashmir. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Farmers want article 370 and 35A to be restored in Kashmir. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Farmers want article 370 and 35A to be restored in Kashmir.<br>2. Article 370 was revoked in 2019.<br>3. Article 370 was revoked in 2019.<br>4. Article 370 was revoked in 2019.<br>5. Article 370 was revoked in 2019. | 5 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Article 370 was in force in Kashmir.<br>2. Article 370 was restored in Kashmir.<br>3. Article 370 was repealed in Kashmir.<br>4. Article 370 was amended in Kashmir.<br>5. Article 370 was superseded by Article 370A in Kashmir.<br>6. Article 370 was superseded by Article 35A in Kashmir. | 6 |
| google/gemma-3-1b-it | 1. Farmers want Article 370 and 35A restored in Kashmir.<br>2. Farmers want article 370 to be restored in Kashmir.<br>3. Farmers want 35A to be restored in Kashmir. | 3 |
| google/gemma-3-4b-it | 1. Farmers want article 370 to be restored in Kashmir.<br>2. Farmers want article 35A to be restored in Kashmir. | 2 |
| gpt-3.5-turbo-0125 | 1. Farmers want article 370 to be restored in Kashmir.<br>2. Farmers want article 35A to be restored in Kashmir. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Farmers want article 370 to be restored in Kashmir.<br>2. Farmers want article 35A to be restored in Kashmir. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Farmers want article 370 and 35A to be restored in Kashmir. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Farmers want article 370 to be restored in Kashmir.<br>2. Farmers want 35A to be restored in Kashmir. | 2 |

---

## Sample ID: quantemp_270
**Original Claim**: COVID-19 vaccines not linked to 8,200% increase in child deaths in past year, as claimed in online video

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. COVID-19 vaccines are not linked to an 8,200% increase in child deaths in the past year, as claimed in an online video. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The claim that COVID-19 vaccines are linked to an 8,200% increase in child deaths is false.<br>2. The online video claims that COVID-19 vaccines are linked to an 8,200% increase in child deaths is false. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. COVID-19 vaccines are not linked to an 8,200% increase in child deaths in the past year.<br>2. The claim about COVID-19 vaccines and child deaths is not linked to an 8,200% increase in child deaths.<br>3. The claim about COVID-19 vaccines and child deaths is not linked to an 8,200% increase in child deaths. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. COVID-19 vaccines were not linked to an 8,200% increase in child deaths in the past year.<br>2. The online video claiming COVID-19 vaccines were linked to an 8,200% increase in child deaths in the past year is false. | 2 |
| google/gemma-3-1b-it | 1. COVID-19 vaccines not linked to 8,200% increase in child deaths in past year.<br>2. Online video claims COVID-19 vaccines not linked to 8,200% increase in child deaths. | 2 |
| google/gemma-3-4b-it | 1. COVID-19 vaccines not linked to 8,200% increase in child deaths in past year.<br>2. This claim is as claimed in online video. | 2 |
| gpt-3.5-turbo-0125 | 1. COVID-19 vaccines are not linked to an 8,200% increase in child deaths in the past year.<br>2. The claim was made in an online video. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. COVID-19 vaccines are not linked to an 8,200% increase in child deaths in the past year.<br>2. An online video claimed that COVID-19 vaccines are linked to an 8,200% increase in child deaths in the past year. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. COVID-19 vaccines not linked to 8,200% increase in child deaths in past year.<br>2. COVID-19 vaccines not linked to 8,200% increase in child deaths in past year, as claimed in online video. | 2 |

---

## Sample ID: quantemp_271
**Original Claim**: Says British voters "under 50, especially millennials, overwhelmingly voted to stay," in the European Union. "It was older voters who voted to leave."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. British voters under 50, especially millennials, overwhelmingly voted to stay in the European Union.<br>2. It was older British voters who voted to leave the European Union. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. British voters overwhelmingly voted to stay in the European Union.<br>2. Older voters voted to leave the European Union. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. British voters under 50, especially millennials, overwhelmingly voted to stay.<br>2. It was older voters who voted to leave. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. British voters under 50, especially millennials, overwhelmingly voted to stay in the European Union.<br>2. British voters over 50 overwhelmingly voted to leave the European Union.<br>3. British voters, especially millennials, overwhelmingly voted to stay in the European Union.<br>4. British voters, especially millennials, overwhelmingly voted to leave the European Union.<br>5. British voters under 50, especially millennials, voted to stay in the European Union.<br>6. British voters over 50 voted to leave the European Union.<br>7. British voters, especially millennials, voted to stay in the European Union.<br>8. British voters, especially millennials, voted to leave the European Union. | 8 |
| google/gemma-3-1b-it | 1. British voters "under 50" voted to stay in the European Union.<br>2. British voters overwhelmingly voted to stay in the European Union.<br>3. Millennials voted to stay in the European Union.<br>4. Older voters voted to leave the European Union. | 4 |
| google/gemma-3-4b-it | 1. British voters under 50 overwhelmingly voted to stay in the European Union.<br>2. Millennials under 50 overwhelmingly voted to stay in the European Union.<br>3. Older voters voted to leave the European Union. | 3 |
| gpt-3.5-turbo-0125 | 1. British voters "under 50, especially millennials," overwhelmingly voted to stay in the European Union.<br>2. It was older voters who voted to leave the European Union. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. British voters under 50, especially millennials, overwhelmingly voted to stay in the European Union.<br>2. Older voters voted to leave the European Union. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. British voters “under 50, especially millennials, overwhelmingly voted to stay,” in the European Union.<br>2. “It was older voters who voted to leave.” | 2 |
| gpt-5.4-mini-2026-03-17 | 1. British voters under 50, especially millennials, overwhelmingly voted to stay in the European Union.<br>2. Older voters voted to leave the European Union. | 2 |

---

## Sample ID: quantemp_272
**Original Claim**: "Wisconsin lost over 600 farms last year & our farmers can't afford the #TrumpShutdown."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the #TrumpShutdown. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the #TrumpShutdown. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the TrumpShutdown. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Wisconsin lost over 600 farms last year.<br>2. The #TrumpShutdown affected Wisconsin farmers.<br>3. The #TrumpShutdown affected farmers. | 3 |
| google/gemma-3-1b-it | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can’t afford the #TrumpShutdown. | 2 |
| google/gemma-3-4b-it | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the #TrumpShutdown. | 2 |
| gpt-3.5-turbo-0125 | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the #TrumpShutdown. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Wisconsin lost over 600 farms last year.<br>2. Wisconsin farmers cannot afford the #TrumpShutdown. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Wisconsin lost over 600 farms last year.<br>2. Our farmers can't afford the #TrumpShutdown. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Wisconsin lost over 600 farms last year.<br>2. Wisconsin farmers can't afford the #TrumpShutdown. | 2 |

---

## Sample ID: quantemp_273
**Original Claim**: Maya Angelou was raped when she was a child, and after the man responsible was found dead, she refused to speak for nearly 5 years.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Maya Angelou was raped when she was a child.<br>2. After the man responsible was found dead, Maya Angelou refused to speak for nearly 5 years. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Maya Angelou was raped when she was a child.<br>2. The man responsible for the rape was found dead.<br>3. After the man responsible was found dead, Maya Angelou refused to speak for nearly 5 years. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Maya Angelou was raped when she was a child.<br>2. The man responsible for the rape was found dead.<br>3. Maya Angelou refused to speak for nearly 5 years. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Maya Angelou was a child when she was raped.<br>2. The man responsible for Maya Angelou's rape was found dead.<br>3. Maya Angelou refused to speak for nearly 5 years after the man responsible for her rape was found dead. | 3 |
| google/gemma-3-1b-it | 1. Maya Angelou was raped when she was a child.<br>2. The man responsible for Maya Angelou’s rape was found dead.<br>3. She refused to speak for nearly 5 years after the incident. | 3 |
| google/gemma-3-4b-it | 1. Maya Angelou was raped when she was a child.<br>2. The man responsible for the rape was found dead.<br>3. Maya Angelou refused to speak for nearly 5 years. | 3 |
| gpt-3.5-turbo-0125 | 1. Maya Angelou was raped when she was a child.<br>2. The man responsible for raping Maya Angelou was found dead.<br>3. Maya Angelou refused to speak for nearly 5 years after the man responsible was found dead. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Maya Angelou was raped when Maya Angelou was a child.<br>2. The man responsible for raping Maya Angelou was found dead.<br>3. After the man responsible for raping Maya Angelou was found dead, Maya Angelou refused to speak for nearly 5 years. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. Maya Angelou was raped when Maya Angelou was a child.<br>2. After the man responsible was found dead, Maya Angelou refused to speak for nearly 5 years. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Maya Angelou was raped when Maya Angelou was a child.<br>2. After the man responsible for raping Maya Angelou was found dead, Maya Angelou refused to speak for nearly 5 years. | 2 |

---

## Sample ID: quantemp_274
**Original Claim**: Says Kobe Bryant and his daughter, Gianna, were both born Aug. 23.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Kobe Bryant was born on August 23.<br>2. Gianna Bryant was born on August 23. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Kobe Bryant was born on Aug. 23.<br>2. Gianna Bryant was born on Aug. 23. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Kobe Bryant was born on Aug. 23.<br>2. Gianna Bryant was born on Aug. 23.<br>3. Kobe Bryant and Gianna Bryant were born on Aug. 23. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Kobe Bryant was born on August 23.<br>2. Gianna Bryant was born on August 23. | 2 |
| google/gemma-3-1b-it | 1. Kobe Bryant and his daughter, Gianna, were both born on August 23rd. | 1 |
| google/gemma-3-4b-it | 1. Kobe Bryant was born Aug. 23.<br>2. Gianna Bryant was born Aug. 23. | 2 |
| gpt-3.5-turbo-0125 | 1. Kobe Bryant was born on August 23.<br>2. Gianna Bryant was born on August 23. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Kobe Bryant was born on Aug. 23.<br>2. Kobe Bryant's daughter, Gianna, was born on Aug. 23. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Says Kobe Bryant and his daughter, Gianna, were both born Aug. 23. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Kobe Bryant was born Aug. 23.<br>2. Gianna was born Aug. 23. | 2 |

---

## Sample ID: quantemp_275
**Original Claim**: Says Jon Corzine "gave away 14 percent raises over 4 years and he stood on the front steps of the Capitol at a public-sector union rally and said, 'I will fight to get you a great contract.’"

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, "I will fight to get you a great contract" at a public-sector union rally. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, 'I will fight to get you a great contract.’ | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. He stood on the front steps of the Capitol at a public-sector union rally.<br>3. He said, 'I will fight to get you a great contract.' | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, 'I will fight to get you a great contract.' | 3 |
| google/gemma-3-1b-it | 1. Jon Corzine stated that he gave away 14% raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, “I will fight to get you a great contract.” | 3 |
| google/gemma-3-4b-it | 1. Jon Corzine said “gave away 14 percent raises over 4 years.”<br>2. Jon Corzine stood on the front steps of the Capitol.<br>3. Jon Corzine said, “I will fight to get you a great contract.”<br>4. The statement was made at a public-sector union rally.<br>5. The time period over which the raises were given was 4 years. | 5 |
| gpt-3.5-turbo-0125 | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, 'I will fight to get you a great contract.' | 3 |
| gpt-4.1-mini-2025-04-14 | 1. Jon Corzine gave away 14 percent raises over 4 years.<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, "I will fight to get you a great contract" at the public-sector union rally on the front steps of the Capitol. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Jon Corzine "gave away 14 percent raises over 4 years."<br>2. Jon Corzine stood on the front steps of the Capitol at a public-sector union rally.<br>3. Jon Corzine said, "I will fight to get you a great contract." | 3 |

---

## Sample ID: quantemp_276
**Original Claim**: An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. An email message accurately says that Target is giving a brand new PlayStation 5 gaming console to a recipient in exchange for answering survey questions. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. An email message says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Target is a retail company.<br>2. Target is giving away a brand new PlayStation 5 gaming console.<br>3. Target is giving away a brand new PlayStation 5 gaming console in exchange for survey questions. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console.<br>2. An email message accurately says that you are being given a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 2 |
| google/gemma-3-1b-it | 1. An email message accurately states that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |
| google/gemma-3-4b-it | 1. An email message says that Target is giving someone a brand new PlayStation 5 gaming console.<br>2. The email message says that someone is receiving a brand new PlayStation 5 gaming console.<br>3. Target is giving someone a brand new PlayStation 5 gaming console.<br>4. Target is giving someone a PlayStation 5 gaming console.<br>5. Someone is receiving a brand new PlayStation 5 gaming console.<br>6. Someone is answering survey questions. | 6 |
| gpt-3.5-turbo-0125 | 1. An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. An email message accurately says that Target is giving you a brand new PlayStation 5 gaming console in exchange for answering survey questions. | 1 |

---

## Sample ID: quantemp_277
**Original Claim**: The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule "is lower than the prescribed tax rate for millionaires already -- not just for millionaires, for people making over $200,000."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>2. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is not just for millionaires.<br>3. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is for people making over $200,000. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. President Barack Obama's proposed Buffett Rule calls for a 30 percent tax rate.<br>2. The 30 percent tax rate called for under President Barack Obama's proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>3. The 30 percent tax rate called for under President Barack Obama's proposed Buffett Rule is not just for millionaires, but for people making over $200,000. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The proposed Buffett Rule was called for under President Barack Obama’s proposed tax reform.<br>2. The proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>3. The proposed Buffett Rule is lower than the prescribed tax rate for millionaires already for people making over $200,000. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The 30 percent tax rate called for under President Barack Obama's proposed Buffett Rule is lower than the prescribed tax rate for millionaires.<br>2. The 30 percent tax rate called for under President Barack Obama's proposed Buffett Rule is lower than the prescribed tax rate for people making over $200,000. | 2 |
| google/gemma-3-1b-it | 1. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>2. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already. | 2 |
| google/gemma-3-4b-it | 1. The 30 percent tax rate is called for under President Barack Obama’s proposed Buffett Rule.<br>2. The Buffett Rule is a proposed rule.<br>3. President Barack Obama proposed the Buffett Rule.<br>4. The tax rate is lower than the prescribed tax rate.<br>5. The prescribed tax rate is for millionaires.<br>6. The prescribed tax rate is for people making over $200,000. | 6 |
| gpt-3.5-turbo-0125 | 1. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>2. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for people making over $200,000. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>2. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for people making over $200,000. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for millionaires already.<br>2. The 30 percent tax rate called for under President Barack Obama’s proposed Buffett Rule is lower than the prescribed tax rate for people making over $200,000. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The 30 percent tax rate was called for under President Barack Obama’s proposed Buffett Rule.<br>2. The 30 percent tax rate is lower than the prescribed tax rate for millionaires already.<br>3. The 30 percent tax rate is lower than the prescribed tax rate for people making over $200,000. | 3 |

---

## Sample ID: quantemp_278
**Original Claim**: This video shows protesting Indian farmers defacing a Hindi sign in January 2021

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. This video shows protesting Indian farmers defacing a Hindi sign in January 2021. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. This video shows protesting Indian farmers.<br>2. The protesting Indian farmers defacing a Hindi sign.<br>3. The defacing of the Hindi sign occurred in January 2021. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. This video shows protesting Indian farmers defacing a Hindi sign in January 2021.<br>2. The video shows Indian farmers defacing a Hindi sign in January 2021.<br>3. The video shows Indian farmers defacing a Hindi sign in January 2021.<br>4. The video shows Indian farmers defacing a Hindi sign in January 2021. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The video is about protesting Indian farmers.<br>2. The video is about defacing a Hindi sign.<br>3. The video is set in January 2021.<br>4. The video is about protesting Indian farmers defacing a Hindi sign in January 2021. | 4 |
| google/gemma-3-1b-it | 1. This video shows protesting Indian farmers defacing a Hindi sign.<br>2. This video took place in January 2021.<br>3. Protesting Indian farmers defacing a Hindi sign occurred in January 2021. | 3 |
| google/gemma-3-4b-it | 1. This video shows protesting Indian farmers defacing a Hindi sign.<br>2. The protesting Indian farmers defaced a Hindi sign in January 2021. | 2 |
| gpt-3.5-turbo-0125 | 1. The video shows protesting Indian farmers.<br>2. The video shows protesting Indian farmers defacing a Hindi sign.<br>3. The video shows protesting Indian farmers defacing a Hindi sign in January 2021. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. This video shows protesting Indian farmers defacing a Hindi sign in January 2021. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. This video shows protesting Indian farmers defacing a Hindi sign in January 2021. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. The video shows protesting Indian farmers defacing a Hindi sign in January 2021. | 1 |

---

## Sample ID: quantemp_279
**Original Claim**: CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The U.S. delegation on CBN denied visas to India predates 2023 Manipur violence.<br>2. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence.<br>3. The U.S. delegation on CBN denied visas to India predates 2023 Manipur violence. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A CBN interview was conducted on the U.S. delegation.<br>2. The U.S. delegation was denied visas to India.<br>3. The denial of visas to India by the U.S. delegation predates the 2023 Manipur violence. | 3 |
| google/gemma-3-1b-it | 1. CBN interview on U.S. delegation was denied visas to India predating 2023 Manipur violence.<br>2. U.S. delegation denied visas to India.<br>3. The interview took place predating 2023 Manipur violence. | 3 |
| google/gemma-3-4b-it | 1. A CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| gpt-3.5-turbo-0125 | 1. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. CBN interview on U.S. delegation denied visas to India predates 2023 Manipur violence. | 1 |

---

## Sample ID: quantemp_280
**Original Claim**: Says pension contributions under Gov. Chris Christie would represent "75 percent of the total contribution made between the years 1995 and 2010. That's right, in 15 years, total state contribution was only $2.1 billion."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Pension contributions under Gov. Chris Christie represent 75 percent of the total contribution made between the years 1995 and 2010.<br>2. The total state contribution between the years 1995 and 2010 was $2.1 billion.<br>3. The period of time for the total state contribution is 15 years. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Gov. Chris Christie's pension contributions represent 75 percent of the total contribution made between the years 1995 and 2010.<br>2. The total state contribution over 15 years was only $2.1 billion. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The total contribution made between 1995 and 2010 was $2.1 billion.<br>2. Pension contributions under Gov. Chris Christie would represent 75 percent of the total contribution made between 1995 and 2010.<br>3. That's right, in 15 years, total state contribution was only $2.1 billion. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Gov. Chris Christie made pension contributions that represented 75 percent of the total contribution made between 1995 and 2010.<br>2. The total contribution made between 1995 and 2010 was $2.1 billion.<br>3. The years 1995 and 2010 represent the time period during which the total contribution was made. | 3 |
| google/gemma-3-1b-it | 1. Pension contributions under Gov. Chris Christie would represent “75 percent” of the total contribution made between the years 1995 and 2010.<br>2. The total state contribution was $2.1 billion between the years 1995 and 2010.<br>3. That’s right, in 15 years, total state contribution was only $2.1 billion. | 3 |
| google/gemma-3-4b-it | 1. Gov. Chris Christie’s pension contributions would represent 75 percent of the total contribution made between the years 1995 and 2010.<br>2. That’s right.<br>3. In 15 years, total state contribution was only $2.1 billion. | 3 |
| gpt-3.5-turbo-0125 | 1. Pension contributions under Gov. Chris Christie would represent "75 percent of the total contribution made between the years 1995 and 2010."<br>2. In 15 years, total state contribution was only $2.1 billion. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Pension contributions under Gov. Chris Christie would represent 75 percent of the total contribution made between the years 1995 and 2010.<br>2. The total state contribution between the years 1995 and 2010 was only $2.1 billion. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Pension contributions under Gov. Chris Christie would represent 75 percent of the total contribution made between the years 1995 and 2010.<br>2. In 15 years, total state contribution was only $2.1 billion. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Pension contributions under Gov. Chris Christie would represent "75 percent of the total contribution made between the years 1995 and 2010."<br>2. In 15 years, total state contribution was only $2.1 billion. | 2 |

---

## Sample ID: quantemp_281
**Original Claim**: Photo shows Russian jet flying under a bridge in 1965

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photo shows a Russian jet flying under a bridge in 1965. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photo shows a Russian jet flying under a bridge in 1965. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The photo shows a Russian jet flying under a bridge in 1965.<br>2. The photo shows a jet flying under a bridge in 1965.<br>3. The photo shows a jet flying under a bridge in 1965. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The photo was taken in 1965.<br>2. A Russian jet was flying under a bridge in 1965.<br>3. The subject of the photo was flying under a bridge in 1965. | 3 |
| google/gemma-3-1b-it | 1. Photo depicts a Russian jet flying under a bridge.<br>2. Photo shows Russian jet flying under a bridge in 1965. | 2 |
| google/gemma-3-4b-it | 1. A photo shows a Russian jet flying under a bridge.<br>2. The photo was taken in 1965. | 2 |
| gpt-3.5-turbo-0125 | 1. The photo shows a Russian jet flying under a bridge in 1965. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The photo shows a Russian jet flying under a bridge in 1965. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Photo shows Russian jet flying under a bridge in 1965. | 1 |

---

## Sample ID: quantemp_282
**Original Claim**: The 2011 Rebuild America Jobs Act "would have cost the average American family $1,000 a year while making no significant impact to fix our infrastructure and roads."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The 2011 Rebuild America Jobs Act was proposed.<br>2. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>3. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The 2011 Rebuild America Jobs Act was passed.<br>2. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>3. The 2011 Rebuild America Jobs Act would have made no significant impact on fixing America's infrastructure and roads. | 3 |
| google/gemma-3-1b-it | 1. The 2011 Rebuild America Jobs Act “would have cost the average American family $1,000 a year.”<br>2. The average American family would have paid $1,000 a year.<br>3. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>4. Making no significant impact to fix our infrastructure and roads. | 4 |
| google/gemma-3-4b-it | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |
| gpt-3.5-turbo-0125 | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix infrastructure and roads. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The 2011 Rebuild America Jobs Act would have cost the average American family $1,000 a year.<br>2. The 2011 Rebuild America Jobs Act would have made no significant impact to fix our infrastructure and roads. | 2 |

---

## Sample ID: quantemp_283
**Original Claim**: Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die or suffer serious adverse events

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die.<br>2. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will suffer serious adverse events. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die or suffer serious adverse events. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Government figures show that 1 in 35 who get the COVID-19 vaccine will die or suffer serious adverse events. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The COVID-19 vaccine was administered to 1 in 35 people.<br>2. Government figures show that 1 in 35 people who get the COVID-19 vaccine will die.<br>3. Government figures show that 1 in 35 people who get the COVID-19 vaccine will suffer serious adverse events. | 3 |
| google/gemma-3-1b-it | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die or suffer serious adverse events. | 1 |
| google/gemma-3-4b-it | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die.<br>2. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will suffer serious adverse events. | 2 |
| gpt-3.5-turbo-0125 | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die or suffer serious adverse events. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die.<br>2. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will suffer serious adverse events. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die.<br>2. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will suffer serious adverse events. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will die.<br>2. Government figures do not show that 1 in 35 who get the COVID-19 vaccine will suffer serious adverse events. | 2 |

---

## Sample ID: quantemp_284
**Original Claim**: Glen Eagles hospital issued an urgent warning because seven women have died after sniffing perfume samples received in the mail.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail.<br>3. Glen Eagles hospital issued an urgent warning because seven women have died after sniffing perfume samples received in the mail. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Glen Eagles issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail.<br>3. The women who died were at Glen Eagles. | 3 |
| google/gemma-3-1b-it | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| google/gemma-3-4b-it | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| gpt-3.5-turbo-0125 | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Glen Eagles hospital issued an urgent warning.<br>2. Seven women have died after sniffing perfume samples received in the mail. | 2 |

---

## Sample ID: quantemp_285
**Original Claim**: "Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by" weapons that were part of a federal arms trafficking operation.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons.<br>2. The weapons that caused the death of at least one U.S. Border Patrol agent were part of a federal arms trafficking operation. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons.<br>2. The weapons were part of a federal arms trafficking operation. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation.<br>2. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation.<br>3. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation. | 1 |
| google/gemma-3-1b-it | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons.<br>2. Weapons that were part of a federal arms trafficking operation caused the death of at least one U.S. Border Patrol agent. | 2 |
| google/gemma-3-4b-it | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons.<br>2. The weapons were part of a federal arms trafficking operation. | 2 |
| gpt-3.5-turbo-0125 | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Ballistic tests have confirmed that the death of at least one U.S. Border Patrol agent was caused by weapons that were part of a federal arms trafficking operation. | 1 |

---

## Sample ID: quantemp_286
**Original Claim**: The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.Cholera killed 938 people in 22 states in Nigeria.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| google/gemma-3-1b-it | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. The number of people killed by cholera in Nigeria as of August 10 was 938.<br>3. The number of states in Nigeria where cholera killed 938 people as of August 10 was 22. | 3 |
| google/gemma-3-4b-it | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in Nigeria.<br>3. Cholera killed 938 people in 22 states in Nigeria. | 3 |
| gpt-3.5-turbo-0125 | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. The total number of suspected cases of cholera in Nigeria as of August 10 was 33,661.<br>2. Cholera killed 938 people in 22 states in Nigeria. | 2 |

---

## Sample ID: quantemp_287
**Original Claim**: There is "a situation in this country where you're nearing 50 percent of people who don't even pay income taxes."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. There is a situation in this country where nearing 50 percent of people do not pay income taxes. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. There is a situation in this country where 50 percent of people do not pay income taxes. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. There is a situation in this country where you're nearing 50 percent of people who don't even pay income taxes. | 1 |
| meta-llama/Llama-3.2-3B-Instruct | 1. There is a situation in this country where nearly 50 percent of people do not pay income taxes. | 1 |
| google/gemma-3-1b-it | 1. There is a situation in this country where you’re nearing 50 percent of people who don’t even pay income taxes. | 1 |
| google/gemma-3-4b-it | 1. There is a situation in this country where you're nearing 50 percent of people who don't even pay income taxes. | 1 |
| gpt-3.5-turbo-0125 | 1. The country is experiencing a situation where nearly 50 percent of people don't even pay income taxes. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. There is a situation in this country where nearly 50 percent of people do not pay income taxes. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. There is a situation in this country where you're nearing 50 percent of people who don't even pay income taxes. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. There is "a situation in this country where you're nearing 50 percent of people who don't even pay income taxes." | 1 |

---

## Sample ID: quantemp_288
**Original Claim**: "It’s estimated that in 2018 alone, dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions."

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. It is estimated that in 2018 alone, dead people received $1 billion in benefits from Medicare.<br>2. It is estimated that in 2018 alone, dead people received $1 billion in benefits from Medicaid.<br>3. It is estimated that in 2018 alone, dead people received $1 billion in benefits from social security payments.<br>4. It is estimated that in 2018 alone, dead people received $1 billion in benefits from federal pensions. | 4 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. It is estimated that in 2018 alone, dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. It's estimated that in 2018 alone, dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions.<br>2. Dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions in 2018 alone. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Dead people received $1 billion in benefits from Medicare in 2018.<br>2. Dead people received $1 billion in benefits from Medicaid in 2018.<br>3. Dead people received $1 billion in benefits from social security payments in 2018.<br>4. Dead people received $1 billion in benefits from federal pensions in 2018. | 4 |
| google/gemma-3-1b-it | 1. It is estimated that in 2018 alone, dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions. | 1 |
| google/gemma-3-4b-it | 1. It’s estimated that in 2018 alone, dead people received $1 billion in benefits.<br>2. It’s estimated that in 2018 alone, dead people received benefits from Medicare.<br>3. It’s estimated that in 2018 alone, dead people received benefits from Medicaid.<br>4. It’s estimated that in 2018 alone, dead people received benefits from social security payments.<br>5. It’s estimated that in 2018 alone, dead people received benefits from federal pensions. | 5 |
| gpt-3.5-turbo-0125 | 1. Dead people received $1 billion in benefits from Medicare in 2018.<br>2. Dead people received $1 billion in benefits from Medicaid in 2018.<br>3. Dead people received $1 billion in benefits from social security payments in 2018.<br>4. Dead people received $1 billion in benefits from federal pensions in 2018. | 4 |
| gpt-4.1-mini-2025-04-14 | 1. Dead people received $1 billion in benefits from Medicare in 2018.<br>2. Dead people received $1 billion in benefits from Medicaid in 2018.<br>3. Dead people received $1 billion in benefits from social security payments in 2018.<br>4. Dead people received $1 billion in benefits from federal pensions in 2018. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In 2018 alone, dead people received $1 billion in benefits from Medicare, Medicaid, social security payments, and federal pensions. | 1 |

---

## Sample ID: quantemp_289
**Original Claim**: New Zealand border workers could be fined $4000 or imprisoned if they are not vaccinated

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. New Zealand border workers could be fined $4000 if they are not vaccinated.<br>2. New Zealand border workers could be imprisoned if they are not vaccinated. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. New Zealand border workers could be fined $4000.<br>2. New Zealand border workers could be imprisoned.<br>3. New Zealand border workers could be fined $4000 or imprisoned. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. New Zealand border workers could be fined $4000 or imprisoned if they are not vaccinated.<br>2. New Zealand is a country.<br>3. New Zealand has a border.<br>4. New Zealand has a border with workers.<br>5. New Zealand has a border with workers.<br>6. New Zealand has a border with workers.<br>7. New Zealand has a border with workers.<br>8. New Zealand has a border with workers.<br>9. New Zealand has a border with workers.<br>10. New Zealand has a border with workers.<br>11. New Zealand has a border with workers.<br>12. New Zealand has a border with workers.<br>13. New Zealand has a border with workers.<br>14. New Zealand has a border with workers.<br>15. New Zealand has a border with workers.<br>16. New Zealand has a border with workers.<br>17. New Zealand has a border with workers.<br>18. New Zealand has a border with workers.<br>19. New Zealand has a border with workers.<br>20. New Zealand has a border with workers.<br>21. New Zealand has a border with workers.<br>22. New Zealand has a border with workers.<br>23. New Zealand has a border with workers.<br>24. New Zealand has a border with workers.<br>25. New Zealand has a border with workers.<br>26. New Zealand has a border with workers.<br>27. New Zealand has a border with workers.<br>28. New Zealand has a border with | 28 |
| meta-llama/Llama-3.2-3B-Instruct | 1. New Zealand border workers could be fined $4000.<br>2. New Zealand border workers could be imprisoned.<br>3. New Zealand border workers could be vaccinated. | 3 |
| google/gemma-3-1b-it | 1. New Zealand border workers could be fined $4000.<br>2. New Zealand border workers could be imprisoned if they are not vaccinated. | 2 |
| google/gemma-3-4b-it | 1. New Zealand border workers could be fined $4000.<br>2. New Zealand border workers could be imprisoned.<br>3. The fines are for border workers who are not vaccinated. | 3 |
| gpt-3.5-turbo-0125 | 1. New Zealand border workers could be fined $4000 if they are not vaccinated.<br>2. New Zealand border workers could be imprisoned if they are not vaccinated. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. New Zealand border workers could be fined $4000 if New Zealand border workers are not vaccinated.<br>2. New Zealand border workers could be imprisoned if New Zealand border workers are not vaccinated. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. New Zealand border workers could be fined $4000 if they are not vaccinated.<br>2. New Zealand border workers could be imprisoned if they are not vaccinated. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. New Zealand border workers could be fined $4000 if they are not vaccinated.<br>2. New Zealand border workers could be imprisoned if they are not vaccinated. | 2 |

---

## Sample ID: quantemp_290
**Original Claim**: Hulu cancelled plans to stream comedian Michelle Wolf’s standup special after her appearance at the 2018 White House Correspondents Dinner.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special.<br>2. Comedian Michelle Wolf appeared at the 2018 White House Correspondents Dinner. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Hulu cancelled plans to stream Michelle Wolf's standup special.<br>2. Michelle Wolf's standup special was not included in Hulu's plans to stream. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Hulu cancelled plans to stream Michelle Wolf's standup special after her appearance at the 2018 White House Correspondents Dinner.<br>2. Michelle Wolf appeared at the 2018 White House Correspondents Dinner.<br>3. The 2018 White House Correspondents Dinner.<br>4. The White House Correspondents Dinner. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Hulu cancelled plans to stream Michelle Wolf's standup special after her appearance at the 2018 White House Correspondents Dinner. | 1 |
| google/gemma-3-1b-it | 1. Hulu cancelled plans to stream Michelle Wolf’s standup special.<br>2. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special. | 2 |
| google/gemma-3-4b-it | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special.<br>2. The cancellation occurred after her appearance at the 2018 White House Correspondents Dinner. | 2 |
| gpt-3.5-turbo-0125 | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special.<br>2. Michelle Wolf appeared at the 2018 White House Correspondents Dinner. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special.<br>2. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special after Michelle Wolf’s appearance at the 2018 White House Correspondents Dinner. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Hulu cancelled plans to stream comedian Michelle Wolf’s standup special after Michelle Wolf’s appearance at the 2018 White House Correspondents Dinner. | 1 |

---

## Sample ID: quantemp_291
**Original Claim**: Pelosi fined $40,000 for tearing up Trump's speech

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Pelosi was fined $40,000 for tearing up Trump's speech. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Pelosi was fined $40,000.<br>2. Pelosi was fined for tearing up Trump's speech. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Pelosi fined $40,000 for tearing up Trump's speech.<br>2. The fine was for violating the Espionage Act of 1917.<br>3. The fine was for violating the Espionage Act of 1917.<br>4. The fine was for violating the Espionage Act of 1917. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Nancy Pelosi fined $40,000 for tearing up Donald Trump's speech. | 1 |
| google/gemma-3-1b-it | 1. Pelosi was fined $40,000 for tearing up Trump’s speech.<br>2. Pelosi received a fine of $40,000 for tearing up Trump’s speech. | 2 |
| google/gemma-3-4b-it | 1. Pelosi was fined $40,000.<br>2. The fine was for tearing up Trump's speech. | 2 |
| gpt-3.5-turbo-0125 | 1. Pelosi was fined $40,000 for tearing up Trump's speech. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. Pelosi was fined $40,000 for tearing up Trump's speech. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. Pelosi fined $40,000 for tearing up Trump's speech. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Pelosi fined $40,000 for tearing up Trump's speech. | 1 |

---

## Sample ID: quantemp_292
**Original Claim**: 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it.<br>2. 20 percent of women who had restraining orders were killed in Intimate Partner Homicides (IPH) within two days of obtaining it.<br>3. 20 percent of women who had restraining orders were killed in Intimate Partner Homicides (IPH) within two days of obtaining restraining orders. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Women who had restraining orders were killed in Intimate Partner Homicides (IPH) 20 percent of the time within two days of obtaining it. | 1 |
| google/gemma-3-1b-it | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it. | 1 |
| google/gemma-3-4b-it | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) existed who had restraining orders.<br>2. Those women were killed within two days of obtaining restraining orders. | 2 |
| gpt-3.5-turbo-0125 | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining the restraining order. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining the restraining orders. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining it. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. 20 percent of women killed in Intimate Partner Homicides (IPH) who had restraining orders were killed within two days of obtaining restraining orders. | 1 |

---

## Sample ID: quantemp_293
**Original Claim**: A photo caption says vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A photo caption says vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A photo caption says vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise.<br>2. The vendors sold Trump-themed merchandise to “stupid” people.<br>3. The vendors sold Trump-themed merchandise outside the U.S. Capitol on Jan. 6. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.<br>2. The vendors sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.<br>3. Trump-themed merchandise was sold to “stupid” people outside the U.S. Capitol on Jan. 6.<br>4. The vendors sold merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Vendors named "Nah" and "Stop asking me questions before you get your a-- kicked" sold Trump-themed merchandise outside the U.S. Capitol on Jan. 6.<br>2. The vendors sold Trump-themed merchandise to people outside the U.S. Capitol on Jan. 6. | 2 |
| google/gemma-3-1b-it | 1. A photo caption states that vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 1 |
| google/gemma-3-4b-it | 1. A photo caption says vendors named “Nah” sold Trump-themed merchandise.<br>2. A photo caption says vendors named “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise.<br>3. The vendors sold Trump-themed merchandise to people.<br>4. The people were outside the U.S. Capitol.<br>5. The people were described as “stupid”.<br>6. The event occurred on Jan. 6.<br>7. The people were not located inside the U.S. Capitol. | 7 |
| gpt-3.5-turbo-0125 | 1. The photo caption says vendors named “Nah” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.<br>2. The photo caption says vendors named “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A photo caption says vendors named “Nah” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.<br>2. A photo caption says vendors named “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. A photo caption says vendors named “Nah” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6.<br>2. A photo caption says vendors named “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. A photo caption says vendors named “Nah” and “Stop asking me questions before you get your a-- kicked” sold Trump-themed merchandise to “stupid” people outside the U.S. Capitol on Jan. 6. | 1 |

---

## Sample ID: quantemp_294
**Original Claim**: Bill Maher and Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Bill Maher and Megyn Kelly argued that 8-year-olds shouldn't be burdened with race issues.<br>2. Bill Maher and Megyn Kelly argued that 9-year-olds shouldn't be burdened with race issues. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. Bill Maher and Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Bill Maher and Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues.<br>2. Bill Maher is a comedian.<br>3. Megyn Kelly is a comedian.<br>4. Bill Maher and Megyn Kelly are both American television personalities. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Bill Maher and Megyn Kelly argued.<br>2. 8-year-olds and 9-year-olds should not be burdened with race issues. | 2 |
| google/gemma-3-1b-it | 1. Bill Maher and Megyn Kelly argued that 8- and 9-year-olds shouldn’t be burdened with race issues. | 1 |
| google/gemma-3-4b-it | 1. Bill Maher and Megyn Kelly argued that 8-year-olds shouldn't be burdened with race issues.<br>2. 8-year-olds shouldn't be burdened with race issues.<br>3. Megyn Kelly is a person.<br>4. Bill Maher is a person. | 4 |
| gpt-3.5-turbo-0125 | 1. Bill Maher argued that 8- and 9-year-olds shouldn't be burdened with race issues.<br>2. Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. Bill Maher argued that 8-year-olds shouldn't be burdened with race issues.<br>2. Bill Maher argued that 9-year-olds shouldn't be burdened with race issues.<br>3. Megyn Kelly argued that 8-year-olds shouldn't be burdened with race issues.<br>4. Megyn Kelly argued that 9-year-olds shouldn't be burdened with race issues. | 4 |
| gpt-5.4-nano-2026-03-17 | 1. Bill Maher argued that 8- and 9-year-olds shouldn't be burdened with race issues.<br>2. Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. Bill Maher argued that 8- and 9-year-olds shouldn't be burdened with race issues.<br>2. Megyn Kelly argued that 8- and 9-year-olds shouldn't be burdened with race issues. | 2 |

---

## Sample ID: quantemp_295
**Original Claim**: Image shows the Coronavirus magnified 2, 600 times.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Image shows the Coronavirus magnified 2,600 times. | 1 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. The image shows the Coronavirus.<br>2. The image magnifies the Coronavirus 2, 600 times. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. The Coronavirus is a type of virus.<br>2. The Coronavirus is a type of virus.<br>3. The Coronavirus is a type of virus.<br>4. The Coronavirus is a type of virus.<br>5. The Coronavirus is a type of virus.<br>6. The Coronavirus is a type of virus.<br>7. The Coronavirus is a type of virus.<br>8. The Coronavirus is a type of virus.<br>9. The Coronavirus is a type of virus.<br>10. The Coronavirus is a type of virus.<br>11. The Coronavirus is a type of virus.<br>12. The Coronavirus is a type of virus.<br>13. The Coronavirus is a type of virus.<br>14. The Coronavirus is a type of virus.<br>15. The Coronavirus is a type of virus.<br>16. The Coronavirus is a type of virus.<br>17. The Coronavirus is a type of virus.<br>18. The Coronavirus is a type of virus.<br>19. The Coronavirus is a type of virus.<br>20. The Coronavirus is a type of virus.<br>21. The Coronavirus is a type of virus.<br>22. The Coronavirus is a type of virus.<br>23. The Coronavirus is a type of virus.<br>24. The Coronavirus is a type of virus.<br>25. The Coronavirus is a type of virus.<br>26. The Coronavirus is a type of virus.<br>27. The Coronavirus is a type of virus.<br>28. The Coronavirus is a type of virus.<br>29. The Coronavirus is | 29 |
| meta-llama/Llama-3.2-3B-Instruct | 1. The Coronavirus was magnified 2,600 times in an image. | 1 |
| google/gemma-3-1b-it | 1. Image shows the Coronavirus magnified 2,600 times. | 1 |
| google/gemma-3-4b-it | 1. The image shows the Coronavirus magnified 2,600 times. | 1 |
| gpt-3.5-turbo-0125 | 1. The image shows the Coronavirus magnified 2,600 times. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. The image shows the Coronavirus magnified 2,600 times. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Image shows the Coronavirus magnified 2, 600 times. | 1 |

---

## Sample ID: quantemp_296
**Original Claim**: A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. A judge told an atheist plaintiff.<br>2. The atheist plaintiff challenged religious holidays.<br>3. The atheist plaintiff is an atheist.<br>4. The judge told the atheist plaintiff that atheists already have their own holiday.<br>5. The holiday that atheists already have is April 1. | 5 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1. | 1 |
| meta-llama/Llama-3.2-1B-Instruct | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1.<br>2. The plaintiff challenged religious holidays.<br>3. The plaintiff is an atheist.<br>4. The plaintiff is a plaintiff.<br>5. The plaintiff is challenging religious holidays.<br>6. The plaintiff is challenging religious holidays.<br>7. The plaintiff is challenging religious holidays.<br>8. The plaintiff is challenging religious holidays. | 8 |
| meta-llama/Llama-3.2-3B-Instruct | 1. A judge told an atheist plaintiff who challenged religious holidays that April 1 is an atheist holiday.<br>2. An atheist plaintiff who challenged religious holidays was told by a judge that April 1 is an atheist holiday. | 2 |
| google/gemma-3-1b-it | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday.<br>2. April 1 was told by a judge to an atheist plaintiff. | 2 |
| google/gemma-3-4b-it | 1. A judge told an atheist plaintiff.<br>2. The atheist plaintiff challenged religious holidays.<br>3. The judge told the atheist plaintiff that atheists already have their own holiday.<br>4. April 1 is the holiday the judge referenced. | 4 |
| gpt-3.5-turbo-0125 | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1. | 1 |
| gpt-4.1-mini-2025-04-14 | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. A judge told an atheist plaintiff who challenged religious holidays that atheists already have their own holiday: April 1. | 1 |

---

## Sample ID: quantemp_297
**Original Claim**: Video shows rescue workers on the scene after a military plane crash that killed 12 people in Myanmar on June 10, 2021.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. Video shows rescue workers on the scene.<br>2. A military plane crash killed 12 people in Myanmar.<br>3. The military plane crash occurred in Myanmar on June 10, 2021. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. A military plane crash occurred in Myanmar on June 10, 2021.<br>2. 12 people were killed in the military plane crash.<br>3. Rescue workers were on the scene after the crash. | 3 |
| meta-llama/Llama-3.2-1B-Instruct | 1. Video shows rescue workers on the scene after a military plane crash that killed 12 people in Myanmar on June 10, 2021.<br>2. The crash occurred in Myanmar on June 10, 2021.<br>3. The crash killed 12 people in Myanmar on June 10, 2021.<br>4. The crash occurred in Myanmar on June 10, 2021. | 4 |
| meta-llama/Llama-3.2-3B-Instruct | 1. Video shows rescue workers on the scene after a military plane crash that killed 12 people in Myanmar on June 10, 2021.<br>2. The military plane crashed in Myanmar on June 10, 2021.<br>3. The military plane that crashed in Myanmar on June 10, 2021, killed 12 people.<br>4. The people killed in the military plane crash in Myanmar on June 10, 2021, were 12. | 4 |
| google/gemma-3-1b-it | 1. Video shows rescue workers on the scene after a military plane crash in Myanmar on June 10, 2021. | 1 |
| google/gemma-3-4b-it | 1. Video shows rescue workers on the scene.<br>2. The scene is after a military plane crash.<br>3. The military plane crash killed 12 people.<br>4. The military plane crash occurred in Myanmar.<br>5. The date of the military plane crash was June 10, 2021. | 5 |
| gpt-3.5-turbo-0125 | 1. The military plane crash killed 12 people in Myanmar on June 10, 2021.<br>2. The video shows rescue workers on the scene after the military plane crash in Myanmar on June 10, 2021. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. A military plane crash killed 12 people in Myanmar on June 10, 2021.<br>2. Rescue workers were on the scene after the military plane crash that killed 12 people in Myanmar on June 10, 2021.<br>3. A video shows rescue workers on the scene after the military plane crash that killed 12 people in Myanmar on June 10, 2021. | 3 |
| gpt-5.4-nano-2026-03-17 | 1. - | 1 |
| gpt-5.4-mini-2026-03-17 | 1. Video shows rescue workers on the scene after a military plane crash in Myanmar on June 10, 2021.<br>2. A military plane crash in Myanmar on June 10, 2021 killed 12 people. | 2 |

---

## Sample ID: quantemp_298
**Original Claim**: In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians.<br>2. In late December 2020, U.S. Rep Ilhan Omar criticized Rep. Alexandria Ocasio-Cortez.<br>3. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians for getting a COVID-19 vaccine before most Americans. | 3 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In late December 2020, U.S. Rep. Ilhan Omar criticized federal politicians, including Rep. Alexandria Ocasio-Cortez.<br>2. U.S. Rep. Ilhan Omar criticized federal politicians, including Rep. Alexandria Ocasio-Cortez, for getting a COVID-19 vaccine before most Americans. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans.<br>2. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans. | 2 |
| meta-llama/Llama-3.2-3B-Instruct | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans. | 1 |
| google/gemma-3-1b-it | 1. Late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez.<br>2. COVID-19 vaccine getting a COVID-19 vaccine before most Americans. | 2 |
| google/gemma-3-4b-it | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians.<br>2. U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez.<br>3. U.S. Rep Ilhan Omar criticized federal politicians for getting a COVID-19 vaccine.<br>4. Rep. Alexandria Ocasio-Cortez got a COVID-19 vaccine.<br>5. Federal politicians got a COVID-19 vaccine. | 5 |
| gpt-3.5-turbo-0125 | 1. U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez.<br>2. U.S. Rep Ilhan Omar criticized federal politicians for getting a COVID-19 vaccine before most Americans.<br>3. U.S. Rep Alexandria Ocasio-Cortez got a COVID-19 vaccine before most Americans. | 3 |
| gpt-4.1-mini-2025-04-14 | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans. | 1 |
| gpt-5.4-nano-2026-03-17 | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians including Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans. | 1 |
| gpt-5.4-mini-2026-03-17 | 1. In late December 2020, U.S. Rep Ilhan Omar criticized federal politicians for getting a COVID-19 vaccine before most Americans.<br>2. In late December 2020, U.S. Rep Ilhan Omar criticized Rep. Alexandria Ocasio-Cortez for getting a COVID-19 vaccine before most Americans. | 2 |

---

## Sample ID: quantemp_299
**Original Claim**: In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam and evacuate refugees.

| Model | Decomposed Claims | Count |
|---|---|---|
| Qwen/Qwen3-4B-Instruct-2507 | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| Qwen/Qwen2.5-1.5B-Instruct | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| meta-llama/Llama-3.2-1B-Instruct | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam and evacuate refugees.<br>2. President Gerald Ford's efforts to aid South Vietnam and evacuate refugees.<br>3. President Gerald Ford's efforts to aid South Vietnam and evacuate refugees. | 3 |
| meta-llama/Llama-3.2-3B-Instruct | 1. In 1975, Joe Biden was a U.S. Senator.<br>2. Joe Biden opposed efforts by Gerald Ford in 1975 to aid South Vietnam.<br>3. Joe Biden opposed efforts by Gerald Ford in 1975 to evacuate refugees. | 3 |
| google/gemma-3-1b-it | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam and evacuate refugees. | 1 |
| google/gemma-3-4b-it | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| gpt-3.5-turbo-0125 | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| gpt-4.1-mini-2025-04-14 | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| gpt-5.4-nano-2026-03-17 | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |
| gpt-5.4-mini-2026-03-17 | 1. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to aid South Vietnam.<br>2. In 1975, then-U.S. Sen. Joe Biden opposed efforts by President Gerald Ford to evacuate refugees. | 2 |

---
