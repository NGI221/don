from collections import deque

event_queue = deque()

def add_event(event):
    event_queue.append(event)
    print(f"Event '{event}' added to the queue.")

def process_next_event():
    if event_queue:
        event = event_queue.popleft()
        print(f"Processed event: {event}")
    else:
        print("No events to process.")

def display_pending_events():
    if event_queue:
        print("Pending events in queue:")
        for e in event_queue:
            print("-", e)
    else:
        print("No pending events.")

def cancel_event(event):
    try:
        event_queue.remove(event)
        print(f"Event '{event}' canceled.")
    except ValueError:
        print(f"Event '{event}' not found or already processed.")

# Interactive CLI
while True:
    print("\nChoose operation: 1) Add Event 2) Process Next Event 3) Display Pending Events 4) Cancel Event 5) Exit")
    choice = input("Enter choice number: ").strip()
    if choice == '1':
        event = input("Enter event description: ")
        add_event(event)
    elif choice == '2':
        process_next_event()
    elif choice == '3':
        display_pending_events()
    elif choice == '4':
        event = input("Enter event description to cancel: ")
        cancel_event(event)
    elif choice == '5':
        print("Exiting event processing system.")
        break
    else:
        print("Invalid choice. Try again.")
