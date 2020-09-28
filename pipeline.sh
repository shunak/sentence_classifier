# label sentence and outputs to __label__x.txt
python3 preprocess1.py claim.txt
python3 preprocess2.py prefer.txt

# unify labeled files
cat __label__1.txt __label__2.txt > model.txt

# make model file
python3 learning.py model.txt model



