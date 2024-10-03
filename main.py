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

calc_category_dict = {'VCE Further Mathematics': 'Pre-Calculus', 'HSC General Mathematics': 'Pre-Calculus', 'TAS General Mathematics': 'Pre-Calculus', 'QCE General Mathematics': 'Pre-Calculus', 'SACE Mathematics': 'Pre-Calculus', 'NTCET Mathematics': 'Pre-Calculus', 'ACT Mathematical Applications': 'Pre-Calculus', 'WACE Mathematical Applications': 'Pre-Calculus', 'IB Applications and Interpretation SL': 'Pre-Calculus', 'VCE Mathematical Methods': 'Calculus Ready', 'QCE Mathematical Methods': 'Calculus Ready', 'SACE Mathematical Methods': 'Calculus Ready', 'NTCET Mathematical Methods': 'Calculus Ready', 'ACT Mathematical Methods': 'Calculus Ready', 'WACE Mathematical Methods': 'Calculus Ready', 'TAS Mathematical Methods': 'Calculus Ready', 'HSC Mathematics Advanced': 'Calculus Ready', 'IB Analysis and Approaches SL': 'Calculus Ready', 'IB Applications and Interpretation HL': 'Calculus Ready', 'NCEA Level 3 Calculus': 'Calculus Ready', 'VCE Specialist Mathematics': 'Extended Calculus', 'QCE Specialist Mathematics': 'Extended Calculus', 'SACE Specialist Mathematics': 'Extended Calculus', 'NTCET Specialist Mathematics': 'Extended Calculus', 'ACT Specialist Mathematics': 'Extended Calculus', 'WACE Mathematics Specialist': 'Extended Calculus', 'TAS Mathematics Specialised': 'Extended Calculus', 'HSC Extension 1': 'Extended Calculus', 'HSC Extension 2': 'Extended Calculus', 'IB Analysis and Approaches HL': 'Extended Calculus', 'NCEA Scholarship Calculus': 'Extended Calculus'}

all_majors_str = ""
with open("all_majors.txt") as file:
    for index, line in enumerate(file):
        all_majors_str += line

