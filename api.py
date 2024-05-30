import openai


class GeneralApi:
    def __init__(self, config, model = 'gpt-3.5-turbo') -> None:
        self.key = config['key']
        self.platform = config['platform']
        self.model = config['model']

        openai.api_key = self.key
        openai.api_base = config['api_base']

    def run(self, message, prompt):
        return self.ask(message, prompt)

    def ask(self, message, prompt):

        messages_list=[{"role": "system", "content": message},
                       {"role": "user", "content": prompt},
                       ]

        result = openai.ChatCompletion.create(
            model=self.model,
            messages=messages_list,
            temperature = 0,
            max_token = 1024,
            )
        return result['choices'][0]['message']['content']


if __name__ == "__main__":
    # key = 'sk-proj-T12yf0xMw9PNWhwMcFbHT3BlbkFJEAs7lGsVlPVjZvq4XQgO'
    # key_l = 'sk-Xn2FJsrA8QTBUXU68983FaF148214f7485C9191802716cA0'
    key_kwwai = 'sk-D28MPhpzU4CY0HpYDb4f1a95E6564fC2Ac9a23D7551c99D7'

    message = "You are GPT-4, answer my questions as if you were an expert in the field."
    prompt = "Write a blog on how to use GPT-4 with python in a jupyter notebook"

    gpt_api = GeneralApi(key_kwwai, model="gpt-3.5-turbo")
    gpt_api.run(message, prompt)
