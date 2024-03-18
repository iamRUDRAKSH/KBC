name = input("Enter your full name : ")
print(f"Lets's Begin {name}.\n")

Questions = [ 
    ["What is the capital city of France?", "Madrid", "Berlin", "Paris", "Rome", 3],
    ["What is the chemical symbol for water?", "O", "H2O", "CO2", "NaCl", 2],
    ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "J.K. Rowling", "Ernest Hemingway", " F. Scott Fitzgerald", 1],
    ["Who is known as the father of modern physics?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 1],
    ["Which planet is known as the Red Planet?", "Jupiter", "Mars", "Venus", "Saturn", 2],
    ["In which year did the Titanic sink?", "1912", "1915", "1918", "1920", 1],
    ["What is the largest mammal in the world?", "Elphant", "Girrafe", "Polar Bear", "Blue Whale", 4],
    ["What is the main ingredient in guacamole?", "Toamtoes", "Onion", "Avocado", "Peppers", 3],
    ["Which element has the chemical symbol Fe?", "Iron", "Gold", "Silver", "Copper", 1],
    ["What is the speed of light in a vacuum?", "150000", "300000", "100000", "500000", 2],
    ["Which continent is the largest by land area?", "Asia", "Europe", "North America", "Africa", 1],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", " Leonardo da Vinci", 4],
    ["What is the currency of Japan?", "Euro", "Yen", "Dollar", "Pound", 2],
    ["What is the longest river in the world?", "Amazon", "Nile", "Mississipi", "Yangtze", 1],
    ["Who was the first woman to win a Nobel Prize?", "Rosa Parks", "Jane Addams", "Mother Teresa", "Marie Curie", 4],
    ["What is the process by which plants make their own food called?", "Photosynthesis", "Respiration", " Transpiration", "Germination", 1],
]

Levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000]
Money = 0
for i in range(16):
    Question = Questions[i]
    print(f"Question for Rs. {Levels[i]}")
    print(i+1, Question[0], sep = ". ")
    print(f"a. {Question[1]}        b. {Question[2]}")
    print(f"c. {Question[3]}        d. {Question[4]}")
    print("\n")
    reply = int(input("Enter your answer (1-4) or press 0 to QUIT : "))
    print("\n")
    if(reply == Question[-1]):
        print(f"Congratulations you won Rs. {Levels[i]}!!\n")
        if(i == 4):
            Money = 10000
        elif(i == 9):
            Money =  320000
        elif(i == 15):
            print("EK CRORE!!(Amitabh Bachchan Voice)")
            Money = 10000000
    elif(reply == 0):
        if(i == 0):
            Money = 0
        else:    
            Money = Levels[i-1]
        break
    else:
        print("Oops!! Worng Answer.")
        print(f"Correct Answer was {Question[-1]}.\n")
        break

print(f"You have won Rs. {Money}!!")    