# -*- coding: utf-8 -*-

import json
import yaml
from typing import List
import webbrowser

from models.problem_container import ProblemContainer
from models.problem import Problem

def import_from_json(file_path: str) -> ProblemContainer:
    with open(file_path, "r") as fr:
        json_obj = json.load(fr)
    
    problems = [Problem(**args) for args in json_obj]
    return ProblemContainer(problems)


def export_to_json(problem_container: ProblemContainer, file_path: str) -> None:
    dump_dicts = problem_container.get_dump_dicts()
    with open(file_path, "w") as fw:
        json.dump(dump_dicts, fw, indent=4)


def app_start(json_file_path: str, browser: object):
    cont = True
    problem_container = import_from_json(JSON_FILE)

    while cont:
        count = int(input("Number of tasks: "))
        problems = problem_container.select(count)
        for i, prob in enumerate(problems):
            print(f"Problems : {i + 1}/{len(problems)}")
            print(prob)
            browser.open(prob.url)
            
            solved = input("Solved? (y or n): ")
            if solved == 'y':
                prob.solve()
        
        problem_container.update(problems)
        cont_input = input("Continue? (y or n): ")
        if cont_input != 'y':
            cont = False
    
    export_to_json(problem_container, json_file_path)

        


if __name__ == "__main__":

    JSON_FILE = "./data/tasks.json"
    YAML_FILE = "./setting.yaml"

    with open(YAML_FILE, "r") as fr:
        data = yaml.safe_load(fr)
    BROWSER_PATH = data["BROWSER_PATH"]

    browser = webbrowser.get(BROWSER_PATH +' %s')

    try:
        app_start(JSON_FILE, browser)
    except Exception as ex:
        print(ex)

