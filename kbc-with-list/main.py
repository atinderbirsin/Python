questionsAns = [
    ['Who created first Iphone', 'Steve jobs', 'Nelson mandela', 'Narendra Modi', 'Justin Bieber', 1, 10000],
    ['What is the color of sky', 'Green', 'Red', 'White', 'Blue', 4, 20000],
    ['What is the minimum age requirement to vote in india', 15, 18, 25, 32, 2, 30000],
    ['Who created facebook', 'Steve jobs', 'Abhinav Malhotra', 'Mark Zukerberg', 'Justin Timberlake', 3, 40000]
]

prize = 0
for question in questionsAns:
    print(question[0],'\n')
    print(question[1], '\n')
    print(question[2], '\n')
    print(question[3], '\n')
    print(question[4], '\n')
    x = int(input('Enter you answer Index:\n'))
    if(x ==  question[5]):
        prize += question[6]
        print('Correct Answer you won', prize, 'amount.','\n')
    else:
        print('Sorry You loss and you have to leave with', prize, 'amount.')
        break;
