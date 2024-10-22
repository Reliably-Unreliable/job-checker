import streamlit as st
import re

def check_suspicious_job(text):
    suspicious_patterns = {
        "給与関連": {
            "patterns": [
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
                r"[0-9]+万円以上",
                r"[0-9]万.*即日",
                r"報酬.*[0-9]+%",
                r"ボーナス.*支給",
                r"お祝い金",
                r"1件.*[0-9]+万"
            ],
            "weight": 3  # 給与関連は重要な判断材料
        },
        "仕事内容": {
            "patterns": [
                r"具体的な仕事内容は面談時",
                r"運ぶだけ",
                r"電話をかけるだけ",
                r"受付だけ",
                r"簡単作業",
                r"誰でもできる",
                r"詳しくはDM",
                r"内容は確実に教えます",
                r"商品を受け取る",
                r"データ入力.*高額",
                r"アンケート.*高額",
                r"モニター.*高額",
                r"在宅ワーク.*高額",
                r"海外.*商品",
                r"商品.*転売"
            ],
            "weight": 2
        },
        "応募条件": {
            "patterns": [
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
                r"男の子募集",
                r"身バレ対策",
                r"身バレ.*心配",
                r"高校生.*可",
                r"学生.*高収入"
            ],
            "weight": 2
        },
        "連絡手段": {
            "patterns": [
                r"LINE",
                r"ライン",
                r"インスタ",
                r"DM",
                r"非通知",
                r"個人携帯",
                r"SNS.*連絡",
                r"Telegram",
                r"テレグラム",
                r"WhatsApp",
                r"ワッツアップ",
                r"メッセンジャー"
            ],
            "weight": 3  # SNSでの連絡は要注意
        },
        "隠語・危険ワード": {
            "patterns": [
                r"UD",
                r"叩き",
                r"逃げ",
                r"運び屋",
                r"掛け子",
                r"受け子",
                r"出し子",
                r"取り子",
                r"副業プラン",
                r"必ず稼げる",
                r"確実に稼げる",
                r"絶対稼げる",
                r"裏バイト",
                r"闇バイト",
                r"グレー",
                r"アンダー",
                r"口座作成",
                r"口座開設.*報酬",
                r"スマホ契約",
                r"携帯契約",
                r"チャトレ",
                r"風俗",
                r"出会い系"
            ],
            "weight": 4  # 隠語は最も危険
        },
        "その他の怪しい表現": {
            "patterns": [
                r"限定.*名様",
                r"今だけ.*特別",
                r"今なら.*特典",
                r"期間限定.*募集",
                r"身バレ",
                r"確実.*安全",
                r"安全.*確実",
                r"完全サポート",
                r"マニュアル完備",
                r"即金",
                r"即現金",
                r"即収入"
            ],
            "weight": 2
        }
    }
    
    results = {}
    score = 0
    total_matches = 0
    
    for category, info in suspicious_patterns.items():
        matches = []
        for pattern in info["patterns"]:
            if re.search(pattern, text, re.IGNORECASE):
                matches.append(pattern)
                score += info["weight"]
                total_matches += 1
        if matches:
            results[category] = {
                "matches": matches,
                "weight": info["weight"]
            }
    
    return results, score, total_matches

def get_power_level(score):
    if score >= 8:
        return "530000"    # フリーザ（第一形態）レベル
    elif score >= 5:
        return "18000"     # ベジータ（地球来襲時）レベル
    elif score >= 3:
        return "1500"      # ラディッツレベル
    else:
        return "5"         # 一般人レベル
        
def get_risk_level(score):
    if score >= 8:
        return "超ヤベェぞ！", "red", "おめぇ、これはとんでもねぇ闇ベェトの気配を感じっぞ！絶対に応募すんじゃねぇ！すぐに警察（#9110）に通報した方がいいぞ！"
    elif score >= 5:
        return "気をつけろよ！", "orange", "おっと、これは怪しいな！闇ベェトの気がプンプンするぞ。オラならこんなベェト、受けねぇな！"
    elif score >= 3:
        return "ちょっと怪しいぞ！", "yellow", "ん？なんか怪しい気を感じるぞ。気ぃつけた方がいいな！"
    else:
        return "大丈夫そうだ！", "green", "よし！このベェトからは悪い気は感じねぇな！オラわくわくすっぞ！でも油断は禁物だぞ！"

st.write("""
### おっす！オラ闇バイト検出チェッカー！
おめぇ、これだけは気ぃつけろよ！
オラが教える危険な特徴だ：
- 仕事の中身がボヤッとしてる
- 男か女かにこだわりすぎ
- お金の話が高すぎてカリン塔より高い
- LINEとかSNSでしか連絡取れない
- 身分証明書がいらねぇって言ってる
- その日にお金がもらえるって言ってる
""")

job_text = st.text_area("求人情報を入力してください...", height=200)

if st.button("いっちょ分析してみっか！"):
    if job_text.strip():
        results, score, total_matches = check_suspicious_job(job_text)
        risk_level, color, description = get_risk_level(score)
        power_level = get_power_level(score)
        
        st.markdown(f"## リスクレベル: :{color}[{risk_level}]")
        st.write(description)
        
        # 戦闘力表示
        st.metric(
            "戦闘力", 
            f"{power_level}", 
            f"スカウターが{total_matches}個の怪しい気を感知！"
        )
        
        if power_level == "530000":
            st.error("フリーザ！！これは最悪の闇ベェトの気配だ！！")
        elif power_level == "18000":
            st.warning("なんと！サイヤ人級の危険な気配を感じるぞ！")
        elif power_level == "1500":
            st.warning("ラディッツ級の怪しい気を感じるな...")
        else:
            st.info("人間レベルの気配だ。大丈夫そうだな！")

            if score >= 3:
                st.warning("""
                ### Z戦士に連絡
                - 警察相談ダイヤル：#9110
                - インターネット・ホットラインセンターにもZ戦士が待機してっぞ！ → https://www.internethotline.jp/
                """)
