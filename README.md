# Estrogen receptor (ER) status prediction  from the MRI image features


## Dataset
The breast MRI dataset contains 922 patients gathered in Duke Hospital from 1 January, 2000 to 23 March, 2014 with invasive breast cancer and available pre-operative MRI at [Duke Hospital](https://sites.duke.edu/mazurowski/resources/breast-cancer-mri-dataset/)

It consists of :

1. Demographic, clinical, pathology, treatment, outcomes, and genomic data
2. Pre-operative dynamic contrast enhanced (DCE)-MRI
3. Locations of lesions in DCE-MRI:
4. Imaging features from DCE-MRI

## Task

Classify the patients Estrogen receptor (ER) status (binary)

## Steps

(The following instructions apply to Posix/bash. Windows users should check
[here](https://docs.python.org/3/library/venv.html).)

First, clone this repository and open a terminal inside the root folder.

Create and activate a new virtual environment (recommended) by running
the following:

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```
 [Run the notebook](../main/subtumor_CLASSIFICATION.ipynb)


## Resources

- To learn more about this task, check out [presentation](../main/docs/presentation.pptx)
