
que = []
for i in range(1,6):
    q = input(f"Enter the Q{i}: ")
    op = []
    for j in range (1,5):
        o = input(f"Options:  ")
        op.append(o)
        
    correct_ans = input("Enter correct answer (A/B/C/D): ")
    
    Ques_dict = {
        "Question" : q,
        "options": op,
        "answer": correct_ans
    }
    que.append(Ques_dict) 
        
print(que)  


prizes = [1000, 5000, 10000, 50000, 100000]  
total_prize = 0

for s in range(len(que)):
    print(que[s]["Question"])
    print(que[s]["options"])
    
    user_ans = input("Select option (A , B , C , D) :").upper() 
    
    if user_ans == que[s]["answer"]:
        total_prize += prizes[s]
        print(f"SAHIII JAWABBBB!! Aapka prize: ₹{total_prize}")
        
    else: 
        print("APPKA SUFFAR YEHI SAMAPT HOTA HAI ! ")
        break

print(f"\nAapka final prize: ₹{total_prize}")