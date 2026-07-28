from simulation import Simulation


def main():

    simulation = Simulation(steps=500)

    simulation.run()

    simulation.print_summary()

    simulation.plot_results()


if __name__ == "__main__":
    main()