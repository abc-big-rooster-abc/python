class Hero:
    HEROS = {"1": ["唐僧", "紧箍咒"], "2": ["悟空", "火眼金晶"], "3": ["八戒", "九齿钉耙"], "4": ["沙僧", "通天禅杖"]}
    HERO = None
    PACK = []
    # 创建一个角色
    def create_hero(self):
        print("---欢迎来到西游戏闯关游戏---")
        print("---请选择西游记主角之一(所代表的数字)开始你的游戏---")
        print("---1:唐僧------2:悟空------3:八戒------4:沙僧---")
        num = input("请输入你要选择的角色所对应的数字：")
        self.HERO = self.HEROS[num][0]
        return self.HERO
    # 展示背包物品
    def show_pack(self):
        for i in self.PACK:
            print("我的背包里还有:{}".format(i))
    def seek_monster(self):
        print("开始寻找妖怪------------")

    def physical_attack(self):
        print("开启物理攻击-------------")

    def magic_attack(self):
        print("开启魔法攻击-------------")

    def use_treasure(self):
        self.show_pack()

