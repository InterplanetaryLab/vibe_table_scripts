# Test Report Python Class
# Creates HTML files with Basic Test Reports
import datetime

class test_report:
    def __init__(self):
        self.title = "Base Report"
        self.test_date = ""
        self.analysis_date =""
        self.running_html = ""
        self.output_dir = ""
        self.report_creation_date = ""
        self.test_type = "base_test"
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

        </style>
        <header style="background-color:DarkMagenta;">
        <h1 style="color:white; font-size: 40px;"> II-Lab Test Report </h1>
        <h2 style="color:white; font-size: 25px;"> Test Report Header </h2>
        <table style="width:100%%">
            <tr>
                <th>Test Type:</th>
                <th>%s</th>
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
        </header>
        """%(self.test_type,self.test_date, self.analysis_date, self.output_dir, self.report_creation_date)
        return header
    def add_image(self,image_path, sizew=1065, sizeh=763):
        self.running_html += """\n <img src=%s alt="image missing" width="%s" height="%s"> """%(image_path,sizew,sizeh)
    def write_html_report(self):
        self.report_creation_date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        html = "<html>\n%s\n%s\n</html>"%(self.create_header(),self.running_html)
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
