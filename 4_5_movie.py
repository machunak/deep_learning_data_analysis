import pandas as pd
import numpy as np
users = pd.read_csv('ml-1m/users.dat',
                    header=None,
                    delimiter='::',
                    engine='python',
                    names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))
#print(users)

ratings = pd.read_csv('ml-1m/ratings.dat',
                      header=None,
                      delimiter='::',
                      engine='python',
                      names='UserID::MovieID::Rating::Timestamp'.split('::'))

#print(ratings)

movies = pd.read_csv('ml-1m/movies.dat',
                      header=None,
                      delimiter='::',
                      engine='python',
                      names='MovieID::Title::Genres'.split('::'),
                      encoding_errors='ignore')

#print(movies)

movies = pd.merge(movies, pd.merge(users, ratings))
print(movies, end='\n\n')

p1 = movies.pivot_table(values='Rating', index='Gender')

print(p1, end='\n\n')

#남녀 평점 평균
# sum_female_rating = 0
# sum_male_rating = 0
# sum_male = 0
# sum_female = 0
# for g, r in zip(movies['Gender'], movies['Rating']):
#     if(g == 'F'):
#         sum_female_rating += r
#         sum_female += 1
#     else:
#         sum_male_rating += r
#         sum_male += 1
#
# print(sum_female_rating / sum_female)
# print(sum_male_rating / sum_male)

b_males = (movies['Gender'] == 'M')
print((b_males))

males = movies['Rating'][b_males]
print(type(males))
print('남자 : ', np.mean(males))

p2 = movies.pivot_table(values='Rating', index='Gender', columns='Age')
print(p2, end='\n\n')

p3 = movies.pivot_table(values='Rating', index='Age', columns='Gender')
print(p3, end='\n\n')

p4 = movies.pivot_table(values='Rating', index='Age', columns='Occupation')
print(p4, end='\n\n')

p5 = movies.pivot_table(values='Rating', index=['Age','Gender'], columns='Occupation')
print(p5, end='\n\n')