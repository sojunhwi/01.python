#팩맨게임
import random
import time
import sys
import os

#에러클래스
class myerror(Exception):
    
    def moveerror(self,x,y,cnt):
        if x<0 or y<0 or x>=cnt or y>=cnt:
            raise myerror()


class pacman(myerror):
    #사용자=[지정숫자,모양,x좌표,y좌표]
    user=[9,'㉾',0,0]
    #유령=[지정숫자,모양,x좌표,y좌표]
    ghostA=[2,'⊙',0,0]
    ghostB=[3,'⊙',0,0]
    ghostC=[4,'⊙',0,0]
    #먹이,빈칸=[지정숫자,모양,유령경로먹이 저장1,2]
    feed=[1,'★',0,0,0]
    nofeed=[8,'☆']
    #게임횟수
    time=0
    #게임결과 승리 or 패배 or 계속
    result=None
    #자동이동
    last=False
    feedx=0
    feedy=0
    #게임판
    matrix=[]
    #게임모드
    mode=''
    #게임크기
    size=0
    
    #게임시작
    def __init__(self):
        self.howtoplay()
        self.gamestart()

        
    #동작순서
    def gamestart(self):
        #설명->보드생성->보드출력
        self.makemap(self.size)
        self.showmap(self.size)
        #결과가 나올때까지 반복
        #유저이동->유령이동->이동후 보드출력->결과확인->안나왔으면 반복
        while self.result==None:
            if self.mode=='auto':
                self.automove(self.size)
                os.system('cls')
            else:
                self.usermove()
            self.ghostmove(self.size)
            self.showmap(self.size)
            self.gamecheck(self.size)
        #결과나오면 게임내용 기록->결과에 따라 승리 or 패배
        self.gameend()
        self.ending()
    
        


#플레이 방법 설명->크기 설정      
    def howtoplay(self):
        os.system('cls')
        a='\t\t\t\t###### 1조 # 김예솔 # 정재욱 # 소준휘 #######\n\
\t\t\t\t################## 팩맨게임 #################\n\
\t\t\t\t####### 나:㉾ 유령:⊙ 먹이:★ 빈칸:☆ #######\n\
\t\t\t\t######## 유령을 피해서 먹이를 다먹자 ########\n\
\t\t\t\t########### 유령에게 잡히면 패배 ############\n\
\t\t\t\t####### 두번 연속 잘못 입력하면 패배 ########\n\
\t\t\t\t#############################################\n'
        print('\n'*5)
        for i in a:
            print(i,end='')
            
            #time.sleep(0.01)
        
        while self.size<4:
            time.sleep(0.01)
            self.size=int(input('\t\t\t\t######게임판 크기를 설정해주세요(4이상):'))

        
#게임 틀 생성 matrix=[[1,1,1].....]
#cnt 크기의 틀을 만든다->유령과 유저 셋팅
    def makemap(self,cnt):
        for i in range(cnt):
            self.matrix.append([])
            for j in range(cnt):
                self.matrix[i].append(self.feed[0])
        self.setghost(self.size)
        self.setuser()
        self.modecheck(self.size)
        os.system('cls')

#사용자 셋팅 matrix
#유저의 좌표 x=user[2] y=user[3] 초기값 0,0
    def setuser(self):
        self.matrix[self.user[2]][self.user[3]]=self.user[0]

#유령 셋팅 matrix
#맨아래에서 위 두 행,무작위 열에 유령 배치
#배치된 자리에 있던 먹이 or 빈칸은 먹이저장소에 저장(유령A->feed[2],유령B->feed[3])
    def setghost(self,cnt):
        self.ghostA[2]=cnt-3
        self.ghostA[3]=random.randint(0,cnt-1)
        self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
        self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]
        self.ghostB[2]=cnt-2
        self.ghostB[3]=random.randint(0,cnt-1)
        self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
        self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]
        self.ghostC[2]=cnt-1
        self.ghostC[3]=random.randint(0,cnt-1)
        self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
        self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

#모드설정
    def modecheck(self,cnt):
        mode=False
        while mode==False:
            self.mode=input('\t\t\t\t######모드 입력(user/auto):')
            if self.mode=='auto' or self.mode=='user':
                mode=True
            else:
                mode=False
                print('다시 입력해주세요(user/auto)')
        
                
