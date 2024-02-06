s1 = """<html>
    <head>

    </head>
    <body>
        <h1>my name is """
s2 = """</h1>
        <h2>I love """
s3 = """</h2>
    </body>
</html>"""
name1 = "Jessy"
interest = "Project managment"
f1 = open(name1+".html","w")
html = s1+name1+s2+interest+s3
f1.write(html)
f1.close()
