"""
Author: Dillon Glasser
Class: CS3023 Intermediate Programming
Assignment: Program Assignment 3
Date: 5/18/2016

"""

from PA3_Glasser_signature import Signature
from PA3_helper import Helper
import os.path

signature = Signature()
helper = Helper()
weights = [0, 11, 33, 50, 0.4, 4]


filename = helper.get_valid_filename("Please enter your Mystery document's filename: ")

with open(filename) as f:
    content = f.readlines()

print("Calculating...")

fiveFeatures = [filename]
fiveFeatures.append(signature.average_word_length(content))
fiveFeatures.append(signature.type_token_ratio(content))
fiveFeatures.append(signature.hapax_legomana_ratio(content))
fiveFeatures.append(signature.average_sentence_length(content))
fiveFeatures.append(signature.average_sentence_complexity(content))
print("The five feature numbers are: ", fiveFeatures)


directory = helper.read_directory_name("Please enter name of directory: ")
signatureNames = os.listdir(directory)


aSignature = signatureNames[0]
sig2 = helper.read_signature('signature/'+aSignature)
likelyScore = signature.compare_signatures(fiveFeatures, sig2, weights)
likelyAuthor = sig2[0]

for aSig in signatureNames[1:]:

    sig2 = helper.read_signature('signature/'+aSig)
    possibleScore = signature.compare_signatures(fiveFeatures, sig2, weights)

    if possibleScore < likelyScore:
        likelyScore = possibleScore
        likelyAuthor = sig2[0]

likelyAuthor = helper.clean_up(likelyAuthor)

print("\nBest author match: '%s' \n with score %s." % (likelyAuthor,likelyScore))


