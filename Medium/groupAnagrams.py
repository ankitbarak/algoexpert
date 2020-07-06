# Write a function that takes in an array of strings and groups anagrams together

# Anagrams are strings made up of exactly the same letters, where order doesn't matter.
# For eample, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

# Your function should return a list of anagram groups in no particular order.

def groupAnagrams(words):
    anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())