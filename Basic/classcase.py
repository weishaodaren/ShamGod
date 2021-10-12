from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """战斗员"""

    # 通过__slots__魔法限定对象可以绑定的成员
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        :param name: 名称
        :param hp: 生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        :return：使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self.hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
      __slots__ = ('_name', '_hp')

      def attack(self, other):
          other.hp -= randint(10, 20)

      def __str__(self):
           return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        return monster.alive > 0

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('weishaodaren', 100, 100)
    m1 = Monster('A', 10)
    m2 = Monster('B', 20)
    m3 = Monster('C', 5)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合' % fight_round)
        m = select_alive_one(ms) # 选中一致怪兽
        skill = randint(1, 10) # 通过随机数选中技能
        if skill <= 6:
            print('%s使用了普通攻击打了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%02d点' % (u.name, u.resume()))

        # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
        elif skill <= 9: 
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)

        # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
        else:
            if u.huge_attack(ms):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        # 如果选中的小怪兽没有死就回击奥特曼
        if m.alive > 0:
             print('%s回击了%s.' % (m.name, u.name))
             m.attack(u)
        # 每个回合结束后显示奥特曼和小怪兽的信息
        display_info(u, ms)
        fight_round += 1
        print('\n=======战斗结束========\n')
        if u.alive > 0:
            print('%s胜利' % u.name)
        else:
            print('${m.name}胜利')


if __name__ == '__main__':
    main()

