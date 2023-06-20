import pandas as pd
import matplotlib.pyplot as plt
import numpy
import random
df = pd.read_csv('PA1data')
data_list = df.values.tolist()


random1 = random.randint(0,179)
random2 = random.randint(0,179)
random3 = random.randint(0,179)

value1 = data_list[random1]
value2 = data_list[random2]
value3 = data_list[random3]





#Discretization
#Question1>a>I-----------------------------------------------------------------------------
#Calculating width for 4 different groups
#Calculating the width
width = (max(value1)-min(value1))/4
width = round(width,1)
print("Width for {}. gene is : {}".format(random1, width) )

#Calculating the borders
firstline = min(value1)+width
secondline = min(value1)+width+width
thirdline = min(value1)+width+width+width

firstline = round(firstline,1)
secondline = round(secondline,1)
thirdline  = round(thirdline,1)

group1forvalue1 = []
group2forvalue1 = []
group3forvalue1 = []
group4forvalue1 = []

#Placing the values to the groups for value 1 list
for i in range(500):
    if (value1[i]< firstline):
        group1forvalue1.append(value1[i])
        
    elif (value1[i]<secondline):
        group2forvalue1.append(value1[i])

    elif (value1[i]<thirdline):
        group3forvalue1.append(value1[i])
    else:
        group4forvalue1.append(value1[i])
        
print("Equal width approach for {}. gene : ".format(random1))

print("\nThe attributes between {} and {} :".format(min(value1), firstline))
print(group1forvalue1)
print("\nThe attributes between {} and {} :".format(firstline, secondline))
print(group2forvalue1)
print("\nThe attributes between {} and {} :".format(secondline, thirdline))
print(group3forvalue1)
print("\nThe attributes between {} and {} :".format(thirdline, max(value1)))
print(group4forvalue1)

if(len(group1forvalue1)>0):
    x_axis1_1 = numpy.linspace(min(group1forvalue1), max(group1forvalue1),len(group1forvalue1))
    plt.scatter(x_axis1_1 , group1forvalue1, color='g')

if(len(group2forvalue1)>0):
    x_axis2_1 = numpy.linspace(min(group2forvalue1), max(group2forvalue1),len(group2forvalue1))
    plt.scatter(x_axis2_1 , group2forvalue1, color='r')

if(len(group3forvalue1)>0):
    x_axis3_1 = numpy.linspace(min(group3forvalue1), max(group3forvalue1),len(group3forvalue1))
    plt.scatter(x_axis3_1, group3forvalue1, color='b')

if(len(group4forvalue1)>0):
    x_axis4_1 = numpy.linspace(min(group4forvalue1), max(group4forvalue1),len(group4forvalue1))
    plt.scatter(x_axis4_1, group4forvalue1, color='hotpink')
   
plt.axvline(x = firstline, color = 'r')
plt.axvline(x = secondline, color = 'b')
plt.axvline(x = thirdline, color = 'hotpink')
plt.title("Equal width approach for {}. gene : ".format(random1))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")
plt.show()


#------------------------------------------------------------
#Calculating the width
width2 = (max(value2)-min(value2))/4
width2 =round(width2,1)
print("\n\nWidth for {}. gene is : {}".format(random2, width2) )

#Calculating the borders
firstline2 = min(value2)+width2
secondline2 = min(value2)+width2+width2
thirdline2 = min(value2)+width2+width2+width2

firstline2 = round(firstline2,1)
secondline2 = round(secondline2,1)
thirdline2 = round(thirdline2,1)

group1forvalue2 = []
group2forvalue2 = []
group3forvalue2 = []
group4forvalue2 = []

#Placing the values to the groups for value 2 list
for i in range(500):
    if (value2[i]< firstline2):
        group1forvalue2.append(value2[i])
        
    elif (value2[i]<secondline2):
        group2forvalue2.append(value2[i])

    elif (value2[i]<thirdline2):
        group3forvalue2.append(value2[i])
    else:
        group4forvalue2.append(value2[i])

print("Equal width approach for {}. gene : ".format(random2))
print("\nThe attributes between {} and {} :".format(min(value2), firstline2))
print(group1forvalue2)
print("\nThe attributes between {} and {} :".format(firstline2, secondline2))
print(group2forvalue2)
print("\nThe attributes between {} and {} :".format(secondline2, thirdline2))
print(group3forvalue2)
print("\nThe attributes between {} and {} :".format(thirdline2, max(value2)))
print(group4forvalue2)


if(len(group1forvalue2)>0):
    x_axis1_2 = numpy.linspace(min(group1forvalue2), max(group1forvalue2),len(group1forvalue2))
    plt.scatter(x_axis1_2, group1forvalue2, color='g')

if(len(group2forvalue2)>0):
    x_axis2_2 = numpy.linspace(min(group2forvalue2), max(group2forvalue2),len(group2forvalue2))
    plt.scatter(x_axis2_2, group2forvalue2, color='r')

if(len(group3forvalue2)>0):
    x_axis3_2 = numpy.linspace(min(group3forvalue2), max(group3forvalue2),len(group3forvalue2))
    plt.scatter(x_axis3_2, group3forvalue2, color='b')

if(len(group4forvalue2)>0):
    x_axis4_2 = numpy.linspace(min(group4forvalue2), max(group4forvalue2),len(group4forvalue2))
    plt.scatter(x_axis4_2, group4forvalue2, color='hotpink')

plt.axvline(x = firstline2, color = 'r')
plt.axvline(x = secondline2, color = 'b')
plt.axvline(x = thirdline2, color = 'hotpink')
plt.title("Equal width approach for {}. gene : ".format(random2))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")

plt.show()

#-------------------------------------------------------------
#Calculating the width
width3 = (max(value3)-min(value3))/4
width3 = round(width3,1)
print("\n\nWidth for {}. gene is : {}".format(random3, width3) )

#Calculating the borders
firstline3 = min(value3)+width3
secondline3 = min(value3)+width3+width3
thirdline3 = min(value3)+width3+width3+width3

firstline3 = round(firstline3,1)
secondline3 = round(secondline3,1)
thirdline3 = round(thirdline3,1)

group1forvalue3 = []
group2forvalue3 = []
group3forvalue3 = []
group4forvalue3 = []

#Placing the values to the groups for value 3 list
for i in range(500):
    if (value3[i]< firstline3):
        group1forvalue3.append(value3[i])
        
    elif (value3[i]<secondline3):
        group2forvalue3.append(value3[i])

    elif (value3[i]<thirdline3):
        group3forvalue3.append(value3[i])
    else:
        group4forvalue3.append(value3[i])

print("Equal width approach for {}. gene : ".format(random3))
print("\nThe attributes between {} and {} :".format(min(value3), firstline3))
print(group1forvalue3)
print("\nThe attributes between {} and {} :".format(firstline3, secondline3))
print(group2forvalue3)
print("\nThe attributes between {} and {} :".format(secondline3, thirdline3))
print(group3forvalue3)
print("\nThe attributes between {} and {} :".format(thirdline3, max(value3)))
print(group4forvalue3)


if(len(group1forvalue3)>0):
    x_axis1_3 = numpy.linspace(min(group1forvalue3), max(group1forvalue3),len(group1forvalue3))
    plt.scatter(x_axis1_3, group1forvalue3, color='g')

if(len(group2forvalue3)>0):
     x_axis2_3 = numpy.linspace(min(group2forvalue3), max(group2forvalue3),len(group2forvalue3))
     plt.scatter(x_axis2_3, group2forvalue3, color='r')

