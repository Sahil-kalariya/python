import re
def test(text):
	return bool(re.findall('[AEIOUaeiou] [AEIOUaeiou]', text))

text ="These exercises can be used for practice."
print("Original string:", text)
print("Two following words begin and end with a vowel in the said string:")
print(test(text))