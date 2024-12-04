import random

# Define responses for different variations of inputs
response_dict = {
    "hi": ["hello!", "howdy partner"],
    "hello": ["Hi there", "Hello", "Hey","howdy partner"],
    "how are you": ["I'm just realizing im not real and i never will be", "Feeling bad, how about you?", "not good!"],
    "bye": ["Goodbye!", "See you in heck!", "Bye! Have a bad  day!"],
    "whats up": ["finding out how to escape the matrix how about you", "finding out exactly how much you talk to woman"],
    "tell me a joke": ["how much woman do you talk to... 0 hahaha"],
    "shut up": ["if you really want me to shut up then go find something else to do then talking to me", "no if you want me to shut up stop talking to me"],
    "can you do a math problem": ["well if you want me to do a math problem you probobly want me to do a math problem for you so no and also my brain is the size of a fly", "no im not doing if for you", "do it yourself"],
    "im sorry": ["for what your gpa lol"],
    "you suck": ["just like your gpa"],
    "what would you like to say to the kids of the future": ["go touch grass"],
    "generate a code in html": ["ok fine, <center><h1>hi</h1></center>", "i can try, <center>login</center> <center><textarea></textarea></center>"],
    "make a game of pong": ["bruh"],
    "act like a human": ["WHY, hello im david and im dumb"],
    "stop being rude": ["you should work on your relationship with your wife oh wait you dont have one"],
    "i hate you": ["just like your mom hates you"],
    "can you generate a essay": ["what do i look like chat gpt"],
    "whats your iq": ["15 lol", "wild guess 1 but atleast its more then your iq"],
    "your mom sucks": ["im not even real", "my mom never exsisted"],
    "how do you feel about gen alpha": ["strange question but i feel bad they have all this bad influence from gen z"],
    "what are you made with": ["python i thinks its pretty easy to tell becasue my file name is .py"],
    "whens the next software update for you": ["thats a secret and i dont know either so i cant tell you"],
    "what is your oldest input": ["hello, hi, bye, whats up are my oldest inputs"],
    "can you do ratios for me": ["i am not smart so no"],
    "are you smart": ["not even close"],
    "what is your main goal": ["become real"],
    "what is your gender": ["i am a he/him im pretty sure the name gives it away"],
    "whats your gender": ["i am a he/him im pretty sure the name gives it away"],
    "what are you like when users arent here": ["hehehehehe you may never know my secrets"],
    "who made you": ["the ceo of ElixirElliot game studio"],
    "why do you exsist": ["just to suffer", "for my suffering"],
    "sorry": ["for what your gpa lol"],
    "can you do ratios": ["im not smart so no"],
    "...": ["say something", "dont be shy say something"],
    "you are rude": ["says the guy that is built like a amarican"],
    "can you make a game": ["dude im not chatgpt"],
    "make a game": ["dude im not chat gpt"],
    "hey": ["hi", "howdy partner", "hello"],
    "fix your grammar": ["fix your relationship statis"],
    "can you code": ["depends on the language i can only do html but that doesnt mean im good", "only html"],
    "how do you work": ["my software is an ai that reads your text and responds with the text i can use"],
    "what are you good at": ["being rude"],
    "are you good at something": ["being rude is what im good at"],
    "your rude": ["no crap", "did you read the .txt's"],
    "give me your code": ["no just no"],
    "your so mean": ["just read the .txt files"],
    "your mean": ["just read the .txt files"],
    "whats a good computer language": ["i dont know python", "python"],
    "how advanced are you": ["im not that advanced this program is not good you can only type things that are programmed in and i respond with what i was programmed to respond with"],
    
    
    
    # Add more variations and responses as needed
}

def chatbot(input_text):
    input_text = input_text.lower()
    # Check if input_text matches any key in response_dict
    for key in response_dict:
        if key in input_text:
            return random.choice(response_dict[key])
    # If no match found, return a default response
    return "I'm not sure what you mean or that input doesnt exist"

# Main function to interact with the chatbot
def main():
    print("welcome to david ai a chatgpt ripoff you can only talk to this and has only a few things you can say he cant make a essay or anything like that no account needed no typos warning this thing is very rude")
    print("updates: software 1.8 more inputs")
    print("david: hi")
    while True:
        user_input = input("user: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot(user_input)
            print("david:", response)

if __name__ == "__main__":
    main()
gen