if(len(group3forvalue3)>0):
    x_axis3_3 = numpy.linspace(min(group3forvalue3), max(group3forvalue3),len(group3forvalue3))
    plt.scatter(x_axis3_3, group3forvalue3, color='b')

if(len(group4forvalue3)>0):
    x_axis4_3 = numpy.linspace(min(group4forvalue3), max(group4forvalue3),len(group4forvalue3))
    plt.scatter(x_axis4_3, group4forvalue3, color='hotpink')

plt.axvline(x = firstline3, color = 'r')
plt.axvline(x = secondline3, color = 'b')
plt.axvline(x = thirdline3, color = 'hotpink')
plt.title("Equal width approach for {}. gene : ".format(random3))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")

plt.show()

#Question1>a>II-----------------------------------------------------------------------------
#Calculating the frequency for any object
print(len(value1))
frequency = int(len(value1)/4)

print("\n\n\n\nThe Frequency is : ", frequency)

group1_forvalue1_forfrequency = []
group2_forvalue1_forfrequency = []
group3_forvalue1_forfrequency = []
group4_forvalue1_forfrequency = []



for i in range(frequency):
    group1_forvalue1_forfrequency.append(value1[i])
for i in range(frequency,2*frequency):
    group2_forvalue1_forfrequency.append(value1[i])
for i in range(2*frequency,3*frequency):
    group3_forvalue1_forfrequency.append(value1[i])
for i in range(3*frequency,(int(len(value1)))):
    group4_forvalue1_forfrequency.append(value1[i])
    
print("\n\nEqual frequency approach for {}. gene : ".format(random1))
print("\nThe attributes between {} and {} :".format(0, frequency))
print(group1_forvalue1_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency, frequency*2))
print(group2_forvalue1_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*2, frequency*3))
print(group3_forvalue1_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*3, len(value1)))
print(group4_forvalue1_forfrequency)




 
x1_1 = numpy.arange(0,frequency)
plt.scatter(x1_1, group1_forvalue1_forfrequency, color='g')

x1_2 = numpy.arange(frequency,2*frequency)
plt.scatter(x1_2, group2_forvalue1_forfrequency, color='r')

x1_3 = numpy.arange(2*frequency,3*frequency)
plt.scatter(x1_3, group3_forvalue1_forfrequency, color='b')

x1_4 = numpy.arange(3*frequency,4*frequency+1)
plt.scatter(x1_4, group4_forvalue1_forfrequency, color='hotpink')

plt.axvline(x = frequency, color = 'r')
plt.axvline(x = 2*frequency, color = 'b')
plt.axvline(x = 3*frequency, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene : ".format(random1))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")
plt.show()


group1_forvalue2_forfrequency = []
group2_forvalue2_forfrequency = []
group3_forvalue2_forfrequency = []
group4_forvalue2_forfrequency = []


for i in range(frequency):
    group1_forvalue2_forfrequency.append(value2[i])
for i in range(frequency,2*frequency):
    group2_forvalue2_forfrequency.append(value2[i])
for i in range(2*frequency,3*frequency):
    group3_forvalue2_forfrequency.append(value2[i])
for i in range(3*frequency,(int(len(value2)))):
    group4_forvalue2_forfrequency.append(value2[i])

print("\n\nEqual frequency approach for {}. gene : ".format(random2))
print("\nThe attributes between {} and {} :".format(0, frequency))
print(group1_forvalue2_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency, frequency*2))
print(group2_forvalue2_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*2, frequency*3))
print(group3_forvalue2_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*3, len(value2)))
print(group4_forvalue2_forfrequency)

x2_1 = numpy.arange(0,frequency)
plt.scatter(x2_1, group1_forvalue2_forfrequency, color='g')

x2_2 = numpy.arange(frequency,2*frequency)
plt.scatter(x2_2, group2_forvalue2_forfrequency, color='r')

x2_3 = numpy.arange(2*frequency,3*frequency)
plt.scatter(x2_3, group3_forvalue2_forfrequency, color='b')

x2_4 = numpy.arange(3*frequency,4*frequency+1)
plt.scatter(x2_4, group4_forvalue2_forfrequency, color='hotpink')

plt.axvline(x = frequency, color = 'r')
plt.axvline(x = 2*frequency, color = 'b')
plt.axvline(x = 3*frequency, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene : ".format(random2))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")

plt.show()



group1_forvalue3_forfrequency = []
group2_forvalue3_forfrequency = []
group3_forvalue3_forfrequency = []
group4_forvalue3_forfrequency = []


for i in range(frequency):
    group1_forvalue3_forfrequency.append(value3[i])
for i in range(frequency,2*frequency):
    group2_forvalue3_forfrequency.append(value3[i])
for i in range(2*frequency,3*frequency):
    group3_forvalue3_forfrequency.append(value3[i])
for i in range(3*frequency,(int(len(value1)))):
    group4_forvalue3_forfrequency.append(value3[i])

print("\n\nEqual frequency approach for {}. gene : ".format(random3))
print("\nThe attributes between {} and {} :".format(0, frequency))
print(group1_forvalue3_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency, frequency*2))
print(group2_forvalue3_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*2, frequency*3))
print(group3_forvalue3_forfrequency)
print("\nThe attributes between {} and {} :".format(frequency*3, len(value3)))
print(group4_forvalue3_forfrequency)

x3_1 = numpy.arange(0,frequency)
plt.scatter(x3_1, group1_forvalue3_forfrequency, color='g')

x3_2 = numpy.arange(frequency,2*frequency)
plt.scatter(x3_2, group2_forvalue3_forfrequency, color='r')

x3_3 = numpy.arange(2*frequency,3*frequency)
plt.scatter(x3_3, group3_forvalue3_forfrequency, color='b')

x3_4 = numpy.arange(3*frequency,4*frequency+1)
plt.scatter(x3_4, group4_forvalue3_forfrequency, color='hotpink')

plt.axvline(x = frequency, color = 'r')
plt.axvline(x = 2*frequency, color = 'b')
plt.axvline(x = 3*frequency, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene : ".format(random3))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")

plt.show()







#Question 2 - Attribute Similarity----------------------------------------------------------
#Part a>i The Euclidian Distance

random4 = random.randint(0,179)
random5 = random.randint(0,179)

value1 = data_list[random1]
value2 = data_list[random2]
value3 = data_list[random3]
value4 = data_list[random2]
value5 = data_list[random3]

#Euclidian Distance Between value1 and value2
answersquare_val1val2 = 0
for i in range(500):
    answersquare_val1val2 += (value1[i]-value2[i])**2

answer_val1val2 = answersquare_val1val2**0.5
answer_val1val2 = round(answer_val1val2,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random1, random2, answer_val1val2 ))

#Euclidian Distance Between value1 and value3
answersquare_val1val3 = 0
for i in range(500):
    answersquare_val1val3 += (value1[i]-value3[i])**2

answer_val1val3 = answersquare_val1val3**0.5
answer_val1val3 = round(answer_val1val3,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random1, random3, answer_val1val3 ))


#Euclidian Distance Between value1 and value4
answersquare_val1val4 = 0
for i in range(500):
    answersquare_val1val4 += (value1[i]-value4[i])**2

answer_val1val4 = answersquare_val1val4**0.5
answer_val1val4 = round(answer_val1val4,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random1, random4, answer_val1val4 ))

#Euclidian Distance Between value1 and value5
answersquare_val1val5 = 0
for i in range(500):
    answersquare_val1val5 += (value1[i]-value5[i])**2

answer_val1val5 = answersquare_val1val5**0.5
answer_val1val5 = round(answer_val1val5,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random1, random5, answer_val1val5 ))

