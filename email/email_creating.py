from jinja2 import Template
import sys

campaign_id = sys.argv[1]

rendered = Template(open('first_day/email.html').read()).render(heatmap = "https://jinja.palletsprojects.com", time = '20', areas = "Santa Monica");

text_file = open("ready_email/"+campaign_id+"email","w")
text_file.write(rendered)
text_file.close()
