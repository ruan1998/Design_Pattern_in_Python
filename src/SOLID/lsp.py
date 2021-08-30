from abc import ABC, abstractmethod

class BaseHuman(ABC):
    def __init__(self, hp=100):
        self._hp = hp

    @property
    def hp(self):
        return self._hp
    @abstractmethod
    def be_attacted(self, demage):
        pass

class ChangableState(ABC):
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self, state):
        self._state_setter(state)
    @abstractmethod
    def _state_setter(self, state):
        pass

class Human(BaseHuman):

    def __init__(self, hp=100):
        super().__init__(hp)
    def be_attacted(self, demage):
        self._hp -= demage

class Giant(BaseHuman, ChangableState):
    GIANT_STATE = "giant"
    HUMAN_STATE = "human"
    def __init__(self, hp=100, giant_hp=10000):
        super().__init__(hp)
        self._giant_hp = giant_hp
        self._state = self.HUMAN_STATE
    def be_attacted(self, demage):
        if self.state == self.HUMAN_STATE:
            self.state = self.GIANT_STATE
        self._hp -= demage
    def _state_setter(self, state):
        if state == self.GIANT_STATE:
            self._hp = self._giant_hp
        self._state = state

# LSP = Liskov Substitution Principle
# Human 正常人
# Giant 巨人 不正常的人
# 一个巨人 是不是 一个正常人？
def _attack_he(he:Human):
    hp = he.hp
    he.be_attacted(3)
    print(f"Expected to get hp {hp - 3}, got {he.hp}")

def attack_he(he:BaseHuman):
    if isinstance(he, ChangableState):
        he.state = he.GIANT_STATE
    _attack_he(he)

if __name__ == "__main__":
    print("For Human:")
    he = Human()
    attack_he(he)

    print("For Giant:")
    giant = Giant()
    attack_he(giant)

