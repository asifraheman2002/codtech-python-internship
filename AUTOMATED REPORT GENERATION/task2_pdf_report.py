import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [88, 72, 95, 68]
}
df = pd.DataFrame(data)

# Save chart
plt.bar(df['Name'], df['Marks'], color='skyblue')
plt.title("Marks of Students")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.savefig("marks_chart.png")

# Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Student Report", ln=True, align='C')

# Table in PDF
for index, row in df.iterrows():
    pdf.cell(200, 10, txt=f"{row['Name']}: {row['Marks']} marks", ln=True)

# Add chart
pdf.image("marks_chart.png", x=10, y=60, w=180)
pdf.output("student_report.pdf")
