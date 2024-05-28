define s = Character("Martin")
define c = Character("Peadar")
define f = Character("Mikhail")
define p = Character("Player")
image s = Transform("images/Martin-new-02.png", zoom=0.23)
image c = Transform("images/PeadarGhalagan.png", zoom=1)
image f = Transform("images/Mikhail-new-02.png", zoom=0.2)
image bg = Transform("images/seems legit.png", zoom=1.5)

init:
    $ score=0
    $ name=""

# The game starts here.

label start:
    scene bg
    
    show c at left
    show f at right
    show s 

    s "Hi! Are you ready for the admission interview?"

    menu:
        "Yes":
            $ score+=1
            jump d0002
        "No":
            jump d0003
        "I don't know what you are talking about":
            jump d0007

    label d0002:
        "d0002"
        s "My name is Martin Sillaots, and I'm the head of the Digital Learning Games master's programme."
        c "My name is Peadar Callaghan. I'm a graduate of the DLG programme and a teacher in this programme."
        f "My name is Mikhail Fiadotau, and I'm a teacher in this programme."
        s"Please, introduce yourself, your background and interest in the DLG programme."

        menu:
            "My name is *player*, and I want to come to study at Tallinn University.":
                jump d0101
            "My name is *player*, and I'm a parent of X kid(s).":
                $ score+=1
                jump d0008
    
    label d0003:
        s "So what should we do then?"
        menu:
            "Can I have this interview some other time?":
                $ score-=1
                jump d0004
            "I would like to be accepted to the programme but fear the interview.":
                jump d0005
            "I changed my mind. I would like to study something else.":
                jump d0006

    label d0004:
        s "Sure. Our study counsellor will contact you and arrange another time for the interview."
        menu:
            "Thank you for this opportunity. Bye!":
                $ score-=80
                "END"
                return
            "Let's have this interview now. I don't believe that next time is better.":
                $ score+=1
                jump d0005

    label d0005:
        s"Relax. Take a deep breath. There is no need to be worried. We are all friendly people here, and we are sure you will do fine."
        menu:
            "Thank you for encouraging me.":
                $ score+=1
                jump d0101
            "Easy for you to say. You are doing this every year, I'm doing this once in a lifetime.":
                jump d0101

    label d0006:
        $ score-=80
        s "We respect your decision. We wish you good luck in your studies."
        "END"
        return

    label d0007:
        "d0007"
        s"This is a DLG admission interview. You applied to Dream Apply, and our study counsellor scheduled a meeting with you for the interview."
        menu:
            "Ah, you are right. I forgot about it.":
                jump d0101
            "Yes, but I was already accepted to another programme.":
                jump d0006
    label d0008:
        s" Is the number of kids the most important factor in starting your studies?"
        menu:
            "No, but this is something that influences my activities.":
                $ score+=1
                jump d0101
            "Yes. I'll do everything for my kids.":
                $ score-=1
                jump d0101

    label d0101:
        s "Why are you interested in Digital Learning Games?"
        menu:
            "I would like to get my foot in the gaming industry":
                #jump d0102
                pass
            "I would like to use games as teaching tools":
                $ score+=1
                #jump d0106
            "I would like to create games that teach something":
                $ score+=1
                #jump d0107
    "end for the demo"
    return
