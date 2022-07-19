"""
This is week 2 of the Python Bootcamp for Data assignment. All of your questions
for this week will come commented out.
To pass, all automated testing of your inputs have to pass their tests.
"""


# This function has a syntax error, no tests will run until this function is
# fixed first
#def invalid(prefix="https", domain):
#    pass


# The following function needs to use variable arguments to work. The developer
# created this function with a single argument which is breaking the tests. We
# need this function to change to allow any number of arguments
def create_urls(domains):
    return [f"https://{domain}/" for domain in domains]


# This function creates a dictionary based on the arguments passed in. The
# `metadata` argument is expected to be a dictionary and the `username`
# argument to be a string. Update the function so that:
# - It accepts a new keyword argument named `verified` which default to `False`
# - Changes `metadata` argument to be a variable keyword argument
def social_media_user(username, metadata):
    information = {
        "username": username,
        "verified": False
    }

    information.update(metadata)
    return information


# This class has a problem with the `as_celsius` method. Update the class so
# that the method works correctly and the test passes
class Fahrenheit:

    def __init__(self, value):
        self.value = value

    def as_celsius():
        return (self.value - 32) / 1.8


# The two social media classes have a `verified` and `url` methods
# that can come from a base class instead.
# Update the classes so that:
# - They both inherit from a base class (you must create a new one)
# - The `verified` and `url` methods come from the base class

class TwitterUser:

    domain = "https://twitter.com"

    def __init__(self, username):
        self.username = username

    def url(self):
        return f"{self.domain}/{self.username}"

    def verified(self):
        if self.username:
            return True
        return False


class LinkedInUser:

    domain = "https://linkedin.com/in"

    def __init__(self, username):
        self.username = username

    def url(self):
        return f"{self.domain}/{self.username}"

    def verified(self):
        if self.username:
            return True
        return False
