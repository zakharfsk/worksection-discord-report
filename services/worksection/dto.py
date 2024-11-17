import dataclasses


@dataclasses.dataclass
class Report:
    """
    DTO class for Worksection report

    Attributes:
        - total_time: str - total time spent on tasks
        - projects: list['Project'] - list of projects with tasks
    """
    date: str
    total_time: str
    projects: list['Project']


@dataclasses.dataclass
class Project:
    """
    DTO class for Worksection project

    Attributes:
        - name: str - project name
        - tasks: list['Task'] - list of tasks in project
    """
    name: str
    tasks: list['Task']


@dataclasses.dataclass
class Task:
    """
    DTO class for Worksection task

    Attributes:
        - name: str - task name
        - time: str - time spent on task
    """
    name: str
    time: str