all_majors_categories = ['Psychology', 'Psychological Sciences', 'Anatomy and Histology', 'Animal Health and Veterinary Bioscience', 'Animal Health, Disease and Welfare', 'Animal Production', 'Applied Medical Science', 'Biology', 'Ecology & Evolutionary Biology', 'Environmental Science', 'Environmental Studies', 'Food Science', 'Genetics and Genomics', 'Geography', 'Health', 'History & Philosophy', 'Human Movement', 'Immunology and Pathology', 'Infectious Diseases', 'Life Sciences', 'Medical Science', 'Neuroscience', 'Nutrition and Dietetics', 'Nutrition Science', 'Pharmacology', 'Physiology', 'Plant Production', 'Soil Science and Hydrology', 'Taronga Wildlife Conservation', 'Chemistry', 'Agricultural Science', 'Geology and Geophysics', 'Medicinal Chemistry', 'Data Science', 'Discrete Mathematics and Algorithms', 'Microbiology', 'Marine Science', 'Physics', 'Nanoscience & Nanotechnology', 'Computer Science', 'Software Development', 'Statistics', 'Mathematics', 'Financial Mathematics and Statistics', 'Mathematical Modelling and Computation', 'Mathematical Sciences"', 'Economics', 'Environmental, Agricultural and Resource Economics', 'Financial Economics', 'Econometrics', 'Accounting', 'Finance', 'Banking', 'Business Analytics']
all_levels_majors = {'Psychology': 'Pre-Calculus', 'Psychological Sciences': 'Pre-Calculus', 'Anatomy and Histology': 'Pre-Calculus', 'Animal Health and Veterinary Bioscience': 'Pre-Calculus', 'Animal Health, Disease and Welfare': 'Pre-Calculus', 'Animal Production': 'Pre-Calculus', 'Applied Medical Science': 'Pre-Calculus', 'Biology': 'Pre-Calculus', 'Ecology & Evolutionary Biology': 'Pre-Calculus', 'Environmental Science': 'Pre-Calculus', 'Environmental Studies': 'Pre-Calculus', 'Food Science': 'Pre-Calculus', 'Genetics and Genomics': 'Pre-Calculus', 'Geography': 'Pre-Calculus', 'Health': 'Pre-Calculus', 'History & Philosophy': 'Pre-Calculus', 'Human Movement': 'Pre-Calculus', 'Immunology and Pathology': 'Pre-Calculus', 'Infectious Diseases': 'Pre-Calculus', 'Life Sciences': 'Pre-Calculus', 'Medical Science': 'Pre-Calculus', 'Neuroscience': 'Pre-Calculus', 'Nutrition and Dietetics': 'Pre-Calculus', 'Nutrition Science': 'Pre-Calculus', 'Pharmacology': 'Pre-Calculus', 'Physiology': 'Pre-Calculus', 'Plant Production': 'Pre-Calculus', 'Soil Science and Hydrology': 'Pre-Calculus', 'Taronga Wildlife Conservation': 'Pre-Calculus', 'Chemistry': 'Calculus Ready', 'Agricultural Science': 'Calculus Ready', 'Geology and Geophysics': 'Calculus Ready', 'Medicinal Chemistry': 'Calculus Ready', 'Data Science': 'Calculus Ready', 'Discrete Mathematics and Algorithms': 'Calculus Ready', 'Microbiology': 'Calculus Ready', 'Marine Science': 'Calculus Ready', 'Physics': 'Extended Calculus', 'Nanoscience & Nanotechnology': 'Extended Calculus', 'Computer Science': 'Extended Calculus', 'Software Development': 'Extended Calculus', 'Statistics': 'Extended Calculus', 'Mathematics': 'Extended Calculus', 'Financial Mathematics and Statistics': 'Extended Calculus', 'Mathematical Modelling and Computation': 'Extended Calculus', 'Mathematical Sciences': 'Extended Calculus', 'Economics': 'Calculus Ready', 'Environmental, Agricultural and Resource Economics': 'Calculus Ready', 'Financial Economics': 'Calculus Ready', 'Econometrics': 'Calculus Ready', 'Accounting': 'Pre-Calculus', 'Finance': 'Calculus Ready', 'Banking': 'Calculus Ready', 'Business Analytics': 'Calculus Ready'}
req_units = {'Agricultural Science': ['ENVX1002', 'ENVX2001'], 'Anatomy and Histology': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Animal and Veterinary Biosciences': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Animal Health, Disease and Welfare': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Animal Production': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Applied Medical Science': ['DATA1001(NR)'], 'Astrophysics': ['MATH1061/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062(NR)/MATH1962(A)(NR)/MATH1972(SSP)(NR)'], 'Biochemistry and Molecular Biology': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Biology': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Chemistry': ['Pre-Calculus/Calculus Ready', 'MATH1050', 'DATA1001/DATA1901(A). Extended Calculus', 'MATH1061(NR)/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062(NR)/MATH1962(A)(NR)/MATH1972(SSP)(NR)'], 'Computer Science': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1064/MATH1964(A)', 'DATA1001/DATA1901(A)'], 'Data Science': ['DATA1001/(DATA1901(A))', 'MATH1061(NR)/MATH1961(A)(NR)/MATH1971(SSP)(NR)'], 'Discrete Mathematics and Algorithms': ['MATH1064/MATH1964(A)', 'MATH1061(NR)/MATH1961(A)(NR)/MATH1971(SSP)(NR)'], 'Ecology and Evolutionary Biology': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Environmental Science': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Environmental Studies': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Financial Mathematics and Statistics': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1062/MATH1962(A)/MATH1972(SSP)'], 'Food Science': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Genetics and Genomics': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Geography': ['DATA1001(NR)'], 'Geology and Geophysics': ['DATA1001/DATA1901(A)', 'MATH1050(NR)'], 'Health': ['DATA1001(NR)', 'SCIE1001(NR)'], 'History and Philosophy of Science': ['SCIE1001(NR)'], 'Human Movement': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Immunology and Pathology': ['DATA1001(NR)'], 'Infectious Diseases': ['DATA1001(NR)'], 'Life Sciences': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Marine Science': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Mathematical Sciences': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1062/MATH1962(A)/MATH1972(SSP)'], 'Mathematics': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1062/MATH1962(A)/MATH1972(SSP)'], 'Medical Science': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Medicinal Chemistry': ['Pre-Calculus/Calculus Ready', 'MATH1050', 'DATA1001/DATA1901(A). Extended Calculus', 'MATH1061(NR)/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062(NR)/MATH1962(A)(NR)/MATH1972(SSP)(NR)'], 'Microbiology': ['Pre-Calculus/Calculus Ready', 'MATH1050', 'DATA1001/DATA1901(A). Extended Calculus', 'MATH1061(NR)/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062(NR)/MATH1962(A)(NR)/(MATH1972(SSP)(NR)'], 'Neuroscience': ['DATA1001(NR)'], 'Nutrition and Dietetics': ['DATA1001(NR)'], 'Nutrition Science': ['DATA1001(NR)'], 'Pharmacology': ['MATH1050', 'DATA1001(NR)'], 'Physics': ['MATH1061/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062/MATH1962(A)(NR)/MATH1972(SSP)(NR)', 'MATH2021/MATH2921(A)(NR)'], 'Physiology': ['DATA1001(NR)'], 'Plant Production': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Plant Science': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Psychology': ['DATA1001/DATA1901(A)', 'PSYC1001', 'PSYC1002', 'PSYC2012'], 'Psychological Science': ['PSYC1001', 'PSYC1002', 'PSYC2012', 'DATA1001(NR)/DATA1901(A)(NR)'], 'Software Development': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1064/MATH1964(A)'], 'Soil Science and Hydrology': ['DATA1001(NR)', 'SCIE1001(NR)'], 'Statistics': ['MATH1061/MATH1961/MATH1971(SSP)', 'MATH1062/(MATH1962(A))/MATH1972(SSP)', 'DATA1001/DATA1901(A)'], 'Taronga Wildlife Conservation': ['ENVX1002', 'ENVX2001'], 'Nanoscience & Nanotechnology': ['MATH1061/MATH1961(A)(NR)/MATH1971(SSP)(NR)', 'MATH1062/MATH1962(A)(NR)/MATH1972(SSP)(NR)', 'MATH2021/MATH2921(A)(NR)'], 'Mathematical Modelling and Computation': ['MATH1061/MATH1961(A)/MATH1971(SSP)', 'MATH1062/MATH1962(A)/MATH1972(SSP)'], 'Environmental, Agricultural and Resource Economics': ['ECON1001', 'ECON1003(NR)'], 'Financial Economics': ['ECON1001', 'ECON1003(NR)', 'ECMT1010'], 'Economics': ['ECON1001', 'ECON1003(NR)'], 'Econometrics': ['ECMT1010', 'ECON1003(NR)'], 'Finance': ['BUSS1040', 'BUSS1020'], 'Banking': ['BUSS1040', 'BUSS1020'], 'Business Analytics': ['BUSS1020', 'QBUS1040']}
calc_level_dict = {'Pre-Calculus' : 0, 'Calculus Ready': 1, 'Extended Calculus': 2}
units_with_calc_category = {'Pre-Calculus': ['DATA1001', 'MATH1111', 'DATA1901', 'ENVX1002', 'ECON1003', 'PSYC1001', 'PSYC1002', 'PSYC2012'], 'Calculus Ready': ['MATH1050', 'MATH1064', 'DATA1001', 'MATH1111', 'DATA1901', 'QBUS1040', 'ECON1003', 'ECON1001', 'ECMT1010', 'BUSS1020', 'BUSS1040', 'ENVX1002', 'PSYC1001', 'PSYC1002', 'PSYC2012'], 'Extended Calculus': ['MATH1061', 'MATH1062', 'MATH1050', 'MATH1064', 'DATA1001', 'MATH1111', 'DATA1901', 'MATH1961', 'MATH1972', 'MATH1964', 'MATH1962', 'QBUS1040', 'ECON1003', 'ECON1001', 'ECMT1010', 'BUSS1020', 'BUSS1040', 'ENVX1002', 'PSYC1001', 'PSYC1002', 'PSYC2012']}

