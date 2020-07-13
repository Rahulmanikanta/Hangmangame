import random 
# A Library that we use to choose a random word from a list of words.
  
name = input("Enter Your Good Name Please...") 
# Here the user will enter His/Her name
  
print("Best Of Luck !... ", name) 
  
words = ['Rahul', 'computer', 'science', 'Student',  
         'good', 'Python', 'Programmer', 'web developer',  
         'google', 'enthusiastic']  
  
# Function to choose one random word from this list of words. 
word = random.choice(words) 
  
  
print("Guess the characters") 
  
guesses = '' 
  
# The total number of Gusses 
turns = 5
   
  
while turns > 0: 
      
   # A variable to count the number of turns 
    failed = 0
      
    # The characters from the input taking one word at a time. 
    for char in word:  
          
        # comparing that character with the characters in the word. 
        if char in guesses:  
            print(char) 
              
        else:  
            print("_") 
              
            # For every failure attempt the failed count will be increased by one. 
            failed += 1
              
  
    if failed == 0: 
        # If the count of the failure is stills remains 0 then congratulations you won will be displayed as output. 
        print("Congratulations " + name + "You won !...")  
          
        # This will print the word
        print("Your word is: ", word)  
        break
      
    # if user has input the wrong alphabet then it will ask user to enter another alphabet. 
    guess = input("guess a character:") 
      

    guesses += guess  
      
    # Checking the user entered character with the word.
		
    if guess not in word: 
          
        turns -= 1
          
        # If the character does not match the word then “Wrong” will be given as the output.
        print("Wrong") 
          
        #It will print the number of turns remaining for the user.
        print("You still have", + turns, 'more guesses') 
          
          
        if turns == 0: 
            print("Oh!.... "+ name + "You Have Lost the Game Let's Give Another Try.") 
