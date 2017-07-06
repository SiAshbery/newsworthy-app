import numpy as np
from sklearn import metrics

# predicted = model.predict(test_data)
def predict_with_test_data(model,structured_test_data):
    return model.predict(structured_test_data)

def mean_accuracy(predicted, test_target):
    return np.mean(predicted == test_target)

def detailed_accuracy(predicted, test_target, categories):
    return metrics.classification_report(test_target, predicted, target_names=categories)
