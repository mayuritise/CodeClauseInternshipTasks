import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
  password = ""
  for _ in range(length):
    password += random.choice(characters)
  return password

def main():
  """Generates and prints a random password."""
  length = int(input("How many characters do you want in your password? "))
  password = generate_password(length)
  print(f"Your password is: {password}")

if __name__ == "__main__":
  main()
