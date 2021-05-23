import discord
import firebase_admin
from PIL import ImageFont, ImageDraw, Image  
import datetime
import cv2  
import numpy as np  
import os
import csv
import urllib.request
import io
import img2pdf
from uuid import uuid4
jsona = {
  "type": "service_account",
  "project_id": "owasp-test-855b8",
  "private_key_id": "230671273ea0407aace1cefeb00d5f057e570e97",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDcIagK9Qo2+Kpb\nqsRHF5VZvNM55/bYHt9PSSyETXMgbyMeDKaoIpat8KU8EOSadbkWosT6ZOG4apT7\nkZd9HrmxQ+D3orKEvsxbpMJTD6tnoOHMRFHvH+s8IbbUZ3UHUeHSm5WWFlyhEEUj\nwO4jkdqhLI7Bzzqy7oOUr8BAMlgUh1udHPB05X3pRmoxS5fkcjmpXDP0t+VJACE7\nRbWBTSHIt9Rmlpc6X0FroJyaMFwkaNwgRSDg1AXgKbVIJxA3uVg4XrewKHiIh0Yt\nN4rokwxTpjqdfMLfppBh3Tk+Uf/MueQljr2XDsBvtONERpy0jcXESDXdpWL7Gm8e\nNOBuvykdAgMBAAECggEAQ51K4mK1yoDCwvlG5JdH1pJ7RtQLLAL/kHjnZZPsgs/g\nN4CnSAmnwrGh7zs5HICAY4WHf2mxM1X5gPQNVe80FlDFLwsYTlHUr2mCDsVHXsM5\n1+Y8THi/Zm7sm31TovXxqSEE517jAM3gjsTZ4K8SOmNXTgx6+S7t16PMJ2vPRi5j\ndS2aAlcEaozavAa5A5EdTxE8JkBAIYlFmvL5UuQ6thaAXkAWeQ1CAcqaMX81lwY5\n7Af+fqcR6cxNnUT8IHG6n3AxhSWNxwrdl1ALTecGYoUfCuxLRq29eSGBLU6wYrVo\nTjz0E+yqfJpgY/0dETDFWGUsz6LjTS4KN3yenm5VuQKBgQD2QcPrFPMO7l947NUp\nT+lskshAKOJAjqkQbabFZBHOuRTEQeWuldVFZI5oAw4m8BAX+tHeNvhqIOa4xD1g\nTF61MAicGJ8APExAiAOn/xN3Hrns1gMqnTy+Wc+p0Mr6pjy+D+2YUXw2MMmwSDME\nUpuJVkPcxaf/rFy3pfWkXBbFlwKBgQDk10cGCW49adT+oobmgELlP7LqkeoqFah+\nMecELxEvKzFWvYwyhBZ434Mvuygeyya5YleHqNiTEBceedvIN3tbklwmJ914CS0z\n9ag9/o3ZGQCHqv8f0FnygB4dREYqZPWEp7XR6UKyAmySnUmubju1w4WQ9p+SqoSM\nFYzCGaplawKBgC2ExoQjoTH3WepuTJCQVuNc1msVo4yvUgzZV+RQtQHzMCV+0MfO\npldnWPNc7TbBVRg5oqVin9RuNHeevoGYXEE9mbnQy0Mt4iJjgdmBysVQBqoCfR9Z\nZSsCSuJm174xEDVJmG95UG5r4jwVfGimJF3kdjLOzljyMUk5AgjZhNQNAoGBANS9\nhZuJHOEfCBIJChwzVP1GcJA9QlIJfHCE990d3H3bS6z13eYAgduw/oZbGXs3JTLm\nx7SoNV7ScIu2ganqWlXRBLW8DdnPviQ11kh742bWJXX6c98hlN0qWdSfahNzdAP0\n3cTdc1GFi2Xpr1vnwr7Bm+QeQk7ZEwwf5JF1xsEtAoGAXk8aRNPinkh9Ghaa9WSK\nY4PL6tmdEDOqNMdO5tK3ycMLcAWcq+7EdQBaC210OVWjSGuY51r0xog2PRmIMWuI\nB02pepuOJcATa0s59R44vsMZTRDwpRwDJ4Uva38a8TrDEva/0mUp6TQSkqwj94wq\n0+Oxdw9UxJnUjF2GFwWKarw=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ky1l9@owasp-test-855b8.iam.gserviceaccount.com",
  "client_id": "104680298966263625877",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ky1l9%40owasp-test-855b8.iam.gserviceaccount.com"
}
from firebase_admin import credentials,db,storage
from discord.ext import commands
from PIL import Image,ImageDraw,ImageFont
import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\siddr\Desktop\owasp.json"
client = commands.Bot(command_prefix = '!')
cred = credentials.Certificate(jsona)
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://owasp-test-855b8-default-rtdb.firebaseio.com/',        
    'storageBucket': 'owasp-test-855b8.appspot.com',
})
ref = db.reference('Certificates')
add = db.reference('Data')
bucket = storage.bucket()
blob = bucket.blob('dynamic certificate/')
counter = 0
@client.event
async def on_ready():
    print("STFU and go to discord!")
