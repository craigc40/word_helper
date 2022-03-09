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

Let's say the word to guess is `GLOVE` and you guess `crate` first.
You'll get Wordle's response that the 'e' is correct. If you now want
to see what words remain, you would run this:

`python words.py ....E --no=crate`

First, note that you specified 'e' in the 'no' list. Words.py will remove that 'e' because there
is already an 'e' in the patterns. It would do the same thing if there were an 'e' in the 'yes'
list. This allows you to type your Wordle guesses in full in the 'no' list of letters without
having to cull the correct letters.

In our example, there are over 300 possible words that fit the arguments you passed in, so you get the message that there are too
many words to print. But you also get suggestions for the next word that are based on the
letters you have no guessed yet. These letters are _silnudymphbgkwfvzjxq_ and are listed in order
of how commonly they appear in the word list.

Your suggestions are:
`lysin lindy sylid nidus idyls unsly unlid indyl linds dinus`

While these are indeed words in our giant 14K word list, most of them probably won't be
accepted by Wordle, Quardle, or other similar games. So let's pick one that will work: `idyls`

Wordle now tells you that there is an 'l', just not in position 4, so you run again:

`python words.py ....E,...l. --no=createidyls`

or you could have combined the patterns:

`python words.py ...lE --no=createidyls`

There are still too many valid words to guess. So let's try another guess from the
list of suggestions: `gumbo`. Now we have a 'G' in the right place and an 'o' in
the wrong place.

`python words.py G..lE,....o --no=createidylsgumbo`

Finally, we get a word list that we can work with:
`glove gloze golee goloe golpe`

The only _normal_ word is `glove`, so we guess it, and bam! Solved it in 4 guesses!

