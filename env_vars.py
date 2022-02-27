import os
db_user = os.environ.get('EMAIL_USER')
db_password = os.environ.get('EMAIL_PASS')

print(db_user)
print(db_password)
