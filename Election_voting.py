import mysql.connector
databases=mysql.connector.connect(host="localhost",username="root",password="12345",database="Election_voting")
mycursor=databases.cursor()
def insert_vote_count():
    sql="insert into election_booth values(%s,%s,%s,%s,%s,%s)"
    voter_name=input("enter your name:")
    voter_id=int(input("enter your voter id:"))
    voter_age=int(input("enter your age:"))
    if voter_age>=18:
        voter=input("ready to vote means press VOTE:")
    DMK=int(input("if you want to vote DMK meams press 1 otherwise press 0:"))
    if DMK==0 or DMK==1:  
        BJP=int(input("if you want to vote BJP meams press 1 otherwise press 0:"))
    if BJP==0 or BJP==1:
        ADMK=int(input("if you want to vote ADMK meams press 1 otherwise press 0:"))
    if  ADMK==1 or ADMK==0:
        DMDK=int(input("if you want to vote DMDK meams press 1 otherwise press 0:"))
    if  DMDK==0 or DMDK==1:
        NTK=int(input("if you want to vote NTK meams press 1 otherwise press 0:"))
    if  NTK==0 or NTK==1 :
        NOTA=int(input("if you want to vote NOTA meams press 1 otherwise press 0:"))
    if  NOTA==1 or NOTA==0:
       val=(DMK,BJP,ADMK,DMDK,NTK,NOTA)
    mycursor.execute(sql,val)
    sum_sql="select SUM(DMK),SUM(BJP),SUM(ADMK),SUM(DMDK),SUM(NTK), SUM(NOTA)from election_booth"
    mycursor.execute(sum_sql)
    result=mycursor.fetchall()
    databases.commit()
    print("data saved sucessfully")
    import datetime
    x=datetime.datetime.now()
    f=open("voter_database.txt","a")
    f.write(f"{voter_name} is voted sucessfully at time of {x}, \n ")
    import smtplib
    import random
    def email_sendings():
        try:
           receiver_mails=["sivan25970@gmail.com"]
           for i in receiver_mails:
            data=voter_id
            print(i,data)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("rogini263@gmail.com","xghh egxe pthh mknm")
            message=f"{voter_name} voted sucessfully at time {x} Thanks for voting"
            s.sendmail("rogini263@gmail.com",i,message)
            s.quit()
            print("mail sends sucessfully")
        except:
            print("mail not send")
    email_sendings()
insert_vote_count()
def election_data():
    from decimal import Decimal
    sum_sql="select SUM(DMK),SUM(BJP),SUM(ADMK),SUM(DMDK),SUM(NTK),SUM(NOTA) from election_booth"
    mycursor.execute(sum_sql)
    myresult=mycursor.fetchone()
    print("Total votes for each parties:")
    party_names = ["DMK", "BJP", "ADMK", "DMDK", "NTK","NOTA"]
    if myresult:
        for party, votes in zip(party_names, myresult):
            votes = int(votes) if isinstance(votes, Decimal) else votes
            print(f"{party}: {votes}")
election_data()