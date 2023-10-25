class Documents:
    def __init__(self):
        pass

    def set(self):
        pass

    def Type_interact(self,x):
        
        #bool 처리
        if x == "True" : x = True
        elif x == "False" : x = False
        
        if x != True and x != False:
            try: x = int(x) #정수
            except:
                try: x = float(x) #실수
                except: pass #아니면 뭐 문자열이겠지
        
        return type(x)
    
    def random_redint(self):
        pass

#==============================
if __name__ == "__main__":
    documents = Documents()

    answer = input("값을 입력해주세요.")
    print(documents.Type_interact(answer))
else:
    print("임포트되어 사용됨")
    print(__name__)
#==============================