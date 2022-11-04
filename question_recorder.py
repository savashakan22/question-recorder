from datetime import datetime
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

global question_record
question_record = pd.DataFrame({
                            "date"      : [],
                            "name"      : [],
                            "department": [],
                            "subject"   : [],
                            "question"  : [],
                            "topic"     : []
})

if os.path.isfile('question_record.csv'):
    question_record = pd.read_csv('question_record.csv')

else:
    question_record.to_csv('question_record.csv')
    
    
class student:


    def __init__(self, name):
        self.name = name
        pass

    
    def add_question(self, department, subject, question, topic, date):
        """ Adds question amount the to name of the student.
                    department -->     Which exam does the questions belong to TYT or AYT
                    subject    -->     Which subject does the questions belong (Like Math, Pyhsics...)
                    question   -->     Amount of the solved questions
                    date       -->     Date is in the DD-MM-YYYY . In the default mode it will add automatically the recorded day
                    topic      -->     Topic of the questions (Like Algebra, Newton's Laws...)"""

        global question_record

        question_record = question_record.append(pd.DataFrame({
                            "date"      : [date],
                            "name"      : [self.name],
                            "department": [department],
                            "subject"   : [subject],
                            "question"  : [question],
                            "topic"     : [topic] 
        }))
        
        question_record.to_csv("question_record.csv")
    
    def question_frame(self):
        """Returns the question_record dataframe.
            Used to transfer data to GUI part"""
        
        return question_record