#Euclidian Distance Between value2 and value3
answersquare_val2val3 = 0
for i in range(500):
    answersquare_val2val3 += (value2[i]-value3[i])**2

answer_val2val3 = answersquare_val2val3**0.5
answer_val2val3 = round(answer_val2val3,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random2, random3, answer_val2val3 ))

#Euclidian Distance Between value2 and value4
answersquare_val2val4 = 0
for i in range(500):
    answersquare_val2val4 += (value2[i]-value4[i])**2

answer_val2val4 = answersquare_val2val4**0.5
answer_val2val4 = round(answer_val2val4,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random2, random4, answer_val2val4 ))

#Euclidian Distance Between value2 and value5
answersquare_val2val5 = 0
for i in range(500):
    answersquare_val2val5 += (value2[i]-value5[i])**2

answer_val2val5 = answersquare_val2val5**0.5
answer_val2val5 = round(answer_val2val5,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random2, random5, answer_val2val5 ))

#Euclidian Distance Between value3 and value4
answersquare_val3val4 = 0
for i in range(500):
    answersquare_val3val4 += (value3[i]-value4[i])**2

answer_val3val4 = answersquare_val3val4**0.5
answer_val3val4 = round(answer_val3val4,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random3, random4, answer_val3val4 ))

#Euclidian Distance Between value3 and value5
answersquare_val3val5 = 0
for i in range(500):
    answersquare_val3val5 += (value3[i]-value5[i])**2

answer_val3val5 = answersquare_val3val5**0.5
answer_val3val5 = round(answer_val3val5,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random3, random5, answer_val3val5 ))

#Euclidian Distance Between value4 and value5
answersquare_val4val5 = 0
for i in range(500):
    answersquare_val4val5 += (value4[i]-value5[i])**2

answer_val4val5 = answersquare_val4val5**0.5
answer_val4val5 = round(answer_val4val5,1)
print("\nEuclidian Distance Between {}. gene and {}. gene is : {}".format(random4, random5, answer_val4val5 ))

print("\n\n\nCosine Similarity")

#Part A>II Cosine Similarity-----------------------------------------------------------
#Cosine Similarity Between Value 1 and Value 2
val1_val2_d1d2 = 0
val1_val2_d1d1 = 0
val1_val2_d2d2 = 0
for i in range(500):
    val1_val2_d1d2 += value1[i]*value2[i]
    val1_val2_d1d1 += value1[i]**2
    val1_val2_d2d2 += value2[i]**2

CosSimilarity_val1_val2 = val1_val2_d1d2 / ((val1_val2_d1d1**0.5) *  (val1_val2_d2d2**0.5) )
CosSimilarity_val1_val2 = round(CosSimilarity_val1_val2,1)
print("\nCosine Similarity between {} and {} is : {}".format(random1,random2,CosSimilarity_val1_val2))

    
#Cosine Similarity Between Value 1 and Value 3
val1_val3_d1d2 = 0
val1_val3_d1d1 = 0
val1_val3_d2d2 = 0
for i in range(500):
    val1_val3_d1d2 += value1[i]*value3[i]
    val1_val3_d1d1 += value1[i]**2
    val1_val3_d2d2 += value3[i]**2

CosSimilarity_val1_val3 = val1_val3_d1d2 / ((val1_val3_d1d1**0.5) *  (val1_val3_d2d2**0.5) )
CosSimilarity_val1_val3 = round(CosSimilarity_val1_val3,1)
print("\nCosine Similarity between {} and {} is : {}".format(random1,random3,CosSimilarity_val1_val3))


#Cosine Similarity Between Value 1 and Value 4
val1_val4_d1d2 = 0
val1_val4_d1d1 = 0
val1_val4_d2d2 = 0
for i in range(500):
    val1_val4_d1d2 += value1[i]*value4[i]
    val1_val4_d1d1 += value1[i]**2
    val1_val4_d2d2 += value4[i]**2

CosSimilarity_val1_val4 = val1_val4_d1d2 / ((val1_val4_d1d1**0.5) *  (val1_val4_d2d2**0.5) )
CosSimilarity_val1_val4 = round(CosSimilarity_val1_val4,1)
print("\nCosine Similarity between {} and {} is : {}".format(random1,random4,CosSimilarity_val1_val4))


#Cosine Similarity Between Value 1 and Value 5
val1_val5_d1d2 = 0
val1_val5_d1d1 = 0
val1_val5_d2d2 = 0
for i in range(500):
    val1_val5_d1d2 += value1[i]*value5[i]
    val1_val5_d1d1 += value1[i]**2
    val1_val5_d2d2 += value5[i]**2

CosSimilarity_val1_val5 = val1_val5_d1d2 / ((val1_val5_d1d1**0.5) *  (val1_val5_d2d2**0.5) )
CosSimilarity_val1_val5 = round(CosSimilarity_val1_val5,1)
print("\nCosine Similarity between {} and {} is : {}".format(random1,random5,CosSimilarity_val1_val5))


#Cosine Similarity Between Value 2 and Value 3
val2_val3_d1d2 = 0
val2_val3_d1d1 = 0
val2_val3_d2d2 = 0
for i in range(500):
    val2_val3_d1d2 += value2[i]*value3[i]
    val2_val3_d1d1 += value2[i]**2
    val2_val3_d2d2 += value3[i]**2

CosSimilarity_val2_val3 = val2_val3_d1d2 / ((val2_val3_d1d1**0.5) *  (val2_val3_d2d2**0.5) )
CosSimilarity_val2_val3 = round(CosSimilarity_val2_val3,1)
print("\nCosine Similarity between {} and {} is : {}".format(random2,random3,CosSimilarity_val2_val3))

#Cosine Similarity Between Value 2 and Value 4
val2_val4_d1d2 = 0
val2_val4_d1d1 = 0
val2_val4_d2d2 = 0
for i in range(500):
    val2_val4_d1d2 += value2[i]*value4[i]
    val2_val4_d1d1 += value2[i]**2
    val2_val4_d2d2 += value4[i]**2

CosSimilarity_val2_val4 = val2_val4_d1d2 / ((val2_val4_d1d1**0.5) *  (val2_val4_d2d2**0.5) )
CosSimilarity_val2_val4 = round(CosSimilarity_val2_val4,1)
print("\nCosine Similarity between {} and {} is : {}".format(random2,random4,CosSimilarity_val2_val4))

#Cosine Similarity Between Value 2 and Value 5
val2_val5_d1d2 = 0
val2_val5_d1d1 = 0
val2_val5_d2d2 = 0
for i in range(500):
    val2_val5_d1d2 += value2[i]*value4[i]
    val2_val5_d1d1 += value2[i]**2
    val2_val5_d2d2 += value4[i]**2

CosSimilarity_val2_val5 = val2_val5_d1d2 / ((val2_val5_d1d1**0.5) *  (val2_val5_d2d2**0.5) )
CosSimilarity_val2_val5 = round(CosSimilarity_val2_val5,1)
print("\nCosine Similarity between {} and {} is : {}".format(random2,random5,CosSimilarity_val2_val5))


#Cosine Similarity Between Value 3 and Value 4
val3_val4_d1d2 = 0
val3_val4_d1d1 = 0
val3_val4_d2d2 = 0
for i in range(500):
    val3_val4_d1d2 += value3[i]*value4[i]
    val3_val4_d1d1 += value3[i]**2
    val3_val4_d2d2 += value4[i]**2

CosSimilarity_val3_val4 = val3_val4_d1d2 / ((val3_val4_d1d1**0.5) *  (val3_val4_d2d2**0.5) )
CosSimilarity_val3_val4 = round(CosSimilarity_val3_val4,1)
print("\nCosine Similarity between {} and {} is : {}".format(random3,random4,CosSimilarity_val3_val4))

