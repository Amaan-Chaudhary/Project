# Link to Video - https://youtu.be/j_pymD63k6o?si=YNgrY_7hciXg_nGT


from manim import *
import random
import os
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService

os.environ["OPENAI_API_KEY"]="  "

class OpenAIExample(VoiceoverScene):
    def construct(self):

        self.set_speech_service(
            OpenAIService(
                voice = "alloy",
                model = "tts-1-hd"
            )
        )

        rec = RoundedRectangle(width=12, height=6, color=WHITE)
        tr_1 = Triangle().scale(0.2).set_fill(WHITE, opacity=1).rotate(PI/6)
        tr_2 = tr_1.copy().next_to(tr_1, RIGHT, buff=0.05)
        t = VGroup(tr_1,tr_2).next_to(rec,UP).shift(5.5*RIGHT)

        matrix = [[1, 1, 1, 35], [3, 2, 1, 75], [4, 3, 1, 105]]
        E = Matrix(matrix,element_alignment_corner=UR,v_buff=1.8, h_buff=1.8, bracket_h_buff=0.75, bracket_v_buff=0.75).scale(0.7)

        apple1 = ImageMobject("/Users/chaudhary/Desktop/Manim/apple.png")
        mango1 = ImageMobject("/Users/chaudhary/Desktop/Manim/mango.png")
        parking1 = ImageMobject("/Users/chaudhary/Desktop/Manim/parking.png")
        
        object_height = 1.5
        
        #Setting height of apples for first equation
        apple1.height = object_height/3
        mango1.height = object_height/3
        parking1.height = object_height/3
        
        no_apple1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3).next_to(rec,UP).shift(0.8*DOWN+2.5*LEFT)
        #no_apple1.shift(3* UP + 2.5*LEFT)
        
        plus1 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        apple1.next_to(no_apple1,buff = 0.1)
        plus1.next_to(apple1)
        
        no_mango1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        plus2 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        no_mango1.next_to(plus1)
        mango1.next_to(no_mango1,buff = 0.1)
        plus2.next_to(mango1,buff = 0.25)
        parking1.next_to(plus2)
        
        equal1 = Text('=', color=WHITE,weight = BOLD).scale(object_height/3)
        equal1.next_to(parking1,buff = 0.25)
        
        ans1 = Text('35', color= RED_E,weight = BOLD).scale(object_height/2.5)
        ans1.next_to(equal1,buff = 0.4)

        apple2 = ImageMobject("/Users/chaudhary/Desktop/Manim/apple.png")
        mango2 = ImageMobject("/Users/chaudhary/Desktop/Manim/mango.png")
        parking2 = ImageMobject("/Users/chaudhary/Desktop/Manim/parking.png")
        
        apple2.height = object_height/3
        mango2.height = object_height/3
        parking2.height = object_height/3
        
        no_apple2 = Text('3 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        no_apple2.shift(2* UP + 2.5*LEFT)
        
        plus3 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        apple2.next_to(no_apple2,buff = 0.1)
        plus3.next_to(apple2)
        no_mango2 = Text('2 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        plus4 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        no_mango2.next_to(plus3)
        mango2.next_to(no_mango2,buff = 0.1)
        plus4.next_to(mango2,buff = 0.25)
    
        parking2.next_to(plus4)
        equal2 = Text('=', color=WHITE,weight = BOLD).scale(object_height/3)
        equal2.next_to(parking2,buff = 0.25)
        
        ans2 = Text('75', color= RED_E,weight = BOLD).scale(object_height/2)
        ans2.next_to(equal2,buff = 0.4)

        apple3 = ImageMobject("/Users/chaudhary/Desktop/Manim/apple.png")
        mango3 = ImageMobject("/Users/chaudhary/Desktop/Manim/mango.png")
        parking3 = ImageMobject("/Users/chaudhary/Desktop/Manim/parking.png")

        apple3.height = object_height/3
        mango3.height = object_height/3
        parking3.height = object_height/3
        
        no_apple3 = Text('4 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        no_apple3.shift(1.42* UP + 2.5*LEFT)
        
        plus5 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        apple3.next_to(no_apple3,buff = 0.1)
        plus5.next_to(apple3)
        
        no_mango3 = Text('3 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        
        plus6 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        no_mango3.next_to(plus5)
        mango3.next_to(no_mango3,buff = 0.1)
        plus6.next_to(mango3,buff = 0.25)
    
        parking3.next_to(plus6)
        equal3 = Text('=', color=WHITE,weight = BOLD).scale(object_height/3)
        equal3.next_to(parking3,buff = 0.25)
        
        ans3 = Text('105', color= RED_E,weight = BOLD).scale(object_height/2)
        ans3.next_to(equal3,buff = 0.4)
        apple4 = ImageMobject("/Users/chaudhary/Desktop/Manim/apple.png")
        mango4 = ImageMobject("/Users/chaudhary/Desktop/Manim/mango.png")
        parking4 = ImageMobject("/Users/chaudhary/Desktop/Manim/parking.png")
        
        apple4.height = object_height/3
        mango4.height = object_height/3
        parking4.height = object_height/3
        
        no_apple4 = Text('5 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        no_apple4.shift(0.85* UP + 2.5*LEFT)
        
        plus7 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        apple4.next_to(no_apple4,buff = 0.1)
        plus7.next_to(apple4)
        
        no_mango4 = Text('5 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/3)
        
        plus8 = Text('+', color=WHITE,weight = BOLD).scale(object_height/3)
        
        no_mango4.next_to(plus7)
        mango4.next_to(no_mango4,buff = 0.1)
        plus8.next_to(mango4,buff = 0.25)
        parking4.next_to(plus8)
        equal4 = Text('=', color=WHITE,weight = BOLD).scale(object_height/3)
        equal4.next_to(parking4,buff = 0.25)
        
        ans4 = Text('?', color= RED_E,weight = BOLD).scale(object_height/2)
        ans4.next_to(equal4,buff = 0.4)

        A1 = Text('A', color= BLUE,weight = BOLD).scale(object_height/3)
        A1.move_to(apple1)
        A2 = A1.copy()
        A2.move_to(apple2)
        A3 = A1.copy()
        A3.move_to(apple3)
        A4 = A1.copy()
        A4.move_to(apple4)
        
        M1 = Text('M', color= BLUE,weight = BOLD).scale(object_height/3)
        M1.move_to(mango1)
        M2 = M1.copy()
        M2.move_to(mango2)
        M3 = M1.copy()
        M3.move_to(mango3)
        M4 = M1.copy()
        M4.move_to(mango4)
        
        P1 = Text('P', color= BLUE,weight = BOLD).scale(object_height/3)
        P1.move_to(parking1)
        P2 = P1.copy()
        P2.move_to(parking2)
        P3 = P1.copy()
        P3.move_to(parking3)
        P4 = P1.copy()
        P4.move_to(parking4)

        #Setting height of apples for first equation
        apple1.height = object_height/2
        mango1.height = object_height/2
        parking1.height = object_height/2
        
        no_apple1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple1.shift(3* UP + 2.5*LEFT)
        
        plus1 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        apple1.next_to(no_apple1,buff = 0.1)
        plus1.next_to(apple1)
        
        no_mango1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        plus2 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        no_mango1.next_to(plus1)
        mango1.next_to(no_mango1,buff = 0.1)
        plus2.next_to(mango1,buff = 0.25)
        parking1.next_to(plus2)
        
        equal1 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal1.next_to(parking1,buff = 0.25)
        
        ans1 = Text('35', color= RED_E,weight = BOLD).scale(object_height/2)
        ans1.next_to(equal1,buff = 0.4)
        
        apple2.height = object_height/2
        mango2.height = object_height/2
        parking2.height = object_height/2
        
        no_apple2 = Text('3 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple2.shift(2* UP + 2.5*LEFT)
        
        plus3 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        apple2.next_to(no_apple2,buff = 0.1)
        plus3.next_to(apple2)
        no_mango2 = Text('2 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        plus4 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        no_mango2.next_to(plus3)
        mango2.next_to(no_mango2,buff = 0.1)
        plus4.next_to(mango2,buff = 0.25)
    
        parking2.next_to(plus4)
        equal2 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal2.next_to(parking2,buff = 0.25)
        
        ans2 = Text('75', color= RED_E,weight = BOLD).scale(object_height/2)
        ans2.next_to(equal2,buff = 0.4)

        apple3.height = object_height/2
        mango3.height = object_height/2
        parking3.height = object_height/2
        
        no_apple3 = Text('4 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple3.shift(1* UP + 2.5*LEFT)
        
        plus5 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        apple3.next_to(no_apple3,buff = 0.1)
        plus5.next_to(apple3)
        
        no_mango3 = Text('3 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        
        plus6 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        no_mango3.next_to(plus5)
        mango3.next_to(no_mango3,buff = 0.1)
        plus6.next_to(mango3,buff = 0.25)
    
        parking3.next_to(plus6)
        equal3 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal3.next_to(parking3,buff = 0.25)
        
        ans3 = Text('105', color= RED_E,weight = BOLD).scale(object_height/2)
        ans3.next_to(equal3,buff = 0.4)
        A1 = Text('A', color= BLUE,weight = BOLD).scale(object_height/2)
        A1.move_to(apple1)
        A2 = A1.copy()
        A2.move_to(apple2)
        A3 = A1.copy()
        A3.move_to(apple3)
        A4 = A1.copy()
        A4.move_to(apple4)
        
        M1 = Text('M', color= BLUE,weight = BOLD).scale(object_height/2)
        M1.move_to(mango1)
        M2 = M1.copy()
        M2.move_to(mango2)
        M3 = M1.copy()
        M3.move_to(mango3)
        M4 = M1.copy()
        M4.move_to(mango4)
        
        P1 = Text('P', color= BLUE,weight = BOLD).scale(object_height/2)
        P1.move_to(parking1)
        P2 = P1.copy()
        P2.move_to(parking2)
        P3 = P1.copy()
        P3.move_to(parking3)
        P4 = P1.copy()
        P4.move_to(parking4)

        matrix = [[1, 1, 1, 35], [3, 2, 1, 75], [4, 3, 1, 105]]
        E = Matrix(matrix,element_alignment_corner=UR,v_buff=1.8, h_buff=1.8, bracket_h_buff=0.75, bracket_v_buff=0.75).scale(0.7)

        x1 = Tex("\(x\)")
        y1 = Tex("\(y\)")
        z1 = Tex("\(z\)")
        x2 = Tex("\(x\)")
        y2 = Tex("\(y\)")
        z2 = Tex("\(z\)")
        x3 = Tex("\(x\)")
        y3 = Tex("\(y\)")
        z3 = Tex("\(z\)")

        self.wait(2)

        with self.voiceover(text='''.......First, we will represent this same set of equations using the variables x , y and z. 
                            We will now convert them into matrix form.''') as tracker:
        
            self.play(AnimationGroup(*[FadeIn(apple1,shift = 0.25*RIGHT),FadeIn(no_apple1),
                FadeIn(plus1,shift = 0.25*RIGHT), FadeIn(mango1,shift = 0.25*RIGHT), FadeIn(no_mango1),
                FadeIn(plus2,shift = 0.25*RIGHT),FadeIn(parking1,shift = 0.25*RIGHT),FadeIn(equal1,shift = 0.25*RIGHT),
                FadeIn(ans1,shift = 0.25*RIGHT)  ],lag_ratio = 0.4),run_time = 1)
        
            self.play(AnimationGroup(*[FadeIn(apple2,shift = 0.25*RIGHT),FadeIn(no_apple2),
                FadeIn(plus3,shift = 0.25*RIGHT), FadeIn(mango2,shift = 0.25*RIGHT), FadeIn(no_mango2),
                 FadeIn(plus4,shift = 0.25*RIGHT),FadeIn(parking2,shift = 0.25*RIGHT),FadeIn(equal2,shift = 0.25*RIGHT),
                                FadeIn(ans2,shift = 0.25*RIGHT)  ],lag_ratio = 0.5),run_time = 1)
        
            self.play(AnimationGroup(*[FadeIn(apple3,shift = 0.25*RIGHT),FadeIn(no_apple3),
                FadeIn(plus5,shift = 0.25*RIGHT), FadeIn(mango3,shift = 0.25*RIGHT), FadeIn(no_mango3),
                 FadeIn(plus6,shift = 0.25*RIGHT),FadeIn(parking3,shift = 0.25*RIGHT),FadeIn(equal3,shift = 0.25*RIGHT),
                                FadeIn(ans3,shift = 0.25*RIGHT)  ],lag_ratio = 0.4),run_time = 1)

            self.play(FadeOut(apple1,mango1,parking1),FadeOut(apple2,mango2,parking2),FadeOut(apple3, mango3, parking3))
            self.play(Write(x1.next_to(no_apple1,RIGHT)),Write(y1.next_to(no_mango1,RIGHT)),Write(z1.next_to(plus2,RIGHT)),Write(x2.next_to(no_apple2,RIGHT)),Write(y2.next_to(no_mango2,RIGHT)),Write(z2.next_to(plus4,RIGHT)),
                      Write(x3.next_to(no_apple3,RIGHT)),Write(y3.next_to(no_mango3,RIGHT)),Write(z3.next_to(plus6,RIGHT)))
        
        vid = Group(no_apple1,x1,plus1,y1,no_mango1,plus2,z1,equal1,ans1,no_apple2,x2,plus3,y2,no_mango2,plus4,z2,equal2,ans2,no_apple3,x3,plus5,y3,no_mango3,plus6,z3,equal3,ans3)
        self.play(FadeOut(vid))

        with self.voiceover(text=''' A matrix is a rectangular arrangement of numbers organized in rows and columns, similar to a table.''') as tracker:
            rec1 = RoundedRectangle(corner_radius=0.2, height = 0.7, width = 5.5, color=PINK).next_to(E,0.01*LEFT).shift(0.82*UP+2.2*RIGHT)
            rec2 = RoundedRectangle(corner_radius=0.2, height = 0.7, width = 5.5, color=PINK).next_to(E,0.01*LEFT).shift(2.2*RIGHT)
            rec3 = RoundedRectangle(corner_radius=0.2, height = 0.7, width = 5.5, color=PINK).next_to(E,0.01*LEFT).shift(0.8*DOWN+2.4*RIGHT)
            self.play(Write(E),E[0].animate.set_color(BLACK),run_time=0.01)

            arr1 = Arrow(start=2*LEFT, end=2*RIGHT, color=YELLOW).next_to(E,UP)
            arr2 = Arrow(start=2*UP, end=2*DOWN, color=YELLOW).next_to(E,LEFT)
            col = Text("columns", color=YELLOW,font_size=22).next_to(arr1,UP)
            row = Text("rows", color=YELLOW,font_size=22).next_to(arr2,0.5*LEFT).rotate(PI/2)
            grp = Group(arr1, arr2, row, col)

            self.wait(1)
            self.play(Create(arr1),Create(arr2))
            self.play(Write(row), Write(col))
            self.play(E.get_rows()[0].animate.set_color(WHITE))
            self.play(E.get_rows()[1].animate.set_color(WHITE))
            self.play(E.get_rows()[2].animate.set_color(WHITE))
            self.play(FadeOut(grp,E))

        with self.voiceover(text='''A system of equations can be represented using an augmented matrix, where each row corresponds to one equation in the system.......
        Thus giving us a 3 by 4 matrix having 3 rows and 4 columns.''') as tracker:
            self.play(FadeIn(vid))
            self.play(vid.animate.shift(2*DOWN+3.5*LEFT).scale(0.8))
            self.play(Write(E.next_to(vid,3.5*RIGHT)),E[0].animate.set_color(BLACK),run_time=0.01)
            self.play(Create(rec1),E.get_rows()[0].animate.set_color(WHITE))
            self.wait(0.5)
            self.play(FadeOut(rec1))
            self.play(Create(rec2),E.get_rows()[1].animate.set_color(WHITE))
            self.wait(0.5)
            self.play(FadeOut(rec2))
            self.play(Create(rec3),E.get_rows()[2].animate.set_color(WHITE))
            self.play(FadeOut(rec3))
            self.play(FadeOut(vid),E.animate.shift(3*LEFT))
            arr3 = Arrow(start=2*LEFT, end=2*RIGHT, color=YELLOW).next_to(E,UP)
            arr4 = Arrow(start=2*UP, end=2*DOWN, color=YELLOW).next_to(E,LEFT)
            col1 = Text("4 - columns", color=YELLOW,font_size=22).next_to(arr3,UP)
            row1 = Text("3 - rows", color=YELLOW,font_size=22).next_to(arr4,0.5*LEFT).rotate(PI/2)
            grp1 = Group(arr3, arr4, row1, col1)
            self.play(Create(arr3),Create(arr4))
            self.play(Write(row1), Write(col1))
            self.play(FadeOut(grp1))

        with self.voiceover(text='''Here, the first column represents the x-coefficients, 
                                the second column represents y-coefficients, the third represents z-coefficients, 
                                and the fourth represents constants.''') as tracker:
                a1 = E[0][0]
                a2 = E[0][8]
                r = VGroup(a1,a2)
                r1 = SurroundingRectangle(r)
                arr = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(r1,2*UP).rotate(PI/2).scale(0.6)
                tx1 = Text("x-coefficients",font_size=20,color=YELLOW).next_to(arr,UP)
                self.play(Create(r1),Create(arr))
                self.play(Write(tx1))
                self.play(FadeOut(r1,arr,tx1))

                a1 = E[0][1]
                a2 = E[0][9]
                r = VGroup(a1,a2)
                r1 = SurroundingRectangle(r)
                arr = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(r1,2*UP).rotate(PI/2).scale(0.6)
                tx1 = Text("y-coefficients",font_size=20,color=YELLOW).next_to(arr,UP)
                self.play(Create(r1),Create(arr))
                self.play(Write(tx1),run_time=0.5)
                self.play(FadeOut(r1,arr,tx1))

                a1 = E[0][2]
                a2 = E[0][10]
                r = VGroup(a1,a2)
                r1 = SurroundingRectangle(r)
                arr = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(r1,2*UP).rotate(PI/2).scale(0.6)
                tx1 = Text("z-coefficients",font_size=20,color=YELLOW).next_to(arr,UP)
                self.play(Create(r1),Create(arr))
                self.play(Write(tx1),run_time=0.5)
                self.play(FadeOut(r1,arr,tx1))

                a1 = E[0][3]
                a2 = E[0][11]
                r = VGroup(a1,a2)
                r1 = SurroundingRectangle(r)
                arr = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(r1,2*UP).rotate(PI/2).scale(0.6)
                tx1 = Text("constants",font_size=20,color=YELLOW).next_to(arr,UP)
                self.play(Create(r1),Create(arr))
                self.play(Write(tx1),run_time=0.5)
                self.play(FadeOut(r1,arr,tx1))
            
        i1 = Text("INPUT", font_size=22, color=RED)
        o1 = Text("OUTPUT", font_size=22, color=GREEN)

        with self.voiceover(text='''
Now, we will divide the process into two parts, represented by two blocks of code.
First, we will use the eliminate function to eliminate the variables as we go from top to bottom.
The augmented matrix E will act as the input for this function........
Here, top to Bottom means that we work row by row, starting with the first row.
                           ''') as tracker:
                
                self.play(E.animate.shift(3.5*RIGHT).scale(0.75))

                code1 = '''
def eliminate(E):
    for i in range(len(E)):
        for j in range(i+1, len(E)):
            mult = E[j][i]/E[i][i]
            for k in range(i, len(E[i])):
                E[j][k] -= E[i][k]*mult
    return E'''
                bg = "window"
                code2 = '''
def solve_elimination(E):
    solution = [0 for _ in range(len(E))]
    i = len(E) - 1
    j = len(E[0]) - 2
    while i > -1:
        row = E[i]
        sum = 0
        for k in range(j+1, len(row) - 1):
            sum += row[k]*solution[k]
        solution[j] = (row[-1] - sum)/row[j]
        i -= 1
        j -= 1
    return solution
'''
                arr5 = Arrow(start=1.5*UP, end=1.5*DOWN, color=YELLOW).next_to(E,LEFT)
                tb = Text("Top to Bottom", font_size=22, color=YELLOW).next_to(E,DOWN)
                grp2 = Group(arr5,tb)
                cd1 = Code(code=code1, tab_width=5, line_spacing=0.5, language="Python", background=bg).shift(3.1*LEFT+2*UP).scale(0.65)
                cd2 = Code(code=code2, tab_width=5, line_spacing=0.5, background=bg,language="Python").shift(3.1*LEFT+1.3*DOWN).scale(0.65)
                rect1 = SurroundingRectangle(cd1, corner_radius=0.1)
                rect2 = SurroundingRectangle(cd2, corner_radius=0.1)
                rect3 = SurroundingRectangle(E.get_rows()[0], color=PINK, corner_radius=0.2)
                rect4 = SurroundingRectangle(E.get_rows()[1], color=PINK, corner_radius=0.2)
                rect5 = SurroundingRectangle(E.get_rows()[2], color=PINK, corner_radius=0.2)
                self.play(Write(cd1),Write(cd2),run_time=2)
                self.play(Create(rect1),Create(rect2),run_time=2)
                self.wait(1)
                self.play(FadeOut(rect2))
                self.wait(3)
                self.play(Write(i1.next_to(E,UP)))
                self.wait(5)
                self.play(Create(arr5), Write(tb))
                self.play(Create(rect3))
                self.play(FadeOut(rect3), Create(rect4))
                self.play(FadeOut(rect4), Create(rect5))
                self.play(FadeOut(rect5))

                self.play(FadeOut(i1, grp2))
        
        with self.voiceover(text='''It will give us the required matrix as the output...... Then, we will pass the output to the solve elimination function which solves the variables from bottom to top.
Bottom to top means that we start with the last row and move upward.
When we reach the topmost row, we will have determined the value of every variable, giving us the solution..............
Does this sound confusing? Let’s break it down in more detail to make it clearer.
                            ''') as tracker:
            A = [[1,1,1,35],[0,-1,-2,-30],[0,0,-1,-5]]
            E1 = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).shift(3.6*RIGHT).scale(0.5)
            self.play(FadeTransformPieces(E,E1),run_time=2)
            self.play(Write(o1.next_to(E1,UP)))
            self.wait(1)
            self.play(FadeOut(rect1))
            arr6 = Arrow(start=1.5*DOWN, end=1.5*UP, color=YELLOW).next_to(E1,LEFT)
            bt = Text("Bottom to Top", font_size=22, color=YELLOW).next_to(E1,DOWN)
            grp3 = Group(arr6,bt)
            rect6 = SurroundingRectangle(E1.get_rows()[2], color=PINK, corner_radius=0.2)
            rect7 = SurroundingRectangle(E1.get_rows()[1], color=PINK, corner_radius=0.2)
            rect8 = SurroundingRectangle(E1.get_rows()[0], color=PINK, corner_radius=0.2)
            self.play(FadeIn(rect2))
            self.play(FadeOut(o1))
            self.play(Write(i1.next_to(E1,UP)))
            self.wait(4)
            self.play(Create(arr6), Write(bt))
            self.play(Create(rect6))
            self.play(FadeOut(rect6), Create(rect7))
            self.play(FadeOut(rect7), Create(rect8))
            self.wait()
            self.play(FadeOut(rect8))
            self.play(FadeOut(i1, grp3))
            B = [[10, 20, 5]]
            F = Matrix(B,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.5, bracket_v_buff=0.5).shift(3.6*RIGHT).scale(0.5)
            aro1 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][0],DOWN)
            xx1 = Text("x",font_size=18,color=YELLOW).next_to(aro1,DOWN)
            aro2 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][1],DOWN)
            yy1 = Text("y",font_size=18,color=YELLOW).next_to(aro2,DOWN)
            aro3 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][2],DOWN)
            zz1 = Text("z",font_size=18,color=YELLOW).next_to(aro3,DOWN)
            self.play(Transform(E1, F))
            self.play(Write(o1.next_to(F,UP)),Create(aro1),Write(xx1),Create(aro2),Write(yy1),Create(aro3),Write(zz1))
            self.wait(2)
            self.play(FadeOut(rect2))

        self.play(FadeOut(cd1, cd2, o1,aro1,xx1,aro2,yy1,aro3,zz1, E1, F))

########################   PART - 1 Eliminate Fubction ###########################

        bg = "window"
        row_len = 3
        col_len = 4
        
        code = '''
def eliminate(E):
    for i in range(len(E)):
        for j in range(i+1, len(E)):
            mult = E[j][i]/E[i][i]
            for k in range(i, len(E[i])):
                E[j][k] -= E[i][k]*mult
    return E'''
    
        cd = Code(code=code, line_spacing = 0.7, tab_width=5, language="Python", background=bg)

        Cb = [0 for _ in range(7)]
        ind_i = [0 for _ in range(row_len)]
        ind_j = [0 for _ in range(col_len)]
        I = [0 for _ in range(3)]
        J = [0 for _ in range(2)]
    
        Cb[0] = always_redraw(lambda: SurroundingRectangle(cd[2][0], stroke_width=3, color=PINK, corner_radius = 0.1 ,buff = 0.03))
        Cb[1] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=2.8, height=0.25, color=PINK).move_to(3.74*LEFT+0.40*UP)
        Cb[2] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5,width=3.4, height=0.258, color=PINK).move_to(2.85*LEFT+0.15*UP)
        Cb[3] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5,width=2.7, height=0.26, color=PINK).move_to(2.63*LEFT+0.11*DOWN)
        Cb[4] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5,width=3.5, height=0.25, color=PINK).move_to(2.21*LEFT+0.36*DOWN)
        Cb[5] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5,width=2.85, height=0.26, color=PINK).move_to(1.97*LEFT+0.61*DOWN)
        Cb[6] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5,width=1.1, height=0.25, color=PINK).move_to(4.6*LEFT+0.855*DOWN)

        with self.voiceover(text='''Here is the complete code for the eliminate function. To understand how it works, we must first go 
                            through the code step by step.
                            ''') as tracker:
            self.play(Write(cd),run_time=2)
            self.play(Create(Cb[0]))

        self.play(cd.animate.shift(3.27*LEFT).scale(0.6))

        A = [[1, 1, 1, 35], [3, 2, 1, 75], [4, 3, 1, 105]]
        E = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).move_to(4*RIGHT).scale(0.6)
        with self.voiceover(text="E represents our augmented matrix.") as tracker:
            # self.play(AnimationGroup(*[Write(E),E[0].animate.set_color(BLACK)]))
            self.play(Write(E),E[0].animate.set_color(BLACK),run_time=0.01)
            self.play(E[0].animate.set_color(WHITE))
            arr7 = Arrow(start=2*LEFT, end=2*RIGHT, color=YELLOW).next_to(E,UP)
            arr8 = Arrow(start=1.5*UP, end=1.5*DOWN, color=YELLOW).next_to(E,LEFT)
            col2 = Text("4 - columns", color=YELLOW,font_size=22).next_to(arr7,UP)
            row2 = Text("3 - rows", color=YELLOW,font_size=22).next_to(arr8,0.5*LEFT).rotate(PI/2)
            grp4 = Group(arr7, arr8, row2, col2)
            self.play(Create(arr7),Create(arr8))
            self.play(Write(row2), Write(col2))
    
        Cb[0].clear_updaters()

        with self.voiceover(text='''The i loop refers to the i-th row of the matrix 
Its value ranges from 0 to the length of the matrix E, which corresponds to the number of rows. In this case, the length of the matrix E is 3. Therefore, i = 0, 1 and, 2.
We will not include 3 here because, the for loop functions only, when the condition i less than length of the matrix holds true.
But, Why start from 0 ? 
In Python, the indexing starts at 0, so 0 represents the first index.
''') as tracker:
            self.play(Transform(Cb[0], Cb[1]))
            iloop = Text("i = 0, 1, 2", font_size=22).next_to(cd, 2*DOWN)
            il = Text("i < length of the matrix [len(E) = 3]",font_size=22).next_to(iloop, 2*DOWN)
            self.wait(12)
            self.play(Write(iloop))
            self.wait(5)
            self.play(Write(il))

        self.play(FadeOut(iloop,il))
        self.wait()

        with self.voiceover(text='''The j loop refers to the j-th row.
Its value ranges from i+1 to length of the matrix E which is 3. 
Both of these loops help us to follow the top to bottom approach and iterate over the matrix row-by-row.
''') as tracker:
            self.play(Transform(Cb[0], Cb[2]))
        self.wait()
        
        with self.voiceover(text='''Mult refers to the multiplier constant. We will discuss its functioning later in the video.
                            ''') as tracker:
            self.play(Transform(Cb[0], Cb[3]))
        self.wait()

        with self.voiceover(text='''The k loop ranges from i to the length of i-th row in the matrix E. 
                            Length of the row refers to the number of elements in a row, which corresponds to the number of columns in the matrix which is equal to 4.
                            ''') as tracker:
            self.play(Transform(Cb[0],Cb[4]))
        self.wait()

        with self.voiceover(text = '''Together, these loops systematically reduce the matrix to a simpler form by eliminating elements from 
                            subsequent rows, following the elimination process.
                            ''') as tracker:
             self.play(Transform(Cb[0],Cb[5]))
        
        self.play(FadeOut(grp4, Cb[0]))
        self.wait()

        with self.voiceover(text='''These are the indices for the rows and the columns.
                            We will be using them to address the elements of the matrix.
                            ''') as tracker:
            # Mark the indices of rows
            for i in range(row_len):
                ind_i[i] = Text(str(i),font_size=24,color = GREEN).next_to(E[0][i*col_len], 3.5*LEFT)
                self.play(Write(ind_i[i]),run_time=0.3)
            self.wait()
            # Mark the indices of columns
            for j in range(col_len):
                ind_j[j] = Text(str(j),font_size=24,color = GREEN).next_to(E[0][2*col_len+j],5*DOWN)
                self.play(Write(ind_j[j]),run_time=0.3)
        
        for i in range(len(I)):
            I[i] = Text("i", weight=BOLD, font_size = 33, color = RED).next_to(E[0][i*col_len],6*LEFT)

        self.wait()
        self.play(Transform(Cb[0],Cb[1]))

        loop1 = Text("First loop : ",font_size=22, color=PURPLE).next_to(cd,2*DOWN)
        iloop1 = Text("i = 0", font_size=22).next_to(loop1,RIGHT)
        jloop1 = Text("j = 1,2", font_size=22).next_to(iloop1,2*DOWN)
        kloop1 = Text("k = 0,1,2,3", font_size=22).next_to(jloop1,2*DOWN)

        loop2 = Text("Second loop : ",font_size=22, color=PURPLE).next_to(cd,2*DOWN)
        iloop2 = Text("i = 1", font_size=22).next_to(loop2,RIGHT)
        jloop2 = Text("j = 2", font_size=22).next_to(iloop2,2*DOWN)
        kloop2 = Text("k = 1,2,3", font_size=22).next_to(jloop2,2*DOWN)

        loop3 = Text("Third loop : ",font_size=22, color=PURPLE).next_to(cd,2*DOWN)
        iloop3 = Text("i = 2", font_size=22).next_to(loop3,RIGHT)
        jloop3 = Text("j = 3 < 3", font_size=22).next_to(iloop3,2*DOWN)
        
        with self.voiceover(text='''Now, let's see the working of this code.
In the first loop, i = 0 which refers to the first row of the matrix.
''') as tracker:
            self.wait(1)
            self.play(E[0].animate.set_color(BLACK))
            self.wait(1)
            self.play((E.get_rows()[0]).animate.set_color(WHITE),Write(I[0]))
            self.play(Write(loop1),Write(iloop1)) 
        
        for j in range(len(J)):
            J[j] = Text("j", weight=BOLD, font_size = 33, color = RED).next_to(E[0][(j+1)*col_len], 6*LEFT)
        self.wait()
        with self.voiceover(text='''The value of j is equal to 1 and 2 as the for loop ranges from i+1 to len E...... 
        It means that when i = 0, the j loop will run twice...........First, j = 1 which refers to the second row of the matrix.
        Don’t get confused and remember that indexing in Python starts at 0.''') as tracker:  
            self.play(Transform(Cb[0],Cb[2]))
            self.play(Write(jloop1))
            self.wait(8)  
            self.play((E.get_rows()[1]).animate.set_color(WHITE), Write(J[0]))
        self.wait()

        K = Text("k",font_size=24, color=RED)

        mult = Text("mult", weight=BOLD, font_size=24, color=ORANGE).move_to(3*UP).shift(1.5*RIGHT)
        eq1 = Text(" = ",font_size=24).next_to(mult,RIGHT)
        l1 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq1,RIGHT)
        e1 = Text("E[j][i]", font_size=24).next_to(l1,UP)
        e2 = Text("E[i][i]", font_size=24).next_to(l1,DOWN)
        e3 = Text("E[1][0]", font_size=24).next_to(l1,UP)
        e4 = Text("E[0][0]", font_size=24).next_to(l1,DOWN)
        eq2 = Text(" = ",font_size=24).next_to(l1,RIGHT)
        l2 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq2,RIGHT)
        eq3 = Text(" = ",font_size=24).next_to(l2,RIGHT)
        ri0 = SurroundingRectangle(ind_i[0])
        ri1 = SurroundingRectangle(ind_i[1])
        ri2 = SurroundingRectangle(ind_i[2])
        rj0 = SurroundingRectangle(ind_j[0])
        rj1 = SurroundingRectangle(ind_j[1])
        rj2 = SurroundingRectangle(ind_j[2])
        rj3 = SurroundingRectangle(ind_j[3])

        for i in range(0,1):
            with self.voiceover(text='''The goal is to eliminate the elements in the j-th row.
For this, the coefficients in both rows must be the same. So, we calculate the multiplier constant by dividing the first element of the j-th row 
by the first element of the i-th row. Here, E-j-i which is E,1,0 = 3..............and E-i-i which is E,0,0 = 1.............Therefore, the multiplier constant comes out to be 3.
''') as tracker:
                self.play(Transform(Cb[0], Cb[3]))
                self.wait(5)
                self.play(Write(mult),Write(eq1),Create(l1))
                r = VGroup(E[0][i],E[0][i+col_len])
                rec = SurroundingRectangle(r)
                self.wait(2)
                a1 = E[0][i+col_len].copy()
                a2 = E[0][i].copy()
                self.play(Write(e1), Write(e2))
                self.wait(2)
                self.play(Create(rec))
                self.play(Write(eq2),Create(l2))
                self.play(Create(ri1),Create(rj0))
                self.play(Transform(e1,e3))
                self.play(a1.animate.move_to(l2).shift(UP*0.3))
                self.play(FadeOut(ri1,rj0))
                self.play(Create(ri0),Create(rj0))
                self.play(Transform(e2,e4))
                self.play(a2.animate.move_to(l2).shift(DOWN*0.3))
                self.play(FadeOut(ri0,rj0))
                m = int(A[1][i]/A[0][i])
                mut = Text(str(m),font_size=22,font="Times New Roman")
                self.wait()
                self.play(Write(eq3),Write(mut.next_to(eq3,RIGHT)))
                self.play(FadeOut(a1,l1,e1,e2,l2,a2,eq2,eq3,rec),run_time=0.5)
                self.play(mut.animate.move_to(eq1).shift(0.5*RIGHT))
                grp5 = Group(mult,eq1,mut)
                self.play(grp5.animate.shift(2*RIGHT))
                self.wait()
            self.play(Transform(Cb[0], Cb[4]))
        
        
        eq2 = Text(" = ",font_size=24)
        eq3 = Text(" = ",font_size=24)
        eq4 = Text(" = ",font_size=24)
        sub = Text(" - ",color=BLUE)
        ast = Text(" * ",color=BLUE, font_size=24)
        b1 = Text(" ( ",font_size=24)
        b2 = Text(" ) ",font_size=24)

        with self.voiceover(text='''Here, comes our k loop. It's value ranges from 0 to 3, as i = 0 and len E i = 4..............The k loop will multiply each element of the i-th row by the multiplier constant, 
                            subtract it from the corresponding element of the j-th row and update the value simultaneously.
                                ''') as tracker:
            for k in range(1):
                re1 = SurroundingRectangle(E.get_rows()[0], color=PINK, corner_radius=0.2)
                re2 = SurroundingRectangle(E.get_rows()[1], color=PINK, corner_radius=0.2)
                strg = Text("E[j][k]",weight=BOLD, font_size=24, color=YELLOW).next_to(mult,2*DOWN+2*LEFT)
                strg1 = Text("E[j][k]",weight=BOLD, font_size=24, color=YELLOW)
                strg2 = Text("E[i][k]",weight=BOLD, font_size=24, color=YELLOW)
                strg3 = Text("mult",weight=BOLD, font_size=24, color=YELLOW)
                self.wait(3)
                self.play(Write(kloop1))
                self.wait(4)
                self.play(Transform(Cb[0], Cb[5]))
                self.play(Create(re1))
                self.play(Write(strg2.next_to(mult,2*DOWN)),Write(ast.next_to(strg2,0.5*RIGHT)),Write(strg3.next_to(ast,0.5*RIGHT)),run_time=2)
                grp6 = Group(strg2,ast,strg3)
                self.play(grp6.animate.shift(1.5*RIGHT))
                self.play(Create(re2))
                self.play(Write(strg),Write(eq3.next_to(strg,0.5*RIGHT)),Write(strg1.next_to(eq3,0.5*RIGHT)),run_time=2)
                self.play(Write(sub.next_to(strg1,0.5*RIGHT)),Write(b1.next_to(sub,0.5*RIGHT)),Write(b2.next_to(strg3,0.5*RIGHT)))
                self.wait(2)
        self.play(FadeOut(sub,b1,strg,eq3,strg1,strg2,strg3,sub,re1,re2,ast,b2))        
        r.clear_updaters()
        self.play(Transform(Cb[0], Cb[4]))

        arr=[]

        with self.voiceover(text='''
At first, k is 0. So, we will multiply E-i-k which is E zero zero by the multiplier constant......and subtract it from E-j-k which is E one zero. On solving the first element from the second row gets eliminated.........Then, k will become 1...............
will multiply E zero one with the multiplier constant.......................subtract it from E one one............................and will update the......second row again.................
This process of.......multiplication and subtraction will continue..........for every element of the second row.
                            ''') as tracker:
            for k in range(col_len):
                if k==3:
                    with self.voiceover('''So, at last, the value of k will be 3............which will update the fourth element in the second row...................
            ''') as tracker:
                        a3 = E[0][k+col_len].copy()
                        a4 = E[0][k].copy()
                        mut2 = mut.copy()
                        r = VGroup(a3, a4)
                        rec = SurroundingRectangle(r)
                        self.play(Create(rec),Write(K.next_to(rec,2*DOWN)))
                        self.play(Transform(Cb[0], Cb[5]))
                        strg = Text("E["+str(1)+"]["+str(k)+"]",font_size=24, color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                        self.play(Create(ri0),Create(rj3))
                        self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                        self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)),run_time=0.5)
                        grp8 = Group(a4,ast,mut2)
                        self.play(FadeOut(ri0,rj3),grp8.animate.shift(1*RIGHT),run_time=0.5)
                        self.play(Create(ri1),Create(rj3),Write(strg),Write(eq3.next_to(strg,RIGHT)))
                        self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                        self.play(Write(sub.next_to(a3,RIGHT)),Write(b1.next_to(sub,0.8*RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)),run_time=0.5)
                        ans = (A[1][k] - (A[0][k]*m))
                        answer = Text(str(ans),font_size=22, font="Times New Roman").next_to(strg,5*RIGHT)
                        grop = Group(a4,b1,b2,ast,mut2)
                        self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                        self.play(FadeOut(ri1,rj3,rec,K),run_time=0.5)
                        fin = answer.copy().move_to(E[0][k+col_len])
                        fin1 = answer.copy()
                        arr.append(fin1)
                        with self.voiceover(text='''With it, the first iteration of the j loop comes to an end.......
                        This indicates that the second row is updated successfully.''') as tracker:
                            self.play(AnimationGroup(*[fin1.animate.move_to(E[0][col_len+k]),AnimationGroup(*[FadeOut(E[0][col_len+k])],run_time=0.5)],lag_ratio=0.6))
                            self.play(FadeOut(strg, eq3, answer),run_time=0.5)
                            self.play(Transform(Cb[0],Cb[2]))
                else:
                    a3 = E[0][k+col_len].copy()
                    a4 = E[0][k].copy()
                    mut2 = mut.copy()
                    r = VGroup(a3, a4)
                    rec = SurroundingRectangle(r)
                    self.play(Create(rec),Write(K.next_to(rec,2*DOWN)))
                    self.play(Transform(Cb[0], Cb[5]))
                    strg = Text("E["+str(1)+"]["+str(k)+"]",font_size=24,color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                    rj = SurroundingRectangle(ind_j[k])
                    self.play(Create(ri0),Create(rj))
                    if k==0:
                        self.wait()
                    self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                    self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)))
                    grp7 = Group(a4,ast,mut2)
                    self.play(FadeOut(ri0,rj),grp7.animate.shift(1*RIGHT))
                    self.play(Create(ri1),Create(rj))
                    self.play(Write(strg),Write(eq3.next_to(strg,RIGHT)))
                    self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                    self.play(Write(sub.next_to(a3,RIGHT)),Write(b1.next_to(sub,RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)))
                    ans = (A[1][k] - (A[0][k]*m))
                    answer = Text(str(ans),font_size=22,font="Times New Roman").next_to(strg,5*RIGHT)
                    if k == 0:
                        self.wait()
                    grop = Group(a4,b1,b2,ast,mut2)
                    self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                    self.play(FadeOut(ri1,rj,rec,K),run_time=0.5)
                    fin = answer.copy().move_to(E[0][k+col_len])
                    fin1 = answer.copy()
                    arr.append(fin1)
                    self.play(AnimationGroup(*[fin1.animate.move_to(E[0][col_len+k]),AnimationGroup(*[FadeOut(E[0][col_len+k])],run_time=0.5)],lag_ratio=0.6))
                    self.play(FadeOut(strg, eq3, answer),run_time=0.5)
                    self.play(Transform(Cb[0], Cb[4]))
                r.clear_updaters()
                mut.clear_updaters()
        self.play(FadeOut(mult,eq1,mut,J[0]))
        for i in range(len(arr)):
            self.play(FadeOut(arr[i]),run_time=0.01)

        with self.voiceover(text="Now, the value of j = 2 which refers to the third row of the matrix.") as tracker:
            self.play((E.get_rows()[2]).animate.set_color(WHITE),Write(J[1]))
        
        mult = Text("mult", weight=BOLD, font_size=24, color=ORANGE).move_to(3*UP).shift(1.5*RIGHT)
        eq1 = Text(" = ",font_size=24).next_to(mult,RIGHT)
        l1 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq1,RIGHT)
        e1 = Text("E[j][i]", font_size=24).next_to(l1,UP)
        e2 = Text("E[i][i]", font_size=24).next_to(l1,DOWN)
        e3 = Text("E[2][0]", font_size=24).next_to(l1,UP)
        e4 = Text("E[0][0]", font_size=24).next_to(l1,DOWN)
        eq2 = Text(" = ",font_size=24).next_to(l1,RIGHT)
        l2 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq2,RIGHT)
        eq3 = Text(" = ",font_size=24).next_to(l2,RIGHT)

        with self.voiceover(text='''We will again calculate the multiplier constant.....So, E-j-i which is E two zero = 4................and E-i-i which is E zero zero = 1..............On dividing, the multiplier constant = 4.
                            ''') as tracker:
            for i in range(0,1):
                self.play(Transform(Cb[0], Cb[3]))
                self.play(Write(mult), Write(eq1), Create(l1))
                r = VGroup(E[0][i],E[0][2*col_len])
                rec = SurroundingRectangle(r)
                a1 = E[0][2*col_len].copy()
                a2 = E[0][i].copy()
                self.play(Write(e1), Write(e2),Create(rec))
                self.play(Write(eq2),Create(l2),Create(ri2),Create(rj0))
                self.play(Transform(e1,e3))
                self.play(a1.animate.move_to(l2).shift(UP*0.3))
                self.play(FadeOut(ri2,rj0))
                self.play(Create(ri0),Create(rj0))
                self.play(Transform(e2,e4))
                self.play(a2.animate.move_to(l2).shift(DOWN*0.3))
                self.play(FadeOut(ri0,rj0))
                m = int(A[2][i]/A[0][i])
                mut = Text(str(m),font_size=22,font="Times New Roman")
                self.play(Write(eq3),Write(mut.next_to(eq3,RIGHT)))
                self.play(FadeOut(a1,l1,e1,e2,l2,a2,eq2,eq3,rec),run_time=0.5)
                self.play(mut.animate.move_to(eq1).shift(0.5*RIGHT))
                grp9 = Group(mult,eq1,mut)
                self.play(grp9.animate.shift(2*RIGHT))

        with self.voiceover(text='''This time k loop will perform operations on the third row.
                            ''') as tracker:
            self.play(Transform(Cb[0], Cb[4]))
            
        eq2 = Text(" = ",font_size=24)
        eq3 = Text(" = ",font_size=24)
        eq4 = Text(" = ",font_size=24)
        sub = Text(" - ",color=BLUE)
        ast = Text(" * ",color=BLUE, font_size=24)
        b1 = Text(" ( ",font_size=24)
        b2 = Text(" ) ",font_size=24)

        arr = []

        with self.voiceover(text='''
We will again start with k = 0. Will multiply E-i-k which is E zero zero by the multiplier constant and subtract it from E-j-k which is E two zero. On solving, 
the first element of the third row gets eliminated........Then, k will become 1..........will multiply E zero one with the multiplier constant.......................subtract it from E two one
......................and will update the third row again...............................We will perform these.........same operations.........on the remaining elements..................
''') as tracker:
            run = 1
            for k in range(col_len):
                a3 = E[0][2*col_len+k].copy()
                a4 = E[0][k].copy()
                mut2 = mut.copy()
                r = VGroup(a3, a4)
                rec = SurroundingRectangle(r)
        
                if k == 3:
                    with self.voiceover(text='''At the end, every element of the third row gets updated''') as tracker:
                        self.play(Create(rec),Write(K.next_to(rec,2*DOWN)))
                        self.play(Transform(Cb[0], Cb[5]))
                        strg = Text("E["+str(2)+"]["+str(k)+"]",font_size=24,color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                        self.play(Create(ri0),Create(rj3))
                        self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                        self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)),run_time=0.5)
                        grp8 = Group(a4,ast,mut2)
                        self.play(FadeOut(ri0,rj3),grp8.animate.shift(1*RIGHT),run_time=0.5)
                        self.play(Create(ri2),Create(rj3),Write(strg),Write(eq3.next_to(strg,RIGHT)))
                        self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                        self.play(Write(sub.next_to(a3,RIGHT)),Write(b1.next_to(sub,0.7*RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)),run_time=0.5)
                        ans = (A[2][k] - (A[0][k]*m))
                        answer = Text(str(ans),font_size=22,font="Times New Roman").next_to(strg,5*RIGHT)
                    with self.voiceover(text='''
With it, the j loop comes to an end..........
                                        ''') as tracker:
                        grop = Group(a4,b1,b2,ast,mut2)
                        self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                        self.play(FadeOut(ri2,rj3,rec,K),run_time=0.5)
                        fin = answer.copy().move_to(E[0][2*col_len+k])
                        fin1 = answer.copy()
                        arr.append(fin1)
                        self.play(AnimationGroup(*[fin1.animate.move_to(E[0][2*col_len+k]),AnimationGroup(*[FadeOut(E[0][2*col_len+k])],run_time=0.5)],lag_ratio=0.6))
                        self.play(FadeOut(answer,eq3,strg,mult,eq1,mut,loop1,iloop1,jloop1,kloop1),run_time=0.5)
                        mut.clear_updaters()
                        self.wait()
                        self.play(Transform(Cb[0], Cb[1]))
                       
                else:
                    self.play(Create(rec),Write(K.next_to(rec,2*DOWN)))
                    self.play(Transform(Cb[0], Cb[5]))
                    strg = Text("E["+str(2)+"]["+str(k)+"]",font_size=24,color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                    rj = SurroundingRectangle(ind_j[k])
                    self.play(Create(ri0),Create(rj))
                    if k==0:
                        self.wait()
                    self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                    self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)))
                    grp7 = Group(a4,ast,mut2)
                    self.play(FadeOut(ri0,rj),grp7.animate.shift(1*RIGHT))
                    self.play(Create(ri2),Create(rj),Write(strg),Write(eq3.next_to(strg,RIGHT)))
                    self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                    self.play(Write(sub.next_to(a3,RIGHT)),Write(b1.next_to(sub,RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)))
                    ans = (A[2][k] - (A[0][k]*m))
                    answer = Text(str(ans),font_size=22,font="Times New Roman").next_to(strg,5*RIGHT)
                    if k==0:
                        self.wait(2)
                    grop = Group(a4,b1,b2,ast,mut2)
                    self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                    self.play(FadeOut(ri2,rj,rec,K),run_time=0.5)
                    fin = answer.copy().move_to(E[0][2*col_len+k])
                    fin1 = answer.copy()
                    arr.append(fin1)
                    self.play(AnimationGroup(*[fin1.animate.move_to(E[0][2*col_len+k]),AnimationGroup(*[FadeOut(E[0][2*col_len+k])],run_time=0.5)],lag_ratio=0.6))
                    self.play(FadeOut(strg, eq3, answer),run_time=0.5)
                    self.play(Transform(Cb[0], Cb[4]))
                r.clear_updaters()

        self.play(FadeOut(arr[0],arr[1],arr[2],arr[3]),(E.get_rows()[0]).animate.set_color(BLACK),FadeOut(I[0],J[1]))
    
        C = [[1, 1, 1, 35], [0, -1, -2, -30], [0, -1, -3, -35]]
        F = Matrix(C,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).move_to(4*RIGHT).scale(0.6)

        with self.voiceover(text='''This is our updated matrix after the first iteration of i loop.
                            ''') as tracker:
            self.play(Transform(E,F),run_time=0.001)
            self.play(FadeOut(E),FadeIn(F))
        self.wait()
        
        with self.voiceover(text='''In the second loop, the value of i will be equal to 1 
        which refers to the first row of the matrix.
        ''') as tracker:
            self.play(F[0].animate.set_color(BLACK))
            self.play(Write(loop2),Write(iloop2),Write(I[1]),(F.get_rows()[1]).animate.set_color(WHITE)) 
        
        with self.voiceover(text='''The value of j will be equal to 2, as the for loop ranges from i+1 which is 2 to len E which is 3. 
So, the j loop will run only once. Here, j = 2 refers to the third row of the matrix.
        ''') as tracker:
            self.play(Transform(Cb[0],Cb[2]))
            self.play(Write(jloop2))
            self.wait(8)  
            self.play((F.get_rows()[2]).animate.set_color(WHITE), Write(J[1]))
        self.wait()

        mult = Text("mult", weight=BOLD, font_size=24, color=ORANGE).move_to(3*UP).shift(1.5*RIGHT)
        eq1 = Text(" = ",font_size=24).next_to(mult,RIGHT)
        l1 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq1,RIGHT)
        e1 = Text("E[j][i]", font_size=24).next_to(l1,UP)
        e2 = Text("E[i][i]", font_size=24).next_to(l1,DOWN)
        e3 = Text("E[2][1]", font_size=24).next_to(l1,UP)
        e4 = Text("E[1][1]", font_size=24).next_to(l1,DOWN)
        eq2 = Text(" = ",font_size=24).next_to(l1,RIGHT)
        l2 = Line(start=[-0.5,0,0],end=[0.5,0,0]).next_to(eq2,RIGHT)
        eq3 = Text(" = ",font_size=24).next_to(l2,RIGHT)

        for i in range(1,2):
            with self.voiceover(text='''Now, we will calculate the multiplier constant....
So, E-j-i which is E two one equal to -1..............and E-i-i which is E one one equalto -1.............On dividing, the multiplier constant = 1.
''') as tracker:
                self.play(Transform(Cb[0], Cb[3])) 
                self.play(Write(mult),Write(eq1),Create(l1))
                r = VGroup(F[0][i+col_len],F[0][i+2*col_len])
                rec = SurroundingRectangle(r)
                a1 = F[0][i+2*col_len].copy()
                a2 = F[0][i+col_len].copy()
                self.play(Write(e1), Write(e2),Create(rec),Write(eq2),Create(l2))
                self.play(Create(ri2),Create(rj1))
                self.play(Transform(e1,e3))
                self.play(a1.animate.move_to(l2).shift(UP*0.3))
                self.play(FadeOut(ri2,rj1))
                self.play(Create(ri1),Create(rj1))
                self.play(Transform(e2,e4))
                self.play(a2.animate.move_to(l2).shift(DOWN*0.3))
                self.play(FadeOut(ri1,rj1))
                m = int(C[2][i]/C[1][i])
                mut = Text(str(m),font_size=22,font="Times New Roman")
                self.play(Write(eq3),Write(mut.next_to(eq3,RIGHT)))
                self.play(FadeOut(a1,l1,e1,e2,l2,a2,eq2,eq3,rec),run_time=0.5)
                self.play(mut.animate.move_to(eq1).shift(0.5*RIGHT))
                grp5 = Group(mult,eq1,mut)
                self.play(grp5.animate.shift(2*RIGHT))
            
        eq2 = Text(" = ",font_size=24)
        eq3 = Text(" = ",font_size=24)
        eq4 = Text(" = ",font_size=24)
        sub = Text(" - ",color=BLUE)
        ast = Text(" * ",color=BLUE, font_size=24)
        b1 = Text(" ( ",font_size=24)
        b2 = Text(" ) ",font_size=24)

        B = [[1,1,1,35],[0,-1,-2,-30],[0,-1,-3,-35]]

        with self.voiceover(text='''
The k loop will perform operations on the third row. Remember that the value of k will range from i to len E-i. 
As, i = 1, so the value of k will range from 1 to 3.''') as tracker:
            self.play(Transform(Cb[0], Cb[4]))
            self.wait(9)
            self.play(Write(kloop2))
        
        arr = []

        with self.voiceover(text='''
At first k = 1. So, we will multiply E-i-k which is E one one by the multiplier constant and subtract it from E-j-k which is E two one. On solving, the second element of the third row gets eliminated......................
these.........same operations will be repeated.............on the remaining elements.................
''') as tracker:
            for k in range(1,col_len):
                a3 = F[0][2*col_len+k].copy()
                a4 = F[0][k+col_len].copy()
                mut2 = mut.copy()
                r = VGroup(a3, a4)
                rec = SurroundingRectangle(r)
        
                if k == 3:
                    with self.voiceover(text="At the end, every element of the third row gets updated.") as tracker:
                        self.play(Create(rec),Write(K.next_to(rec,2*DOWN)),run_time=0.5)
                        self.play(Transform(Cb[0], Cb[5]))
                        strg = Text("E["+str(2)+"]["+str(k)+"]",font_size=24,color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                        self.play(Create(ri1),Create(rj3))
                        self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                        self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)),run_time=0.5)
                        grp8 = Group(a4,ast,mut2)
                        self.play(FadeOut(ri1,rj3),grp8.animate.shift(1*RIGHT),run_time=0.5)
                        self.play(Create(ri2),Create(rj3),Write(strg),Write(eq3.next_to(strg,RIGHT)))
                        self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                        self.play(Write(sub.next_to(a3,0.6*RIGHT)),Write(b1.next_to(sub,0.6*RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)),run_time=0.5)
                        ans = (B[2][k] - (B[1][k]*m))
                        answer = Text(str(ans),font_size=22,font="Times New Roman").next_to(strg,5*RIGHT)
                    with self.voiceover(text='''
With it, the j loop comes to an end..........
                                        ''') as tracker:
                        grop = Group(a4,b1,b2,ast,mut2)
                        self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                        self.play(FadeOut(ri2,rj3,rec,K),run_time=0.5)
                        fin = answer.copy().move_to(F[0][2*col_len+k])
                        fin1 = answer.copy()
                        arr.append(fin1)
                        self.play(AnimationGroup(*[fin1.animate.move_to(F[0][2*col_len+k]),AnimationGroup(*[FadeOut(F[0][2*col_len+k])],run_time=0.5)],lag_ratio=0.6))
                        self.play(FadeOut(answer,eq3,strg,mult,eq1,mut,loop2,iloop2,jloop2,kloop2),run_time=0.5)
                        self.play(Transform(Cb[0], Cb[1]))
                        mut.clear_updaters()
                        self.play(FadeOut(I[1],J[1]))
                else:
                    self.play(Create(rec),Write(K.next_to(rec,2*DOWN)))
                    self.play(Transform(Cb[0], Cb[5]))
                    strg = Text("E["+str(2)+"]["+str(k)+"]",font_size=24,color=TEAL_B).next_to(mult,2*DOWN+2*LEFT)
                    rj = SurroundingRectangle(ind_j[k])
                    self.play(Create(ri1),Create(rj))
                    if k==1:
                        self.wait()
                    self.play(a4.animate.set_color(YELLOW).move_to(mult).shift(0.75*DOWN))
                    self.play(Write(ast.next_to(a4,RIGHT)),Write(mut2.next_to(ast,RIGHT)),run_time=0.5)
                    grp7 = Group(a4,ast,mut2)
                    self.play(FadeOut(ri1,rj),grp7.animate.shift(1*RIGHT))
                    self.play(Create(ri2),Create(rj),Write(strg),Write(eq3.next_to(strg,RIGHT)))
                    self.play(a3.animate.set_color(YELLOW).move_to(eq3).shift(0.5*RIGHT))
                    self.play(Write(sub.next_to(a3,RIGHT)),Write(b1.next_to(sub,0.8*RIGHT)),Write(b2.next_to(mut2,0.3*RIGHT)),run_time=0.5)
                    ans = (B[2][k] - (B[1][k]*m))
                    answer = Text(str(ans),font_size=22,font="Times New Roman").next_to(strg,5*RIGHT)
                    if k==1:
                        self.wait(2)
                    grop = Group(a4,b1,b2,ast,mut2)
                    self.play(AnimationGroup(*[FadeOut(a3),FadeOut(grop, shift=0.25*LEFT),FadeTransform(sub,answer)]))
                    self.play(FadeOut(ri2,rj,rec,K),run_time=0.5)
                    fin = answer.copy().move_to(F[0][2*col_len+k])
                    fin1 = answer.copy()
                    arr.append(fin1)
                    self.play(AnimationGroup(*[fin1.animate.move_to(F[0][2*col_len+k]),AnimationGroup(*[FadeOut(F[0][2*col_len+k])],run_time=0.5)],lag_ratio=0.6))
                    self.play(FadeOut(strg, eq3, answer),run_time=0.5)
                    self.play(Transform(Cb[0], Cb[4]))
                r.clear_updaters()

        self.play(FadeOut(arr[0],arr[1],arr[2]),(F.get_rows()[1]).animate.set_color(BLACK),(F[0][8]).animate.set_color(BLACK))

        A = [[1, 1, 1, 35], [0, -1, -2, -30], [0, 0, -1, -5]]
        E = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).move_to(4*RIGHT).scale(0.6)

        with self.voiceover(text='''This is our updated matrix after second iteration of i loop.
                       ''') as tracker:
            self.play(Transform(F,E),run_time=0.001)
            self.play(FadeOut(F),FadeIn(E))
        self.wait()

        self.play(E[0].animate.set_color(BLACK))

        with self.voiceover(text='''
In the third loop, the value of i will be equal to 2 which represents the third row of the matrix.
                            ''') as tracker:
            self.play(Write(loop3))
            self.wait()
            self.play((E.get_rows()[2]).animate.set_color(WHITE),Write(I[2]),Write(iloop3))
        self.wait()
        with self.voiceover(text='''
This time, the j loop will not function as the condition of the for loop gets violated. 
The for loop ranges from i+1 which is now equals to 3, to len E which is also 3.
Therefore, the loop will break and none of the operations will occur.  
                            ''') as tracker:
            self.play(Transform(Cb[0], Cb[2]))
            self.wait()
            self.play(Write(jloop3))
        
        self.play(FadeOut(Cb[0],I[2],loop3,iloop3,jloop3))
        self.play((E.get_rows()[2]).animate.set_color(BLACK))
        for i in range(len(ind_i)):
            self.play(FadeOut(ind_i[i]),run_time=0.1)
        for j in range(len(ind_j)):
            self.play(FadeOut(ind_j[j]),run_time=0.1)
        with self.voiceover(text='''
Hence, this updated matrix is our required output.
                            ''') as tracker:

            self.play(E[0].animate.set_color(WHITE))
            self.wait(2)

        x1 = Tex("\(x\)")
        y1 = Tex("\(y\)")
        z1 = Tex("\(z\)")
        x2 = Tex("\(x\)")
        y2 = Tex("\(y\)")
        z2 = Tex("\(z\)")
        x3 = Tex("\(x\)")
        y3 = Tex("\(y\)")
        z3 = Tex("\(z\)")
        
        object_height = 1.5
        
        no_apple1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple1.shift(1*UP + 2.5*LEFT)
        
        plus1 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        x1.next_to(no_apple1,buff = 0.1)
        plus1.next_to(x1)
        
        no_mango1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        plus2 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        no_mango1.next_to(plus1)
        y1.next_to(no_mango1,buff = 0.1)
        plus2.next_to(y1,buff = 0.25)
        no_park1 = Text('1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_park1.next_to(plus2)
        z1.next_to(no_park1,buff = 0.1)

        equal1 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal1.next_to(z1,buff = 0.25)
        
        ans1 = Text('35', color= RED_E,weight = BOLD).scale(object_height/2)
        ans1.next_to(equal1,buff = 0.4)
        
        no_apple2 = Text('0 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple2.shift(2.5*LEFT)
        
        plus3 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        x2.next_to(no_apple2,buff = 0.1)
        plus3.next_to(x2)
        no_mango2 = Text('-1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        plus4 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        no_mango2.next_to(plus3)
        y2.next_to(no_mango2,buff = 0.1)
        plus4.next_to(y2,buff = 0.25)

        no_park2 = Text('-2 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_park2.next_to(plus4)
        z2.next_to(no_park2,buff = 0.1)
        equal2 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal2.next_to(z2,buff = 0.25)
        
        ans2 = Text('30', color= RED_E,weight = BOLD).scale(object_height/2)
        ans2.next_to(equal2,buff = 0.4)
        
        no_apple3 = Text('0 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_apple3.shift(1*DOWN + 2.5*LEFT)
        
        plus5 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        x3.next_to(no_apple3,buff = 0.1)
        plus5.next_to(x3)
        
        no_mango3 = Text('0 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        
        plus6 = Text('+', color=WHITE,weight = BOLD).scale(object_height/2)
        
        no_mango3.next_to(plus5)
        y3.next_to(no_mango3,buff = 0.1)
        plus6.next_to(y3,buff = 0.25)
        
        no_park3 = Text('-1 *', t2c={'[2:]': WHITE},color= GREEN_C,weight = BOLD).scale(object_height/2)
        no_park3.next_to(plus6)
        z3.next_to(no_park3,buff = 0.1)

        equal3 = Text('=', color=WHITE,weight = BOLD).scale(object_height/2)
        equal3.next_to(z3,buff = 0.25)
        
        ans3 = Text('-5', color= RED_E,weight = BOLD).scale(object_height/2)
        ans3.next_to(equal3,buff = 0.4)

        self.play(FadeOut(cd,E))

        with self.voiceover(text='''
We can represent this matrix in the form of equations as shown here.......
we will pass on this matrix to the next function..........
To make things less confusing, let’s outline the steps we’ll be following next.
                            ''') as tracker:
            
            self.play(AnimationGroup(*[FadeIn(x1,shift = 0.25*RIGHT),FadeIn(no_apple1),
            FadeIn(plus1,shift = 0.25*RIGHT), FadeIn(y1,shift = 0.25*RIGHT), FadeIn(no_mango1),
                FadeIn(plus2,shift = 0.25*RIGHT),FadeIn(z1,shift = 0.25*RIGHT),FadeIn(no_park1),FadeIn(equal1,shift = 0.25*RIGHT),
                                FadeIn(ans1,shift = 0.25*RIGHT)]),run_time=0.5)
            self.play(AnimationGroup(*[FadeIn(x2,shift = 0.25*RIGHT),FadeIn(no_apple2),
                FadeIn(plus3,shift = 0.25*RIGHT), FadeIn(y2,shift = 0.25*RIGHT), FadeIn(no_mango2),
                 FadeIn(plus4,shift = 0.25*RIGHT),FadeIn(z2,shift = 0.25*RIGHT),FadeIn(no_park2),FadeIn(equal2,shift = 0.25*RIGHT),
                                FadeIn(ans2,shift = 0.25*RIGHT)]),run_time=0.5)
            self.play(AnimationGroup(*[FadeIn(x3,shift = 0.25*RIGHT),FadeIn(no_apple3),
                FadeIn(plus5,shift = 0.25*RIGHT), FadeIn(y3,shift = 0.25*RIGHT), FadeIn(no_mango3),
                 FadeIn(plus6,shift = 0.25*RIGHT),FadeIn(z3,shift = 0.25*RIGHT),FadeIn(no_park3),FadeIn(equal3,shift = 0.25*RIGHT),
                                FadeIn(ans3,shift = 0.25*RIGHT)]),run_time=0.5)
            
            vid = Group(no_apple1,x1,plus1,y1,no_mango1,plus2,no_park1,z1,equal1,ans1,no_apple2,x2,plus3,no_mango2,y2,plus4,no_park2,z2,equal2,ans2,no_apple3,x3,plus5,y3,no_mango3,plus6,no_park3,z3,equal3,ans3)
            self.wait(3)
            self.play(vid.animate.shift(3.5*LEFT).scale(0.8),FadeIn(E))

        self.play(FadeOut(E),vid.animate.shift(3.5*RIGHT).scale(1.3))

        with self.voiceover(text='''
        These are our equations in simplified form.
        ''') as tracker:

            self.play(FadeOut(no_apple3,x3,plus5,no_mango3,y3,plus6,no_apple2,plus3,x2))
            grop1 = Group(no_park3,z3,equal3,ans3)
            grop2 = Group(no_mango2,y2,plus4,no_park2,z2,equal2,ans2)
            self.play(grop2.animate.shift(1*LEFT),grop1.animate.shift(1.9*LEFT))

        with self.voiceover(text='''
        First, we will solve the last equation to find the value of variable z, which comes out to be 5.
        ''') as tracker:
            ans3_new = Text('5', color= RED_E,weight = BOLD).scale(object_height/2).next_to(equal3,buff = 0.4)
            self.wait(4)
            self.play(FadeOut(no_park3),FadeTransform(ans3,ans3_new))

        with self.voiceover(text='''
        Next, we’ll use this value of z to solve the second equation, giving us the value of y, which is 20.
        ''') as tracker:
            z2_new = Text('5', color= GREEN_C,weight = BOLD).scale(object_height/2).next_to(no_park2,buff = 0.1)
            self.wait()
            self.play(Transform(z2,z2_new))
            self.wait()
            sub3 = Text('-', color=WHITE,weight = BOLD).scale(object_height/2).next_to(y2,LEFT,buff = 0.25)
            sub4 = Text('-', color=WHITE,weight = BOLD).scale(object_height/2).next_to(y2,buff = 0.25)
            z_2 =  Text('10', color= GREEN_C,weight = BOLD).scale(object_height/2).next_to(sub4,buff = 0.25)
            grop2 = Group(equal2,ans2)
            self.play(FadeTransform(plus4,sub4),FadeTransform(no_mango2,sub3),FadeOut(no_park2,z2,z2_new),FadeIn(z_2),grop2.animate.shift(0.7*LEFT))
            self.wait()
            ans2_new = Text('20', color= RED_E,weight = BOLD).scale(object_height/2).next_to(equal2,buff = 0.4)
            grop3 = Group(equal2,ans2_new)
            self.play(FadeOut(sub3,sub4,z_2),FadeTransform(ans2,ans2_new))
            self.play(y2.animate.shift(0.8*RIGHT),grop3.animate.shift(0.3*LEFT))    

        with self.voiceover(text='''
        Finally, using both y and z, we’ll solve the first equation to find the value of x, which is 10.
        ''') as tracker:    
            y1_new = Text('20', color= GREEN_C,weight = BOLD).scale(object_height/2).next_to(no_mango1,buff = 0.1)
            z1_new = Text('5', color= GREEN_C,weight = BOLD).scale(object_height/2).next_to(no_park1,buff = 0.1)
            self.wait()
            self.play(Transform(y1,y1_new),plus2.animate.shift(0.1*RIGHT),Transform(z1,z1_new))
            self.wait()
            s1 = Text('25', color= GREEN_C,weight = BOLD).scale(object_height/2).next_to(plus1,buff = 0.25)
            self.play(FadeOut(no_apple1,no_mango1,plus2,no_park1,z1,y1),FadeIn(s1))
            grop4 = Group(x1,plus1,s1)
            grop5 = Group(equal1,ans1)
            self.play(grop4.animate.shift(0.4*RIGHT),grop5.animate.shift(1.65*LEFT))
            ans1_new = Text('10', color= RED_E,weight = BOLD).scale(object_height/2).next_to(equal1,buff = 0.4)
            self.play(FadeOut(plus1,s1),FadeTransform(ans1,ans1_new),x1.animate.shift(1.3*RIGHT))

        with self.voiceover(text='''Now let’s perform these steps in Python.
        ''') as tracker:
            self.wait(2)
            self.play(FadeOut(x1,y2,z3,equal1,equal2,equal3,ans1_new,ans2_new,ans3_new))
        

################################### PART - 2 Solve Eliminate Function #######################################

        bg = "window"
        row_len = 3
        col_len = 4

        code = '''
def solve_elimination(E):
    solution = [0 for _ in range(len(E))]
    i = len(E) - 1
    j = len(E[0]) - 2
    while i > -1:
        row = E[i]
        sum = 0
        for k in range(j+1, len(row) - 1):
            sum += row[k]*solution[k]
        solution[j] = (row[-1] - sum)/row[j]
        i -= 1
        j -= 1
    return solution'''
        cd = Code(code=code, line_spacing=0.7, tab_width=5, background=bg,language="Python")
        cb = [0 for _ in range(13)]
        cb[0] = always_redraw(lambda : SurroundingRectangle(cd[2][0],PINK,stroke_width=3,corner_radius=0.1,buff=0.03))
        solution = [0 for _ in range(row_len)]
        ind_i = [0 for _ in range(3)]
        ind_j = [0 for _ in range(4)]

        cb[1]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=4.5, height=0.25, color=PINK).move_to(2.96 *LEFT + 2.67*UP)
        cb[2]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=1.78, height=0.25, color=PINK).move_to(4.326*LEFT + 2.43*UP)
        cb[3]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=2.18, height=0.25, color=PINK).move_to(4.18  *LEFT + 2.16*UP)
        cb[4]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=1.6, height=0.23, color=PINK).move_to(4.42  *LEFT + 1.91*UP)
        cb[5]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=1.32, height=0.25, color=PINK).move_to(4  *LEFT + 1.65*UP)
        cb[6]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.4, width=0.93, height=0.25, color=PINK).move_to(4.17  *LEFT + 1.4*UP)
        cb[7]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=4.1,   height=0.26, color=PINK).move_to(2.57  *LEFT + 1.15*UP)
        cb[8]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=3.05, height=0.25, color=PINK).move_to(2.5  *LEFT + 0.9*UP)
        cb[9]  = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=4.42, height=0.26, color=PINK).move_to(2.4 *LEFT + 0.63*UP)
        cb[10] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=0.8, height=0.25, color=PINK).move_to(4.22 *LEFT + 0.38*UP)
        cb[11] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=0.8, height=0.25, color=PINK).move_to(4.23 *LEFT + 0.12 *UP)
        cb[12] = RoundedRectangle(corner_radius=0.1, stroke_width=2.5, width=1.88, height=0.24, color=PINK).move_to(4.26 *LEFT + 0.13*DOWN)
        
        A = [[1,1,1,35],[0,-1,-2,-30],[0,0,-1,-5]]
        E = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).move_to(4*RIGHT).scale(0.6)
        i = row_len - 1
        j = col_len - 2
        solution = [0 for _ in range(row_len)]
        F = Matrix([solution]).scale(0.6)
        sub = Text("-",color=BLUE,font_size=24)

        with self.voiceover(text='''This is the complete code for the Solve elimination function. 
                            Let's understand how it works.''') as tracker:
            self.play(Write(cd))
            self.play(Create(cb[0]))
            self.wait(2)
            self.play(cd.animate.shift(3.27*LEFT).scale(0.6))
        with self.voiceover(text="Here we will input the E matrix, which was returned by the eliminate function in previous code.") as tracker:
            self.play(Write(E),E[0].animate.set_color(BLACK),run_time=0.01)
            self.play(E[0].animate.set_color(WHITE))

        self.play(cd.animate.shift(1.5*UP))
        self.play(E.animate.move_to(cd).shift(3.5*DOWN+1*LEFT).scale(0.65))
        for a in range(3):
                ind_i[a] = Text(str(a),font_size=18,color = GREEN).next_to(E[0][a*col_len], 2.5*LEFT)
                self.play(Write(ind_i[a]),run_time=0.1)
        for b in range(4):
                ind_j[b] = Text(str(b),font_size=18,color = GREEN).next_to(E[0][2*col_len+b],2*DOWN)
                self.play(Write(ind_j[b]),run_time=0.1)

        g1 = Group(E[0][8],E[0][9],E[0][10],E[0][11])
        g2 = Group(E[0][4],E[0][5],E[0][6],E[0][7])
        g3 = Group(E[0][0],E[0][1],E[0][2],E[0][3])
        rec1 = SurroundingRectangle(g1, corner_radius=0.1, color=TEAL_B)
        rec2 = SurroundingRectangle(g2, corner_radius=0.1, color=TEAL_B)
        rec3 = SurroundingRectangle(g3, corner_radius=0.1, color=TEAL_B)

        I = Text("i",weight = BOLD,font_size=24,color=RED).next_to(E,4*RIGHT).shift(UP)
        eq1 = Text(" = ",font_size=24).next_to(I,RIGHT)
        J = Text("j",weight = BOLD,font_size=24,color=RED).next_to(I,2*DOWN)
        eq2 = Text(" = ",font_size=24).next_to(J,RIGHT)
        K = Text("k",weight = BOLD,font_size=24,color=RED).next_to(J,2*DOWN)
        eq3 = Text(" = ",font_size=24).next_to(K,RIGHT)
        S = Text("solution", font_size=24,color=YELLOW).next_to(cd,2*RIGHT)
        eq5 = Text(" = ",font_size=24)
        sm1 = Text("sum",font_size=24,color=MAROON).next_to(cd,2*RIGHT).shift(2*RIGHT+0.5*UP)
        eq4 = Text(" = ",font_size=24).next_to(sm1,RIGHT)
        
        cb[0].clear_updaters()

        with self.voiceover(text='''First, we create a zero array to store the value of the variables x, y and z. Its length will be equal to the number of variables, which is 3. 
                            But, why zero? You will get the answer later in the video''') as tracker:
            self.play(Transform(cb[0],cb[1]))
            self.play(Write(S.shift(RIGHT+1.5*UP)),Write(eq5.next_to(S,RIGHT)))
            self.play(Write(F.next_to(eq5,RIGHT)))
        self.wait()
        i1 = Text(str(i+1),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
        sub1 = Text(" - ",color=BLUE,font_size=24).next_to(i1,RIGHT)
        i2 = Text(str(1),font_size=22,font="Times New Roman").next_to(sub1,RIGHT)
        i3 = Text(str(i),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
        j1 = Text(str(j+2),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
        sub2 = Text(" - ",color=BLUE,font_size=22).next_to(j1,RIGHT)
        j2 = Text(str(2),font_size=22,font="Times New Roman").next_to(sub2,RIGHT)
        j3 = Text(str(j),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
        reci0 = SurroundingRectangle(ind_i[0],color=YELLOW)
        reci1 = SurroundingRectangle(ind_i[1],color=YELLOW)
        reci2 = SurroundingRectangle(ind_i[2],color=YELLOW)
        recj0 = SurroundingRectangle(ind_j[0],color=YELLOW)
        recj1 = SurroundingRectangle(ind_j[1],color=YELLOW)
        recj2 = SurroundingRectangle(ind_j[2],color=YELLOW)
        recj3 = SurroundingRectangle(ind_j[3],color=YELLOW)
        sm2 = Text("sum",color=ORANGE,font_size=24).next_to(cd,2*RIGHT).shift(RIGHT+DOWN)
        eq7 = Text(" = ",font_size=24).next_to(sm2,RIGHT)
        sm3 = Text("sum",color=ORANGE,font_size=24).next_to(eq7,RIGHT)
        sol0 = SurroundingRectangle(F[0][0],corner_radius=0.1,color = BLUE)
        sol1 = SurroundingRectangle(F[0][1],corner_radius=0.1,color = BLUE)
        sol2 = SurroundingRectangle(F[0][2],corner_radius=0.1,color = BLUE)
        with self.voiceover(text='''Following the bottom-to-top approach, 
        we start with the last row and move upward through the matrix. 
        The variable i is used to iterate over the matrix row by row. Initially, i = 2, which refers to the index of the last row.
        ''') as tracker:
            self.play(Transform(cb[0],cb[2]))
            self.wait(4)
            self.play(AnimationGroup(*[Write(I),Write(eq1)],lag_ratio=0.5))
            self.play(AnimationGroup(*[Write(i1),Write(sub1),Write(i2)],lag_ratio=0.5))
            self.wait()
            self.play(AnimationGroup(*[FadeOut(sub1,shift=0.25*LEFT),FadeOut(i2,shift=0.5*LEFT),FadeTransform(i1,i3)]))
            self.play(Create(reci2))
        self.play(FadeOut(reci2))
        self.wait()
        with self.voiceover(text='''The value of variable j is equal to 2. It stores the index of the second-to-last column in the matrix. 
        This is because, in the last row, only the coefficient in the second-to-last column is non-zero. 
        J will help us to perform necessary computations. ''') as tracker:
            self.play(Transform(cb[0],cb[3]))
            self.play(AnimationGroup(*[Write(J),Write(eq2)]))
            self.play(AnimationGroup(*[Write(j1),Write(sub2),Write(j2)],lag_ratio=0.2))
            self.play(AnimationGroup(*[FadeOut(sub2,shift=0.25*LEFT),FadeOut(j2,shift=0.5*LEFT),FadeTransform(j1,j3)]))
            self.play(Create(recj2))
            self.wait(4)
            self.play(FadeOut(recj2))
        with self.voiceover(text="We use the condition of i greater than -1 in the while loop to ensure that i includes 0 index and does not become negative") as tracker:
            self.play(Transform(cb[0],cb[4]))

        while i > -1:
            sum = 0
            if i==2:
                with self.voiceover(text='''Now we extract the last row from the matrix and store it in a variable named row.
The sum adds up the parts of the equation which involve variables we’ve already solved.
You will understand more about this in the next iteration.
 ''') as tracker:
                    self.play(Transform(cb[0],cb[5]))
                    self.play(Create(rec1))
                    R = Text("row",font_size=24,color=GREEN).next_to(E,RIGHT).shift(4*RIGHT)
                    e = Text(" = ",font_size=24).next_to(R,RIGHT)
                    r = Matrix([A[i]]).scale(0.6)
                    self.play(Write(R),Write(e))
                    self.play(Write(r.next_to(e,RIGHT)))
                    self.play(Transform(cb[0],cb[6]))
                    self.play(Write(sm1),Write(eq4))
                    s1 = Text(str(sum),font_size=24).next_to(eq4,RIGHT)
                    self.play(Write(s1))

                k = j+1
                with self.voiceover(text='''The value of k ranges from j+1 to length of row - 1. 
                Here, j+1 = 3 and len(row) - 1 is also equal to 3. 
                Therefore, the condition gets violated and the k loop will not be iterated.
''') as tracker:
                    self.play(Transform(cb[0],cb[7]))
                    self.wait(3)
                    self.play(Write(K),Write(eq3))
                    K_1 = Text("3 < 3",font_size=22).next_to(eq3,RIGHT)
                    self.play(Write(K_1))
                self.play(FadeOut(K_1,eq3,K))
                ans = int((int(A[i][-1]) - sum) / int(A[i][j]))
                solution[j] = ans
                answer = Text(str(ans),font_size=22,font="Times New Roman")
                x = Text("solution["+str(j)+"]",color=ORANGE,font_size=24).next_to(cd,2*RIGHT).shift(RIGHT+DOWN)
                eq6 = Text(" = ",font_size=24).next_to(x,RIGHT)
                l = Line(start=[-1,0,0],end=[1,0,0]).next_to(eq6,RIGHT)
                rowjrec = SurroundingRectangle(r[0][2],corner_radius=0.1,color=PINK)
                rowm1 = SurroundingRectangle(r[0][3],corner_radius=0.1,color=PINK)

                with self.voiceover(text=''' To calculate the values of the variables x, y, and z, we subtract the sum variable from row[-1] and then divide it by row[j].
Here, row[-1] refers to the last element in the row, which represents the constant term of the equation. 
row[j] refers to the coefficient at index j in the row.
''') as tracker:
                    self.play(Transform(cb[0],cb[9]))
                    self.wait(2)
                    self.play(Write(x),Write(eq6))
                    l1 = Line(start=[-1,0,0],end=[1.2,0,0]).next_to(eq6,RIGHT)
                    f1 = Text("row[-1]",color=YELLOW,font_size=24).next_to(l1,UP).shift(0.6*LEFT)
                    sub0 = Text("-",color=BLUE,font_size=24).next_to(f1,RIGHT)
                    f2 = Text("sum",color=YELLOW,font_size=24).next_to(sub0,RIGHT)
                    f3 = Text("row[j]",color=YELLOW,font_size=24).next_to(l1,DOWN)
                    self.play(Create(l1))
                    a1 = r[0][-1].copy().move_to(f1)
                    a1copy = r[0][-1].copy()
                    a2 = s1.copy().move_to(f2)
                    a2copy = s1.copy()
                    a3 = r[0][j].copy().move_to(f3)
                    a3copy = r[0][j].copy()
                    br3 = Text(" (",font_size=24)
                    br4 = Text(") ",font_size=24)
                    self.play(Write(f1),Write(sub0),Write(f2))
                    self.play(Write(f3))
                    self.wait(2)
                    self.play(Create(rowm1))
                    self.wait(4)
                    self.play(Create(rowjrec))

                with self.voiceover(text='''Therefore, we subtract the sum variable from row[-1] and then divide it by row[2] to calculate the value. 
                    Thus, solution[2] comes out to be 5. Hence, the value of variable z = 5.
                    ''') as tracker:
                    self.play(Create(sol2))
                    self.play(AnimationGroup(*[a2copy.animate.move_to(f2),FadeOut(f2)],lag_ratio=0.1))
                    self.play(AnimationGroup(*[a1copy.animate.move_to(f1),FadeOut(f1)],lag_ratio=0.1))
                    self.play(AnimationGroup(*[a3copy.animate.move_to(f3),FadeOut(f3)],lag_ratio=0.1))
                    self.play(Write(br3.next_to(sub0,RIGHT)),run_time=0.3)
                    self.play(Write(br4.next_to(f2,0.02*RIGHT)),run_time=0.3)
                    self.wait(2)
                    self.play(AnimationGroup(*[FadeOut(a1copy,br3,a2copy,br4,a3copy,sub0,l1,sol2,rowjrec,rowm1),Write(answer.next_to(eq6,RIGHT))],lag_ratio=0.5))
                    fin = answer.copy().move_to(F[0][j])
                    fin1 = answer.copy()
                    self.play(AnimationGroup(*[fin1.animate.move_to(F[0][j]),AnimationGroup(*[FadeOut(F[0][j])],run_time=0.5)],lag_ratio=0.6))
                    F[0][j] = fin1
                
                self.play(FadeOut(i3,j3,I,eq1,J,eq2,s1,eq4,sm1,R,e,r,rec1,x,eq6,answer))

                with self.voiceover(text=''' we will reduce the value of i by 1 to consider the second row this time.
                               So, i becomes 1''') as tracker:
                    i -= 1
                    self.play(Transform(cb[0],cb[10]))
                    i1 = Text(str(i+1),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
                    sub1 = Text(" - ",color=BLUE,font_size=24).next_to(i1,RIGHT)
                    i2 = Text(str(1),font_size=22,font="Times New Roman").next_to(sub1,RIGHT)
                    i3 = Text(str(i),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
                    self.play(AnimationGroup(*[Write(I),Write(eq1)]))
                    self.play(AnimationGroup(*[Write(i1),Write(sub1),Write(i2)],lag_ratio=0.3))
                    self.wait()
                    self.play(AnimationGroup(*[FadeOut(sub1,shift=0.25*LEFT),FadeOut(i2,shift=0.5*LEFT),FadeTransform(i1,i3)]))
                    self.play(Create(reci1))
                self.play(FadeOut(reci1))
                with self.voiceover(text='''We also reduce the value of j by 1. So, j becomes 1''') as tracker:
                    self.play(Transform(cb[0],cb[11]))
                    j -= 1
                    j1 = Text(str(j+1),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
                    sub2 = Text(" - ",color=BLUE,font_size=24).next_to(j1,RIGHT)
                    j2 = Text(str(1),font_size=22,font="Times New Roman").next_to(sub2,RIGHT)
                    j3 = Text(str(j),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
                    self.play(AnimationGroup(*[Write(J),Write(eq2)]))
                    self.play(AnimationGroup(*[Write(j1),Write(sub2),Write(j2)],lag_ratio=0.05))
                    self.play(AnimationGroup(*[FadeOut(sub2,shift=0.25*LEFT),FadeOut(j2,shift=0.5*LEFT),FadeTransform(j1,j3)]))
                    self.play(Create(recj1))
                self.play(FadeOut(recj1))
            
            if i==1:
                sum = 0
                with self.voiceover(text="Now the row variable contains the second row.") as tracker:
                    self.play(Transform(cb[0],cb[5]))
                    self.play(Create(rec2))
                    R = Text("row",font_size=24,color=GREEN).next_to(E,RIGHT).shift(4*RIGHT)
                    e = Text(" = ", font_size=24).next_to(R,RIGHT)
                    r = Matrix([A[i]]).scale(0.6)
                    self.play(Write(R),Write(e))
                    self.play(Write(r.next_to(e,RIGHT)))

                with self.voiceover(text="We initialize the sum to 0.") as tracker:
                    self.play(Transform(cb[0],cb[6]))
                    self.play(Write(sm1),Write(eq4))
                    s1 = Text(str(sum),font_size=22,font="Times New Roman").next_to(eq4,RIGHT)
                    self.play(Write(s1))
                k = j+1
                
                for k in range (j+1, col_len-1): 
                    with self.voiceover(text="This time k ranges from 2 to 3. So, this loop will run only once, and the value of k will be 2.") as tracker:
                        self.play(Transform(cb[0],cb[7]),Write(K),Write(eq3))
                        K_1 = Text((str(k)+" < 3"),font_size=22,font="Times New Roman").next_to(eq3,RIGHT)
                        self.play(Write(K_1))
                    with self.voiceover(text='''This formula is used to update the value of sum. 
                                        It helps add up the parts of the equation that involve variables we’ve already solved.
                                        ''') as tracker:
                        self.play(Transform(cb[0],cb[8]))
                        add = Text("+", color=BLUE,font_size=24).next_to(sm3,0.5*RIGHT)
                        br1 = Text("(",font_size=24).next_to(add,0.5*RIGHT)
                        rk = Text("row[k]",color=ORANGE,font_size=24).next_to(br1,0.5*RIGHT)
                        ast = Text("*",color=BLUE,font_size=24).next_to(rk,0.5*RIGHT)
                        sk = Text("solution[k]",color=ORANGE,font_size=24).next_to(ast,0.5*RIGHT)
                        br2 = Text(")",font_size=24).next_to(sk,0.5*RIGHT)
                        self.play(Write(sm2),Write(eq7),Write(sm3),Write(add),Write(br1),Write(rk),Write(ast),Write(sk),Write(br2))
                    with self.voiceover(text='''As, we have already solved the variable z in the last iteration. 
                                        So here, we multiply row[2] by the solution[2] and add the value to sum.
                                        ''') as tracker:    
                        sum_1 = s1.copy().move_to(sm3)
                        sum1copy = s1.copy()
                        A1 = r[0][k].copy().move_to(rk)
                        A1copy = r[0][k].copy()
                        A2 = F[0][k].copy().move_to(sk)
                        A2copy = F[0][k].copy()
                        self.play(AnimationGroup(*[sum1copy.animate.move_to(sm3),FadeOut(sm3)],lag_ratio=0.1))
                        self.wait(3)
                        self.play(AnimationGroup(*[A1copy.animate.move_to(rk),FadeOut(rk)],lag_ratio=0.1))
                        self.play(AnimationGroup(*[A2copy.animate.move_to(sk),FadeOut(sk)],lag_ratio=0.1))
                        sum += int(A[i][k])*solution[k]
                        self.wait()
                        sum1 = Text(str(sum),font_size=24).next_to(eq7,RIGHT)
                        gpr = Group(add,br1,sum1copy,A1copy,ast,A2copy,br2)
                        self.play(AnimationGroup(*[FadeOut(gpr,shift=0.25*LEFT),FadeTransform(sum_1,sum1)]))
                        s2 = sum1.copy().move_to(s1)
                        self.play(Transform(s1,s2))
                self.play(FadeOut(K_1,eq3,K,sm2,eq7,sum1,s2))
                       
                ans = int((int(A[i][-1]) - sum) / int(A[i][j]))
                solution[j] = ans
                answer = Text(str(ans),font_size=22,font="Times New Roman")
                x = Text("solution["+str(j)+"]",color=ORANGE,font_size=22,font="Times New Roman").next_to(cd,2*RIGHT).shift(RIGHT+DOWN)
                eq6 = Text(" = ",font_size=24).next_to(x,RIGHT)
                l = Line(start=[-1,0,0],end=[1,0,0]).next_to(eq6,RIGHT)
                rowjrec = SurroundingRectangle(r[0][j],corner_radius=0.1,color=PINK)
                rowm1 = SurroundingRectangle(r[0][3],corner_radius=0.1,color=PINK)

                with self.voiceover(text='''
To calculate the variables, we subtract the sum value from row[-1] and then divide it by row[1]. Thus, solution[1] comes out to be 20. 
Hence, the value of y = 20.
                                    ''') as tracker:
                    self.play(Transform(cb[0],cb[9]),Write(x),Write(eq6),Create(sol1),Create(l))
                    a1 = r[0][-1].copy()
                    a2 = s1.copy()
                    a3 = r[0][j].copy()
                    br3 = Text("(",font_size=24)
                    br4 = Text(")",font_size=24)
                    self.play(a2.animate.move_to(l).shift(UP*0.3+0.5*RIGHT),Create(rowm1))
                    self.play(a1.animate.move_to(l).shift(UP*0.3+0.7*LEFT))
                    self.play(Write(sub.next_to(a1,RIGHT)),Create(rowjrec))
                    self.play(a3.animate.move_to(l).shift(DOWN*0.3),Write(br3.next_to(sub,RIGHT)),Write(br4.next_to(a2,0.5*RIGHT)))
                    self.wait()
                    self.play(AnimationGroup(*[FadeOut(a1,br3,a2,br4,a3,sub,l,sol1,rowjrec,rowm1),Write(answer.next_to(eq6,RIGHT))],lag_ratio=0.5))
                    fin = answer.copy().move_to(F[0][j])
                    fin1 = answer.copy()
                    self.play(AnimationGroup(*[fin1.animate.move_to(F[0][j]),AnimationGroup(*[FadeOut(F[0][j])],run_time=0.5)],lag_ratio=0.6))
                    F[0][j] = fin1

                self.play(FadeOut(i3,j3,I,eq1,J,eq2,s1,eq4,sm1,R,e,r,rec2,x,eq6,answer))
                with self.voiceover(text=''' we will again reduce the value of i by 1 to consider the first row.
                               So, i becomes 0''') as tracker:
                    i -= 1
                    self.play(Transform(cb[0],cb[10]))
                    i1 = Text(str(i+1),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
                    sub1 = Text(" - ",color=BLUE,font_size=24).next_to(i1,RIGHT)
                    i2 = Text(str(1),font_size=22,font="Times New Roman").next_to(sub1,RIGHT)
                    i3 = Text(str(i),font_size=22,font="Times New Roman").next_to(eq1,RIGHT)
                    self.play(AnimationGroup(*[Write(I),Write(eq1)]))
                    self.play(AnimationGroup(*[Write(i1),Write(sub1),Write(i2)],lag_ratio=0.3))
                    self.wait()
                    self.play(AnimationGroup(*[FadeOut(sub1,shift=0.25*LEFT),FadeOut(i2,shift=0.5*LEFT),FadeTransform(i1,i3)]))
                    self.play(Create(reci0))
                self.play(FadeOut(reci0))
                with self.voiceover(text='''We will also reduce the value of j by 1. So, j becomes 0''') as tracker:
                    self.play(Transform(cb[0],cb[11]))
                    j -= 1
                    j1 = Text(str(j+1),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
                    sub2 = Text(" - ",color=BLUE,font_size=24).next_to(j1,RIGHT)
                    j2 = Text(str(1),font_size=22,font="Times New Roman").next_to(sub2,RIGHT)
                    j3 = Text(str(j),font_size=22,font="Times New Roman").next_to(eq2,RIGHT)
                    self.play(AnimationGroup(*[Write(J),Write(eq2)]))
                    self.play(AnimationGroup(*[Write(j1),Write(sub2),Write(j2)],lag_ratio=0.05))
                    self.play(AnimationGroup(*[FadeOut(sub2,shift=0.25*LEFT),FadeOut(j2,shift=0.5*LEFT),FadeTransform(j1,j3)]))
                    self.play(Create(recj0))
                self.play(FadeOut(recj0))
            
            if i==0:
                sum = 0
                with self.voiceover(text="Now the row variable will store the first row.") as tracker:
                    self.play(Transform(cb[0],cb[5]))
                    self.play(Create(rec3))
                    R = Text("row",font_size=24,color=GREEN).next_to(E,RIGHT).shift(4*RIGHT)
                    e = Text(" = ", font_size=24).next_to(R,RIGHT)
                    r = Matrix([A[i]]).scale(0.6)
                    self.play(Write(R),Write(e))
                    self.play(Write(r.next_to(e,RIGHT)))

                with self.voiceover(text="We again initialize the sum to 0.") as tracker:
                    self.play(Transform(cb[0],cb[6]))
                    self.play(Write(sm1),Write(eq4))
                    s1 = Text(str(sum),font_size=24).next_to(eq4,RIGHT)
                    self.play(Write(s1))
                k = j+1

                for k in range (j+1, col_len-2): 
                    with self.voiceover(text='''This time, k ranges from 1 to 3, so the loop will run twice. This means we will calculate the sum twice.
In the first iteration, the value of k is 1.''') as tracker:
                        self.play(Transform(cb[0],cb[7]),Write(K),Write(eq3))
                        K_1 = Text((str(k)+" < 3"),font_size=22,font="Times New Roman").next_to(eq3,RIGHT)
                        self.play(Write(K_1))
                    with self.voiceover(text='''As, we have already solved the variable y in the last iteration. 
                                        So here, we multiply row[1] by the solution[1] and add the value to sum.
                                        ''') as tracker:
                        self.play(Transform(cb[0],cb[8]))
                        self.play(Write(sm2),Write(eq7))
                        sum_1 = s1.copy()
                        self.play(sum_1.animate.move_to(eq7).shift(0.4*RIGHT))
                        add = Text(" + ", color=BLUE,font_size=24).next_to(sum_1,RIGHT)
                        br1 = Text(" ( ",font_size=24).next_to(add,RIGHT)
                        A1 = r[0][k].copy()
                        ast = Text(" * ",color=BLUE,font_size=24).next_to(br1).shift(0.5*RIGHT)
                        A2 = F[0][k].copy()
                        br2 = Text(") ",font_size=24).next_to(ast).shift(0.4*RIGHT)
                        self.wait()
                        self.play(Write(add),Write(br1),A1.animate.move_to(br1).shift(0.4*RIGHT))
                        self.play(Write(ast),A2.animate.move_to(ast).shift(0.4*RIGHT))
                        self.play(Write(br2))
                        sum += int(A[i][k])*solution[k]
                        self.wait(1)
                        gpr = Group(add,br1,A1,ast,A2,br2)
                        sum1 = Text(str(sum),font_size=22,font="Times New Roman").next_to(eq7,RIGHT)
                        self.play(AnimationGroup(*[FadeOut(gpr, shift=0.25*LEFT),FadeTransform(sum_1,sum1)]))
                        s2 = sum1.copy().move_to(s1)
                        self.play(Transform(s1,s2))
                        self.play(FadeOut(K_1,eq3,K,sm2,eq7,sum1,s2))
                for k in range (j+2, col_len-1): 
                    with self.voiceover(text='''In the second iteration, the value of k = 2.''') as tracker:
                        self.play(Transform(cb[0],cb[7]))
                        self.play(Write(K),Write(eq3)) 
                        K_1 = Text((str(k)+" < 3"),font_size=22,font="Times New Roman").next_to(eq3,RIGHT)
                        self.play(Write(K_1))
                    with self.voiceover(text='''We take the previous value of sum, and update it by adding the product of row[2] and solution[2]. 
                                        This gives us the required value of sum.''') as tracker:
                        self.play(Transform(cb[0],cb[8]))
                        self.play(Write(sm2),Write(eq7))
                        sum_1 = s1.copy()
                        self.play(sum_1.animate.move_to(eq7).shift(0.4*RIGHT))
                        add = Text(" + ", color=BLUE,font_size=24).next_to(sum_1,RIGHT)
                        br1 = Text(" ( ",font_size=24).next_to(add,RIGHT)
                        A1 = r[0][k].copy()
                        ast = Text(" * ",color=BLUE,font_size=24).next_to(br1).shift(0.5*RIGHT)
                        A2 = F[0][k].copy()
                        br2 = Text(") ",font_size=24).next_to(ast).shift(0.4*RIGHT)
                        self.play(Write(add),Write(br1),A1.animate.move_to(br1).shift(0.4*RIGHT))
                        self.play(Write(ast),A2.animate.move_to(ast).shift(0.4*RIGHT))
                        self.play(Write(br2))
                        sum += int(A[i][k])*solution[k]
                        gpr = Group(add,br1,A1,ast,A2,br2)
                        sum1 = Text(str(sum),font_size=22,font="Times New Roman").next_to(eq7,RIGHT)
                        self.play(AnimationGroup(*[FadeOut(gpr, shift=0.25*LEFT),FadeTransform(sum_1,sum1)]))
                        s2 = sum1.copy().move_to(s1)
                        self.play(Transform(s1,s2))
                self.play(FadeOut(K_1,eq3,K,sm2,eq7,sum1,s2))

                ans = int((int(A[i][-1]) - sum) / int(A[i][j]))
                solution[j] = ans
                answer = Text(str(ans),font_size=22,font="Times New Roman")
                x = Text("solution["+str(j)+"]",color=ORANGE,font_size=24).next_to(cd,2*RIGHT).shift(RIGHT+DOWN)
                eq6 = Text(" = ",font_size=24).next_to(x,RIGHT)
                l = Line(start=[-1,0,0],end=[1,0,0]).next_to(eq6,RIGHT)
                rowjrec = SurroundingRectangle(r[0][j],corner_radius=0.1,color=PINK)
                rowm1 = SurroundingRectangle(r[0][3],corner_radius=0.1,color=PINK)

                with self.voiceover(text='''
To calculate the last variable, we subtract the sum value from row[-1] and then divide it by row[0]. 
Thus, solution[0] comes out to be 10. Hence, the value of x = 10.
                                    ''') as tracker:
                    self.play(Transform(cb[0],cb[9]),Write(x),Write(eq6),Create(sol0),Create(l))
                    a1 = r[0][-1].copy()
                    a2 = s1.copy()
                    a3 = r[0][j].copy()
                    br3 = Text("(",font_size=24)
                    br4 = Text(")",font_size=24)
                    self.play(a2.animate.move_to(l).shift(UP*0.3+0.5*RIGHT),Create(rowm1))
                    self.play(a1.animate.move_to(l).shift(UP*0.3+0.7*LEFT))
                    self.play(Write(sub.next_to(a1,RIGHT)),Create(rowjrec))
                    self.play(a3.animate.move_to(l).shift(DOWN*0.3),Write(br3.next_to(sub,1.2*RIGHT)),Write(br4.next_to(a2,0.8*RIGHT)))
                    self.wait()
                    self.play(AnimationGroup(*[FadeOut(a1,br3,a2,br4,a3,sub,l,sol0,rowjrec,rowm1),Write(answer.next_to(eq6,RIGHT))],lag_ratio=0.5))
                    fin = answer.copy().move_to(F[0][j])
                    fin1 = answer.copy()
                    self.play(AnimationGroup(*[fin1.animate.move_to(F[0][j]),AnimationGroup(*[FadeOut(F[0][j])],run_time=0.5)],lag_ratio=0.6))
                    F[0][j] = fin1

                self.play(FadeOut(i3,j3,s1,eq4,eq2,eq1,sm1,J,I,R,e,r,rec3,x,eq6,answer))
                grp = Group(S,eq5,F)
                for a in range(len(ind_i)):
                    self.play(FadeOut(ind_i[a]),run_time=0.1)
                for b in range(len(ind_j)):
                    self.play(FadeOut(ind_j[b]),run_time=0.1)
                self.play(grp.animate.shift(2*DOWN))

                arr1 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][0],DOWN)
                x1 = Text("x",font_size=18,color=YELLOW).next_to(arr1,DOWN)
                arr2 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][1],DOWN)
                y1 = Text("y",font_size=18,color=YELLOW).next_to(arr2,DOWN)
                arr3 = Arrow(start=0.5*DOWN, end=0.5*UP, color=YELLOW).next_to(F[0][2],DOWN)
                z1 = Text("z",font_size=18,color=YELLOW).next_to(arr3,DOWN)

                with self.voiceover(text='''Now we have the value of each variable and this becomes our final solution. 
                                    ''') as tracker:
                    self.play(Transform(cb[0],cb[12]))
                    self.play(Create(arr1),Write(x1),Create(arr2),Write(y1),Create(arr3),Write(z1))
                i -=1

        self.play(FadeOut(cd,cb[0],arr1,x1,arr2,y1,arr3,z1,E,S,eq5,F))

##############################  ENDING  ##############################################

        bg="window"

        code1 = '''
def eliminate(E):
    for i in range(len(E)):
        for j in range(i+1, len(E)):
            mult = E[j][i]/E[i][i]
            for k in range(i, len(E[i])):
                E[j][k] -= E[i][k]*mult
    return E'''

        code2 = '''
def solve_elimination(E):
    solution = [0 for _ in range(len(E))]
    i = len(E) - 1
    j = len(E[0]) - 2
    while i > -1:
        row = E[i]
        sum = 0
        for k in range(j+1, len(row) - 1):
            sum += row[k]*solution[k]
        solution[j] = (row[-1] - sum)/row[j]
        i -= 1
        j -= 1
    return solution'''
        
        code3 = '''
def solve(E):
    E = eliminate(E)
    return solve_elimination(E)
'''
        code4 = '''
E = [
    [1, 1, 1, 35],
    [3, 2, 1, 75],
    [4, 3, 1, 105]
   ]
solve(E)
'''
        A = [[1, 1, 1, 35], [3, 2, 1, 75], [4, 3, 1, 105]]
        B = [[10, 20, 5]]
        cd1 = Code(code=code1, tab_width=5, line_spacing=0.5, language="Python", background=bg).shift(3.1*LEFT+2*UP).scale(0.65)
        cd2 = Code(code=code2, tab_width=5, line_spacing=0.5, background=bg,language="Python").shift(3.1*LEFT+1.3*DOWN).scale(0.65)
        cd3 = Code(code=code3, tab_width=5, line_spacing=0.5, background=bg,language="Python").next_to(cd1,RIGHT).shift(0.48*UP+0.4*LEFT).scale(0.65)
        cd4 = Code(code=code4, tab_width=5, line_spacing=0.5, background=bg,language="Python").next_to(cd3,DOWN).shift(0.45*UP+0.1*LEFT).scale(0.65)
        E = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).next_to(cd4,DOWN).shift(1.5*UP).scale(0.4)
        F = Matrix(B,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.5, bracket_v_buff=0.5).next_to(cd4,DOWN).scale(0.5)

        with self.voiceover(text='''
        This is the complete code to automate the implementation of elimination method....which we discussed in the beginning of the video.
        You are already familiar with the two blocks of code on left side....Now let's discuss the other two.
        ''') as tracker:
            self.play(Write(cd1),Write(cd2),Write(cd3),Write(cd4))
        
        rec1 = SurroundingRectangle(cd1,corner_radius=0.1)
        rec2 = SurroundingRectangle(cd2,corner_radius=0.1)
        rec3 = SurroundingRectangle(cd3,corner_radius=0.1)
        rec4 = SurroundingRectangle(cd4,corner_radius=0.1)
        rec5 = SurroundingRectangle(E,corner_radius=0.1,buff=0.2, color=TEAL_B)
        rec6 = SurroundingRectangle(F,corner_radius=0.1,buff=0.2, color=TEAL_B)

        with self.voiceover(text='''
        Here, we are defining the E matrix which we introduced earlier and inputting the same to the solve function mentioned above.
        ''') as tracker:
            self.play(Create(rec4))
            self.play(Write(E))
            self.wait()
        
        self.play(FadeOut(rec4))
        a1 = Text("0", font="Times New Roman", font_size=16).move_to(E[0][4])
        a2 = Text("-1", font="Times New Roman", font_size=16).move_to(E[0][5])
        a3 = Text("-2", font="Times New Roman", font_size=16).move_to(E[0][6])
        a4 = Text("-30", font="Times New Roman", font_size=16).move_to(E[0][7])
        a5 = Text("0", font="Times New Roman", font_size=16).move_to(E[0][8])
        a6 = Text("0", font="Times New Roman", font_size=16).move_to(E[0][9])
        a7 = Text("-1", font="Times New Roman", font_size=16).move_to(E[0][10])
        a8 = Text("-5", font="Times New Roman", font_size=16).move_to(E[0][11])

        with self.voiceover(text='''
        The solve function plays the most important role here. It calls the eliminate function with E as the input,
        which performs the operations and returns the updated matrix. This new matrix is again termed as E.
        At the end, it calls the solve elimination function which performs the operations over this new matrix E 
        and returns the solution matrix as output that contains the values of variables.
        Hence, our goal is completed here........
        You can also try to implement the same with different equations.
        ''') as tracker:
            self.play(Create(rec3))
            self.wait(1.5)
            self.play(FadeOut(rec3),Create(rec1))
            self.play(Transform(E[0][4],a1))
            self.play(Transform(E[0][5],a2))
            self.play(Transform(E[0][6],a3))
            self.play(Transform(E[0][7],a4))
            self.play(Transform(E[0][8],a5))
            self.play(Transform(E[0][9],a6))
            self.play(Transform(E[0][10],a7))
            self.play(Transform(E[0][11],a8))
            self.play(Create(rec5))
            self.play(FadeOut(rec1),FadeIn(rec3))
            self.wait(1.5)
            self.play(FadeOut(rec3,rec5),Create(rec2))
            self.wait(4)
            self.play(FadeOut(rec2),FadeIn(rec3))
            self.play(Transform(E,F))
            self.wait(1)
            self.play(Create(rec6))
            self.wait()
            self.play(FadeOut(rec3,rec6))
        
        self.play(FadeOut(cd1,cd2,cd3,cd4,F,E))

############# QUESTIONS ##################

        A = [[3, 1, -8, 15], [6, 2, 7, 11], [4, 0, 5, -28]]
        B = [[4, -8, 20], [19, 6, 12]]
        C = [[9, -5, 0, -30], [10, 14, 4, 16], [8, -3, 1, 23]]
        D = [[8],[3],[7]]

        qs = Text("QUESTIONS",color=GREEN,weight=BOLD, font_size=30).shift(3.5*UP)
        q1 = Text('''Q 1.) Perform Matrix Addition - ''', color=RED, font="Times New Roman", font_size=25).next_to(qs, 7*DOWN).shift(4*LEFT)
        E = Matrix(A,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).next_to(q1,RIGHT).shift(2.05*LEFT).scale(0.45)
        plus1 = Text(" + ",font_size=25).next_to(E,1.2*RIGHT)
        F = Matrix(C,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).next_to(plus1,RIGHT).shift(2*LEFT).scale(0.45)

        q2 = Text('''Q 2.) Perform Matrix Multiplication - ''', color=RED, font="Times New Roman", font_size=25).next_to(q1, 11*DOWN).shift(0.4*RIGHT)
        G = Matrix(B,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).next_to(q2,RIGHT).shift(1.5*LEFT).scale(0.45)
        mult1 = Text(" * ",font_size=25).next_to(G,1.2*RIGHT)
        H = Matrix(D,v_buff=1.8, h_buff=1.8,bracket_h_buff=0.75, bracket_v_buff=0.75).next_to(mult1,RIGHT).shift(0.55*LEFT).scale(0.45)

        self.play(Write(qs))
        with self.voiceover(text='''Now here are some questions for you. Try solving them and post your
                            answer in the comments. 
                            ''') as tracker:
            self.play(Write(q1),Write(E),Write(plus1),Write(F))
            self.play(Write(q2),Write(G),Write(mult1),Write(H))
        
        self.wait(2)

        with self.voiceover(text='''That's all for this video. 
                            In the next video we will cover quadratic interpolation, showing how to solve a problem
                            and predict values using curves. Stay Tuned.''') as tracker:
            self.wait(4)

        self.play(FadeOut(qs,q1,E,plus1,F,q2,G,mult1,H))
        
