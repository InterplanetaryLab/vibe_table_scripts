# Test Report Python Class
# Creates HTML files with Basic Test Reports
import datetime
import os

class test_report:
    def __init__(self):
        self.running_html = ""
        self.output_dir = ""
        self.report_creation_date = ""

        # Header Elements
        self.title = "Base Report"
        self.report_creation_date = ""
        self.test_date = ""
        self.analysis_date =""
        self.test_type = "base_test"
        self.test_description_paragraph = ""
        self.test_description_short = ""
        self.project_name = ""
        self.test_purpose = ""
        self.test_outcome = ""
        self.object_under_test = ""
        self.customer = ""
        self.lab_operator = ""
    def create_header(self):
        header = """
        <style>
        table, th, td {
          border:1px solid black;
          color:white;
          font-size: 22px;
        }

        .center{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%%;
        }

        p {
            font-size: 20px;
        }

        </style>
        <header style="background-color:#604a8b;">
        <h1 style="color:white; font-size: 40px;"> II-Lab Test Report </h1>
        <img src="%s" alt="missing logo" width="1400" height="200">
        <h2 style="color:white; font-size: 25px;"> Test Report Header </h2>
        <table style="width:100%%">
            <tr>
                <th>Test Type:</th>
                <th>%s</th>
            </tr>
            <tr>
                <th>Project Name: </th>
                <th>%s</th
            </tr>
            <tr>
                <th>Test Purpose: </th>
                <th>%s</th
            </tr>
            <tr>
                <th>Test Outcome: </th>
                <th>%s</th
            </tr>
            <tr>
                <th>Object Under Test: </th>
                <th>%s</th
            </tr>
            <tr>
                <th>Customer</th>
                <th>%s</th
            </tr>
            <tr>
                <th>Lab Operator</th>
                <th>%s</th
            </tr>
            <tr>
                <th>Test Date:</th>
                <th>%s</th>
            </tr>
            <tr>
                <th>Analysis Date: </th>
                <th>%s</th>
            </tr>
            <tr>
                <th>Output Directory: </th>:
                <th>%s</th>
            </tr>
            <tr>
                <th>Report Creation Date: </th>:
                <th>%s</th>
            </tr>
        </table>
        <h2 style="color:white" >Test Description Short: </h2>
        <p style="color:white">%s</p>
        <h2 style="color:white">Test Description Paragraph: </h2>
        <p style="color:white">%s</p>
        </header>
        """%(self.output_dir+"/logo.png",self.test_type,self.project_name, self.test_purpose, self.test_outcome, self.object_under_test, self.customer, self.lab_operator, self.test_date, self.analysis_date, self.output_dir, self.report_creation_date, self.test_description_short, self.test_description_paragraph)
        return header
    def add_image(self,image_path, sizew=1065, sizeh=763):
        self.running_html += """\n <img src=%s alt="image missing" width="%s" height="%s"> """%(image_path,sizew,sizeh)
    def add_images(self, image_filename_partial, sizew=1065, sizeh=763): # adds_images based upon partial match to filename
        filenames_arr = []
        if (self.base_path != ""):
            base_path = self.base_path+"/images"
            for file in os.listdir(base_path):
                if (image_filename_partial in file):
                    filenames_arr.append("./images/"+file)
            filenames_arr.sort()
            for i in range(len(filenames_arr)):
                self.add_h2(image_filename_partial+" %d"%(i+1))
                self.add_image(filenames_arr[i], sizew, sizeh)
        else:
            return -1

    def add_p(self, text):
        self.running_html += """\n <p>%s</p>"""%text
    def add_h2(self, text):
        self.running_html += """\n <h2 style="font-size: 25px">%s</h2>"""%text
    def create_results(self):
        self.running_html += ""
    def write_html_report(self):
        self.report_creation_date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        results = """
        <h1 style="font-size: 35px;"> Results Section: </h1>
        """
        self.create_results()
        html = "<html>\n%s\n%s\n%s\n</html>"%(self.create_header(),results,self.running_html)
        file_name = self.title.replace(" ","-")+"_"+self.test_date+".html"
        try:
            f= open(self.output_dir+"/"+file_name, 'w')
            f.write(html)
            f.close()
        except:
            print("error opening/writing file")

if __name__ == "__main__":
    report = test_report()
    report.output_dir = "/home/rommac/test_reports"
    report.add_image("./CF1_X.PNG")
    report.write_html_report()