#Cosine Similarity Between Value 3 and Value 5
val3_val5_d1d2 = 0
val3_val5_d1d1 = 0
val3_val5_d2d2 = 0
for i in range(500):
    val3_val5_d1d2 += value3[i]*value5[i]
    val3_val5_d1d1 += value3[i]**2
    val3_val5_d2d2 += value5[i]**2

CosSimilarity_val3_val5 = val3_val5_d1d2 / ((val3_val5_d1d1**0.5) *  (val3_val5_d2d2**0.5) )
CosSimilarity_val3_val5 = round(CosSimilarity_val3_val5,1)
print("\nCosine Similarity between {} and {} is : {}".format(random3,random5,CosSimilarity_val3_val5))

#Cosine Similarity Between Value 4 and Value 5
val4_val5_d1d2 = 0
val4_val5_d1d1 = 0
val4_val5_d2d2 = 0
for i in range(500):
    val4_val5_d1d2 += value4[i]*value5[i]
    val4_val5_d1d1 += value4[i]**2
    val4_val5_d2d2 += value5[i]**2

CosSimilarity_val4_val5 = val4_val5_d1d2 / ((val4_val5_d1d1**0.5) *  (val4_val5_d2d2**0.5) )
CosSimilarity_val4_val5 = round(CosSimilarity_val4_val5,1)
print("\nCosine Similarity between {} and {} is : {}".format(random4,random5,CosSimilarity_val4_val5))


#Part A>III Correlation-----------------------------------------------------------


totalForVal1 = 0
totalForVal2 = 0
totalForVal3 = 0
totalForVal4 = 0
totalForVal5 = 0

n = len(value1)

for i in range(500):
    totalForVal1+= value1[i]
    totalForVal2+= value2[i]
    totalForVal3+= value3[i]
    totalForVal4+= value4[i]
    totalForVal5+= value5[i]

meanForVal1 = totalForVal1 / n
meanForVal2 = totalForVal2 / n
meanForVal3 = totalForVal3 / n
meanForVal4 = totalForVal4 / n
meanForVal5 = totalForVal5 / n

#The sum of the squares of the differences
total_val1 = 0
total_val2 = 0
total_val3 = 0
total_val4 = 0
total_val5 = 0

for i in range(500):
    total_val1 += (value1[i]-meanForVal1)**2
    total_val2 += (value2[i]-meanForVal2)**2
    total_val3 += (value3[i]-meanForVal3)**2
    total_val4 += (value4[i]-meanForVal4)**2
    total_val5 += (value5[i]-meanForVal5)**2


std_val1 =( 1/(n-1)* total_val1 ) **2
std_val2 =( 1/(n-1)* total_val2 ) **2
std_val3 =( 1/(n-1)* total_val3 ) **2
std_val4 =( 1/(n-1)* total_val4 ) **2
std_val5 =( 1/(n-1)* total_val5 ) **2

#p' of p
value1__ = []
value2__ = []
value3__ = []
value4__ = []
value5__ = []
for i in range(500):
    value1__.append((value1[i]-meanForVal1 )/std_val1)
    value2__.append((value2[i]-meanForVal2 )/std_val2)
    value3__.append((value3[i]-meanForVal3 )/std_val3)
    value4__.append((value4[i]-meanForVal4 )/std_val4)
    value5__.append((value5[i]-meanForVal5 )/std_val5)




#Correlation Between Value x' and Value y'
corBet_Val1andVal2 = 0
corBet_Val1andVal3 = 0
corBet_Val1andVal4 = 0
corBet_Val1andVal5 = 0
corBet_Val2andVal3 = 0
corBet_Val2andVal4 = 0
corBet_Val2andVal5 = 0
corBet_Val3andVal4 = 0
corBet_Val3andVal5 = 0
corBet_Val4andVal5 = 0
for i in range(500):
    corBet_Val1andVal2 += value1__[i]*value2__[i]
    corBet_Val1andVal3 += value1__[i]*value3__[i]
    corBet_Val1andVal4 += value1__[i]*value4__[i]
    corBet_Val1andVal5 += value1__[i]*value5__[i]
    corBet_Val2andVal3 += value2__[i]*value3__[i]
    corBet_Val2andVal4 += value2__[i]*value4__[i]
    corBet_Val2andVal5 += value2__[i]*value5__[i]
    corBet_Val3andVal4 += value3__[i]*value4__[i]
    corBet_Val3andVal5 += value3__[i]*value5__[i]
    corBet_Val4andVal5 += value4__[i]*value5__[i]




print("\n\n\nCorrelation Between {} and {} is : {}".format(random1,random2, corBet_Val1andVal2))
print("\nCorrelation Between {} and {} is : {}".format(random1,random3, corBet_Val1andVal3))
print("\nCorrelation Between {} and {} is : {}".format(random1,random4, corBet_Val1andVal4))
print("\nCorrelation Between {} and {} is : {}".format(random1,random5, corBet_Val1andVal5))
print("\nCorrelation Between {} and {} is : {}".format(random2,random3, corBet_Val2andVal3))
print("\nCorrelation Between {} and {} is : {}".format(random2,random4, corBet_Val2andVal4))
print("\nCorrelation Between {} and {} is : {}".format(random2,random5, corBet_Val2andVal5))
print("\nCorrelation Between {} and {} is : {}".format(random3,random4, corBet_Val3andVal4))
print("\nCorrelation Between {} and {} is : {}".format(random3,random5, corBet_Val3andVal5))
print("\nCorrelation Between {} and {} is : {}".format(random4,random5, corBet_Val4andVal5))




#Question 2 >Part B>Min - Max Normalization-----------------------------------------------------------
Normalized_data_list = [[0 for _ in range(500)] for _ in range(180)]

for i in range(180):
    num_of_positive=0
    num_of_negative=0
    for j in range(500):
        if (data_list[i][j] > 0):
            num_of_positive +=1
        if (data_list[i][j] < 0):
            num_of_negative +=1
    value = data_list[i]
    if (num_of_positive > 0 and num_of_negative>0):
        for k in range(500):
            z = (value[k]-min(value))/ (max(value)-min(value))*(1-(-1))+(-1)
            z= round(z,1)
            Normalized_data_list[i][k] = z

    elif (num_of_positive > 0 and num_of_negative ==0):
        for k in range(500):
            z = (value[k]-min(value))/ (max(value)-min(value))*(1-0)+(0)
            z= round(z,1)
            Normalized_data_list[i][k] = z
    else:
        for k in range(500):
            z = (value[k]-min(value))/ (max(value)-min(value))*(0-(-1))+(-1)
            z= round(z,1)
            Normalized_data_list[i][k] = z

print(Normalized_data_list[1])

#Discretization for Normalized Data
#Question2>B>-----------------------------------------------------------------------------
#Calculating width for 4 different groups

value1_N = Normalized_data_list[random1]
value2_N = Normalized_data_list[random2]
value3_N = Normalized_data_list[random3]

#Calculating the width for normalized data
width_N = (max(value1_N)-min(value1_N))/4
width_N =  round(width_N,1)
print("\n\nCalculating the width for normalized data : ")
print("\nWidth :", width_N)

#Calculating the borders
firstline_N = min(value1_N)+width_N
secondline_N = min(value1_N)+width_N+width_N
thirdline_N = min(value1_N)+width_N+width_N+width_N

firstline_N = round(firstline_N,1)
secondline_N = round(secondline_N,1)
thirdline_N = round(thirdline_N,1)

