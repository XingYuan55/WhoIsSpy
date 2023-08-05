import wis_core
import tkinter as tk


class WhoIsSpyGui:
    def __init__(self) -> None:
        self._n = 0
        self.controls = dict()
        self.win = tk.Tk()
        self.words = []
        self.nop = 3
        self.controls["mainLbl"] = tk.Label(self.win, text="欢迎来到单机【谁是卧底】", fg="brown")
        self.controls["mainBtn"] = tk.Button(self.win, text="点击开始", command=self.start_game)
        
        self.layout()
        
    def start_game(self):
        self.words = wis_core.distribute_words(nop=self.nop)
        
    def show_words(self):
        self._n = 0
        self.controls["mainLbl"].config(text="你是一号玩家")
        for i in range(self.nop):
            self._n=i
            self.controls["mainBtn"].config(text="点我看词", command=self.see_a_word)
            self.controls["mainBtn"].config(text="看完点我", command=self.close_a_word)
        
    def see_a_word(self):
        self.controls["mainLbl"].config(text=str(self.words[self._n]))
        
    def close_a_word(self):
        self.controls["mainLbl"].config(text=f"你是{self._n+1}号玩家")

        
        
    def layout(self) -> int:
        for control in self.controls.values():
            control.pack()
            
        self.win.mainloop()
            
        
if __name__ == "__main__":
    whoisspygui = WhoIsSpyGui()