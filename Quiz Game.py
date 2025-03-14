question =[

''' Q1 :Question 1: What is the capital city of France? 
            a) Paris
            b) London
            c) Rome''',

''' Q2 :What is the largest planet in the solar system? 
            a) Earth
            b) Jupiter
            c) Mars''',

''' Q3 :Which planet is closest to the sun?
            a) Earth
            b) Jupiter
            c) Mercury''',
    
''' Q4 :Which part of the human body has the most bones?
            a) Mouth
            b)hands
            c)legs'''
]

answers = ['a','b','c','b']

for i in range(len(question)):
    user_answer = input(question[i]).strip().lower()
    
    if user_answer  == answers[i]:
        print('✔ Correct answer')
    else:
        print('❌ Oops! Wrong answer Game Over')
        break
else:
    print("🎉 Congratulations! You answered all questions correctly!")
