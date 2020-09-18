# mecab 大文字小文字に注意
import MeCab
# datetime
import time
# 引数取得
import sys
from sys import argv

#引数の取得
input_file_name = sys.argv[1]

# 解析対象テキストファイルのインポート
with open(input_file_name,'r') as f:
    mecab = MeCab.Tagger("-Owakati")
    text = mecab.parse('解析文字列はこちらです。')
    mecab.parse('')

#ファイル実行開始時刻を取得
timestr = time.strftime('%Y%m%d-%H%M%S')

#出力ファイル名
out_file_name = "ochasen_" + timestr +  ".txt"
with open(out_file_name, 'w') as f:
    f.write(text)
