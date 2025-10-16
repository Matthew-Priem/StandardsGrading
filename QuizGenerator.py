import os
from random import sample

class Question:
    def __init__(self,question_text:str, standard:str):
        self.std = standard
        self.text = question_text
    
    def get_std(self): return self.std
    def get_text(self): return self.text
    def __str__(self): return self.text

class ProblemSet:
    def __init__(self,standard:str):
        self.std = standard
        self.questions = []

    def get_std(self): return self.std
    def get_questions(self): return self.questions

    def add_question(self, question:Question):
        self.questions.append(question)
    
    def show_questions(self):
        for question in self.questions:
            print(question)

def parse_file(file_path):
    my_file = open(file_path,'r')

    first_line = my_file.readline().lower() #in case I write Stanard
    standard = None
    if first_line.startswith('%standard'):
        standard = first_line[9:].strip()
    else:
        return None

    problem_set = ProblemSet(standard)

    # Go to first question
    line_data = ''
    while '%new_question' not in line_data:
        line_data = my_file.readline()

    # Parse questions
    data_list = my_file.read().split('%new_question')
    for question in data_list:
        # Store question in problemset
        problem_set.add_question(Question(question, standard))
    my_file.close()

    return problem_set

def parse_all_files():
    all_problem_sets = []
    for root, dirs, files in os.walk('./'):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('.tex'):
                problem_set = parse_file(file_path)
                if problem_set is not None:
                    all_problem_sets.append(problem_set)
    #print(len(all_problem_sets))
    #for problem_set in all_problem_sets:
    #    print(problem_set.get_std())
    return all_problem_sets

def write_make_up(questions, file_name, midterm: bool=True):
    quiz_name = 'midterm retake' if midterm else 'final retake'
    new_file = open(f'./quizFolder/{quiz_name}_quiz.tex','w')

    # All packages used should be written in skeleton file
    skeleton_file = open('./skeletonFile/skeleton.tex')

    # Copies content of skeleton file to new_file
    # ie. writes up to begin document
    new_file.write(skeleton_file.read())
    skeleton_file.close()

    # Code to write each person's unique make up quiz
    my_class = open(file_name)

    for person in my_class.readlines()[1:]:
        data = person.strip().split(',')
        last_name = data[1]
        first_name = data[2]
        section = data[3]
        grades = data[4:]
        question_pool = []

        if midterm: #only retake for std 1.1 -- 8.3. That is, week 1 - 7
            for index, std in enumerate(grades[:21]):
                if not std or not int(std): #this means the std was not met ie. blank or 0
                    #pick a question from corresponding problem sets. 
                    problem_set = questions[index]
                    question_pool.append(sample(problem_set.get_questions(),1)[0])
        else: #end of semester retake. 
            for index, std in enumerate(grades):
                if index != 24 and index != 25: #skip debug standrd. Must be shown in lab with IDE. 
                    if not std or not int(std): #this means the std was not met ie. blank or 0
                        #pick a question from corresponding problem sets. 
                        problem_set = questions[index]
                        question_pool.append(sample(problem_set.get_questions(),1)[0])
        
        if question_pool != []:
            new_file.write(f'{first_name} {last_name} \\hfill {quiz_name} quiz\\\\\n')
            new_file.write(f'section {section}\\\\\n')
            #new_file.write('\\noindent\makebox[\linewidth]{\\rule{\paperwidth}{0.4pt}}')
            
            new_file.write('\\begin{enumerate}\n')

            # Write the selected questions with chapter headers
            selected_questions = sample(question_pool, min(5, len(question_pool)))
            for question in selected_questions:
                # Add a comment with the chapter name before each question
                new_file.write(f'\\item ({question.get_std()})')
                new_file.write(question.get_text().split('\\item',maxsplit=1)[1]) #gets the text after the first \item

            new_file.write('\n\\end{enumerate}\n')
            new_file.write('\\pagebreak\n')

    new_file.write('\\end{document}')
    new_file.close()

def write_quiz(quiz_name:str, stds:list[float], all_problem_sets, file_name):
    '''Generates a unique quiz for each student with questions of specified difficulty'''

    def find_std(std,each_problem_sets=all_problem_sets):
        for problem_set in each_problem_sets:
            if str(std) == problem_set.get_std():
                return problem_set
        print("Something went wacky finding the std. Debug ME!!!")


    new_file = open(f'./quizFolder/{quiz_name}_quiz.tex','w')

    #all packages used should be written in skeleton file
    skeleton_file = open('./skeletonFile/skeleton.tex')

    #copies content of skeleton file to new_file
    #skeleton file contains all packages and custom fuctions
    #ie. writes up to begin document
    new_file.write(skeleton_file.read())
    skeleton_file.close()

    #code to write each person's unique quiz
    my_class = open(file_name)
    #my_class = open('Sp25_CIS121_ClassList.csv')
    for person in my_class.readlines()[1:]:
        techid, last_name, first_name, section_number = person.strip().split(',')[0:4]

        new_file.write(f'{first_name} {last_name} \\hfill {quiz_name} quiz\\\\\n')
        new_file.write(f'section {section_number}\\\\\n')
        #new_file.write('\\noindent\makebox[\linewidth]{\\rule{\paperwidth}{0.4pt}}')
        
        new_file.write('\\begin{enumerate}\n')
        
        #pick a question with the given std.        
        for std in stds:
            problem_set = find_std(std)
            question = sample(problem_set.get_questions(),1)[0]
            new_file.write(f'\\item ({question.get_std()})')
            new_file.write(question.get_text().split('\\item',maxsplit=1)[1]) #gets the text after the first \item


        new_file.write('\\end{enumerate}\n')
        new_file.write('\\pagebreak\n')

    new_file.write('\\end{document}')
    new_file.close()


def main():
    all_problem_sets = parse_all_files()

    #This must be a csv file with format id, last name, first name, section, each of the stds
    students_grades = 'Sample_Grades.csv'


    #write_quiz('Basic IO', [1.1,1.2,1.3], all_problem_sets, students_grades)
    #write_quiz('Expressions', [2.1,2.2,2.3], all_problem_sets, students_grades)
    #write_quiz('Branching', [3.1,3.2,3.3], all_problem_sets, students_grades)
    #write_quiz('Loops', [4.1,4.2,4.3], all_problem_sets, students_grades)
    #write_quiz('Fctns and Strings', [5.1,5.2,6.1], all_problem_sets, students_grades)
    #write_quiz('Lists', [7.1,7.2,7.3], all_problem_sets, students_grades)
    #write_quiz('Dictionaries', [8.1,8.2,8.3], all_problem_sets, students_grades)
    #write_quiz('Advanced Functions', [9.1,9.2], all_problem_sets, students_grades)
    #write_quiz('Debugger', [10.1,10.2], all_problem_sets, students_grades)
    #write_quiz('Classes Part 1', [11.1,11.2,11.3], all_problem_sets, students_grades)
    #write_quiz('Classes Part 2', [12.1,12.2], all_problem_sets, students_grades)
    #write_quiz('Classes Part 3', [13.1,13.2,13.3], all_problem_sets, students_grades)
    #write_quiz('Files', [14.1,14.2,14.3], all_problem_sets, students_grades)
    #write_quiz('Exceptions', [15.1,15.2,15.3], all_problem_sets, students_grades)



    write_make_up(all_problem_sets, students_grades)
    write_make_up(all_problem_sets, students_grades, midterm=False)





if __name__ == '__main__':
    main()



