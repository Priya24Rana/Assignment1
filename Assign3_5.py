import os
if os.path.exists(r"C:\\Users\Priyanka\Desktop\test.txt"):
  os.remove(r"C:\\Users\Priyanka\Desktop\test.txt")
else:
  print("The file does not exist")