#게임확인
    def gamecheck(self,cnt):
        #유령과 만났을때 죽음
        #유저의 다음 이동좌표와 유령의 다음 이동 좌표가 겹칠때
        if self.matrix[self.user[2]][self.user[3]]==self.ghostA[0] or self.matrix[self.user[2]][self.user[3]]==self.ghostB[0] or self.matrix[self.user[2]][self.user[3]]==self.ghostC[0]:
            self.result=False
        #게임안에 먹이 남아있는지 확인
        else:
            for i in range(cnt):
                #matrix 모든 행에 1(feed)가 없고, 지금 유령이 있는 칸에도 없어야함->True
                if 1 not in self.matrix[i] and 1 not in self.feed[2:4]:
                    self.result=True
                    continue
                #하나라도 있으면 확인 종료
                else:
                    self.result=None
                    break

####################################
#게임 결과->게임기록
#result값에 따라 승리 or 패배
    def gameend(self):
        self.gamerecord()       
        if self.result==True:
            for i in range(5):
                string='□■'
                print('\t\t\t\t\t',end= " ")
                print(string[1]*i+string[0]*(5-i))
                time.sleep(1)
                os.system('cls')
                self.showmap(self.size)
        elif self.result==False:
            time.sleep(3)
            os.system('cls')
            print('\n'*10)
            print('\t\t\t\t\t죽었습니다.........')
            time.sleep(3)
            print('\n')
            print('\t\t\t\t\t감사합니다!')
            time.sleep(5)
            sys.exit(1)

#게임결과 기록
#C:/python/1조.txt 파일에 보드크기,움직인 횟수, 결과 입력
    def gamerecord(self):
        f=open('C:/python/1조.txt','a')
        f.write('모드: %s       '%self.mode)
        f.write('보드크기: %sx%s    '%(self.size,self.size))
        f.write("움직인 횟수: %s   "%self.time)
        if self.result==True:
            f.write("결과: 승리")
        else: f.write("결과: 패배")
        f.write('\n')
        f.close()
######################################       

                

        



#틀->맵 생성 (숫자->문자)
#matrix안의 숫자에 맞는 이미지 출력
    def showmap(self,cnt):
        print('\n'*5)
        print(' '*self.time+'〓'+'★')
        for i in range(cnt):
            for j in range(cnt):
                if self.matrix[i][j]==8:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.nofeed[1],end="  ")
                elif self.matrix[i][j]==1:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.feed[1],end="  ")
                elif self.matrix[i][j]==2:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.ghostA[1],end="  ")
                elif self.matrix[i][j]==3:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.ghostB[1],end="  ")
                elif self.matrix[i][j]==4:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.ghostC[1],end="  ")
                elif self.matrix[i][j]==9:
                    if j==0:
                        print('\t\t\t\t\t',end=" ")
                    print(self.user[1],end="  ")
            print(" ")


