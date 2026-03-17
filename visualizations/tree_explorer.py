from dtreeviz import model as dtreeviz_model

def visualize_tree(model, X, y, feature_names, class_names):

    viz = dtreeviz_model(
        model,
        X,
        y,
        feature_names=feature_names,
        target_name="algorithm",
        class_names=class_names
    )

    return viz