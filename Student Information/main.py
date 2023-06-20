import csv
from fpdf import FPDF


csv_file = open("student.csv", "w+", newline="")
csv_writer = csv.writer(csv_file)


header = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of birth", "Phone_no."]
csv_writer.writerow(header)

while True:
    try:
        n = int(input("How many student records do you want to insert : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    else:
        break

data = []


for i in range(n):
    print("Enter Student record", i + 1, ":")
    student_id = input("Student ID: ")
    name = input("Name: ")
    while True:
        try:
            roll = int(input("Roll: "))
        except ValueError:
            print("Invalid Roll. Please enter a valid Roll.")
            continue
        else:
            break
    semester = input("Semester: ")
    shift = input("Shift: ")
    dept = input("Department: ")
    dob = input("Date of birth (dd/mm/yyyy): ")
    phone_no = input("Phone No: ")
    rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
    data.append(rec)

csv_writer.writerows(data)

csv_file.close()

pdf = FPDF()
pdf.add_page()
page_width = pdf.w + 3 

pdf.set_font("Times", "B", 12.0)
pdf.cell(page_width, 0.0, 'Students Data Report', align='C')
pdf.ln(10)

pdf.set_font("Courier", "", 12)
col_width = page_width / 6


csv_file = open("student.csv", "r")
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    for item in row:
        pdf.cell(col_width, 10, str(item), border=1)
    pdf.ln()

pdf.ln(10)
pdf.set_font("Times", "", 10.0)
pdf.cell(page_width, 0.0, "End of report", align='C')


pdf.output('student.pdf', 'F')

csv_file.close()
