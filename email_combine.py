contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

merged_contacts = set(contacts_A) | set(contacts_B)  # Union
print("Merged contacts:", merged_contacts)