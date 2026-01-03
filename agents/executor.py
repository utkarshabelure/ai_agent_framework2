def execute_task(task, plan, mock_mode=True):
    if mock_mode:
        return {
            "final_answer": (
                "AI agents are autonomous systems that observe their environment, "
                "reason about tasks, and take actions to achieve goals.\n\n"
                "They include:\n"
                "• Planner – decides steps\n"
                "• Executor – performs actions\n"
                "• Reviewer – validates results\n\n"
                "Used in chatbots, automation, robotics, and assistants."
            )
        }

