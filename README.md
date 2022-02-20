# mentalist
Perform a classification task on mental issue via text

## Model:
* We built a NLP model for this classification task. We used a state-of-the-art pretrained model called `DistilBERT base uncased`, which is available on `huggingface`:
https://huggingface.co/distilbert-base-uncased

* Our rationale is based on the paper "DistilBERT, a distilled version of BERT: smaller, cheaper and lighter" of SANH et el. (2020):
https://arxiv.org/pdf/1910.01108.pdf

* We also attempted to use Logistic Regression for this task, based on the paper "Classification of mental illnesses on social media using RoBERTa" by Murarka et el. (2021):
https://aclanthology.org/2021.louhi-1.7.pdf

## Data:
Our training data `both_train.csv` is retrieved from Murarka et el. (2021) github repo:
* https://github.com/amurark/mental-health-classification
* https://drive.google.com/drive/folders/11aW_fpXjA-O51uv3xYY3xj6NWGh1VYh_

## Contributors:
* Viet Anh Duong: Project Architecturer, NLP model maker
* Thu Ha Nguyen: Project Leader, UI designer
* Long Khanh Tran: Techinical Lead, fullstack developer

## Set up
Requirements: Git, Python >= 3.7.11, npm, and node.

To replicate our results, the required dependencies are specified in the `requirements.txt` file.

(Optional) A virtual machine is highly recommended. Set up guidance:
* With conda:
```bash
conda create -n venv python=3.7
```
```bash
conda activate venv
```
```bash
pip3 install -r requirements.txt
```

## To run our app
* On terminal:
```bash
npm run dev
```
* Open another terminal:
```bash
cd mentalist
```
```bash
python3 manage.py runserver
```
A local development server is located at
```bash
http://localhost:8000/
```