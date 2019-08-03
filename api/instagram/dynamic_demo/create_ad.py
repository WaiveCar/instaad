import sys
import jinja2 import Template

entry_id = sys.argv[1]

username = select_from_db("username")
full_name = select_from_db("full_name")
most_recent_post = select_from_db("most_recent_post")
second_post = select_from_db("second_post")
hd_profile_picture = select_from_db("hd_profile_picture")

rendered = Template(open('/etc/pyfiles/html/template_old.html').read()).render(username=username,full_name=full_name,most_recent_post=most_recent_post,second_post=second_post,hd_profile_picture=hd_profile_picture)

text_file = open("/var/www/html/campaign_files/instaad_html/"+entry_id+".html", "w")
text_file.write(rendered)
text_file.close()
 
