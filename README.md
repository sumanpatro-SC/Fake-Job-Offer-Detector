# Fake-Job-Offer-Detector🛡️ Fake Job Offer Detector

A simple cybersecurity tool that helps users identify fake job and internship offers using rule-based risk analysis.

🚀 Problem Statement

Fake job offers are increasingly targeting students and fresh graduates through emails, messaging apps, and social media. These scams often demand registration fees, promise instant hiring, or use unofficial communication channels, leading to financial loss and data theft.

💡 Solution

Fake Job Offer Detector analyzes job messages and detects scam patterns such as:
Requests for fees
Urgent hiring language
Unofficial email domains
Unrealistic job promises

It provides a risk score and clear warning so users can make safer decisions.

✨ Features

📄 Paste any job or internship message
⚠️ Detects common scam indicators
📊 Shows risk score (0–100%)
🟢 Low / 🟡 Medium / 🔴 High risk classification
🔐 No data storage (privacy-friendly)
⚡ Fast and easy to use

🛠️ Built With

Python
Flask
HTML5
CSS3
JavaScript
Rule-based detection logic
Git & GitHub



fake-job-offer-detector/
│
├── app.py                 # Flask backend
├── detector.py            # Detection logic
├── rules.py               # Scam rules & keywords
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   ├── style.css          # Styling
│   └── script.js          # Frontend logic
└── requirements.txt       # Dependencies

⚙️ How It Works

User pastes a job message
The system checks for suspicious patterns
Each indicator adds to a risk score
Final risk level is displayed with reasons

Risk Calculation
Risk Score=∑Suspicious Indicators

▶️ How to Run the Project
1️⃣ Install Dependencies 
               pip install -r requirements.txt
2️⃣ Run the Application
             python app.py
3️⃣ Open in Browser
             http://127.0.0.1:5000

🧪 Example Use Case

Input:

“Congratulations! You are selected. Pay ₹2000 registration fee for instant joining. Contact hrcompany@gmail.com
”

Output:

🔴 High Risk

Risk Score: 80%

Reason
Registration fee requested
Unofficial email domain
Instant joining claim

🚧 Challenges Faced

Designing effective detection rules without false positives
Keeping logic simple yet meaningful
Making cybersecurity results easy to understand for non-technical users

🔮 Future Enhancements
OCR support for screenshots
Browser extension for email/LinkedIn
Multi-language support
Machine learning-based detection
Mobile app version

🎯 Conclusion

Fake Job Offer Detector demonstrates how simple cybersecurity tools can create real-world impact. By focusing on awareness and prevention, this project helps users stay safe from job scams.