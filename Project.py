import streamlit as st
import base64
from pathlib import Path


# --- 網頁設定 ---
st.set_page_config(page_title="我的轉職作品集", page_icon="🚀", layout="wide")

# --- 路徑設定 ---
# 取得目前這份 app.py 所在的資料夾路徑
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# 指向你的 assets 資料夾
ASSETS_DIR = current_dir / "assets"
# 定義檔案路徑
PDF_FILE = ASSETS_DIR / "第十二組_專題成果發表書.pdf"
MP4_FILE = ASSETS_DIR / "profile.mp4"

# --- 側邊欄 ---
with st.sidebar:
    st.title("導覽選單")
    st.markdown("---")
    st.write("🏃‍♂️ [個人簡介](#about)")
    st.write("🎓 [大學專題](#project)")
    st.write("📁 [個人作品](#portfolio)")
    st.write("📫 [聯絡我](#contact)")

# --- 主頁面：個人簡介 ---
st.title("👨‍💻 你好，我是 柯柏維", anchor="about")
st.subheader("目標職業：軟體工程師")
st.write("  在大學期間，我主修資訊相關課程，除了與軟體相關的必修課 C 語言程式設計與資料結構外，亦積極選修了多門進階課程，如 Python 程式設計與圖像處理等，並考取程式語言相關證照，也選修與硬體相關的課程如計算機組織結構，以強化專業基礎。課餘時間，我也持續自學並動手實作。例如:在個人電腦上嘗試運行語言模型，利用LM Studio與Ollama下載模型並將 Meta 提供的 llama 模型、阿里巴巴的qwen利用discord與openclaw進行整合；同時基於對遊戲的興趣，學習 Java 語言並嘗試開發遊戲 模組，以提升對多樣程式語言的應用能力與實務經驗。")

st.markdown("---")

# --- 主頁面：大學專題展示 ---
st.header("🎓 大學專題：智慧電控水果分級機", anchor="project")

# 建立兩欄：左邊放影片，右邊放文字介紹與 PDF
col_video, col_info = st.columns([3, 2])

with col_video:
    st.subheader("📺 專題演示影片")
    if MP4_FILE.exists():
        # 顯示影片，設置 start_time 可以指定開始秒數
        st.video(MP4_FILE, format="video/mp4", start_time=0)
        st.caption("這是我們專題的實際運行演示。")
    else:
        st.error(f"找不到影片檔案：{MP4_FILE}，請確認檔案已放入 assets 資料夾。")

with col_info:
    st.subheader("📝 專題摘要")
    st.write("""
    在這項專題中，我們解決了...
    - **問題：** 硬體方面:電控元件與嵌入式系統的python程式碼套件衝突 軟體方面:圖像分割模型與嵌入式系統的兼容性問題
    - **方法：** 軟體方面利用google提供的tensorflow套件、keras套件並以python作為開發平台訓練我們的模型。另外硬體方面使用了主要使用Raspberry Pi 4，電控原件為DC無刷馬達、攝影機、HX711電子秤套件
    - **成果：** 與果農合作，成功辨識與分類率高達80%
    """)
    
    st.markdown("---")
    
    # PDF 展示區塊
    st.subheader("📄 專題詳細報告")
    if PDF_FILE.exists():
        # 1. 提供下載按鈕
        with open(PDF_FILE, "rb") as f:
            PDFbyte = f.read()
        st.download_button(
            label="📥 下載 PDF 專題報告",
            data=PDFbyte,
            file_name="大學專題報告.pdf",
            mime="application/pdf",
        )
        
        st.write("或是直接在下方預覽：")
        
        # 讀取 PDF 並轉換為 base64 字符串
        # 2. 嵌入 PDF 預覽 (優化版)
        with open(PDF_FILE, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
        # 改用 iframe 標籤，並設定寬度為 100%
        pdf_display = f"""
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="600" 
                type="application/pdf"
                style="border:none;">
            </iframe>
        """
        
        # 使用 st.markdown 顯示 HTML
        st.markdown(pdf_display, unsafe_allow_html=True)

    else:
        st.error(f"找不到 PDF 檔案：{PDF_FILE}，請確認檔案已放入 assets 資料夾。")

st.markdown("---")

# (後續的個人作品專案和聯絡資訊區塊保持不變...)
# 個人作品
# 定義作品資料
projects = [
    {
        "title": "Discord AI 助手 (LM Studio)",
        "file": ASSETS_DIR / "project_discord.mp4",
        "desc": "展示如何將 LM Studio 串連至 Discord...",
    },
    {
        "title": "Discord AI 助手 (LM Studio)",
        "file": ASSETS_DIR / "project_discord.png",
        "desc": "展示如何將 LM Studio 串連至 Discord...",
    },
    {
        "title": "Openclaw 整合應用",
        "file": ASSETS_DIR / "project_openclaw.mp4",
        "desc": "展示如何將 Ollama 模型串連至 Openclaw...",
    },
    {
        "title": "Openclaw 整合應用",
        "file": ASSETS_DIR / "project_openclaw.png",
        "desc": "展示如何將 Ollama 模型串連至 Openclaw...",
    }
]

# --- 個人作品迴圈 ---
st.header("📁 個人作品", anchor="portfolio")

for p in projects:
    col_media, col_txt = st.columns([3, 2])

    with col_media:
        st.subheader(f"🖼️/📺 {p['title']}")
        
        if p["file"].exists():
            # 取得副檔名並轉為小寫
            file_extension = p["file"].suffix.lower()
            
            # 判斷檔案類型
            if file_extension in [".mp4", ".mov", ".avi"]:
                st.video(str(p["file"]))
            elif file_extension in [".png", ".jpg", ".jpeg", ".gif"]:
                st.image(str(p["file"]), width="stretch")
            else:
                st.warning(f"不支援的檔案格式：{file_extension}")
        else:
            st.error(f"找不到檔案：{p['file'].name}，請確認檔案已放入 assets 資料夾。")

    with col_txt:
        st.subheader("📝 作品摘要")
        st.write(p["desc"])
    
    st.markdown("---")

st.subheader("📫 聯絡方式", anchor="contact")
st.write("""
    聯絡我
    - **電子郵件：** jh959a222@gmail.com
    - **電話：** 0937798302(平日7:30~20:30為工作時間不會接電話)
    - **備註** - 麻煩您請以電郵聯絡為主，感謝您~ 
    """)