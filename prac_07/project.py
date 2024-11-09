from datetime import datetime

class Projects:

    def __init__(self, name="", start_date="", priority="", cost_estimate="", completion_percentage=""):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"  {self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${float(self.cost_estimate):.2f}, completion: {self.completion_percentage}%"

    def main(self, projects_list="", new_load=True):
        if new_load == True:
            projects_list = Projects.load_file(self)
        print("- (L)oad projects ")
        print("- (S)ave projects ")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        user_option = input(">>> ").upper()
        Projects.option_selector(self, user_option, projects_list)

    def option_selector(self, user_option, projects):
        if user_option == "L":
            Projects.load_projects(self, projects)
        elif user_option == "S":
            Projects.save_projects(self, projects)
        elif user_option == "D":
            Projects.display_objects(self, projects)
        elif user_option == "F":
            Projects.filter_projects(self, projects)
        elif user_option == "A":
            Projects.add_new_project(self, projects)
        elif user_option == "U":
            Projects.update_project(self, projects)
        elif user_option == "Q":
            Projects.quit(self, projects)

    def load_file(self):
        FILENAME = "projects.txt"
        with open(FILENAME, 'r') as in_file:
            projects = []
            project = []
            new_in_file = in_file.readlines()[1:]
            for line in new_in_file:
                project = line.strip('\n').split('\t')
                print(project)
                line = Projects(project[0], project[1], project[2], project[3], project[4])
                print(project)
                line.start_date = datetime.strptime(project[1], "%Y-%m-%d").date()
                projects.append(line)
            return projects

    def load_projects(self, projects):
        count = 0
        for line in projects:
            print(f'{count}. ', line)
            count += 1
        return Projects.main(self, projects, False)

    def save_projects(self, projects, mid_save=True):
        FILENAME = "projects.txt"
        with open(FILENAME, 'w') as out_file:
            out_file.write(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage")
            for line in projects:
                out_file.write(f"\n{line.name}\t{line.start_date}\t{line.priority}\t{line.cost_estimate}\t{line.completion_percentage}")
        if mid_save == True:
         return Projects.main(self, projects, False)

    def display_objects(self, projects):
        print("Incomplete projects:")
        for line in projects:
            if line.completion_percentage != "100":
                print(str(line))
        print("Completed projects")
        for line in projects:
            if line.completion_percentage == "100":
                print(str(line))
        return Projects.main(self, projects, False)

    def filter_projects(self, projects):
        project_date = input("Show projects that start after date (dd/mm/yy): ")
        formatted_project_date = datetime.strptime(project_date, "%d/%m/%Y").date()
        for line in projects:
            if line.start_date > formatted_project_date:
                print(line)
        return Projects.main(self, projects, False)

    def add_new_project(self, projects):
        new_project = Projects()
        new_project.name = input("Name: ")
        new_project.start_date = input("Start date (dd/mm/yy): ")
        new_project.start_date = datetime.strptime(new_project.start_date, "%d/%m/%Y").date()
        new_project.start_date.strftime('%Y-%m-%d')
        new_project.priority  = int(input("Priority: "))
        new_project.cost_estimate = float(input("Cost estimate: $"))
        new_project.completion_percentage = int(input("Percentage complete: "))
        projects.append(new_project)
        return Projects.main(self, projects, False)

    def update_project(self, projects):

        count = 0
        numbered_project_list = []
        for line in projects:
            numbered_project_list.append([count, line])
            print(f"{count}. {line}")
            count += 1
        choice_of_project = int(input("Project choice: "))
        for line in numbered_project_list:
            if choice_of_project == line[0]:
                print(line[1])
                new_percentage = int(input("New Percentage: "))
                if new_percentage == "":
                    pass
                else:
                    line[1].completion_percentage = new_percentage
                new_priority = int(input("New Priority: "))
                if new_priority == "":
                    pass
                else:
                    line[1].priority = new_priority
        return Projects.main(self, projects, False)

    def quit(self, projects):
        user_quit = input("Would you like to save to projects.txt? ")
        if "no" in user_quit:
            print("Thank you for using custom-built project management software.")
        if "yes" in user_quit:
            Projects.save_projects(self, projects, False)
            print("your file has been saved!")
            print("Thank you for using custom-built project management software.")
