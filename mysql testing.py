import mysql.connector

mydb = mysql.connector.connect(
  host="brfytvylwdzhculozfq5-mysql.services.clever-cloud.com",
  user="uh06snweshud7gzj",
  password="24c1orUcFmlEOgctcpFH",
  database="brfytvylwdzhculozfq5"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SN, sourceName, title, description, content, publishedAt FROM NewsFeeds")

myresult = mycursor.fetchall()

for x in myresult: 
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print(str(x[0]) + '. ' + x[1])
    print()
    print('Title : ' + x[2])
    print()
    print('Description : ' + x[3])
    print()
    print('Dated On : ' + x[4])
    print()