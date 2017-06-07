def Mix_word():
    return ['+',0,0,0,0,0,0]

def sign_flip(s):
    # flips sign stored as char + or -
    r=s
    if s=='-': r='+'
    if s=='+': r='-'
    return r

def to_int(a):
    # coverts a mix word into an integer 
    if a[0]=='+' or a[0]=='-': a1=a[1:]
    else: a1=a
    r=0
    for x in range(len(a1)):
        r=r+(a[-(x+1)]*(64**x))
    if a[0]=='-': r=0-r
    return r

def to_word(a):
    # converts a integer into a mix word
    if a>0 or a==0:
        r1=['+']
        a1=a
    else:
        r1=['-']
        a1=0-a
    r2=[]
    for x in range(5):
        r2=[a1%64]+r2
        a1=int(a1/64)
    r=r1+r2
    return r
        

def n_to_field(f):
    f1=int(f/8)
    f2=(f%8)+1
    r=[f1,f2]
    return r


class Mix_main():
    # Main emulator containg the rejestors? funtions and ram
    def __init__(self):
        self.rA=Mix_word()
        self.rX=Mix_word()
        self.rJ=Mix_word()
        self.I1=Mix_word()
        self.I2=Mix_word()
        self.I3=Mix_word()
        self.I4=Mix_word()
##        self.I5=Mix_word()
##        self.I6=Mix_word()
        self.I0=[0,0]
        self.overflow_toggle=0
        self.comparison_indicator=0
        self.RAM=[['+',0,0,0,0,0]]*4000
        self.RAM_L=0
        self.is_running=0
        self.byte_s=8
    def check_o(self,n):
        if n>=(self.byte_s**5):
            self.overflow_toggle=1
        
    def check_i(self,data):
        r=0
        if data[1:4]==[0,0,0]:
            r=1
        return r
    def load_data(self,data,location,size):
        # loads input on to ram of emulated machine
        for x in range(size):
            self.RAM[location+x]=data[x]
    def output_data(self,location,size):
        # returns the bytes on ram frome location to location + (size-1)
        return self.RAM[location:(location+size)]
    def run_main(self):
        # runs the emulation on the current ram
        self.is_running=1
        while self.is_running==1 and self.RAM_L<4000:
            self.run_fn(self.RAM[self.RAM_L])
            self.RAM_L=self.RAM_L+1
        self.is_running=0
    def run_fn(self,word):
        fn=eval('self.fn_'+str(word[5]))
        f=word[4]
        i=['+',0,0]
        if word[3]<7:
            i=eval('self.I'+str(word[3]))
        m=(to_int(word[1:3]))+(to_int(i))
        data=self.RAM[m]
        f1=int(f/8)
        f2=(f%8)+1
        print (('self.fn_'+str(word[5]))+' '+str(to_int(data))+' ['+str(f1)+':'+str(f2-1)+'] '+str(m))
        fn(data,f1,f2,m)
    def fn_0(self,data,f1,f2,m): ## NOP
        return 0
    def fn_1(self,data,f1,f2,m):
        r1=to_int(self.rA)
        r2=to_int(data[f1:f2])
        self.check_o((r1+r2))
        self.rA=to_word((r1+r2))
        print("self.rA to "+str(self.rA))
        
    def fn_2(self,data,f1,f2,m):
        r1=to_int(self.rA)
        r2=to_int(data[f1:f2])        
        self.check_o((r1+r2))
        self.rA=to_word((r1-r2))
        print("self.rA to "+str(self.rA))
        
    def fn_3(self,data,f1,f2,m):
        r1=to_int(self.rA)
        r2=to_int(data[f1:f2])
        self.rA=to_word((r1-r2)%self.byte_s)
        print("self.rA to "+str(self.rA)+"/n")
        self.rX=to_word((r1-r2)/self.byte_s)
        
    def fn_4(self,data,f1,f2,m):
        return 0
    def fn_5(self,data,f1,f2,m):
        if f1==0:
            if f2-1==0:
                r=1
            if f2-1==1:
                r=1
            if f2-1==2:
                self.is_running=0
        
    # def fn_6(self,data,f1,f2,m):
    #     d=self.rA
    #     if f2 in [2,3,4,5]:
    #       d=1
    #     r=shift_main(data,f1,2)
        
    def fn_7(self,data,f1,f2,m):
        return 0
    def load_m(self,data,f1,f2):
        rs=[]
        r1=data[f1:f2]+[data[f2]]
        if r1[0]=='+' or r1=='-':
            rs=[r1[0]]
            r1=r1[1:]
        r2=to_int(r1)
        r=to_word(r2)
        return r
    def fn_8(self,data,f1,f2,m): ## LDA 
        self.rA=self.load_m(data,f1,f2)
        
    def fn_9(self,data,f1,f2,m): ## LD1
        r1=self.load_m(data,f1,f2)
        if self.check_i(r1)==1:
            self.I1=r1
        
    def fn_10(self,data,f1,f2,m): ## LD2
        r1=self.load_m(data,f1,f2)
        if self.check_i(r1)==1:
            self.I2=r1
        
    def fn_11(self,data,f1,f2,m): ## LD3
        r1=self.load_m(data,f1,f2)
        if self.check_i(r1)==1:
            self.I3=r1
        
    def fn_12(self,data,f1,f2,m): ## LD4
        r1=self.load_m(data,f1,f2)
        if self.check_i(r1)==1:
            self.I4=r1
        
