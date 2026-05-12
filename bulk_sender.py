import pandas as pd
import time

from sender import send_email

data = pd.read_csv('contacts.csv')

with open('templates/welcome_template.html','r') as f:

    template = f.read()

for index,row in data.iterrows():

    name = row['name']
    
    email = row['email']

    personalized_html = template.format(name = name)


    send_email(
        receiver=email,
        subject='Welcome!',
        body=f"Hello {name}",
        html_content=personalized_html,
        
    )

    time.sleep(5)