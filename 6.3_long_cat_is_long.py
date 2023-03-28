
def count_words(t):
    """
      This function takes a string as input and returns a dictionary with each unique word in the input string as keys and the length of the words as values.
      It only considers alphanumeric words and excludes any other characters or symbols.

      Args:
      t (str): The input text to be analyzed.

      Returns:
      dict_variable (dict): A dictionary containing words as keys and their respective lengths as values.
      """
    pattern = ".,!?"
    t = [c.strip(pattern) for c in t.split(" ") if c.strip(pattern).isalpha()]
    dict_variable = {word: len(word) for word in t}
    return dict_variable


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat."""
    print(count_words(text))
