
#TODO variable names, class names, and class attribute names are all pretty bad
import re

class Scored_Pattern():
    """A pattern with a score attatched to it"""
    def __init__(self, score, pattern):
        self.score = score
        self.pattern = pattern
        self.re_obj = re.compile(pattern)

class Score_Legend(set):
    """List of Scored_Pattern objects"""
    def find_patterns_by_score(self, score):
        """Returns a list of all of the Scored_Pattern objects
        that have a score attribute that matches the provided number"""
        return_list = list()
        for i in self:
            if i.score == score:
                return_list.append(i)
        return return_list

    def pattern_exists(self, pattern):
        """Check if there is a pattern in this instance that matches the
        provided string"""
        for i in self:
            if i.pattern == pattern:
                return True
        return False

    def add(self, Scored_Pattern):
        """Works just like add for the 'set' class, but doesn't allow multiple
        of the same pattern"""
        if not self.pattern_exists(Scored_Pattern.pattern):
            super(Score_Legend, self).add(Scored_Pattern)

class Document():
    """This class just contains some text, a Score_Legend to score it by,
    and and optional title and author"""
    def __init__(self, legend, text, author=None, title=None):
        self.text = text
        self.author = author
        self.title = title
        self.legend = legend
        self.score_total = self._score()

    def _score(self):
        """Scores the provided document based on the number of matches with the
        patterns in the legend's regex"""
        total = 0
        match_total = 0
        for scored_pattern in self.legend:
            matches = re.findall(scored_pattern.re_obj, self.text)
            for match in matches:
                total = total + int(scored_pattern.score)
                match_total = match_total + 1
        if not (total == 0 or match_total == 0):
            self.score_total = total /match_total
        else:
            self.score_total = 0.0
