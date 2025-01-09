emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

spam_emails = set(emails_received) & set(spam_list)  # Intersection
print("Spam emails:", spam_emails)