from app.services.markov_model import MarkovChain


def run_simulation(matrix, steps):
    mc = MarkovChain(matrix)
    transient = mc.transient_states(steps)
    steady = mc.steady_state()
    return {"transient": transient.tolist(), "steady": steady.tolist()}
