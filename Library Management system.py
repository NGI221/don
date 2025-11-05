members = {
    'Prashant': {'Ram Charitra ': 2, 'Krishna Charitra ': 0, 'Vishnu Charitra ': 1},
    'Om': {'Ram Charitra ': 0, 'Krishna Charitra ': 1, 'Vishnu Charitra ': 0},
    'Sanskruti': {'Ram Charitra ': 3, 'Krishna Charitra ': 1, 'Vishnu Charitra ': 2},
    ' Pramod': {'Ram Charitra ': 0, 'Krishna Charitra ': 0, 'Vishnu Charitra ': 0},
}

from collections import defaultdict, Counter

def average_books_borrowed(members):
    total_books = 0
    member_count = len(members)
    for borrowings in members.values():
        total_books += sum(borrowings.values())
    return total_books / member_count if member_count > 0 else 0


def book_borrow_counts(members):
    counts = defaultdict(int)
    for borrowings in members.values():
        for book, count in borrowings.items():
            counts[book] += count
    max_book = max(counts, key=counts.get)
    min_book = min(counts, key=counts.get)
    return max_book, counts[max_book], min_book, counts[min_book]

def count_inactive_members(members):
    inactive = 0
    for borrowings in members.values():
        if sum(borrowings.values()) == 0:
            inactive += 1
    return inactive

def mode_borrowed_book(members):
    counts = defaultdict(int)
    for borrowings in members.values():
        for book, count in borrowings.items():
            counts[book] += count
    freq_counts = Counter(counts.values())
    mode_count = freq_counts.most_common(1)[0][0]
    mode_books = [book for book, count in counts.items() if count == mode_count]
    return mode_books, mode_count

print("Average books borrowed:", average_books_borrowed(members))
max_book, max_count, min_book, min_count = book_borrow_counts(members)
print("Highest borrowed book:", max_book, "with", max_count, "borrowings")
print("Lowest borrowed book:", min_book, "with", min_count, "borrowings")
print("Inactive members (borrow count 0):", count_inactive_members(members))
mode_books, mode_count = mode_borrowed_book(members)
print("Most frequently borrowed book(s):", mode_books, "with borrow count:", mode_count)