##    def fn_13(self,data,f1,f2,m): ## LD5
##        r1=self.load_main(data,f1,f2)
##        if self.check_i(r1)=1:
##            self.I5=r1
##        
##    def fn_14(self,data,f1,f2,m): ## LD6
##        r1=self.load_main(data,f1,f2)
##        if self.check_i(r1)=1:
##            self.I6=r1
##        
    def fn_15(self,data,f1,f2,m): ## LDX
        print(str(f1))
        print(str(f2))
        print(str(data))
        self.rX=self.load_m(data,f1,f2)
        
    def fn_16(self,data,f1,f2,m): ## LDA
        self.rA=self.load_m(data,f1,f2)
        self.rA[0]=sign_flip(self.rA[0])
        
    def fn_17(self,data,f1,f2,m): ## LD1N
        r1=self.load_m(data,f1,f2)
        r1[0]=sign_flip(r1[0])
        if self.check_i(r1)==1:
            self.I1=r1
        
    def fn_18(self,data,f1,f2,m): ## LD2N
        r1=self.load_m(data,f1,f2)
        r1[0]=sign_flip(r1[0])
        if self.check_i(r1)==1:
            self.I2=r1
        
    def fn_19(self,data,f1,f2,m): ## LD3N
        r1=self.load_m(data,f1,f2)
        r1[0]=sign_flip(r1[0])
        if self.check_i(r1)==1:
            self.I3=r1
        
    def fn_20(self,data,f1,f2,m): ## LD4N
        r1=self.load_m(data,f1,f2)
        r1[0]=sign_flip(r1[0])
        if self.check_i(r1)==1:
            self.I4=r1
        
##    def fn_21(self,data,f1,f2,m): ## LD5N
##        if self.check_i(data,f1,f2)==1:
##            self.I5=load_main(data,f1,f2)
##            self.I5[0]=sign_flip(self.I5[0])
##            self.I5=self.get_i(self.I5)
##        
##    def fn_22(self,data,f1,f2,m): ## LD6N
##        if self.check_i(data,f1,f2)==1:
##            self.I6=load_main(data,f1,f2)
##            self.I6[0]=sign_flip(self.I6[0])
##            self.I6=self.get_i(self.I6)
##        
    def fn_23(self,data,f1,f2,m): ## LDXN
        self.rX=self.load_m(data,f1,f2)
        self.rX[0]=sign_flip(self.rX[0])
        
    def store_m(self,data,f1,f2,m):
        n1=f1
        n2=f2+1
        if f1==0:
            self.RAM[m][0]=data[0]
            n1=n1+1
        n=n1-n2
        n=n+1
        self.RAM[m][n1:n2]=data[n:]
        print("self.RAM["+str(m)+"]to "+str(self.RAM[m])+"/n")
        
    def fn_24(self,data,f1,f2,m): ## STA
        self.store_m(self.rA,f1,f2,m)
        
    def fn_25(self,data,f1,f2,m): ## ST1
        self.store_m(self.I1,f1,f2,m)
        
    def fn_26(self,data,f1,f2,m): ## ST2
        self.store_m(self.I2,f1,f2,m)
        
    def fn_27(self,data,f1,f2,m): ## ST3
        self.store_m(self.I3,f1,f2,m)
        
    def fn_28(self,data,f1,f2,m): ## ST4
        self.store_m(self.I4,f1,f2,m)
        
