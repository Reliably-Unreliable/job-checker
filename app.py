import streamlit as st
import re

def check_suspicious_job(text):
    suspicious_patterns = {
        "給与関連": [
            r"日給[0-9]+万",
            r"月収[0-9]+0万",
            r"高額収入",
            r"日払い",
            r"即日払い",
            r"時給[2-9],[0-9]{3}",
            r"短期.*高収入",
            r"誰でも.*高収入",
            r"簡単.*高収入",
            r"即日.*高収入",
            r"[0-9]+万円以上"
        ],
        "仕事内容": [
            r"具体的な仕事内容は面談時",
            r"運ぶだけ",
            r"電話をかけるだけ",
            r"受付だけ",
            r"簡単作業",
            r"誰でもできる",
            r"詳しくはDM"
        ],
        "応募条件": [
            r"身分証不要",
            r"経験不問",
            r"18歳以上",
            r"秘密厳守",
            r"本名不要",
            r"ノルマなし",
            r"日時自由",
            r"即日勤務",
            r"女性のみ",
            r"男性のみ",
            r"女の子募集",
            r"男の子募集"
        ],
        "連絡手段": [
            r"LINE",
            r"ライン",
            r"インスタ",
            r"DM",
            r"非通知",
            r"個人携帯",
            r"SNS.*連絡"
        ],
        "隠語": [
            r"UD",
            r"叩き",
            r"逃げ",
            r"運び屋",
            r"掛け子",
            r"受け子",
            r"出し子",
            r"取り子"
        ]
    }
    
    results = {}
    score = 0
    
    for category, patterns in suspicious_patterns.items():
        matches = []
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                matches.append(pattern)
                score += 1
        if matches:
            results[category] = matches
    
    return results, score

def get_risk_level(score):
    if score >= 5:
        return "非常に危険", "red", "闇バイトの可能性が極めて高いです。応募は絶対に避け、警察（#9110）に通報することをお勧めします。"
    elif score >= 3:
        return "要注意", "orange", "闇バイトの可能性があります。応募は避けることをお勧めします。"
    else:
        return "低リスク", "green", "明らかな危険信号は検出されませんでした。ただし、必ず自己判断も行ってください。"

st.title("闇バイト検出チェッカー")

st.write("""
### 重要なポイント
以下の特徴が1つでもある場合は要注意です：
- 仕事内容が具体的でない
- 性別を限定している
- 給料が異常に高い
- 連絡方法がSNSである
""")

job_text = st.text_area("求人情報を入力してください...", height=200)

if st.button("分析する"):
    if job_text.strip():
        results, score = check_suspicious_job(job_text)
        risk_level, color, description = get_risk_level(score)
        
        st.markdown(f"## リスクレベル: :{color}[{risk_level}]")
        st.write(description)
        
        if results:
            st.markdown("### 検出された危険信号")
            for category, matches in results.items():
                with st.expander(f"{category}（{len(matches)}個の特徴を検出）"):
                    for match in matches:
                        st.write(f"- {match}")
            
            if score >= 3:
                st.warning("""
                ### 相談窓口
                - 警察相談ダイヤル：#9110
                - インターネット・ホットラインセンターでも通報を受け付けています
                """)