import string
from random import choice, random, seed
import random
from typing import List

import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx

def gen_id(len: int) -> string:
    letters = string.ascii_letters
    return "".join(choice(letters) for _ in range(len))


def markov_chain(
    tran_matrix: pd.DataFrame,
    num_scooters: int,
    num_days: int,
    num_iterations: int
):
    a = np.array([100])
    b = np.array([100])
    c = np.array([100])
    for n in range(num_iterations):
        # create a state dict. for keeping track of the num of scooters
        # at each center
        state = {k: [gen_id(10) for _ in range(num_scooters)]
                 for k in tran_matrix.keys()}
        # keep track of each individual scooters state over time
        scooters_state = {
            k: [start] for start, scooters_state in state.items() for k in scooters_state}
        names = list(state.keys())

        for _ in range(num_days):
            for scooter, history in scooters_state.items():
                curr_center = history[-1]
                # randomly select new center Y from the probability distibution
                # given that scooter is currently as center X
                transition = np.random.choice(
                    names, replace=True, p=tran_matrix.T[curr_center])

                # add new state for scooter
                scooters_state[scooter].append(transition)

                # scooter has changed center
                if transition != curr_center:
                    # remove scooter from center
                    state[curr_center].remove(scooter)
                    # append scooter to new center
                    state[transition].append(scooter)

        a = np.append(a, len(state["A"]))
        b = np.append(b, len(state["B"]))
        c = np.append(c, len(state["C"]))
        print(
            f"Average number of scooters at each center after {n} iters: A = {a.mean()}, B = {b.mean()}, C = {c.mean()}", end="\r")

    return scooters_state


# class AnimatedScatter(object):
#     ab_x_line = np.linspace(1, 4, 50)
#     ab_y_line = np.linspace(2, 7, 50)

#     ba_x_line = np.linspace(4, 1, 50)
#     ba_y_line = np.linspace(7, 2, 50)

#     ac_x_line = np.linspace(1, 7, 50)
#     ac_y_line = np.linspace(2, 2, 50)

#     ca_x_line = np.linspace(7, 1, 50)
#     ca_y_line = np.linspace(2, 2, 50)

#     bc_x_line = np.linspace(4, 7, 50)
#     bc_y_line = np.linspace(7, 2, 50)

#     cb_x_line = np.linspace(7, 4, 50)
#     cb_y_line = np.linspace(2, 7, 50)

#     """An animated scatter plot using matplotlib.animations.FuncAnimation."""
#     def __init__(self, data=dict, numpoints=50):
#         self.numpoints = numpoints
#         self.stream = self.data_stream(data)

#         # Setup the figure and axes...
#         self.fig, self.ax = plt.subplots()

#         # initial points for centers A, B, C
#         x = [1, 4, 7]
#         y = [2, 7, 2]
#         category = ["Center", "Center", "Center"]

#         self.df = pd.DataFrame({
#             "x": x,
#             "y": y,
#             "category": category,
#             "s": [50.0, 50.0, 50.0]
#         })

#         self.scat = None
#         # Then setup FuncAnimation.
#         self.ani = anim.FuncAnimation(self.fig, self.update, interval=5,
#                                           init_func=self.setup_plot, blit=True)

#     def setup_plot(self):
#         """Initial drawing of the scatter plot."""

#         self.ax.axis([0, 8, 0, 8])
#         self.ax.set_axis_off()

#         # initial points for centers A, B, C
#         x = [1, 4, 7]
#         y = [2, 7, 2]

#         # generate scooter data points around each of the three centers
#         centers = ["A", "B", "C"]
#         for idx, (i, j) in enumerate(zip(x.copy(), y.copy())):
#             plt.text(i, j, centers[idx], va="bottom", ha="center", fontdict={'size': 20})
#             for _ in range(self.numpoints):
#                 new_x = i + random.uniform(-.15, .15)
#                 new_y = j + random.uniform(-.15, .15)
#                 self.df.loc[len(self.df)] = [new_x, new_y, "Scooter", 10.0]

#         groups = self.df.groupby("category")
#         for name, group in groups:
#             self.scat = self.ax.scatter(group.x, group.y, s=group.s, label=name)

#         # For FuncAnimation's sake, we need to return the artist we'll be using
#         # Note that it expects a sequence of artists, thus the trailing comma.
#         return self.scat,

#     def data_stream(self, data: dict):

#         for scooter in data.keys():


#         while True:
#             x += 1
#             yield x

#     def update(self, i):
#         """Update the scatter plot."""
#         data = next(self.stream)
#         print(data)

#         return self.scat,


def simulation_sim(states: List[str], tran_matrix: pd.DataFrame) -> None:

    graph = nx.MultiDiGraph()
    [graph.add_node(s, style='filled', fillcolor='white',
                    shape='circle', fixedsize='true', width=0.5) for s in states]

    labels = {}
    edge_labels = {}

    for origin_state in states:
        for destination_state in states:
            rate = float(tran_matrix.T[origin_state].loc[[destination_state]])
            if rate > 0:
                graph.add_edge(origin_state, destination_state,
                               weight=rate, label="{:.02f}".format(rate), len=2)
                edge_labels[(origin_state, destination_state)
                            ] = "{:.02f}".format(rate)

    A = to_agraph(graph)
    A.layout()
    plt.show()

    return


def stats_analysis():

    tran_matrix = pd.DataFrame(
        np.array([
            [.2, .3, .5],
            [.7, .1, .2],
            [.1, .3, .6]
        ]),
        columns=["A", "B", "C"],
        index=["A", "B", "C"]
    )

    print(tran_matrix)

    # markov_chain(tran_matrix, 100, 5, 1)

    #simulation_sim(["A", "B", "C"], tran_matrix)

    return


if __name__ == "__main__":
    stats_analysis()
