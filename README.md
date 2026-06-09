# Star Citizen Language Fixer / 星际公民输入法修复工具 / Star Citizen 言語修正ツール / 스타 시티즌 언어 수정 도구

**English** | [中文](#中文) | [日本語](#日本語) | [한국어](#한국어)

---

## English

### Overview
This tool automatically detects when the Star Citizen window is in focus and forces the keyboard layout to English (US). This prevents issues where the game does not recognize inputs from other input methods (IMEs) like Chinese, Japanese, or Korean.

### Usage
#### Standard Usage (Recommended)
1.  Download the latest `SC_Language_Fix.zip` from the **[Releases](../../releases)** page on the right side of this page.
2.  Extract the zip file.
3.  Run `SC_Language_Fix.exe` as Administrator (required to change keyboard layout for game processes).
4.  Keep the window open while playing.

#### For Developers (Source Code)
1.  Install Python dependencies: `pip install -r requirements.txt`
2.  Run as Admin: `python sclang.py`

### Features
*   **Auto-Detection**: Only activates when Star Citizen or the RSI Launcher is the active window.
*   **Auto-Switch**: Automatically switches your keyboard layout to English (US).
*   **Setup Check**: Warns you if "English (United States)" is not installed.

---

## <a id="中文"></a>中文 (Chinese)

### 简介
此工具会自动检测《星际公民》(Star Citizen) 窗口是否处于活动状态，并强制将键盘布局切换为英语 (US)。这解决了游戏无法识别中文输入法（或其他 IME）按键的问题。

### 使用方法
#### 标准版 (推荐)
1.  在页面右侧的 **[Releases](../../releases)** (发布) 页面下载最新的 `SC_Language_Fix.zip`。
2.  解压文件。
3.  以“管理员身份”运行 `SC_Language_Fix.exe`（更改游戏进程的输入法需要此权限）。
4.  游戏过程中请保持窗口开启。

#### 开发者 (源码运行)
1.  安装依赖：`pip install -r requirements.txt`
2.  管理员运行：`python sclang.py`

### 功能
*   **自动检测**：仅在《星际公民》处于活动窗口时生效。
*   **自动切换**：自动将键盘布局切换为美式英语。
*   **环境检查**：如果未安装“英语 (美国)”输入法，会提示您安装。

---

## <a id="日本語"></a>日本語 (Japanese)

### 概要
このツールは、スターシチズン (Star Citizen) のウィンドウがアクティブになったことを自動的に検出し、キーボードレイアウトを英語 (US) に強制的に切り替えます。日本語入力 (IME) に起因するキー認識の問題を解決します。

### 使い方
#### 通常版 (推奨)
1.  このページの右側にある **[Releases](../../releases)** (リリース) から最新の `SC_Language_Fix.zip` をダウンロードします。
2.  ファイルを解凍します。
3.  `SC_Language_Fix.exe` を管理者として実行します (ゲームプロセスの設定を変更するために必要です)。
4.  プレイ中はウィンドウを開いたままにしてください。

#### 開発者向け (ソースコード)
1.  依存関係をインストール: `pip install -r requirements.txt`
2.  管理者で実行: `python sclang.py`

### 特徴
*   **自動検出**: スターシチズンがアクティブな場合のみ動作します。
*   **自動切り替え**: キーボードレイアウトを自動的に英語 (US) に切り替えます。
*   **環境チェック**: 「英語 (米国)」がインストールされていない場合、警告を表示します。

---

## <a id="한국어"></a>한국어 (Korean)

### 개요
이 도구는 스타 시티즌 (Star Citizen) 창이 활성화되었을 때를 자동으로 감지하여 키보드 레이아웃을 영어(US)로 강제 전환합니다. 한글 입력기(IME)로 인한 키 입력 오류를 방지합니다.

### 사용법
#### 일반 사용자 (추천)
1.  페이지 오른쪽의 **[Releases](../../releases)** 에서 최신 `SC_Language_Fix.zip` 을 다운로드합니다.
2.  압축을 풉니다.
3.  `SC_Language_Fix.exe` 를 관리자 권한으로 실행합니다.
4.  게임 플레이 중에는 창을 열어 두세요.

#### 개발자용 (소스 코드)
1.  의존성 설치: `pip install -r requirements.txt`
2.  관리자 권한 실행: `python sclang.py`

### 기능
*   **자동 감지**: 스타 시티즌이 활성 창일 때만 작동합니다.
*   **자동 전환**: 키보드 레이아웃을 자동으로 영어(US)로 전환합니다.
*   **환경 확인**: "영어(미국)" 언어 팩이 설치되어 있지 않으면 경고합니다.
