# word_helper
Python script that helps you choose words for Wordle and other similar word games

## Examples

`python words.py .Ei.. --no=cdu`

Look for words where 'E' is in position 2, 'i' is somewhere but not 
in position 3, and letters 'c', 'd', 'u' do not exist

`python words.py LEyfa --no=x`

Look for words that begin with 'LE', have 'yfa' in some order
but not in the positions shown, and do not contain 'x' anywhere
    
`python words.py .R..n,..I..,....r`

Uses three patterns to describe the following:
* Word contains 'RI' in positions 2 and 3.
* Word has an 'r' and an 'n', but neither is in position 5 (Note that this does not mean there is a second 'r'. There might be, but the "no 'r' in position 5" pattern could be entirely redundant with the 'R' in position 2.)
This could have been compressed to two patterns:
`.RI..n,....r`

## Scenario

Let's say the word to guess is GLOVE and you guess 'crate' first.
You'll get Wordle's response that the 'e' is correct. If you now want
to see what words remain, you would run this:

`python words.py ....E --no=crat`

You'll get over 300 possible words. But you also find out that the top letters used in
those 300+ words are:
* o:143
* i:141
* l:121
* s:116
* n:92

So your next guess should use as many of those letters as possible. How do you find a good word?

`python words.py --yes=oils`

This says to tell you all 5 letter words that contain all of 'o', 'i', 'l', 's' in any order.
From that list, you pick "solid".

Now Wordle tells you that the 'l' and 'o' are used but in the wrong place. So you run again:

`python words.py ....E,.ol.. --no=cratsid`

or you could have combined the patterns:

`python words.py .ol.E --no=cratsid`

Either way, you're asking for words that end in 'E' and have 'o' and 'l' somewhere in them not at the positions
shown. Now you're down to 10 words. Keep going until you solve it!

