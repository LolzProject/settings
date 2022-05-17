# Add code

option = input("settings>>> ")
if option == "reset":
  print("Feature still a WIP.")
elif option == "change-name":
  user = input("settings/change-name>>> ")
  print("Name changed.")
elif option == "clear":
  print("Are you sure?")
  option = input("(y/n)>>> ")
  if option == "y":
    os.system('clear')
    print("Cleared.")
    time.sleep(5)
    os.system('clear')
  elif option == "n":
    print("Canceled operation.")
  else:
    print("Invalid Input, Canceling...")
