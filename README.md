## install
```
git clone https://github.com/shunak/sentence_classifier.git
```
## how to use
```
cd sentence_classifier
```
### make model
put sentence file which you wanna classify.
ex. 2 patterns classify
case, user's claim opinion
touch claim.txt
echo "your company's product is nasty..." >> claim.txt
case, user's prefer opinion
touch prefer.txt
echo "your company's product is awesome!" >> prefer.txt
```
bash pipeline.sh
```
check if "model" file in the model directory

### predict
```
python3 prediction.py "sentence you wanna judge claim or prefer"
```
#### predict results
if the sentence is "claim"
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
批判 0.5000186

output results like underneath format
"label" "probability"

if you wanna modify output lable, edit prediction.py

