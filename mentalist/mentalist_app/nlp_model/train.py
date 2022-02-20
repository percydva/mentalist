import torch
import json
import numpy as np
import pandas as pd
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from transformers import DistilBertModel, DistilBertTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold, cross_val_score
import os

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')
path = os.path.abspath('mentalist_app/nlp_model')+'/both_train.csv'
print(path)
df_train = pd.read_csv(path)
df_train = df_train[:3000]

def tokenize(df_train, tokenizer):
    batch_ds = df_train[['title', 'class_name']]
    return batch_ds, batch_ds['title'].apply(lambda x: tokenizer.encode(x, add_special_tokens=True))

def len_max(tokenized):
    max_len = 0
    for value in tokenized.values:
        if len(value) > max_len:
            max_len = len(value)
    return max_len

def preprocessing(tokenized, max_len, model):
    padded = tf.keras.preprocessing.sequence.pad_sequences(tokenized.values, max_len+1, padding='post')
    attention_mask = np.where(padded!=0, 1, 0)
    input_ids = torch.tensor(padded)
    attention_mask = torch.tensor(attention_mask)
    with torch.no_grad():
        last_hidden_states = model(input_ids.long(), attention_mask=attention_mask)
    return last_hidden_states[0][:, 0, :].numpy()

def split_data(class_name, features):
    return train_test_split(features, class_name, test_size=0.20, stratify=class_name)

def model_with_regression(train_features, train_labels):
    lr_clf = LogisticRegression(multi_class='ovr', max_iter=1000)
    lr_clf.fit(train_features, train_labels)
    return lr_clf

def cross_validation(lr_clf, train_features, train_labels):
    kf = KFold(n_splits=10, random_state=42, shuffle=True)
    scores = cross_val_score(lr_clf, train_features, train_labels, cv=kf, scoring='roc_auc_ovo_weighted')
    return scores.mean()

def confusion_matrix(class_name, test_labels, test_features, lr_clf):
    lb = LabelEncoder()
    y = lb.fit_transform(class_name)
    cf = confusion_matrix(test_labels, lr_clf.predict(test_features))
    sns.heatmap(cf, annot=True, fmt='g', xticklabels=lb.classes_, yticklabels=lb.classes_)
    plt.savefig('confusion_matrix.png')

def save_model(lr_clf):
    model_param = {}
    model_param['classes'] = lr_clf.classes_.tolist()
    model_param['n_features_in'] = lr_clf.n_features_in_
    model_param['coef'] = lr_clf.coef_.tolist()
    model_param['intercept'] = lr_clf.intercept_.tolist()
    model_param['n_iter'] = lr_clf.n_iter_.tolist()
    json_txt = json.dumps(model_param, indent=4)
    with open('model.json', 'w') as file:
        file.write(json_txt)

def main():
    batch_ds, tokenized = tokenize(df_train, tokenizer)
    class_name = batch_ds['class_name']
    max_len = len_max(tokenized)
    features = preprocessing(tokenized, max_len, model)
    train_features, test_features, train_labels, test_labels = split_data(class_name, features)
    lr_clf = model_with_regression(train_features, train_labels)
    save_model(lr_clf)
    cross_validation_accuracy = cross_validation(lr_clf, train_features, train_labels)
    print("cross validation accuracy: ", cross_validation_accuracy)
    # confusion_matrix(class_name, test_labels, test_features, lr_clf) 

if __name__ == "__main__":
    main()