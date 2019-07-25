import sys
import _mysql

entry_id = sys.argv[1]

def select_from_db(column_name):
    db_conn = _mysql.connect(user="pyuser",passwd="t34igj",db='instaad_db')
    db_query = db_conn.query("SELECT "+column_name+" FROM user_data WHERE entry_id = '"+entry_id+"';")
    db_result = db_conn.store_result()
    db_list = list(db_result.fetch_row(10000))
    res = [list(i) for i in db_list]
    res = res[0]
    res = res[0]
    res = res.decode("utf-8")
    return res

username = select_from_db("username")
full_name = select_from_db("full_name")
most_recent_post = select_from_db("most_recent_post")
second_post = select_from_db("second_post")
profile_picture = select_from_db("profile_picture")

#html = "<h2> Instagram Ad </h2><p>"+full_name+"</p>"

#print(html)

html = """ <!DOCTYPE html> <html> <head>
  <title> Instagram Ad </title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    #main_container {
    }
    span {
       display: inline-block;
    }
    #profile{
      width:30%
      }
    #user_name {
      font-size: xx-large;
      padding-left: 20%;
    }
    #profile_pic {
      width : 80%;
      border-radius: 50%;
    }
    #pics {
      width:60%;
    }
    .pic {
      width:50%;
    }
  </style> </head> <body> <container id = "main_container">
  <span id = "profile">
    <span id = "user_name"></span>
    <img id = "profile_pic"></img>
  </span>
  <span id = "pics"></span> </container> <script>
  var instaProfile = {
      display_name : "A",
      user_name: '"""+username+"""',
      profile_pic: '"""+profile_picture+"""',
      most_recent_post : '"""+most_recent_post+"""',
      second_post : '"""+second_post+"""',
      pics: [
        "https://scontent.cdninstagram.com/vp/63ac79c74f644f062a9e7f56ddcc16cc/5DD12679/t51.2885-15/sh0.08/e35/s640x640/67578752_349693785962003_4253384163365456291_n.jpg?_nc_ht=scontent.cdninstagram.com",
        "https://scontent-lax3-2.cdninstagram.com/vp/09bd33eaa2d539658cba23e09411f1fd/5DE01C58/t51.2885-15/e35/s1080x1080/46204479_522168848295712_8844560794998887349_n.jpg?_nc_ht=scontent-lax3-2.cdninstagram.com"
      ]
    };
    document.getElementById("user_name").innerHTML = "@" + instaProfile.user_name;
    /*profile_pic_node = document.createElement("img")
    profile_pic_node.src = instaProfile.profile_pic
    document.getElementById("profile_pic").appendChild(profile_pic_node)*/
    profile_pic_node = document.getElementById("profile_pic")
    profile_pic_node.src = instaProfile.profile_pic
    pic_node_recent = document.createElement("img")
    pic_node_recent.src = instaProfile.most_recent_post
    pic_node_recent.setAttribute("class", "pic");
    document.getElementById("pics").appendChild(pic_node_recent)
    pic_node_second = document.createElement("img")
    pic_node_second.src = instaProfile.second_post
    pic_node_second.setAttribute("class", "pic");
    document.getElementById("pics").appendChild(pic_node_second)
    /*for (i = 0; i < instaProfile.pics.length; i++) {
      pic_node = document.createElement("img")
      pic_node.src = instaProfile.pics[i]
      pic_node.setAttribute("class", "pic");
      document.getElementById("pics").appendChild(pic_node)
    }*/
</script> </body> </html>
"""

print(html)
