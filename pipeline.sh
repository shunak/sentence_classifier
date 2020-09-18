python3 preprocess1.py claim.txt
python3 preprocess2.py prefer.txt
cat __label__1.txt __label__2.txt > model.txt
python3 learning.py model.txt model



