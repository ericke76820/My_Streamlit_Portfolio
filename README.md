# 🚀 個人轉職作品集網站 (Python & Streamlit)

這是一個使用 **Python** 與 **Streamlit** 框架架設的個人作品集網站。旨在向招募團隊展示我的大學專題成果、AI 實作專案以及我的技術成長軌跡。

---

## 🛠️ 技術棧 (Tech Stack)

* **開發語言：** Python 3.9+
* **網頁框架：** [Streamlit](https://streamlit.io/) (用於快速開發資料驅動的 Web 應用)
* **部署環境：** Streamlit Cloud / Render 
* **核心套件：** * `pathlib`: 跨平台路徑管理
    * `base64`: PDF 編碼與內嵌預覽

---

## 🌟 專案亮點 (Project Highlights)

### 1. 互動式作品展示
* **動態影片演示：** 整合 MP4 檔案，直觀呈現 Discord AI 機器人與 Ollama 模型的運行實況。
* **PDF 線上預覽：** 透過 Base64 編碼技術，讓人資無需下載即可直接在瀏覽器翻閱大學專題報告。

### 2. AI 實作整合 (LLM Integration)
* **LM Studio & Discord:** 實作在地端執行大型語言模型並串接至通訊軟體。
* **Ollama 流程自動化:** 探索地端模型與 Openclaw 的整合應用。

### 3. 專業工程實踐
* **物件導向路徑管理:** 捨棄傳統字串拼接，採用 `pathlib` 確保程式碼在不同作業系統間的相容性。
* **模組化設計:** 使用 Python List 與 Dictionary 結構化管理專案內容，便於後續擴展。

---

## 📂 目錄結構

```text
.
├── Project.py              # 網站主程式
├── assets/             # 靜態資源資料夾 (影片、PDF、圖片)
│   ├── project_demo.mp4
│   └── project_report.pdf
├── requirements.txt    # 專案依賴套件表
└── README.md           # 本說明文件