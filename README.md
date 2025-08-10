# 🔍 Job Checker - Suspicious Job Detection Tool

> "おっす！オラ闇バイト検出チェッカー！" - A Dragon Ball Z themed tool to detect suspicious and potentially dangerous job postings.

## 🎯 Purpose

This tool helps identify potentially fraudulent, illegal, or dangerous job postings (commonly known as "闇バイト" or "dark part-time jobs" in Japanese). It analyzes job descriptions for suspicious patterns and provides risk assessments to protect job seekers from scams and criminal recruitment schemes.

## ⚡ Features

### Detection Categories
- **💰 Salary-related (給与関連)** - Unrealistic high pay, daily payments, immediate cash
- **📋 Job Content (仕事内容)** - Vague descriptions, "easy money" claims, suspicious tasks
- **📝 Application Requirements (応募条件)** - No ID required, age/gender targeting
- **📱 Contact Methods (連絡手段)** - SNS-only communication, unofficial channels
- **⚠️ Criminal Slang (隠語・危険ワード)** - Terms associated with illegal activities
- **🚨 Suspicious Expressions** - Limited-time offers, guaranteed income claims

### Risk Assessment System
- **Power Level Scoring** (Dragon Ball Z themed):
  - `5` - Safe (一般人レベル)
  - `1,500` - Suspicious (ラディッツレベル)
  - `18,000` - Dangerous (ベジータレベル)
  - `530,000` - Extremely Dangerous (フリーザレベル)

- **Color-coded Warnings**:
  - 🟢 Green: Safe
  - 🟡 Yellow: Somewhat suspicious
  - 🟠 Orange: Dangerous
  - 🔴 Red: Extremely dangerous

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Reliably-Unreliable/job-checker.git
cd job-checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 💻 Usage

1. **Input Job Description**: Paste or type the job posting text into the text area
2. **Analyze**: Click "いっちょ分析してみっか！" (Let's analyze it!)
3. **Review Results**: 
   - Check the risk level and color coding
   - Review the "power level" assessment
   - See which suspicious patterns were detected
   - Follow safety recommendations if high risk is detected

### Safety Recommendations
For high-risk job postings, the tool provides:
- Police consultation hotline: `#9110`
- Internet Hotline Center link for reporting suspicious content

## 🛡️ What Makes a Job Posting Suspicious?

The tool looks for various red flags including:

- **Unrealistic compensation** (extremely high pay for simple tasks)
- **Vague job descriptions** or "details explained later"
- **Unofficial communication** (LINE, Instagram DMs only)
- **No verification required** (no ID, experience, background checks)
- **Immediate payment** promises
- **Age/gender specific targeting**
- **Criminal terminology** and coded language

## 🔧 Technical Details

- **Framework**: Streamlit
- **Language**: Python
- **Detection Method**: Regex pattern matching with weighted scoring
- **Categories**: 6 main suspicious pattern categories
- **Scoring**: Weighted risk assessment system

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional suspicious patterns
- Multi-language support
- Enhanced detection algorithms
- UI/UX improvements

## ⚠️ Disclaimer

This tool is for **defensive security purposes only** - to help protect people from potentially dangerous job scams and criminal recruitment. It should not be used to create, facilitate, or improve malicious job postings.

The tool provides guidance but users should always:
- Use their own judgment
- Research employers independently
- Report suspicious activities to authorities
- Never provide personal information to unverified sources

## 📞 Emergency Contacts

- **Police Consultation**: `#9110`
- **Internet Hotline Center**: https://www.internethotline.jp/

## 📄 License

This project is intended for educational and safety purposes. Use responsibly.

---

**Stay safe and remember: If it sounds too good to be true, it probably is! 🛡️**