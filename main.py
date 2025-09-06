from asia_speech import listen, speak
from email_module import send_email
import datetime

def run():
    speak("Hello Arshit, jaris here. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        print("Command received:", command)

        if "stop" in command or "exit" in command or "goodbye" in command:
            speak("Goodbye bro, shutting down now.")
            break

        elif "send email" in command:
            # Ask for recipient email
            while True:
                speak("Who do you want to send the email to? Please say the email address.")
                to_email = listen()
                if to_email and "@" in to_email and "." in to_email:
                    break
                else:
                    speak("That doesn't sound like a valid email. Please try again.")

            # Ask for subject
            while True:
                speak("What should be the subject?")
                subject = listen()
                if subject:
                    break
                else:
                    speak("Subject cannot be empty. Please say it again.")

            # Ask for body
            while True:
                speak("What is the message?")
                body = listen()
                if body:
                    break
                else:
                    speak("Message cannot be empty. Please say it again.")

            # Confirmation
            speak(f"Sending email to {to_email} with subject {subject}. Please confirm, say yes to continue.")
            confirm = listen()

            if confirm and "yes" in confirm.lower():
                ok, msg = send_email(to_email, subject, body)
                speak(msg)
            else:
                speak("Okay, cancelled the email.")

        elif "hello" in command:
            speak("Hello bro, how are you doing today?")

        elif "your name" in command or "who are you" in command:
            speak("My name is Asia, your personal AI assistant.")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"The time is {now}")

        else:
            speak("Sorry bro, I did not understand. Please try again.")

if __name__ == "__main__":
    run()
