 

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



##pick between one of the two and add an # to the other to keep it

##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']


##both combined
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


#example of a character with the typing sound
define Type = Character("", callback=type_sound)





define kr = Character("Kashima", image="kashima", color="#ffffff", callback=type_sound)
image kashima:
    "side kashima.png"




# Define a transform for Sayuri to appear on the right
transform right_side:
    xpos 0.8      # 0.0 = left, 0.5 = center, 1.0 = right
    ypos 0.6
    linear 0.25 yoffset -10
    linear 0.25 yoffset 0

# Define a transform for Yuki to appear on the left
transform left_side:
    xpos 0.0
    ypos 0.6
    linear 0.25 yoffset -10
    linear 0.25 yoffset 0

# --- Yuki setup ---
image yuki = "side yuki.png"

init python:
    def yuki_jump_callback(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("yuki", at_list=[left_side])
        return None

define yu = Character("Yuki", color="#ffffff", callback=yuki_jump_callback)


# --- Sayuri setup ---
image sayuri = "side sayuri.png"

init python:
    def sayuri_jump_callback(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("sayuri", at_list=[right_side])
        return None

define say = Character("Sayuri", color="#ffffff", callback=sayuri_jump_callback)


# --- Script ---
label start:
    scene bg buscheck

    jump menu1


label menu1:
    menu:
        "HIII":
            yu "Hii!"
            jump answer1

        "Wasup":
            yu "Nothing much."
            jump answer1

        "YO":
            yu "What's going on?"
            jump answer1

        "What's up?":
            yu "Oh you know."
            yu "Nothing really, just waiting for you."
            jump answer1


label answer1:
    say "It's so quiet."



yu "The early trains are canceled and the next bus won't come for a long time."

yu "Although it's okay! We'll take the late train together."

kr "Excuse me..."
kr "Do you know when the next bus comes?"

yu "oh! Um, I'm not entirely sure but maybe in an hour?"

yu "And um are you okay?"

kr "My legs won't let me walk far. I was trying to get home."









label menu2:
    menu:
        "Offer to sit with her":
            jump sit_with

        "Keep a cautious distance":
            jump cautious_distance





label cautious_distance:

kr "Can you help me I seriously need help..."
kr "I can't feel my legs."
kr "Where are they?"

label menu3:
    menu:
        "Answer":
            jump answer

        "Don't answer":
            jump dontanswer





label sit_with:
    say "Sit here. We'll wait with you."

    kr "Thank you." 

    say "What's your name?"

    kr "Kashima Reiko."

    yu "Do you live nearby, Kashima-san?"

    kr "....."
  
    yu "Kashima-san?"


    kr "Can I ask a question?"

    yu "Of course."


    kr "Where are my legs?"


label menu4:
    menu:
        "Answer":
            jump answer

        "Don't answer":
            jump dontanswer


label answer:

say "Right here..."
say "Wait..."
say "Why is there nothing there?"

jump Running



label dontanswer:

yu "ON THE MEISHIN RAILWAY!"
yu "....."
yu "SAY IT!"
say "On the Meishin Railway..."
kr "...."
yu "Sayori..."
yu "I think she's this urban legend I've heard about..."
yu "That's the only question I knew how to answer, but we need to answer them all right or..."
yu "She might kill us!"

jump Running

label Running:
kr "teke..."
kr "teke.....teke"
kr "teke.....teke.....teke"

menu5:
    "RUN!":
    jump Running2

label Running2:

say "We have to get the hell out of here!"

    menu6:
        "Right":
        jump Right1

        "Left":
        jump Left1

label Right1

yu "Where do we go now???"

menu7:
    "straight":
    jump straight









    
























