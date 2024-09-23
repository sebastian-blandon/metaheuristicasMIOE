import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def plot_bin_packing_bl(bin_capacity, packed_bin):
    """
    Plots the bin packing results for a single bin.

    Args:
        items: A list of tuples representing items (width, height).
        bin_capacity: The capacity (area) of the bin (tuple of width, height).
        packed_bin: A tuple representing the packed bin,
                    as returned by the bin_pack_bl function.
    """

    usable_empty_space_Area,occupied_area, item_placements = packed_bin
    bin_width, bin_height = bin_capacity

    # Create a figure and subplot
    fig, ax = plt.subplots()

    # Set plot dimensions and labels
    ax.set_aspect('equal')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_xlim(0, bin_width)
    ax.set_ylim(0, bin_height)

    # Plot the bin boundary
    ax.plot([0, bin_width, bin_width, 0, 0], [0, 0, bin_height, bin_height, 0], color='black')

    # Generate random colors for each item
    colors = [(random.random(), random.random(), random.random()) for _ in item_placements]

    # Plot the items
    for i, placement in enumerate(item_placements):
        x, y, item_width, item_height = placement
        rectangle = patches.Rectangle((x, y), item_width, item_height, fill=True, facecolor=colors[i])
        ax.add_patch(rectangle)
        
        # Add text label indicating index
        ax.text(x + item_width / 2, y + item_height / 2, str(i), color='black', ha='center', va='center', fontsize=8)

    # Add title and show the plot
    plt.title(f"Bin: Occupied Area = {occupied_area}, usable empty space = {usable_empty_space_Area}")
    plt.show()

