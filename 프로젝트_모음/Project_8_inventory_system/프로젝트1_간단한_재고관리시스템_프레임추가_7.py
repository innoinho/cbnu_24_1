import tkinter as tk
from tkinter import messagebox

# 초기 재고 딕셔너리
initial_stock = {item: 0 for item in ["품목명"]}

# 이전 재고 딕셔너리 초기화
previous_total_stock = initial_stock.copy()

# 파일에 재고 저장
def save_stock():
    with open("stock_data.txt", "w") as file:
        for item, stock in previous_total_stock.items():
            file.write(f"{item}:{stock}\n")

# 파일에서 재고 불러오기
def load_stock():
    try:
        with open("stock_data.txt", "r") as file:
            for line in file:
                item, stock = line.strip().split(":")
                previous_total_stock[item] = int(stock)
    except FileNotFoundError:
        pass

# 프로그램 실행 시 저장된 재고 데이터 불러오기
load_stock()

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

def close_window():
    save_stock()  # 프로그램 종료 시 재고 데이터 저장
    root.withdraw()  # root 창 숨기기
    root.quit()  # root 창 종료

def show_less_stock():
    try:
        less_stock_threshold = int(entry_less_stock_threshold.get())
    except ValueError:
        messagebox.showerror("오류", "숫자를 입력하세요.")
        return

    less_stock_items = [item for item, stock in previous_total_stock.items() if stock < less_stock_threshold]
    messagebox.showinfo("재고 {}개 미만 품목".format(less_stock_threshold), f"재고가 {less_stock_threshold}개 미만인 품목: {', '.join(less_stock_items)}")

def add_item():
    new_item = entry_new_item.get()
    if new_item:
        previous_total_stock[new_item] = 0
        item_menu['menu'].add_command(label=new_item, command=tk._setit(item_var, new_item))
        entry_new_item.delete(0, tk.END)

root = tk.Tk()

# 창의 크기 조정
root.geometry("600x600")  # 가로픽셀, 세로픽셀

# Tkinter 상태 표시줄 텍스트 변경
root.title("재고관리")

# 프레임 추가
frame = tk.Frame(root, bg="lightblue")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# 품목 선택을 위한 드롭다운 메뉴 생성
items = list(previous_total_stock.keys())
item_var = tk.StringVar(root)
item_var.set(items[0])  # 초기 선택값을 설정합니다.
item_menu = tk.OptionMenu(frame, item_var, *items, command=update_stock)
item_menu.pack(pady=10, fill=tk.X)

# 입고 수량 입력을 위한 Entry
label_in_stock = tk.Label(frame, text="입고 수량:", bg="lightblue")
label_in_stock.pack()
entry_in_stock = tk.Entry(frame)
entry_in_stock.pack()

# 출고 수량 입력을 위한 Entry
label_out_stock = tk.Label(frame, text="출고 수량:", bg="lightblue")
label_out_stock.pack()
entry_out_stock = tk.Entry(frame)
entry_out_stock.pack()

submit_button = tk.Button(frame, text="Submit", command=on_submit)
submit_button.pack(pady=10)

label = tk.Label(frame, text="", bg="lightblue")
label.pack(pady=10)

# 윈도우 닫기 버튼 클릭 시 close_window 함수 호출
root.protocol("WM_DELETE_WINDOW", close_window)

# 특정 재고 수량 미만인 품목 확인을 위한 입력 상자 및 버튼 추가
label_less_stock_threshold = tk.Label(frame, text="특정 재고 수량 미만인 품목을 확인하려면 숫자를 입력하세요:", bg="lightblue")
label_less_stock_threshold.pack()
entry_less_stock_threshold = tk.Entry(frame)
entry_less_stock_threshold.pack()

show_less_stock_button = tk.Button(frame, text="특정 재고 미만 품목 확인", command=show_less_stock)
show_less_stock_button.pack(pady=10)

# 새 품목 추가를 위한 입력 상자 및 버튼 추가
label_new_item = tk.Label(frame, text="새 품목 추가:", bg="lightblue")
label_new_item.pack()
entry_new_item = tk.Entry(frame)
entry_new_item.pack()

add_item_button = tk.Button(frame, text="추가", command=add_item)
add_item_button.pack(pady=10)

root.mainloop()