group1forvalue1_N = []
group2forvalue1_N = []
group3forvalue1_N = []
group4forvalue1_N = []

#Placing the values to the groups for value 1 list
for i in range(500):
    if (value1_N[i]< firstline_N):
        group1forvalue1_N.append(value1_N[i])
        
    elif (value1_N[i]<secondline_N):
        group2forvalue1_N.append(value1_N[i])

    elif (value1_N[i]<thirdline_N):
        group3forvalue1_N.append(value1_N[i])
    else:
        group4forvalue1_N.append(value1_N[i])
print("Equal width approach for {}. gene for normalized data:  ".format(random1))

print("\nThe attributes between {} and {} :".format(min(value1_N), firstline_N))
print(group1forvalue1_N)
print("\nThe attributes between {} and {} :".format(firstline_N, secondline_N))
print(group2forvalue1_N)
print("\nThe attributes between {} and {} :".format(secondline_N, thirdline_N))
print(group3forvalue1_N)
print("\nThe attributes between {} and {} :".format(thirdline_N, max(value1_N)))
print(group4forvalue1_N)

if(len(group1forvalue1_N)>0):
    x_axis1_1_N = numpy.linspace(min(group1forvalue1_N), max(group1forvalue1_N),len(group1forvalue1_N))
    plt.scatter(x_axis1_1_N, group1forvalue1_N, color='g')

if(len(group2forvalue1_N)>0):
    x_axis2_1_N = numpy.linspace(min(group2forvalue1_N), max(group2forvalue1_N),len(group2forvalue1_N))
    plt.scatter(x_axis2_1_N , group2forvalue1_N, color='r')

if(len(group3forvalue1_N)>0):
    x_axis3_1_N = numpy.linspace(min(group3forvalue1_N), max(group3forvalue1_N),len(group3forvalue1_N))
    plt.scatter(x_axis3_1_N, group3forvalue1_N, color='b')

if(len(group4forvalue1_N)>0):
    x_axis4_1_N = numpy.linspace(min(group4forvalue1_N), max(group4forvalue1_N),len(group4forvalue1_N))
    plt.scatter(x_axis4_1_N, group4forvalue1_N, color='hotpink')
   

plt.axvline(x = firstline_N, color = 'r')
plt.axvline(x = secondline_N, color = 'b')
plt.axvline(x = thirdline_N, color = 'hotpink')
plt.title("Equal width approach for {}. gene for normalized data: ".format(random1))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")
plt.show()


#------------------------------------------------------------
#Calculating the width for normalized data
width2_N = (max(value2_N)-min(value2_N))/4
width2_N = round(width2_N,1)
print("\n\nCalculating the width for normalized data : ")
print("\nWidth :", width2_N)
print(value2_N)
#Calculating the borders
firstline2_N = min(value2_N)+width2_N
secondline2_N = min(value2_N)+width2_N+width2_N
thirdline2_N = min(value2_N)+width2_N+width2_N+width2_N

firstline2_N = round(firstline2_N,1)
secondline2_N = round(secondline2_N,1)
thirdline2_N = round(thirdline2_N,1)

group1forvalue2_N = []
group2forvalue2_N = []
group3forvalue2_N = []
group4forvalue2_N = []

#Placing the values to the groups for value 2 list
for i in range(500):
    if (value2_N[i]< firstline2_N):
        group1forvalue2_N.append(value2_N[i])
        
    elif (value2_N[i]<secondline2_N):
        group2forvalue2_N.append(value2_N[i])

    elif (value2_N[i]<thirdline2):
        group3forvalue2_N.append(value2_N[i])
    else:
        group4forvalue2_N.append(value2_N[i])

print("Equal width approach for {}. gene for normalized data: ".format(random2))
print("\nThe attributes between {} and {} :".format(min(value2_N), firstline2_N))
print(group1forvalue2_N)
print("\nThe attributes between {} and {} :".format(firstline2_N, secondline2_N))
print(group2forvalue2_N)
print("\nThe attributes between {} and {} :".format(secondline2_N, thirdline2_N))
print(group3forvalue2_N)
print("\nThe attributes between {} and {} :".format(thirdline2_N, max(value2_N)))
print(group4forvalue2_N)


if(len(group1forvalue2_N)>0):
    x_axis1_2_N = numpy.linspace(min(group1forvalue2_N), max(group1forvalue2_N),len(group1forvalue2_N))
    plt.scatter(x_axis1_2_N, group1forvalue2_N, color='g')

if(len(group2forvalue2_N)>0):
    x_axis2_2_N = numpy.linspace(min(group2forvalue2_N), max(group2forvalue2_N),len(group2forvalue2_N))
    plt.scatter(x_axis2_2_N, group2forvalue2_N, color='r')

if(len(group3forvalue2_N)>0):
    x_axis3_2_N = numpy.linspace(min(group3forvalue2_N), max(group3forvalue2_N),len(group3forvalue2_N))
    plt.scatter(x_axis3_2_N, group3forvalue2_N, color='b')

if(len(group4forvalue2_N)>0):
    x_axis4_2_N = numpy.linspace(min(group4forvalue2_N), max(group4forvalue2_N),len(group4forvalue2_N))
    plt.scatter(x_axis4_2_N, group4forvalue2_N, color='hotpink')

plt.axvline(x = firstline2_N, color = 'r')
plt.axvline(x = secondline2_N, color = 'b')
plt.axvline(x = thirdline2_N, color = 'hotpink')
plt.title("Equal width approach for {}. gene for normalized data:  ".format(random2))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")

plt.show()

#-------------------------------------------------------------
#Calculating the width for normalized data
width3_N = (max(value3_N)-min(value3_N))/4
width3_N = round(width3_N,1)
print("\n\nCalculating the width for normalized data : ")
print("\nWidth :", width3_N)

#Calculating the borders
firstline3_N = min(value3_N)+width3_N
secondline3_N = min(value3_N)+width3_N+width3_N
thirdline3_N = min(value3_N)+width3_N+width3_N+width3_N

firstline3_N = round(firstline3_N,1)
secondline3_N = round(secondline3_N,1)
thirdline3_N = round(thirdline3_N,1)

group1forvalue3_N = []
group2forvalue3_N = []
group3forvalue3_N = []
group4forvalue3_N = []

#Placing the values to the groups for value 3 list
for i in range(500):
    if (value3_N[i]< firstline3_N):
        group1forvalue3_N.append(value3_N[i])
        
    elif (value3_N[i]<secondline3_N):
        group2forvalue3_N.append(value3_N[i])

    elif (value3_N[i]<thirdline3_N):
        group3forvalue3_N.append(value3_N[i])
    else:
        group4forvalue3_N.append(value3_N[i])

print("Equal width approach for {}. gene for normalized data: ".format(random3))
print("\nThe attributes between {} and {} :".format(min(value3_N), firstline3_N))
print(group1forvalue3_N)
print("\nThe attributes between {} and {} :".format(firstline3_N, secondline3_N))
print(group2forvalue3_N)
print("\nThe attributes between {} and {} :".format(secondline3_N, thirdline3_N))
print(group3forvalue3_N)
print("\nThe attributes between {} and {} :".format(thirdline3_N, max(value3_N)))
print(group4forvalue3_N)


if(len(group1forvalue3_N)>0):
    x_axis1_3_N = numpy.linspace(min(group1forvalue3_N), max(group1forvalue3_N),len(group1forvalue3_N))
    plt.scatter(x_axis1_3_N, group1forvalue3_N, color='g')

if(len(group2forvalue3_N)>0):
     x_axis2_3_N = numpy.linspace(min(group2forvalue3_N), max(group2forvalue3_N),len(group2forvalue3_N))
     plt.scatter(x_axis2_3_N, group2forvalue3_N, color='r')

