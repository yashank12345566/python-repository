s = input("Type your input here:")
reverse=s[::-1]#[start:stop:step]
if( s== reverse):
    print("Yes it is a palindrome")
else:
    print("No it is not a palindrome")
