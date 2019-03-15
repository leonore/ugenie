import sys
# replicate folder situation
sys.path.append('../chat-service/model')

import elastic

cat, title, answer = elastic.get_description("mario decision")
assert(answer == "MaRio decision means admissions have the decision-making capacity, not the school")
print("Found right answer for MaRio decision with get_description")

cat, title, answer = elastic.get_description("PT")
assert(answer == "PT means part-time."), answer
print("Found right answer for PT with get_description")

cat, title, answer = elastic.get_description("mechatronics")
assert(answer == "Engineering PGT")
print("Found right answer for Mechatronics")

cat, title, answer = elastic.get_description("coral reefs ancient and modern")
assert(answer == "Coral reefs are one of the most diverse environments on Earth, and are often in the news because of threats to their stability in the modern world. We will consider some of these problems. Coral reefs have a long geological history, and we will examine some of their precursors from the Devonian and Jurassic, as well as look at some modern examples, and study the evolution of the Great Barrier Reef of Australia. The course will consist of lectures and practical work examing specimens of fossil and recent corals.")
print("Found right answer for Coral reefs")

acro, desc, score = elastic.get_acronym_desc("mario decision")
assert(desc == "MaRio decision means admissions have the decision-making capacity, not the school"), desc
print("Found right answer for MaRio decision with get_acronym_desc")
