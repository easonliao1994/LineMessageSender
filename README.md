# LineMessageSender

LineMessageSender 是一個用於自動發送 Line 訊息的 Python 程式。透過指定視窗名稱和訊息內容，程式能自動觸發 Line 應用程式並發送訊息。

## 功能
- 自動搜尋並激活指定的 Line 視窗
- 自動發送預設的訊息

## 安裝

請確保已安裝 Python 3 和以下相依套件：
```sh
pip install pygetwindow pyautogui pyperclip
```

## 使用方法

1. 執行程式
```
python send_message.py
```

## 注意事項
1. 請確保 Line 應用程式已開啟，並且指定的視窗名稱與 target_window_name 相符 (聊天視窗點擊右鍵->以個別視窗開啟)。
2. 根據電腦效能，可能需要調整 time.sleep 的時間。