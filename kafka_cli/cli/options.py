from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint

class options:    
    @staticmethod
    def option_page():
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
                'name': 'topic',
                'message': 'What is the name of your topic?',
                'filter': lambda val: val.lower()
            },
            {
                'type': 'input',
                'name': 'broker',
                'message': 'What is your broker address?',
                'filter': lambda val: val.lower()
            }
        ]

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
        answers = prompt(questions)
        
        if answers["choices"]=="consume":
            prompt(con_question)
        else:
            prompt(prod_question)

if __name__ == "__main__":
    options.option_page()