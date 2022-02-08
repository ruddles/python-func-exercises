# Write a filter call that filters out passwords less than 9 chars
passwords = ["short", "thisIsAL0ngPass", "tiny", "password", "password1"]
allowed_passwords = filter(lambda password: len(password) > 8, passwords)
print(list(allowed_passwords))  # expected ['thisIsAL0ngPass', 'password1']
