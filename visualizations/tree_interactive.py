from sklearn import tree

def build_tree_structure(model, feature_names, class_names):

    tree_ = model.tree_

    def recurse(node):

        if tree_.feature[node] != -2:

            name = feature_names[tree_.feature[node]]

            return {
                "label": f"{name} <= {tree_.threshold[node]:.2f}",
                "value": node,
                "children": [
                    recurse(tree_.children_left[node]),
                    recurse(tree_.children_right[node])
                ]
            }

        else:

            values = tree_.value[node][0]
            predicted = class_names[values.argmax()]

            return {
                "label": f"Predict: {predicted}",
                "value": node
            }

    return [recurse(0)]