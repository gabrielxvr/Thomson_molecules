import numpy as np
import matplotlib.pyplot as plt

def group_duplicates(input_list):
    # Dictionary to store values and their counts
    count_dict = {}

    # Iterate over the list to count the occurrence of each value
    for value in input_list:
        if value in count_dict:
            count_dict[value].append(value)
        else:
            count_dict[value] = [value]

    # Return a list of lists with the duplicated values
    return list(count_dict.values())


def plot_energy_levels(evals_var, dec, energ_unit='eV'):
    evals_round = np.around(evals_var, decimals=dec)
    evals_dp = group_duplicates(evals_round)
    print(evals_dp)
    fig = plt.figure(figsize=(5, 20))

    for energ in evals_dp:
        total_space = 0.6
        line_space = 0.5
        num_deg = len(energ)
        centers = np.linspace(-(num_deg-1)*total_space, (num_deg-1)*total_space, num_deg)
        for i in range(num_deg):
            # Create the plot
            plt.plot([centers[i] - line_space, centers[i] + line_space], [energ[i], energ[i]], color='black', linestyle='-', linewidth=2)
    
    # Add labels and title
    plt.ylabel(f'Energy ({energ_unit})')
    plt.title('Orbitals energy levels')
    
    # Remove x-axis labels
    plt.xticks([])
