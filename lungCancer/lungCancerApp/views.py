from django.shortcuts import render
from lungCancerApp.models import users
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Create your views here.
def loginview(request):
    return render(request,'login.html')

def regiterview(request):
    return render(request,'registration.html')
def saveuserview(request):
    usersname=request.POST["name"]
    contactno=request.POST["Contact Number"]
    useremail=request.POST["Email"]
    address=request.POST["Address"]
    username=request.POST["username"]
    userpassword=request.POST["password"]
    

    newuser=users(name=usersname,ContactNumber=contactno,Email=useremail,Address=address,Username=username,Password=userpassword)
    newuser.save()
    return render(request,'login.html')
def verifyloginview(request):
    usersname=request.POST["username"]
    password=request.POST["password"]

    user=users.objects.filter(Username=usersname)
    for u in user:
        if u.Password == password:
            return render(request,'home.html')
        else:
            return render(request,'login.html')
        
def CheckDiseaseview(request):
    Gender=request.POST["Gender"]
    Age=request.POST["Age"]
    Smoking=request.POST["Smoking"]
    YellowFingers=request.POST["YellowFingers"]
    Anxiety=request.POST["Anxiety"]
    Peer_Pressure=request.POST["Peer_Pressure"]
    Chronic_Disease=request.POST["Chronic_Disease"]
    Fatigue=request.POST["Fatigue"]
    Allergy=request.POST["Allergy"]
    Wheezing=request.POST["Wheezing"]
    Alcohol_Consuming=request.POST["Alcohol_Consuming"]
    Coughing=request.POST["Coughing"]
    Shortness_of_Breath=request.POST["Shortness_of_Breath"]
    Swallowing_Difficulty=request.POST["Swallowing_Difficulty"]
    Chest_Pain=request.POST["Chest_Pain"]
    
    dataset = pd.read_csv("lungCancer.csv")
    X=dataset.iloc[:,:-1]
    Y=dataset.iloc[:,-1]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=.90)
    model=RandomForestClassifier(random_state=48)

    model.fit(X_train,Y_train)
    test_data=np.array([Gender,Age,Smoking,YellowFingers,Anxiety,Peer_Pressure,Chronic_Disease,Fatigue,Allergy,Wheezing,Alcohol_Consuming,Coughing,Shortness_of_Breath,Swallowing_Difficulty,Chest_Pain]).reshape(1,-1)

    predicted_result=model.predict(test_data)
    print(predicted_result[0])

    if predicted_result[0] == 1:
        print("Based on our analysis, the patient has been diagnosed with Lung Cancer.")
        result="Based on our analysis, the patient has been diagnosed with Lung Cancer."
    else:
        print("Good news! The patient is normal and healthy.")
        result="Good news! The patient is normal and healthy."
    return render(request,'result.html',{'result':result})


  
