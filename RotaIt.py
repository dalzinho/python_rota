from collections import namedtuple
from datetime import date

skills = {'Cleaning': {'Gordon', 'Erfan', 'Roger', 'Yuri'},
          'Cooking': {'Erfan', 'Yuri'},
          'Driving': {'Gordon', 'Erfan', 'Roger'},
          'Shopping': {'Gordon', 'Erfan', 'Roger', 'Yuri'}}

jobs_assigned = {'Gordon': 0,
                 'Erfan': 0,
                 'Roger': 2,
                 'Yuri': 0}

dates = {date(2017,10,25): {'Gordon', 'Erfan', 'Roger', 'Yuri'},
         date(2017,10,26): {'Erfan', 'Yuri'},
         date(2017,10,27): {'Gordon', 'Erfan', 'Roger'},
         date(2017,10,28): {'Gordon','Yuri'}}

monday_jobs = [None, None, 'driving', 'shopping']

Job = namedtuple('Job', ['date', 'task'] )

jobs = [Job(date(2017,10,25), 'Driving'), Job(date(2017,10,26), 'Shopping')]

class Availability:
    def __init__(self, skills, vacations):
        self.skills = skills
        self.vacations = vacations

    def who_can(self, job):
        return self.skills.get(job.task, set()) & self.vacations.get(job.date, set())

    def assign_jobs(self, job_list, assignation_count):
        assignations = [(job, list(self.who_can(job))[0]) for job in job_list]
        
availability = Availability(skills, dates)

print(availability.assign_jobs(jobs))

