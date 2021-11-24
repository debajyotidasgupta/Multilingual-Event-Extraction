# Multilingual-Event-Extraction

NLP Term Project

## Folder structure

```
.
|- scripts: All parsing scripts
|- models: scripts for training and testing 
|          on the BERT model
|- data
|  |- raw: Zip files
|  |- unzipped: Unzipped data files
|  |- processed: Final Datasets
```

## Important files
joint_ee_bert_train_18_10.py - Script for training the neural network model \
joint_ee_bert_test_18_10.py - Script for testing the trained model

## Description of scripts

- `parser.py`: Parses a given directory of XML files into sentence, tuple and pointer files.
- `cleanup.py`: Deletes sentences with 0 events and 0 arguments.
- `event_arg_gen.sh`: Generates the text files with distinct events and argument names.
- `get_sent_len.py`: Sentence length statistics
- `phrase_len.py`: Trigger phrase length statistics
- `f1_plot.py`: Plots the epoch vs f1 score given the training log file.
- `gen_stat.py`: Generates overall trigger phrase stats.

## Hyperparameters

> maximum length of trigger phrase

BENGALI - 28 \
HINDI - 68

> maximum length of entity phrase

BENGALI - 7  \
HINDI - 22 

> maximum sentence length

BENGALI 106 \
HINDI 199

## Results

```Glossary```\
P = precision\
R = recall\
F1 = F1 score

trigger span identification(TI)\
trigger type classification(tc)\
argument span identification (ai)\
argument type classification(ro)

### HINDI

Prediction time:  0:00:19.604934\
no of correctly identified triggers= 919\
no of correctly classified triggers= 407\
no of correctly identified arguments= 267\
no of correctly identified roles= 267

```Precision```\
P_tuple:  0.061\
P_ti:  0.421\
P_tc:  0.187\
P_ai:  0.122\
P_ro:  0.122

```Recall```\
R_tuple:  0.036\
R_ti:  0.244\
R_tc:  0.108\
R_ai:  0.071\
R_ro:  0.071

```F1```\
F1:  0.045\
TI F1:  0.309\
TC F1:  0.137\
AI F1:  0.09\
RO F1:  0.09

### BENGALI

Prediction time:  0:00:08.623305\
no of correctly identified triggers= 604\
no of correctly classified triggers= 380\
no of correctly identified arguments= 262\
no of correctly identified roles= 262

```Precision```\
P_tuple:  0.067\
P_ti:  0.342\
P_tc:  0.215\
P_ai:  0.148\
P_ro:  0.148

```Recall```\
R_tuple:  0.031\
R_ti:  0.158\
R_tc:  0.1\
R_ai:  0.069\
R_ro:  0.069

```F1```\
F1:  0.043\
TI F1:  0.216\
TC F1:  0.136\
AI F1:  0.094\
RO F1:  0.094
