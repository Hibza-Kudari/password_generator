# 🔐 Secure Password Generator - ADP Mini Project

## 📄 Abstract

In the modern digital landscape, the security of online accounts and sensitive data is heavily reliant on the strength of passwords. This project presents a **Password Generator** built using **Python** that enables users to generate strong, random, and customizable passwords. Users can define password length and choose to include uppercase letters, lowercase letters, digits, and special symbols. Leveraging Python’s `random` and `string` modules, the tool ensures high entropy and unpredictability, promoting better cybersecurity practices.

---

## 📘 Contents

| Sl. No | Title                  | Page No. |
| ------ | ---------------------- | -------- |
| 1      | Introduction           | 1        |
| 2      | Problem Definition     | 2        |
| 3      | Proposed Methodology   | 3–4      |
| 4      | Implementation         | 5–8      |
| 5      | Results and Discussion | 9        |
| 6      | Conclusion             | 10       |

### 📊 List of Figures

| Sl. No | Figure Title                   | Page No. |
| ------ | ------------------------------ | -------- |
| 4.2.1  | Prompt on Execution            | 5        |
| 4.2.2  | ERROR: Password too short      | 6        |
| 4.2.3  | ERROR: Invalid Input           | 6        |
| 4.2.4  | Successful Password Generation | 6        |

---

## 🔍 Introduction

With the rapid digitization of services, users must manage numerous accounts, each requiring secure passwords. Remembering complex passwords is difficult, leading many to use simple or repetitive ones—compromising security.

Cyber threats such as brute-force and dictionary attacks exploit these weak passwords. This project introduces a Python-based **Password Generator** that helps users create secure and customizable passwords easily.

---

## 🧩 Problem Definition

Weak or reused passwords are a major cause of data breaches. Users often:

* Use short/common passwords like `123456` or `password`
* Struggle to meet password policy requirements
* Avoid updating passwords frequently

Common attacks include:

* **Brute-force attacks**: Trying every possible combination.
* **Dictionary attacks**: Using lists of commonly used passwords.
* **Credential stuffing**: Using leaked credentials from one platform on another.

This project solves the lack of a simple, effective tool to generate secure passwords without needing technical expertise.

---

## 🔧 Proposed Methodology

This project uses a **command-line based Password Generator** built in Python. The key methodology involves:

### 1. 🧑‍💻 User Interaction

* User inputs desired password length
* User selects character types:

  * Lowercase (a–z)
  * Uppercase (A–Z)
  * Digits (0–9)
  * Special characters (!, @, #, \$, etc.)

### 2. 🛠️ Character Pool Creation

* Combines selected character types into a master set
* Ensures at least one character from each selected type is included

### 3. 🔄 Password Generation

* Uses `random` and `string` libraries to generate random characters
* Shuffles characters to eliminate patterns

### 4. 🖥️ Output Delivery

* Displays the final password to the user (not stored or saved)

### 5. ✅ Testing and Validation

* Ensures compliance with password policies
* Validates uniqueness, strength, and randomness

---

## 💻 Implementation

### 4.1 Technologies Used

| Technology      | Purpose                      |
| --------------- | ---------------------------- |
| Python 3.13     | Core programming language    |
| `random` module | Random character selection   |
| `string` module | Provides sets of characters  |
| Python IDLE     | Code execution and debugging |

---

## 📊 Results and Discussion

The password generator was successfully tested across various use cases. Key findings:

* **⚡ Performance**: Executes instantly and can generate thousands of unique passwords per second.
* **🔐 Security**: High entropy in passwords reduces risks of brute-force and dictionary attacks.
* **⚙️ Customization**: Users can tailor password structure to fit any security requirement.
* **✅ Reliability**: Ensures uniqueness and correct policy compliance every time.

---

## ✅ Conclusion

This mini project demonstrates how Python can be used to solve real-world security problems. The password generator provides a fast, reliable, and user-friendly solution to generate secure passwords on demand. It promotes good password hygiene and showcases how even simple automation tools can make a significant impact in enhancing digital security.

---

## 👨‍💻 Developed for

**ADP (Application Development using Python Laboratory)**
