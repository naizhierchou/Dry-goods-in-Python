def make_avg():
    data=list()
    def addnumber(value):
        data.append(value)
        total=sum(data)
        return total/len(data)
    return addnumber
myavg=make_avg()
print(myavg(100))
print(myavg(200))