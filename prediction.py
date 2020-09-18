import sys
import fasttext as ft
import MeCab


class predict:

    def __init__(self):
        # モデル読み込み
        self.classifier = ft.load_model('model/model')
        # model = ft.load_model('md/model')

    def get_surfaces(self, content):
        """
        文書を分かち書き
        """
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surfaces = []
        node = tagger.parseToNode(content)
        while node:
            surfaces.append(node.surface)
            node = node.next
        return surfaces

    def tweet_class(self, content):
        # def tweet_class(model, content):
        """
        ツイートを解析して分類を行う
        """
        words = " ".join(self.get_surfaces(content))
        # labels, probabilities = self.classifier.predict([words], k=2)[1][0]
        labels, probabilities = self.classifier.predict([words])

        if labels[0][0] == "__label__1,":
            print('批判', probabilities[0][0])
        elif labels[0][0] == "__label__2,":
            print('好意', probabilities[0][0])
        # elif labels == "__label__3,":
        #     print('暮らし系', probabilities)
        # print(labels[0][0], probabilities)


if __name__ == '__main__':
    pre = predict()
    pre.tweet_class("".join(sys.argv[1:]))
