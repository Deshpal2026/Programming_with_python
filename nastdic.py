student = {
    "Name" : "Rahul Pal",
    "Subj" : {
        "phy" : 90,
        "chem" : 98,
        "Maths": 79,
        "Age" : {
            "Anu" : 18,
            "Mahak": 16,
            "Shuba": 19
        }


    },

    "Kamal" : {
        "phy" : 70,
        "chem" : 88,
        "Maths": 69

    } 
    
}
print(student)
print(student["Name"])
print(student["Subj"]["phy"])
print(student["Kamal"])
print(student ["Kamal"] ["Maths"])
print(student["Subj"]["Age"]["Shuba"])
print("Total number of values in the dictinary :", str(len(student)))
print(len(student["Subj"]))
