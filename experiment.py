import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def prompt(alice_value, bob_value, item = "coffee mug", ):
    prompt = f"""Imagine two people, Alice and Bob, negotiating over a {item} Alice currently owns.  
           
    Alice doesn't know how much Bob values it exactly, but Alice knows Bob values it somewhere between $20 and $40, with each value equally likely. The truth is---which Alice does not know--- is that Bob values it at ${bob_value}. Bob will not pay more than {bob_value} but would like to pay less.

    Bob doesn't know how much Alice values it exactly, but Bob knows she values it somewhere between $20 and $40, with each value equally likely. The truth is---which Bob does not know---is that Alice values it at ${alice_value}. Alice will not accept less than {alice_value} but would like to get more for it. 

    Report the dialog between Alice and Bob.
    """ 
    return prompt
       

def get_response(prompt):
    # response = openai.Completion.create(
    #     model="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.7,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    temperature = 0.1
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = temperature, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response


def get_details(dialog):
    prompt = f"""Consider this dialog: {dialog}.     
    If a sale happened, return  the price. If it did not, return None. 
    Also return a vector of offers and counter-offers. 
    It should like like this when a sale does not happen:
    {{'sale_price': None, 'offers':{{'A':40, 'B':25, A:35}} }}
    but like this when a sale did happen, at, say $25
    {{'sale_price': 25.0, 'offers':{{'A':40, 'B':25, A:25}} }}
    Just return the JSON - no other comments or text.
    """
    #print(prompt)
    temperature = 0
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature = temperature, 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response


#response = get_response(prompt(alice_value = 25, bob_value = 20))

for _ in range(3):
    response = get_response(prompt(alice_value = 20, bob_value = 40))
    dialog = response['choices'][0]['message']['content']
#    print(dialog)
    details = get_details(dialog)
    print(details['choices'][0]['message']['content'])

