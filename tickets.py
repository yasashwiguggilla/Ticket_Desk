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
def filter_by_status(tickets, status):
    result = []

    for ticket in tickets:
        if ticket.status == status:
            result.append(ticket)

    return result


def filter_by_priority(tickets, priority):
    result = []

    for ticket in tickets:
        if ticket.priority == priority:
            result.append(ticket)

    return result


def search_title(tickets, word):
    result = []

    word = word.lower()

    for ticket in tickets:
        if word in ticket.title.lower():
            result.append(ticket)

    return result


def sort_by_priority(tickets):
    priority_order = {
        "high": 0,
        "medium": 1,
        "low": 2
    }

    result = sorted(
        tickets,
        key=lambda ticket: (priority_order[ticket.priority], ticket.id)
    )

    return result


def count_by_status(tickets):
    counts = {}

    for ticket in tickets:
        counts[ticket.status] = counts.get(ticket.status, 0) + 1

    return counts


def summary_lines(tickets):
    counts = count_by_status(tickets)

    statuses = ["open", "in_progress", "resolved", "closed"]

    result = []

    for status in statuses:
        result.append(f"{status}: {counts.get(status, 0)}")

    return result