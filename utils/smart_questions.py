import numpy as np

def get_top_features(model, feature_names, k=5):
    """
    Select top-k most important features from the decision tree.
    This allows the AI to ask only the most useful questions.
    """

    importances = model.feature_importances_

    indices = np.argsort(importances)[::-1][:k]

    return [feature_names[i] for i in indices]