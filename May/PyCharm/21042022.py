months={'Jan','Feb','Mar','Apr',"May",'Jun','Jul','Aug','Sep','Oct',"Nov",'Dec'}
m30={'Apr','Jun','Aug','Nov'}
m31={'Jan','Mar','May','Jul','Sep','Oct','Dec'}
m28={'Feb'}

#.intersection() Method : Returns Set of common values
a1=months.intersection(m30)
print(a1)

#.symmetric_differenve Method() : Returns set of Uncommon Elements
#Print Months having days other than 30 days (i.e Months with 31 days and 28 days)

a3=months.symmetric_difference(m30)
print(a3)

#Print Months having days other than 30 days excluding Feb as well

a2=months.symmetric_difference(m30.symmetric_difference(m28)) #Or We can add m30 and m28 and use symmetric_difference
print(a2)
