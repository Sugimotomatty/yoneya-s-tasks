
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
import csv
import os
source_default=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

source_csv="source_csv"

### 検索ツール


def search():
    if os.path.exists(source_csv):
        with open(source_csv,'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            list_of_row=list(csv_reader)
        word =input("登場人物の名前を入力してください >>> ")

        if word in list_of_row:
            print(f"{word}が見つかりました")
        else:
            print(f"{word}が見つかりませんでした")
            list_of_row.append(word)
            with open('name_list.csv','w',newline='') as file:
                writer =csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
                writer.writerows(list_of_row)

    else:
        word =input("鬼滅の登場人物の名前を入力してください >>> ")
        
        ### ここに検索ロジックを書く
        if word in source_default:
            print(f"{word}が見つかりました")
        else:
            print(f"{word}が見つかりませんでした")
            source_default.append(word)
            with open('name_list.csv','w',newline='') as file:
                writer =csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
                writer.writerows(source_default)

    

if __name__ == "__main__":
    search()


