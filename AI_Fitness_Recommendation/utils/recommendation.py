def get_recommendation(user_data, model):
    pred = model.predict(user_data)
    recommendations = {
        'Workout Plan': pred[0]['workout'],
        'Diet Plan': pred[0]['diet'],
        'Tips': pred[0]['tips']
    }
    return recommendations