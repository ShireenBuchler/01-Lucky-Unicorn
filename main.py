#Ask user for a number
#get_number = int(input("choose a number?"))

#Multiply number by 5
#times_five = get_number * 5

#answer = "{} times 5 is equal to {}".format(get_number, times_five)

#show output
#print(answer)

#count up from 1 to 10
print("\ngoing up")
for item in range(0,10+1,2):
  print(item)
  
#count down from 10 to 1
print("\nGoing down")
for item in range(10,0,-2):
  print(item)  
  
#loop trough a string
print("\na string")
greeting = "hello world"

for letter in greeting(2):
  print(letter)
  
#loop through a list/array
print("\na list")
options = ["unicorn","zebra","horse","donkey"]
for item in options:
  print item