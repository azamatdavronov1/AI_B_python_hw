import statistics


def enrollment_stats(nameOfU, numberOfS, tuitionFees):
    totalStudents = []
    totalTuitionFees = []
    for i in numberOfS:
        totalStudents.append(i)
    for j in tuitionFees:
        totalTuitionFees.append(j)
    return totalStudents, totalTuitionFees


def mean(lst):
    mean = sum(lst) / len(lst)
    return float(format(mean, '.2f'))


def median(lst):
    median = statistics.median(lst)
    return float(format(median, '.2f'))


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


studentNumbers = [row[1] for row in universities]
totalFees = [row[2] for row in universities]
print("Total Students: ", sum(studentNumbers))
print("Total Fees: ", sum(totalFees))
print()
print("Student mean: ", mean(studentNumbers))
print("Student median: ", median(studentNumbers))
print()
print("Tuiton mean: ", mean(studentNumbers))
print("Student median: ", median(studentNumbers))







