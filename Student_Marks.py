srn_num=["PECS001","PECS015","PECS065","PECS035","PECS038"]#given srn num
physics_marks=[98,99,85,92,79]#given physics marks
chemistry_marks=[91,90,84,98,99]#given chemistry marks
math_marks=[78,39,60,50,84]#given mathematics marks
bio_marks=[95,59,78,80,89]#given biology marks
stu_mar={}#empty dictionary
mar_det={}#empty dictionary
for k in range(len(srn_num)):#passing through the list for adding marks
   mar_det['phy']=physics_marks[k]#adding physics marks
   mar_det['chem']=chemistry_marks[k]#adding chemistry marks
   mar_det['math']=math_marks[k]#adding math marks
   mar_det['bio']=bio_marks[k]#adding biology marks
   stu_mar[srn_num[k]]=mar_det
print("STUDENT MARKS IS :",stu_mar)#printing student marks
print("MARKS OF AFTER SUBJECTS ARE ADDED",mar_det)#adding all the subject's marks