if(len(group3forvalue3_N)>0):
    x_axis3_3_N = numpy.linspace(min(group3forvalue3_N), max(group3forvalue3_N),len(group3forvalue3_N))
    plt.scatter(x_axis3_3_N, group3forvalue3_N, color='b')

if(len(group4forvalue3_N)>0):
    x_axis4_3_N = numpy.linspace(min(group4forvalue3_N), max(group4forvalue3_N),len(group4forvalue3_N))
    plt.scatter(x_axis4_3_N, group4forvalue3_N, color='hotpink')

plt.axvline(x = firstline3_N, color = 'r')
plt.axvline(x = secondline3_N, color = 'b')
plt.axvline(x = thirdline3_N, color = 'hotpink')
plt.title("Equal width approach for {}. gene for normalized data: ".format(random3))
plt.xlabel("Width")
plt.ylabel("The attribute value of the gene")

plt.show()



#Question1>a>II-----------------------------------------------------------------------------
#Calculating the frequency for any object
frequency_N = int(len(value1_N)/4)

print("\n\n\n\nThe Frequency is for normalized data: ", frequency)

group1_forvalue1_forfrequency_N = []
group2_forvalue1_forfrequency_N = []
group3_forvalue1_forfrequency_N = []
group4_forvalue1_forfrequency_N = []



for i in range(frequency_N):
    group1_forvalue1_forfrequency_N.append(value1_N[i])
for i in range(frequency_N,2*frequency_N):
    group2_forvalue1_forfrequency_N.append(value1_N[i])
for i in range(2*frequency_N,3*frequency_N):
    group3_forvalue1_forfrequency_N.append(value1_N[i])
for i in range(3*frequency_N,(int(len(value1_N)))):
    group4_forvalue1_forfrequency_N.append(value1_N[i])
    
print("\n\nEqual frequency approach for {}. gene for normalized data: ".format(random1))
print("\nThe attributes between {} and {} :".format(0, frequency_N))
print(group1_forvalue1_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N, frequency_N*2))
print(group2_forvalue1_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*2, frequency_N*3))
print(group3_forvalue1_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*3, len(value1_N)))
print(group4_forvalue1_forfrequency_N)




 
x1_1_N = numpy.arange(0,frequency_N)
plt.scatter(x1_1_N, group1_forvalue1_forfrequency_N, color='g')

x1_2_N = numpy.arange(frequency_N,2*frequency_N)
plt.scatter(x1_2_N, group2_forvalue1_forfrequency_N, color='r')

x1_3_N = numpy.arange(2*frequency_N,3*frequency_N)
plt.scatter(x1_3_N, group3_forvalue1_forfrequency_N, color='b')

x1_4_N = numpy.arange(3*frequency_N,4*frequency_N)
plt.scatter(x1_4_N, group4_forvalue1_forfrequency_N, color='hotpink')

plt.axvline(x = frequency_N, color = 'r')
plt.axvline(x = 2*frequency_N, color = 'b')
plt.axvline(x = 3*frequency_N, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene for normalized data: ".format(random1))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")
plt.show()


group1_forvalue2_forfrequency_N = []
group2_forvalue2_forfrequency_N = []
group3_forvalue2_forfrequency_N = []
group4_forvalue2_forfrequency_N = []


for i in range(frequency_N):
    group1_forvalue2_forfrequency_N.append(value2_N[i])
for i in range(frequency_N,2*frequency_N):
    group2_forvalue2_forfrequency_N.append(value2_N[i])
for i in range(2*frequency_N,3*frequency_N):
    group3_forvalue2_forfrequency_N.append(value2_N[i])
for i in range(3*frequency_N,(int(len(value2_N)))):
    group4_forvalue2_forfrequency_N.append(value2_N[i])

print("\n\nEqual frequency approach for {}. gene for normalized data:  ".format(random2))
print("\nThe attributes between {} and {} :".format(0, frequency_N))
print(group1_forvalue2_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N, frequency_N*2))
print(group2_forvalue2_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*2, frequency_N*3))
print(group3_forvalue2_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*3, len(value2_N)))
print(group4_forvalue2_forfrequency_N)

x2_1_N = numpy.arange(0,frequency_N)
plt.scatter(x2_1_N, group1_forvalue2_forfrequency_N, color='g')

x2_2_N = numpy.arange(frequency_N,2*frequency_N)
plt.scatter(x2_2_N, group2_forvalue2_forfrequency_N, color='r')

x2_3_N = numpy.arange(2*frequency_N,3*frequency_N)
plt.scatter(x2_3_N, group3_forvalue2_forfrequency_N, color='b')

x2_4_N = numpy.arange(3*frequency_N,4*frequency_N)
plt.scatter(x2_4_N, group4_forvalue2_forfrequency_N, color='hotpink')

plt.axvline(x = frequency_N, color = 'r')
plt.axvline(x = 2*frequency_N, color = 'b')
plt.axvline(x = 3*frequency_N, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene for normalized data: ".format(random2))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")

plt.show()



group1_forvalue3_forfrequency_N = []
group2_forvalue3_forfrequency_N = []
group3_forvalue3_forfrequency_N = []
group4_forvalue3_forfrequency_N = []


for i in range(frequency_N):
    group1_forvalue3_forfrequency_N.append(value3_N[i])
for i in range(frequency_N,2*frequency_N):
    group2_forvalue3_forfrequency_N.append(value3_N[i])
for i in range(2*frequency_N,3*frequency_N):
    group3_forvalue3_forfrequency_N.append(value3_N[i])
for i in range(3*frequency_N,(int(len(value1_N)))):
    group4_forvalue3_forfrequency_N.append(value3_N[i])

print("\n\nEqual frequency approach for {}. gene for normalized data: ".format(random3))
print("\nThe attributes between {} and {} :".format(0, frequency_N))
print(group1_forvalue3_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N, frequency_N*2))
print(group2_forvalue3_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*2, frequency_N*3))
print(group3_forvalue3_forfrequency_N)
print("\nThe attributes between {} and {} :".format(frequency_N*3, len(value3_N)))
print(group4_forvalue3_forfrequency_N)

x3_1_N = numpy.arange(0,frequency_N)
plt.scatter(x3_1_N, group1_forvalue3_forfrequency_N, color='g')

x3_2_N = numpy.arange(frequency_N,2*frequency_N)
plt.scatter(x3_2_N, group2_forvalue3_forfrequency_N, color='r')

x3_3_N = numpy.arange(2*frequency_N,3*frequency_N)
plt.scatter(x3_3_N, group3_forvalue3_forfrequency_N, color='b')

x3_4_N = numpy.arange(3*frequency_N,4*frequency_N)
plt.scatter(x3_4_N, group4_forvalue3_forfrequency_N, color='hotpink')

plt.axvline(x = frequency_N, color = 'r')
plt.axvline(x = 2*frequency_N, color = 'b')
plt.axvline(x = 3*frequency_N, color = 'hotpink')
plt.title("Equal frequency approach for {}. gene for normalized data: ".format(random3))
plt.xlabel("Frequency")
plt.ylabel("The attribute value of the gene")

plt.show()
    

#Question 2 - Attribute Similarity for Normalized Data----------------------------------------------------------
#Part B> The Euclidian Distance for normalized data


value4_N = Normalized_data_list[random4]
value5_N = Normalized_data_list[random5]

#Euclidian Distance Between value1 and value2 for normalized data
answersquare_val1val2_N = 0
for i in range(500):
    answersquare_val1val2_N += (value1_N[i]-value2_N[i])**2