def zero_shot_class_major(user_input):
    candidate_labels = all_majors_categories
    result = classifier(user_input, candidate_labels)
    return result['labels'][0]

calculus_background_text = """Based on the course you have taken in high school you have been placed into the {} category
Then, ask the user: "Alternatively, if you would like to check your allocation, you can use our Calculus Checker, and answer a few questions to determine your maths background.
Answer with either:
- I am happy with the current allocation
- I would like to be allocated using the Calculus Checker"""

calc_satisfied = "Your Calculus Background of {calc_category} satisfies the requirements for {major}."
calc_not_satisfied_bridging = "There are no units that can be taken without bridging materials at your current maths background"
calc_satisfied_bridging = "Here are units relevant to {major} that you can take without further bridging materials: {satified_units}"
support_pathways = "However, given your mathematical background of {calc_category} to do a {major} Degree you must complete: {pathway}"

relevant_units = """{bridging}

{is_calc_satisfied} The mathematics units you will need to take are:
{all_units}
The terminology used for required units is:

NR: Not Strictly Required but Highly Recommended
A: Advanced
SSP: Special Studies Program

{support_pathways}
If you would like to look at the Support Pathway/requirements for a different degree please answer with another degree name. Feel free to ask further questions if you need clarification. Some examples might be:

Try typing: I'd like more information on {major}
When do I need to take these units?
Can I have further unit descriptions of required units?"""



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
You are an Academic Advisor, specializing in mathematics, at the University of Sydney. 
The user is a Year 12 student who needs advice on what mathematic pathways to take for a given degree and their mathematical background.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    step = 0
    calculus_category = "Pre-Calculus"
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
            print("We will use a quick quiz to determine your calculus knowledge. This is not a test, but to know a little bit more about your maths background.\nThis will be done using Qualtrics. Link: https://sydney.au1.qualtrics.com/jfe/form/SV_1AYHXErsa1NHMLI After you complete the quiz, please state your categorisation of either Pre-Calculus, Calculus Ready, or Extended Calculus")
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
            print(units_without_bridging_output)
            all_units_major_output = all_units_for_major(major_label)
            all_units_major_output_str = ""
            for unit in all_units_major_output:
                all_units_major_output_str += "- {}\n".format(unit)
            
            units_without_bridging_output_str = ""
            if len(units_without_bridging_output) == 0:
                print(calc_level_dict[calculus_category])
                print(calc_level_dict[all_levels_majors[major]])
                if calc_level_dict[calculus_category] < calc_level_dict[all_levels_majors[major]]:
                    print(relevant_units.format(major = major, bridging = calc_not_satisfied_bridging, is_calc_satisfied = "", all_units = all_units_major_output_str, support_pathways=""))
            else:
                for unit in units_without_bridging_output:
                    units_without_bridging_output_str += "- {}\n".format(unit)
            
            
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

