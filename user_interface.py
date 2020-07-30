import pgp


class Execute:

    def instruction(self):
        print("[+] Select your choice!")
        print("------------------------")
        print("[1] Generate")
        print("[2] Encrypt")
        print("[3] Decrypt")
        print("[4] Export keys via mail")
        print("[5] Quit")
        print("------------------------")

    def execute(self):
        obj = pgp.Pgp()
        inp = int(input())
        if inp == 1:
            obj.generate_key()

        elif inp == 2:
            print("[+] Specify [-e email_id_public_key] [-f file_path]")
            email_key = input("Email-id linked to public key: ")
            file_path = input("File path for encryption: ")
            obj.encrypt(email_key, file_path)
            print("[+] File encrypted!")

        elif inp == 3:
            print("[+] Specify [-n new_name_file] [-f file_path]")
            new_name = input("Set name of the file: ")
            file_path = input("File path for decryption: ")
            obj.decrypt(new_name, file_path)
            print("File Decrypted!")

        elif inp == 4:
            print("[+] Specify [-s sender_email] [-p pswd] [-r receiver_email] [-a email_id_public_key] [-n name_of_file.asc]")
            sender = input("Specify email address of sender: ")
            password = input("Specify Password of email address: ")
            receiver = input("Specify Email address of receiver: ")
            email_key = input("Email-id linked to public key: ")
            file_name = input("Set name of the file: ")
            obj.send_email(sender, password, receiver, email_key, file_name)

        elif inp == 5:
            exit()

        else:
            print("[-] Invalid selection")


obj_exe = Execute()
obj_exe.instruction()
obj_exe.execute()
