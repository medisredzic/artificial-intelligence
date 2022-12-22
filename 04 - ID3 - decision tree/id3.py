import numpy as np


class ID3():
    def __init__(self):
        self.root = None

    def fit(self, X, y):
        self.root = DecisionTreeNode().split(X, y)
        return self

    def __str__(self):
        return str(self.root)


def entropy(labels):
    """returns the same as scipy.stats.entropy([positive, negative], base=2)"""
    n = len(labels)
    if n == 0:
        return 0.0
    positive = sum(labels) / n
    negative = 1 - positive
    if positive == 0 or negative == 0:
        return 0.0
    return -positive * np.log2(positive) - negative * np.log2(negative)


class DecisionTreeNode():
    def __init__(self):
        self.label = None
        self.split_point = None
        self.split_feature = None
        self.left_child = None
        self.right_child = None

    def get_all_possible_split_points(self, features, labels):
        nr_samples, nr_features = features.shape
        split_points = []  # this should be a list of tuples (f_idx, split_at) where split_at is the value to split feature f_idx
        # add tuples using: split_points.append((f_idx, split_at))

        for f_idx in range(nr_features):
            # sort by feature feat
            idx_sort = features[:, f_idx].argsort()
            features = features[idx_sort, :]
            labels = labels[idx_sort]

            for k in range(len(features) - 1):
                if labels[k] != labels[k + 1]:
                    split_at = np.mean(features[k:k + 2, f_idx])
                    split_points.append((f_idx, split_at))

            # TODO: check for consecutive samples whether the labels and features are different
            # be careful to not compare the 0th sample with the last sample when indexing
            # if labels and feature values are different, compute splitting values and add to list as shown above

        return split_points

    def get_optimal_split_point(self, features, labels):
        split_feature, split_point = None, None
        possible_split_points = self.get_all_possible_split_points(features, labels)
        # print(possible_split_points)
        current_best_ig = -np.Inf

        # loop over all possible splitting points that you computed and return the best one
        for (f_idx, split_at) in possible_split_points:
            # TODO: compute information gain for splitting points and store the best one
            calc_ig = self.get_information_gain(features[:, f_idx], labels, split_at)
            if calc_ig > current_best_ig:
                current_best_ig = calc_ig
                split_feature = f_idx
                split_point = split_at
        # print(split_feature, split_point)
        return split_feature, split_point

    def get_information_gain(self, x, y, split_point):
        ig = 0.0
        # TODO: implement the information gain as described in the slides
        # use the provided entropy() function
        # use <= and > for comparison (to get a comparable result)

        ig = entropy(y)

        tmp_left = []
        tmp_right = []

        for k in range(len(x)):
            if x[k] <= split_point:
                tmp_left.append(y[k])
            elif x[k] > split_point:
                tmp_right.append(y[k])

        tmp_left = len(tmp_left) / len(y) * entropy(tmp_left)
        tmp_right = len(tmp_right) / len(y) * entropy(tmp_right)
        ig = ig - tmp_left - tmp_right

        return ig

    def split(self, X, y):
        # TODO: implement the ID3 algorithm
        # if you reach a node that only contains samples with the same label store the label
        # otherwise compute the optimal split point using get_optimal_split_point
        # and create the child nodes (store them in self.left_child and self.right_child)
        # call split(X_left, y_left) and split(X_right, y_right) to recursively create the tree
        # again: use <= and > for comparison
        if np.all(y == y[0]):
            self.label = y[0]
        else:
            self.split_feature, self.split_point = self.get_optimal_split_point(X, y)
            # print(self.split_feature)
            X_left = X[X[:, self.split_feature] <= self.split_point]
            X_right = X[X[:, self.split_feature] > self.split_point]
            y_left = y[X[:, self.split_feature] <= self.split_point]
            y_right = y[X[:, self.split_feature] > self.split_point]

            self.right_child = DecisionTreeNode()
            self.right_child.split(X_right, y_right)
            self.left_child = DecisionTreeNode()
            self.left_child.split(X_left, y_left)

        return self

    def __str__(self):
        if self.label is not None: return "(" + str(self.label) + ")"

        str_value = str(self.split_feature) + ":" + str(self.split_point) + "|"
        str_value = str_value + str(self.left_child) + str(self.right_child)
        return str_value
