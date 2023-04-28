import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def monte_carlo(
    min_drive_time: int,
    num_lights: int,
    wait_time: int,
    mean: float,
    std: float,
    num_iterations: int,
    X: float
):

    time_to_office = []
    num_success = 0
    prob = []
    for i in range(1, num_iterations + 1):
        wait_penalty = 0
        for _ in range(num_lights):
            wait_penalty += wait_time * np.random.randint(0, 2)

        walk_time = random.gauss(mean, std)

        time_to_office.append(min_drive_time + wait_penalty + walk_time)

        if time_to_office[-1] <= X:
            num_success += 1

        prob.append((num_success / i)*100)
        print("Probability of X: %.2f" % prob[-1], end="\r")

    fig, ax = plt.subplots()
    x = np.arange(num_iterations)
    line, = ax.plot(np.arange(num_iterations), prob)

    def animate(num, x, y, line):
        line.set_data(x[:num], y[:num])
        line.axes.axis([0, num_iterations, 0, 100])
        return line,

    ani = anim.FuncAnimation(fig, animate, len(x), fargs=[
                             x, prob, line], interval=25, blit=True)

    ax.set_xlabel("Number of iterations")
    ax.set_ylabel(f"Probability of X <= {X} minutes")

    ani.save("prob.gif")
    plt.show()

    return


def stats_analysis():

    x = np.array([6, 10])
    print(x.std())

    monte_carlo(
        15.0,
        4,
        1,
        8.0,
        2.0,
        1000,
        23
    )

    return


if __name__ == "__main__":

    stats_analysis()
