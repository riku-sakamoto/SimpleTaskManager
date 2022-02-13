from typing import List, Dict
import json

from models.problem import Problem


class ProblemContainer():
    def __init__(self, problems: List[Problem]) -> None:
        self.problems_dict = { prob.url: prob for prob in problems}

    def select(self, num: int) -> List[Problem]:
        # priority順にソート
        problems = self.problems_dict.values()
        sorted_problems = sorted(problems, key=lambda x: -1 * x.priority)
        return sorted_problems[:num]
    
    def update(self, problems: List[Problem]) -> None:
        for prob in problems:
            self.problems_dict[prob.url] = prob

    def get_dump_dicts(self) -> List[Dict]:
        problems = [vars(prob) for prob in self.problems_dict.values()]
        return problems
