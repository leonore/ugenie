# Common questions asked about acronyms, as provided by the customer
admissions_questions = [{"question": "Plan Code",
                    "answer": "Plan Code is the unique code given to a course when created on MyCampus"},
                    {"question": "MaRio decision",
                    "answer": "MaRio decision means admissions have the decision-making capacity, not the school"},
                    {"question": "FT",
                    "answer": "FT means full-time."},
                    {"question": "PT",
                    "answer": "PT means part-time."},
                    {"question": "IELTS requirements",
                    "answer": "IELTS requirements is the English language test score required for non-English speakers"},
                    {"question": "ATAS",
                    "answer": "The Academic Technology Approval Scheme (ATAS) requires all international students\
                    subject to existing UK immigration permissions, who are applying to study for a postgraduate qualification\
                     in certain sensitive subjects, knowledge of which could be used in programmes to develop weapons of mass destruction\
                     (WMDs) or their means of delivery, to apply for a certificate before they can study in the UK."}
                    ]

short_questions = [{"question": "Is there funding available?",
                    "answer": "https://www.gla.ac.uk/study/short/informationforstudents/fees/"},
                    {"question": "Can I have a refund?",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                    {"question": "Can I transfer?",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                     {"question": "Can I cancel?",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                  ]

for q in admissions_questions:
    q["type"] = "admissions"

for q in short_questions:
    q["type"] = "short"

questions = admissions_questions + short_questions

# store index to populate elastic
for i in range(len(questions)):
    questions[i]["index"] = i+1
