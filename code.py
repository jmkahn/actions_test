def main(x_lbls):
    """helper function.
    returns rows in which each x_lbl occurs, as a list of np arrays"""
    x_lbl_indices = []
    # for each x class that exists,
    for x_lbl in np.unique(x_lbls):
        # add an array of the indices where that label occurs to the list
        currentIndices = np.where(x_lbls == x_lbl)[0]
        x_lbl_indices.append(currentIndices)
    return x_lbl_indices
