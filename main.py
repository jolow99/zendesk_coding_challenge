from utility import get_tickets, format_ticket, ThreadWithReturnValue
import json

if __name__ == '__main__':
    # Introduction
    tickets_thread = ThreadWithReturnValue(target=get_tickets)
    tickets_thread.start()
    print("Hello there! Welcome to the Zendesk Ticket Viewer")
    print("---Please type any key to input---")
    print("---Type 'q' to exit the program---")
    user_input = input()
    
    # Request all tickets and store into a JSON file 
    if user_input != 'q':
        tickets = tickets_thread.join()
        with open(f"my_tickets.json", "w") as outfile: 
            outfile.write(tickets)

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
                elif user_input == 'q':
                    quit()
                elif user_input.isnumeric(): 
                    if int(user_input) <= len(tickets) and int(user_input) > 0:
                        print(f"You selected ticket {user_input}")
                        print(json.dumps(format_ticket(int(user_input)-1, tickets), indent=4))
                        input("Type any key to continue \n")
                    else:
                        print("That is not a valid ticket number")
                elif user_input.isalpha():
                    print("That is not a valid command")
    print("Goodbye!")
    quit()