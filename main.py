from orchestrator.dag import Orchestrator

def run_task(user_input, mock_mode=True):
    orchestrator = Orchestrator(mock_mode=mock_mode)
    return orchestrator.run(user_input)
