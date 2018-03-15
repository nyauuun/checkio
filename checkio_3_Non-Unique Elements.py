def checkio(data):

    list = data
    list_cnt = []
            
    for n in list:
        if list.count(n) >= 2:
            list_cnt.append(n)
        else:
            continue

    return list_cnt

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")

"""
■アルゴリズム
・forで頭から１つづつ値を取得
・取得した値が重複してれば新規の配列に格納する

■学習したこと
・list.count("A") => Aが何個リストにあるか出力
https://www.pythonweb.jp/tutorial/list/index10.html
・set() 配列の重複項目を削除
li_uniq = set(data)

■Next
・内包表記とは？

"""