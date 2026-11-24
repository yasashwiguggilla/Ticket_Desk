from sample_data import SAMPLE_DATA


class Ticket:
    def __init__(self, ticket_id, title, description, priority="medium", status="open"):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def describe(self):
        return f"#{self.id} [{self.priority}] {self.title} ({self.status})"


def make_sample_tickets():
    tickets = []

    for data in SAMPLE_DATA:
        ticket = Ticket(
            data["id"],
            data["title"],
            data["description"],
            data["priority"],
            data["status"]
        )
        tickets.append(ticket)

    return tickets


def print_tickets(tickets):
    for ticket in tickets:
        print(ticket.describe())
def find_by_id(tickets, ticket_id):
    for ticket in tickets:
        if ticket.id == ticket_id:
            return ticket

    return None
def add_ticket(tickets, title, description, priority="medium"):
    if tickets:
        next_id = max(ticket.id for ticket in tickets) + 1
    else:
        next_id = 1

    ticket = Ticket(next_id, title, description, priority, "open")
    tickets.append(ticket)

    return ticket