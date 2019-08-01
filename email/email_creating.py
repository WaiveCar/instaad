import sys
from jinja2 import Template

campaign_id = sys.argv[1]
###Some sort of bug going on here
rendered = Template(open('first_day/email.html').read()).render(heatmap = "https://jinja.palletsprojects.com", time = 'asd', areas = "Santa Monica");

text_file = open("ready_email/"+campaign_id+"email","w")
text_file.write(rendered)
text_file.close()
