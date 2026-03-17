import numpy as np


def select_next_question(model, feature_names, asked_features):

    importances = model.feature_importances_

    remaining = []

    for i, f in enumerate(feature_names):
        if f not in asked_features:
            remaining.append((f, importances[i]))

    remaining.sort(key=lambda x: x[1], reverse=True)

    if len(remaining) == 0:
        return None

    return remaining[0][0]