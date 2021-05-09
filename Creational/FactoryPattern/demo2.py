from abc import ABCMeta, abstractmethod
import xlsxwriter
import csv


class File(metaclass=ABCMeta):
    @abstractmethod
    def export(self):
        pass


class Excel(File):
    def __init__(self, students):
        self.students = students

    def export(self):
    	workbook = xlsxwriter.Workbook('Grades.xlsx')
    	worksheet = workbook.add_worksheet()
    	worksheet.write(0, 0, "Adı")
    	worksheet.write(0, 1, "Soyadı")
    	worksheet.write(0, 2, "Not")
    	for num, student in enumerate(self.students, start=1):
    		worksheet.write(num, 0, student["first_name"])
    		worksheet.write(num, 1, student["last_name"])
    		worksheet.write(num, 2, student["grade"])
    	workbook.close()
    	print("exported")

class Csv(File):
	def __init__(self, students):
	    self.students = students

	def export(self):
		with open('Grades.csv', mode='w') as file:
			writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(['Adı', 'Soyadı', 'Not'])
			for student in self.students:
				writer.writerow([ student["first_name"], student["last_name"], student["grade"] ])



class FileFactory:
    def create_file(self, students, format):
        if format == 'EXCEL':
            return Excel(students)
            print("file created")

        elif format == 'CSV':
            return Csv(students)
        else:
        	raise ValueError(format)





if __name__ == "__main__":
	student1 = {
		"first_name": "Name-1",
		"last_name": "Surname-1",
		"grade":90
	}
	student2 = {
		"first_name": "Name-2",
		"last_name": "Surname-2",
		"grade":93
	}
	student3 = {
		"first_name": "Name-3",
		"last_name": "Surname-3",
		"grade":95
	}
	students = [student1, student2, student3]
	file_factory = FileFactory()
	file = file_factory.create_file(students, "CSV")
	file.export()
