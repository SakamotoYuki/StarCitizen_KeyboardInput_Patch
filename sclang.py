import win32gui
import win32process
import win32api
import win32con
import time
import psutil
import sys
import threading
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import ctypes
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon

class StarCitizenLanguageManager:
    def __init__(self, log_callback=None):
        self.target_language = "en-US"
        self.starcitizen_names = ["Star Citizen", "RSI Launcher"]
        self.english_layout_id = 0x0409
        self.log_callback = log_callback
        self.running = True

    def log(self, message):
        if self.log_callback:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.log_callback(f"[{timestamp}] {message}")
        else:
            print(message)

    def get_window_pid(self, hwnd):
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            return pid
        except:
            return None
    
    def get_process_name(self, pid):
        try:
            process = psutil.Process(pid)
            return process.name().lower()
        except:
            return None
    
    def is_starcitizen_window(self, hwnd):
        try:
            if not win32gui.IsWindowVisible(hwnd):
                return False
            
            window_title = win32gui.GetWindowText(hwnd)
            if not window_title:
                return False
            
            for name in self.starcitizen_names:
                if name in window_title:
                    return True
            
            pid = self.get_window_pid(hwnd)
            if pid:
                process_name = self.get_process_name(pid)
                if process_name and ("starcitizen" in process_name or "rsi" in process_name or "star citizen" in process_name):
                    return True
            return False
        except:
            return False
    
    def set_english_keyboard_layout(self, hwnd):
        try:
            hkl = win32api.LoadKeyboardLayout("00000409", win32con.KLF_ACTIVATE)
            win32api.PostMessage(hwnd, 0x0050, 0, int(hkl))
            self.log("Request sent to switch to English keyboard layout")
            return True
        except Exception as e:
            self.log(f"Error switching to English: {e}")
            return False
    
    def check_current_layout(self):
        try:
            hwnd = win32gui.GetForegroundWindow()
            thread_id = win32process.GetWindowThreadProcessId(hwnd)[0]
            layout_id = win32api.GetKeyboardLayout(thread_id) & 0xFFFF
            return layout_id
        except:
            return None
    
    def is_english_layout_active(self):
        current_layout = self.check_current_layout()
        return current_layout == self.english_layout_id
    
    def monitor_loop(self):
        self.log("Monitoring started...")
        was_in_focus = False
        
        while self.running:
            try:
                hwnd = win32gui.GetForegroundWindow()
                is_starcitizen = self.is_starcitizen_window(hwnd)
                
                if is_starcitizen and not was_in_focus:
                    self.log("Star Citizen detected / in focus")
                elif not is_starcitizen and was_in_focus:
                    self.log("Star Citizen out of focus")
                
                was_in_focus = is_starcitizen
                
                if is_starcitizen:
                    if not self.is_english_layout_active():
                        self.log("Star Citizen in focus - Enforcing English Layout")
                        self.set_english_keyboard_layout(hwnd)
                    time.sleep(1)
                else:
                    time.sleep(1)
                    
            except Exception as e:
                self.log(f"Error in monitor loop: {e}")
                time.sleep(5)

class ScLangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Star Citizen Language Fixer")
        self.root.geometry("400x300")
        
        # Status Label
        self.status_label = tk.Label(root, text="Status: Running", fg="green", font=("Arial", 10, "bold"))
        self.status_label.pack(pady=5)
        
        # Log Area
        self.log_area = scrolledtext.ScrolledText(root, width=50, height=15, state='disabled')
        self.log_area.pack(padx=10, pady=5)
        
        # Manager
        self.manager = StarCitizenLanguageManager(self.update_log)
        
        # Start Thread
        self.monitor_thread = threading.Thread(target=self.manager.monitor_loop, daemon=True)
        self.monitor_thread.start()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Check for English layout on startup
        self.ensure_english_available()

    def update_log(self, message):
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.configure(state='disabled')

    def on_closing(self):
        self.manager.running = False
        self.root.destroy()
        sys.exit(0)

    def check_english_installed(self):
        try:
            # Try to load United States - English keyboard layout
            # 00000409 is the identifier for English (United States)
            # KLF_NOTELLSHELL prevents the shell from getting a notification, 
            # we just want to see if we CAN load it.
            hkl = win32api.LoadKeyboardLayout("00000409", win32con.KLF_NOTELLSHELL)
            if not hkl:
                raise Exception("LoadKeyboardLayout returned None/0")
            return True
        except Exception as e:
            print(f"English check failed: {e}")
            return False

    def ensure_english_available(self):
        if not self.check_english_installed():
            response = tk.messagebox.askyesno(
                "Missing English Layout / 缺少英语布局",
                "English (United States) keyboard layout is required but not detected.\n"
                "Do you want to open Language Settings to install it?\n\n"
                "《星际公民》语言修复工具需要“英语(美国)”键盘布局。\n"
                "是否打开设置页面进行安装？"
            )
            if response:
                import os
                os.system("start ms-settings:region-language")
            # We don't exit, we just warn, in case the check was a false negative.
            # But maybe we should? The tool won't work without it.
            # Let's just warn and let them proceed if they insist.
            self.update_log("WARNING: English layout check failed. Tool may not work.")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    executable = sys.executable
    script_path = sys.argv[0]
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    try:
        ShellExecuteEx(
            nShow=win32con.SW_SHOW,
            fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
            lpVerb='runas',
            lpFile=executable,
            lpParameters=f'"{script_path}" {params}'
        )
        sys.exit(0)
    except Exception as e:
        print(f"Failed to elevate: {e}")

def main():
    # If not admin, try to elevate
    if not is_admin():
        # If we are packaged with PyInstaller, the --uac-admin flag handles this usually,
        # but this check is good for dev/script usage.
        run_as_admin()
        return

    root = tk.Tk()
    app = ScLangApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()