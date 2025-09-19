import random 
from datetime import datetime
import os
import pyttsx3
def speak(text):
    engine= pyttsx3.init()
    engine.setProperty("rate",160) #spped of voice
    engine.setProperty("volume",1) #Volume of voice
    engine.say(text)
    engine.runAndWait()
    engine.stop


name={
    "Sports": ["Virat Kohli", "MS Dhoni", "Lionel Messi", "Cristiano Ronaldo"],
    "Bollywood": ["Shahrukh Khan", "Salman Khan", "Alia Bhatt", "Kareena Kapoor"],
    "Politics": ["Narendra Modi", "Barack Obama", "Donald Trump", "Rahul Gandhi"],
    "Random Fun": ["A group of monkeys", "An alien", "Your neighbor", "A robot"],
    "Tech": ["Elon Musk", "Mark Zuckerberg", "Bill Gates", "Sundar Pichai"]
}

action={
    "Sports": ["hits century at", "throws ball into", "dances in", "declares match at"],
    "Bollywood": ["dances at", "launches movie in", "sings loudly at", "shouts in"],
    "Politics": ["announces election in", "argues at", "gives speech at", "debates in"],
    "Random Fun": ["steals samosa from", "starts singing at", "falls asleep in", "rides bicycle around"],
    "Tech": ["launches rocket from", "codes all night at", "hacks into", "builds AI in"]
}

places={
    "Sports": ["Eden Gardens", "Wankhede Stadium", "Old Trafford", "Chinnaswamy Stadium"],
    "Bollywood": ["Film City Mumbai", "Red Carpet", "IIFA Awards", "Local Theatre"],
    "Politics": ["Parliament House", "White House", "India Gate", "UN Headquarters"],
    "Random Fun": ["a chai tapri", "a samosa stall", "a playground", "a bus stand"],
    "Tech": ["Silicon Valley", "ISRO", "NASA HQ", "Google Office"]
}
folder="Headlines"
os.makedirs(folder, exist_ok=True)
today=datetime.now().strftime("%d-%m-%Y")
filename=os.path.join(folder,f"headlines_{today}.txt")

def Show_headline():
    if not os.path.exists(folder) or not os.listdir(folder):
        print("No Headlines Saved Yet,")
        return
    print("\n All Saved Headlines:\n")
    for file in os.listdir(folder):
        filepath=os.path.join(folder,file)
        with open(filepath,"r") as f:
            print(f"---{file}---")
            print(f.read().strip())
            print()

def search_Headlines(Keyword):
    if not os.path.exists(folder) or not os.listdir(folder):
        print("No Headlines Saved Yet,")
        return
    print(f"\n Search Results for {Keyword}: \n")
    found=False
    for file in os.listdir(folder):
        filepath=os.path.join(folder,file)
        with open(filepath,"r") as f:
            for line in f:
                if Keyword.lower() in line.lower():
                    print(f"[{file}]{line.strip()}")
                    found=True
    
    if not found:
        print("No Matching Headlines Found.")

def generate(category):
    if category not in name:
        print("invalid category!! Please Chode again")
        return
    names=random.choice(name[category])
    actions=random.choice(action[category])
    place=random.choice(places[category])
    return f"Breaking News: {names} {actions} {place}"
while True:
    print("\nFunctions \n1.Generate Headlines \n2.View All Headlines That Are Generated \n3.Search Headlines \n4.Exit")
    choice=input("Choose an option: ").strip()
    if choice=="1":
        while True:
            print("Categories:\n1. Sports\n2. Bollywood\n3. Politics\n4. Random Fun \n5. Tech")
            category=input("Chose The Category: ").strip()
            headline=generate(category)
            if headline:
                print(headline)
                speak(headline)
                with open(filename,"a") as f:
                    f.write(f"{headline} \n")

            a=input("Do You want More Headline?(yes/no):").lower().strip()
        
            if a=='no':
                    break
    elif choice=="2":
        Show_headline()

    elif choice=='3':
        Keyword=input("Enter Keyword to Search: ").strip()
        search_Headlines(Keyword)

    elif choice=="4":
        print("Goodbye")
        speak("Goodbye")
        break
    else:
        print("Invalid Choice!!!!!")
