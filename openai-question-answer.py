import openai
import sys

openai.api_key='<aquí debes copiar tu secret key>'

def generate_answer(question):
    response=openai.Completion.create(
        model='text-davinci-003', 
        prompt=question, 
        temperature=0, 
        max_tokens=150, 
        top_p=1, 
        frequency_penalty=0, 
        presence_penalty=0
    )
    print(response.choices[0].text.strip())

if __name__ == '__main__':
    generate_answer(sys.argv[1])