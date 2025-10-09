#####TYPEINGSOUNDS
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


define Type = Character("", callback=type_sound)
define NoType = Character("")
define narrator = Character("", callback=type_sound)





#CHARACTERS
define kr = Character("Kashima Reiko")
# teke teke girl

define ak = Character("Akari")
# random girl? I don't know what to set her as

define say = Character("Sayuri")

# another random girl
define yu = Character("Yuki", color="#ffffff", callback=type_sound)

########PLAYER
define pov = Character("[povname]")
define pov = Character("[povname]", color = "#78637B")



label start:


"What is your name?"
$ povname = renpy.input("",length=20)
if not povname:
 $ povname = "MC"


scene bg busstop



pov "Three of my friends are waiting near the train station for me. I better hurry."

scene bg busstop



label menu1:
    menu:
        "HIII":
            yu "ello"
            jump answer

        "Wasup":
            yu "whats good"
            jump answer

        "YO":
            yu "What's going on?"
            jump answer

        "What's up?":
            yu "oh you know"
            jump answer






label answer:
    # Add your dialogue or logic here
    yu "So, what do you want to do next?"


pov "It's so quiet."

ak "The early trains are canceled and the next bus won't come for a long time."

say "It's fine. We'll take the late train together."

kr "Excuse me..."
kr "Do you know when the next bus comes?"

say "oh! Um, I'm not entirely sure but maybe in an hour?"

say "And um are you okay?"

kr "My leg won't let me walk far. I was trying to get home."









label menu2:
    menu:
        "Offer to sit with her":
            jump sit_with

        "Keep a cautious distance":
            jump cautious_distance







label sit_with:
    say "Sit here. We'll wait with you."

    kr "Thank you." 

    ak "What's your name?"

    kr "Kashima Reiko."

    ak "Do you live nearby, Kashima-san?"

    kr "Not anymore. The last place I remember had sliding doors, a corridor… a sound like scraping metal."

    say "Scraping metal?"

    kr "You wouldn't want to hear it."

######Add audio for teke sound
play sound "audio/bus_idle.ogg" fadein 0.2



kr "They told me not to come here after midnight."

ak "Who told you that?"

kr "People on late trains. An old woman. A radio. I can't— sometimes I wake up and the floor is different."

say "You mean... like a memory that doesn't belong to you?"

kr "Yes. Bits. Pieces. There's one that repeats: I run, and the floor is only half beneath me."



#####ADD SOME FLICKERING STUFF

kr "Can I ask a favor?"

ak "Of course."
kr "If... if you ever hear the tapping of two things running, please—make more noise. Don't be quiet."

say "Tapping? Running?"
kr "Like... 'tekeke.' People call her Tekeke. But she is not only 'tekeke.'"

ak "You're scaring us, Kashima."

kr "Sorry. I don't mean I only remember the ending."

#####MORE AUDIO NOISE
jump bus_arrival



##### cautious distance

label cautious_distance

say "What happened to your leg?"

kr "Insert what happened here"

ak "wow thats... unfortunate." #### i dont know what to say what happened to her leg so im just gonna have templace placement text we can change
##### i also didnt know how you wanted the story to progress so i added this
##### with our remaining time frame i say we get straight into the mini game and make it super super short we might not be able to get a artist

pov "Would it be better to just walk?"

say "I mean we could... but its late and cold out."
ak "Yea, and I dont really know my way back."

##### instert creepy music?

kr "I wouldnt at this time tekeke could be out at this time"
say "tekeke?"

kr "if you ever hear the sound of two things tapping, make more noise"
kr "they dont like me on trains"
kr "the people on buses"
kr "they hear us"

ak "W-what, your scaring me..."
pov "yea are you ok?"

#### bus arival noise
jump bus_arrival












