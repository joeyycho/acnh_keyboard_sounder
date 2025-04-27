import os
import pygame
import threading
from pynput import keyboard
import tkinter as tk
from tkinter import ttk
import sys

# base_path 세팅 (pyinstaller 대응)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)
SOUND_DIR = os.path.join(base_path, "sounds")

# 초기 설정
current_volume = 0.5
is_shift_pressed = False

# pygame 초기화
pygame.mixer.init()

# 문자 및 특수문자 매핑
char_sound_map = {ch: f"{ch}.wav" for ch in 'abcdefghijklmnopqrstuvwxyz0123456789'}
shift_combos = {
    '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
    '-': '_', '=': '+', '[': '{', ']': '}', '\\': '|',
    ';': ':', "'": '"', ',': '<', '.': '>', '/': '?'
}
special_keys = {
    'space': 'space.wav', 'enter': 'enter.wav', 'tab': 'tab.wav',
    'backspace': 'backspace.wav', 'caps_lock': 'caps_lock.wav',
    'shift': 'shift.wav', 'shift_r': 'shift.wav',
    'esc': 'esc.wav'
}

# 사운드 로딩
sounds = {}

def load_sound(key, filename):
    path = os.path.join(SOUND_DIR, filename)
    if os.path.exists(path):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(current_volume)
        sounds[key] = sound

# 전체 사운드 로드
for key, filename in {**char_sound_map, **special_keys}.items():
    load_sound(key, filename)
for k, symbol in shift_combos.items():
    load_sound(symbol, f"{symbol}.wav")

# 볼륨 조절 함수
def set_all_volume(vol):
    for snd in sounds.values():
        snd.set_volume(vol)

# 키보드 리스너
def on_press(key):
    global is_shift_pressed
    try:
        k = key.char
        if is_shift_pressed and k in shift_combos:
            k = shift_combos[k]
        k = k.lower()
    except AttributeError:
        k = str(key).replace("Key.", "").lower()
        if k in ['shift', 'shift_r']:
            is_shift_pressed = True

    if k in sounds:
        sounds[k].play()

def on_release(key):
    global is_shift_pressed
    try:
        if key.name.lower() in ['shift', 'shift_r']:
            is_shift_pressed = False
    except AttributeError:
        pass

# GUI 스레드
def run_gui():
    global current_volume
    def on_slider_change(val):
        global current_volume
        current_volume = float(val)
        set_all_volume(current_volume)

    root = tk.Tk()
    root.title("🔊 키음 볼륨 조절기")
    root.geometry("300x80")
    root.resizable(False, False)

    label = ttk.Label(root, text="볼륨 조절", font=("Arial", 12))
    label.pack(pady=5)

    volume_slider = ttk.Scale(root, from_=0, to=1, orient="horizontal",
                              value=current_volume, command=on_slider_change)
    volume_slider.pack(fill="x", padx=20)

    root.mainloop()

def main():
    threading.Thread(target=run_listener, daemon=True).start()
    run_gui()

def run_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
