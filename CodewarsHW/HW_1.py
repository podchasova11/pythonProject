#  № 1 Create a method that takes as input a name,
#  city, and state to welcome a person.
#  Note that name will be an array consisting of one
#  or more values that should be joined together with
#  one space between each, and the length of the name
#  array in test cases will vary.
#
# Example:
#
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

# name = ['John', 'Smith']
# print(f"Hello, {name[0]} {name[1]}! Welcome to Phoenix, Arizona!")

#  № 2 Jenny has written a function that returns a greeting for a user.
#  However, she's in love with Johnny, and would like to greet him slightly different.
#  She added a special case to her function, but she made a mistake.
#
# Can you help her?

import codewars_test as test
from solution import say_hello

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'), 'Hello, John Smith! Welcome to Phoenix, Arizona!')
        test.assert_equals(say_hello(['Franklin','Delano','Roosevelt'], 'Chicago', 'Illinois'), 'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!')
        test.assert_equals(say_hello(['Wallace','Russel','Osbourne'],'Albany','New York'), 'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')
        test.assert_equals(say_hello(['Lupin','the','Third'],'Los Angeles','California'), 'Hello, Lupin the Third! Welcome to Los Angeles, California!')
        test.assert_equals(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'), 'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!')


