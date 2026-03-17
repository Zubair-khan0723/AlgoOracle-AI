import pandas as pd
import plotly.express as px

def plot_feature_importance(model, feature_names):

    importance = model.feature_importances_

    df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    })

    df = df.sort_values("Importance", ascending=False)

    fig = px.bar(
        df,
        x="Feature",
        y="Importance",
        title="Feature Importance"
    )

    return fig