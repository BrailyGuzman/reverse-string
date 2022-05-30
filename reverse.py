while(1):
    reverse_input = input("[?} Enter Word: ")

    reverse = (reverse_input) [::-1]

    if reverse == (reverse_input):
        print("[+] Word: " + reverse_input)
        print("[/] This word is a palindrome. [\]")
    else:
        print("[+] Word: " + reverse_input)
        print("[X] This Word is not a palindrome. [X]")
