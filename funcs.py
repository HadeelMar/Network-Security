def sep_posts(location):
    temp = open(location)
    temp1 = temp.read()
    posts = temp1.split('</p>')
    return posts

def find_birthday(posts):
    interest=[]
    for i in range(len(posts)):
        if "Birthday" in posts[i]:
            interest.append(posts[i])
    days = []
    count = []
    for i in range(len(interest)):
        post=interest[i]
        index_end =post.index('at ')
        date = post[21:index_end]
        if date not in days:
            days.append(date)
            count.append(1)
        else:
            index = days.index(date)
            count[index] = count[index]+1
    temp = days[count.index(max(count))]
    temp = temp.split(', ')
    temp = temp[1]
    return temp

def find_year(posts):
    years = []
    count = []
    for i in range(len(posts)):
        if "Birthday" in posts[i]:
            str = posts[i]
            temp = [int(s) for s in str.split() if s.isdigit()]
            if len(temp)>1:
                print str
                year = int(temp[0])-int(temp[1])
                if year not in years:
                    years.append(year)
                    count.append(1)
                else:
                    index = years.index(year)
                    count[index] = count[index]+1
    if not temp:
	return 0
    else:
    	temp = years[count.index(max(count))]
    	return temp
def replace_special_char(string):
    string = string.replace('(','')
    string = string.replace(')','')
    string = string.replace(':','')
    string = string.replace('!','')
    string = string.replace('#','')
    string = string.replace(';','')
    string = string.replace('<',' ')
    string = string.replace('>',' ')
    return string

def find_high_school(posts):
    schools=[]
    count=[]
    for i in range(len(posts)):
        if "High" in posts[i]:
            str = posts[i]
            str = replace_special_char(str)
            temp = str.split(' ')
            index = temp.index("High")
            if index>0:
                h_s = temp[index-1]+' '+temp[index]
                if h_s not in schools:
                    schools.append(h_s)
                    count.append(1)
                else:
                    index1 = schools.index(h_s)
                    count[index1] = count[index1]+1
            if index>1:
                h_s = temp[index-2]+' '+temp[index-1]+' '+temp[index]
                if h_s not in schools:
                    schools.append(h_s)
                    count.append(1)
                else:
                    index1 = schools.index(h_s)
                    count[index1] = count[index1]+1
    if not schools:
	return "None"
    else:
    	temp = schools[count.index(max(count))]
    	return schools,count

def find_year_graduation(posts):
    years = []
    count = []
    temp=[]
    for i in range(len(posts)):
        if "Gradua" in posts[i]:
            stri = posts[i]
            temp = [int(s) for s in stri.split() if s.isdigit()]
            if len(temp)>0:
                year = int(temp[0])-18
                if year not in years:
                    years.append(year)
                    count.append(1)
                else:
                    index = years.index(year)
                    count[index] = count[index]+1
    if not temp:
	return 0
    else:
    	temp = years[count.index(max(count))]
    	return temp
def find_emails(posts):
    emails=[]
    count=[]
    for i in range(len(posts)):
        if "@" in posts[i]:
            str = posts[i]
            str = replace_special_char(str)
            temp = str.split(' ')
            for j in range(len(temp)):
                words = temp[j]
                if "@" in words:
                    index = j
            if index>0:
                h_s = temp[index]
                if h_s not in emails:
                    emails.append(h_s)
                    count.append(1)
                else:
                    index1 = emails.index(h_s)
                    count[index1] = count[index1]+1
    if not emails:
	return "None"
    else:
    	temp = emails[count.index(max(count))]
    	return emails,count
