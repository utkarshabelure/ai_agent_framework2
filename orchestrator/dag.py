from agents.planner import plan_task
from agents.executor import execute_task
from agents.reviewer import review_task

class Orchestrator:
    def __init__(self, mock_mode=True):
        self.mock_mode = mock_mode

    def run(self, task):
        plan = plan_task(task, self.mock_mode)
        execution = execute_task(task, plan, self.mock_mode)
        review = review_task(task, execution, self.mock_mode)

        return {
            "plan": plan,
            "execution": execution,
            "review": review
        }

