### **Important Warning**
- This script automatically opens multiple browser tabs to access URLs, which may trigger robot detection mechanisms on websites.
- Use responsibly; the repository owner is not liable for any issues resulting from misuse or automated detection by websites.

### **Instructions for Using the Script**

#### **Prerequisites**

Before starting, ensure the following:

1. **Python**: Version 3.7 or higher installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Mozilla Firefox**: Download and install it from [Mozilla Firefox](https://www.mozilla.org/firefox/).
3. **Geckodriver**: Download the Geckodriver that matches your Firefox version from [Geckodriver Releases](https://github.com/mozilla/geckodriver/releases).
   - **Windows**: Download the `.zip` file and extract it.
   - **Mac/Linux**: Download the `.tar.gz` file and extract it.
4. **CSV File**: Prepare a CSV file named `Key_Contributions_with_URLs.csv` with the following structure:

| Title          | URL                                    |
|----------------|----------------------------------------|
| Paper 1        | https://example.com/paper1.pdf         |
| Paper 2        | https://example.com/paper2.pdf         |
| Paper 3        | https://example.com/paper3.pdf         |

---

#### **Step 1: Setting Up the Environment**

##### **Windows**:
1. Move the extracted `geckodriver.exe` to a folder like `C:\geckodriver`.
2. Add this folder to your system PATH:
   - Right-click on **This PC** > **Properties**.
   - Select **Advanced System Settings** > **Environment Variables**.
   - Under **System Variables**, find `Path` and click **Edit**.
   - Add the path to the folder (e.g., `C:\geckodriver`).
   - Click **OK** to save changes.

##### **Mac/Linux**:
1. Move the extracted `geckodriver` to `/usr/local/bin`:
   ```bash
   sudo mv geckodriver /usr/local/bin/
   ```
2. Make it executable:
   ```bash
   chmod +x /usr/local/bin/geckodriver
   ```

##### **Common Steps**:
1. Open a terminal or command prompt.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```
4. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

#### **Step 2: Running the Script**

1. Place the `Key_Contributions_with_URLs.csv` file in the same directory as the script.
2. Update the `firefox_driver_path` in the script to the full path of Geckodriver.
3. Run the script:
   ```bash
   python firefox_browser_opener.py
   ```

---

#### **What the Script Does**

1. Reads the `Key_Contributions_with_URLs.csv` file.
2. Validates the structure of the file.
3. Opens each URL in a new tab in Firefox.
4. Prints the title and URL being accessed.
5. Waits briefly before moving to the next URL.

---

#### **Troubleshooting**

- **Error: Geckodriver not found**: Ensure Geckodriver is in your system PATH or update the `firefox_driver_path` variable in the script.
- **CSV File Errors**: Ensure the file contains `Title` and `URL` columns and is properly formatted.
- **Robot Detection**: If the website blocks access, try reducing the number of tabs opened or increase the delay between actions.

---

#### **Final Notes**

- This script is designed for educational purposes and research workflows. Use it responsibly.
- Always ensure compliance with website terms of use when automating access.
