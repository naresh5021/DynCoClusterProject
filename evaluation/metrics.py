from sklearn.metrics import precision_score, recall_score, f1_score

def compute_metrics(true_labels, pred_labels):
    precision = precision_score(true_labels, pred_labels, average='macro')
    recall = recall_score(true_labels, pred_labels, average='macro')
    f1 = f1_score(true_labels, pred_labels, average='macro')
    return precision, recall, f1