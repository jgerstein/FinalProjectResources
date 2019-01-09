examining = True

options = ['book', 'umbrella', 'notebook', 'pen']

while examining:
    choice = input(f"Choose one of the following: {', '.join(options)}")
    
    while choice not in options:
        choice = input(f"Choose one of the following: {', '.join(options)}")
    
    print("Examining stuff")
    
    options.remove(choice)
        
    if input("Do you want to examine more evidence?").lower() in ['no', 'n'] or len(options) == 0:
        examining = False