##    def fn_29(self,data,f1,f2,m): ## ST5 
##        self.store_m(self.I5,f1,f2,m)
##        
##    def fn_30(self,data,f1,f2,m): ## ST6
##        self.store_m(self.I6,f1,f2,m)
##        
    # def fn_31(self,data,f1,f2,m): ## STX
    #     self.store_m(self.rx,f1,f2,m)
    #     
    def fn_32(self,data,f1,f2,m): ## STJ
        self.store_m(to_word(self.rJ),f1,f2,m)
        
    def fn_33(self,data,f1,f2,m): ## STZ
        self.store_m(Mix_word(),f1,f2,m)
        
    # def fn_34(self,data,f1,f2,m):
        
    # def fn_35(self,data,f1,f2,m):
        
    # def fn_36(self,data,f1,f2,m):
        
    # def fn_37(self,data,f1,f2,m):
        
    # def fn_38(self,data,f1,f2,m):
        
    def JMP(self,m):
        self.rJ=self.RAM_L+1
        self.RAM_L=m
    def JMP_testx(self,m,f,x):
        if f==0:
            if x<0:
                self.JMP(m)
        if f==1:
            if x==0:
                self.JMP(m)
        if f==2:
            if x>0:
                self.JMP(m)
        if f==3:
            if x>=0:
                self.JMP(m)
        if f==4:
            if x!=0:
                self.JMP(m)
        if f==5:
            if x<=0:
                self.JMP(m)
        
    def fn_39(self,data,f1,f2,m): ## J
        f=(8*f1)+f2
        if f==0:
            self.JMP(m)
        if f==1:
            self.RAM_L=m
        if f==2:
            if self.overflow_toggle==1:
                self.overflow_toggle=0
                self.JMP(m)
        if f==3:
            if self.overflow_toggle==0:
                self.JMP(m)
            else:
                self.overflow_toggle=0
        if f==4:
            if self.comparison_indicator in [0]:
                self.JMP(m)
        if f==5:
            if self.comparison_indicator in [1]: self.JMP(m)
        if f==6:
            if self.comparison_indicator in [2]:
                self.JMP(m)
        if f==7:
            if self.comparison_indicator in [1,2]:
                self.JMP(m)
        if f==8:
            if self.comparison_indicator in [0,2]:
                self.JMP(m)
        if f==9:
            if self.comparison_indicator in [0,1]:
                self.JMP(m)
        
    def fn_40(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.rA))
        
    def fn_41(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.I1))
        
    def fn_42(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.I2))
        
    def fn_43(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.I3))
        
    def fn_44(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.I4))
        
##    def fn_45(self,data,f1,f2,m):
##        self.JMP_testx(m,((8*f1)+f2),to_int(self.rA))
##        
##    def fn_46(self,data,f1,f2,m):
##        self.JMP_testx(m,((8*f1)+f2),to_int(self.rA))
##        
    def fn_47(self,data,f1,f2,m):
        self.JMP_testx(m,((8*f1)+f2),to_int(self.rX))
        
    # def fn_48(self,data,f1,f2,m):
        
    # def fn_49(self,data,f1,f2,m):
        
    # def fn_50(self,data,f1,f2,m):
        
    # def fn_51(self,data,f1,f2,m):
        
    # def fn_52(self,data,f1,f2,m):
        
    # def fn_53(self,data,f1,f2,m):
        
    # def fn_54(self,data,f1,f2,m):
        
    # def fn_55(self,data,f1,f2,m):
        
    # def fn_56(self,data,f1,f2,m): 
##        if >x:
##        self.comparison_indicator=r
        
    # def fn_57(self,data,f1,f2,m):
        
    # def fn_58(self,data,f1,f2,m):
        
    # def fn_59(self,data,f1,f2,m):
        
    # def fn_60(self,data,f1,f2,m):
        
    # def fn_61(self,data,f1,f2,m):
        
    # def fn_62(self,data,f1,f2,m):
        
    # def fn_63(self,data,f1,f2,m):
        
    


f1=[['+',0,6,0,5,1],['+',0,7,0,5,1],['+',0,8,0,5,2],['+',0,9,0,5,2],['+',0,19,0,5,24]]
f2=[['+',0,0,0,2,5],['+',42,61,0,0,5],['-',22,31,0,0,8],['-',0,0,0,10,15],['+',0,0,0,10,20]]
fm=f1+f2

M1=Mix_main()
M1.load_data(fm,0,len(fm))
M1.run_main()
t0=M1.rA
t1=M1.RAM[19]


        
        




