import numpy as np


class MarkovChain:
    def __init__(self, transition_matrix):
        self.transition_matrix = np.array(transition_matrix)
        self.num_states = self.transition_matrix.shape[0]

    def steady_state(self):
        """
        Calculate the steady-state probabilities.
        """
        P = self.transition_matrix.T
        n = P.shape[0]
        A = np.vstack([P - np.eye(n), np.ones(n)])
        b = np.append(np.zeros(n), 1)
        steady_state = np.linalg.lstsq(A, b, rcond=None)[0]
        return steady_state

    def transient_states(self, steps):
        """
        Simulate transient state probabilities.
        """
        return np.linalg.matrix_power(self.transition_matrix, steps)
