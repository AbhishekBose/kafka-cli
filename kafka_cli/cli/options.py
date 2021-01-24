from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint
from .log import log
import time

class options:  

    @staticmethod
    def greet():
        color = "blue"
        log("Kafka CLI",color=color,figlet=True)
        log("Welcome to Kafka CLI", "green")
        time.sleep(1)

    @staticmethod
    def opt_option():
        questions = [
            {
                'type': 'list',
                'name': 'choices',
                'message': 'What operation do you want to perform?',
                'choices': ['Produce', 'Consume'],
                'filter': lambda val: val.lower()
            },

            {
                'type': 'confirm',
                'name': 'broker',
                'message': 'Is your broker localhost:9092?',
            }
        ]

        broker_question = [
            {
                'type': 'input',
                'name': 'broker',
                'message': 'What is your broker?',
                'filter': lambda val: val.lower()
            }
        ]
        answers = prompt(questions)
        if answers["broker"]:
            answers["broker"]="localhost:9092"
        else:
            broker_answer = prompt(broker_question)
            answers["broker"]= broker_answer["broker"]
        return answers
    

    @staticmethod
    def topic_prompt():
        questions = [
            {
                'type': 'input',
                'name': 'topic',
                'message': 'What is the name of your topic?',
                'filter': lambda val: val.lower()
            }
        ]
        answers = prompt(questions)
        return answers

    @staticmethod
    def confirm_opt(opt_type):
        con_question = [
            {
                "type":"confirm",
                "name":"start",
                "message":"Shall we start reading messages?"
            }
        ]
        
        prod_question = [
            {
                "type":"confirm",
                "name":"start",
                "message":"Shall we start producing messages?"
            }
        
        ]
        if opt_type["choices"]=="consume":
            opt_answer = prompt(con_question)
        else:
            opt_answer = prompt(prod_question)
        
        return opt_answer

    @staticmethod
    def topic_option(topic_list):

        topic_list = ["other"]+topic_list
        # exit()
        # 
        if len(topic_list):
            questions = [
                {
                    "type": "list",
                    "name":"topic",
                    "message":"Select topic from below. Choose other in case not present:",
                    "choices":topic_list,
                    'filter': lambda val: val.lower()
                }
            ]
            answers = prompt(questions)
        else:
            answers = {}
        

        if answers["topic"]=="other":
            answers = options.topic_prompt()
        return answers

if __name__ == "__main__":
    options.option_page()