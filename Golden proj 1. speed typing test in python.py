import random
import time

def get_sentence():
  """Returns a random sentence."""
  words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
  sentence = ""
  for _ in range(5):
    word = random.choice(words)
    sentence += word + " "
  return sentence

def main():
  """Runs the speed typing test."""
  sentence = get_sentence()
  start_time = time.time()
  typed_sentence = input("Type the sentence: ")
  end_time = time.time()

  # Calculate the typing speed.
  typing_speed = len(typed_sentence) / (end_time - start_time)
  typing_speed = typing_speed * 60
  print("Your typing speed is: {} WPM".format(typing_speed))

if __name__ == "__main__":
  main()
