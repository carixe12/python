import time

CHAT_FILE = 'chat.txt'

def get_username():
    username = input("Enter your username: ")
    return username.strip()

def view_chat():
    print("----- Chat -----")
    with open(CHAT_FILE, 'r') as file:
        print(file.read())

def send_message(username):
    message = input("Enter your message: ")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    formatted_message = f"[{timestamp}] {username}: {message}\n"

    with open(CHAT_FILE, 'a') as file:
        file.write(formatted_message)

    print("Message sent successfully!")

def main():
    username = get_username()

    while True:
        print("\nActions:")
        print("1. View chat")
        print("2. Send message")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_chat()
        elif choice == '2':
            send_message(username)
        elif choice == '3':
            print("Exiting the chat.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()