from utility import get_tickets, format_ticket, ThreadWithReturnValue
import json

def get_write_tickets():
    # Request all tickets and store into a JSON file 
    tickets_thread = ThreadWithReturnValue(target=get_tickets)
    tickets_thread.start()
    user_input = input('Hello There! \nWelcome to the Zendesk Ticket Viewer\nPress enter to continue...\n or type "q" to exit\n')
    if user_input != 'q':
        if tickets_thread.is_alive():
            print("Please wait, currently loading tickets...")
        tickets = tickets_thread.join()
        with open(f"my_tickets.json", "w") as outfile: 
            outfile.write(tickets)
    else: 
        quit("Goodbye!")
    return user_input

def main(): 
    user_input = get_write_tickets()

    # Reads ticket subjects from the JSON file in batches of 25
    page = 1
    while user_input != 'q':
        with open(f"my_tickets.json", "r") as infile:
            tickets = json.load(infile)
        
        for i in range((page-1)*25, page*25):
            print(f"{i+1}. {tickets[i]['subject']}")
        print("You are on page ", page)
        valid_input = False
        while not valid_input:
            user_input = input("Select a ticket by typing in its number \n type > or < to go to the next or previous page \n type 'q' to exit. \n")
            if user_input == '>' and page < len(tickets)//25:
                page += 1
                valid_input = True
            elif user_input == '<' and page >1:
                page -= 1
                valid_input = True
            elif user_input == '>' and page == len(tickets)//25:
                print("You are already on the last page")
            elif user_input == '<' and page == 1:
                print("You are already on the first page")
            elif user_input == "q":
                quit("Goodbye!")
            elif user_input.isnumeric(): 
                if int(user_input) <= len(tickets) and int(user_input) > 0:
                    print(f"You selected ticket {user_input}")
                    print(json.dumps(format_ticket(int(user_input)-1, tickets), indent=4))
                    input("Press Enter to continue \n")
                else:
                    print("That is not a valid ticket number")
            elif user_input.isalpha():
                print("That is not a valid command")
    quit("Goodbye")

if __name__ == '__main__':
    main()
    