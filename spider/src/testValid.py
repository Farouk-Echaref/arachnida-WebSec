#!/usr/bin/python3
import validators


validation = validators.url("images.unsplash.com/photo-1696075619078-6cb640d329ec?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw3fHx8ZW58MHx8fHx8")

if validation:
    print("URL is valid")
else:
    print("URL is invalid")