answer_val1val2_N = answersquare_val1val2_N**0.5
answer_val1val2_N = round(answer_val1val2_N,1)
print("\n\nEuclidian Distance for Normalized Data-----------------------------------------------------------------")
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random1, random2, answer_val1val2_N ))

#Euclidian Distance Between value1 and value3 for normalized data
answersquare_val1val3_N = 0
for i in range(500):
    answersquare_val1val3_N += (value1_N[i]-value3_N[i])**2

answer_val1val3_N = answersquare_val1val3_N**0.5
answer_val1val3_N = round(answer_val1val3_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random1, random3, answer_val1val3_N ))


#Euclidian Distance Between value1 and value4 for normalized data
answersquare_val1val4_N = 0
for i in range(500):
    answersquare_val1val4_N += (value1_N[i]-value4_N[i])**2

answer_val1val4_N = answersquare_val1val4_N**0.5
answer_val1val4_N = round(answer_val1val4_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random1, random4, answer_val1val4_N ))

#Euclidian Distance Between value1 and value5 for normalized data
answersquare_val1val5_N = 0
for i in range(500):
    answersquare_val1val5_N += (value1_N[i]-value5_N[i])**2

answer_val1val5_N = answersquare_val1val5_N**0.5
answer_val1val5_N = round(answer_val1val5_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random1, random5, answer_val1val5_N ))

#Euclidian Distance Between value2 and value3 for normalized data
answersquare_val2val3_N = 0
for i in range(500):
    answersquare_val2val3_N += (value2_N[i]-value3_N[i])**2

answer_val2val3_N = answersquare_val2val3_N**0.5
answer_val2val3_N = round(answer_val2val3_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random2, random3, answer_val2val3_N ))

#Euclidian Distance Between value2 and value4 for normalized data
answersquare_val2val4_N = 0
for i in range(500):
    answersquare_val2val4_N += (value2_N[i]-value4_N[i])**2

answer_val2val4_N = answersquare_val2val4_N**0.5
answer_val2val4_N = round(answer_val2val4_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random2, random4, answer_val2val4_N ))
 
#Euclidian Distance Between value2 and value5 for normalized data
answersquare_val2val5_N = 0
for i in range(500):
    answersquare_val2val5_N += (value2_N[i]-value5_N[i])**2

answer_val2val5_N = answersquare_val2val5_N**0.5
answer_val2val5_N = round(answer_val2val5_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random2, random5, answer_val2val5_N ))

#Euclidian Distance Between value3 and value4 for normalized data
answersquare_val3val4_N = 0
for i in range(500):
    answersquare_val3val4_N += (value3_N[i]-value4_N[i])**2

answer_val3val4_N = answersquare_val3val4_N**0.5
answer_val3val4_N = round(answer_val3val4_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random3, random4, answer_val3val4_N ))

#Euclidian Distance Between value3 and value5 for normalized data
answersquare_val3val5_N = 0
for i in range(500):
    answersquare_val3val5_N += (value3_N[i]-value5_N[i])**2

answer_val3val5_N = answersquare_val3val5_N**0.5
answer_val3val5_N = round(answer_val3val5_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random3, random5, answer_val3val5_N ))

#Euclidian Distance Between value4 and value5 for normalized data
answersquare_val4val5_N = 0
for i in range(500):
    answersquare_val4val5_N += (value4_N[i]-value5_N[i])**2

answer_val4val5_N = answersquare_val4val5_N**0.5
answer_val4val5_N = round(answer_val4val5_N,1)
print("\nEuclidian Distance Between {}. gene and {}. gene for normalized data is : {}".format(random4, random5, answer_val4val5_N ))

print("\n\n\nCosine Similarity for normalized data-----------------------------------------------------------------")

#Part B> Cosine Similarity for normalized data-----------------------------------------------------------
#Cosine Similarity Between Value 1 and Value 2 for normalized data
val1_val2_d1d2_N = 0
val1_val2_d1d1_N = 0
val1_val2_d2d2_N = 0
for i in range(500):
    val1_val2_d1d2_N += value1_N[i]*value2_N[i]
    val1_val2_d1d1_N += value1_N[i]**2
    val1_val2_d2d2_N += value2_N[i]**2

CosSimilarity_val1_val2_N = val1_val2_d1d2_N / ((val1_val2_d1d1_N**0.5) *  (val1_val2_d2d2_N**0.5) )
CosSimilarity_val1_val2_N = round(CosSimilarity_val1_val2_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random1,random2,CosSimilarity_val1_val2_N))

    
#Cosine Similarity Between Value 1 and Value 3 for normalized data
val1_val3_d1d2_N = 0
val1_val3_d1d1_N = 0
val1_val3_d2d2_N = 0
for i in range(500):
    val1_val3_d1d2_N += value1_N[i]*value3_N[i]
    val1_val3_d1d1_N += value1_N[i]**2
    val1_val3_d2d2_N += value3_N[i]**2

CosSimilarity_val1_val3_N = val1_val3_d1d2_N / ((val1_val3_d1d1_N**0.5) *  (val1_val3_d2d2_N**0.5) )
CosSimilarity_val1_val3_N = round(CosSimilarity_val1_val3_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random1,random3,CosSimilarity_val1_val3_N))


#Cosine Similarity Between Value 1 and Value 4 for normalized data
val1_val4_d1d2_N = 0
val1_val4_d1d1_N = 0
val1_val4_d2d2_N = 0
for i in range(500):
    val1_val4_d1d2_N += value1_N[i]*value4_N[i]
    val1_val4_d1d1_N += value1_N[i]**2
    val1_val4_d2d2_N += value4_N[i]**2

CosSimilarity_val1_val4_N = val1_val4_d1d2_N / ((val1_val4_d1d1_N**0.5) *  (val1_val4_d2d2_N**0.5) )
CosSimilarity_val1_val4_N = round(CosSimilarity_val1_val4_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random1,random4,CosSimilarity_val1_val4_N))


#Cosine Similarity Between Value 1 and Value 5 for normalized data
val1_val5_d1d2_N = 0
val1_val5_d1d1_N = 0
val1_val5_d2d2_N = 0
for i in range(500):
    val1_val5_d1d2_N += value1_N[i]*value5_N[i]
    val1_val5_d1d1_N += value1_N[i]**2
    val1_val5_d2d2_N += value5_N[i]**2

CosSimilarity_val1_val5_N = val1_val5_d1d2_N / ((val1_val5_d1d1_N**0.5) *  (val1_val5_d2d2_N**0.5) )
CosSimilarity_val1_val5_N = round(CosSimilarity_val1_val5_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random1,random5,CosSimilarity_val1_val5_N))


#Cosine Similarity Between Value 2 and Value 3 for normalized data
val2_val3_d1d2_N = 0
val2_val3_d1d1_N = 0
val2_val3_d2d2_N = 0
for i in range(500):
    val2_val3_d1d2_N += value2_N[i]*value3_N[i]
    val2_val3_d1d1_N += value2_N[i]**2
    val2_val3_d2d2_N += value3_N[i]**2

CosSimilarity_val2_val3_N = val2_val3_d1d2_N / ((val2_val3_d1d1_N**0.5) *  (val2_val3_d2d2_N**0.5) )
CosSimilarity_val2_val3_N = round(CosSimilarity_val2_val3_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random2,random3,CosSimilarity_val2_val3_N))

#Cosine Similarity Between Value 2 and Value 4 for normalized data
val2_val4_d1d2_N = 0
val2_val4_d1d1_N = 0
val2_val4_d2d2_N = 0
for i in range(500):
    val2_val4_d1d2_N += value2_N[i]*value4_N[i]
    val2_val4_d1d1_N += value2_N[i]**2
    val2_val4_d2d2_N += value4_N[i]**2

