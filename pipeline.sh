# label sentence and outputs to __label__x.txt
# set text file name which you wanna labeling xxx.txt
# if you classify sentence as claim or prefer for example, set claim.txt , prefer.txt like underneath
python3 preprocess1.py claim.txt
python3 preprocess2.py prefer.txt

# unify labeled files
cat __label__1.txt __label__2.txt > model.txt

# make model file
python3 learning.py model.txt model



