import sys
import time
import wis_core
import tkinter as tk
from custom_logging import Log


class WhoIsSpyGui:
    def __init__(self) -> None:
        self.controls = dict()
        self.win = tk.Tk()
        self.words = []
        self.nop = 5
        self.ready_new_game()

        self.layout()

    def ready_new_game(self):
        self._n = 0
        self.controls["mainLbl"] = tk.Label(self.win, text="欢迎来到单机【谁是卧底】", fg="brown", font=("黑体", 100))
        self.controls["mainBtn"] = tk.Button(self.win, text="点击开始", command=self.start_new_game,
                                             font=("微软雅黑", 50))
        
    def start_new_game(self):
        w = wis_core.distribute_words(nop=self.nop)
        self.words = w[0]
        self.spy_word = w[1]
        self.show_words()

    # 第一步：分词
    def show_words(self):
        self._n = 0
        self.controls["mainLbl"].config(text="你是一号玩家")  # 第一个玩家
        Log(f"_n = {self._n}，" )
        self._seeword_wait_sign = tk.IntVar()
        self._seeword_wait_sign.set(0)
        for self._n in range(self.nop):
            self.controls["mainBtn"].config(text="点我看词", command=self._see_a_word)
            self.controls["mainBtn"].wait_variable(self._seeword_wait_sign)


    def _see_a_word(self):
        Log(f"SEE _n = {self._n}, nop = {self.nop}, word={self.words[self._n], }")

        self.controls["mainLbl"].config(text=str(self.words[self._n]))

        self._closeword_wait_sign = tk.IntVar()
        self._closeword_wait_sign.set(0)
        self.controls["mainBtn"].config(text="看完点我", command=self._close_a_word)
        self.controls["mainBtn"].wait_variable(self._closeword_wait_sign)
        self._seeword_wait_sign.set(1)
        
    def _close_a_word(self):
        Log(f"CLOSE _n = {self._n}, nop = {self.nop}")
        if(self._n + 1) < self.nop:
            self.controls["mainLbl"].config(text=f"你是{self._n+2}号玩家")
        else:
            self.controls["mainLbl"].config(text=f"分词结束，开始讨论")
            self.controls["mainBtn"].config(text=f"讨论完了开始投票", command=self.voting)
        self._closeword_wait_sign.set(1)

    # 第二步：投票
    def voting(self):
        try:
            del self.voting_buttons
        except:
            pass
        self.voting_buttons = dict()
        self._vote_n = 0
        self._voted_wait_sign = tk.IntVar()
        self.had_voted = []
        for i in range(0, self.nop):
            self.had_voted += 0
        for self._vote_n in range(0, self.nop):
            self._voted_wait_sign.set(0)
            # TODO: 按按钮时投票，并将被投这个人的编号传给vote_sb
            self.voting_buttons[self._vote_n] = tk.Button(text=f"投{self._vote_n+1}号", command=...)
            self.voting_buttons[self._vote_n].pack()

    def vote_sb(self):
        Log(f"SPY_WORD: {self.spy_word}, n: {self._vote_n}")
        if self.words[self._vote_n] == self.spy_word:
            self.controls["mainLbl"].config(text=f"{self._vote_n+1}号是卧底，平民胜利！卧底词：{self.spy_word}\n5秒后自动退出")
            time.sleep(5)
            sys.exit()
        else:
            self.controls["mainLbl"].config(text=f"{self._vote_n+1}号是平民")
            self._voted_wait_sign.set(1)

    def layout(self) -> int:
        layout_controls_number = 0

        for control in self.controls.values():
            control.pack()
            
        self.win.mainloop()



def find_val_from_key_in_a_dict(dic: dict, val):
    for i in dic:
        if dic[i] == val:
            return i
        
if __name__ == "__main__":
    whoisspygui = WhoIsSpyGui()