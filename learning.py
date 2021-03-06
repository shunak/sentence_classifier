import sys
import fasttext as ft

argvs = sys.argv
input_file = argvs[1]
output_file = argvs[2]

classifier = ft.train_supervised(input_file)
classifier.save_model('{}/model'.format(output_file))
