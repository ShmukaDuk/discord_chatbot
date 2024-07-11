
class OlamaAPI:
    def __init__(self, olama_address):
        self.filename = 'data/prompt'        
        self.init_prompt = self.load_init_prompt()
        self.olama_address = olama_address
        print(self.olama_address)


    def __str__(self):
        return f"Ollama_unhappy instance: {self.name}"
    
    def load_init_prompt(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def print_prompt(self):
        print (self.init_prompt)

    def run_lama(self, message_from_user):
        from ollama import Client
        client = Client(host=self.olama_address)
        response = client.chat(model='llama2-uncensored', messages=[
        {
            'role': 'user',
            'content': self.init_prompt + message_from_user,
        },
        ])
        message_content = response['message']['content']
        # print(message_content)
        return str(message_content)
    
    def greetUser(self, message_from_user=''):
        from ollama import Client
        client = Client(host=self.olama_address)
        response = client.chat(model='llama2-uncensored', messages=[
        {
            'role': 'user',
            'content': self.init_prompt,
        },
        ])
        message_content = response['message']['content']
        print('[OLAMA]:\t Response: ${message_content}')
        return str(message_content)

olama = OlamaAPI('http://192.168.1.196:11434')
print(olama.run_lama(''))