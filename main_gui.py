import time
import wis_core
import tkinter as tk
from custom_logging import Log



class WhoIsSpyGui:
    def __init__(self) -> None:
        self._n = 0
        self.controls = dict()
        self.win = tk.Tk()
        self.words = []
        self.nop = 3
        self.controls["mainLbl"] = tk.Label(self.win, text="欢迎来到单机【谁是卧底】", fg="brown", font=("黑体", 100))
        self.controls["mainBtn"] = tk.Button(self.win, text="点击开始", command=self.start_new_game, font=("微软雅黑", 50))

        self.layout()
        
    def start_new_game(self):
        self.words = wis_core.distribute_words(nop=self.nop)[0]
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
        self._closeword_wait_sign.set(1)



    def layout(self) -> int:
        layout_controls_number = 0

        for control in self.controls.values():
            control.pack()
            
        self.win.mainloop()



            
        
if __name__ == "__main__":
    whoisspygui = WhoIsSpyGui()