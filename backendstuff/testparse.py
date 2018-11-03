import re

# testingstring = "If you're visiting this page, you're likely here because you're searching for a random sentence. Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. By inputting the desired number, you can make a list of as many random sentences as you want or need. Producing random sentences can be helpful in a number of different ways."
#
# hopefullyarray = testingstring.split(".")
# print(hopefullyarray)
#
# alsohopefullyanarray = [x for x in map(str.strip, testingstring.split('.')) if x]
# print(alsohopefullyanarray)
#
#
# randomstring = "wtffffff. weeeeeee! -10HP?"
#
# sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", randomstring)
# for sentence in sentences:
#     print(sentence)

def sentenceBreak(inputstring):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s", inputstring)
    return sentences
