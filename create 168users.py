#create the session

import boto3
import csv
def client():
    session_obj=boto3.session.Session()
    client_obj=session_obj.client("iam")
    return client_obj

def reading_file(txt):
    with open(txt,"r") as f:
        file=csv.DictReader(f)
        user_details=list(file)
        return user_details
def main():
    user_client=client()
    user_details=reading_file("IAM_168_users_inventory.csv")
    
    for user in user_details:
        username=user["IAM_User_Name"]
        userpol=user["PolicyARN"]
        user_client.create_user(UserName=username)
        user_client.attach_user_policy(
    UserName=username,
    PolicyArn=userpol)
    print ("all users has been created successfully")
if __name__=="__main__":
    main() 
#moaz test




   

