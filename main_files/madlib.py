template= """Once upon a time in a {place}, there lived a {adjective} {animal}. 
It loved to {verb1} every day. One day, it met a {color} {object}. 
They became {adverb} friends and lived {adverb2} ever after."""

place = input("Enter a place: ").title()
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ").title()
verb1 = input("Enter a verb: ")
color = input("Enter a color: ")
object = input("Enter an object: ")
adverb = input("Enter an adverb: ")
adverb2 = input("Enter an adverb: ")

filled_story = template.format(place=place, adjective=adjective, animal=animal, verb1=verb1, color=color, object=object, adverb=adverb, adverb2=adverb2)

print("\nHere's your Madlib Story:")
print(filled_story)