@client.command()
async def addCertificate(ctx, member: discord.Member, year):
    maincounter=0
    damn = add.get()
    for i in damn.values():
        if i['Discord']==member.name:
            ref.child(f'{member.name}').push({
                'Discord':member.name,
                'Name': i['Name'],
                'Year':year,
            })
            await ctx.send('User id,name verified ........Certificate added !')
            maincounter=1
            break
        
    if maincounter==0:
        await ctx.send(f'smthng is fishhhhyyyy...{ctx.message.author.name} is recommended to wear specs')
@client.command()
async def adddata(ctx,member:discord.Member,*,name):
   add.push({
       'Discord':member.name,
       'Name': name
   })
   await ctx.send('Data added . Reference "data" for certification')
@client.command()
async def bye(ctx):
    await client.close()
@client.command()
async def getCertificate(ctx, member: discord.Member):
    damn = ref.child(f'{member.name}').get()
    j = 0
    for i in damn.values():
        username = i['Name']
        useryear = i['Year']
        # img = Image.open('Certificate.png')
        blob = bucket.blob(f'dynamic certificate/{username}-{useryear}')
        url = "https://firebasestorage.googleapis.com/v0/b/owasp-test-855b8.appspot.com/o/Certificate.png?alt=media&token=2f73cc57-b841-41d0-8f61-68fb1f4fc5f7"
        url_response = urllib.request.urlopen(url)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        cv2_im_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)  
        new_token = uuid4()
        metadata  = {"firebaseStorageDownloadTokens": new_token}
        draw = ImageDraw.Draw(pil_im) 
        font = ImageFont.truetype('poppins.ttf',55)
        # draw = ImageDraw.Draw(img)
        name = i['Name']
        year = i['Year']
        x = 625-(len(name)*13.6)
        draw.text(xy=(x,350),text=name,fill=(255,255,255),font=font)
        draw.text(xy=(775,565),text=year,fill=(255,255,255),font=font)
        img_bytes = io.BytesIO()
        pil_im.save(img_bytes, format = 'PNG')
        img_byte_arr = img_bytes.getvalue()
        # pdf_bytes = img2pdf.convert(img_byte_arr)
        # cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        blob.metadata = metadata
        blob.upload_from_string(img_byte_arr,content_type = 'image/png')
        url = blob.generate_signed_url(datetime.timedelta(seconds = 600), method = 'GET')
        # myurl = bucket.ref('dynamic certificate/').getDownloadURL()
        await ctx.send(f'{url}')
        await ctx.send(f"Certificates of   {username}    have been saved to the Database (path:dynamic certificates/)" )
client.run('ODQ0ODYzMDE0MTE2MjYxOTAx.YKYl_w.9y-EXswQVLSv-cyKl7RxcOl-Qyw')