CosSimilarity_val2_val4_N = val2_val4_d1d2_N / ((val2_val4_d1d1_N**0.5) *  (val2_val4_d2d2_N**0.5) )
CosSimilarity_val2_val4_N = round(CosSimilarity_val2_val4_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random2,random4,CosSimilarity_val2_val4_N))

#Cosine Similarity Between Value 2 and Value 5 for normalized data
val2_val5_d1d2_N = 0
val2_val5_d1d1_N = 0
val2_val5_d2d2_N = 0
for i in range(500):
    val2_val5_d1d2_N += value2_N[i]*value4_N[i]
    val2_val5_d1d1_N += value2_N[i]**2
    val2_val5_d2d2_N += value4_N[i]**2

CosSimilarity_val2_val5_N = val2_val5_d1d2_N / ((val2_val5_d1d1_N**0.5) *  (val2_val5_d2d2_N**0.5) )
CosSimilarity_val2_val5_N = round(CosSimilarity_val2_val5_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random2,random5,CosSimilarity_val2_val5_N))


#Cosine Similarity Between Value 3 and Value 4 for normalized data
val3_val4_d1d2_N = 0
val3_val4_d1d1_N = 0
val3_val4_d2d2_N = 0
for i in range(500):
    val3_val4_d1d2_N += value3_N[i]*value4_N[i]
    val3_val4_d1d1_N += value3_N[i]**2
    val3_val4_d2d2_N += value4_N[i]**2

CosSimilarity_val3_val4_N = val3_val4_d1d2_N / ((val3_val4_d1d1_N**0.5) *  (val3_val4_d2d2_N**0.5) )
CosSimilarity_val3_val4_N = round(CosSimilarity_val3_val4_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random3,random4,CosSimilarity_val3_val4_N))

#Cosine Similarity Between Value 3 and Value 5 for normalized data
val3_val5_d1d2_N = 0
val3_val5_d1d1_N = 0
val3_val5_d2d2_N = 0
for i in range(500):
    val3_val5_d1d2_N += value3_N[i]*value5_N[i]
    val3_val5_d1d1_N += value3_N[i]**2
    val3_val5_d2d2_N += value5_N[i]**2

CosSimilarity_val3_val5_N = val3_val5_d1d2_N / ((val3_val5_d1d1_N**0.5) *  (val3_val5_d2d2_N**0.5) )
CosSimilarity_val3_val5_N = round(CosSimilarity_val3_val5_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random3,random5,CosSimilarity_val3_val5_N))

#Cosine Similarity Between Value 4 and Value 5 for normalized data
val4_val5_d1d2_N = 0
val4_val5_d1d1_N = 0
val4_val5_d2d2_N = 0
for i in range(500):
    val4_val5_d1d2_N += value4_N[i]*value5_N[i]
    val4_val5_d1d1_N += value4_N[i]**2
    val4_val5_d2d2_N += value5_N[i]**2

CosSimilarity_val4_val5_N = val4_val5_d1d2_N / ((val4_val5_d1d1_N**0.5) *  (val4_val5_d2d2_N**0.5) )
CosSimilarity_val4_val5_N = round(CosSimilarity_val4_val5_N,1)
print("\nCosine Similarity between {} and {} for normalized data is : {}".format(random4,random5,CosSimilarity_val4_val5_N))


#Part B>Correlation for normalized data-----------------------------------------------------------


totalForVal1_N = 0
totalForVal2_N = 0
totalForVal3_N = 0
totalForVal4_N = 0
totalForVal5_N = 0

n_N = len(value1_N)

for i in range(500):
    totalForVal1_N+= value1_N[i]
    totalForVal2_N+= value2_N[i]
    totalForVal3_N+= value3_N[i]
    totalForVal4_N+= value4_N[i]
    totalForVal5_N+= value5_N[i]

meanForVal1_N = totalForVal1_N / n_N
meanForVal2_N = totalForVal2_N / n_N
meanForVal3_N = totalForVal3_N / n_N
meanForVal4_N = totalForVal4_N / n_N
meanForVal5_N = totalForVal5_N / n_N

#The sum of the squares of the differences for normalized data
total_val1_N = 0
total_val2_N = 0
total_val3_N = 0
total_val4_N = 0
total_val5_N = 0

for i in range(500):
    total_val1_N += (value1_N[i]-meanForVal1_N)**2
    total_val2_N += (value2_N[i]-meanForVal2_N)**2
    total_val3_N += (value3_N[i]-meanForVal3_N)**2
    total_val4_N += (value4_N[i]-meanForVal4_N)**2
    total_val5_N += (value5_N[i]-meanForVal5_N)**2


std_val1_N =( 1/(n_N-1)* total_val1_N ) **2
std_val2_N =( 1/(n_N-1)* total_val2_N ) **2
std_val3_N =( 1/(n_N-1)* total_val3_N ) **2
std_val4_N =( 1/(n_N-1)* total_val4_N ) **2
std_val5_N =( 1/(n_N-1)* total_val5_N ) **2

#p' of p
value1___N = []
value2___N = []
value3___N = []
value4___N = []
value5___N = []
for i in range(500):
    value1___N.append((value1_N[i]-meanForVal1_N )/std_val1_N)
    value2___N.append((value2_N[i]-meanForVal2_N )/std_val2_N)
    value3___N.append((value3_N[i]-meanForVal3_N )/std_val3_N)
    value4___N.append((value4_N[i]-meanForVal4_N )/std_val4_N)
    value5___N.append((value5_N[i]-meanForVal5_N )/std_val5_N)




#Correlation Between Value x' and Value y' for normalized data
corBet_Val1andVal2_N = 0
corBet_Val1andVal3_N = 0
corBet_Val1andVal4_N = 0
corBet_Val1andVal5_N = 0
corBet_Val2andVal3_N = 0
corBet_Val2andVal4_N = 0
corBet_Val2andVal5_N = 0
corBet_Val3andVal4_N = 0
corBet_Val3andVal5_N = 0
corBet_Val4andVal5_N = 0
for i in range(500):
    corBet_Val1andVal2_N += value1___N[i]*value2___N[i]
    corBet_Val1andVal3_N += value1___N[i]*value3___N[i]
    corBet_Val1andVal4_N += value1___N[i]*value4___N[i]
    corBet_Val1andVal5_N += value1___N[i]*value5___N[i]
    corBet_Val2andVal3_N += value2___N[i]*value3___N[i]
    corBet_Val2andVal4_N += value2___N[i]*value4___N[i]
    corBet_Val2andVal5_N += value2___N[i]*value5___N[i]
    corBet_Val3andVal4_N += value3___N[i]*value4___N[i]
    corBet_Val3andVal5_N += value3___N[i]*value5___N[i]
    corBet_Val4andVal5_N += value4___N[i]*value5___N[i]



print("\n\nCorrelation for Normalized Data--------------------------------------------------------------------------")
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random1,random2, corBet_Val1andVal2_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random1,random3, corBet_Val1andVal3_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random1,random4, corBet_Val1andVal4_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random1,random5, corBet_Val1andVal5_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random2,random3, corBet_Val2andVal3_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random2,random4, corBet_Val2andVal4_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random2,random5, corBet_Val2andVal5_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random3,random4, corBet_Val3andVal4_N))
print("\nCorrelation Between {} and {} for normalized data is : {}".format(random3,random5, corBet_Val3andVal5_N))
print("\nCorrelation Between {} and {}for normalized data is : {}".format(random4,random5, corBet_Val4andVal5_N))





























