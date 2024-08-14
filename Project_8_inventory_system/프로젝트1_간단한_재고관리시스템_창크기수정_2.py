import tkinter as tk
from tkinter import messagebox

# 초기 재고 딕셔너리
initial_stock = {item: 0 for item in ["늘봄1", "늘봄2", "늘봄3", "늘봄4", "늘봄5", "품목6", "품목7", "품목8", "품목9", "품목10"]}

# 이전 재고 딕셔너리 초기화
previous_total_stock = initial_stock.copy()

def on_submit():
    global previous_total_stock  # 함수 내에서 전역 변수를 사용하기 전에 선언

    selected_item = item_var.get()
    
    # 입고 및 출고 수량 입력 확인
    in_stock_entry = entry_in_stock.get()
    out_stock_entry = entry_out_stock.get()
    
    # 입고 및 출고 수량이 입력되지 않으면 0으로 처리
    if in_stock_entry == "":
        in_stock = 0
    else:
        in_stock = int(in_stock_entry)
        
    if out_stock_entry == "":
        out_stock = 0
    else:
        out_stock = int(out_stock_entry)
        
    # 이전 품목 재고
    previous_item_stock = previous_total_stock[selected_item]
    
    # 전체 재고 수량 계산
    total_stock = previous_item_stock + in_stock - out_stock
    
    # 출고 수량이 전체 재고보다 많은지 확인하여 예외 처리
    if total_stock < 0:
        messagebox.showerror("오류", "출고 수량이 전체 재고보다 많습니다.")
        return
    
    # 재고 수량 업데이트
    label.config(text="선택된 품목: {}\n입고 수량: {}\n출고 수량: {}\n재고 수량: {}".format(selected_item, in_stock, out_stock, total_stock))
    
    # 현재 품목 재고를 다음 계산을 위해 저장
    previous_total_stock[selected_item] = total_stock
    
    # 입력 상자 초기화
    entry_in_stock.delete(0, tk.END)
    entry_out_stock.delete(0, tk.END)

def update_stock(event):
    selected_item = item_var.get()
    previous_item_stock = previous_total_stock[selected_item]
    label.config(text="선택된 품목: {}\n현재 재고 수량: {}".format(selected_item, previous_item_stock))

root = tk.Tk()

# 창의 크기 조정
root.geometry("600x400")  # 가로 600픽셀, 세로 400픽셀

# 품목 선택을 위한 드롭다운 메뉴 생성
items = ["늘봄1", "늘봄2", "늘봄3", "늘봄4", "늘봄5", "품목6", "품목7", "품목8", "품목9", "품목10"]
item_var = tk.StringVar(root)
item_var.set(items[0])  # 초기 선택값을 설정합니다.
item_menu = tk.OptionMenu(root, item_var, *items, command=update_stock)
item_menu.pack()

# 입고 수량 입력을 위한 Entry
label_in_stock = tk.Label(root, text="입고 수량:")
label_in_stock.pack()
entry_in_stock = tk.Entry(root)
entry_in_stock.pack()

# 출고 수량 입력을 위한 Entry
label_out_stock = tk.Label(root, text="출고 수량:")
label_out_stock.pack()
entry_out_stock = tk.Entry(root)
entry_out_stock.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

