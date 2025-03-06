time_of_day=input("time of day:  ")
name=input("name:  ")
verb1=input("verb: ")
feild=input("field of study:  " )
abstract_noun1=input("abstract noun:  ")
number=input("numbers:   ")
skill_profession=input("skill or profession: " )
job_title=input("job title:   ")
company= input ("company or organization:   ")
verb2=input("verb ending in -ing:  ")
challenges=input(" problem or challenge:   ")
adjective1=input("adjective:   ")
adjective2=input("adjective:   ")
abstract_noun2=input("abstract noun:  ")
verb3=input("verb:")
adjective3=input("adjective:   ")

 
madlib =  f"Good {time_of_day},\
My name is {name}, and I am honored to {verb1}with you today.\
With a background in {feild}and a passion for {abstract_noun1}, \
I have dedicated {number} years to refining my expertise in {skill_profession}.\
Currently, I serve as a {job_title} at {company}, where I focus on \
{verb2} innovative solutions to {challenges}.\
My work revolves around {adjective1} thinking, {adjective2}collaboration, \
and a commitment to {abstract_noun2}.\
I am eager to {verb3} and exchange ideas with all of you. \
Thank you for this opportunity, and I look forward to a {adjective3}discussion ahead!"


print(madlib)
