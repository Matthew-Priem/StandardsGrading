def palindromes(words):
    result = {"palindrome": [], "non-palindrome": []}
    
    reversed_word = ''
    for word in words:        
        #reverse the word and check if it is the orginal word
        for letter in word:
            reversed_word = letter + reversed_word
            if reversed_word == word:
                result["non-palindrome"].append(word)
            else:
                result["palindrome"].append(word)
    
    return result

# Test the function with a sample input
print(palindromes(["madam", "racecar", "hello", "level", "python"]))
# Expected output: {'palindrome': ['madam', 'racecar', 'level'], 'non-palindrome': ['hello', 'python']}

print(palindromes(["noon", "civic", "deed", "open", "loop"]))
# Expected output: {'palindrome': ['noon', 'civic', 'deed'], 'non-palindrome': ['open', 'loop']}

print(palindromes(["apple", "banana", "cherry"]))
# Expected output: {'palindrome': [], 'non-palindrome': ['apple', 'banana', 'cherry']}