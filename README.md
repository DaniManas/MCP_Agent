# 🧠 AI Stick Notes — MCP Agent for Notes & Email Automation

This project is a custom AI agent powered by **Claude + FastMCP**, capable of taking notes, summarizing them, and even sending real emails — all via natural language prompts.

It connects a local Python toolset to Claude through the **Model Context Protocol (MCP)**, allowing the LLM to actually call functions, not just generate responses.

---

## 🚀 Features

- 📝 `add_note()` – Save a quick note to your local file
- 📖 `read_notes()` – View all saved notes
- 🔁 `get_latest_note()` – Get the most recently added note
- 🧠 `note_summary_prompt()` – Ask the AI to summarize all notes
- 📬 `send_email()` – Send an email using Gmail SMTP (secure via `.env`)

---

## 📂 Project Structure

```bash
.
├── main.py            # The MCP agent code with tool definitions
├── notes.txt          # Stores all saved notes
├── .env               # Contains secure Gmail credentials
```

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/DaniManas/MCP_Agent.git
cd MCP_Agent
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password
```

> ⚠️ Use a Gmail **App Password**, not your regular password.  
> You must have 2FA enabled on your account to generate this.

4. **Run the MCP agent**

```bash
uv run --with mcp[cli] mcp run main.py
```

---

## 🧪 Example Usage

Ask Claude (in your MCP-connected environment):

> “Add a note saying ‘Finish AI assignment tonight.’”  
> → ✅ Claude will call `add_note()` and save it in `notes.txt`.

> “Send an email to alice@example.com about the team dinner.”  
> → ✅ Claude will use `send_email()` and deliver it via Gmail SMTP.

---

## 🛡️ Security Notes

- `.env` is ignored via `.gitignore` — never share your credentials publicly
- Uses TLS via `smtplib` to ensure secure email transmission
- App Passwords are required for Gmail authentication

---

## 💡 Future Ideas

- Discord integration for message delivery  
- Add file attachment support to emails  
- AI-powered tagging and sorting of notes

---

## 🙋‍♂️ Author

**Manas A Dani**  
Built this as part of my journey into agentic AI and tool-using LLMs.  
If you have cool agent ideas or are building something similar, feel free to connect!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
