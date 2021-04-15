#!/usr/bin/env python
# coding: utf-8

# 
# Exploring Hackers News Posts
# 
# Hacker News is a popular site where technology related stories (or 'posts') are voted and commented upon. 
# 
# The goal of this project is to compare two different types of posts on the website:
# 1. Ask HN : posts that are submitted to as k a specific question
# 2. Show HN: posts that share a piece of information
# 
# We will be answering two questions:
# 1. Do Ask HN or Show HN receive more comments on average?
# 2. Do posts created at a certain time receive more comments on average?
# 

# In[1]:


# reading the data
from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)

hn[:5]


# In[2]:


#removing the headers
headers = hn[1]
hn = hn[1:]
hn[:5]


# In[3]:


# Separate posts beginning with Ask HN and Show HN (and case variations) into two different lists next.ask_posts = []
show_posts = []
other_posts = []
for row in hn:
    title = row [1]
    title = title.lower()

    if title.startswith("ask hn"):
        ask_posts.append(row)
    elif title.startswith("show hn"):
         show_posts.append(row)
    else: 
        other_posts.append(row)
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[4]:


# Calculate the average number of comments `Ask HN` posts receive.

total_ask_comments = 0

for row in ask_posts:
    total_ask_comments += int(row[4])
avg_ask_comments = (total_ask_comments) / len(ask_posts)
print(avg_ask_comments)

## Calculate the average number of comments `Ask HN` posts receive.

total_show_comments = 0
for row in show_posts:
    total_show_comments += int(row[4])
avg_show_comments = (total_show_comments) / len(show_posts)
print(avg_show_comments)


# avg_ask_comments receieve more comments on average, so let's focus our analysis on these.

# Determine if ask posts created at a certain time are more likely to attract comments.

# In[19]:


#changed the date format to avoid error

for row in ask_posts:
    date_time = row[6]
    date_time = date_time.replace("-","/")
    row[6] = date_time

#creating a list to extract the date and time each ask post was created, and number of comments on each post    

import datetime as dt
result_list = []

for row in ask_posts:
    created_at = row[6]
    num_ask_comments = int(row[4])
    result_list.append([created_at, num_ask_comments])

#counting the number of comments by hour
counts_by_hour = {}
comments_by_hour = {}

for row1 in result_list:
    dtime = dt.datetime.strptime(row1[0], "%m/%d/%Y %H:%M")
    hour = dtime.strftime("%H") 
    ask_comments = row1[1]
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = ask_comments 
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += ask_comments

comments_by_hour


    
    
    
    


# In[18]:


# calculating the average number of comments per post for posts created during each hour of the day.

avg_by_hour = []
for hour in comments_by_hour:
    avg = comments_by_hour[hour] / counts_by_hour[hour]
    avg_by_hour.append([hour, avg])    

avg_by_hour


# The result is a list of lists in which the first element is the hour and the second element is the average number of comments per post. Next, Lets sort the list of lists and print the five highest values in a format that's easier to read.

# In[23]:


swap_avg_by_hour = []

for row in avg_by_hour:
    first_element = row[1]
    second_element = row[0]
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour) 


# In[25]:


sorted_swap = sorted(swap_avg_by_hour, reverse=True)
sorted_swap


# In[27]:


print("Top 5 Hours for 'Ask HN' Comments")

for row in sorted_swap[:5]:
    hour = dt.datetime.strptime(row[1], "%H").strftime("%H:%M")
    print("{}: {:.2f} average comments per post".format(hour,row[0]))
    


# The most comments recieved  on average were at 15:00, with an average of 38.59 comments per post. 
# 
# Conclusion: One should create a post during 15:00 to 16:00 to have a higher chance of receiving comments.
