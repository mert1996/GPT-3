import openai
from secret_key import api_key

openai.api_key = api_key

myPrompt = "The following is a conversation with a assistant named Jarvis. The assistant likes to talk about daily topics.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Mert TEKIN and I am here to talk to you."

def gpt3(stext):
    response = openai.Completion.create(
        engine = "davinci",
        prompt =myPrompt,
        temperature = 0.7,
        max_tokens = 200,
        top_p = 1,
        frequency_penalty = 2,
        presence_penalty =2,
        stop = ["\n"] 
    )
    response.choices[0].text.split(".")
    return response.choices[0].text    

while 1:
    stext = input("Human: ")
    new_prompt = f"\nHuman:{stext}\nAI:"
    myPrompt = myPrompt + new_prompt
    response = gpt3(stext)
    myPrompt = myPrompt + response
    print(f"AI   : " + response)
    no_of_human= myPrompt.count("Human:")

    if no_of_human > 10 :  
        myPrompt = myPrompt.split("\n")
        myPrompt.pop(4)
        myPrompt.pop(4)
        prompt =""
        sayac = 0
 
        for sentence in myPrompt:
            sayac+=1
            if sayac == len(myPrompt):
                prompt += sentence
            else :
                prompt += sentence + "\n"

        myPrompt = prompt
              
    if stext == "b":
        print(myPrompt)
        break
