# inter annotator agreement

Script developed for the "Linguistica Computazione II" class at the University of Pisa.

The input files must follow the structure of the examples files.

You need to have installed NLTK to make it work.

#### How to use
Find the annotation agreement for tags between two annotators, starting from two files:
```sh
python script.py tag file1.txt file2.txt 
```
Find the annotation agreement for dependencies between two annotators, starting from two files:
```sh
python script.py dep file1.txt file2.txt 
```
Returns the list of rows where the two annotators disagree:
```sh
python script.py tag file1.txt file2.txt -u
```
or:
```sh
python script.py dep file1.txt file2.txt -u
```
