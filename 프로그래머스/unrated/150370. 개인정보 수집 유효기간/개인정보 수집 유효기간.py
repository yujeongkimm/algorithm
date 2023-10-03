def dateToTime(date):
    year,month,day=map(int,date.split("."))
    dates = day + month*28 + year*12*28
    return dates

def solution(today, terms, privacies):
    answer = []
    
    today_dates = dateToTime(today)

    dict={}
    for term in terms:
        code,month=term.split()
        dict[code]=int(month)
    
    for i in range(len(privacies)):
        dates = dateToTime(privacies[i].split()[0])
        month = dict[privacies[i].split()[1]]
        dates += int(month)*28
        print(today_dates,dates)
        if today_dates>dates-1:
            answer.append(i+1)
        
    return answer