#https://www.youtube.com/watch?v=d0o89z134CQ

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-3")


def zero_shot_class_domestic_international(user_input):
    candidate_labels = ['domestic', 'international', 'other']
    result = classifier(user_input, candidate_labels)
    return result['labels'][0]

domestic_maths = []
with open("domestic_maths.txt") as file:
    for line in file:
        if line[0:2] == "- ":
            domestic_maths.append(line.lstrip("- ").rstrip())

def zero_shot_class_domestic_maths(user_input):
    candidate_labels = domestic_maths
    result = classifier(user_input, candidate_labels)
    return result['labels'][0]

calc_category_dict = {'VCE Further Mathematics': 'pre-calculus', 'HSC General Mathematics': 'pre-calculus', 'TAS General Mathematics': 'pre-calculus', 'QCE General Mathematics': 'pre-calculus', 'SACE Mathematics': 'pre-calculus', 'NTCET Mathematics': 'pre-calculus', 'ACT Mathematical Applications': 'pre-calculus', 'WACE Mathematical Applications': 'pre-calculus', 'IB Applications and Interpretation SL': 'pre-calculus', 'VCE Mathematical Methods': 'calculus ready', 'QCE Mathematical Methods': 'calculus ready', 'SACE Mathematical Methods': 'calculus ready', 'NTCET Mathematical Methods': 'calculus ready', 'ACT Mathematical Methods': 'calculus ready', 'WACE Mathematical Methods': 'calculus ready', 'TAS Mathematical Methods': 'calculus ready', 'HSC Mathematics Advanced': 'calculus ready', 'IB Analysis and Approaches SL': 'calculus ready', 'IB Applications and Interpretation HL': 'calculus ready', 'NCEA Level 3 Calculus': 'calculus ready', 'VCE Specialist Mathematics': 'extended calculus', 'QCE Specialist Mathematics': 'extended calculus', 'SACE Specialist Mathematics': 'extended calculus', 'NTCET Specialist Mathematics': 'extended calculus', 'ACT Specialist Mathematics': 'extended calculus', 'WACE Mathematics Specialist': 'extended calculus', 'TAS Mathematics Specialised': 'extended calculus', 'HSC Extension 1': 'extended calculus', 'HSC Extension 2': 'extended calculus', 'IB Analysis and Approaches HL': 'extended calculus', 'NCEA Scholarship Calculus': 'extended calculus'}

all_majors_str = ""
with open("all_majors.txt") as file:
    for index, line in enumerate(file):
        if index in [0, 1]:
            continue
        all_majors_str += line

all_majors_categories = []
with open("all_majors.txt") as file:
    for line in file:
        if line[0:2] == "- ":
            all_majors_categories.append(line.lstrip("- ").rstrip())

def zero_shot_class_major(user_input):
    candidate_labels = all_majors_categories
    result = classifier(user_input, candidate_labels)
    return result['labels'][0]

calculus_background_text = """Based on the course you have taken in high school you have been placed into the {} category
Then, ask the user: "Alternatively, if you would like to check your allocation, you can use our Calculus Checker, and answer a few questions to determine your maths background.
Answer with either:
- I am happy with the current allocation
- I would like to be allocated using the Calculus Checker"""

relevant_units = """Here are units relevant to {major} that you can take without further bridging materials:
{satified_units}
Your Calculus Background of extended calculus satisfies the requirements for {major}. The mathematics units you will need to take are:
{all_units}
The terminology used for required units is:

NR: Not Strictly Required but Highly Recommended
A: Advanced
SSP: Special Studies Program
If you would like to look at the Support Pathway/requirements for a different degree please answer with another degree name. Feel free to ask further questions if you need clarification. Some examples might be:

Try typing: I'd like more information on Physics
When do I need to take these units?
Can I have further unit descriptions of required units?"""

req_units = {}
with open("all_units_for_majors.txt") as file:
    for line in file:
        next_line = 0
        vals = line.split(":")
        #print(len(vals))
        #print(vals)
        units_clean = []
        for index, units in enumerate(vals[1:]):
            for idx, unit in enumerate(units.split(", ")):
                unit_stripped = unit.lstrip().rstrip()
                calc_level = {}

                if unit_stripped == "pre-calculus/calculus ready": #in other use if dict.keys == None
                    calc_level_units = []
                    for j in vals[index + 2].split(","):
                        x = j.lstrip().rstrip(". extended calculus")
                        calc_level_units.append(x)
                    calc_level["pre-calculus"] = calc_level_units
                    calc_level["calculus ready"] = calc_level_units
                    calc_level_units = []
                    for k in vals[index + 3].split(","):
                        x = k.lstrip().rstrip()
                        calc_level_units.append(x)
                    calc_level["extended calculus"] = calc_level_units
                    #print(calc_level)
                    req_units[vals[0]] = calc_level
                    next_line = 1
                    break
                else:
                    units_clean.append(unit_stripped)   
                    req_units[vals[0]] = units_clean
            if next_line == 1:
                break
