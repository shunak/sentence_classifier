import re
import json
import MeCab
import sys

argvs = sys.argv #get value from argument
input_file = sys.argv[1] #set 1st argument as a value
f = open(input_file, 'r', encoding='utf-8') #open file and read it

CLASS_LABEL = "__label__1"

def get_surfaces():
    """
    文書を分かち書きし単語単位に分割
    """
    results=[]
    for line in open(argvs[1],'r'):
        tagger = MeCab.Tagger('-Owakati')
        words = tagger.parse(line)
        word = words.rstrip('\n')
        results.append(word)
        # print(word)
    return results

def write_txt(contents):
    """
    評価モデル用のテキストファイルを作成する
    """
    try:
        if(len(contents) > 0):
            fileNema = CLASS_LABEL + ".txt"
            labelText = CLASS_LABEL + ", "

            f = open(fileNema, 'a')
            for row in contents:
                # 空行区切りの文字列に変換
                spaceTokens = "".join(row);
                result = labelText + spaceTokens + "\n"
                # 書き込み
                f.write(result)
            f.close()

        print(str(len(contents))+"行を書き込み")

    except Exception as e:
        print("テキストへの書き込みに失敗")
        print(e)

def main():
    surfaces = get_surfaces()
    print(surfaces)
    write_txt(surfaces)               #入力テキストを書き込み

# def text_reader(cnt):
#     row_no=0
#     while True:
#         line = cnt.readline()
#         if line:
#             row_no += 1
#             print(row_no, ":", line)
#         else:
#             break

# def test(cnt):
#     row_no=0
#     count=0
#     while True:
#         line = cnt.readline()
#         if line:
#             print(line)
#             surfaces = get_surfaces(line)
#             count+=1
#             print(count)
#             print(surfaces)
#         else:
#             break

# entry point
if __name__ == '__main__':
    main()
