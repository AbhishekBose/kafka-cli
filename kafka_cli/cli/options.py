from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint

class options:    
    @staticmethod
    def option_page():
        questions = [
            {
                'type': 'list',
                'name': 'Kafka operation',
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

        answers = prompt(questions)
        print(answers)

if __name__ == "__main__":
    options.option_page()