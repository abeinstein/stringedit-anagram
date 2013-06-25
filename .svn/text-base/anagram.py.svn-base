# Anagram Finder -- Andrew Beinstein
import pprint
import itertools
import stringedit

# ----- PART 2 ------
def all_sets_of_anagrams(wordfile):
  """Returns all sets of anagrams, sorted by the length of the individual words"""
  anagram_hash = {}
  for word in wordfile.readlines():
    word = word.strip()
    sorted_word = ''.join(sorted(word))
    if sorted_word not in anagram_hash:
      anagram_hash[sorted_word] = [word]
    else:
      anagram_hash[sorted_word].append(word)
      
  all_anagrams = set()
  for k, v in anagram_hash.iteritems():
    if len(v) > 1:
      all_anagrams.add(tuple(v))
      
  return sorted(all_anagrams, key=length_of_set, reverse=True)
  
# ----- PART 5 -----
def sorted_sets_of_anagrams(wordfile):
  """Returns all n-sets, n >= 6, sorted first by the size (n), then
  by the length of the words in the set, and then by overlap score."""
  anagram_hash = {}
  for word in wordfile.readlines():
    word = word.strip()
    if len(word) < 6:
      None # Do nothing
    else:
      sorted_word = ''.join(sorted(word))
      if sorted_word not in anagram_hash:
        anagram_hash[sorted_word] = [word]
      else:
        anagram_hash[sorted_word].append(word)
        
  sorted_anagrams = set()
  for k, v in anagram_hash.iteritems():
    if len(v) > 1:
      sorted_anagrams.add(tuple(v))
      
  # Sort by increasing overlap...
  sorted_anagrams = sorted(sorted_anagrams, key=overlap_of_set)
  # Then by decreasing length...
  sorted_anagrams = sorted(sorted_anagrams, key=length_of_set, reverse=True)
  # Finally, by decreasing size
  sorted_anagrams = sorted(sorted_anagrams, key=size_of_set, reverse=True)
  
  return sorted_anagrams
  
def overlap_of_set(anagram_set):
  """ Returns the aggreate overlap score of the set.
  I defined this to be the sum of all the overlap scores of each
  combination of two words in the set. """
  score = 0
  for string1, string2 in itertools.combinations(anagram_set, 2):
    score += overlap_score(string1, string2)
  return score
  

def overlap_score(string1, string2):
  """Returns the overlap score, which is the number of adjacent bigrams
  that overlap between the two strings. """
  score = 0
  for i in range(len(string1) - 1):
    if string1[i:i+2] == string2[i:i+2]:
      score += 1
  return score

  
# ----- PART 6 ------
# My solution to part (6). The most interesting anagrams are the ones
# with the shortest shared substrings. For example, 'renavigate' and 'vegetarian'
# are a surprising set of anagrams, because they do not have a single substring in common.
def find_surprising_anagrams(wordfile):
  """Returns the 100 most surprising anagram sets"""
  sorted_set = sorted_sets_of_anagrams(wordfile)
  sorted_by_longest_substring = sorted(sorted_set, key=average_longest_substring)
  return sorted(sorted_by_longest_substring[:100], key=length_of_set, reverse=True)
  
def average_longest_substring(anagram_set):
  """Returns the average length of the longest substring anagram_set"""
  total_longest_substring = 0.0
  total_combos = 0
  for string1, string2 in itertools.combinations(anagram_set, 2):
    total_longest_substring += len_longest_shared_substring(string1, string2)
    total_combos += 1

  return total_longest_substring / total_combos

# NOTE: Algorithm and Code are from WikiBooks
def len_longest_shared_substring(S1, S2):
  """Returns the length of the longest shared subsequence"""
  M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
  longest, x_longest = 0, 0
  for x in xrange(1,1+len(S1)):
      for y in xrange(1,1+len(S2)):
          if S1[x-1] == S2[y-1]:
              M[x][y] = M[x-1][y-1] + 1
              if M[x][y]>longest:
                  longest = M[x][y]
                  x_longest  = x
          else:
              M[x][y] = 0
  return len(S1[x_longest-longest: x_longest])  
  
# ---- PART 6 (ALTERNATE SOLUTION) ----
# My first idea to find the most 'surprising' anagrams was to 
# analyze the total string edit distance of the set. However, this was
# not the best metric. For example, the two words 'occipitotemporal' and 
# 'temporooccipital' have a large string-edit distance becuase, but the anagram
# is not very surprising. Thus, I decided to use largest shared subsequence (see above)
def string_edit_dist_of_set(anagram_set):
  """Returns the toal string-edit distnace of the set"""
  total_dist = 0
  total_combos = 0
  for string1, string2 in itertools.combinations(anagram_set, 2):
    d = stringedit.string_edit_distance(string1, string2)[0]
    total_dist += d
    total_combos += 1
    
  # Divide by number of combos
  set_distance = total_dist / total_combos
  return set_distance

# --- HELPER METHODS ----

def length_of_set(anagram_set):
  """Returns the length of all the words in anagram_set"""
  return len(anagram_set[0])
  
def size_of_set(anagram_set):
  """Returns the number of words in anagram_set"""
  return len(anagram_set)

# ----- MAIN METHOD ------
if __name__ == "__main__":
  english_word_file = open("dict.txt", 'r')
  
  print "Do you want to see the solution to part (2), (5), or (6)?"
  i = raw_input("Enter 'i' to see the solution for part (i), where i={2,5,6}: ")
  if i == str(2):
    pprint.pprint(all_sets_of_anagrams(english_word_file))
  elif i == str(5):
    pprint.pprint(sorted_sets_of_anagrams(english_word_file))
  elif i == str(6):
    print "100 Most Surprising anagram sets:"
    pprint.pprint(find_surprising_anagrams(english_word_file))
  else:
    print "Invalid input. Enter '2', '5', or '6'."
  

  

  
  