import re
import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="Phishing Detector", page_icon="🛡️")
st.title("🛡️ AI Phishing & Scam Detection")
st.caption("An explainable baseline detector using URL and message heuristics. Treat results as a warning signal, not proof.")

SUSPICIOUS_TERMS = ["verify your account", "urgent action", "password expires", "claim your prize",
                    "gift card", "wire transfer", "login immediately", "suspended account",
                    "bank details", "one-time password", "otp", "click here"]

def inspect_url(raw):
    reasons = []
    candidate = raw.strip()
    if not candidate:
        return reasons
    if "://" not in candidate:
        candidate = "http://" + candidate
    try:
        parsed = urlparse(candidate)
        host = parsed.hostname or ""
        if parsed.scheme != "https":
            reasons.append("URL does not use HTTPS.")
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", host):
            reasons.append("URL uses an IP address instead of a recognizable domain.")
        if len(host) > 35:
            reasons.append("Unusually long hostname.")
        if host.count("-") >= 3:
            reasons.append("Hostname contains several hyphens.")
        if parsed.username or parsed.password:
            reasons.append("URL contains embedded username/password information.")
        if len(parsed.query) > 100:
            reasons.append("URL has a long query string.")
    except Exception:
        reasons.append("URL could not be parsed.")
    return reasons

def inspect_message(message):
    low = message.lower()
    return [f"Contains suspicious phrase: '{term}'." for term in SUSPICIOUS_TERMS if term in low]

url = st.text_input("Paste a suspicious URL (optional)", placeholder="https://example.com/login")
message = st.text_area("Paste an email, SMS, or message", height=180)
if st.button("Analyze", type="primary"):
    findings = inspect_url(url) + inspect_message(message)
    score = min(100, len(findings) * 18)
    c1, c2 = st.columns(2)
    c1.metric("Heuristic risk score", f"{score}/100")
    c2.metric("Signals detected", len(findings))
    if score >= 54:
        st.error("High-risk signals detected. Do not click links or share credentials.")
    elif score:
        st.warning("Some suspicious signals were detected. Verify through an official channel.")
    else:
        st.success("No configured warning signals detected. This does NOT guarantee safety.")
    if findings:
        st.markdown("### Why it was flagged")
        for f in findings:
            st.write("- " + f)
    else:
        st.write("No matches from the current rule set.")
    st.info("Never enter passwords, OTPs, or payment details from a link in an unsolicited message. Visit the official website directly.")