#유저 이동
#움직임 조작->키 입력받으면 새로운 화면 출력,입력 횟수+1
    def usermove(self):
        print('\t\t\t\t\t조작키: 위-w 아래-s 왼쪽-a 오른쪽-d')
        key=input('\t\t\t\t\t입력:')
        os.system('cls')
        self.time+=1
        #실행->에러발생하면->except myerror로 이동
        #유저가 이동하면 원래 자리는 9(user)-1(feed)=8(nofeed)가 되고 키에 따라 유저의 x,y 바꿈
        try:
            if key=='d':
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                self.user[3]+=1
                self.moveerror(self.user[2],self.user[3],self.size)
                self.matrix[self.user[2]][self.user[3]]=self.user[0]
            elif key=='s':
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                self.user[2]+=1
                self.moveerror(self.user[2],self.user[3],self.size)
                self.matrix[self.user[2]][self.user[3]]=self.user[0]
            elif key=='w':
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                self.user[2]-=1
                self.moveerror(self.user[2],self.user[3],self.size)
                self.matrix[self.user[2]][self.user[3]]=self.user[0]
            elif key=='a':
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                self.user[3]-=1
                self.moveerror(self.user[2],self.user[3],self.size)
                self.matrix[self.user[2]][self.user[3]]=self.user[0]
            #한번입력실수허용->두번 하면 result=False->패배
            else:
                print('\n'*10)
                print('\t\t\t\t\t\t입력 오류')
                time.sleep(0.5)
                os.system('cls')
                self.time-=1
                self.showmap(self.size)
                key=input('\t\t\t\t\t다시 입력:')
                os.system('cls')
                if key=='d':
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                    self.user[3]+=1
                    self.moveerror(self.user[2],self.user[3],self.size)
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]
                elif key=='s':
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                    self.user[2]+=1
                    self.moveerror(self.user[2],self.user[3],self.size)
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]
                elif key=='w':
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                    self.user[2]-=1
                    self.moveerror(self.user[2],self.user[3],self.size)
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]
                elif key=='a':
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                    self.user[3]-=1
                    self.moveerror(self.user[2],self.user[3],self.size)
                    self.matrix[self.user[2]][self.user[3]]=self.user[0]
                else:
                    print('\n'*10)
                    print('\t\t\t\t\t입력 오류 두번으로 실패')
                    self.result=False
                    self.gameend()
        #맵을 넘어가면(x,y>cnt or x,y<0) ->좌표 다시 바꿈->이동x
        except myerror:
            os.system('cls')
            if self.user[2]<0:
                self.user[2]=0

            elif self.user[2]>=self.size:
                self.user[2]=self.size-1

            elif self.user[3]<0:
                self.user[3]=0

            elif self.user[3]>=self.size:
                self.user[3]=self.size-1
            self.setuser()
            print('\n'*10)
            print('\t\t\t\t\t이동할 수 없습니다!!!')
            time.sleep(0.1)
            os.system('cls')
        

     
    #유령 이동       
    def ghostmove(self,cnt):
        
        #유저가 유령이 있던 자리로 이동하면 유령은 다른곳 이동하면서 저장소에 있던 값 반환x
        if self.matrix[self.ghostA[2]][self.ghostA[3]]==self.ghostA[0]:
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.feed[2]
        elif self.matrix[self.ghostA[2]][self.ghostA[3]]==self.user[0]:
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.user[0]
        elif self.matrix[self.ghostA[2]][self.ghostA[3]]==self.ghostB[0]:
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostB[0]
            self.feed[3]=self.feed[2]
        elif self.matrix[self.ghostA[2]][self.ghostA[3]]==self.ghostC[0]:
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostC[0]
            self.feed[4]=self.feed[2]
        

        #방향 정하기 0이면 x , 1이면 y
        ran_move=random.sample([0,1],1)[0]

        #(0,0)
        if self.ghostA[2]==0 and self.ghostA[3]==0:
            if ran_move==0:
                self.ghostA[2]+=1
            elif ran_move==1:
                self.ghostA[3]+=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


        #(0,4)
        elif self.ghostA[2]==0 and self.ghostA[3]==cnt-1:
            if ran_move==0:
                self.ghostA[2]+=1
            elif ran_move==1:
                self.ghostA[3]-=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


        #(4,0)
        elif self.ghostA[2]==cnt-1 and self.ghostA[3]==0:
            if ran_move==0:
                self.ghostA[2]-=1
            elif ran_move==1:
                self.ghostA[3]+=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]

        #(4,4)
        elif self.ghostA[2]==cnt-1 and self.ghostA[3]==cnt-1:
            if ran_move==0:
                self.ghostA[2]-=1
            elif ran_move==1:
                self.ghostA[3]-=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


    #가장자리
        #위쪽
        elif self.ghostA[2]==0 and self.ghostA[3]!=0: 
            if ran_move==0:
                self.ghostA[2]+=1
            elif ran_move==1:
                self.ghostA[3]+=random.randint(-1,1)
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


        #왼쪽     
        elif self.ghostA[3]==0 and self.ghostA[2]!=0:
            if ran_move==0:
                self.ghostA[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostA[3]+=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


        #오른쪽   
        elif self.ghostA[3]==cnt-1 and self.ghostA[2]!=cnt-1:
            if ran_move==0:
                self.ghostA[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostA[3]-=1
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]


        #아래
        elif self.ghostA[2]==cnt-1 and self.ghostA[3]!=cnt-1:
            if ran_move==0:
                self.ghostA[2]-=1
            elif ran_move==1:
                self.ghostA[3]+=random.sample([-1,1],1)[0]
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]



        #안쪽   
        else:
            if ran_move==0:
                self.ghostA[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostA[3]+=random.sample([-1,1],1)[0]
            self.feed[2]=self.matrix[self.ghostA[2]][self.ghostA[3]]
            self.matrix[self.ghostA[2]][self.ghostA[3]]=self.ghostA[0]

#####유령1######

#####유령2######
        if self.matrix[self.ghostB[2]][self.ghostB[3]]==self.ghostB[0]:
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.feed[3]
        elif self.matrix[self.ghostB[2]][self.ghostB[3]]==self.user[0]:
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.user[0]
        elif self.matrix[self.ghostB[2]][self.ghostB[3]]==self.ghostC[0]:
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostC[0]
            self.feed[4]=self.feed[3]
        elif self.matrix[self.ghostB[2]][self.ghostB[3]]==self.ghostA[0]:
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostA[0]
            self.feed[2]=self.feed[3]

        ran_move=random.sample([0,1],1)[0]
        if self.ghostB[2]==0 and self.ghostB[3]==0:
            if ran_move==0:
                self.ghostB[2]+=1
            elif ran_move==1:
                self.ghostB[3]+=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #(0,4)
        elif self.ghostB[2]==0 and self.ghostB[3]==cnt-1:
            if ran_move==0:
                self.ghostB[2]+=1
            elif ran_move==1:
                self.ghostB[3]-=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #(4,0)
        elif self.ghostB[2]==cnt-1 and self.ghostB[3]==0:
            if ran_move==0:
                self.ghostB[2]-=1
            elif ran_move==1:
                self.ghostB[3]+=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #(4,4)
        elif self.ghostB[2]==cnt-1 and self.ghostB[3]==cnt-1:
            if ran_move==0:
                self.ghostB[2]-=1
            elif ran_move==1:
                self.ghostB[3]-=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]


    #가장자리
        #위쪽
        elif self.ghostB[2]==0 and self.ghostB[3]!=0: 
            if ran_move==0:
                self.ghostB[2]+=1
            elif ran_move==1:
                self.ghostB[3]+=random.randint(-1,1)
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #왼쪽     
        elif self.ghostB[3]==0 and self.ghostB[2]!=0:
            if ran_move==0:
                self.ghostB[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostB[3]+=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #오른쪽   
        elif self.ghostB[3]==cnt-1 and self.ghostB[2]!=cnt-1:
            if ran_move==0:
                self.ghostB[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostB[3]-=1
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]

        #아래
        elif self.ghostB[2]==cnt-1 and self.ghostB[3]!=cnt-1:
            if ran_move==0:
                self.ghostB[2]-=1
            elif ran_move==1:
                self.ghostB[3]+=random.sample([-1,1],1)[0]
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]


        #안쪽   
        else:
            if ran_move==0:
                self.ghostB[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostB[3]+=random.sample([-1,1],1)[0]
            self.feed[3]=self.matrix[self.ghostB[2]][self.ghostB[3]]
            self.matrix[self.ghostB[2]][self.ghostB[3]]=self.ghostB[0]
####유령3
        if self.matrix[self.ghostC[2]][self.ghostC[3]]==self.ghostC[0]:
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.feed[4]
        elif self.matrix[self.ghostC[2]][self.ghostC[3]]==self.user[0]:
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.user[0]
        elif self.matrix[self.ghostC[2]][self.ghostC[3]]==self.ghostA[0]:
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostA[0]
            self.feed[2]=self.feed[4]
        elif self.matrix[self.ghostC[2]][self.ghostC[3]]==self.ghostB[0]:
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostB[0]
            self.feed[3]=self.feed[4]

        ran_move=random.sample([0,1],1)[0]
        #(0,0)
        if self.ghostC[2]==0 and self.ghostC[3]==0:
            if ran_move==0:
                self.ghostC[2]+=1
            elif ran_move==1:
                self.ghostC[3]+=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #(0,4)
        elif self.ghostC[2]==0 and self.ghostC[3]==cnt-1:
            if ran_move==0:
                self.ghostC[2]+=1
            elif ran_move==1:
                self.ghostC[3]-=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #(4,0)
        elif self.ghostC[2]==cnt-1 and self.ghostC[3]==0:
            if ran_move==0:
                self.ghostC[2]-=1
            elif ran_move==1:
                self.ghostC[3]+=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #(4,4)
        elif self.ghostC[2]==cnt-1 and self.ghostC[3]==cnt-1:
            if ran_move==0:
                self.ghostC[2]-=1
            elif ran_move==1:
                self.ghostC[3]-=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]


    #가장자리
        #위쪽
        elif self.ghostC[2]==0 and self.ghostC[3]!=0: 
            if ran_move==0:
                self.ghostC[2]+=1
            elif ran_move==1:
                self.ghostC[3]+=random.randint(-1,1)
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #왼쪽     
        elif self.ghostC[3]==0 and self.ghostC[2]!=0:
            if ran_move==0:
                self.ghostC[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostC[3]+=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #오른쪽   
        elif self.ghostC[3]==cnt-1 and self.ghostC[2]!=cnt-1:
            if ran_move==0:
                self.ghostC[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostC[3]-=1
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

        #아래
        elif self.ghostC[2]==cnt-1 and self.ghostC[3]!=cnt-1:
            if ran_move==0:
                self.ghostC[2]-=1
            elif ran_move==1:
                self.ghostC[3]+=random.sample([-1,1],1)[0]
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]


        #안쪽   
        else:
            if ran_move==0:
                self.ghostC[2]+=random.sample([-1,1],1)[0]
            elif ran_move==1:
                self.ghostC[3]+=random.sample([-1,1],1)[0]
            self.feed[4]=self.matrix[self.ghostC[2]][self.ghostC[3]]
            self.matrix[self.ghostC[2]][self.ghostC[3]]=self.ghostC[0]

######유령2########################


####자동이동
    def automove(self,size):
        try:
            count=0
            
            if self.last==False:
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                x=self.user[2]
                y=self.user[3]
                ran_move=random.sample([0,1],1)[0]
                while self.matrix[x][y]!=self.feed[0] and self.matrix[x][y]!=self.ghostA[0] and self.matrix[x][y]!=self.ghostB[0] and self.matrix[x][y]!=self.ghostC[0]:
                    count+=1
                    x=self.user[2]
                    y=self.user[3]
                    ran_move=random.sample([0,1],1)[0]
                    if ran_move==0:
                        x+=random.sample([-1,1],1)[0]
                        self.moveerror(x,y,size)
                    elif ran_move==1:
                        y+=random.sample([-1,1],1)[0]
                        self.moveerror(x,y,size)
                    if count>10:
                        self.last=True
                        break
                self.user[2]=x
                self.user[3]=y
                self.matrix[self.user[2]][self.user[3]]=self.user[0]
                time.sleep(1)
                    
                              
            else: 
                for i in range(size):
                    if self.matrix[i].count(1)!=0:
                        self.feedx=i
                        self.feedy=self.matrix[i].index(1)
                        break
                self.matrix[self.user[2]][self.user[3]]=self.user[0]-self.feed[0]
                if self.user[2]<self.feedx:
                    self.user[2]+=1
                elif self.user[2]>self.feedx:
                    self.user[2]-=1
                else:
                    if self.user[3]<self.feedy:
                        self.user[3]+=1
                    elif self.user[3]>self.feedy:
                        self.user[3]-=1             
                self.matrix[self.user[2]][self.user[3]]=self.user[0]

        except myerror:
                    if self.user[2]<0:
                        self.user[2]=0

                    elif self.user[2]>=self.size:
                        self.user[2]=self.size-1

                    elif self.user[3]<0:
                        self.user[3]=0

                    elif self.user[3]>=self.size:
                        self.user[3]=self.size-1
                    self.setuser()
        self.time+=1


    def ending(self):
        os.system('cls')
        string='승리하였습니다!'
        for i in range(20):
            for j in range(25):
                num=random.randint(5,15)
                if i%3==0:
                    print('〓'*(num+5)+'★')
                else:
                    print('〓'*(num)+'★')
            time.sleep(0.05)
            os.system('cls')
        
        for i in range(8):
            print('\n'*10)
            print('\t\t\t\t\t',end=" ")
            print(string[0:i])
            time.sleep(0.5)
            os.system('cls')
        print('축하'*self.time)
        print('\n'*10)
        print('\t\t\t\t\t플레이해주셔서 감사합니다!!')
        time.sleep(3)
        sys.exit(1)
a=pacman()



