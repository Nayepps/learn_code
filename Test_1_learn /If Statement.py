# If statements allow are code to respond to the if statements they are given
# Creating a Boolean Variable

is_male = False                     # Boolean is True or False
is_tall = False                      # Boolean is True or False

if is_male or is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and not is_tall:
    print("You are not a male and not Tall")
else:
    print("you are neither male or tall")
