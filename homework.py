#greeting = input("Hello, possible pirate! What's the password?")
#if "rrr" in greeting:
#	print("Go away, pirate.")
#else:
#    print("Greetings, hater of pirates!")

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

#authors = {
#    "Charles Dickens": "1870",
#    "William Thackeray": "1863",
#    "Anthony Trollope": "1882",
#    "Gerard Manley Hopkins": "1889"
#}
#for (author, date) in authors.items():
#    print(author + " died in " + date)

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#year = input("Greetings! What is your year of origin? ")

#if int(year) <= 1900:
#    print ("Woah, that's the past!")
#elif int(year) > 2020:
#    print ("Far out, that's the future!!")
#else:
#    print ("That's totally the present!")

    # Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".
#phrase = " The quick brown fox jumped over the lazy dog "
#wordlist = phrase.split()
#current_longest = wordlist[0]
#for word in wordlist:
#    if int(len(word)) > int(len(current_longest)):
#        current_longest = word
#print(current_longest + " is " + str(len(current_longest)) + " characters long.")

years = (0, 100)
population = [0,10]
for i in range(years):
    population.append = population[-1] + population[-2]
print(population)
