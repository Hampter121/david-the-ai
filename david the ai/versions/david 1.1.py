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
