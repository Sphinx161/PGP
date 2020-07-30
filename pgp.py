import smtplib
import subprocess


class Pgp:

    def generate_key(self):
        subprocess.call(["gpg", "--full-generate-key"])

    def encrypt(self, email_key, filepath):
        email = email_key
        file = filepath
        if not email_key:
            print("[-]Email missing!")
        if not file:
            print("[-]File path missing!")
        subprocess.call(["gpg", "--encrypt", "--sign", "-r", email, file])

    def send_email(self, sender, password, receiver, email_key, file_name):
        if not sender:
            print("[-]Sender email address not found!")
        if not password:
            print("[-]Password not found!")
        if not receiver:
            print("[-]Receiver email address not found")
        msg = self.export_keys(email_key, file_name)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg)
            server.quit()
            print("Mail sent successfully")
        except smtplib.SMTPException:
            print("Error: unable to send email")

    def export_keys(self, email_key, file_name):
        if not email_key:
            print("[-]Email missing!")
        if not file_name:
            print("[-]File name not defined! (publickey.asc)")
        email = email_key
        file = file_name
        message = subprocess.check_output(["gpg", "--armor", "--export", email, ">", file])
        return message

    def decrypt(self, new_name, file_path):
        if not file_path:
            print("[-]Encrypted file missing!")
        if not new_name:
            print("[-]File name not defined! (publickey.asc)")
        encrypted_file = file_path
        name_file = new_name
        subprocess.call(["gpg", "--output", name_file, "--decrypt", encrypted_file])


