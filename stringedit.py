# String Edit Distance -- Andrew Beinstein
import sys

VOWELS = list("aeiou")
CONSONENTS = list("bcdfghjklmnpqrstvwxyz")
GAP_COST = 1.0
VOWEL_VOWEL = 1.2
CONS_CONS = 1.3
VOWEL_CONS = 5
IDEN = 0.0
GAP_CHAR = "-"

def string_edit_distance(string1, string2):
  m = len(string1)
  n = len(string2)
  
  # Let OPT(i, j) be the string-edit distance of the first i characters
  # in string 1, and the first j characters of stirng 2
  # We are trying to calculate OPT(m, n).
  opt = [[None for j in range(n+1)] for i in range(m+1)]
  
  
  # Initialize OPT(i,0) and OPT(0, j), because the only way
  # to match a word of length-i with an empty string is 
  # to use i gaps
  for i in range(m+1):
    opt[i][0] = GAP_COST*i
  for j in range(n+1):
    opt[0][j] = GAP_COST*j
    
  for i in xrange(1, m+1):
    for j in xrange(1, n+1):
      string1_char = string1[i-1]
      string2_char = string2[j-1]
      
      mismatch = cost_of_mismatch(string1_char, string2_char)
        
      mismatch_cost = mismatch + opt[i-1][j-1]
      gap1_cost = GAP_COST + opt[i-1][j]
      gap2_cost = GAP_COST + opt[i][j-1]
    
      opt[i][j] = min(mismatch_cost, gap1_cost, gap2_cost)    
      
  return (opt[m][n], opt)
  
  
# Backtrack through the optimum array, giving the actual alignment
# Returns a tuple of the two strings, with a gap character
# inserted in the appropriate places.
def backtrack(string1, string2, opt):
  
  string1_align = ""
  string2_align = ""
  i, j = len(opt)-2, len(opt[0])-2 # rows, columns
  
  while i >= 0 or j >= 0:
    gap1 = opt[i-1][j] + GAP_COST
    gap2 = opt[i][j-1] + GAP_COST
    mismatch = opt[i-1][j-1] + cost_of_mismatch(string1[i], string2[j])
    min_cost = min(gap1, gap2, mismatch)
    if mismatch == min_cost:
      string1_align = string1[i] + string1_align
      string2_align = string2[j] + string2_align
      i -= 1
      j -= 1
    elif gap1 == min_cost:
      string1_align = string1[i] + string1_align
      string2_align = GAP_CHAR + string2_align
      i -= 1
    elif gap2 == min_cost:
      string1_align = GAP_CHAR + string1_align
      string2_align = string2[j] + string2_align
      j -= 1

  return (string1_align, string2_align)

# This returns 0 if char1 and char2 are equal,
# or else, it assigns the appropriate value, which 
# depends on the characters being a vowel or not.
def cost_of_mismatch(char1, char2):
  if char1 == char2:
    return IDEN
  elif char1 in VOWELS and char2 in VOWELS:
    return VOWEL_VOWEL
  elif char1 in CONSONENTS and char2 in CONSONENTS:
    return CONS_CONS
  else:
    return VOWEL_CONS
  
# Prints distance and alignment to standard output
def print_output(string1, string2):
  distance, opt = string_edit_distance(string1, string2)
  print "String-edit distance between " + string1 + " and " + string2+ " is " + str(distance)
  string1_align, string2_align = backtrack(string1, string2, opt)
  print "Alignment ('-' represents a gap)"
  print string1_align
  print string2_align

# Main function
def run():
  # Instructor Demo
  if len(sys.argv) == 1:
    print_output("thenameofthegame", "theresmyname")
    print
    print_output("ninakushukuru", "unamshukuru")
  # User Arguments
  elif len(sys.argv) == 3:
    print_output(sys.argv[1], sys.argv[2])
  else:
    print "Invalid number of arguments."
    print "Enter two strings as arguments, or don't use an argument for a demo."
    
  