# 自動販売機
import random


class Drink:
    def __init__(self, name, price, stock):
        self.name = name  
        self.price = price  
        self.stock = stock  

    def info(self):
        """情報（名称と価格）を返す"""
        return self.name + ' ' + str(self.price) + '円'


class VendingMachine:
    def __init__(self):
        self.drink_list = [] 

    def show_all(self):
        """全ての飲み物を表示"""
        for drink in self.drink_list:
            print(drink.info())

    def add_drink(self, drink):
        """1種類の飲み物を登録"""
        self.drink_list.append(drink)

    def select_drink(self, kth):
        """kth番目の飲み物の情報を返す"""
        return self.drink_list[kth].info()

    def show_selected_drink(self, kth):
        """kth番目の飲み物の売り切れまたは値段を表示"""
        drink = self.drink_list[kth]
        if drink.stock <= 0:
            print(drink.name + "は売り切れています。申し訳ありません")
        else:
            print(drink.name + "を選択しました。" + str(drink.price) + "円になります")

    def gacha(self):
        """ガチャ（1/5の確率で当たり（True）を返す）"""
        return random.randint(1, 5) == 1

    def purchase_drink(self, kth, fee):
        """お金を投入してkth番目の飲み物を1本購入"""
        drink = self.drink_list[kth]
        print(str(fee) + '円が投入されました')
        if fee < drink.price:
            print('購入金額が足りません')
            return
        change = fee - drink.price
        if change > 0:
            print(str(change) + "円のお釣りになります")
        drink.stock -= 1  

        if drink.stock > 0 and self.gacha():
            print('大当たりーーー')
            print('もう1本 「' + drink.name + "」を差し上げます！")
            drink.stock -= 1


vm = VendingMachine()
vm.add_drink(Drink('珈琲', 130, 10))
vm.add_drink(Drink('お茶', 150, 12))
vm.add_drink(Drink('サイダー', 110, 2))

print('=== 全商品の表示 ===')
vm.show_all()

print('\n=== 3番目の商品のボタンを押します ===')
vm.show_selected_drink(2)

print('\n=== 3番目の商品を選択し100円を投入 ===')
vm.purchase_drink(2, 100)

print('\n=== 3番目の商品を選択し150円を投入 ===')
vm.purchase_drink(2, 150)

print('\n=== 3番目の商品のボタンを押します ===')
vm.show_selected_drink(2)