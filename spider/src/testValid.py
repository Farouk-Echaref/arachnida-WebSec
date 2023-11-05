import validators


validation = validators.url("http:/www.google.com")

if validation:

print("URL is valid")

else:

print("URL is invalid")