#print(req_units)

units_with_calc_category = {}
with open("units_with_calc_level.txt") as file:
    category = ""
    for index, line in enumerate(file):
        if index % 2 == 0:
            category = line.lstrip("- ")
            category = category[:-9].lower()
        else:
            ls = []
            for unit in line.split(", "):
                ls.append(unit.lstrip().rstrip())
            units_with_calc_category[category] = ls
#print(units_with_calc_category)

def units_without_bridging(clean_user_input, calculus_category):
    all_calc_level_units = units_with_calc_category[calculus_category]
    major_req_units = req_units[clean_user_input]
    units = []
    for unit in all_calc_level_units:
        for req_unit in major_req_units:
            if unit in req_unit:
                units.append(unit)
    return units

def all_units_for_major(clean_user_input):
    major_req_units = req_units[clean_user_input]
    return major_req_units
#could be prompt engineering
template = """ 
You are an Academic Advisor, specializing in mathematics, 
at the University of Sydney. 
The user is a Year 12 student who needs advice on what 
mathematic pathways to take for a given degree and their 
mathematical background.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    step = 0
    calculus_category = "pre-calculus"
    major = "Physics"
    context = ""
    print("I am the Maths Advice Bot (MAB) and I am here to advise you on choosing first year maths units at the University of Sydney, and any maths support you might need.\nTry starting with 'Hi, I need some help choosing my first year maths units'.")
    user_input = input("You : ") #Should be "Hi, I need some help choosing my first year maths units"
    print("Hi! I'm happy to help! I will get some information on your maths background and degree aspirations, then I can show you any maths support you might need if you do not meet the assumed knowledge any of the units you need to complete for your degree. Let's get started!\nAre you an International Student or a Domestic Student? (If you are a NZ student please answer with Domestic)")
    step = 1
    while True:
        if step == 1:
            user_input = input("You : ")
            if user_input.lower() == "domestic" or user_input.lower() == "international":
                user_output_label = user_input.lower()
                print("cool")
            else:
                #zero shot model classification
                user_output_label = zero_shot_class_domestic_international(user_input.lower())
                print(user_output_label)
            if user_output_label == "domestic":
                step = 2
            elif user_output_label == "international":
                step = 3
            elif user_output_label == "other":
                #LLM to output something on its own accord
                pass
        elif step == 2:
            print("What mathematics course did you complete in Year 12? Please answer with the name of the mathematics course. E.g 'HSC Mathematics Extension 1'")
            user_input = input("You : ")
            if user_input.lower() in domestic_maths:
                pass
            else:
                user_output_label = zero_shot_class_domestic_maths(user_input.lower())
                print(user_output_label)
            calculus_category = calc_category_dict[user_output_label]
            print(calculus_background_text.format(calculus_category))
            user_input = input("You : ")
            if user_input == "I am happy with the current allocation":
                step = 4
            elif user_input == "I would like to be allocated using the Calculus Checker": #NEED TO DO Zero shot here
                step = 3
        elif step == 3:
            print("We will use a quick quiz to determine your calculus knowledge. This is not a test, but to know a little bit more about your maths background.\nThis will be done using Qualtrics. Link: https://sydney.au1.qualtrics.com/jfe/form/SV_1AYHXErsa1NHMLI After you complete the quiz, please state your categorisation of either pre-calculus, calculus ready, or extended calculus")
            break
        elif step == 4:
            print("Next we will look at what degree or pathway you are interested at the University of Sydney. Here is a list of degrees/pathways/majors available in the Faculty of Science , Business and Economics, each with their calculus requirement. Note there is support pathways for courses in which your calculus background doesnt fill the requirements for.\n")
            print(all_majors_str)
            user_input = input("You : ")
            if user_input in all_majors_categories:
                major_label = user_input
            else:
                major_label = zero_shot_class_major(user_input)
                print(major_label)
            major = major_label
            step = 5
        elif step == 5:
            units_without_bridging_output = units_without_bridging(major_label, calculus_category)
            units_without_bridging_output_str = ""
            for unit in units_without_bridging_output:
                units_without_bridging_output_str += "- {}\n".format(unit)
            
            all_units_major_output = all_units_for_major(major_label)
            all_units_major_output_str = ""
            for unit in all_units_major_output:
                all_units_major_output_str += "- {}\n".format(unit)
            print(relevant_units.format(major = major, satified_units = units_without_bridging_output_str, all_units = all_units_major_output_str))
            break

        
        # user_input = input("You : ")
        # if user_input.lower() == 'exit':
        #     break

        # result = chain.invoke({"context": context, "question": user_input})
        # print("Bot: ", result)
        # context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()

