import pygetwindow as gw
import pyautogui
import pyperclip
import time

# 指定目標視窗名稱的關鍵字
target_window_name = "test_group"

# 要發送的訊息
message = "這是測試訊息!"

# 尋找target_window_name視窗
windows = [w for w in gw.getWindowsWithTitle(target_window_name) if target_window_name in w.title]
if windows:
    # active 視窗
    window = windows[0]
    window.activate()  # 將視窗移到前景
    print(f"找到視窗並active: {window.title}")

    time.sleep(2)  # 依據電腦性能調整

    try:
        pyperclip.copy(message)  # 將message複製到剪貼簿

        # 模擬 Ctrl+V
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)  # 確保已貼上

        # 按下 Enter 發送訊息
        pyautogui.press("enter")
        print("訊息已發送!")
    except Exception as e:
        print(f"Exception: {e}")
else:
    print(f"找不到 '{target_window_name}' 視窗!")
