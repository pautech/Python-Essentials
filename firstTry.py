# Create New Python File
#2. The user will input 6 information (3 nouns and 3 adjectives)
#3. Search for any poem or song on the internet
#4. Replace the poem or song lyrics string with the nouns and adjectives from user's input.
#5. Display the original song and poem and display the result (nouns and adjectives
#must be in all caps)

noun1=input("Enter First Noun: ")
noun2=input("Enter Second Noun: ")
noun3=input("Enter Third Noun: ")

adjective1=input("Enter First Adjective: ")
adjective2=input("Enter Second Adjective: ")
adjective3=input("Enter Third Adjective: ")


print("This is the original Poem ")
print("\n")
print("This is the field where the battle did not happen,")
print("where the unknown soldier did not die.")
print("This is the field where grass joined hands,")
print("where no monument stands,")
print ("and the only heroic thing is the sky.")
print("\n")
print("Birds fly here without any sound,")
print("unfolding their wings across the open.")
print("No people killed—or were killed—on this ground")
print("hallowed by neglect and an air so tame")
print("that people celebrate it by forgetting its name.")

print("This is the Modified Poem ")
print("\n")
print("This is the field where the battle did not happen,")
print("where the unknown ",noun1.upper+"did not die.")
print("This is the field where ",noun2.upper +" joined hands,")
print("where no monument stands,")
print ("and the only ",adjective2.upper+" thing is the sky.")
print("\n")
print(noun3.upper+"fly here without any sound,")
print("unfolding their wings across the open.")
print("No people killed—or were killed—on this ground")
print("hallowed by neglect and an air so ",adjective3.upper)
print("that people",adjective1.upper+" it by forgetting its name.")