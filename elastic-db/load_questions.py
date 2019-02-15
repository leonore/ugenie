general_questions = [{"question": "Plan Code",
                    "topic": "acronyms",
                    "answer": "Plan Code is the unique code given to a course when created on MyCampus"},
                    {"question": "MaRio decision",
                    "topic": "acronyms",
                    "answer": "It means admissions have the decision-making capacity, not the school"},
                    {"question": "FT",
                    "topic": "acronyms",
                    "answer": "FT means full-time."},
                    {"question": "PT",
                    "topic": "acronyms",
                    "answer": "PT means part-time."},
                    {"question": "IELTS requirements",
                    "topic": "requirements",
                    "answer": "IELTS requirements is the English language test score required for non-English speakers"},
                    {"question": "ATAS",
                    "topic": "acronyms",
                    "answer": "The Academic Technology Approval Scheme (ATAS) requires all international students\
                    subject to existing UK immigration permissions, who are applying to study for a postgraduate qualification\
                     in certain sensitive subjects, knowledge of which could be used in programmes to develop weapons of mass destruction\
                     (WMDs) or their means of delivery, to apply for an Academic Technology Approval Scheme (ATAS) certificate before they can study in the UK."}
                    ]

short_questions = [{"question": "Is there funding available?",
                    "topic": "funding",
                    "answer": "https://www.gla.ac.uk/study/short/informationforstudents/fees/"},
                    {"question": "Can I have a refund?",
                     "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                    {"question": "Can I transfer?",
                    "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                     {"question": "Can I cancel?",
                     "topic": "cancellations",
                     "answer": "https://www.gla.ac.uk/study/short/informationforstudents/transfers/"},
                  ]

for q in general_questions:
    q["type"] = "admissions"

for q in short_questions:
    q["type"] = "short"

questions = general_questions + short_questions
for i in range(len(questions)):
    questions[i]["index"] = i+1
