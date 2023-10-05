import numpy as np
from scipy.stats import mode

def linear_decision_boundary_classifier(decision_boundary_line_vec, target_features, class_names=None):
    """
    decision_boundary_line_vec: Vector representation of a linear decision boundary.  Convert the line to the form Ax + By + ... + C = 0.  Then turn the coefficients into a vector.  So, for example, 5x - y + 2 = 0 will turn into <5, -1, 2>.
    
    target_features: points to predict labels for as a 2D numpy array.  There should be one less column than the number of entries in the decision boundary vector.
    """
    
    # add column of 1s to match dimension of decision_boundary_line_vec
    # this constant is for the intercept
    features_with_intercept = np.hstack([target_features, np.ones((len(target_features), 1))])
    
    # calculate dot product. sign of the dot product tells us which "side" of the
    # line on which the points are located
    dot_products = np.dot(features_with_intercept, decision_boundary_line_vec)

    # predict labels based on which side of the line the points are located on
    # use -1's so that it's easier to debug
    # nothing should be -1 when done
    predicted_labels = -1 * np.ones(len(target_features), int)

    neg_mask = dot_products <= 0.0
    predicted_labels[neg_mask] = 0.0
    pos_mask = dot_products > 0.0
    predicted_labels[pos_mask] = 1.0

    if class_names:
        predicted_labels = np.array([class_names[c] for c in predicted_labels])
    
    return predicted_labels