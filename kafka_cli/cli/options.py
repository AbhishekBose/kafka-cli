from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint


class options:    
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
                'type': 'input',
                'name': 'broker',
                'message': 'What is your broker address?',
                'filter': lambda val: val.lower()
            }
        ]
        answers = prompt(questions)
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
    def topic_option(topic_list):

        topic_list = ["other"]+topic_list
        # exit()
        # con_question = [
        #     {
        #         "type":"confirm",
        #         "name":"start",
        #         "message":"Shall we start reading messages?"
        #     }
        # ]
        
        # prod_question = [
        #     {
        #         "type":"confirm",
        #         "name":"start",
        #         "message":"Shall we start producing messages?"
        #     }
        
        # ]
        if len(topic_list):
            questions = [
                {
                    "type": "list",
                    "name":"topics",
                    "message":"Select topic from below. Choose other in case not present:",
                    "choices":topic_list,
                    'filter': lambda val: val.lower()
                }
            ]
            answers = prompt(questions)
        else:
            answers = {}
        
        # if answers["choices"]=="consume":
        #     opt_answer = prompt(con_question)
        # else:
        #     opt_answer = prompt(prod_question)
        
        # answers.update(opt_answer)
        
        return answers

if __name__ == "__main__":
    options.option_page()