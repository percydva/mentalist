# mentalist
Perform a classification task on mental issue via text

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