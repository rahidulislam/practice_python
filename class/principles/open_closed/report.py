from abc import ABC, abstractmethod
# without OCP (Open-Closed Principle)
class Report:
    def __init__(self, report_type:str):
        self.report_type = report_type

    def generate_report(self):
        if self.report_type == 'PDF':
            print("Generating PDF report")
        elif self.report_type == 'CSV':
            print("Generating CSV report")
        else:
            print("Unsupported report type")

# Instantiate the class
pdf_report = Report('PDF')
pdf_report.generate_report()

csv_report = Report('CSV')
csv_report.generate_report()

# with OCP
class Report(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class PDFReport(Report):
    def generate_report(self):
        print("Generating PDF report")

class CSVReport(Report):
    def generate_report(self):
        print("Generating CSV report")

class ExcelReport(Report):
    def generate_report(self):
        print("Generating Excel report")

# Instantiate the class
pdf_report = PDFReport()
pdf_report.generate_report()

csv_report = CSVReport()
csv_report.generate_report()

excel_report = ExcelReport()
excel_report.generate_report()