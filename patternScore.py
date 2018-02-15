

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
        return_list = list()
        for i in self:
            if i.score == score:
                return_list.append(i)
        return return_list

    def pattern_exists(self, pattern):
        for i in self:
            if i.pattern == pattern:
                return True
        return False

    def add(self, Scored_Pattern):
        if not self.pattern_exists(Scored_Pattern.pattern):
            super(Score_Legend, self).add(Scored_Pattern)

class document():
    def __init__(self, text, legend):
        self.text = text
        self.legend = legend
        self.score_total = 0

    def score(self):
        total = 0
        for scored_pattern in self.legend:
            matches = re.findall(scored_pattern.re_obj, self.text)
            for match in matches:
                total = total + scored_pattern.score
        return total
