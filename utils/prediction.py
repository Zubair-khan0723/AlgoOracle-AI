import numpy as np

def predict_algorithm(model, encoder, feature_vector):

    X = np.array(feature_vector).reshape(1, -1)

    pred = model.predict(X)[0]

    probs = model.predict_proba(X)[0]

    confidence = max(probs)

    pred_name = encoder.inverse_transform([pred])[0]

    return pred_name, confidence, probs