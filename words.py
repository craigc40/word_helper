# usr/bin/env python3

import argparse
import re
import string
import textwrap
import sys
from wordlist import w5list
import itertools


def contains_all(word, s):
    """Return True if 'word' contains all characters in 's'"""
    for c in s:
        if c not in word:
            return False
    return True


def contains_any(word, s):
    """Return True if 'word' contains any characters in 's'"""
    for c in s:
        if c in word:
            return True
    return False


def count_str(wlist):
    """Make English real good"""
    s = f"{len(wlist)} "
    s += "word matches" if len(wlist) == 1 else "words match"
    return s


class FiveLetterWordClass:
    def __init__(self, patterns=".....", yes="", no="", debug=False):
        self.patterns = patterns
        self.yes = yes
        self.no = no
        self.debug = debug
        self.wlist = w5list[:]
        self.initial_count = len(self.wlist)
        self.yes_letters = set()
        self.no_letters = set()

    def dprint(self, *args, **kwargs):
        if not self.debug:
            return
        print(*args, **kwargs)

    def do_patterns(self):
        # reduce 5-letter word list to those that match self.patterns
        self.dprint(f"Processing patterns='{self.patterns}' yes='{self.yes}' no='{self.no}'")
        self.dprint(f"    initial word count={self.initial_count}\n")
        for pattern in self.patterns.split(","):
            self.dprint(f"Processing pattern {pattern}")
            for i, c in enumerate(pattern):
                if c == ".":
                    continue
                self.yes_letters.add(c.lower())
                if c in string.ascii_lowercase:
                    # the lower case letters must exist, so keep only words
                    # that have them
                    self.dprint(f"    keeping words that contain '{c}'")
                    self.wlist = [w for w in self.wlist if c in w]
                    self.dprint(f"        count={len(self.wlist)}")
                    # make sure the remaining words don't have those
                    # characters in the invalid positions
                    nopat = "." * i + c + "." * (4 - i)
                    self.dprint(f"    excluding words that match '{nopat}'")
                    self.wlist = [w for w in self.wlist if not re.match(nopat, w)]
                    self.dprint(f"        count={len(self.wlist)}")
                else:
                    # keep words that have characters matching the
                    # uppercase letters
                    c = c.lower()
                    yespat = "." * i + c + "." * (4 - i)
                    self.dprint(f"    keeping words that match '{yespat}'")
                    self.wlist = [w for w in self.wlist if re.match(yespat, w)]
                    self.dprint(f"        count={len(self.wlist)}")
            self.dprint()

    def do_yes_letters(self):
        # reduce word list to those that contain all characters in the 'yes' list
        if len(self.yes):
            self.yes_letters |= set(self.yes.lower())
            self.wlist = [w for w in self.wlist if contains_all(w, self.yes)]
            self.dprint(f"{count_str(self.wlist)} everything in YES list '{self.yes}'")

    def do_no_letters(self):
        # reduce word list to those that exclude the 'no' list
        if len(self.no):
            self.no_letters = set(self.no.lower()) - self.yes_letters
            self.wlist = [w for w in self.wlist if not contains_any(w, self.no_letters)]
            self.dprint(f"{count_str(self.wlist)} nothing in NO list '{self.no_letters}'")

    def check_info(self):
        if ints := self.yes_letters.intersection(self.no_letters):
            print(f"Error: You have the following letters common between yes and no lists: {ints}")
            sys.exit(-1)

    def num_words_left(self):
        return len(self.wlist)

    def report_results(self):
        self.dprint(f"\n{count_str(self.wlist)} requirements:")
        wrapper = textwrap.TextWrapper(width=90)
        print(f"Possible answers matching patterns='{self.patterns}', yes='{self.yes}', no='{self.no}':")
        if len(self.wlist) <= 30:
            print("\n".join(wrapper.wrap(" ".join(self.wlist))))
            print()
        else:
            print("    (too many words to print)")

    def get_top_unspecified_letters(self, yes=True, no=True):
        """return dictionary of letters not yet guessed sorted by count"""
        if len(self.wlist) <= 1:
            return dict()
        letters = set()
        if yes:
            letters |= self.yes_letters
        if no:
            letters |= self.no_letters
        unspec_dict = {c: 0 for c in string.ascii_lowercase if c not in letters}
        for c in unspec_dict:
            for w in w5list:
                if c in w:
                    unspec_dict[c] += 1
        return "".join(reversed(sorted(unspec_dict, key=unspec_dict.get)))

    def report_unspecified_letter_counts(self):
        # show counts of characters that have not been specified in the patterns
        # or in the 'yes' list
        letters = self.get_top_unspecified_letters()
        if len(letters) == 0:
            return
        str = re.sub("(.)", r"\1 ", letters)
        print(f"Unused letters in order of importance:\n  {str}")

    def process(self):
        self.do_patterns()
        self.do_yes_letters()
        self.do_no_letters()
        self.check_info()


# get arguments
parser = argparse.ArgumentParser(
    description="Helper for figuring out what words to guess with Wordle.",
    epilog="For examples, refer to README.md",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    "patterns",
    nargs="?",
    default=".....",
    help=textwrap.dedent(
        """\
        Comma-separated list of patterns. Capital letter means correct in current position.
        Lower-case letter means correct but not in current position.
        """
    ),
)
parser.add_argument("--yes", "-y", default="", help="specify letters that must be included")
parser.add_argument(
    "--no",
    "-n",
    default="",
    help="specify letters that must not be included (yes/pattern letters will be subtracted from no letters)",
)
parser.add_argument("--quiet", "-q", action="store_true", default="", help="don't print stats")
args = parser.parse_args()

obj1 = FiveLetterWordClass(args.patterns, args.yes, args.no)
obj1.process()
obj1.report_results()


def show_best_words(letters, num):
    combo = set()
    words = set()
    for top_letter_index in range(num, len(letters) + 1):
        subset = letters[0:top_letter_index]
        # print(f"subset = {subset}")
        combo = set(itertools.combinations(subset, num)) - combo
        for d in combo:
            obj = FiveLetterWordClass(yes="".join(d))
            obj.process()
            words.update(obj.wlist)
            # print(f"Words for {obj.yes} = {obj.wlist}")
            if len(words) >= 10:
                print(
                    f"Best words to try based on {num} unspecified letters '{letters}':\n  {' '.join(words)}"
                )
                sys.exit(0)
    if len(words):
        print(f"Best words to try based on {num} unspecified letters '{letters}':\n  {' '.join(words)}")


d = obj1.get_top_unspecified_letters()
for i in range(5, 2, -1):
    show_best_words(d, i)
