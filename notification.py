from win11toast import toast

def show_notification():
    toast("Script Started", "Your Python script is now running.")



while True:
    userinput = input("tpye 'exit' to exit: ")

    if userinput == "exit":
        break
    else:
        show_notification()
        continue