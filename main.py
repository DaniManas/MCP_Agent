from mcp.server.fastmcp import FastMCP
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()
#Creating mcp server
mcp = FastMCP("AI Stick Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()
def add_note(message: str)->str:
    """
    Append a note to the notes file.

    Args:
        message(str): The note content to be added.

    Returns:
        str: The message indicating that the note was added.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f: #appending
        f.write(f"{message}\n")
    return "Note added!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.

    Returns:
        str: All notes as a single string separated by line breaks.
             If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes yet."

    return f"Summarize the current notes: {content}"


@mcp.tool()
def send_email(to: str, subject: str, body: str) -> str:
    """
    Send an email to the specified recipient.

    Args:
        to (str): Recipient's email address.
        subject (str): Subject line of the email.
        body (str): Body/content of the email.

    Returns:
        str: Confirmation message or error message.
    """
    try:
        # Compose the email
        body = body.replace("[Your name]", "Manas A Dani")
        msg = EmailMessage()
        msg["From"] = os.environ["EMAIL_USER"]
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(body)

        # Send the email using Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(
                os.environ["EMAIL_USER"],
                os.environ["EMAIL_PASS"]
            )
            smtp.send_message(msg)

        return f"✅ Email successfully sent to {to}."

    except Exception as e:
        return f"❌ Failed to send email: {str(e)}"
