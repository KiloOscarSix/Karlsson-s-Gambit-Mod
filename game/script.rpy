




define p = Character(("[pname]"), color="#00bfff")
define d = Character("Dominique", color="#ff0000")
define j = Character("Juliette", color="#ff00cc")
define a = Character("Alessandra", color="#ccffff")
define v = Character("Veronica", color="#6600cc")
define z = Character("Tess", color="#ff00cc")
define y = Character("Our victim...err...maybe heroic protagonist", color="#66ffff")
define dd = Character("Doctor Clarke", color="#99ffff")
define xx = Character("????????", color="#ff6666")
define ak = Character("Alexander Karlsson", color="#cccccc")
define pp = Character("Guard Patricia", color="#1e90ff")
define p1 = Character("Prisoner 912", color="#ff1493")
define ec = Character("Elena", color="#f08080")
define p2 = Character("Prisoner 1821", color="#ff1493")
define p3 = Character("To be named Protagonist", color="#00bfff")
define pp2 = Character("Guard Samantha", color="#1e90ff")
define fs9 = Character("Footstool Nine", color="#ff1493")
define db = Character("Dumbo", color="#1e90ff")
define jk = Character("Junko", color="#f08080")
define cs = Character("Computer Screen", color="#ffff66")
define pbf = Character(("[pname2]"), color="#99ff66")
define kk = Character("Kitty", color="#f08080")
define ns = Character("Nurse Jones", color="#f08080")
define sis = Character(("[pname3]"), color="#9400d3")
define dj = Character("Doctor Janssen", color="#99ffff")
define ua = Character("Male Assailant", color="#888888")
define bro = Character(("[pname4]"), color="#99ff66")

define nath = Character("Servant Nathan", color="#ff1493")
define gary = Character("Gary", color="#ff1493")
define zach = Character("Prisoner Zach", color="#ff1493")
define comp = Character("Test Computer Screen", color="#ffff66")
define hack = Character("Unknown Hacker", color="#6600cc")
define kw = Character("Kwame", color="#6600cc")
define p5 = Character("Prisoner 4301", color="#ff1493")
define cass = Character("Cassandra", color="#ff0000")
define tp = Character("Test Penis Subject", color="#ff1493")
define ky = Character("Kiyomi", color="#f08080")
define al = Character("Alicia", color="#ffff66")

define mom = Character("Callista", color="#ffff66")
define kk2 = Character("Katsumi", color="f08080")
define de = Character("Delilah", color="#ff0000")
define sy = Character("Sonya", color="#ff0000")
define cman = Character("Chained Man", color="#ff1493")
define di = Character("Diana", color="#ff1493")
define br = Character("Brad", color="#ff1493")
define sc = Character("Scarlett", color="#ff0000")
define queen = Character("Gambit Queen", color="#cccccc")
define anne = Character("A.N.N.E.", color="#ffff66")
define dan = Character("Daniel", color="#ff1493")
define chan = Character("Chanel", color="#ff0000")
define nurse = Character("Nurse Reyes", color="f08080")























define gui.name_text_outlines = [ (2, "#000", 0, 0) ]
define gui.dialogue_text_outlines = [ (2, "#000", 0, 0) ]
define gui.idle_small_color_outlines = [ (0, "#000000", 2, 2) ]
define gui.hover_color_outlines = [ (0, "#000000", 2, 2) ]

define fade = Fade(0.5, 0.5, 0.5, color="#241e20")
define mediumfade = Fade(0.7, 0.7, 1.0, color="#241e20")
define longfade = Fade(1.0, 1.5, 2.0, color="#241e20")
define superfade = Fade(2.0, 2.0, 2.0, color="#241e20")
define flash = Fade(0.1, 0.0, 1.0, color="#f2eee2")
define quickflash = Fade(0.1, 0.0, 0.1, color="#f2eee2")
define mediumflash = Fade(0.1, 0.0, 1.0, color="#f2eee2")
define longflash = Fade(0.1, 0.0, 2.0, color="#f2eee2")
define quickdissolve = Dissolve(0.3)
define mediumdissolve = Dissolve(1.5)
define longdissolve = Dissolve(2.0)
define superdissolve = Dissolve(3.0)


transform pan_scene_up:
    ypos 0
    linear 10 ypos 1920
transform pan_scene_down:
    ypos 1920
    linear 10 ypos 0




label start:

    default good = 0
    default evil = 0
    default dom = 0
    default sub = 0
    default shock = 0
    default elena_mentor = False
    default bad_joke = False
    default elena_p = 0
    default samsadist = False
    default patpunish = False
    default friend = 0
    default selfisheater = False
    default sam_p = 0
    default samupset = False
    default pat_p = 0
    default pat_secpath = False
    default sisdom = 0
    default sissub = 0
    default sisgood = 0
    default sisevil = 0
    default sis_a_p = 0
    default dome11 = False

    default sis_bro_p = 0
    default sisbonus = False
    default poornath = False
    default sis_d_p = 0
    default patdealyes = False
    default patdealno = False
    default beggarboy = False
    default slavepoints = 0
    default veronica_p = 0
    default alessandra_p = 0
    default dominique_p = 0
    default juliette_p = 0
    default soloplayer = False
    default teamplayer = False
    default gambitplayer = False
    default hackersecret = False
    default bro_e_p = 0
    default zachweak = False
    default sprintwalk = False
    default jogwalk = False
    default strongjog = False
    default kanefallone = False
    default gambitpoints = 0
    default k4 = False
    default k5 = False
    default k6 = False
    default sis_c_p = 0
    default poorprisoners = False
    default richprisoners = False
    default bro_k_p = 0
    default pissboy = False
    default kitty_p = 0
    default redass = False

    default kitty_scale = 0
    default brotherpunish = False
    default elena_meeting = False
    define dmeet = 0
    define jmeet = 0
    define vmeet = 0
    define kittyoffer = False
    default jromanceopen = False
    default jfriendopen = False
    default jslaveopen = False
    default scarlett_scale = 0
    default junko_scale = 0
    default scarlett_p = 0
    default junko_p = 0
    default junkopet = False
    default scarlettpeg = False
    default busyboy = False
    default freeagent = False
    default cassandraloyal = False
    default evilpolice = False
    default moralityone = False
    default sis_v_p = 0
    default sis_j_p = 0
    default proboss = False
    default reddevil = False
    default danieljailed = False
    default danielpet = False
    default danieltoilet = False
    default danielfurniture = False
    default murderess = False
    default moralitytwo = False
    default sisgambitqueen = 0
    default julietteworried = False
    default sethweak = False
    default sethtough = False
    default kwamefriendopen = False
    default bestfriendloyalopen = False
    default chanel_scale = 0
    default chanel_p = 0
    default veronica_scale = 0
    default nurse_scale = 0
    default toughpain = False
    default weakpain = False
    default injuredass = False
    default dominiqueinterest = False
    default chanelpunish = False
    default juliette_scale = 0
    default juliettesponsor = False
    default dominiquesponsor = False
    default veronicasponsor = False
    default momknowledge = False
    default kiyomi_p = 0
    default kiyomisethlight = False
    default vipertoy = False
    default dominique_scale = 0
























    init python:
        renpy.music.register_channel("one", mixer="sfx", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.7, delay=0.0, channel='one')
    init python:
        renpy.music.register_channel("two", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=1.0, delay=0.0, channel='two')
    init python:
        renpy.music.register_channel("three", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=1.0, delay=0.0, channel='three')
    init python:
        renpy.music.register_channel("four", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.6, delay=0.0, channel='four')
    init python:
        renpy.music.register_channel("five", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.6, delay=0.0, channel='five')
    init python:
        renpy.music.register_channel("seven", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.3, delay=0.0, channel='seven')
    init python:
        renpy.music.register_channel("eight", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.3, delay=0.0, channel='eight')
    init python:
        renpy.music.register_channel("nine", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    $ renpy.music.set_volume(volume=0.4, delay=0.0, channel='nine')





    scene black

    stop music fadeout 3


    play one "audio/heart.mp3"

    dd "It's about time Sir."
    ak "Then leave us."
    dd "Yes Sir."

    ak "Can you play her song? One last time."
    xx "Yes, Father."

    play two "music/thesong.mp3"

    ak "This is our last chance to talk, are you ready for everything?"
    xx "I am."
    ak "Good. Just remember that this is your final exam for my empire, and you know my wishes if you want it all. If you are not worthy, I'd rather my empire fall apart."
    ak "Your sisters have been trained well too and I am giving them their chance as well, but I know deep down you are the strongest and best of them."
    ak "You also know you are not enough on your own to succeed. You must do what I ask completely."
    ak "Focus. It's up to you."
    ak "Do you intend to work with your sisters, or destroy them? I guess I will never know."
    ak "Watch out for my remaining lovers of course."
    ak "They will scheme until the very last breath. They will not accept so easily being bypassed."
    xx "I know."
    ak "Remember...*cough* the true nature of power that you could wield if you succeed."
    ak "Embrace it. Accept it."
    xx "\"...unlimited power in the hands of one person always leads to cruelty...\""
    ak "...And last...last...him...test him. You...must...you must know...she...I...that is my final price for all that I have."
    xx "I will."
    ak "If you succeed, you can shape everything to your whims. In any way you wish. With or without whoever you desire too..."
    ak "Do what you will with everyone if you succeed...your...your desire should rule over all else..."
    ak "You are such a brilliant mind. Shining far more than I even though you hide it very well."
    xx "I know what you truly want Father. I will do it, if it is a worthy choice."
    ak "I know...I am glad too. I knew you truly understood me deep down."
    ak "...So brilliant, but I worried as I taught you that you were not willing to do what was necessary to control your fate."
    ak "But only now as I look into your eyes...*cough*...truly only right now do I actually see you as I die..."
    ak "I understand now and I see your real brilliance because you even fooled me didn't you?"
    xx "Yes, Father."
    ak "Well done. But, will you ever consider a different way than who you are now?"
    ak "You can change the world for better or worse. And yourself too."
    ak "But take the world as you see fit."
    ak "Ugghhh, my head! It's over for me now..."
    ak "Remember well everything I have taught you."
    ak "Let the song fade now as I do...I am ready to leave."

    stop two fadeout 3

    ak "Maybe in a different life...maybe it could have been..."
    ak "Maybe..."
    ak "Farewell, my daughter."

    stop one fadeout 1

    play one "audio/heart2.mp3" fadein 1

    ak "...I...I can see the...the...it's so...wow...wow..."

    stop one fadeout 5

    play two "audio/laugh2.mp3" fadein 1

    xx "Goodbye, Father."

    stop two fadeout 2





    play music "<from 10 to 165.5>music/hallway.mp3" fadein 1

    scene jail1 with superfade
    pp "Prisoner 2719! Get your ass up!"
    scene jail2 with quickdissolve
    pp "Hey! Let's move it! Got a special visitor for you maggot!"
    scene jail3 with longdissolve
    pp "A VIP! Corporate! Wonder what she wants with you."
    scene jail4 with mediumdissolve
    pp "Especially since you're such a special boy anyway! You get your own cell all by yourself with a real toilet, bed, fresh sink water, and even a pillow!"
    pp "All the other worms here are so jealous of you, they are so cramped like sardines in a tiny can and get the luxury of sleeping with their own shit!"
    pp "They'd probably cry with joy just to be able to drink your dirty toilet water!"
    scene jail5 with longdissolve
    pp "Anytime now maggot!"
    scene jail5b with longdissolve
    pp "That's better, at least you can move well, better than a lot of my worms here right now, haha!"
    scene jail6 with longdissolve
    pp "Our VIP visitor also insisted you didn't need cuffs to talk to her, but don't you get any ideas!"
    pp "You've still got 24/7 surveillance and your shock collar maggot so you can be knocked out in one second so just don't!!"
    scene jail7 with longdissolve
    pp "You've never caused trouble or annoyed me so I'm going to give you a little leeway."
    pp "Let's go see what this is all about!"

    stop music fadeout 3

    scene hallway1 with superfade

    play music "<from 1 to 60>music/meeting0.mp3" fadein 1

    pp "I suggest you make a good impression, this lady is serious business."
    pp "She's part of the Executive Council of the entire company, that's only like seven people."
    scene hallway2 with longdissolve
    p2 "Please...I'm so thirsty, just a little water."
    scene hallway3 with mediumdissolve
    pp "You stay here and behave a second. I need to speak to this worm. They're still watching you on camera 24/7 so don't get any funny ideas."
    scene hallway4 with mediumdissolve
    pp "Oh, they cleaned you up so nice! It was so funny seeing you piss yourself but now look at you!"
    p2 "Please, some water."
    scene hallway5 with longdissolve
    pp "Oh, so thirsty, aren't you? You didn't clean all of the guards' boots well enough so you have to finish your punishment."
    scene hallway6 with quickdissolve
    p2 "But I scrubbed, cleaned and polished them over 16 hours straight! And then you poured my only drinking water on one single pair and said I failed!! It's just so unfair!"
    scene hallway7 with mediumdissolve
    pp "A clean boot means it's totally dry too. Too bad for you. And for talking back and questioning my judgment, I think you need a visit with Samantha."
    scene hallway8 with quickdissolve
    p2 "NO PLEASE! Anything but that!"
    scene hallway8b with quickdissolve
    p2 "I'll do anything, please please!"
    scene hallway8c with longdissolve
    pp "Then ask nicely and apologize like the bug you are."
    scene hallway9 with mediumdissolve
    p2 "Please...I'm sorry...please"
    scene hallway9b with quickdissolve
    p2 "Have mercy...please."
    scene hallway10 with longdissolve
    pp "Good job bitch. On your knees where you belong."
    scene hallway10b with mediumdissolve
    pp "But you need to learn the value of hard work here so this time you are going to have to clean and polish all of our boots with just your tongue only."
    p2 "*softly* oh no...you cruel...no"
    scene hallway10c with quickdissolve
    pp "I'll make sure your boot cleaning day is right after a hard rain when you work outside and you can stay niiiiiice and busssy with all of the extra dirt and grime."
    pp "And...I just can't have you talking back to me because it might make you think you matter. So Samantha will be seeing you real soon."
    scene hallway11 with longflash
    p2 "oh no oh no please no no no no no no"
    scene hallway12 with mediumdissolve
    pp "Oh NO, you poor baby, maybe if you cry and cry she will be a little easier on you!"
    pp "Oh! You could lick your tears for water! Fix your painful thirst that way!"
    scene hallway13 with longdissolve
    p2 "no no no..."
    pp "Awwwwww, poor little worm, maybe you can start practicing your boot cleaning right now, haha!"
    scene hallway14 with longdissolve
    pp "(oh yessssss, I love love LOVE my job!)"
    scene hallway14b with mediumdissolve
    p3 "(That is one cruel and mean bitch...)"
    scene hallway15 with longfade
    pp "Ah, so sad for the short little turd isn't it. As for you, at least you are a tall maggot and not a worm, eh?"
    p3 "(How is a maggot better than a worm anyway???)"
    pp "But I'm so good at my job aren't I, maggot?"

    menu:
        "Call her out on her cruelty. [DomPath] [GoodPath]":
            $ dom += 1
            $ good += 1
            scene hallway15a with mediumdissolve
            p3 "You're just an evil bitch."
            scene hallway15b with mediumdissolve
            pp "Why thank you maggot, right you are. Perfect job for me, don't you think?"
            p3 "I suppose. It doesn't make it right."
            pp "I guess you'd fail as a guard here. Maybe the collar is better for you?"
        "Say nothing but frown. [SubPath] [GoodPath]":
            $ sub += 1
            $ good += 1
            scene hallway15d with longdissolve
            p3 "......."
            scene hallway15c with mediumdissolve
            pp "Oh. You disapprove. Too bad. Maybe I would have let you have some fun."
        "Tell her you don't care as long as you're left alone. [SubPath] [EvilPath]":
            $ sub += 1
            $ evil += 1
            scene hallway15e with mediumdissolve
            p3 "Better him than me, I just want to be left alone."
            scene hallway15b with longdissolve
            pp "Don't you care about the welfare of your fellow worms?"
            p3 "No."
            scene hallway15h with mediumdissolve
            pp "Hmm, I can appreciate your desire for survival."
            scene hallway15k with mediumdissolve
            pp "You know, maybe if you keep being a good little maggot, I'll let you have a little fun later."
        "I could do a better job. [DomPath] [EvilPath]":
            $ dom += 1
            $ evil += 1
            scene hallway15a with mediumdissolve
            p3 "I could do better."
            scene hallway15b with mediumdissolve
            pp "Oh really? You haven't even seen my best work yet, but ok! Tell me what you could do better."
            scene hallway15f with mediumdissolve
            p3 "Why don't you let me be in charge and find out."
            scene hallway15g with mediumdissolve
            pp "Haha, you wish."
            scene hallway15h with mediumdissolve
            pp "But...maybe now I see why they gave you special treatment here."
            scene hallway15i with mediumdissolve
            pp "You know, it's too bad I'm not in charge of the entire jail. With the power to...enjoy...any prisoner I want."
            scene hallway15j with mediumdissolve
            pp "I got so in the mood to fuck savoring that worm cry in fear and I bet you clean up reeeeeaaal nice."
            scene hallway15l with mediumdissolve
            pp "When I'm this turned on, you wouldn't believe how much fun I am to fuck. Pity."

    scene hallway16 with longfade
    pp "Anyway...such a nice quick diversion! But I think we've kept her waiting long enough."
    pp "Let's go maggot."

    stop music fadeout 2

    scene meeting1 with longfade

    play music "music/prop.mp3"

    ec "Ah, there you are. Please have a seat."
    ec "You can wait in the observation room and watch us there Patricia."
    scene meeting2 with longdissolve
    ec "I am sure our guest here will behave, but if he makes any sudden moves, I am confident Samantha can shock him immediately."
    p3 "(Guest my ass...)"
    pp "Yes, Miss Caspari."
    scene meeting3 with longdissolve
    ec "Now then, let's have a little chat."
    ec "What's your name?"

    python:
        pname = renpy.input("My first name is...(just type name and press Enter)")
        pname = pname.strip()

        if not pname:
            pname = "Kane"

    python:
        pname_f = renpy.input("My last name is...")
        pname_f = pname_f.strip()

        if not pname_f:
            pname_f = "Jacobs"



    scene meeting3b with quickdissolve
    p "[pname_f]."
    p "[pname] [pname_f]."
    p "But surely you know that already."
    scene meeting4 with mediumdissolve
    ec "Of course. But I just wanted to hear you say your own name. Sometimes it illuminates something about you."
    p "Whatever you say."
    scene meeting5 with mediumdissolve
    ec "I can't help but notice right away that's quite a nasty little set of bruises you have on your face. How did that happen?"

    menu:
        "Play it straight":
            scene meeting6 with mediumdissolve
            p "I got jumped in the laundry room by another prisoner."
            ec "I see. We can talk about that in a bit."
        "Sarcastic [ElenaPath] \[Bad Joke\]":
            $ bad_joke = True
            $ elena_p += 1
            scene meeting6 with mediumdissolve
            p "Had to beat up my own meat product dinner, it was crawling away from my plate. The cuisine here is of course top notch."
            scene meeting7 with mediumdissolve
            ec "Nice that you can display humor with your situation."
            ec "Oh...I like meat too and you know, I know a little about beating an uncooperate and worthless piece of meat that tries to...crawl away..."
            scene meeting9 with mediumdissolve
            p "I see..."
            ec "You are quite good at minimizing your reactions, but don't fret [pname], I could be your best friend today if you are lucky."
        "Silent treatment [ElenaPath]":
            $ elena_p += 1
            scene meeting8 with mediumdissolve
            p ".............."
            scene meeting10 with quickdissolve
            ec "Hmm, don't want to volunteer anything do we? I can respect if you are being calculating and distrusting of those around you. And I guess I can't blame you."
            ec "But I think you will soon see you would want me as an ally."

    scene meeting11 with longdissolve
    ec "But let's get to why I am here. My name is Elena Caspari, and I am the Senior Legal Officer for The Karlsson Group."
    p "Oh, Karlsson. Let's see, slave diamond and mineral mines everywhere, arms dealing, slave level clothing sweatshops, and of course you own this lovely prison and a thousand others like it...did I miss anything?"
    ec "A lot actually. You forgot for example our very important medical research division. We also do a lot more than what is deemed...controversial by so many."
    scene meeting12 with mediumdissolve
    p "But likely even worse stuff no one knows about."
    scene meeting13 with mediumdissolve
    ec "Perhaps. You know, it's apparent right away your mind is quick as your file indicates and it's impressive for one of your...peasant background."
    scene meeting14 with quickdissolve
    p "Sorry I wasn't born part of the one tenth of one percent of the world now that actually has real opportunity to get educated and make money."
    ec "Very fair. But you are still luckier than most."

    stop music fadeout 2

    play music "<from 3 to 45>music/meeting1.mp3" fadein 1

    scene meeting16 with mediumdissolve
    ec "So many people now starve to death or die of thirst, the shortages have changed so much in only 20 years."
    ec "Fortunately, The Karlsson Group is very well off and controls the food and water supply for millions of people."
    ec "And every day, we often have to make decisions on who lives...and who dies."
    scene meetings1 with longdissolve
    ec "I see throngs of people begging everyday for a pitiful crumb or pittance just to stay alive."
    ec "It's quite a feeling seeing them begging at the side of the road while I slowly eat caviar in my limo..."
    scene meetings2 with longdissolve
    ec "What a world it is today isn't it with so few people being so rich and powerful while almost everyone else struggles to survive."
    ec "If only you had the opportunity to enjoy your life more [pname]."
    scene meetings3 with longdissolve
    ec "Wouldn't it be nice for you to be in a position like mine where you could do or...take what you want? Would you be meek...or strong given that chance?"
    ec "It would be so much better than being a little pig in here wouldn't it?"
    scene meetings4 with quickdissolve
    p "(Damn...what the...?)"
    ec "You don't have it good to be sure, but maybe it could be worse for you, eh? At least you have some minimal food and water here at our special hotel."
    p "Lucky me."

    stop music fadeout 2

    scene 2meeting1 with superfade

    play music "music/prop.mp3" fadein 2

    ec "Let's move on though. Believe it or not, I feel a little bad teasing you so soon."
    p "Fine."
    scene 2meeting2 with quickdissolve
    ec "Lets talk about you. I read over your file on the way here. You were sentenced two months ago to five years for beating up another man, yes?"
    scene 2meeting3 with mediumdissolve
    p "That's what it says I guess."
    scene 2meeting4 with mediumdissolve
    ec "Ok, what should it say? You beat down that man and he apparently was hurt pretty badly. Your time from arrest to sentencing to being here was only one month. Quite fast and unusual."
    ec "And five years seems a little stiff too because he seemingly recovered quite quickly."
    scene 2meeting5 with mediumdissolve
    p "It was a complete set up and frame job. I don't know why someone would target me of all people, but it's bullshit. I barely touched that guy."
    p "But somehow a day later he's magically a near cripple with life threatening injuries and then right after I am jailed he seems awfully healthy all of a sudden."
    ec "I see. I bet if you had me as your attorney, you would have been fine. But he had money...and you didn't."
    p "Again, I'm such a lucky guy."
    scene 2meeting6 with longdissolve
    ec "You might be actually..."
    p "Why?"
    ec "First things first, be patient [pname]. You were raised by a single mother and have an older sister and younger brother?"
    scene 2meeting7 with quickdissolve
    p "Yeah, that's right. Why are we talking about this?"
    scene 2meeting8 with longdissolve
    ec "And your mother died in a helicopter crash? Your sister at least is healthy but alone without you..."
    ec "Your current situation seems like it is because you tried to steal money from the man you beat...to help your brother. And your brother's suffering from a severe medical..."

    menu:
        "Interrupt her forcefully [DomPath]":
            $ dom += 1
            scene 2meeting9 with mediumdissolve
            p "I think you better stop right there. Family history time is over."
            scene 2meeting9b with mediumdissolve
            ec "I am the one in the position of power here. Why should I bother listening to you [pname]?"
            menu:
                "Appeal to her decency and that there is no sense going into detail about your brother's medical condition.":
                    p "There's no need to go into detail about him. Have some decency."
                    scene 2meeting9c with mediumdissolve
                    ec "Showing weakness by appealing to my decency will get you nowhere. Now, about your brother..."
                    jump taunt
                "Argue that if she wants to get something from me to her own advantage, a little gesture to accommodate me helps her accomplish that. [ElenaPath]":
                    $ elena_p += 1
                    p "It's such a small gesture of good faith for you to stop about my brother, and it probably helps you get what you want from me easier."
                    scene 2meeting9c with mediumdissolve
                    ec "Hmm, a thoughtful answer. Appealing to my own desire is smart of you."
                    ec "Very well, let's move on from your brother, and I can understand that from your perspective."
                    scene 2meeting10 with mediumdissolve
                    ec "But I have to say quickly it's obvious your brother's sickness could be cured with a little money."
                    p "Yeah, I fucking know ok?"
                    jump prop
        "Allow her to continue without interruption [SubPath]":

            $ sub += 1
            jump taunt

label taunt:

    stop music fadeout 1

    play music "<from 19 to 38>music/poorbrother3.mp3" fadein 2

    scene 2meeting11 with longdissolve
    ec "Hmm, he's suffering from an obviously serious medical condition. Poor thing."
    ec "That's such a painful condition too, the pain is so severe throughout all the nerves on the body."
    scene 2meeting12 with longdissolve
    ec "It must be so hard for you to know he is in such excruciating pain. Day. After. Day. Constantly in agony. He can't even afford effective painkillers to ease his suffering a little."
    ec "And I hear he's just strapped to a bed. So the poor thing can't even kill himself if he wanted to end his suffering."
    scene 2meeting12b with mediumdissolve
    ec "Isn't it even worse to think about the fact that he could be treated and even cured with just a little bit of money. Oops, not for you, but such a tiny bit of money for me."
    ec "I think less than a month in pay from my salary could completely cure him. Less than that time of my passive income for doing nothing. So so easy for me...but you have nothing."
    scene 2meeting13 with mediumdissolve
    ec "I probably spent that much yesterday just for a set of jewelry and new luxury pet house for my dog."
    ec "A dog gets jewels and luxury while your poor and penniless brother cries in pain."
    ec "So. Brutal. Isn't it [pname]?"

    menu:
        "Say nothing. [ElenaPath]":
            $ elena_p += 1
            scene 2meeting14 with mediumdissolve
            ec "You want to...rage at your poor situation don't you? If only you had some power to do something."
            ec "But still, very good to stop yourself rather than act irrationally with an outburst in an inferior position of power. Remember that. It will help you survive."
            jump prop
        "Lash out in anger and stand up to show it. [Shock]":
            $ shock += 1
            scene 2meeting15 with quickdissolve
            p "Damn it...!"
            ec "[pname]! I wouldn't..."
            scene 2meeting15a with quickdissolve
            p "*bzzzzzzztt* Aaaaggghghhhghhh!"
            scene 2meeting16 with longfade
            ec "Quite foolish [pname]. Your collar can shock and even paralyze if desired instantly and Samantha is extremely diligent if I am here. She loves to watch you anyway."
            ec "Always always think. If you act without thinking, you will end up as a real pig of one of the Karlsson girls. Or worse. Remember that. Now sit back down."
            p "(Ughhhh that hurt. And I don't even know how many kids that Karlsson prick has...)"
            jump prop

label prop:
    stop music fadeout 2

    play five "music/prop.mp3"

    scene prop1 with longfade
    ec "Now just relax [pname], maybe this could be a chance for you to change your fate."
    ec "I'm here because I may want to offer you a proposition."
    ec "The Karlsson Group has instituted a new training and pardon program for selected inmates that meet certain criteria."
    scene prop2 with quickdissolve
    p "What criteria?"
    ec "That's a corporate secret for now but in time you may discover that I think. Suffice to say that the program allows you to work under our company..."
    scene prop3 with quickdissolve
    ec "...for a period of six months and if that experience goes well, you would be offered a position with The Karlsson Group and your remaining prison time would be eliminated with a complete pardon."
    ec "Keep in mind you would still be a prisoner with very little rights under this program, but under the right supervision or situation you could enjoy some freedoms you could never have here."
    scene prop4 with mediumdissolve
    p "What kind of work for the six months and what kind of work afterwards?"
    ec "Honestly, it depends on how you test and perform. Some work will not be that great and quite manual labor intensive, but if you are lucky, you could do much more...pleasant duties."
    p "Why even bother with prisoners? You must have so many people begging for work already."
    scene prop5 with mediumdissolve
    ec "Think about it carefully [pname]. Sometimes our company might want people that are more...negotiable when it comes to their morality."
    ec "And prisoners have almost no rights so it gives us high flexibility in how we use them."
    scene prop6 with mediumdissolve
    p "Oh I bet. I wonder if prison here isn't actually better for me than what you might be offering."
    ec "Maybe, maybe not. But consider that I have come here personally to talk to you. Do you think I do this often?"
    p "(Ok, but why me specifically?)"
    scene prop7 with mediumdissolve
    ec "And how the six months goes is all on you and what you make of it. You could honestly end up the luckiest or unluckiest person on Earth with my possible offer, believe me."
    p "But you say possible offer. Not an actual one yet. Why not?"

    scene prop8 with longfade

    stop five fadeout 1

    play two "<from 3 to 22>music/lickelena.mp3"

    ec "Good catch. Yes, I want to see what you are...willing to do to receive my offer. Consider it your first application question."
    ec "No pressure [pname]."
    scene prop9 with superdissolve
    ec "The hard truth for you right now is I could get you out of this prison within two days if you are willing to...please me."
    p "(Shit, I see where this is going.)"
    ec "I just need you to get down on your knees and lick my heels and then move up to my pussy until I get off."
    scene prop10 with mediumdissolve
    ec "A very simple and direct request."
    ec "There are many perks to being one of the top executives at Karlsson, and one of them is having so many chances to enjoy your power."
    ec "So what do you say?"

    menu:
        "(I think I better obey her. I might stay stuck here for five years versus a chance for only six months? How could it be worse than here? Maybe I wouldn't even mind obeying her?) [SubPath]":

            p "Alright."
            ec "Giving in so soon? Is it because of fear or need or because you truly are deep down a pig that wants to serve on the ground..."
            menu:
                "Let her know you feel like you have no choice with her power and your current situation.":
                    $ sub += 1
                    scene prop11 with mediumdissolve
                    p "I feel like I need your help, and I can't imagine refusing you is a good idea."
                    ec "Fair enough, but at least you hold a shred of manhood still. But I imagine bloody knees are in your future at this rate."

                    stop two fadeout 1
                    jump lick
                "I think I want to serve a woman like her. I feel like I want to be dominated by her. Maybe I really am truly more submissive than I realize. [SubPath]":
                    $ sub += 2
                    scene prop12 with mediumdissolve
                    p "I...I think I want to serve you. To please you."
                    ec "Oh [pname], the Karlsson girls are going to just eat you alive. Maybe one will take pity on you like a stray dog though. There's hope with one or maybe even two of them."
                    p "(Why do these girls even matter? This is just a training program?)"
                    stop two fadeout 1
                    jump lick
        "(I don't want to submit, but my position is very weak. But why come all this way to me specifically to NOT give this offer? Maybe she has to offer it. Perhaps I should call her bluff and risk that she offers it anyway. She might respect an intelligent pushback.) [ElenaPath]":

            $ elena_mentor = True
            $ elena_p += 1
            stop two fadeout 1

            play music "music/prop.mp3"

            scene prop13 with longdissolve

            p "With all due respect Ms. Caspari, I don't think you came all this way for nothing. You're too important to waste time on me."
            p "I think for whatever reason I am supposed get an offer and be in this training program no matter what."
            scene prop13b with quickdissolve
            p "If you are forcing me to do what you ask, maybe I can't turn you down as I know my position right now."
            p "But I'm not going to volunteer to be your slave on what I believe is a false choice."
            scene prop14 with mediumdissolve
            ec "That's a big risk for you to turn me down. You don't want to actually please me if you could? I'm not at least a little desirable?"
            p "I'm not blind and I'm a man. But not as a slave if I can help it. If you want a brainless slave, I guess you can just order me on my knees if you want."
            scene prop15 with superdissolve
            ec "Oh [pname] [pname] [pname], of all the responses I anticipated, this one surprises me. I'm very pleased. I'm giving you an A+ on your first application question."
            ec "Who knows, you may even have the potential to win over the strongest Karlsson girl of all. Perhaps there is even some Alexander Karlsson in you."
            scene prop15b with quickdissolve
            p "Wait, who is the strongest Karlsson girl of all? What do you mean by that and why does it even matter about the Karlssons or anything?"
            scene prop16 with mediumdissolve
            ec "No [pname], you have to learn certain things by self-discovery for the greatest impact. It's better that way."
            ec "And, I won't force you to be my cunt licking piggy because of your thoughtful answer. We will have much more to discuss...in better circumstances."
            jump elena
        "(Maybe she wants pure strength and dominance. It's possible no one ever says no to her and she might like some resistance as a sign of a real man versus a pig as she says. Perhaps I should just refuse to submit.) [DomPath]":

            $ dom += 1
            stop two fadeout 1

            scene prop17 with longdissolve
            p "I'm not going to be your little pig as you say and just get on my knees and get you off."
            p "You can just fuck off if you expect me to submit so easily."
            scene prop18 with quickdissolve

            play seven "music/lick.mp3"

            ec "Oh poor poor [pname]. Nothing wrong sometimes with strength and not being submissive, but stupidity is unforgiveable."
            scene prop19 with longflash
            ec "You need to learn your place and what can happen if you make a stupid decision with the wrong person."
            jump punish

label lick:


    play seven "music/lick.mp3"

    scene lick1 with longfade
    ec "Now, time for me to relax. Let me get ready for you. Your poor situation got me very wet..."
    scene lick2 with superfade
    ec "There we go, so comfortable, aren't we? At my age, I'm quite proud of my body."
    ec "I imagine you haven't had many chances to see an elite lady like me, so enjoy the view."
    ec "Lie down like the pig you are and work on my shoes first. I hope you have a strong back [pname]."
    scene lick3 with longfade
    p "ugnnnggghh!"
    ec "My shoes are so nice, aren't they? It would take my entire yard staff over 50 years of their pay to afford this pair. Isn't that funny?"
    p "(Ugh, she's damn tall but so glad she's not a huge fattie.)"
    scene lick3b with mediumdissolve
    ec "You're nothing but a piggy with a tongue right now."
    ec "Maybe I'll train you to suck my heel and you could give my heels a blowjob every day haha!"
    scene lick4 with longfade
    p "(Oh thank God she got off me!)"
    ec "That's not very impressive [pname], don't make me shove my heel all the way in your mouth. Soooo dissapointing piggy."
    ec "Ok [pname], my pussy needs attention. Hmm, I think I want you to lie down on the table. Not my usual standard of luxury for a pussy licking but it will do. Move it."
    scene lick5 with longfade
    ec "Poor [pname], I'd hate to see you stuck here for five whole years. And our guards here are so sadistic and just abuse prisoners."
    ec "Isn't that right Patricia? Mmm, remember when you and I played with poor Timothy? Over four hours..."
    scene lick6 with longfade
    ec "Get to work [pname], I do reward loyalty with pleasure and sometimes power."
    ec "And Patricia is very good at being my bad little girl so she is rewarded with both. You can be too [pname]. I bet you want to play with [pname] don't you Patricia?"
    scene lick7 with longdissolve
    ec "Oh [pname], I've think you've got Patricia very hot and bothered now."
    ec "Maybe I need to give you to her for special...training."
    scene lick7b with mediumdissolve
    ec "I've heard rumors that clients can come here to this jail and just...well...nothing nice."
    ec "I hear some prisoners even disappear forever and fall through the cracks and nobody cares."
    scene lick8 with mediumdissolve
    ec "Of course I don't know annnnnything about that do I Patricia?"
    ec "Mmmmmm, keep licking."
    scene lick9 with longfade
    ec "That's enough, just get deep in there already. I'll let you move a little back on the table for your poor head, haha!"
    scene lick10 with longfade
    ec "Yeeessss, that's good. Young tongues...mmmm"
    ec "I'm feeling merciful right now, what a break for you."
    scene lick11 with longdissolve
    ec "I only need one orgasm right now and luckily for you I can feel it's coming so quickly. Talking about my power is the ultimate aphrodisiac."
    ec "Remember this first lesson. In this world, you are either a slave or a slave owner. Right now, you know what you are."
    scene lick12 with mediumflash
    play audio "audio/slap.mp3"
    ec "*slap* What will you do about it?"
    play audio "audio/slap.mp3"
    ec "*slap* Or do you enjoy being a submissive little pig cunt?"
    scene lick13 with quickflash
    ec "Oh yes, right there, a little more!"
    p "mmfffhmmmmpffhhh!"
    scene lick14 with quickflash
    ec "Fuck yes, almost..."
    scene lick15 with quickflash
    ec "Faster cunt...faster, yes..."
    scene lick16 with longflash
    ec "Yeesssssss! Mmmmmm..."
    scene lick17 with longfade
    ec "Wonderful. Too bad I can't keep you. Now lie on the floor and you can rest there piggie."
    p "(What now...)"
    scene lick17b with longfade
    ec "Good boy. Perfect, down there where you belong."
    p "So is that it?"
    scene lick18 with mediumdissolve
    ec "Well I think you need your reward. You worked so hard to please me."
    ec "Samantha! Level 5 shock please."
    scene lick19 with longdissolve
    $ shock += 1
    if shock >= 2:
        p "*bzzzzzzzzttt* Arrgggghh!"
        p "Why, I did everything you asked!"
        ec "Aww [pname], another shock, I can feel my pussy getting wet again...poor poor [pname]."
    else:
        p "*bzzzztttt* Arrgggghgh!"
        p "Why, I did everything you asked!"
    scene lick20 with mediumdissolve
    ec "You need to know that you are always at the mercy of your superior."
    ec "And with a Mistress like me, I may punish you at any time simply because I enjoy watching you suffer. Even if you do everything perfectly."
    scene lick21 with quickdissolve
    ec "Just because I can."
    ec "Other Mistresses you may deal with could treat you much better, but some could be even worse than I."
    ec "You have no control in this sense. Do you understand?"
    scene lick22 with mediumdissolve
    p "Yes! I got it!"
    ec "I understand...Mistress. Say it like a good little pig."
    p "I understand, Mistress!"
    scene lick23 with mediumdissolve
    ec "Good. Samantha, relieve this poor pig's pain. Now get up."
    ec "Don't forget what I've said. I have little hope you can survive the Karlssons, but it should be fun watching you try."
    scene lick24 with longdissolve
    ec "Take a second to recover [pname], I know it must have hurt quite a bit, but your shocks don't do any long term damage."
    ec "Shocks are a favored disciplinary tool for the Karlssons because it can cause great pain but still preserve the bodies of the bottom feeders for slav..err menial labor."
    ec "Now, I am a woman of my word about the offer. Let me just freshen up again and get my clothes and chair, hehe...sit back down please [pname]."

    stop seven fadeout 3

    jump testchoice1

label elena:
    scene elena1 with superfade
    ec "You have impressed me enough to make me consider mentoring you. But a clever answer or two is not enough. I need to see more."
    ec "With my help, you would undoubtedly have a much better chance to gain power versus barely struggling to survive, but you have a long way to go."
    scene elena2 with quickdissolve
    ec "And it has to benefit me. I need to know I have your complete loyalty as an ally, and I will test you on that soon."
    ec "And don't forget I have a very powerful ally above me, and she intends to win her own situation so to speak."
    ec "We will see what happens, but let's finally get to your offer, and yes, you were going to receive it all along. Kudos to you on that [pname]."
    jump testchoice1

label punish:
    scene punish1 with longflash
    ec "Samantha! Level 3 shock our defiant guest here!"
    scene punish2 with quickdissolve
    $ shock += 1
    if shock >= 2:
        ec "Oh dear, shocked again [pname], hurts doesn't it?"
        ec "Poor baby."
    else:
        p "*bzzzzzttttt* Oh my!....unnngggghhh!"
        ec "Hurts a bit, doesn't it [pname]?"
    scene punish3 with longdissolve
    ec "I appreciate and even admire the desire to not submit, but to outright refuse someone in my position without good reason is incredibly stupid."
    ec "You better learn to use your brain and learn how and to whom you can refuse things if you hope to get anywhere with the Karlsson Group."
    scene punish4 with mediumdissolve
    p "Yeah, I think I get the fuckin' point!"
    ec "I can dominate and control almost anyone I want, but even I must bend my knee to my one true Mistress at the top of everyone."
    scene punish5 with mediumdissolve
    ec "If I did to her what you just did to me, I would suffer far far worse pain than you right now."
    p "(I wish I was her right now so I could...)"
    scene punish6 with longdissolve
    ec "So learn to know when to fight, and when to survive. This is the game of power."
    ec "Believe it or not, I want to help you if you don't want to be a slave, but I can't if you are a fool."
    scene punish6b with mediumdissolve
    ec "Now learn to play the game and get off that chair and grovel at my feet for a short time to avoid being a pig forever."
    ec "Show me you can think."

    menu:
        "Grovel at her feet.":
            scene punish7 with longfade
            ec "Good [pname]. This is a start."
            ec "You can stop now, I have no desire to make you submit longer than you have to...I don't need another mindless slave."
            ec "Samantha, that's enough for poor [pname]."
            scene punish7b with longfade
            p "(Ugh...)"
            ec "Now, let's conclude our business for today. Back on the chair you go."

            stop seven fadeout 3

            jump testchoice1
        "Refuse to grovel. [DomPath] [ElenaPath] [Shock]":
            $ shock +=1
            $ dom +=1
            $ elena_p -=1
            scene punish8 with longdissolve
            p "No!"
            ec "*sighs* So stubborn [pname]. Samantha! Level 7 shock him!"
            scene punish9 with mediumflash
            if shock >= 2:
                ec "Another shock [pname], are you a glutton for pain?"
                p "Holy shit! Arrrgghh!"
                ec "Foolishness will only get you killed [pname]."
            else:
                p "Holy shit! Arrrrrghgghghgh!"
                ec "Foolish bravado will get you killed [pname]."
            scene punish10 with mediumdissolve
            ec "If you won't use your brain, you will be forced to submit by extreme force like a true animal in a cage."
            ec "Don't get yourself in this kind of position again."
            scene punish11 with quickdissolve
            p "That's too much...nggggh stop it..."
            ec "Samantha! That's enough."
            scene punish12 with mediumdissolve
            ec "I hope you can learn from this [pname] or you won't last long. If you want true power, be patient and calculating."
            ec "Now, let's conclude our business here today."

            stop seven fadeout 3

            jump testchoice1


label testchoice1:
    scene tc1 with longfade

    stop music fadeout 1

    play seven "music/samvisit.mp3"

    ec "Now [pname], I'm officially giving you an offer to participate in our corporate inmate training program."
    ec "I will be giving you some basic information on the program and also The Karlsson Group itself."
    scene tc2 with mediumdissolve
    ec "I expect you to learn everything in it over the next two days."
    ec "After those two days, you will be transported to one of our corporate locations to be assigned work."
    scene tc3 with mediumdissolve
    ec "I also want you to fill out a very basic psych test to help us understand a little more about you beyond what your file says."
    p "Alright."
    scene tc4 with mediumdissolve
    ec "Now I have to run soon so I need an answer."
    ec "Do you accept my offer?"
    scene tc5 with mediumdissolve
    p "Yes."
    ec "Good. I look forward to everything."
    jump testchoice2

label testchoice2:
    scene tcc1 with longdissolve
    ec "Oh, one last thing..."
    ec "A good faith gesture to you for accepting our offer."
    if bad_joke:
        ec "While I appreciated your sarcastic joke on this, I do know how you got your bruises."
        ec "A prisoner ambushing you is not amusing to me at all. Especially since he had a makeshift weapon, making it an unfair surprise attack."
    else:
        ec "I am well aware how you got your bruises. A prisoner ambushing you is not amusing to me at all, especially since he had a makeshift weapon."
    scene tcc1-2 with mediumdissolve
    ec "I also know it's Prisoner 912, and I'm going to let you decide how you want justice for your injuries."
    ec "You are now valuable Karlsson property, and Prisoner 912 is beneath you, so he is at your mercy."
    ec "Let's call this your next application question, and first executive decision."
    ec "How should this prisoner be disciplined for his actions?"
    scene tcc1-3 with mediumdissolve
    ec "On paper, his standard punishment for an attack like this would be two weeks in solitary."
    ec "But of course I have the power to allow almost any...discipline you like."

    menu:
        "Give him a lesser punishment of one week in solitary. [GoodPath]":
            $ good += 2
            scene tcc2 with mediumdissolve
            p "Just one week of solitary is enough."
            ec "Very merciful. How generous of you [pname]."
            ec "I will make sure it is done as you instructed."
            stop music fadeout 1
            jump elenadone
        "Give him the standard two weeks of solitary.":
            scene tcc2 with mediumdissolve
            p "I think the standard two weeks of solitary is very appropriate."
            ec "Very by the book [pname]. Not always a bad thing either."
            ec "I will ensure he is disciplined accordingly."
            stop music fadeout 1
            jump elenadone
        "Give him a more severe punishment beyond two weeks of solitary. [EvilPath]":
            scene tcc3 with mediumdissolve
            p "I don't think two weeks of solitary is enough. What else can I do?"
            ec "For more serious infractions, we do two weeks or longer of solitary but..."
            ec "...Patricia can be called to...personally administer further punishments."
            scene tcc4 with mediumdissolve
            ec "The prisoner could suffer great pain, but no permanent damage."
            ec "There is even one more option I can offer you."
            p "What's that?"
            scene tcc5 with mediumdissolve

            stop seven fadeout 1

            play eight "<from 1 to 40>music/samantha.mp3"

            ec "Samantha. But [pname], be aware she is very brutal."
            ec "Prisoner 912 would likely suffer...permanent damage."
            ec "But I am giving you virtually unlimited power to decide his fate. It's up to you."

            menu:
                "Have Patricia discipline the prisoner. [PatriciaPath]":
                    $ patpunish = True
                    $ evil += 1
                    stop eight fadeout 1
                    scene tcc6 with mediumdissolve
                    p "Have Patricia punish him."
                    ec "I will make sure it is done as you desire [pname]."
                    scene tcc7 with longdissolve
                    $ pat_p += 1
                    ec "And I think you made a new friend in Patricia."
                    jump elenadone
                "Have Samantha discipline the prisoner. (warning: very evil choice more extreme content later) [EvilPath]":
                    $ samsadist = True
                    $ evil += 3
                    scene tcc8 with mediumdissolve
                    p "Fuck him. Samantha."
                    ec "I see [pname]."
                    scene tcc9 with mediumdissolve
                    ec "I am pleased you show no mercy but I hope you didn't do it for a purely emotional reason."
                    ec "But we can speak on this later."
                    stop eight fadeout 2
                    jump elenadone

label elenadone:

    play seven "music/samvisit.mp3"

    scene elenadone1 with longfade
    ec "Patricia, ensure that Prisoner 912's punishment is administered soon."
    pp "I will do as you command, Miss Caspari."
    ec "Good girl."
    scene elenadone2 with mediumdissolve
    ec "And cover [pname]'s face bruises immediately after I leave with makeup and make sure they heal quickly, it's an eyesore."
    ec "And get him a decent shirt for goodness' sake! Fix his hair too, everything. He needs to clean up well Patricia."
    ec "Also make sure he can read everything I give him on a computer and that he is ready in two days."
    scene elenadone3 with mediumdissolve
    ec "Oh one last thing. Take off his shock collar for now. I trust you will behave [pname]?"
    ec "Anyway, I look forward to seeing what you can do."
    if elena_mentor:
        scene elenadone4 with longdissolve
        ec "I'll be calling on you soon to get to know you a little better...in private."
    else:
        ec "I am sure we shall meet again soon."

    stop seven fadeout 2
    jump sisters1

label sisters1:

    play five "<from 1 to 136>music/meeting0.mp3" fadein 1

    scene ship1 with superfade
    j "(......)"
    scene ship2 with longdissolve
    j "(What's taking so long?)"
    scene ship3 with mediumdissolve
    j "(It's so hard to rely on decent help...)"
    scene ship4 with mediumdissolve
    j "Ah, there you are Dumbo. We need to call Dominique real quick."
    j "This one looks a little too well fed and strong. What number is he?"
    scene ship5 with mediumdissolve
    db "Nnnnnuubbbbbmbbmerrrr.....nnnniinnnneee....Mmmmmisssstrrrressss."
    j "Oh Dumbo. Your brain is truly mush now isn't it? Maybe I injected too much into you?"
    j "But luckily I don't need you to talk much, do I?"
    scene ship6 with mediumdissolve
    j "Maybe this footstool will do. Bring him here and dial up my sister."
    j "You just have to press the button 3 on the phone and then the phone button. Can you manage that Dumbo?"
    db "Yyyyeeeeessssssss....Mmmmmmmmissstreeeessssssssss."
    scene ship7 with quickdissolve
    j "Let's see if my voice activiation works on this dick collar...Dick Shock 3!"
    fs9 "Ughhhh!"
    j "Good! Now number 9 was it? You need to stay perfectly still so I can relax my feet while I talk."
    j "If you don't, I'm going to increase the shock higher and higher."
    scene ship8 with mediumdissolve
    j "(At least he can still use a phone hee hee)"
    d "Yes, Julie? I was about to leave for a meeting so let's make it quick."
    j "I want an update. What is happening?"
    scene office1 with mediumfade
    d "Elena is meeting him today. He should be available within two or three days I imagine."
    j "And what is he like? Who are we dealing with?"
    d "I don't know yet. I trust Elena to give us a good first impression in her report."
    scene ship9 with mediumdissolve
    j "And the brother and sister?"
    d "Veronica suggested sending Alessandra to meet the sister personally. I agree with that idea."
    j "I do too. Alessandra is perfect."
    scene office2 with mediumdissolve
    d "You know the problems with his brother. I think we should wait for Elena's feedback on this one."
    j "Ok. By the way, do we know if he realizes that his brother..."
    d "I don't think he knows from Veronica's reports, but we shall see."
    scene ship10 with mediumdissolve
    d "Julie! I can hear one of your toys whining, can you curtail your sadistic kinks until we are done?"
    j "Ok, ok, always so serious Dominique. I really think you need a good fuck to relax you."
    j "You better calm down little stool, you don't want my sister mad at you."
    fs9 "uggggghhhhh"
    scene office3 with mediumdissolve
    d "Veronica is back from Africa in about three days. The mine collapse issue should be resolved then."
    d "And you are back in two days?"
    j "Yes."
    scene office4 with quickdissolve
    d "Ok great. I'm back in one day. I'm at the West Coast estate right now. All four of us should meet soon and go from there."
    j "Let's send Alessandra now and bring the sister into the game."
    d "This is not a game Julie. This is serious business."
    scene ship11 with mediumdissolve
    j "Oh yes yes, of course. Daddy couldn't make it easy for us, could he?"
    d "Did you expect any different?"
    j "No. I guess not."
    scene office5 with mediumdissolve
    j "You know he wouldn't be pulling this bullshit if we weren't all female."
    j "His poor sperm couldn't make a son, I bet that pissed him off, four girls haha!"
    d "Maybe. It doesn't matter, we have to do what we have to do."
    scene ship12 with mediumdissolve
    j "But we agree on the sister?"
    d "Yes. I'll talk to Alessandra."
    scene ship13 with quickdissolve
    d "By the way, how did it go for you?"
    j "I processed over 200, so it was a pretty good batch."
    scene office6 with mediumdissolve
    d "Ok. I've got to finalize the right plan and program for him for everyone to review. See you in a few sis."
    j "Bye bye Dominique and let me at him first!"

    stop five fadeout 3

    play music "music/death1.mp3"

    scene ship14 with longfade
    j "Put the phone away Dumbo. Dick Shock 6!"
    fs9 "Arrggghhh!"
    db "Yyessss....Mmm"
    j "Uh uh, just stop talking for now ssssslllllooowwwww bbbbboooyyy oh Dumbo so so dumb now. Poor baby..."
    scene ship15 with longdissolve
    j "What I am going to do with you Footstool number who cares."
    j "Put on my heels now quickly and maybe I'll stop your pain."
    scene ship16 with longdissolve
    j "Thank you! Let's test my heels, haha!"
    fs9 "Oh my God, Nooooo please!"
    j "Oh, I can feel your dick vibrating on my shoe, maybe your little weenie cock could actually feel good in a woman's pussy vibrating like that!"
    scene ship17 with mediumdissolve
    j "Dumbo, I'm a little dissapointed with this one. He doesn't scream well enough. I think I need a new one."
    j "How many more footstools do I have in my cage right now?"
    scene ship18 with longdissolve
    db "Ttttttweeennnnnnnttttyyy......Mmmmmmmmmiiisssssttttrreeeesss."
    j "Oh you can still count to 20? How precious. Now, I think this stool is broken. He looks so hot from the sun too."
    j "I think he needs to cool off in the water. Please pick him up Dumbo."
    scene ship20 with mediumdissolve
    j "Oh but servants can't use my pool of course."
    j "I have an idea, we have the best pool right outside the ship!"
    scene ship21 with longdissolve
    fs9 "Ugh, no no no!"
    j "I usually love hearing last minute begging, but I'm bored of you."
    j "Please throw him overboard so he can cool off!"
    scene ship22 with longdissolve
    fs9 "Noooooooooooooooooo!"
    scene ship23 with longdissolve
    j "Good job Dumbo."
    j "Now I want you to get two more footstools for me. And I want the two shortest and skinniest looking ones you can find."
    j "I want them very weak and their hands and feet chained tightly because I need some physical exercise now."
    scene ship24 with mediumdissolve
    j "And I'm going to be very...very...thirsty after using them, so I will need you ready to please me."
    j "Now go and do as I say."
    db "Yyyeeeeeesssss....Miiissssstrreeeesss"
    scene ship25 with mediumdissolve
    j "(I really hope he's a man I can have some fun with...)"

    stop music fadeout 3

label sisters2:

    play five "music/dominiqueintro.mp3"

    scene office7 with longfade
    jk "(Please please work)"
    scene office7b with longdissolve
    jk "My Lady, may I ask a favor?"
    d "What is it Junko?"
    scene office8 with mediumdissolve
    jk "Sorry, my Lady. My father actually has two days off next week for the first time in years. I would like to see him if possible."
    d "You know how it can look if I show leniency as a Karlsson. Especially right now."
    jk "I know, my Lady. But I haven't seen him in four years, and you know I have never asked for anything."
    scene office9 with mediumdissolve
    jk "Don't I serve you very well? I do anything you ask, and never cause trouble."
    d "You do. One of my most trusted servants. But I can't let you run off on your own right now."
    scene office9b with longflash
    jk "Please my Lady, I beg of you, I do everything you ask of me..."
    d "Very well Junko, I have an idea about what I can do for you."
    scene office10 with mediumdissolve
    d "I can arrange to bring your father to our corporate headquarters for two days next week. I can also procure a quiet location for you two to stay there."
    d "I can say you are both working on a special project for me. I can even have some luxury meals delivered to you. What a rare treat for you both I imagine."
    scene office11 with mediumdissolve
    jk "Oh thank you my Lady! I am so lucky to be serving you!"
    d "If you obey me well, I can be generous and kind. But privately. I have to keep up appearances you know."
    jk "I understand, my Lady, I will make sure no one ever knows!"
    scene office12 with mediumdissolve
    d "Don't forget your father too. If he advertises my kindness, you realize I might have to have him killed."
    jk "I...I understand my Lady. I will make sure he obeys you too."
    scene office13 with longdissolve
    d "Now then, my sister actually did for her a rare thing and said something wise to me earlier about needing to relax."
    d "I think my meeting can wait a little. Come help me relax in the nice sun here a bit."
    jk "Right away my Lady..."
    scene office14 with longdissolve
    jk "I hope I can please you my Lady."
    d "I am sure you will be adequate."
    scene office15 with longdissolve
    d "Use both your fingers and tongue like you've been trained."
    d "Ahhhhh, there we go, good job Junko..."

    stop five fadeout 2
    jump reading

label reading:

    scene black with longfade

    pp2 "*over intercom* Oh boys, enjoy some relaxing reading music!"

    play five "music/readingtune.mp3" fadein 2

    scene reading1 with longfade
    p "(What the hell is this elevator shit??...trying to sedate us apparently)"
    p "(Well, let's get to it, a brief summary of The Karlsson Group, here we go...)"
    cs "{i} The Karlsson Group famously came to riches by the machinations of its founding CEO, Alexander Karlsson.{/i}"
    cs "{i} Karlsson successfully accumulated much of the newly rare fertile lands for food and water mere months before the Great Collapse and the planet's environmental catastrophe.{/i}"
    scene reading2 with quickdissolve
    p "(Yeah, no shit. Common knowledge.)"
    cs "{i} The Karlsson Group also skirted numerous ethical and legal dilemmas as constant rumors swirled about the nefarious activites of the company.{/i}"
    cs "{i} These included rumors of an illegal slave market, arms dealing, slave level labor, unethical medical research, and deliberate destruction of food and water to drive artificial demand.{/i}"
    scene reading3 with quickdissolve
    cs "{i} It is unknown but commonly believed that Alexander Karlsson was the richest person in the world before his death about three and a half months ago.{/i}"
    cs "{i} His death was actually kept secret for over a month before it was announced to the world.{/i}"
    p "(Wait, he's dead? Thanks, prison. Always good to be in the loop, and who's running the show now?)"
    cs "{i} Karlsson left behind four daughters that help run the Karlsson Group.{/i}"
    p "(Ok, here we go...)"
    scene reading4 with mediumdissolve
    cs "{i} These four daughters were products of Alexander Karlsson's famous Karlsson Gambit, in which he sought out the most beautiful and smartest women to sire his future children.{/i}"
    cs "{i} The details of what happened are cloaked in secrecy, but it is now known that he attempted to sire children with a select number of women to carry on his name and legacy.{/i}"
    cs "{i} The current succession and inheritance plan of how the company will be divided amongst his four daughters is unknown, but for now the company is being run by the Executive Council.{/i}"
    p "(This won't be hard to remember so far, this was written for a high school kid or something.)"
    cs "{i} The Executive Council is composed of seven members, but for purposes of this briefing, the duties of the four daughters are of note.{/i}"
    p "(I heard Patricia say Elena was on this Council? So that's five of seven counting his daughters right there?)"
    scene reading5 with quickdissolve
    cs "{i} The Chief Financial Officer of The Karlsson Group is Alessandra Karlsson. She is supposedly a mathematical genius with an amazing faculty for finances and numbers.{/i}"
    cs "{i} She manages the entire array of assets and investments and all other financial aspects of The Karlsson Group.{/i}"
    p "(Pfft. No pictures. I'm curious how they look. Supposed to be beautiful and smart mothers and all...so daughters are maybe hot too?)"
    cs "{i} The Chief of Business Operations for the Karlsson Group is Dominique Karlsson. She is said to have inherited her father's charisma and leadership qualities.{/i}"
    cs "{i} Dominique runs all operations of the company outside of the Research Division and is rumored to be the favorite to inherit the bulk of her father's empire.{/i}"
    cs "{i} These operations include all mining, manufacturing, arms, and other day to day operations of the company.{/i}"
    scene reading6 with quickdissolve
    p "(What, no operations in making childrens' dreams come true? Shocker.)"
    cs "{i} The Chief of Research and Design for the Karlsson Group is Veronica Karlsson. She runs all research and design in medicine, weapons, products, and other unknown areas.{/i}"
    cs "{i} It's also known that she runs the Karlsson prisons and spy networks.{/i}"
    cs "{i} She is rumored to be the personal protector of Dominique Karlsson under secret orders of her father, only adding more fuel to rumors of how the company will change hands.{/i}"
    cs "{i} The Chief of Revenue, Sales, and Marketing for the Karlsson Group is Juliette Karlsson. She famously is as ruthless as her father.{/i}"
    cs "{i} Juliette is responsible for generating revenue and doing sales and marketing for all Karlsson activities, and is known as a master of producing revenue efficiently and maximizing profit.{/i}"
    cs "{i} She is rumored to be the other main candidate to inherit the bulk of the Karlsson empire.{/i}"
    scene reading7 with longdissolve
    p "(Ah, that's enough for now, sounds like such a lovely family. I need to stretch and loosen up, walk a bit maybe.)"
    p "(What the hell am I getting into? Why keep mentioning these girls this way?)"
    scene reading8 with longdissolve
    p "(Not sure why they let me read in here of all places. Wonder if there is any juicy information in these boxes.)"
    p "(Wait! I heard a cough, someone else is in here.)"
    scene reading9 with longdissolve
    p "(Are you fucking kidding me?? This can't be a coincidence!!)"
    p "(It's...)"


    python:
        pname2 = renpy.input("My best friend's first name is...(just type and press Enter)")
        pname2 = pname2.strip()

        if not pname2:
            pname2 = "Jake"

    python:
        pname_f2 = renpy.input("My best friend's last name is...")
        pname_f2 = pname_f2.strip()

        if not pname_f2:
            pname_f2 = "Robertson"

    scene reading10 with mediumdissolve
    p "...[pname2]!"
    scene friend1 with longdissolve
    pbf "[pname]? What the? Wow!"
    p "It's good to see you!"
    pbf "Same my man. What are the odds right?"
    scene friend2 with longdissolve
    p "Not an accident obviously..."
    pbf "Hey, no collar for you? Every prisoner I've seen has one."
    p "I had one before, but they took it off."
    pbf "Alright [pname], who did you blow to get that taken off? Sexy hair and beard too."
    scene friend3 with quickdissolve
    p "Fuck you man, haha! But...damn good to see you, how did you end up here?"
    scene friend3b with quickdissolve
    pbf "I swear to you [pname], on my mother's soul, that I'm innocent."
    pbf "Two cops stop my car randomly, and my trunk has got some high tech stolen shit inside. I didn't put it there!"
    scene friend4 with quickdissolve
    p "Frame job it seems...How long are you supposed to be here?"
    pbf "2 years, but then I got offered some training program to get out of here within six months."
    p "Ah, so you got that six month offer too? Me too, how was dealing with Elena?"
    pbf "Who's that? *starts to whisper* She is probably listening, but I talked to this chick Samantha."
    scene friend5 with quickdissolve
    p "Oh. Her. Yeah, she's definitely watching me for sure on camera a lot."
    p "I'll keep my voice down too. Sounds like a lot of prisoners are scared of her."
    scene friend6 with quickdissolve
    pbf "She looks like a sweet girl but something about her freaks me out."
    scene friend7 with quickdissolve
    p "How long have you been here?"
    pbf "About two months, a month after I got pinched I was sent here."
    p "Almost the exact same for me. About three months from arrest until now."
    p "Ok, we gotta assume that both of us happening to meet like this and being in the same situation was planned for a reason. Probably not a good one."
    scene friend8 with quickdissolve
    pbf "Yeah, but why? Who the fuck cares about two nobodies like us?"
    p "I don't know, but I hope we manage to be together in whatever shitstorm that comes our way."
    p "Nice to know that we can help each other cover our collective asses with whatever is coming."
    scene friend9 with quickdissolve
    pbf "You know it, bro. I got you."
    pbf "Bro and sis ok? I mean how could they arrest him in his condition...sorry man, just thinking out loud and my stupid mouth..."
    scene friend10 with quickdissolve
    p "It's ok. I don't think their situation has changed, but I can't be sure being stuck in here."
    p "I have a feeling the woman I met for the training offer would have used them against me more if their situation was worse."
    pbf "Sounds like a bitch. Another guard or even the Warden?"
    p "No, some corporate lawyer way up in the company, but she didn't meet with you, so I wonder why she met with me specifically."
    scene friend11 with quickdissolve
    p "How about your cell? What is it like?"
    pbf "I've got two cellmates, but I hear most are cramped in packs of ten or more in much smaller cells, so I'm not complaining."
    p "Ok. I somehow am alone in a cell, so that might be important. Plus I met Elena and maybe nobody else did."
    scene friend12 with quickdissolve
    pbf "Mr. VIP I guess. Hope it helps us somehow."
    p "Me too. Let's just make sure we share what we can, and protect ourselves as best as possible...I have a feeling that..."

    scene friend12b with quickdissolve
    pp2 "*over intercom* Oh [pname]! That's enough of a reunion for now!"

    stop five fadeout 2

    pp2 "I need you to finish up and come and see me at Chamber 6A, it's a huge room down the hall all the way to your right when you exit!"
    pp2 "The guard at the main security door will let you through into the guards' area. Then the last door down that corridor on the left. See you soon!"
    scene friend13 with longdissolve
    p "Oh great...well at least she spared us anymore of that repetitive music I suppose..."
    pbf "She was sweet to me, but I met her only for the training offer and then one more time she just cut my hair and shit. Be careful."
    pbf "I bet's she's scary to so many for a good reason."
    scene friend13b with quickdissolve
    p "Ok. I don't know how we'll meet again, but I have a feeling there is a grand plan behind this that involves both of us..."
    p "...so I am pretty confident we'll be in this together somehow. I guess it could be worse."
    scene friend14 with longdissolve
    pbf "Going through hell with a friend is better than a solo trip. We'll figure it out, and you better not keep her waiting."
    p "Yeah. Watch your back [pname2]."
    pbf "You too [pname]."
    jump sam

label sam:

    play seven "<from 1 to 92>music/samintro.mp3" fadein 2

    scene sam1 with longfade
    pp2 "Why hello there [pname], nice to actually see you in the flesh for once!"
    pp2 "A monitor doesn't do you justice. Very few prisoners are worth looking at, but I feel differently about you."
    p "Err, glad to hear it."
    scene sam1b with mediumdissolve
    pp2 "This room is where we put prisoners to death for serious crimes. I'm the one that has the sad task of executing them."
    p "(She doesn't sound very sad about it at all) I see."
    pp2 "It's off limits to anyone but a few select guards and the Warden, so we can often have privacy here."
    scene sam2 with longdissolve
    p "And, this doesn't seem like a guard uniform? Seems very out of place with this prison."
    pp2 "Hah! No, behind the guard doors away from the prisoner wing, we can all dress more casual and relax and enjoy ourselves."
    pp2 "We are such a good work environment, guards just love working here."
    scene sam3 with mediumdissolve
    pp2 "You seem a little nervous. Don't worry [pname], I'm just a harmless sweet thing, right?"
    pp2 "I'm like a tiny button in the background that just helps prisoners behave better in little ways here."
    pp2 "After all, so many of them are dangerous, aren't they? You got attacked by one!"
    if samsadist:
        pp2 "I'm SO happy and excited you chose me to punish your attacker, I promise I will make him regret touching you."
        scene sam4 with mediumdissolve
        pp2 "I can be as quick or as...slow with his punishment as you want, [pname]. And we do special punishments in the guard area...off the record."
        pp2 "I like to think I am very good at making men scream with either pleasure or pain."
        pp2 "I hope I can give you the former and him the latter."
        scene sam5 with mediumdissolve
        pp2 "Elena has asked me to make sure you observe some of his punishment."
        pp2 "She wants you to learn the reach and results of the power of your decisions as you make them."
        jump samcont
    elif patpunish:
        scene sam6 with mediumdissolve
        pp2 "I'm so sad you didn't pick me to punish Prisoner 912, but Patty should still be fun."
        pp2 "She's not exactly sweet, but you should have picked me [pname]."
        scene sam5 with quickdissolve
        pp2 "But anyway, Elena has asked me to make sure you observe some of his punishment."
        pp2 "She wants to you to always know the results of your decisions when possible."
        jump samcont
    else:
        scene sam5 with mediumdissolve
        pp2 "Elena has asked me to make sure you observe the solitary confinement of Prisoner 912."
        pp2 "She wants you to understand the power of your decisions as you make them."
        jump samcont

label samcont:
    scene sam7 with longdissolve
    pp2 "Let's also talk about one last little thing while we wait for Pat to arrive."
    pp2 "Elena has another application question for you as she calls it."
    scene sam8 with mediumdissolve
    pp2 "I know you haven't been eating great food here, and Elena is offering you a simple choice."
    pp2 "You can get the delicious food we guards eat for the rest of your stay here...or you can share your good fortune with your friend [pname2] or twenty other prisoners."
    pp2 "But if you share the food, you won't get any for yourself."
    p "(What the?)"
    scene sam9 with mediumdissolve
    pp2 "Elena is just messing with you at this point [pname]! So what's it going to be?"
    menu:
        "Give the food to 20 prisoners. [GoodPath]":
            $ good += 2
            scene sam10 with mediumdissolve
            p "I'll share my good fortune with twenty prisoners."
            pp2 "Wow, so generous to give up your own comfort to help twenty people! I'm surprised!"
            pp2 "I think you should take care of your own needs first, but I'm still amazed you did it."
            jump patarrives
        "Give the food to [pname2]. [FriendPath]":
            $ good += 1
            $ friend += 1
            scene sam10 with mediumdissolve
            p "I have to give the food to [pname2], he'd do the same for me."
            pp2 "So sweet of you to help your friend, I do hope he would do the same for you."
            p "He would."
            pp2 "Good for you [pname], it's hard to trust anyone in this world. But don't assume that can't change someday."
            jump patarrives
        "Keep the food for yourself. [EvilPath]":
            $ evil += 1
            $ selfisheater = True
            scene sam10 with mediumdissolve
            p "I'm keeping the food for myself."
            pp2 "Oh [pname], that's so selfish of you. Getting to eat so well while your friend or even twenty people still have to eat garbage like rats."
            scene sam11 with mediumdissolve
            pp2 "*whispering* But I have to admit to you a secret confession."
            pp2 "My food is so much more delicious when I eat, as I imagine those underneath me eating almost literal shit."
            pp2 "It makes me all tingly inside. Is your food going to taste that much better for you too [pname]?"
            jump patarrives

label patarrives:

    scene pat1 with longfade
    pp2 "Patty! You are finally here! Glad you could get off duty, but you are a tad late!"
    pp "I had to grab him you know."
    pp2 "Oh yes, I forgot!"
    pp2 "But I have to fix one thing bothering me before we see your attacker! I can't fix your hair yet [pname], but that beard has to go right now!"
    pp "Good idea, let's go!"

    stop seven fadeout 2

    jump fork

label fork:

    if samsadist:
        jump sampunish
    elif patpunish:
        jump patpunish
    else:
        jump solitary

label solitary:

    play seven "<from 1 to 68>music/solitary.mp3" fadein 2

    scene solitary1 with longfade
    pp2 "Ah, here we are [pname]. This is one area we place prisoners on solitary."
    pp2 "We also put in some nice little perks for ourselves in here so we can enjoy discipling prisoners."
    p "(A jacuzzi in here? A bed too? Really?)"
    scene solitary1b with longfade
    pp2 "Without the proper punishments, we can't ensure good behavior in here, can we? Ah, Prisoner 912."
    p1 "Please...please..."
    pp2 "He looks so sad and broken [pname], maybe your punishment is mentally damaging him."
    pp "Aww, I want to see him cry!"
    scene solitary1c with mediumdissolve
    pp2 "Oh! Patty, be a dear and quickly feed the prisoners in my new cage some slop and then come back. It's on the other side of the basement, I just got it yesterday!"
    pp "More prisoners down here? You have too much fun without me Sam!"
    scene solitary2 with mediumdissolve
    pp2 "So pathetic. Oh [pname], he's not special like you without a collar. We use a special chip we inject in their neck for shock control."
    pp2 "The chips are quite expensive so it's a very special privilege for this level of prisoner or lower as it hurts a lot more, haha!"
    p1 "You...terrible...bitches..."
    p "(I didn't realize solitary was like this...)"
    menu:
        "Try and lessen the punishment and object to this kind of cage. [GoodPath]":
            $ good += 1
            scene solitary3 with mediumdissolve
            p "I had no idea this was solitary. I thought it would be a small cell maybe, but nothing like this."
            p "This seems a little too much. How can he even sleep or shit?"
            scene solitary4 with mediumdissolve
            pp2 "The poor thing has to manage somehow, but this is the punishment for 912."
            pp2 "Elena taught me so well that the anticipation of something is often as fun as what you actually do. Look how pitiful he looks. So sad!"
            jump solitarytwo
        "Don't object to the cage.":
            jump solitarytwo

label solitarytwo:

    if sub >= 3:
        scene solitary5 with longfade
        pp2 "Now [pname], we both know you are a little subbie, so I want to relax."
        pp2 "Lie down on the bed. But you need to angle your body so I can see the cage directly. It's so nice you can rest your back on a real mattress, right?"
        pp2 "Then be a sweet little pet and lick me."
        scene solitary6 with longfade
        pp2 "Oh, I don't need my panties do I? Do you see how soaked it is [pname]? I'm so excited even with your poor choice of punishment!"
        pp2 "Patty!!! Hurry back over here and come up here too and play with [pname]'s dick a little to encourage him to lick me better."
        pp "Of course Sam!"
        scene solitary7 with longfade
        pp2 "Be gentle with him Patty so he can concentrate on me."
        pp2 "Now 912, you need to apologize to [pname] for attacking him and beg for his forgiveness."
        p "(Holy...she is so wet down here.)"
        scene solitary7b with mediumdissolve
        pp2 "Now...poor little prison rat, you're going to be stuck here for such a long time. So terrible isn't it..."
        p1 "You won't change anything...you're just a bitch."
        pp "He's still not crying. I wish I could have punished him."
        pp2 "Me too. Oh, you are so lucky [pname] didn't choose for me to punish you because you would really, really, regret what you just said."
        scene solitary8 with mediumdissolve
        pp2 "But that's ok, just looking at your pathetic face in that cage is enough for me."
        pp2 "Just looking at you and I'm already so close. Knowing how long you are going to have to just sit there like a caged rat."
        scene solitary9 with mediumdissolve
        pp "I'm so jealous at how fast and often you can orgasm Sam!"
        pp2 "Thanks, oh don't get him too excited with your foot, he has to earn a bonus by being a good little sub for me."
        pp "That's hard to do, just like him right now, haha!"
        scene solitary9b with mediumdissolve
        pp2 "[pname], if you cum without my permission, I'm going to have you...whipped."
        pp "Oh, I want to get him off now!"
        scene solitary10 with mediumdissolve
        pp2 "So close already..."
        scene solitary10b with mediumdissolve
        pp2 "Maybe you'll just rot away in there 912..."
        scene solitary10c with mediumdissolve
        pp2 "Oh yes!...poor poor baby, nothing but a rat...stuck...all alone."
        scene solitary11 with mediumdissolve
        pp2 "Oh 912...I've decided to leave you in that cage for an extra two months."
        scene solitary11b with quickflash
        p1 "What? You fucking! No!"
        scene solitary12 with longflash
        pp2 "Oh yessssss! That's all I needed."
        scene solitary12b with longfade
        pp2 "Ah, Patty, he was actually pretty good at pussy licking, you need to try him too!"
        pp "I hope to soon!"
        pp2 "Thank you [pname] for helping me, maybe later I'll give you a little treat."
        scene solitary13 with mediumdissolve
        pp2 "Patty, take [pname] back to his cell!"
        pp "Oh no, I think he was hoping for something right now! Haha!"
        pp2 "He needs to work a little harder to get anything even close to real pleasure from us. The poor two men in here, hahaha!"
        scene solitary13b with longfade
        pp2 "Oh, before I forget little 912, enjoy my little spikes and rotting in your little cage!"
        p1 "Ouch! Errghhh..."

        stop seven fadeout 2

        jump aftermath
    else:

        scene solitary14 with longdissolve
        pp2 "Prisoner 912! Your attack on this poor boy is what got you in there!"
        pp2 "I think you need to apologize to him and beg for his forgiveness."
        scene solitary15 with mediumdissolve
        p1 "You won't change anything, you're just a bitch."
        pp2 "Oh, you are so lucky [pname] didn't let me punish you because you would really, really, regret what you just said."
        scene solitary16 with mediumdissolve
        pp2 "Unfortunately [pname], you didn't let me or Pat punish him directly, so we can't give you a great show!"
        pp2 "I'm so sad! But maybe you don't need or want to see our cruelty, do you?"
        pp2 "Patty, take [pname] back to his cell for now."
        scene solitary13b with longdissolve
        pp2 "Oh, enjoy my little spikes and rotting in your little cage, 912!"
        p1 "Ouch! Errggghh..."

        stop seven fadeout 2

        jump aftermath

label patpunish:

    scene pat1a with longfade

    play seven "music/pattest2.mp3"

    pp2 "Ah, here we are [pname], your attacker is waiting for you. I love this room, so many good memories here."
    pp2 "I can't wait to see you have some fun, Patty!"
    p "(A jacuzzi in here? A bed? Really?)"
    scene pat1b with longfade
    p1 "Don't...just..."
    pp2 "I hear this poor prisoner just turned 19 today! Caged on your birthday, oh boo hoo...hoo. Begging won't help you at this point."
    pp "Wait, don't say that, I want to see him beg! This is my prisoner Sam!"
    p "(Oh no for him. I guess better him than me but...)"
    scene pat2 with mediumdissolve
    pp2 "Oh poop. You're right, [pname] picked you over me. I just forgot in my enthusiasm."
    pp2 "Very well. I made a remote shocker for him Patty, it's over there if you want to use it."
    pp "Thank you Sam! But let me get more comfortable...I can't wait to get off..."
    pp2 "Oooh, show off your tall pretty body, I'm always so jealous of it Patty!"
    scene pat2b with longfade
    pp "I'm so ready, thank you [pname] for letting me have a little fun."
    pp "For now, I think I want to feed this poor worm. Let me go grab ummm, a special birthday meal for him!"
    pp2 "And you [pname], you sit down on the couch and just watch like a nice little prisoner."
    scene pat3 with longfade
    p "(oh yuck, what is that?!)"
    pp "Ok...Happy Birthday! It's time for your special treat! Let me move it a little closer so you can smell the fresh aroma better!"
    p1 "I'm not hungry..."
    scene pat4 with mediumdissolve
    pp "Oh, but the prison is required to make sure you get enough nutrition! And you are all skin and bones right now...you need to fatten up!"
    pp "Down you go!"
    scene pat5 with mediumdissolve
    p1 "Mppgmmppnmmmhh"
    pp "Mmmmmm, must be so good! Eat it all up! I'm not letting you come up until it's allllll gone."
    scene pat6 with longdissolve
    if selfisheater:
        pp2 "Isn't your lovely food later going to taste that much better now after seeing what this wretch has to eat?"
        pp2 "It looks really bad too, doesn't it? I don't even know what it is!"
        jump patpunishtwo
    else:
        pp2 "Aren't you glad that isn't you [pname]?"
        if sub >= 3:
            pp2 "Then again, you're such a weak sub that maybe you'd like to be on the ground licking that garbage."
            jump patpunishtwo
        else:
            pp2 "I don't even know what that stuff is!"
            jump patpunishtwo

label patpunishtwo:

    scene pat7 with mediumdissolve
    pp "Keep eating you little worm!"
    pp "This is the only meal I may give you for days, so lap it all up."
    p1 "Bhguutt, mopggh!"
    scene pat8 with mediumdissolve
    if dom >= 2:
        pp2 "You know [pname], I've noticed you're not really a good submissive. You have a little more backbone."
        pp2 "I'm glad...I like that about you."
        jump patpunishthree
    else:
        pp2 "Do you regret your punishment decision now?"
        pp2 "Maybe you regret it because Pat is too harsh, or maybe you even regret it because it wasn't me instead?"
        jump patpunishthree

label patpunishthree:

    scene pat9 with mediumdissolve
    pp2 "That's enough Patty, clean his face up with a rag, I want to see it clearly with what you do next."
    pp "*snorts* Yes, dear."
    pp2 "Oh no you didn't, better not be sarcastic with me again. Understand?"
    pp "Yes, I'm sorry Sam. I need his face totally clean anyway if he's going to lick me."
    scene pat10 with longfade
    pp2 "What's next for your punishment, Patty?"
    pp "Sam, can you kiss me while he eats me out?"
    scene pat10b with mediumdissolve
    pp2 "And there it is. Is that really a punishment or just your thirst kicking in? But ask nicely and maybe I will."
    pp2 "No, wait. Ask [pname], it's his punishment. And ask nicely."
    scene pat11 with longdissolve
    pp "[pname], my lovely sweetie, can I play with my friend Sam while this prisoner licks my pussy? Pretty pleeeaaassseee?"
    pp2 "Haha, that was so nice how you asked! What do you think [pname]?"
    menu:
        "Let them kiss. [Recommend]":
            scene pat12 with mediumdissolve
            p "Go ahead, I can't say no to that."
            pp2 "I don't think it was a tough decision for you was it? Very well, I will play with you Patty."
            jump patpunishfour
        "Refuse.":
            scene pat12b with mediumdissolve
            p "No, I don't think so."
            pp "What?? You really don't want to see us kiss?"
            pp2 "Too bad Patty, I'm surprised too!"
            pp "Well my whole mood is spoiled! Hmph. I think I'm done."
            scene pat13 with mediumdissolve
            pp "Can you get him out of here? I think I need to take it out on 912 alone."
            pp2 "Ok Patty, I understand. Let's go [pname], maybe we can have some fun later."
            jump aftermath

label patpunishfour:

    scene pat14 with longfade
    pp "Lick! Or would you rather deal with Samantha than please me?"
    p1 "Oh no not Samantha! I'd rather please you! Ok ok..."
    pp "Mmmm, now if you are a good little tongue slave, I won't increase the shock as I get off...Sam, can you please shock him at a lower level and then come here?"
    scene pat15 with mediumdissolve
    pp2 "Of course. Happy to help."
    pp2 "After all, it's your time to have fun since [pname] picked you! Enjoy some pain 912!"
    scene pat16 with mediumdissolve
    p1 "Rrrrrgghhhh!"
    pp "Poor thing! What a sad birthday! And you'll never be free, stuck in this pathetic existence forever and ever..."
    pp "Birthday after birthday, groveling and serving your superiors."
    scene pat16b with mediumdissolve
    pp2 "Let me help you sweetie..."
    pp "Yes, please."
    scene patkiss with longdissolve
    pp "Mmmmmmmmm..."
    if dom >= 2:
        p "(Wow! I'd love to have them both servicing me instead...)"
        jump patpunishfive
    elif sub >= 2:
        p "(They're so strong and dominant, I wonder how many men they have had on their knees for their pleasure.)"
        jump patpunishfive
    else:
        p "(Such sweet looking lips but what comes out of them is quite different...)"
        jump patpunishfive

label patpunishfive:

    scene pat17 with mediumdissolve
    pp2 "You see [pname], if you make us happy, maybe you will get to play with us too."
    pp2 "But not yet, you need to earn it a little more, so sorry to do that to your poor thing down there."
    pp "Ok...but I wouldn't mind a nice fuck right now...I'm really wet and you know I think [pname] is..."
    if sub >= 3:
        pp2 "You are NOT going to give this subbie that kind of reward so fast!"
        pp2 "Enjoy your lick toy right now..."
        jump patpunishsix
    else:
        pp2 "Uh uh, shhhh, patience, enjoy your lick toy right now."
        jump patpunishsix

label patpunishsix:

    scene pat18 with longdissolve
    pp "Oh yes, right there..."
    pp "Good..."
    scene pat19 with longdissolve
    pp "Mmmm...."
    pp2 "I've licked you enough with my tongue, I want to watch you now."
    pp "Aww, I wish I had three tongues with [pname] too all making me happy..."
    scene pat20 with longdissolve
    pp2 "You're close already, aren't you?"
    pp "Yes..."
    pp2 "Enjoy the power. He's your toy, do whatever you want."
    scene pat21 with mediumflash
    play audio "audio/slap.mp3"
    pp "*slap* Faster...you little..."
    p1 "Mmmhhmmph!"
    pp2 "912! If you don't make Patty perfectly happy, I'm going to punish you instead!"
    scene pat22 with mediumdissolve
    pp "Oh! He's licking even faster now, haha!"
    pp2 "Look in my eyes as you cum. And thank me for being so good to you."
    scene pat23 with longdissolve
    pp "Yes Sam...oh..."
    pp2 "Good girl. Think how lucky you are with pleasure and more pleasure while your toy birthday boy has nothing in life to look forward to but pain and misery."
    scene pat24 with quickflash
    pp "Oh that's so deliciously unfair..."
    pp "Yes, right there!"
    scene pat25 with longflash
    pp "Oh yeeeessssssssss..."
    pp2 "Oh, looks like he finished! Good girl. Now thank me like you should."

    stop seven fadeout 2

    scene pat26 with longdissolve
    pp "Thank you Sam!"
    pp2 "So lucky I hired you, aren't you?"
    pp "Yes, thank you thank you! I love my job!"
    scene pat26b with longdissolve
    pp2 "(So easy to keep her loyal.)"
    pp2 "Good girl. Now get dressed and then put this trash in a cage for solitary. Oh, you can stop his shock too!"
    p1 "Ughhhhh..."
    pp "Happy Birthday worm!"
    scene pat27 with longfade
    pp2 "Well [pname], I hope you enjoyed seeing us in action. Good on the job training for her."
    p "I can see that."
    pp2 "Oh don't pout, you may get your chance to have some fun if you please me. Promise!"
    p "(Sure. I trust you of all people.)"
    scene pat28 with longdissolve
    pp2 "Patty, you can punish him some more tomorrow. Let him sleep in chains tonight. Oh, he needs a bucket for you know...haha!"
    pp "Gross! Oh you poor poor birthday boy haha!"
    pp2 "I'll take you back to your cell [pname], but hopefully we can all play together later."
    jump aftermath

label sampunish:

    play seven "<from 1 to 44>music/sampunish.mp3" fadein 2

    scene samp1 with longfade
    pp2 "Ah, here we are [pname], where magic and dreams come true!"
    p "I think that only applies to you."
    pp2 "It can be true for you too. I haven't forgotten that you chose me to be your instrument of destruction."
    p "(Destruction? That sounds ominous...and wtf? A jacuzzi and bed in here? What?)"
    scene samp1b with longdissolve
    pp2 "So sorry Patty, but you only get to watch here. This is my punishment!"
    pp "I know. [pname], I would have been a little nicer if you had chosen me. Sam is that quote Elena told me, \"A sadist of her kind is an artist in evil.\""
    pp2 "Elena is a smart woman!"
    scene samp2 with longdissolve
    pp2 "Now, let's take a look at our victim. Hmm, he already doesn't look too good, does he [pname]? Poor thing."
    pp2 "Patty might have knocked him out too much."
    pp2 "So I suppose you've heard that I'm so cruel, evil, and scary? Little bitty me?"
    p "Yes. Something like that."
    scene samp3 with mediumdissolve
    pp2 "The truth is, it's so easy to torture almost anyone, and yes, I have done that many times."
    pp2 "But what's far more fun is messing with someone's mind. That's much more pleasurable."
    p "That does sound worse than physical torture. You really are scary."
    pp2 "Thank you! I love hearing compliments."
    scene samp4 with mediumdissolve
    pp2 "Now, last chance [pname], you can stop now and go back to your cell. I won't take offense because I'm going to really punish him you know."
    pp2 "He'll probably die. But I won't touch him personally. It was your choice of course, but it's too late to save him now."
    pp2 "But you, you can still turn back now."
    menu:
        "I don't think I want to watch Sam. I'm out.":
            scene samp5 with mediumdissolve
            p "I don't think I want to see this. No offense."
            pp2 "I understand. Maybe you should have picked Patty, hmm?"
            pp2 "I'll take you back to your cell before getting to work on 912."
            jump aftermath
        "This sounds bad, but I'm too curious. (warning!!!! leads to cruel death of 912!!) [Recommend]":
            scene samp5 with mediumdissolve
            p "I'm a little unsure about this, but I think I need to see the consequence of my choice."
            pp2 "Very well, let's proceed."
            jump sampunishtwo

label sampunishtwo:
    scene samp6 with longfade
    pp2 "Now [pname], this poor soul had a very traumatic experience as a child in an enclosed area with rats and it's given him an extreme phobia."
    pp2 "It's quite serious by all accounts, and I suspect it would only take a strong enough nudge to drive him insane."
    pp2 "Doesn't that sound like fun?"
    menu:
        "Fuck him, he deserves what he gets for attacking me. [EvilPath]":
            $ evil += 2
            scene samp7 with mediumdissolve
            p "Screw him, he deserves whatever he gets for attacking me."
            pp2 "Oh my [pname], you certainly know how to push my buttons the right way!"
            pp2 "But first we need to put him in the box I prepared so please help me...then we can wake him up."

            stop seven fadeout 2

            jump sampunishthree
        "No, do you really need to go this far? [GoodPath]":
            $ good += 1
            scene samp8 with mediumdissolve
            p "Do you really have to go this far? If what you say is true, he might lose it."
            pp2 "That's the fun part! Too late now, you delivered this fate to him personally."
            pp2 "But first we need to put him in the box I prepared so please help me...then we can wake him up."

            stop seven fadeout 2

            jump sampunishthree

label sampunishthree:

    play music "music/death1.mp3"

    scene samp9 with longfade
    pp2 "Now [pname], this is serious prison justice so I trust you can stay still and just watch, please? You too Patty."
    p "Fine."
    pp2 "Thank you, I'm so glad you are cooperating so well, I promise to make it up to you. Go ahead and have a seat with Patty and just relax."
    pp2 "My skirt is only going to interfere with my fun. Can I trust you not to try and rape me if you see my body, [pname]? I'm so so small after all..."
    scene samp10 with longfade
    pp2 "Wake up wake up, little mouse!"
    p1 "....Ugghhh, wait, where am I?"
    pp2 "Prisoner 912, you attacked one of your fellow prisoners without provocation."
    pp2 "For this violation, I'm afraid I have to punish you."
    scene samp11 with mediumdissolve
    p1 "What the? Why am I inside a box? What the hell is this, let me out!"
    pp2 "If you look carefully, you will see a small hole above your head that you can't quite reach on top of your box."
    pp2 "It connects to another part of the box, a small area. But, right next to you, I have given you a small knife and a working flashlight so you can see better in there."
    p1 "Why, what the fuck is this?"
    scene samp12 with mediumdissolve
    pp2 "Well little mouse, that small hole is going to allow a few friendly animals from above your head to visit you in there! I just opened the hole real small for you!"
    pp2 "Every so often or so, a rat will join you in there! You could always use your knife maybe to kill them, but you have to work quickly before more show up."
    scene samp13 with quickdissolve
    p1 "Oh my god, no please!! Not rats! Oh my please, please, I'm so sorry, I'll never do it again, please!!!!"
    pp2 "Oh [pname], I just love it when they beg!"
    p1 "No no no! Please!"
    pp2 "Oh...you poor poor baby..."
    scene samp14 with mediumdissolve
    pp2 "Oh! I hear one in there now! Enjoy!"
    p1 "No no! *stabbing noises* ooohohohoh no..."
    pp2 "Don't give up! If you can fight them off, you can get out of the box eventually!"
    scene samp14b with mediumdissolve
    pp2 "Oh, I don't hear it anymore! Did you get it? Must be hard with how tight it is in there! Good job!"
    p1 "Oh please please, arrrggghhh, I can't take this, please!!!"
    pp2 "Of course, that was only one. I think a lot more are coming! You can do it, try hard to survive!"
    p1 "No no no no no please please oh my God stop it please!"
    scene samp14c with mediumdissolve
    pp "Oh my God [pname], she is so cruel."
    pp "I have so much to learn..."
    scene samp15 with mediumdissolve
    p "(This is a truly evil woman...much worse than Patricia right now.)"
    p1 "No more! Please, I'll do anything! Anything! Just stop it!"
    pp2 "Oh, I think the next wave is ten rats if I remember! Enjoy!"
    scene samp16 with mediumdissolve
    p1 "*multiple squeaking noises* Oh no, no no no! Oh no!!! Please, stop it stop stop stop stop!"
    p1 "Aaaaaaagggghgghghgh"
    pp2 "Keep fighting little mouse...don't die yet...you can do it..."
    scene samp17 with longdissolve
    p1 "oh my! Please..!! Make it stop, please please please, help me help me! Mommy!!"
    p "(Wait, what? Has he lost it already?)"
    pp2 "Oooh yes, maybe we can rescue you, I have an idea..."
    p1 "Anything, anything, I see even more coming!!!"
    scene samp18 with longdissolve
    pp2 "If you take that knife, and cut off the fingers on one of your hands, then I'll get that box open for you."
    p1 "Wait, what? I can't...! Shit, ok ok! I'll do anything, I'm going to.....arrrrrrggghhh!"
    pp2 "It has to be at least four fingers..., and I want to hear it clearly! Don't worry, the knife is super sharp by design for your hand! Hurry before more and more come!"
    scene samp19 with longdissolve
    p1 "Ok! I go go fast fffasdatgt fast, I go oh no...arrrggh, it hurts, I feel dizzy, help, hurry, they are all over me!!"
    pp2 "Keep going little mouse...you're almost there...you can do it!"
    p1 "Aagggh, that's all, please open it!"
    scene samp20 with mediumflash
    pp2 "Oh, I'm afraid dozens of rats are now coming for you and I just wanted your blood exposed to get them excited for you."
    pp2 "But I wanted to make sure you could see how excited I am too! While your fingers are wet with blood, my fingers are wet with my pussy!"
    p1 "Noooooooo! Please...!!!!!!"
    scene samp21 with longfade
    pp2 "Goodbye little mouse...!"
    p1 "No ack, argghgh, *lots more squeaking*....urrggghhh..uuuuuu...."
    p1 "nooo!! help help omn nmymymy gofdof..hellllp!"
    scene samp22 with longflash
    pp2 "Ahhhhh.....yes!"
    pp2 "So good..."

    stop music fadeout 2

    scene samp22b with longfade
    pp2 "Wonderful...ahhh, I wish I could have been fucking you [pname] during my fun, maybe in the jacuzzi. Mmmmmm."
    pp2 "But Elena won't let me. Yet."
    scene samp23 with longfade
    pp2 "I should have put a camera inside the box to record it, but to tell you the truth [pname], I'm a little squeamish about blood!"
    p "(...)"
    pp2 "I have to ask you, what did you think of my...punishment?"
    menu:
        "Call her a sick and evil woman. [GoodPath]":
            scene samp23b with longdissolve
            $ samupset = True
            $ good += 1
            $ sam_p -= 2
            p "What you did. It's just sick. Evil. I..."
            pp2 "Now who's the squeamish one? I hope you can figure out how to survive better by not insulting someone who can make your life a living hell!"
            pp2 "Let's go! Patty, take him back to his cell!"
            jump aftermath
        "Comment that you hope you never get on her bad side. ":
            scene samp24 with longdissolve
            $ sam_p +=1
            p "Honestly, I hope I never get on your bad side. I wouldn't want to be in your doghouse or dogbox I suppose."
            pp2 "Hah, I appreciate the honest answer. But I like you right now [pname], no need to worry that much."
            pp2 "Maybe next time we can just do the normal whips and chains sort of thing, that's more common for me. Let's go back to your cell."
            jump aftermath
        "Agree with her that it would have been better if she had been fucking you. [DomPath] [SamamthaPath]":
            $ dom += 1
            $ sam_p += 2
            scene samp24 with longdissolve
            p "You're right. It would have been better for you if we had been fucking."
            scene samp25 with mediumdissolve
            pp2 "Ooooh [pname], I really, really, want to fuck you now."
            pp2 "You seem strong, and capable. I don't like men that are too moral and submissive at all. I wish you could stay here at the prison for a much longer time..."
            pp2 "...but I know something unusual is in your future if it warrants Elena's attention."
            scene samp26 with mediumdissolve
            pp2 "I hope to play with you before you leave, and I really hope you end up with a lot of power and influence someday."
            pp2 "I'd be a very willing...employee for you."
            pp2 "Let's go back to your cell, babe."
            jump aftermath

label aftermath:

    play seven "music/darkness.mp3" fadein 2

    scene aftermath1 with longfade
    p "(What the fuck is going on here? Hey, my pillow is different...not too shabby...)"
    p "(...A strange offer just like that. Meeting Elena but no one else did maybe...one of the top executives of one of the biggest companies in the world talking to a random prisoner???)"
    p "(All this talk about the Karlsson sisters. [pname2] magically being here at the same time. For the same program.)"
    p "(We are both arrested, tried, and brought here at almost the exact same time in dubious circumstances. Both about three months or so.)"
    scene aftermath2 with mediumdissolve
    p "(There's definitely something strange about all this, but what?)"
    p "(I guess I can't complain yet. Maybe I'm not stuck here five years, and maybe I have a chance to do something.)"
    p "(I don't think many would do well in this prison after five years, that much is very clear.)"
    scene aftermath3 with mediumdissolve
    p "(Is this just kind of weird game for bored rich people?)"
    p "(But my gut feels like it's more than that, but I don't know why...)"
    if elena_mentor:
        p "(Elena talking about mentoring or helping me makes me sure it's far beyond a simple training program.)"
        p "(I definitely feel like I passed a big initial hurdle with her with how I responded to her questions.)"
        p "(At the same time, I better not piss her off or it could be that much worse for me.)"
        p "(I have to take a psych test too, I better be very cognizant and aware of how I fill that out.)"
        jump aftermathtwo
    else:
        p "(Especially Elena. I could clearly feel her evaluating me much more beyond suitability for her training offer. I could feel it was much deeper.)"
        p "(Logically, no way they would send a top executive like that without a very big reason.)"
        p "(They said I have to take a psych test too, I better be very cognizant and aware of how I fill that out.)"
        jump aftermathtwo

label aftermathtwo:
    scene aftermath4 with longdissolve
    p "(But now, I'm so tired. Just a little rest should do the trick...)"
    p "(Yeah, just a little rest...)"

    stop seven fadeout 2

    jump fork2

label fork2:
    if elena_mentor:
        jump elenavisit
    if dom >= 3:
        jump samvisit
    else:
        jump sisterintro

label samvisit:

    play seven "music/samvisit.mp3" fadein 2

    scene black with mediumfade
    pp2 "Ohhhhh [pname], wakey wakey..."
    scene samvisit1 with longfade
    p "Ngghhh....wha...Samantha? Patricia?"
    if samupset:
        pp2 "Even though you upset me [pname], calling me such a mean girl after my punishment, I still want to visit you!"
        jump samvisit2
    else:
        pp2 "Evening, babe. We're here to visit our favorite prisoner!"
        jump samvisit2
label samvisit2:
    scene samvisit2 with mediumdissolve
    $ dome11 = True
    pp2 "I wish I could say I visited for a fuck [pname], but I don't dare disobey Elena. And she says no right now."
    pp2 "I have a message from Elena. I had to basically memorize a lot of it for you. She said you should take it to heart."
    p "Ugh, ok, give me a sec."
    scene samvisit3 with longfade
    pp2 "Now you sit, I'd like to be tall once in a while!"
    pp2 "Here it is for you from Elena. [pname], you have shown some dominant tendencies right away as I have observed you."
    pp2 "The road to power through dominance will be tougher and you will have to be a little more patient."
    pp2 "Remember this old proverb [pname]. One moment of patience may ward off great disaster. One moment of impatience may ruin a whole life."
    scene samvisit3b with mediumdissolve
    pp2 "Patty, stop teasing [pname]?! I have to finish this, do you want to upset Elena?"
    pp "Oh you are so right, sorry!"
    pp2 "Anyway...Gaining true dominance will require more cunning and you will have to delay instant gratification at times for the bigger picture."
    scene samvisit4 with mediumdissolve
    pp2 "You did not impress me enough in your interview to make me consider mentoring you right away, but remember a few things."
    pp2 "Build power through allies, information, and favors to others' self-interests."
    pp2 "If you can do these things, you will have better chances later to enjoy the fruits of your labor."
    pp2 "Maybe then I will be very impressed and ready to assist you a little more."
    scene samvisit5 with mediumdissolve
    pp2 "I personally want you to be dominant and strong for my own reasons. So, I want to give you a little motivation."
    pp2 "I am sending a present to you soon if you want to enjoy it. I also am going to soon allow Samantha or Patricia to enjoy you and each other if you all agree."
    pp2 "A very small sample of what you can have if you play the game well. You have no idea what is coming, but don't blow the chance you have. Good luck [pname]."
    scene samvisit6 with longdissolve
    pp2 "That's her whole message, and did you hear that? Maybe tomorrow we can have soooo much fun."
    if samsadist:
        scene samvisit6b with longdissolve
        pp2 "After all, I was such a baaaaad girl for basically murdering a poor prisoner for my sick fun, right?"
        pp2 "Maybe I need to be...punished."
        jump samvisittwo
    else:
        pp2 "But you still have to be a good little prisoner on the outside."
        jump samvisittwo

label samvisittwo:
    scene samvisit7 with longdissolve
    pp2 "Now, I want to feel you under me as I sit here..."
    pp "Sam! What about me?"
    pp2 "I outrank you Patty, so you have to wait your turn. Sorry!"
    scene samvisit8 with mediumdissolve
    pp2 "I hope you want me as much as I want you...oooohh, it feels like you do...mmmm."
    pp2 "Don't masturbate tonight. Maybe I want all of your...juice...on and in me tomorrow."
    scene samvisit9 with mediumdissolve
    pp2 "Mmmmm."
    pp2 "And don't worry Patty, I will always take care of my favorite girl. But I go first."
    scene samvisit10 with mediumdissolve
    pp2 "Sweet dreams [pname], see you later."

    stop seven fadeout 3

    jump sisterintro



label elenavisit:

    play seven "music/samvisit.mp3"

    scene black with mediumfade
    pp2 "Time to wake up [pname]!"
    scene samvisit1 with longfade
    p "Wha? Saman...Pat, it feels like I barely slept."
    pp2 "You only napped a short while. It's still the evening, but you need to get up."
    scene samvisit2 with mediumdissolve
    p "Ok, but why?"
    pp2 "Patty is going to take you to visit Elena. She wants to speak to you again. I don't need to remind you not to fuck with her of all people, right?"
    p "No, no, I get it. What does she want?"
    pp2 "That's for you to find out, but hurry it up and get going."
    jump elenavisittwo

label elenavisittwo:

    scene limo1 with longfade
    p "Well, you certainly don't see a limo in a prison yard very often."
    pp "Just behave [pname], you don't know how lucky you are right now for even getting some of her valuable time."
    p "I understand that. I think you must be very loyal to Elena by how you speak of her."
    pp "Yes, I owe her so much. I grew up poor like you [pname], and she's given me a new life."
    scene limo2 with mediumdissolve
    p "(Would it kill these women to give me some damn shoes!!? These steps are rough!)"
    pp "Elena found me and took me under her and Sam's wing."
    menu:
        "(Maybe I should ask her for advice on meeting Elena.)":
            p "Is there any advice you could give me for meeting with her?"
            pp "Do you really need my advice for her? Make her happy and hope she makes you happy in return. Even obeying her is no guarantee of safety for you."
            pp "But not obeying is a sure ticket to pain. Many many people have suffered and died by her order, so tread carefully. I still watch what I say around her."
            scene limo3 with mediumdissolve
            p "Ok, but anything more practical? What she really likes or hates personally?"
            pp "Oh [pname], I think you should be doing something for me if I help you...but I'll be nice to you a little."
            if patpunish:
                pp "Especially since you chose me to punish Prisoner 912. I really did get to have some fun thanks to you."
                pp "She likes brains and cunning, you won't impress her much any other way."
                jump elenavisitthree
            else:
                pp "Even though I'm still a little upset you didn't pick me to punish Prisoner 912."
                pp "But, I will tell you that she likes brains and cunning, so anything outside of that might not do much for her."
                jump elenavisitthree
        "(Maybe I should try and compliment her to butter her up.) [PatriciaPath]":
            p "I have to be honest and say I'm really impressed with you."
            pp "Oh, why's that [pname]?"
            menu:
                "(Appeal to her looks and let her know how hot she is.)":
                    scene limo3 with mediumdissolve
                    p "You're just really hot, and seeing you all the time has to be sexually frustrating to a lot of other prisoners too."
                    pp "Yes, I know. I wouldn't be working here if I was an ugly fattie. I'd be the female version of the worms in here maybe!"
                    pp "You better not try and appeal to Elena's looks too much, that probably won't impress her."
                    jump elenavisitthree
                "(I should let her know how powerful she is, and how it makes me want to serve her.) [SubPath]":
                    scene limo3 with mediumdissolve
                    $ sub += 1
                    p "You're just really impressive and powerful, it makes me want to just serve your needs and wishes."
                    if sub >= 3:
                        pp "In your case [pname], I already have seen how submissive you can be at times. You belong on your knees if you keep that mindset."
                        pp "If you don't change, that's where you will always be. Kneeling and begging. Maybe for you, that's ok, but it's not for me."
                    else:
                        pp "Be careful [pname], others will run over you if you let them. I know Elena is impressed if she wants to meet with you, so don't screw it up."
                        pp "And of course I'm never unhappy if you tell her how amazing I am too..."
                        jump elenavisitthree
                "(Let her know you would want to hire her if you had power.) [PatriciaPath]":
                    scene limo3 with mediumdissolve
                    $ pat_secpath = True
                    $ pat_p += 2
                    p "If I was in a position of power, I definitely would want to hire you. You're just really impressive overall."
                    scene limo4 with mediumdissolve
                    pp "Really, [pname]? Thank you. If you can manage to impress Elena and move up in the world, you never know. I might be open to...working with you."
                    pp "But my job here is so fun, you'd have to offer some good...perks to entice me if it's my choice. But I appreciate what you said, so..."
                    pp "...[pname], I'll give you the best advice I can. Don't be weak or worse too macho and show some intelligence! A dominant and cunning man is what she wants you to be!"
                    scene limo5 with mediumdissolve
                    pp "Just in her main home alone, she probably has over 100 servants. They are basically slaves. I don't think she wants another one, but something more."
                    pp "I don't know what, but this is a big chance for you to avoid being a little maggot in this jail. Take advantage of it."
                    jump elenavisitthree

label elenavisitthree:

    stop seven fadeout 3

    scene limo6 with longfade

    play seven "<from 1 to 60>music/meeting0.mp3" fadein 2

    pp "Well, here we are. Get in there."
    p "You're not coming in too?"
    pp "No, she wants me to wait outside. I'm actually driving her to the airport after dropping you back in your cell, so don't make me wait forever!"
    p "Sure thing."
    scene limo7 with longfade
    p "(Oh, a female prisoner? Or a virtual slave I bet...)"
    ec "[pname], glad you could meet me again. I appreciate you taking the time to leave your wonderful cell to visit."
    p "Uh huh. I had a lot of choice in that, didn't I? But yes, this definitely beats my cell."
    ec "I hope you can appreciate the very unique chance you have right now."
    scene limo8 with mediumdissolve
    p "Yes. I do."
    ec "Good. As I told you, I'm considering mentoring you for what lies ahead of you. It will be a challenging road, but a huge opportunity as well."
    p "What does lie ahead? What is all of this? This is more than just some normal training program, isn't it?"
    ec "Patience [pname], over time, answers will come your way. But as I said to you before, some things are best to learn by self-discovery for the greatest impact."
    scene limo9 with mediumdissolve
    ec "But I'll say one thing. A novelist named Ralph Ellison wrote something that I think you should remember for your journey. \"When I discover who I am, I'll be free.\""
    ec "It has more than a singular meaning for you. And others around you too. Maybe later it will crystallize in your mind when it matters."
    ec "But for now, you need to focus on surviving the gauntlet of your training program. It will not be easy."
    scene limo10 with mediumdissolve
    ec "And I only want to help you if it's in my interest. And you can help me [pname]. In ways you can't even imagine yet."
    ec "You are about to play a very dangerous game, and it's life and death stakes for the players. You are a key player, believe or not."
    p "Why?"
    scene limo11 with mediumdissolve
    ec "Don't search hard for that answer quite yet. You need to prove yourself first."
    ec "I told you I would test your loyalty and toughness, but I won't do it so quickly tonight. I want to see a little more first."
    ec "I'm going to give you some starting advice soon, but first..."
    scene limo12 with longdissolve

    play seven "music/limo.mp3" fadein 2

    ec "...I want to give you a taste of my generosity for loyalty. I am a very fair and generous woman to those that please me. And you pleased me during your interview."
    ec "I do want to ask you a few more questions before giving some advice. But let's spice it up and have Kitty service you while you try and concentrate on my inquiries."
    p "(Oh!)"
    scene limo13 with mediumdissolve
    ec "Kitty, service [pname] while I continue to talk to him. Do a good job, the poor thing has been stuck in prison you know."
    kk "Yes, Mistress Elena."
    menu:
        "(No, I don't want a blowjob like this.)":
            $ elena_p -= 1
            p "No, that's ok, I don't want it like this."
            ec "Really [pname]? Too bad, you forget I am in power here. Kitty needs to taste your cum for training."
            jump elenavisit3b
        "(I need some release. Badly.) [ElenaPath]":
            p "Err, you're in charge."
            ec "Yes I am, appreciate my generosity."
            jump elenavisit3b

label elenavisit3b:

    scene limo14 with longfade
    ec "Now [pname], I won't bother you about your sick brother right now, but I do want to ask about your family a little."
    ec "Tell me about your mother."
    p "You want me to talk about my mother while??"
    scene limo15 with longdissolve
    ec "Having trouble concentrating [pname]? You need to have a sharp mind at all times."
    p "Ok, ok. She was great. Very smart, talented. I believe she would have been something special if born under better circumstances."
    ec "I see. Tell me a little more."
    scene limo16 with longdissolve
    p "(Jeez, this is distracting...)"
    p "But we moved a lot. And she always seemed a little...I don't know. Nervous and sad in a way I can't pinpoint. But she was so good to all of us."
    scene limo17 with mediumdissolve
    ec "Did she ever talk to you about her past?"
    p "No. She said her parents died while she was young and that she had a tough past not worth talking about when the future mattered more."
    scene limo18 with longdissolve
    p "(Oh wow, she's good!)"
    ec "Very well. Let's move on."
    scene limo19 with longdissolve
    ec "What about your sister?"
    ec "Can you just describe her in a word or two if you could?"
    menu:
        "(I think strong.) [SisDomPath]":
            $ sisdom += 1
            p "Strong. She's tough, and can handle herself."
            jump elenavisitfour
        "(I'd say gentle.) [SisSubPath]":
            $ sissub += 1
            p "She's a very gentle soul."
            jump elenavisitfour
        "(I'm not sure.)":
            p "Honestly, I'm not sure. It's tough to encapsulate her entirely with a word or two."
            jump elenavisitfour

label elenavisitfour:

    scene limo20 with longdissolve
    p "Umm, oh my...what else do you want to know about her?"
    ec "No...no, nothing else. I'm done for now."
    scene limo21 with longdissolve
    ec "I have to say, I thought you would finish by now [pname]. Kitty is very good at what she does. Did you masturbate recently in your cell?"
    p "No, I'm close...yeah, she's good."
    ec "Oh yes, I had her trained very well, but not with any real men. She's still a virgin. Maybe you want to deflower her?"
    p "(Oh my God, she sped up even more all of a sudden!)"
    scene limo22 with longdissolve
    ec "Just imagine having the power to order her to do...anything. If you listen to me, many things will be possible for you."
    p "Oh my! I'm going to...!"
    scene limo23 with longflash
    p "(oh yess!)"
    kk "bllmlgfpph..!"
    scene limo24 with longfade
    ec "Oops, sorry [pname], I've trained her to swallow and lick everything. Maybe next time, I'll let you explode all over her if you prefer."
    kk "Mistress, he tasted so good, thank you for letting me finally serve a man. I want him to be my first."
    ec "You're welcome Kitty, and we'll see. Now [pname], I do have some small advice to get you started when you leave our wonderful facility here."

    stop seven fadeout 3

    scene limo25 with mediumdissolve
    ec "Don't show weakness if possible, but also don't try to prove your strength over a superior power either. Patience and cunning [pname]."
    ec "Find the strengths and weaknesses of everyone around you. Find powerful allies to benefit you long-term. I can be one of them if you are smart [pname]."
    scene limo26 with mediumdissolve
    ec "You have your friend [pname2] too. You probably can trust him, but don't assume that will last forever."
    ec "My most loyal person here at the jail is Patricia. Stay on her good side, and you can even fuck her if she wants to as well."
    ec "Now most of all [pname], you will end up interacting with all of the Karlsson sisters. Learn which ones can help you the best, they are quite different."
    scene limo27 with mediumdissolve
    ec "Don't relax and don't ever let your guard down, it only takes one big mistake to pay dearly."
    ec "Anyway, that's enough for now. I have a long flight ahead of me and let's see how you do [pname]. Good luck."
    jump sisterintro

label sisterintro:

    scene sisintro1 with longfade

    play seven "music/sisintro.mp3"
    pause 3

    scene sisintro2 with longfade
    ns "Oh, hi there..."

    python:
        pname3 = renpy.input("My sister's first name is...(just type name and press Enter)")
        pname3 = pname3.strip()

        if not pname3:
            pname3 = "Olivia"

    python:
        pname4 = renpy.input("My brother's first name is...(just type name and press Enter)")
        pname4 = pname4.strip()

        if not pname4:
            pname4 = "Seth"


    scene sisintro3 with mediumdissolve
    ns "...[pname3]. I'm glad you came so quickly, I know it's really late."
    sis "What's wrong?"
    ns "[pname4] has had a complication. Doctor Janssen should be out in a just in a minute or two."
    sis "What kind of complication? Is he ok?"
    scene sisintro4 with longdissolve
    ns "I don't know, if you could wait a minute please."
    ns "She let me know she was almost done, it shouldn't be too long."
    menu:
        "Demand she get the doctor more quickly for answers. [SisDomPath]":
            scene sisintro5 with mediumdissolve
            $ sisdom += 1
            sis "You expect me to just sit quietly when you are telling me there has been a complication?"
            sis "I want you to get her out here as soon as possible, or get anyone else to just give me information!"
            ns "I'm sorry [pname3], I'll try and get you something quicker, I know...it's...been so hard and with [pname] gone too..."
            scene sisintro6 with mediumdissolve
            sis "Just hurry it up, I'll sit for now."
            jump sisintrotwo
        "Wait quietly for the doctor. [SisSubPath]":

            scene sisintro7 with mediumdissolve
            $ sissub += 1
            sis "Ok, but please let me know something when you can."
            ns "I will dear. I know it's been so hard for you, plus with [pname] too...sorry."
            sis "It's ok."
            jump sisintrotwo

label sisintrotwo:

    stop seven fadeout 2

    play seven "<from 86 to 180>music/sisintro2.mp3" fadein 2

    scene sisintro8 with longfade
    dj "Ah, [pname3], thanks for coming so quickly. I need to speak with you. Shall we sit down somewhere else?"
    sis "No, right here. What's happened? I was told there were some complications."
    dj "Yes, I'm afraid his condition has worsened his muscle atrophy and done other damage in his legs."
    scene sisintro9 with mediumfade
    sis "What does that mean practically? What's changed?"
    dj "It means the damage to his muscles and nerves in his legs may make it difficult for him to ever walk again..."
    dj "...even if we were able to cure his condition later."
    scene sisintro10 with quickdissolve
    sis "You damn well could cure the condition if there was enough money behind it!"
    dj "I know. I can't change the world we live in today. I can't even get access to that kind of medicine in this entire hospital."
    dj "I'm doing everything I can, but at some point, the limitations here are not enough."
    scene sisintro11 with mediumdissolve
    dj "Your mother set up a wise fund for certain medical care for all of you before she died, but there was no way she could have forseen this severe situation."
    dj "That kind of money for care is way beyond what she anticipated. I can care for him reasonably with what I have, but no, I can't magically get him healthy again."
    scene sisintro12 with mediumdissolve
    sis "So this hospital makes money on [pname4] but never really can fix anything I suppose..."
    dj "Look, his legs may actually feel less pain for the wrong reasons obviously, and I can manage his head pain and a little bit more here and there."
    dj "But the rest of his body...at some point, are you just prologing his suffering? I'm not trying to just nickel and dime money here [pname3]."
    scene sisintro13 with quickdissolve
    sis "Ok, speaking of money, how much would it actually take to really have a chance? You have dodged this question before, but I think I deserve to at least know."
    dj "It's...what does it matter? It's so beyond 99.99 percent of people on this planet."
    sis "Just humor me. How much?"
    scene sisintro14 with quickdissolve
    dj "I'd say a complete battery of all the medicines I would need would cost about two to three million dollars."
    sis "Wow. That's like...forever rent for my room, I only pay like twenty dollars a month."
    dj "Before the Great Collapse, a lot of people had that kind of money. Well, not a ton, but certainly a decent amount."
    scene sisintro15 with quickdissolve
    dj "With the severe deflation and restructure in currency now, I think that amount may as well be a trillion dollars for all but the top zero point one percent of people today."
    dj "People used to pay thousands a month for rent, but only like five dollars for a meal. Food is obviously much more scarce now."
    dj "So again, I hate to but have to ask...are you just prologing his suffering for nothing?"
    scene sisintro16 with quickdissolve
    sis "How much longer can you keep him stable without more permanent damage?"
    dj "I...I don't know. Maybe weeks, months, but probably not a year."
    dj "But I wouldn't have seen his legs happening either right now. Anything could happen at any time."
    scene sisintro17 with quickdissolve
    sis "Ok. Can I see him tonight?"
    dj "No, he needs to rest after we stabilized him."
    sis "I understand. I'll be back later to see him."

    stop seven fadeout 2

    scene sisintro18 with mediumfade
    dj "Wait, you still won't answer my question about his long-term..."
    sis "Talk soon Doc!"
    jump sisapt

label sisapt:

    scene sisapt1 with longfade

    pause 3

    scene sisapt2 with longfade
    sis "(So sleepy...)"
    scene sisapt2b with longdissolve
    sis "(What a long day...)"
    scene sisapt3 with longdissolve
    sis "Ok...stay strong..."
    scene sisapt4 with quickdissolve
    sis "Tough times never last, but tough people do..."
    scene sisapt5 with longfade

    play eight "<from 2 to 13>music/s2.mp3" fadein 1
    pause 3

    scene sisapt6 with mediumfade
    sis "([pname] and [pname4], I always thought you could help me someday, but it seems...)"

    stop eight fadeout 1
    scene sisapt7 with mediumdissolve

    play seven "<from 17 to 162>music/s2.mp3" fadein 1
    sis "Oh my God! Who the!??!"
    scene black with quickdissolve
    sis "What the? Get this off me!! Aaaaaaa!"
    ua "Calm down! I'm just trying to take you to meet someone, I'm not going to hurt you!"
    sis "Let me go! You piece of! Why cover my head and kidnap me if it's just to talk to someone!"
    ua "Sorry, you leave me no choice, I have to hold your mouth down to calm you down and carry you to my car."
    sis "Mmmpppgh!"
    scene black2 with longfade
    ua "*car engine starting* Now just relax, I'm not here to hurt you, just taking you somewhere."
    menu:
        "Berate and yell at your kidnapper. [SisDomPath]":
            $ sisdom += 1
            sis "Putting a bag over my head and abducting me...for a meeting? What a real man you are! Grabbing a girl that way!"
            ua "We'll be there soon, just calm down."
            sis "(....)"
            stop seven fadeout 2
            jump sismeetingone
        "Remain quiet and say nothing. [SisSubPath]":
            $ sissub += 1
            ua "Look, glad you could calm down, I really am just taking you to meet someone."
            sis "(....)"
            stop seven fadeout 2
            jump sismeetingone

label sismeetingone:


    play seven "music/pattest.mp3" fadein 1
    scene black with superfade
    sis "(The road is smoother, we are heading into a richer sector.)"
    pause 3

    scene black with superfade
    sis "(Maybe I can use my heel as a weapon if I have to...)"

    pause 3

    scene black with superfade
    ua "Alright, just picking you up a second, we're here."

    pause 3

    scene black with longfade
    stop seven fadeout 2
    ua "Ok, just putting you down here, and just wait, and let me take this off..."
    scene sismeeting1 with longfade
    ua "There you go."
    scene sismeeting1b with longdissolve
    sis "Where am I?"
    ua "Just a hotel room. Just relax please."
    scene sismeeting1c with mediumdissolve
    sis "Relax whatever! What do you intend to do with me?"
    ua "Nothing, hey, just a talk."
    scene sismeeting2 with longdissolve

    play seven "<from 40 to 210>music/allesandra.mp3" fadein 2

    a "Why does she look so upset and frightened?!"
    ua "Mistress Alessandra! I, err...the pickup didn't go smoothly."
    scene sismeeting2b with longdissolve
    a "Why not?"
    ua "Err...well, it just wasn't smooth."
    scene sismeeting3 with mediumfade
    a "[pname3], I'm so happy to meet you, but why are you so upset?"
    sis "You know my name. Now I'm very curious why you have me here."
    a "It's really important I speak to you, but again, what happened? I just asked him to bring you to talk to me."
    scene sismeeting4 with mediumfade
    sis "Why shouldn't I be upset since your goon bagged my head, picked me up, and literally kidnapped me."
    a "What?!!"
    scene sismeeting5 with mediumdissolve
    a "I asked you to have her meet me, not kidnap her! What were you thinking?!!"
    ua "I..err, I'm sorry, I thought..."
    a "There's your problem right there, you shouldn't be thinking beyond your intellectual capacity! Bring someone doesn't mean what you did!"
    scene sismeeting6 with mediumdissolve
    ua "It's just...when Mistress Juliette has me pick up people, it's always that way, I..."
    a "I am NOT my sister, and you should be able to serve all of us equally well! Kneel down right now and just wait while I decide what to do!"
    scene sismeeting7 with longdissolve
    a "I am SO sorry [pname3], that was completely unacceptable. Will you please forgive my horrible first impression?"
    menu:
        "(Handle it diplomatically and be friendly to her.) [SisPath]":
            scene sismeeting8 with mediumdissolve
            $ sis_a_p += 1
            sis "It's ok, I can see you didn't mean for this to happen the way it did."
            a "Thank you [pname3], I really do appreciate your understanding, I promise I will make it up to you."
            jump sismeetingtwo
        "(Handle it with suspicion and coolness.)":
            scene sismeeting9 with mediumdissolve
            sis "I'm relieved I'm not going to get raped or anything, but forgive me if I'm not still suspicious about all of this."
            a "I understand [pname3], and I really am sorry."
            jump sismeetingtwo

label sismeetingtwo:

    scene sismeeting9b with longfade
    a "[pname3], my name is Alessandra Karlsson, and I wanted to speak to you about yourself and your brother [pname]."
    sis "Oh, The Karlsson Group...What about [pname]?"
    scene sismeeting10 with longdissolve
    a "Hmm, first let's deal with this problem you had. And you know [pname3], I think I am going to cut this talk a little short and let you rest anyway..."
    a "We do have to address what happened to you with my servant. I am not going to let your suffering go unpunished. That must have been a horrible and scary experience!"
    scene sismeeting11 with mediumdissolve
    a "Come here simpleton, and kneel before your judge."
    sis "Judge?"
    a "Yes, you are the wronged party, I think it's only fair that you decide how he can make it up to you."
    scene sismeeting12 with mediumdissolve
    sis "I'm not sure what you mean."
    a "This servant is supposed to serve with distinction, and this was a horrible mistake on his part."
    a "Now, he's going to apologize to you first, and then let's figure this out. Go ahead..."
    scene sismeeting13 with mediumdissolve
    ua "I'm so sorry Mistress...err..."
    a "I said her name more than once, is your feeble mind incapable of even remembering it? Pathetic."
    ua "I'm so sorry, please don't punish me."
    scene sismeeting14 with mediumdissolve
    sis "I don't understand what I can do here. This is not something I have done before. You want me to punish him somehow?"
    a "Forgive me [pname3], I know you are not used to power. Let me help."
    a "Usually, this kind of serious mistake by a servant would require either a punishment of pain or something more serious like a demotion."
    scene sismeeting15 with quickdissolve
    a "All of our servants that interact with someone at my level have numerous chips embedded in their bodies that allow for a variety of voice activated punishments."
    a "This simpleton is a Level 6 servant, on a scale of one through ten. Personal servants with access like this also are injected with a...special serum."
    scene sismeeting16 with mediumdissolve
    sis "What does that do?"
    a "It's a company secret but one thing it does is make one more docile and compliant. And with servant levels, a Level 10 servant is usually a happy one with many freedoms and a Level 1..."
    a "...servant is not going to last much longer, being honest."
    scene sismeeting17 with mediumdissolve
    sis "So I can either punish him with pain or demote him?"
    a "Yes, you can also spare him completely. And the pain level you can administer can vary too. I'm a softie compared to my sisters, but I do think discipline is needed sometimes."
    a "I'll let you figure this one out [pname3]."

    stop seven fadeout 2

    scene sismeeting18 with longdissolve

    play seven "music/pattest2.mp3" fadein 3

    sis "I want to ask him about this too. Can I have him kneel upright?"
    a "He'll do anything you say [pname3]."
    sis "Ok Mr. Goon, can you kneel so I can see your face better?"
    scene sismeeting19 with longfade
    sis "Do you think you deserve to be punished for kidnapping me?"
    ua "Yes! I deserve it, I screwed up! But please give me pain, don't demote me! It took me so long to get to Level 6!"
    scene sismeeting19b with mediumdissolve
    sis "What's so bad about being demoted?"
    ua "If I go back down to Level 5, I have to sleep packed with other servants again! And my food...oh no...please don't."
    sis "I see..."
    menu:
        "(I can't make this kind of serious decision, maybe I should leave it up to Alessandra.) [SisSubPath]":
            $ sissub += 1
            scene sismeeting20 with mediumdissolve
            sis "I...I can't make this kind of decision, I think I should leave it up to you Alessandra."
            a "I understand, it's not easy to possibly change an entire life on a single decision. But I have to do this everyday."
            scene sismeeting21 with mediumdissolve
            a "Your punishment is going to be a demotion to a Level 5 servant for one month. If you can serve me well in that time, I will restore you back to 6."
            ua "Oh thank you Mistress Alessandra! I promise I will earn it back, and serve you perfectly!"
            a "Well, now we have that business concluded..."
            jump sismeetingthree
        "(I don't really want to punish him. I think just an apology should suffice and he probably will really appreciate my generosity.) [SisDomPath] [SisGoodPath]":
            $ sisdom += 1
            $ sisgood += 1
            scene sismeeting20 with mediumdissolve
            sis "I'm not going to punish you Mr. Goon, so I hope you can learn from this mistake going forward. But I want another apology."
            ua "Yes! I am so so sorry! I am just a stupid servant who screwed up! Thank you Mistress for sparing me!"
            a "Very merficul of you [pname3], but don't always be so nice to the point where people run over you! Well, we now have this settled..."
            jump sismeetingthree
        "(It seems like he prefers a little pain to a demotion. Maybe I should go that route.) [SisDomPath]":
            $ sisdom += 1
            scene sismeeting22 with mediumdissolve
            sis "I'm going to give you some pain Mr. Goon. How does that work Alessandra?"
            a "Since this is your first time and your voice is not activated on this servant to give pain, please leave it to me. I'll show you kind of what I might normally do, if that's ok?"
            sis "Ok."
            scene sismeeting23 with mediumdissolve
            a "Servant 112 Pain Stomach. Now apologize and thank [pname3] for your pain as well."
            ua "Arrrgh! I'm sorry again Mistress, and thank you for the pain. I deserve it..."
            a "I usually run this about a minute or so, but he really did something pretty bad in scaring you so much. I won't object if you want him to suffer a little more."
            menu:
                "(I think the current punishment is enough.)":
                    scene sismeeting24 with mediumdissolve
                    sis "No, a minute is fine."
                    a "Hear that simpleton? You better thank her for being merciful, and you really, really, have to make it up to her."
                    ua "Yes! Uggghh, thank you! Err, thank you Mistress!"
                    a "Good. Servant 112 Pain Off. Now that we have that little matter settled..."
                    jump sismeetingthree
                "(I think I want to see him suffer a little more.) [SisEvilPath]":
                    $ sisevil += 1
                    scene sismeeting25 with mediumdissolve
                    sis "Alessandra, I think I want see him to suffer a little more."
                    a "Very well [pname3], I want to wrap this up so I will just increase the pain rather than making it too long."
                    a "Servant 112 Pain Chest, Head, Butt."
                    scene sismeeting26 with mediumdissolve
                    ua "Arrgggh, no please! I beg you Mistress, I am so sorry!!!"
                    a "You're lucky I'm not Juliette! You'd better be thankful you are dealing with me! Now thank [pname3] for your punishment!"
                    scene sismeeting27 with longdissolve
                    ua "Thank you Mistress [pname3], thank you for punishing me for my unworthy duties!"
                    a "Good boy. That's enough. Servant 112 Pain Off. Now, I am glad we have this little problem settled..."
                    jump sismeetingthree
        "(He's most terrified of being demoted. I want him to suffer his worst punishment.) [SisDomPath] [SisEvilPath]":
            $ sisevil += 1
            $ sisdom += 1
            scene sismeeting26b with longdissolve
            sis "You really scared me to death. You deserve a very serious punishment, so I'm demoting you to Level 5, was it?"
            ua "Nooooooo!! Please! I'm sorry!"
            ua "I'll do anything! Please please!"
            menu:
                "(I think I've done enough and maybe I did the right thing to show Alessandra I can handle myself.)":
                    scene sismeeting27b with mediumdissolve
                    sis "That's enough! I've decided."
                    ua "Yes, Mistress. Sorry..."
                    a "Excellent [pname3], you are a little crueler than me, but you handled this well! I am glad we have this little problem settled."
                "(Am I actually enjoying the power to crush this man's spirit? I think I want to demote him again for talking back to me.) [SisEvilPath]":
                    scene sismeeting28 with longdissolve
                    $ sisevil += 1
                    sis "How dare you talk back to me...I'm demoting you again to Level 4 now. And if you say anything more, it's going to get even worse."
                    ua "Oh no...sorr...sorry Mistress, I...oh no no no...oh..."
                    scene sismeeting29 with longdissolve
                    a "Oh my [pname3], so brutal, I think you might be breaking him. But, I think if I got such a scare, I might be pretty severe too."
                    a "But now I am glad we have this litle matter settled."
                    jump sismeetingthree

label sismeetingthree:

    stop seven fadeout 3
    scene sismeeting30 with longfade
    a "Now you've bothered us enough, get out and reflect on your stupidity and how to serve better."
    ua "Yes, Mistress Alessandra."
    scene sismeeting31 with longfade
    sis "Can you tell me now what's going on? Why did you bring me?"
    a "Is it ok if we wait until tomorrow? I'd like to show you a few places I bet you have never seen, and we can spend the day together."
    a "I also have an appointment to call my sister Veronica very soon out in Africa, and I won't have enough time for us without having to cut it short."
    sis "But I'd really like to know why I am here and about [pname] too."
    scene sismeeting32 with mediumdissolve

    play seven "music/relax.mp3" fadein 2

    a "I can understand your worries, but I promise you I am a bearer of good news for you, and I'm actually really tired too. Let's rest and talk in the morning."
    sis "I'm disappointed, but I understand. Is it possible to get a ride back home then? I think I am pretty far from my place."
    a "Absolutely not! This room right here is yours to use and enjoy!"
    scene sismeeting33 with quickdissolve
    sis "This room? Oh wow, just the shower and tub..."
    a "Haha, enjoy it [pname3]! Oh, you have no clothes or anything else."
    scene sismeeting34 with mediumdissolve
    a "The bathroom should be fine for your needs, but clothes. Hmm. You are slender like me, but you might be a tad too tall for some of my outfits."
    a "Just in case, I think you would easily fit my sister Dominique's clothes. She's tall and lean like you and I can access her room here and get you something."
    sis "Oh, thank you! I really appreciate being able to use this room."
    scene sismeeting35 with mediumdissolve
    a "Great, it's settled! Stay here tonight and sleep in tomorrow too! Just dial 7 on the phone in here to grab me, I will let you sleep as long as you want!"
    sis "Oh I'm sorry Alessandra, but I work at 10 tomorrow, I just remembered."
    a "[pname3], don't worry about that job. I want to save everything for tomorrow, but I guess I have to at least give away that you have a much better job offer coming tomorrow."
    scene sismeeting36 with quickdissolve
    sis "Really? What?"
    a "No! Let me have my fun tomorrow! Just relax tonight, and we'll talk tomorrow."
    sis "Ok, thank you Alessandra."
    a "Enjoy the room and relax! Bye!"

    stop seven fadeout 2
    scene sismeeting37 with longfade
    sis "(Oh wow...what a day...)"
    jump endcuts

label endcuts:
    play one "audio/heart.mp3" fadein 1

    scene endcuts1 with longfade

    play seven "music/tsg.mp3" fadein 2
    sis "(How much longer can [pname4] go on?)"
    scene endcuts2 with longfade
    stop one fadeout 1
    sis "(And what is happening with [pname]?)"
    scene endcuts3 with longfade
    sis "(But what a room this is! Just the bathroom is like the size of my entire rental! And this tub! Oh my God! So awesome!)"
    sis "(I hope everything works out...)"
    scene black with longfade
    sis "(...No one saves us but ourselves. We ourselves must walk the path...)"
    sis "(Time to walk...)"

    stop seven fadeout 1
    jump zend

label zend:

    pause 2

    scene zendsavegame with longfade

    $ renpy.pause (4.0, hard=True)

    z "Episode 2 awaits! Enjoy!"
    jump episodetwostart

label episodetwostart:

    scene chess1 with superfade

    play music "<from 178 to 184>music/darkness.mp3" fadein 1

    $ renpy.pause (6.0, hard=True)

    jump patmeeting

label patmeeting:

    stop music fadeout 1
    scene black with longfade

    play seven "<from 1 to 69>music/solitary.mp3" fadein 2

    pp "Authorization P12749, Gudinna Vault Access 26666, Patricia!"
    scene e2patmeeting1 with superfade
    pp "(Ok, don't show you're nervous...)"
    scene e2patmeeting2 with longfade
    pp "Grym Gudinna, I'm here as requested. I am alone for voice communication."
    scene e2patmeeting3 with longfade
    xx "Very good Patricia. And just Mistress is fine for this report. Just tell me what I asked for only."
    if elena_mentor:
        scene e2patmeeting4 with mediumdissolve
        pp "Mistress, [pname] passed Elena's interview and she intends to mentor him."
        xx "Interesting. Continue."
        jump patmeetingtwo
    elif dom >= 3:
        scene e2patmeeting4 with mediumdissolve
        pp "Mistress, [pname] has already shown dominant tendencies but he did not pass Elena's interview for mentoring."
        xx "Very well. Continue."
        jump patmeetingtwo
    elif sub >= 3:
        scene e2patmeeting5 with mediumdissolve
        pp "Mistress, [pname] has initially shown some submissive tendencies."
        xx "Does it seem natural to you, or rather, does it feel like he is just trying to survive?"
        scene e2patmeeting6 with mediumdissolve
        if sub >=4:
            pp "The extreme circumstances may have awakened his true submissive nature. That is my guess so far, Mistress."
            xx "I see. Change your guess to something more concrete and find out. Continue."
            jump patmeetingtwo
        else:
            pp "Mistress, I'm not sure yet."
            xx "Find out."
            jump patmeetingtwo
    else:
        scene e2patmeeting7 with mediumdissolve
        pp "Mistress, [pname] is very hard to read so far. He hasn't clearly shown a specific tendency."
        xx "Keep testing him and find out. Continue."
        jump patmeetingtwo

label patmeetingtwo:

    scene e2patmeeting8 with longfade
    pp "Yes, Mistress. Elena also asked the punishment question."
    xx "And?"
    if samsadist:
        pp "He chose Samantha."
        xx "I see. Do you think he enjoyed watching it?"
        if good >= 3:
            scene e2patmeeting9 with mediumdissolve
            pp "I'm not really sure, he seems to have some good in him too."
            jump patmeetingthree
        elif evil >= 4:
            scene e2patmeeting9 with mediumdissolve
            pp "I'm not really sure, but maybe. I think he has a strong evil streak inside of him."
            jump patmeetingthree
        else:
            pp "I'm honestly not sure Mistress."
            jump patmeetingthree
    if patpunish:
        pp "He chose me."
        xx "Did you enjoy yourself?"
        scene e2patmeeting10 with mediumdissolve
        pp "Yes, but I behaved as instructed by you Mistress."
        xx "Good."
        jump patmeetingthree
    else:
        pp "[pname] chose solitary punishment for the prisoner."
        xx "Perhaps playing it safe without more information."
        jump patmeetingthree

label patmeetingthree:

    scene e2patmeeting11 with longdissolve
    xx "And everything is on schedule I take it?"
    pp "Mistress, the initial prep training will begin today. 12 candidates right now."
    xx "Make sure you train [pname] and [pname2] personally if possible."
    pp "I will try Mistress, but Sam outranks me."
    scene e2patmeeting12 with quickdissolve
    xx "I understand your situation, but do your best. I am concerned that Samantha is too loose a cannon."
    xx "[pname] must not be seriously hurt or injured before he starts the real program. Punishments are fine if that is what he has earned."
    pp "I understand, Mistress."
    scene e2patmeeting13 with quickdissolve
    xx "Anything else?"
    pp "I don't think so, Mistress. I will do whatever I can, but can you tell me what you really want from [pname] so I can help you best?"
    scene e2patmeeting14 with quickdissolve
    xx "No Patricia, but I will at least tell you that I need to know if [pname] will be someone I want to truly be with, just fuck, enslave...or destroy."
    xx "The kind of man he really is deep down will determine what I do. Not what he is on the surface. That is all you need to know."
    pp "I understand, Mistress. I will obey and serve as best I can."
    scene e2patmeeting15 with quickdissolve
    xx "Good. Continue as planned. I shall have the chance to explore the real [pname] for myself soon enough."
    pp "Yes, Mistress."
    jump sisjobofferone

label sisjobofferone:

    stop seven fadeout 2

    play seven "music/allesandra.mp3" fadein 2

    scene e2sisjoboffer1 with superfade
    sis "This is such an incredible place Alessandra! So beautiful."
    a "Thank you [pname3], it was a joy designing this place for myself. It's one of my little sanctuaries away from the world."
    a "Even two of my sisters haven't been here before. Only my sister Veronica has been here, so it's rare for me to have visitors here."
    sis "Hearing that, I appreciate seeing this place even more. I can't believe how wonderfully you are treating me."
    scene e2sisjoboffer1b with mediumdissolve
    a "Well [pname3], I think you will enjoy our next conversation even more. I imagine you are anxious to talk about everything."
    sis "I am. This...I mean, everything. Why offer me a job? I'm sure you know I have no amazing educational background or credentials."
    a "Yes, but you have been vetted very carefully. We believe you may be perfect for this job. But this also involves [pname], so we have to be sure."
    scene e2sisjoboffer2 with mediumdissolve
    sis "How?"
    a "Let's go sit and talk. And let's start with your brother. Just so you know, he has been offered a position with the Karlsson Group under a special training program for prisoners."
    a "I don't want to go too deep into the details, but basically if he can do well in our program and successfully finish six months, he is a free man and has a job offer with our company."
    scene e2sisjoboffer3 with mediumdissolve
    sis "Wow, that seems very generous. What's the catch?"
    a "You assume the worst of us [pname3]? A wise instinct to be honest. The catch is that he can fail and go back to jail or even worse as the program can be very tough on people."
    sis "(Even worse than jail...)"
    scene e2sisjoboffer3b with mediumdissolve
    sis "Hmm, can you tell me some more details about it?"
    a "Actually, I will likely be giving a lot of this information to you later, but for now, the main point to understand is that almost all of the prisoners fail the program."
    sis "Why?"
    scene e2sisjoboffer4 with quickdissolve
    a "Because it is designed that way. It's very unfair at times, and only the strongest, brightest, and best can realistically finish it successfully."
    a "And I'm not going to sugarcoat or lie about this program to you [pname3]. It's even designed to make many of them suffer and be humiliated for the enjoyment of...others."
    a "But it is possible to do well in the program, and The Karlsson Group can respect a man tough enough to survive. That respect translates to a great job and future with us."
    menu:
        "Show anger at the thought of your own brother having to endure such treatment in this program. [SisGoodPath]":
            scene e2sisjoboffer5b with mediumdissolve
            $ sisgood += 1
            $ sis_a_p -= 1
            sis "[pname] is going to have to suffer and be humiliated? For the enjoyment of others?! What kind of program is this!?"
            a "A program where he has a chance to actually make it in life versus five years in jail and probably no future! Think of that reality."
            a "Isn't a small chance to have a real life better than his current situation? Does he really have that much to lose?"
            sis "(Maybe...)"
            jump sisjoboffertwo
        "Show confidence in [pname] and tell Alessandra that he can successfully do the program. [SisBroPath]":
            scene e2sisjoboffer5 with mediumdissolve
            $ sis_bro_p += 1
            sis "Whatever you throw at [pname], he can handle it. I think he'll be able to make it just fine."
            a "I am glad you show such confidence in him. I guess we will see how right you are, won't we?"
            jump sisjoboffertwo
        "Question out loud the coincidence and timing of your possible job offer and your brother's situation. [SisPath]":
            scene e2sisjoboffer5 with mediumdissolve
            $ sis_a_p += 1
            sis "I have to believe it's no coincidence that both [pname] and I have been contacted by the Karlsson Group at the same time."
            a "You really are a smart girl [pname3]! But perhaps one of you drew attention to the other. Or maybe not."
            jump sisjoboffertwo

label sisjoboffertwo:

    scene e2sisjoboffer6 with longdissolve
    a "Now believe me, we will get back to [pname] in much greater detail later, but I want to talk about you right now. I want to talk about your future."
    sis "Ah, are you finally going to offer me a job now? I'm really anxious to hear what you have in mind."

    stop seven fadeout 2

    scene e2sisjoboffer7 with mediumdissolve

    play seven "music/sisoffer.mp3" fadein 2

    a "Now the first thing I want to say up front is that this position is formally for six months to see if you fit what we need. If you do well, a new and improved permanent position awaits you."
    sis "(Six months...just like...)"
    a "Don't stress super hard about the six months [pname3]. Unlike [pname]'s program, it's not designed to make you struggle! But you still have to perform."
    scene e2sisjoboffer8 with longdissolve
    a "Now, don't react too quickly when I talk about your possible job. It may surprise you what we have in mind, but promise to hear me out until the end?"
    sis "Of course, but just tell me already please!"
    a "Ok [pname3], the reason I just said that I might be sharing a lot more about the prisoner training program with you is because..."
    scene e2sisjoboffer8b with mediumdissolve
    a "...The Karlsson Group wants you to be the main day to day manager of this program."
    sis "Wait, what? But you just said my own brother is..."
    scene e2sisjoboffer8c with mediumdissolve
    a "...We know that. So you will still be under myself and my three sisters for the program just in case. But we have vetted you carefully and feel you can do it even with [pname] there."
    sis "(This...is...)"
    a "Can you run such a program? Knowing [pname] might have to be under your direct supervision, and knowing it's designed to be hard on him?"
    menu:
        "State your doubt that you can handle being in charge of your own brother in such a program. [SisSubPath]":
            scene e2sisjoboffer8d with mediumdissolve
            $ sissub += 1
            sis "I'm...I'm not sure I can handle that so easily. But I can try my best."
            a "Good [pname3], that's all we ask for now. Your best effort."
            jump sisjobofferthree
        "(Lie) I will treat him the same as any other person in the program without special treatment (unless I can help him quietly). [SisGoodPath] [SisBroPath]":
            $ sisgood += 1
            $ sis_bro_p += 1
            scene e2sisjoboffer8e with mediumdissolve
            sis "I will treat him the same as everyone else if that's what the job requires. I can do it."
            a "Very good [pname3], I know it could be awkward or even worse, but I think personally you have what it takes."
            jump sisjobofferthree
        "(Truth) I will treat him the same as any other person in the program without special treatment.":
            scene e2sisjoboffer8e with mediumdissolve
            sis "I will treat him the same as everyone else if that's what the job requires. I can do it."
            a "Very good [pname3], if you can be counted on to run things well yourself, we will definitely give you a great deal of latitude in running things."
            jump sisjobofferthree
        "State confidently you will run the program extremely well no matter who is there and that The Karlsson Group need not worry at all. [SisDomPath]":
            scene e2sisjoboffer8f with longdissolve
            $ sisdom += 1
            sis "Don't worry Alessandra, I will run the program extremely well. Even with [pname] there I will make sure The Karlsson Group is happy with my work."
            a "I love your answer [pname3]! I think our faith in you will prove very correct."
            jump sisjobofferthree

label sisjobofferthree:

    scene e2sisjoboffer9 with mediumdissolve
    a "Don't worry about all the details yet, I will give you a lot of prep information ahead of time. But your job is to make sure the prisoners provide maximum value to the Karlsson Group."
    sis "What does that really mean? What value?"
    a "We want this program over six months to produce a few strong men that can actually work for us, and also...entertainment from the rest. Your job is to help us achieve that goal."

    stop seven fadeout 2

    scene e2sisjoboffer10 with longfade
    sis "Ok, can you be more specific about what you mean by entertainment? I think I have a guess, but if I'm supposed to manage this, I better know everything."
    a "Of course [pname3], these men being prisoners is no accident. They are powerless and must serve us, and they will endure many entertaining things we...and of course you...desire."
    a "And I do mean anything. Physically. Mentally. The limits of your power over all of them is your own imagination."
    sis "So can I literally just do anything to any of them? At any time?"
    scene e2sisjoboffer11 with mediumdissolve
    a "Well, for example abusing a prisoner just on a whim could be a waste of resources. So it has to be within the structure of the program, but you will be given great...flexibility if you can be trusted."
    a "You will have a lot of authority to implement challenges, rules, and other things to make the program run as well as possible. We will provide input and advice too."
    a "And of course some of us will have very specific things we want to do, so at times we will control things. But I will try and keep my sisters off your back if you are doing well."
    scene e2sisjoboffer12 with longdissolve
    sis "Wow. This is a lot to take in. I guess I have to ask at some point. What about salary? Benefits?"
    a "Oh good! Something easy and pleasant! You are in my domain now, so I am very straight and to the point about finances. Your offer is $8,000."
    scene e2sisjoboffer12b with quickdissolve
    sis "Oh wow! That's way more than I was making at my job. I was only making about $1,000 a year!"
    scene e2sisjoboffer13b with quickdissolve
    a "Oh [pname3], I'm so sorry for laughing at your sad and poor life before but I can't help it, haha!"
    scene e2sisjoboffer13c with quickdissolve
    sis "What's so funny?"
    scene e2sisjoboffer13 with mediumdissolve
    a "Just the thought it would never occur to you that the offered number isn't an annual one. It's so different being poor. And I'm sorry for being rude, it was my natural reaction."
    a "The offer is $8,000. Not per year. Per week. And you can use your hotel room for free until you want to get your own place."
    scene e2sisjoboffer14 with longdissolve
    sis "Per...week? Oh my God! I guess I just lost all bargaining power with my reaction!"

    play eight "music/oliviasoft.mp3" fadein 2

    a "Haha, it's ok [pname3]. Now one thing I want to make clear is that no one else in the program can know you and [pname] are related. It's probably better for [pname] too when you think about it."
    scene e2sisjoboffer15 with mediumdissolve
    a "I'm also going to give you a $5,000 signing bonus that I expect you to use on some nice outfits and accessories so you can look like a proper Karlsson executive."
    if sis_a_p >= 2:
        $ sisbonus = True
        a "And since I control all the books for the entire company...and you've been so nice to me, I'm going to throw in a surprise bonus for you later. And you can't ask! Shhh...haha!"
        jump sisjobofferfour
    else:
        a "I want you to get comfortable and ready for the position!"
        jump sisjobofferfour

label sisjobofferfour:
    scene e2sisjoboffer16 with longdissolve
    sis "Alessandra, I don't know what else to say..."
    a "Just say yes to the offer sweetie!"
    sis "Ok, yes! And I still can't figure out why you are willing to do all this for me, but I will do my best."
    scene e2sisjoboffer17 with mediumdissolve
    sis "It's...it's just hard to believe everything, you know you easily could have offered way less money to hire me and yet you are extremely generous."
    a "I can imagine how unbelievable or even suspicious this might be to you, but all I can say is that personally I really do want you to succeed."
    scene e2sisjoboffer18 with mediumdissolve
    a "If you can perform well, you can be so much more [pname3]. You can be like us...rich, powerful..."
    a "...and being able to indulge in any, and I mean any, desire you want. But baby steps first, just do the best you can with this opportunity."
    scene e2sisjoboffer18b with quickdissolve
    sis "Ok, I will."
    scene e2sisjoboffer19 with longfade
    a "But enough talk of work, plenty of time for that later. I see our food has arrived! Let's have you indulge in a more simple pleasure first!"
    sis "Sounds great!"
    scene e2sisjoboffer20 with longdissolve
    a "If you'd rather not sit in the sun, I can have our food moved into the shade."
    sis "No, it's lovely outside today, let's enjoy it where it is!"
    scene e2sisjoboffer21 with mediumdissolve
    a "Ah, it looks wonderful Nathan, nice job. Maybe I really will give you a small pay raise if you keep this up."
    nath "Thank you, Mistress Alessandra. I do my best to serve you."
    a "Good, now this woman here is Mistress [pname3]. You will obey her the same as me. Don't make her unhappy for any reason."
    scene e2sisjoboffer22 with mediumdissolve
    nath "Yes, Mistress."
    a "So [pname3], Nathan here has been asking for a small pay raise."
    sis "How much is he asking for?"
    scene e2sisjoboffer23 with longdissolve
    a "He currently makes $12 a week and wants a $3 a week pay raise. He says it will help take care of his unemployed brother too."
    sis "Oh! Three dollars. Has he been an excellent servant for you? How long since he got a raise?"
    a "He's been a good servant, but not perfect and he hasn't received a raise in about three years of service. What do you think?"

    stop eight fadeout 3
    menu:
        "It's her servant, I don't think it's my place to tell her what to do. [SisSubPath]":
            scene e2sisjoboffer23b with mediumdissolve
            $ sissub += 1
            sis "I don't think it's my place to tell you what to do with him. I am sure you know best."
            a "Ok [pname3], I'm not going to make a decision yet anyway. Understand Nathan?"
            nath "Yes, Mistress, thank you!"
            jump sisjobofferfive
        "Maybe I can show some mercy and offer to take out $3 of my own pay for him. I will never miss such a small amount of money. [SisGoodPath]":
            scene e2sisjoboffer23b with mediumdissolve
            $ sisgood += 2
            $ sis_d_p += 1
            sis "You can take $3 a week from my own pay for his raise, I'll never miss it."
            a "Wow, so generous [pname3]! You better thank her for this Nathan!"
            nath "Thank you Mistress [pname3]! I don't deserve your generosity!"
            jump sisjobofferfive
        "I should show some thought behind this and suggest no pay raise until I get a chance to see for myself if he's worth it. [SisDomPath]":
            scene e2sisjoboffer23c with mediumdissolve
            $ sisdom += 1
            sis "I don't think it's fair for me to say what he should or should not get until I see him work. I want to judge him myself."
            a "You're absolutely right [pname3]! Nathan, you need to prove yourself a little more to get that $3. So impress Mistress [pname3]."
            nath "Yes, Mistress Alessandra."
            jump sisjobofferfive
        "I'll show Alessandra I can be ruthless by making him suffer. I'll recommend a pay cut of $3 a week for him and that it be transferred to my own pay as a raise for myself. [SisEvilPath]":
            scene e2sisjoboffer23d with mediumdissolve
            $ poornath = True
            $ sisevil += 2
            sis "You know Alessandra, I think he looks like a terrible servant. And we're not a charity that should just pay someone extra to help a brother. I think you should cut his pay by $3..."
            sis "...and give it to me instead. I'm only making $8,000 a week, and I really need to be making $8,003 a week."
            scene e2sisjoboffer24 with quickdissolve
            nath "What? But!"
            a "Silence Nathan! [pname3], that figure is supposed to be confidential, haha! But Nathan has already forgotten it, haven't you?"
            nath "Yes...but please don't cut my pay!"
            scene e2sisjoboffer25 with mediumdissolve
            a "I'm sorry, but I really need my new hire to be happy. I'm cutting your pay but if you please both of us we can talk in say six months about getting that $3 back."
            nath "I...yes Mistress."
            jump sisjobofferfive

label sisjobofferfive:
    scene e2sisjoboffer25b with longdissolve
    a "Now go away Nathan, make sure to clean all of my vehicles here by tonight as I don't know which one I want to use later."
    nath "Yes, Mistress."
    scene e2sisjoboffer26 with superfade
    a "Now, we can talk more about everything later, but for now, let's just enjoy our food!"
    sis "Mmm, this looks delicious Alessandra!"
    jump patofferone

label patofferone:

    scene black with longfade
    p "(Lunch...)"
    if selfisheater:
        scene e2patoffer1 with mediumfade
        p "(Samantha really wasn't kidding about choosing the food for myself. It's a huge upgrade from my slop.)"
        jump patoffertwo
    else:
        scene e2patoffer2 with mediumfade
        p "(Sigh, different day, same shit food...but now I have a spoon! Oh Sam really went all out this time...)"
        jump patoffertwo

label patoffertwo:
    scene e2patoffer3 with longfade

    play five "music/hallway.mp3" fadein 2

    pp "Enjoying yourself [pname]?"
    if selfisheater:
        scene e2patoffer3b with mediumdissolve
        p "It's nice to be able to eat fresh food for once. But I think guards get even better food than this so did Samamtha hold out on me? You guards have it pretty good I imagine."
        pp "Yes we do, but I think you already know the best perks for us have nothing to do with food."
        pp "And that food should last you a while too. Don't eat it all at once [pname], you never know with Sam what could happen next."
        jump patofferthree
    else:
        scene e2patoffer3c with mediumdissolve
        p "Oh sure, this is just perfect for my nutritional needs."
        pp "I hear you had a chance to get better food and you declined. That's your own fault [pname]."
        pp "And let me tell you, the food I just had was so lovely."
        jump patofferthree

label patofferthree:
    scene e2patoffer4 with longdissolve
    pp "Hmm, I think the hair works for you, I knew you would clean up well. Still too greasy, dirty, and stringy though, clean it up before training today [pname]."
    scene e2patoffer4b with mediumdissolve
    pp "I want to discuss something with you. Move over to the bed. I'll save your food for later. You can eat after we finish."
    p "Alright."
    scene e2patoffer5 with longfade
    pp "Now [pname], today you are going to do a little training and testing in preparation for the real inmate rehabilitation program."
    pp "How you do today could greatly impact your future in the actual program later."
    p "How?"
    scene e2patoffer6 with mediumdissolve
    pp "Your performance here today can determine your employee level when you leave this prison and start working."
    p "Levels? Like ranks?"
    scene e2patoffer7 with mediumdissolve
    pp "Yes, exactly that. You want to be as high as possible when you start."
    p "What's the difference between the levels?"
    scene e2patoffer8 with mediumdissolve
    pp "I honestly don't know. That's up to whoever is managing the program to decide I suppose."
    pp "But I know with a lower rank, you are in a much weaker position of power. Also the pay is different as well."
    scene e2patoffer9 with mediumdissolve
    pp "Even worse for you is if you completely fail the training today. That would be very bad for you."
    p "Ok, but why are you telling me all this right now?"
    scene e2patoffer10 with mediumdissolve
    pp "Well...[pname], a certain someone in this room will be testing you today."
    pp "Maybe I could make your day go very well, but I could also ensure that you do very, very, poorly. You could even fail."
    scene e2patoffer11 with mediumdissolve
    p "Ok. I get it. What do you want from me?"
    pp "Good [pname], I'm glad we understand each other. Let me get to what I really want..."

    if pat_secpath:
        scene e2patoffer12 with longfade
        pp "Now, you told me last night you would want to hire me if you had power. I've thought about that a lot this morning."
        pp "I believe it's possible you may actually acquire power someday with The Karlsson Group."
        scene e2patoffer13 with mediumdissolve
        pp "So I want to propose a deal. I help you do well today, and you help me later."
        p "What kind of help do you want from me?"
        pp "I don't know yet because you have no power today. Only that maybe later you will. If that happens, I want you to remember my help, and return the favor."
        scene e2patoffer14 with mediumdissolve
        p "There's no guarantee I could get anything."
        pp "Of course. I know that. But remember [pname], I grew up poor and powerless like you, and many Karlsson employees don't know what that is like. I do."
        pp "And I've learned that to survive, you never needlessly close the door of an opportunity to enrich yourself. You might be that for me."
        scene e2patoffer15 with mediumdissolve
        pp "But don't get any grand ideas of betraying me later. I still have friends in high places. Very high."
        pp "And I need a few things from you today to make me really help you."
        jump pattermsone
    elif dom >= 3:
        scene e2patoffer12 with longdissolve
        pp "Now, you've done well to show some dominance so far [pname]. And I have thought about you a lot this morning."
        pp "I believe you have a chance to acquire more power someday as part of The Karlsson Group."
        scene e2patoffer16 with mediumdissolve
        pp "Because of that, I want to propose a deal. I help you today, and you help me later if you are in a position to do so later."
        p "What kind of help do you want?"
        pp "You have no power right now so I can't give a specific example. But maybe later you will have such power. If so, you better remember my help and return the favor."
        scene e2patoffer15 with mediumdissolve
        pp "But think hard if you plan to try and use that power against me later. You'd be surprised what I am capable of."
        pp "And I will need a few things from you today as well to make me really help you."
        jump pattermsone
    elif sub >= 2:
        scene e2patoffer18 with mediumdissolve

        stop five fadeout 2
        pp "Poor little [pname], so helpless right now. Maybe I should just fail you...I bet Sam would really like that too."
        p "(Ugh!)"

        play seven "music/pattest2.mp3" fadein 2

        jump pattermstwo
    else:
        scene e2patoffer12 with longdissolve
        pp "Now, I can't get a good read on you yet [pname], but I do think it's possible someday you could actually help me."
        p "How?"
        pp "By acquiring power over time. I'm not sure you can do it yet, but I'm willing to take a chance on it."
        scene e2patoffer13 with mediumdissolve
        pp "So I want to propose to you a deal. I help you do well today, and in the future you return the favor if you ever manage to actually gain any power."
        p "What kind of help?"
        pp "I don't know yet because you have no power right now. But maybe later that changes."
        scene e2patoffer17 with mediumdissolve
        pp "But I do want a few things from you today for my direct help."
        jump pattermsone


label pattermsone:

    scene e2patoffer19 with longdissolve
    p "Ok, what do you want from me?"
    pp "Let's see..."
    scene e2patoffer20 with longfade
    pp "Three things. First, you will not cause trouble for me today or help or even encourage in any way your fellow trainees. They are on their own as it should be. This includes [pname2] too."
    pp "Two, you will address me as Mistress during the training like any other normal trainee. I will not make you do anything too degrading or humiliating if you hold up your end of the bargain."
    pp "Three, if you sense anyone is close to mentally or physically breaking, I want you to signal me somehow. A simple hand gesture like fingers up somehow is enough. I will understand."
    scene e2patoffer21 with mediumdissolve
    pp "If you agree to all of this, I will help ensure that you do very well today. I can't guarantee perfection as I can't do everything for you, but I can do what I can to help."
    pp "That is my offer for today. Accept it or not, I leave that up to you right now."
    menu:
        "Accept Patricia's offer [PatriciaPath]":
            scene e2patoffer22 with mediumdissolve
            $ pat_p += 2
            $ patdealyes = True
            p "I have to accept. It makes too much sense."
            pp "Very good [pname], I think this could end up helping both of us. And maybe I'll really let you play later if it goes well. Enjoy your food and see you shortly."

            stop five fadeout 2

            jump jakeone
        "Reject her offer":
            scene e2patoffer23 with mediumdissolve
            $ pat_p -= 2
            $ patdealno = True
            p "I have to say no."
            pp "I see [pname]. You are making a big mistake. But, so be it. I will see you shortly. Enjoy your food while you can."

            stop five fadeout 2

            jump jakeone

label pattermstwo:

    scene e2patsub1 with longdissolve
    pp "Maybe your entire future depends on today. A lot of pressure on you."
    pp "Hmmm, what ever shall I do [pname]? It's SO hard to decide what to do today..."
    menu:
        "Beg with everything you have for her to show you mercy, and be clear that you will do anything she says. [SlavePath] [SubPath]":
            scene e2patsub2 with mediumdissolve
            $ slavepoints += 3
            $ sub += 2
            $ beggarboy = True
            $ patdealno = True
            p "Please Patrcia, have mercy on me today. I will do anything you ask. Anything."
            pp "I know...it's so pathetic but I do believe you really would do anything."
            scene e2patsub2b with mediumdissolve
            pp "Such a worthless worm. I had such high hopes for you, and I thought you could rise up like I did and more. But you're actually weak and useless."
            pp "Only useful as a toy for amusement. Maybe even your poor little sick brother is more of a man than you."
            scene e2patsub3 with mediumdissolve
            pp "Now, I think I want you on your knees in the middle of the cell here."
            pp "Get over there worm..."
            scene e2patsub4 with longfade
            pp "Ahh, much better! What to do...what to do."
            pp "If you want to survive today, you better behave very well with whatever I want right now [pname]."
            scene e2patsub4b with mediumdissolve
            pp "Now...What kind of fun should I have with you?"
            menu:
                "I think I want to sit on [pname]'s poor little face for a bit! [gr]\[Facesitting\]":
                    scene e2patsub5 with mediumdissolve
                    pp "[pname], I'm going to just sit down and think a little more about this. On your face."
                    p "(Oh...)"
                    scene e2patsub6 with longdissolve
                    pp "But my pants feel so uncomfortable. I think you need to feel my bare ass so I can think more clearly about today!"
                    pp "Get on the floor there [pname]."
                    jump patfacesitting
                "I think he needs to worship my feet and move up to my ass and pussy a little. [gr]\[FeetWorship\]":
                    scene e2patsub7 with mediumdissolve
                    pp "Little worm, I think you need to worship my feet and move up my body to help me relax for your training."
                    pp "If you do a good job and please me, I just may decide to show a little mercy on you today."
                    scene e2patsub8 with mediumdissolve
                    pp "I'm sure you want to make me happy, don't you [pname]?"
                    jump patworship
                "I think I want to tease his worthless dick but then deny him any pleasure. [gr]\[Denial\]":
                    scene e2patsub8b with mediumdissolve
                    pp "You know [pname], I almost feel sorry for you. I bet you'd love to fuck me or Sam if you could."
                    pp "Maybe I can help you feel better...your poor little thing down there must be starved for attention."
                    scene e2patsub9 with mediumdissolve
                    pp "Wouldn't you like that [pname]? Yes, I bet you would. Let's play a little."
                    pp "Go ahead and take your pants off and lie down. Keep your hands flat and your sides too. I don't want you touching me with your hands."
                    jump patdenial
        "Stay silent and don't beg for mercy. [DomPath]":
            scene e2patsub10 with mediumdissolve
            $ patdealno = True
            pp "Oh, you have nothing to say on your behalf [pname]? I'm so disappointed in you, I really thought you could rise up like I did and more."
            pp "Instead, you're weak and deserve to stay on the ground as a poor beggar. So beg for me to take it easy on you today."
            menu:
                "I think I better listen to her this time. I might really need her help today.":
                    scene e2patsub11 with mediumdissolve
                    $ sub += 1
                    $ slavepoints += 1
                    p "Ok. Please Guard..."
                    pp "That's Mistress to you!"
                    p "Mistress Patricia, please help me do well in training today."
                    scene e2patsub12 with mediumdissolve
                    pp "Hmm, I might be tempted to help you...if you do something for me right now."
                    p "What do you want?"
                    scene e2patsub13 with mediumdissolve
                    pp "I think I want to have a little fun with you, but I'll at least give you a choice!"
                    pp "You can serve as a seat for my ass, you can get on your knees and worship me, or I can play with your cock a little."
                    menu:
                        "Ass seat? Why not. [gr]\[Facesitting\]":
                            scene e2patsub14 with mediumdissolve
                            p "I'll help you sit comfortably."
                            pp "Interesting decision [pname]. But my pants feel so uncomfortable. I think you need to feel my bare ass while I decide your fate."
                            p "(Oh...)"
                            jump patfacesitting
                        "Worshipping Patricia doesn't sound too bad... [gr]\[FeetWorship\]":
                            scene e2patsub15 with mediumdissolve
                            p "I'll worship you. Where should I start?"
                            pp "You'll start at the bottom. Where the worms live and crawl."
                            jump patworship
                        "I really could use some pleasure. Maybe she will actually let me get off if she plays with my dick. [gr]\[Denial\]":
                            scene e2patsub16 with mediumdissolve
                            p "I guess I'd like for you to play with my dick a little please."
                            pp "Hmm, go ahead and take your pants off and lie down. Hands flat and still too."
                            pp "I think I will enjoy this. But don't be sure you will [pname]."
                            p "(Uh oh...)"
                            jump patdenial
                "I'm not going to just beg for her mercy. I won't do it.":
                    scene e2patsub17 with mediumdissolve
                    $ dom += 1
                    p "I'm not going to just beg for your mercy. Maybe you'll just have to do what you have to do."
                    pp "Oh, you actually said no to me? You seemed so submissive before, so this is very interesting. Maybe there is hope for you [pname]."
                    scene e2patsub18 with mediumdissolve
                    pp "But unfortunately for you, you should have had a backbone earlier. I won't help you today. And I will do what I have to do."
                    pp "Enjoy your food while you can. I'll be seeing you."
                    jump jakeone

label patfacesitting:

    scene e2patface1 with longfade

    stop seven fadeout 2

    pp "Don't take this personally [pname]. I have to take advantage and treat you like garbage. If I don't do that, then I might end up being the garbage."
    pp "You should have figured this out by now too. So get ready for my ass."
    scene e2patface2 with mediumdissolve

    play seven "<from 36 to 188>music/femdom2.mp3" fadein 2

    pp "Ahh, now let's just relax. Make sure to lick everywhere really well!"
    p "(Umph, little heavier than I expected...)"
    scene e2patface3 with mediumdissolve
    pp "Not bad [pname]! Maybe this is a natural thing for you."
    pp "A little higher please, you're not hitting my sweet spot!"
    scene e2patface4 with mediumdissolve
    pp "There you go. I want to hear how beautiful my ass is too."
    p "(...) Mpmmhh."
    pp "Well?"
    scene e2patface5 with mediumdissolve
    pp "I guess you need to feel it a little better! Hold on..."
    pp "Up we go and..."
    scene e2patface6 with quickdissolve
    pp "...down!"
    p "(Ugh!)"
    scene e2patface7 with mediumdissolve
    pp "I think one more time won't hurt will it [pname]?"
    pp "Let me even get my feet off the ground with a full jump and drop this time!"
    scene e2patface8 with quickdissolve
    p "(ooooof!)"
    pp "Oh! Did that hurt?"
    scene e2patface9 with mediumdissolve
    pp "Now worship me perfectly or I'm going to keep grinding on you harder and harder..."
    pp "I really am so annoyed at your pathetic nature, I was hoping you could be valuable to me."
    scene e2patface10 with mediumdissolve
    p "(Shit, she's trying to make me lick her...)"
    pp "Keep going [pname]! I'm not super thrilled right now, so I'm going to cover your whole face again!"
    scene e2patface11 with mediumdissolve
    pp "Oh, I can feel you really struggling now!"
    pp "I'm not Sam, so I'll let you breathe a little here and there."
    scene e2patface12 with quickdissolve
    pp "There we go. Ah sweet relief, isn't it?"
    scene e2patface13 with mediumdissolve
    pp "And keep licking!"
    pp "(Hmm, I feel so naughty, and feel a little gas coming down there...do I even?)"
    menu:
        "Let loose some gas on his poor face. [SlavePath] [SubPath]":
            scene e2patface14 with mediumdissolve
            $ slavepoints += 3
            $ sub += 1
            pp "Ahhh, why don't you enjoy something special from me. So nice to let it out."
            p "(What the fu...omg!)"
            pp "Hahaha!"
            scene e2patface14b with quickdissolve
            pp "Oh my [pname], how incredibly degrading for you, haha! I almost can't view you as a human being now!"
            scene e2patface15 with mediumdissolve
            pp "To have to lie there and get humiliated that way, that's so horrible!"
            pp "I really wanted to fuck you when you first arrived at this jail, and look at you now!"
            jump patfacesittingtwo
        "No, that's a little too disgusting.":
            scene e2patface16 with mediumdissolve
            pp "You don't even know how lucky you are [pname], I could be degrading you so much more right now. You should appreciate my generosity."
            jump patfacesittingtwo

label patfacesittingtwo:

    scene e2patface17 with mediumdissolve
    pp "Now you need to get up and kneel behind my butt, I'm almost done!"
    scene e2patface18 with longfade
    pp "Suck and lick me with everything you got, and maybe I'll be merciful at your training today!"
    pp "Come on worm, finish it up and...ahh, good."
    scene e2patface19 with mediumdissolve
    pp "Right there you little worm!"
    scene e2patface20 with mediumdissolve
    pp "Oh yes..."
    scene e2patface21 with longflash
    pp "Yes! Good job [pname]!"
    scene e2patface22 with longfade
    pp "[pname], you did so well as a face seat slut. Maybe you can do that for all of the Karlsson sisters and their friends at one of their famous parties!"
    pp "Just literally kiss ass over and over. What fun for you!"
    scene e2patface23 with longdissolve
    pp "Now get back on the ground. I'm done with you."
    scene e2patface23b with longdissolve
    pp "I'm tempted to just have you lick my ass and pussy during the entire training today while the others actually get tested, but believe it or not, I am a fair woman [pname]."
    scene e2patface24 with longdissolve
    pp "So do your best today, I'll be watching..."
    jump jakeone

label patworship:

    stop seven fadeout 2

    scene e2patworship1 with longfade
    pp "Now [pname], in my position here, I have to take advantage and treat you like garbage. If I don't do that, then I might end up being the garbage."
    pp "Don't take it personally. I'm not completely heartless like Sam. I just want what's best for me and that means right now you have to serve me."
    scene e2patworship2 with mediumdissolve

    play seven "<from 36 to 188>music/femdom2.mp3"

    pp "In fact, I want to show you that I'm not a complete bitch. I'm going to let you choose how to start with my worship."
    pp "You can lick my boots with your tongue, or I can take them off and you can lick my feet instead. Either is ok with me as I only want to look down at your submissive face."
    menu:
        "I'd like to lick Patricia's boots.":
            scene e2patworship3 with mediumdissolve
            p "I guess I'll lick your boots if I can choose."
            pp "Wonderful! Get to work."
            scene e2patworship4 with longfade
            pp "I love these boots [pname], they are perfect for stomping any prisoners that get out of line."
            pp "Plus, I think they look very sexy, don't you agree [pname]?"
            scene e2patworship5 with mediumdissolve
            pp "Move up my boots, make sure to look up at times so I can enjoy seeing your sad face."
            scene e2patworship5b with mediumdissolve
            pp "Yes, just like that. I do wish I had even more power than I do right now so I could do this more often."
            scene e2patworship5c with mediumdissolve
            pp "I have to be honest [pname], and tell you that I get off on the mental humiliation of boots more than feet but physically your tongue doesn't do much for me on a boot."
            scene e2patworship5d with mediumdissolve
            pp "But that's ok, you will be licking my skin soon enough."
            scene e2patworship6 with longdissolve
            pp "Mmmm, good [pname]. One last lick from the bottom part of my other boot to remind you of your worm status."
            pp "I think that's enough with my boots and I'd like to take them off now."
            jump patworshiptwo
        "I'd like to lick Patricia's feet.":
            scene e2patworship3 with mediumdissolve
            p "I guess I'll lick your feet given the choice."
            pp "Wonderful! Let me take off my boots so you can get to work."
            scene e2patworship3b with longfade
            pp "Now take special care of my feet [pname], and I won't use them against you today."
            scene e2patworship7 with longdissolve
            pp "I used to work in the fields [pname] when I was younger. You know what that can do to one's feet."
            scene e2patworship7b with longdissolve
            pp "I had to do a lot to get them back into a presentable state. I hope you can appreciate them down there."
            scene e2patworship8 with mediumdissolve
            pp "Not bad, mmmm, very relaxing and nothing annoying like a ticklish feeling. Maybe you were born to be a footslave."
            scene e2patworship9 with mediumdissolve
            pp "I have to be honest with you [pname]. I get off more on the mental humiliation of a worm licking my boots more than my feet."
            scene e2patworship9b with mediumdissolve
            pp "But physically, it's no contest. Your tongue does feel so good."
            scene e2patworship10 with mediumdissolve
            pp "I was so unhappy at first at how submissive you turned out to be, but now looking at you...I think you belong at my feet."
            scene e2patworship11 with mediumdissolve
            pp "Mmm, that's enough, I think it's time to move up my body now. Let me get a little more comfortable too..."
            jump patworshiptwo

label patworshiptwo:

    scene e2patworship12 with longfade
    pp "There have been many, many, men that have desired my long legs. What a treat for you to lick them."
    scene e2patworship13 with mediumdissolve
    pp "Go slowly up my legs. Enjoying my smell? Can you almost taste my pussy so close to your face?"
    pp "Or the residue of the smell of my leather boots mixed with my sweat and pussy juices slowly leaking out..."
    scene e2patworship14 with mediumdissolve
    pp "Uh uh, no pussy for you yet. Stay with my inner thighs."
    pp "Good job [pname], you see how nice I can be sometimes? Sam would probably just be torturing you at this point."
    scene e2patworship14b with mediumdissolve
    pp "Go behind and worship my tight ass. Not my asshole, I'll save that for another day."
    scene e2patworship15 with longdissolve
    pp "I worked so hard to maintain my shape you know. Hours and hours of exercise day after day to make my body what it is today."
    pp "My looks were my only way out."
    scene e2patworship16 with mediumdissolve
    pp "That's why I'm the one on top and you're licking me from below. Willpower. Nothing would stop me from escaping poverty. No matter what."
    scene e2patworship17 with mediumdissolve
    pp "Good. You can move around to right above my pussy and then go slowly down."
    scene e2patworship18 with longdissolve
    pp "Mmm, wonderful. I'm almost tempted to help you today at training. But I won't."
    pp "I would have helped you if I thought you could help me someday, but I'm not convinced of that at all right now."
    scene e2patworship19 with mediumdissolve
    pp "Ah, the final stop. Beg to lick my pussy and I might let you do it."
    menu:
        "Do a really good job begging Patricia to lick her pussy. [SubPath] [PatriciaPath]":
            scene e2patworship20 with mediumdissolve
            $ slavepoints += 1
            $ sub += 1
            p "Please let me lick your pussy Mistress Patricia."
            pp "Tell me you are a pathetic worm, and I'll let you do it."
            p "I'm...I'm a worthless worm Mistress. I'm pathetic."
            scene e2patworship21 with mediumdissolve
            pp "So pitiful. I'm almost ashamed I wanted to fuck you before."
            pp "I'm also so jealous of how much fun the Karlssons will have with you when you get out of here. But go ahead and lick."
            jump patworshipthree
        "Do a poor job of begging by saying almost nothing and stating you don't know what to say. [SlavePath]":
            scene e2patworship21b with mediumdissolve
            $ slavepoints += 3
            $ pat_p -= 1
            p "I..."
            scene e2patworship22 with mediumdissolve
            pp "Well?"
            p "I...I don't know what to say."
            scene e2patworship23 with mediumdissolve
            pp "*slap* Worthless worm. You are definitely hurting yourself for today's testing."
            pp "Not only are you worthless as a real man, you are even bad at begging! Are you good at anything? Just get in there and lick!"
            jump patworshipthree

label patworshipthree:

    scene e2patworship24 with longdissolve
    pp "To tell you the truth [pname], I'm already about to cum. Having my body touched like that already has me going..."
    scene e2patworship25 with mediumdissolve
    pp "But you need to finish me off. Maybe...just maybe I'll be a little lenient on you out there today if I get off."
    scene e2patworship26 with longdissolve
    pp "Oh, that's it, keep going!"
    scene e2patworship26b with mediumdissolve
    pp "It's so nice having this much control. If only I could do even more like Grym...err...keep licking!"
    p "(What was that?)"
    scene e2patworship27 with mediumdissolve
    pp "Just a little more..."
    scene e2patworship28 with mediumdissolve
    pp "Almost..."
    scene e2patworship29 with mediumflash
    pp "Almost..."
    scene e2patworship30 with mediumflash
    pp "Yes!"
    scene e2patworship31 with longfade
    pp "Ah, I'd just love to help you [pname], but what can you offer me now that I am done with you here?"
    pp "You won't survive the Karlssons with your personality when you get out of here."
    scene e2patworship32 with longdissolve
    pp "So you are on your own today out there! Have fun trying!"
    p "(Oof!)"
    scene e2patworship33 with longfade
    pp "Haha, I understand so much better the rush of watching helpless people at your mercy. I want more so badly. What power I have right now isn't nearly enough for my desires."
    scene e2patworship34 with mediumdissolve
    pp "But at least I'm not someone like you right now. But do your best today, I'll be watching..."
    jump jakeone

label patdenial:

    stop seven fadeout 2

    scene e2patdenial1 with longfade
    pp "Now [pname], don't cry or take it so personally if I treat you like garbage. If I don't, I could end up as the garbage instead."
    pp "But I have to admit, I am starting to enjoy my power and freedom the more I use it."
    scene e2patdenial2 with mediumdissolve

    play seven "<from 36 to 188>music/femdom2.mp3"

    pp "Hmm, I only saw your dick once when you first checked in this jail, [pname]."
    pp "Looking at it again, it's...good. At least you have something down there. Oh, it grew nicely there didn't it, haha!"
    scene e2patdenial3 with mediumdissolve
    pp "But I want to hear you beg for me to play with your dick. And that's Mistress Patricia to you."
    pp "The better you do at begging, the better I may do for you."
    menu:
        "Give it your best effort begging Patricia to play with your dick. [SubPath] [SlavePath]":
            scene e2patdenial4 with mediumdissolve
            $ slavepoints += 1
            $ sub += 1
            p "Please Mistress Patricia, I beg you to play with my dick."
            pp "Mmmhmm, and tell me about your penis."
            menu:
                "(I think she wants to hear me degrade my penis by calling it worthless without her.) [SlavePath]":
                    scene e2patdenial5 with mediumdissolve
                    $ slavepoints += 2
                    p "My penis is useless and worthless without your help. Please help me."
                    scene e2patdenial5b with mediumdissolve
                    pp "Good answer [pname], maybe I will help you out a little."
                    jump patdenialtwo
                "(Don't give her that much satisfaction, tell her it has its uses.)":
                    scene e2patdenial6 with mediumdissolve
                    p "I think my penis can have its uses at times."
                    scene e2patdenial6b with mediumdissolve
                    pp "Ahhh, I detect a little pride in yourself there [pname]. Good. Maybe there is hope for you as a man yet."
                    pp "I think I will play with it a little."
                    jump patdenialtwo
        "Give a half hearted effort begging Patricia.":
            scene e2patdenial7 with mediumdissolve
            p "Umm, can you use my penis...and...ummm"
            pp "Oh [pname], you are just terrible at this begging thing. Maybe that's not the worst thing though..."
            pp "I guess I'll see what your thing can do."
            jump patdenialtwo

label patdenialtwo:

    scene e2patdenial8 with longfade
    pp "I want to see this up close. This might be the only time you ever see me on the floor [pname]. Let's see how quickly I can get you going."
    pp "It must be torture for you to be stuck in here without any women to enjoy."
    scene e2patdenial9 with mediumdissolve
    pp "But I bet you are masturbating a lot in your cell. Do you picture me at all in your mind when you do that? If so, what do you imagine?"
    menu:
        "Having Patricia on her knees serving my needs. [PatriciaPath] [DomPath]":
            scene e2patdenial10 with mediumdissolve
            $ dom += 1
            $ pat_p += 1
            p "I imagine you on your knees serving all of my sexual needs."
            pp "Oh! A little aggression from the worm! You should have shown this earlier, you might have been in a different situation right now."
            jump patdenialthree
        "Being on my knees serving all of Patricia's needs. [SubPath]":
            scene e2patdenial11 with mediumdissolve
            $ sub += 1
            p "I imagine myself on my knees serving all of your needs and desires."
            pp "Oh [pname], that's so pathetically sweet and obedient. I am sure you will make the Karlssons very happy."
            jump patdenialthree
        "I don't think of Patricia at all when I do my thing in my cell.":
            scene e2patdenial12 with mediumdissolve
            $ pat_p -= 1
            p "I don't think of you when I am alone in my cell."
            pp "Oh, I'm SO hurt [pname], I thought we had something special, haha! Maybe my hand won't even do anything for you right now?"
            jump patdenialthree
        "I don't masturbate in my cell.":
            scene e2patdenial12 with mediumdissolve
            $ pat_p -= 1
            p "I don't masturbate in my cell at all."
            pp "Oh [pname], did you forget you are watched 24/7 by camera? I think we both know you are lying right now."
            jump patdenialthree

label patdenialthree:

    scene e2patdenial13 with longdissolve
    pp "But let's see how you respond to a little more speed."
    scene e2patdenial14 with mediumdissolve
    pp "Not bad [pname], your dick could actually please a woman if you knew how to use it."
    pp "But it's your brain that's the problem right now. What a waste."
    scene e2patdenial15 with mediumdissolve
    p "(Oh wow, I'm getting closer.)"
    pp "Oh, you look quite pleased with yourself. I guess I'm pretty good at this, aren't I? And no no, keep your hands down!"
    scene e2patdenial16 with mediumdissolve
    pp "I think you better get used to the idea that your penis is no longer your own."
    scene e2patdenial17 with mediumdissolve
    pp "Maybe they'll lock it up in a cage where you can never use it at all!"
    scene e2patdenial18 with mediumdissolve
    pp "And your nice large thing will slowly shrink...and shrink until it's a useless stub of a tool."
    pp "I think you know this is a real possibility with the type of people you will be dealing with everyday."
    scene e2patdenial19 with mediumdissolve
    pp "So you better get it all out right now, shouldn't you?"
    scene e2patdenial20 with mediumdissolve
    pp "I'd almost love to take daily pictures of your penis [pname], watching it get more pathetic and small day after day."
    scene e2patdenial21 with quickdissolve
    pp "Oh! Watching your face and feeling you, I know you are really close!"
    pp "Beg for me to finish you off!"
    menu:
        "Beg. [SubPath]":
            scene e2patdenial22 with mediumdissolve
            $ sub += 1
            p "Please finish me off!"
            pp "That's a good worm...but it really doesn't matter if you begged or not..."
            jump patdenialfour
        "Don't say anything.":
            scene e2patdenial23 with mediumdissolve
            p "(.......)"
            pp "Oh [pname], no begging? It's ok, it doesn't make a difference either way for me this time..."
            jump patdenialfour

label patdenialfour:
    scene e2patdenial24 with longdissolve
    pp "...because I'm going to squeeze, hit, and ruin your orgasm instead, haha!"
    p "Aaagh! (Damnit...talk about blueballing ugh...!)"
    scene e2patdenial25 with mediumdissolve
    pp "There is no way I would let you cum if I haven't [pname]!"
    pp "Even if I had, I still probably don't let you cum! Now stand up."
    scene e2patdenial26 with longfade
    pp "Don't you dare touch yourself in front of me."
    pp "Maybe you will never ever cum again after you leave here, haha! Better get off by yourself in this cell while you can."
    scene e2patdenial27 with longdissolve
    pp "Actually, let me touch your penis one last time!"
    scene e2patdenial27b with quickdissolve
    p "Ugh!"
    scene e2patdenial28 with longfade
    p "Why even do that?! Didn't you have enough fun already?!"
    pp "I told you [pname], if I don't step all over you, someone else will step all over me. Someone is always watching. Always."
    pp "But I'm starting to enjoy my small power and I find myself wanting more."
    scene e2patdenial29 with mediumdissolve
    pp "Now I will be fair [pname], and maybe, just maybe, I won't try and fail you today at training. If you don't upset me. But I won't help you either."
    pp "Sucks to be you, but you had your chance for better treatment. I suggest you do your best today, I'll be watching..."
    jump jakeone

label jakeone:

    stop seven fadeout 2



    scene e2jake1 with longfade
    pbf "[pname]! Your seat is on the left here."
    p "(A classroom? I wish our cells were this bright and nice.) [pname2], good to see you."

    play seven "music/jakechill.mp3" fadein 3

    scene e2jake2 with longdissolve
    pbf "Oh, I get it. Black guy gets white shirt, white guy gets black shirt. Obviously some coded meaning!"
    p "No clue man, but let me know when you crack the code. Anyway, anything weird happen to you since we last spoke?"
    scene e2jake3 with longdissolve
    pbf "No, it's been quiet for me. I didn't even hear any prisoners screaming last night in agony."
    if friend >= 1:
        pbf "[pname], Sam told me my meal today was thanks to you...I mean, seriously, I appreciate it, but take care of yourself too."
        p "I'm good, and besides, you'd have my back too right? "
        scene e2jake4 with mediumdissolve
        pbf "Well obviously, but only if I could have [pname3] as a reward too!"
        p "Hah, dream on! I think it's clear what your chances with her are after all your sad attempts."
        pbf "[pname3] is just scared that if she goes black she will never go back and..."
        p "...Woah woah stop it! You're starting to put the wrong imagery in my head!"
        jump jaketwo
    else:
        scene e2jake4 with mediumdissolve
        pbf "I spent last night fantasizing about getting an extra large pizza at Luigi's with all of my rent money, and of course, [pname3]."
        p "Hah, dream on! I think it's clear what she thinks of you after all your sad attempts with her."
        pbf "[pname3] is just scared that if she goes black she will never go back..."
        p "Oh man, come on, give it a rest."
        jump jaketwo

label jaketwo:

    scene e2jake5 with longdissolve
    pbf "But I really do hope she is ok. [pname4] too."
    p "Yeah. It sucks bad enough being stuck here, but having no clue about the outside world too..."
    scene e2jake6 with longdissolve
    pbf "Oh...look at this guy."
    pbf "Hey there, what's your name?"
    scene e2jake7 with mediumdissolve
    zach "Z..z...Zach. I don't wanna talk...sorry."
    pbf "It's ok, your charming personality might be too overwhelming for me!"
    scene e2jake8 with mediumdissolve
    pbf "Pssst...so how is THAT guy somehow here under the same standards that got us in this situation? It makes me feel like a real loser now."
    pbf "But look at his shirt [pname]! White guy, black shirt again. Makes you think?"
    p "Don't you think we need to focus on our situation?"
    scene e2jake9 with mediumdissolve
    pbf "We need to be able to relax too [pname], being too wound up won't help us either."
    p "Ok, fair enough. But we need to do as well as possible today."
    scene e2jake10 with mediumdissolve
    pbf "Alright, one last bit of fun, and I'm down for all business."
    pbf "*whispering* I bet they might be listening, but I have to ask? Who you taking? Sam or Pat?"
    p "What?"
    scene e2jake11 with mediumdissolve
    pbf "You. A room. A bed. Sam or Pat?"
    menu:
        "Samantha is definitely a scary chick but there's something about her and she's damn hot... [SamamthaPath]":
            scene e2jake12 with mediumdissolve
            $ sam_p += 1
            p "I have to go with Sam I guess. But I wonder if it's worth the risk."
            pbf "I hear you [pname], and you have to admit, she's tight in all the right places."
            jump jakethree
        "Patricia is more interesting to me, and she looks damn good... [PatriciaPath]":
            scene e2jake12 with mediumdissolve
            $ pat_p += 1
            p "I would say Patricia. I think she's more my type than Sam if I had to choose one."
            pbf "I hear you [pname], and her long legs and lean body. Oh yes..."
            jump jakethree
        "Why not both at the same time? [FriendPath]":
            $ friend += 1
            scene e2jake13 with mediumdissolve
            p "Well [pname2], your question is flawed and missing the correct choice. The correct answer is both of them at the same time!"
            pbf "Now there you go [pname]! This is why I'll always have your back. Because of your enlightened mind."
            jump jakethree
        "Give a little scolding about needing to concentrate on the task at hand. [VeronicaPath]":
            $ friend -= 1
            $ veronica_p += 1
            scene e2jake14 with mediumdissolve
            p "[pname2]! I don't know, shit, we need to focus on what's happening today! A lot is at stake, don't you know that?"
            pbf "Of course I know that, but I'm just trying to lighten the mood right now. Sorry Dad."
            jump jakethree

label jakethree:

    scene e2jake15 with longfade
    pbf "So I get that we have some kind of testing today, but what does it all mean? You seem to be the VIP prisoner with your own cell and all, do you know anything else?"

    stop seven fadeout 3

    menu:
        "I think I should share what I know including my meeting with Pat, he's my best friend and I could use his help today and beyond [SlavePath] [FriendPath]":
            $ slavepoints += 1
            $ friend += 1
            scene e2jake16 with mediumdissolve
            p "So Patricia came and met with me earlier. She told me how we do today impacts our starting overall employee level as she called it when we start working."
            p "She warned that we want to be a higher level employee because it impacts our pay and overall privileges and work."
            scene e2jake17 with mediumdissolve
            pbf "Is that right? Shit, I wonder why she told you though ahead of time."
            if sub >= 3:
                p "It was just an excuse for her to try and dominate me in private. Nothing worth talking about."
                pbf "Damn [pname]. Sorry."
                jump jakefour
            else:
                p "(I better not piss off Pat too much by disclosing every little detail...) She just wanted to mess with me. Nothing worth talking about."
                pbf "I gotcha [pname], I guess we just have to do the best we can today."
                jump jakefour
        "I should share a little about what I have heard, but not disclose that I met Patricia as that might piss her off":
            scene e2jake16 with mediumdissolve
            p "So I've heard that our performance today impacts our employee level when we start working."
            pbf "Employee level? What does that mean?"
            p "My guess is that it impacts our type of work, privileges, and pay."
            scene e2jake18 with mediumdissolve
            pbf "Wait, we are going to get paid? Actual money?"
            p "I think so? Samantha didn't mention that to you?"
            pbf "I don't remember hearing that. Probably slave wages though."
            jump jakefour
        "I better not say anything at all. Especially talking about Patricia meeting me, I am quite sure that would alter how she treats me today [_SlavePath]":
            scene e2jake19 with mediumdissolve
            $ slavepoints -= 1
            p "I really haven't heard anything, but I think it's safe to say we better kick ass today as best as we can."
            pbf "I'm with you. And we got this."
            jump jakefour

label jakefour:

    scene e2jake20 with superfade

    play seven "music/samintro.mp3" fadein 2

    pp2 "Ah three more little pigs! Sit down! It's time to start!"
    scene e2jake20b with longfade
    pp2 "Well hello boys! Welcome to your first official day as the new guinea pigs of The Karlsson Group!"
    pp2 "It's a step up from being a rat, so congratulations! This is our guard classroom, so you should feel lucky you can use it instead of your sad facilities!"
    scene e2jake21 with longdissolve
    pp2 "Now, I don't have much time to talk as I have another assignment outside of the prison today, so let's do this quick and dirty!"
    pp2 "I bet some of you pigs like it that way too!"
    pp2 "This is the start of your employee testing and training for placement at The Karlsson Group's inmate rehabilitation program."
    scene e2jake22 with mediumdissolve
    pp2 "There are 12 of you that have been selected, and you have been split into four groups of three."
    pp2 "I have already tested my two groups of three, and right now Patricia is administering physical testing on a third group."
    scene e2jake23 with mediumdissolve
    pp2 "She will do the same with your group after you finish here."
    pp2 "When you finish today, you will be evaluated and ultimately placed on an employee level between 4 and 6. This will be designated as K4, K5, and so on."
    pp2 "Your first job, pay, privileges, and even the tiniest details like your sleeping arrangements and toiletries could be determined by your initial placement."
    scene e2jake24 with mediumdissolve
    pp2 "Most of you pigs are stupid and pathetic. Weak. So many of you will start at K4. But a few of you might do better."
    pp2 "After you start the program, you will be able to move up and down from K1 all the way to K10 depending how you do."
    scene e2jake25 with longdissolve
    pp2 "As for today, the first part is simple...well...for those of you with a brain. You will have a set of questions on your computer that you are expected to answer to the best of your ability."
    pp2 "This test will be about 60 questions and you have two hours to finish everything."
    scene e2jake26 with longdissolve
    pp2 "You will quickly see that is not a test of knowledge, but instead a test about how you think and what you might do in specific situations."
    pp2 "So that's it! Get started!"
    scene e2jake27 with longfade
    pbf "Fuck me...we're back in school, you know how that went for me [pname]."
    p "Let's just get to it..."

    stop seven fadeout 2

    jump julietteone

label julietteone:

    scene black with superfade
    gary "(Ugh, what the hell...what happened...that guy just whacked me on the...)"
    scene e2juliette1 with longfade

    play five "music/fore.mp3" fadein 2

    j "Oh Gary Gary Gary, how unhappy I am with you. But I'm so glad you could visit me today!"
    j "This nice little room will allow us to bond and develop a greater understanding of each other. Welcome!"
    gary "(Oh my God, oh shit...)"
    scene e2juliette2 with longdissolve
    j "So, on to our business today. I only gave you a few simple tasks and you failed to deliver anything of value to me."
    gary "Mistress Juliette, I am trying! Give me more time!"
    scene e2juliette3 with mediumdissolve
    j "My father's true goals remain a mystery, and they are right there at your firm. Somewhere."
    j "And yet, you haven't found anything that can give me an advantage over my sisters. A top executive that knows little to nothing!"
    scene e2juliette4 with mediumdissolve
    gary "Mistress, I'm sorry! Your father...he set it up extremely well, he has safeguards to prevent anyone from finding out everything!"
    gary "I only have access to mostly what you have! You must go through and win his Gambit to get everything! More instructions will leak over time as he intends it!"
    scene e2juliette5 with mediumdissolve
    j "And yet, I know that my sister Veronica has been visiting your firm for some reason. On numerous occasions."
    j "And your own words betray you. You said mostly what I have, which means you have information I do not right now!"
    scene e2juliette6 with mediumdissolve
    j "So I better know right now every single thing you do. Or you will see the true depths of what I can do to make someone suffer."
    j "In fact, let's give you an itty bitty taste. I have a few things here to help you get motivated."
    scene e2juliette7 with longfade
    gary "Please Mistress, I could be ruined...it could hurt you too if you are found to have too much information!"
    j "Mmmhmm..."
    scene e2juliette7b with quickdissolve
    j "Silly fool, like anyone could ever pry from me that I have extra information! And I think you do need to be ruined...just a little right now."
    scene e2juliette8 with mediumdissolve
    gary "*thwack! thwack!* Agggghghhhh, please no!"
    j "Scream again and I double it! Once again Veronica receives special treatment! She was always Daddy's favorite!"
    j "The only way I could ever get his attention was to be as ruthless..."
    scene e2juliette9 with mediumdissolve
    gary "...But Mistress, she...she built up the entire division from nothing. Without Alexander, and it's the most profitable arm of the entire Karlsson portfolio."
    scene e2juliette10 with longdissolve
    j "And who do you think generated all those profits for her precious division!??? If she was the one forced to actually try and sell and close deals, the company would collapse within months!"
    j "Last chance, I want to know everything you know. Now!"
    scene e2juliette10b with mediumdissolve
    gary "*thwack! thwack!* MMMghgughhhhh! Ok Mistress. I will tell you the facts I know, and even share my speculations about things, but I may not be correct Mistress!"
    j "Good boy."
    scene e2juliette11 with quickdissolve
    gary "Yes, Veronica is visiting the firm. I do not know exactly why, but she goes to a private secure room and stays there for about an hour each time. No one else has access."
    j "What do you believe she is doing?"
    gary "I personally believe she is receiving further instructions from Alexander that he recorded before his death."
    scene e2juliette12 with quickdissolve
    j "My father always said this was supposed to be fair for all of us. But she's getting more information!"
    gary "May I give my theory about that Mistress?"
    j "Very well. Let's hear it."
    scene e2juliette13 with mediumdissolve
    gary "Mistress, if you were your father would you really want Veronica to take over your entire empire? With her charisma and personality? Or would you rather she stay where she is?"
    j "Hmm, now that actually makes some sense. Plus, I think she definitely wouldn't want it all either. So why is some information possibly going only to her?"
    scene e2juliette14 with quickdissolve
    gary "I believe someone has to ultimately judge who wins the Gambit. I think your sister is that person. But because of that, she won't be a contender for inheriting everything."
    gary "And I also imagine that her position in charge of the Research Division will be protected as a condition for inheriting your father's empire."
    scene e2juliette15 with quickdissolve
    j "She knows how I feel about her. That bitch will be able to screw me over if this is true."
    j "Veronica...that little...*thwack! thwack! thwack! thwack! thwack! thwack! thwack! thwack!*"
    scene e2juliette15b with longdissolve
    gary "Oh my God, please stop Mistress!"
    gary "Unngggh...! Sorry to disagree, but I don't think she will just screw you over. I think she will analyze it without much emotion and bias the same way she does everything else."
    gary "Makes even more sense to me why she would be a good judge in the eyes of Alexander. She isn't wired that way mentally, don't you agree Mistress!?"
    scene e2juliette16 with mediumdissolve
    j "Actually, I do agree. You may be right...good. And what about [pname], [pname3], and [pname4]'s role in all of this?"
    gary "I don't know. No one really does beyond the instructions you all have been given so far. Perhaps Veronica knows more, but I sure don't."
    scene e2juliette17 with quickdissolve
    gary "I do believe your sister has been tracking them for a while, even before Alexander died. But I don't really know, and I think that's all the info I have that is useful too."
    scene e2juliette18 with quickdissolve
    j "So it seems. You have provided me some valuable input today. But you could have shared that before today, and you didn't. So you need further punishment."
    gary "Wait, please Mistress! I didn't think you..."
    j "Quiet you pitiful excuse of a man! I swear what I wouldn't give to have a real man around!"
    scene e2juliette19 with mediumdissolve
    j "I've got some special restraints to tie you on the ground and I expect you to behave...but you will see a little more of my body, lucky you!"
    gary "Ye...yes Mistress."
    menu:
        "Continue femdom scene.":
            jump juliettetwo
        "Skip rest of femdom scene and continue story.":
            stop five fadeout 2
            jump ptrainone

label juliettetwo:

    stop five fadeout 2

    scene e2juliette20 with longfade
    j "Much better. I feel so much more comfortable too!"
    j "When I look at your pathetic dick, it just upsets me that you can't deliver a pleasing one to look at..."
    scene e2juliette21 with longdissolve

    play seven "music/juliette2.mp3" fadein 2

    j "So let's make it look a little better!"
    scene e2juliette22 with quickdissolve
    gary "Arrgh, no please! Please!"
    j "You know, the only time your face looks attractive is when it's in pain! At least you are good for something!"
    scene e2juliette23 with mediumdissolve
    j "Maybe it can look good in other ways!"
    j "I'm not too tall or heavy, so I think your face can handle a little pressure too!"
    scene e2juliette23b with mediumdissolve
    j "Let's see!"
    scene e2juliette23c with quickdissolve
    gary "Stop please, Mistress!"
    scene e2juliette24 with mediumdissolve
    j "Hmm, let's stomp your face a little more!"
    scene e2juliette24b with quickdissolve
    j "Yesss, haha!"
    gary "Aaaaaggghhhghgvnfggh!"
    j "But I can't really see your face. And I don't want to anymore. So let's try one more thing!"
    scene e2juliette25 with longfade
    j "I'll just sit right here and your new job starting right now is ass and pussy worship. So do well if you know what's good for you."
    j "I'll be such a sweet girl and give you a wonderful handjob too!"
    scene e2juliette26 with mediumdissolve
    j "And let's play a small game. Whoever cums first loses. So if you can make me cum before I get you off, you win and I'll just set you free to enjoy life!"
    j "But if you cum first, you lose and enjoy my continued hospitality here for a while longer!"
    scene e2juliette26b with mediumdissolve
    j "Of course, I'll only play if you want to, you can always refuse, right? So?"
    gary "I...I'll play to please you Mistress. I...will...I will do my best."
    j "Good, let's begin!"
    scene e2juliette27 with longdissolve
    j "Oh Gary, your dick really is so pathetic! Your little trophy wife must be so unhappy with it. Oh, maybe she will be happy if you vanish. She can enjoy your money plus find a real dick!"
    j "Or you know, if you are stuck here forever, maybe I will just take your wife and give her to Alessandra. I'm only into tormenting men, but maybe she would enjoy her..."
    scene e2juliette27b with mediumdissolve
    j "But I won't do anything to your wife if you object right now!"
    gary "Mpppghghg psdllxlxdd!"
    j "Oh, I didn't catch that! So sorry, but you have to speak clearly for me to understand! Guess I have to assume you don't object! I thought you actually loved her, guess not!"
    scene e2juliette28 with mediumdissolve
    j "I hope you can lick better than that, because you are definitely going to lose if you don't improve."
    j "Lick lick little Gary!"
    scene e2juliette29 with mediumdissolve
    j "Mmmm, better, better. I might keep you around for a...week...or...two..."
    scene e2juliette30 with mediumdissolve
    j "Oh, but you seem awfully close too. My God, look at your penis compared to just my little thumb...poor poor Gary!"
    scene e2juliette31 with mediumdissolve
    j "So wonderful isn't it? Your body so badly wants to release, but your mind desperately wants to stop..."
    gary "Mmppgg, pleszzz Mmmmstrrsss, pl.."
    scene e2juliette32 with mediumdissolve
    j "Cumming means your doom and your mind knows it, but you still can't control yourself. Oh, you ARE close now, haha!"
    scene e2juliette33 with mediumdissolve
    j "I'm pretty wet too now, maybe you have a chance!"
    scene e2juliette34 with longdissolve
    j "Oh wait, I forgot to use my other hand! How unfair! Let's make this more fun for you!"
    j "But two hands can't fit around your small thing! How funny!"
    gary "Ohmyggg..oh.."
    scene e2juliette35 with mediumdissolve
    gary "nnnnplllss, noo, no..."
    j "Is your life as you know it about to end? I can feel you're about to burst! But let's just stop your orgasm from happening right now! "
    scene e2juliette36 with mediumflash
    gary "Ouch, nooo!"
    j "Oh no Gary! Denied so harshly with a painful dribble instead of a wonderful explosion! Poor baby!"
    j "And you did technically cum. So you lose! I guess you love being around me all the time!"
    scene e2juliette37 with longfade
    j "Oh no Gary, are you ever going to see your wife again? Or anyone else but me?"
    gary "Please Mistress, I will...I will do anything...anything...I can still help you..."
    scene e2juliette38 with mediumdissolve
    j "Oh no, you're crying! Don't worry, I'm definitely the most fun Karlsson sister to be around! It won't be so bad, haha!"
    scene e2juliette39 with longdissolve
    j "A shattered man's tears, so tasty!"
    gary "Miissstress...please..."
    scene e2juliette40 with longdissolve
    j "Well, this was fun, but I think we both know what you really are. A useless loser. Luckily, I have another at your firm to take your place."
    j "Enjoy yourself here! I'll move you to a more private play area later. Have fun without me!"

    stop seven fadeout 2

    jump ptrainone

label ptrainone:

    play seven "music/testing.mp3" fadein 2

    scene e2ptrain1 with superfade
    p "(Ugh, this is brutal, so many weird questions...almost done at least. This damn so called relaxing music over the intercom doesn't help...did they make it this way on purpose?)"
    comp "{i} Question 58 -- You are in charge of a Karlsson mining operation in Africa. Some valuable equipment and 12 miners are suddenly trapped...{/i}"
    comp "{i} ...in a tunnel collapse. This particular tunnel was about 95 percent tapped out on value but your foreman is concerned about both the equipment...{/i}"
    comp "{i} ...and the workers. Which of the following four courses of action make the most sense to you based on this limited information?{/i}"
    menu:
        "A. Try and recover the equipment and workers and maximize the positive publicity as best as you can from the rescue regardless of short-term cost. [DominquePath] [GoodPath]":
            $ good += 1
            $ dominique_p += 1
            scene e2ptrain2 with mediumdissolve
            p "(I think Option A looks pretty good. I think you do the right thing when you can.)"
            jump ptraintwo
        "B. Calculate the value of the equipment and other variables long-term versus the cost of a recovery and rescue operation and implement the most cost effective plan over any other factor. [AlessandraPath]":
            $ alessandra_p += 1
            scene e2ptrain2 with mediumdissolve
            p "(I think Option B looks pretty good. The business is about profit above all. But I wonder about other future costs and problems with not rescuing the workers?)"
            jump ptraintwo
        "C. Quickly determine everyone who actually knows about the collapse and try to ensure complete silence to cover up the situation before deciding anything else. [VeronicaPath]":
            $ veronica_p += 1
            scene e2ptrain3 with mediumdissolve
            p "(I think Option C looks pretty good. You should ensure silence and do damage control to allow yourself time to make the best decision without worrying about publicity.)"
            jump ptraintwo
        "D. Go in and rescue a worker or two publicly for positive press as a miracle rescue, but secretly take the other workers for medical research or other illegal company operations. [JuliettePath] [EvilPath]":
            $ evil += 1
            $ juliette_p += 1
            scene e2ptrain4 with mediumdissolve
            p "(I think Option D looks pretty good. You rescue the equipment, get positive press, and I have no doubt The Karlsson Group could be this ruthless.)"
            jump ptraintwo

label ptraintwo:

    scene e2ptrain4b with mediumdissolve
    comp "{i} Question 59 -- You are in charge of a Karlsson top secret and extremely valuable medical research lab. One of your top researchers comes to you and tells you that...{/i}"
    comp "{i} ...he can't take the job anymore and that he questions doing some research he considers immoral. He tells you he wants to quit working here...{/i}"
    comp "{i} ...but that he will agree to a deal that he can never speak of this research or use it in any future job. What option below makes the most sense to you?{/i}"
    menu:
        "A. Investigate everything about him (and make a determination based on that) and decide if he can be trusted to leave the job, blackmailed to stay, or killed if necessary. [VeronicaPath]":
            $ veronica_p += 1
            scene e2ptrain5 with mediumdissolve
            p "(Option A could be a little brutal, but it makes sense to me to protect the research if he's a security risk.)"
            jump ptrainthree
        "B. Determine how valuable he actually is as a researcher versus other alternatives, and bribe him enough to stay if his value to the research exceeds other alternatives and the bribe. [AlessandraPath]":
            $ alessandra_p += 1
            scene e2ptrain5 with mediumdissolve
            p "(Hmm, Option B is sensible to me. If you can keep him this way, do it. But what if he can't be bought?)"
            jump ptrainthree
        "C. Don't let him leave. Keep him in the same research program. As a test subject. This will also help scare other researchers from having their own moral awakening. [JuliettePath] [EvilPath]":
            $ juliette_p += 1
            $ evil += 1
            scene e2ptrain6 with mediumdissolve
            p "(Option C is pretty extreme, but I have to think this research would have naturally some immorality behind it. It doesn't hurt to have a climate of fear to ensure obedience.)"
            jump ptrainthree
        "D. Look at ways to move the researcher into a less morally grey research area where his skills can still benefit the company. If that fails, allow him to leave with his proposed deal. [DominquePath] [GoodPath]":
            $ dominique_p += 1
            $ good += 1
            scene e2ptrain7 with mediumdissolve
            p "(Option D looks very reasonable. Maybe he can still be productive, but if not, you can still try and protect the research with this deal.)"
            jump ptrainthree

label ptrainthree:

    scene e2ptrain8 with mediumdissolve
    comp "{i} Final Question -- You are in charge of the entire Karlsson empire and you discover you are dying of a terminal illness. You have six months to live and must decide...{/i}"
    comp "{i} ...how best to give your empire to your numerous children. You are not convinced any of them are ready to run your empire.{/i}"
    comp "{i} Which of the options below might be best given this limited information?{/i}"
    p "(This question seems...hmmm)"
    menu:
        "A. Simply determine as best as you can which child is the best overall for everything, and award that child the bulk of the power and authority to run the company going forward. [gr]\[SoloPlayer\]":
            scene e2ptrain9 with mediumdissolve
            $ soloplayer = True
            p "(I think you need centralized authority at some point, too many chefs in the kitchen could create problems. Best to pick one.)"
            jump ptrainfour
        "B. Try and split up the empire to each child's strengths with a strong and unified Board to maximize the efficiency of everyone going forward. [gr]\[TeamPlayer\]":
            scene e2ptrain9 with mediumdissolve
            $ teamplayer = True
            p "(Ok, I think it's good to create a strong team. It might eliminate stupid mistakes and especially disaster from picking the wrong child.)"
            jump ptrainfour
        "C. Try and gather additional data even after your death, knowing that this process could end up being unhelpful, very beneficial, or even a complete disaster making things worse. [gr]\[GambitPlayer\]":
            scene e2ptrain10 with mediumdissolve
            $ gambitplayer = True
            p "(This answer is risky, but if you are not convinced about any of the kids, I say take the chance to try and get it right.)"
            jump ptrainfour

label ptrainfour:

    scene e2ptrain11 with longdissolve
    comp "{i} Thank you for taking this exam. You have completed all 60 questions.{/i}"

    stop seven fadeout 2
    p "(Whew! Thank God! I'm done.)"
    p "(Oh, that music has finally...)"
    scene e2ptrain12 with longdissolve
    p "(Wait, what the? My computer is glitching...)"
    hack "{i} Hello there [pname]. I'm glad you finished the test.{/i}"
    scene e2ptrain13 with mediumdissolve
    p "(Wait, what?)"
    hack "{i} Just read what I type quickly. You can't respond and I only have a little bit of time before I can be traced.{/i}"
    hack "{i} You are walking into a very difficult dance with danger all around you.{/i}"
    scene e2ptrain14 with mediumdissolve
    hack "{i} But you have one thing all of them will need from you. Discover what that is.{/i}"
    p "(Umm, so just tell me then?)"
    hack "{i} This is the question that will lead you towards that answer. With all of his money and power, what did Alexander Karlsson really want?{/i}"
    hack "{i} He didn't get it while alive, but he's still determined to get it even after his death.{/i}"
    scene e2ptrain15 with mediumdissolve
    hack "{i} Even the most accomplished and complex person can have a basic or even strange desire that goes unfilfilled. Sometimes it's not so simple.{/i}"
    hack "{i} But alas, so quickly our time is up. It's up to you. Farewell.{/i}"
    scene e2ptrain16 with longdissolve
    pp "*over intercom* Time's up! Wrap it up and leave everything right there! You can relax for 20 minutes in the common area before heading outside for testing!"
    pp "So hurry up and take a leak or shit or whatever and gather up your strength! You will need it soon!"
    p "(What the hell was that...I...)"
    scene e2ptrain17 with longdissolve
    pbf "Hey Earth to [pname]! Did you hear me? What's up man?"
    menu:
        "Share what happened with your computer. [FriendPath]":
            $ friend += 1
            scene e2ptrain17b with mediumdissolve
            p "[pname2], my computer got hacked, and I got a strange message on it. It just said figure out what Alexander Karlsson really wanted."
            pbf "What the hell does that mean? And a hacker? What is going on?"
            p "I don't know..."
            jump ptrainfive
        "Don't share what happened. [gr]\[HackerSecret\]":
            $ hackersecret = True
            scene e2ptrain17c with mediumdissolve
            p "Sorry [pname2], what was that?"
            jump ptrainfive

label ptrainfive:

    scene e2ptrain18 with mediumdissolve
    pbf "I have to say [pname], that test was brutal. I didn't even finish! Maybe I'd actually rather do the physical stuff!"
    p "I wouldn't be so sure about that, but I guess we'll find out in a little bit. Let's at least enjoy this break while it lasts."
    pbf "All good [pname], I hear you."
    jump sethone

label sethone:

    play seven "music/hospital.mp3" fadein 3

    scene e2seth1 with longfade
    ec "I'm giving you a chance to show you can be trusted at a much higher level, do not make me regret it."
    kk "I will not disappoint you, Mistress."
    scene e2seth2 with mediumdissolve
    ec "Good. I'm a little sad about your hair, I quite liked how colorful it was. But, you need to look professional right now and you can color it back later."
    ec "If you do your duties well today, I will reward you. You know I am always fair with those that are loyal and useful to me."
    kk "You have always treated me well, Mistress. I was very lucky to fall into your hands instead of someone else."
    scene e2seth3 with mediumdissolve
    ec "You see how your sister moved beyond her low station in life and is now a prized confidant of Veronica Karlsson. Not even a slave or servant anymore, but a true asset."
    ec "This is your chance here. [pname4] is a very important part of the Gambit, so you are being given a great deal of trust right now."
    ns "(Poor [pname4], nothing we can do...)"
    scene e2seth4 with mediumdissolve
    kk "I will make the most of it, Mistress. I am ready."
    if elena_mentor:
        ec "You certainly seemed ready with [pname] last night. You still want him as your first, don't you?"
        kk "Yes, Mistress. He is very hot to me."
        scene e2seth5 with mediumdissolve
        ec "Well, he may be off limits to you during the meat of Karlsson's Gambit. But, I may allow you to go back with Sam to the jail tonight."
        ec "You have earned quite a lot moving up from such a low position to where you are now. Perhaps you can have a little fun with [pname] before reporting back to me."
        kk "Oh, thank you Mistress!"
        jump sethtwo
    else:
        ec "I would not have given you this chance if I did not think you were ready. Prove me right."
        kk "Thank you, Mistress."
        scene e2seth6 with mediumdissolve
        ec "After you finish with your duty here, I want you to go back with Sam to the prison where [pname] is being released soon."
        ec "Poor [pname] might be desperate for any crumbs from a woman. I am allowing you the freedom to have a little fun with him but talk with Patricia first about that."
        kk "Oh? May I ask a question, Mistress? Is he...umm, is he...?"
        scene e2seth7 with mediumdissolve
        ec "...hot? I think you will be happy, assuming they have cleaned him up well. I saw him in less than ideal shape."
        ec "But don't wonder about [pname] right now, focus on [pname4] and playing your role perfectly. You can have some fun later if you are a good girl."
        kk "Of course, Mistress!"
        jump sethtwo

label sethtwo:

    scene e2seth8 with longdissolve
    ec "Here we are. Are you sure you are capable of doing what is necessary long-term? You may have to be extremely cruel and evil if necessary."
    kk "You have taught me the need to do whatever it takes to get what I want. No matter what. I have learned that lesson well, Mistress. I won't fail you."
    scene e2seth9 with mediumdissolve
    ec "I have faith in you Kitty. It's no accident you are my top servant, and I believe I understand who you truly are deep down. You would not have this chance without that belief."
    ec "Let's proceed. Oh, I do give you permission to correct me immediately if I accidently say Kitty."
    kk "As you command Mistress."

    stop seven fadeout 2

    jump seththree

label seththree:

    scene black with longfade
    bro "(Where is...wow my head actually feels good?! No pain, how!?)"
    scene e2seth10 with longfade

    play seven "music/seth.mp3" fadein 3

    bro "Wha...? Who..."
    scene e2seth11 with longdissolve
    ec "Hello there, [pname4], how are you feeling? Is your pain lower than normal?"
    bro "Err, yes! My head...it's not in pain. Just my body, and even that feels much better than it usually does. Who are you?"
    scene e2seth12 with mediumdissolve
    ec "My name is Elena Caspari, and I am the Senior Legal Officer for The Karlsson Group."
    scene e2seth12b with quickdissolve
    ec "Katherine here has administered a very special medicine to help you with your pain, but it can't alleviate all of it of course given your condition."
    ec "Your blanket is being changed too by Nurse Jones is it? And...I know you said your pain is lower than normal, but is this the best you have felt since your diagnosis?"
    scene e2seth13 with mediumdissolve
    bro "Yes! It is! I'm still in pain in my legs and chest, but I feel so much better than normal! I can sit up and even move my legs! Wow!"
    bro "Why have you done this? I mean, why are you here speaking to me?"
    scene e2seth14 with mediumdissolve
    ec "Well [pname4], I am here to help you. You have both [pname] and [pname3] to thank for this."
    bro "What? What's happened? [pname] is in jail for five...five years. And [pname3] is on her own all alone, how have they..."
    scene e2seth15 with mediumdissolve
    ec "Relax [pname4]. I have good news. Let's start with [pname]. He has been selected for a six month inmate rehabilitation program with our company."
    ec "If he can successfully finish it, he can get an early release from prison after those six months and a long-term job with us."
    menu:
        "Question her skeptically about how it benefits The Karlsson Group. [gr]\[BroEP +1\]":
            scene e2seth16 with mediumdissolve
            $ bro_e_p += 1
            bro "You're not doing this out of the goodness of your heart. How does it benefit your company?"
            ec "Fair question. It is good public relations and optics for us, but we also really are looking for diamonds in the rough so to speak."
            scene e2seth17 with mediumdissolve
            ec "[pname] was evaluated very carefully, and we feel he fits the profile of one who could take advantage of this opportunity and turn his life around."
            ec "And I think we both know he is not truly an evil criminal or anything of that sort. We wouldn't want that type of person in this program."
            bro "Ok, what does he have to do to finish the program successfully?"
            jump sethfour
        "Question her about what criteria was used to select your brother. [gr]\[BroEP +2\]":
            scene e2seth16 with mediumdissolve
            $ bro_e_p += 2
            bro "How was [pname] selected? What criteria or standards were used to pick him?"
            ec "Excellent question [pname4]! I can't give you the specific metrics as they are confidential, but they were quite extensive."
            scene e2seth18 with mediumdissolve
            ec "[pname] was evaluated very carefully among many candidates, and he fits the profile of one who we feel could take advantage of this program and turn his life around."
            ec "And [pname4], I think we both know your brother is not a true criminal that needs to be locked up for five years."
            bro "No, he isn't. But what does he have to do in this program to succeed?"
            jump sethfour
        "Thank her for giving your brother the opportunity to get out of prison. [red]\[BroEP -1\]":
            scene e2seth19 with mediumdissolve
            $ bro_e_p -= 1
            bro "I'm so happy to hear that [pname] is getting a chance to get out of prison early. Thank you for giving him that chance."
            ec "Of course [pname4], and I assure you we selected him very carefully based on a detailed evaluation."
            scene e2seth20 with mediumdissolve
            ec "We feel your brother fits the profile of one who could take advantage of this opportunity to turn his life around."
            ec "And I think we both know that [pname] is not a dangerous criminal that needs to be locked up for five years."
            bro "No, of course not. What does he have to do in this program?"
            jump sethfour

label sethfour:

    scene e2seth21 with mediumdissolve
    ec "[pname] simply has to finish the program, and then he is good to go with our company. That's it."
    ec "And as for [pname3], she has recently been hired by us as well. I do not know anything yet about her position or role, so I'm afraid I can't tell you much more about her specifically."
    ec "But she has been hired and is now part of the Karlsson family."
    bro "(Family is not the first word I would associate with this company...)"
    scene e2seth22 with mediumdissolve
    ec "The Karlsson Group feels this program can be even more successful for [pname] if the entire family is part of the rehabilitation so to speak. So your sister was evaluated carefully too."
    ec "And of course you as well."
    scene e2seth23 with mediumdissolve
    bro "So are you going to try and hire me for a job too? In my condition?"
    ec "No, at least not yet. To help [pname] feel more at ease, we are going to transfer you to a much better hospital with superior facilities and medicine."
    scene e2seth24 with mediumdissolve
    ec "Katherine here will be taking you to one of the best hospitals in the country, and it's run personally by Veronica Karlsson herself."
    ec "The finest medical professionals work there, with the latest in cutting edge research and medicine. We will do what we can to make you more comfortable and pain free."
    scene e2seth25 with mediumdissolve
    ec "And I do apologize, but I have to leave for another meeting. Katherine here will take care of you, and I have arranged for an escort to comfortably take you to your new home."
    bro "Ok. When can I see [pname] or [pname3]? Are they aware of all of this already?"
    scene e2seth26 with mediumdissolve
    ec "Of course [pname4]! They are being told everything so they can focus on their new duties! We wouldn't have it any other way!"
    ec "They will probably be busy for at least a few weeks settling into their roles, but they will be able to visit you in the near future."

    stop seven fadeout 3

    scene e2seth27 with mediumdissolve
    ec "Now I really must run. Katherine here has already arranged your discharge and transfer, and I wish you luck in recovering."
    kk "I'm SO happy I can help you out!"
    bro "Ok. Thank you to both of you."
    ec "Of course [pname4]. Think nothing of it. This can be a win win for everyone. Farewell."
    jump sethfive

label sethfive:

    scene e2seth28 with longfade

    play seven "<from 11 to 117>music/samhospital.mp3" fadein 3

    ec "Sam! You are late. You have a very small window of time to accomplish your one task for [pname4] so who should I blame?"
    pp2 "My plane. It was delayed a bit, sorry. I came as fast as I could. Your plane is already ready to go too, I saw it when I landed."
    ec "Very well. It's critical you tell [pname4] exactly what I have told you to say about [pname]'s time in prison."
    scene e2seth29 with mediumdissolve
    ec "I'm already a little late so tell me very briefly how the training has gone so far."
    pp2 "I tested six of the candidates. Pathetic. Five K4s and one outright failed. I think K4 is too high a servant level to start with personally."
    ec "Sam, it's no fun to demean and humiliate them if they are already at their lowest point when they start. You should understand that already. And [pname] and [pname2]?"
    scene e2seth30 with mediumdissolve
    pp2 "They are testing last so I don't know. I will head back after taking care of [pname4] as soon as I can."
    ec "That's fine, I know Patricia will do a good job. How do you think [pname] will do?"
    if sub >= 3:
        scene e2seth31 with mediumdissolve
        pp2 "With how submissive he is, I think he's going to have some trouble. But maybe he can tough it out."
        ec "Let me know how it goes. And remember to take Kitty with you when you return."
        pp2 "I understand Miss Caspari."
        jump sethsix
    else:
        scene e2seth32 with mediumdissolve
        pp2 "He's shown some flashes of strength. And he's not heavily submissive. I actually think he might do better than K4. That would be impressive, how often does it happen?"
        ec "Very rare. I think less than two percent for K5, and only a few times at K6. It would indeed be an impressive start."
        scene e2seth33 with mediumdissolve
        ec "Let me know how it goes. Remember to take Kitty with you when you return to the prison."
        pp2 "I understand Miss Caspari."
        jump sethsix

label sethsix:

    scene e2seth34 with longfade
    kk "Oh, [pname4], our ride is here! Isn't it exciting that you are going to be moving to a much better hospital?"
    bro "(Oh my God, she smells so good and her...) Err, yes, err very good."
    kk "(So easy.)"
    scene e2seth35 with longdissolve
    kk "[pname4], this is Sam, she is a police officer that is going to help us move!"
    pp2 "Sorry, I was running late, you must be [pname4]! My name is Sam! Nice to meet you! I see some resemblance to your brother!"
    scene e2seth36 with mediumdissolve
    bro "Wait, you've seen [pname]!? How is he doing?! What is happening?"
    pp2 "Haha, relax [pname4], it's a bit of a ride to your new home, we can talk on the way! We have to get going right away!"
    scene e2seth37 with mediumdissolve

    stop seven fadeout 3

    pp2 "Now we have to move you, so can you do me a favor and just lie back down, and close your eyes and relax...think of something pleasant."

    play one "<from 5 to 45>music/meeting1.mp3" fadein 1

    pp2 "We're going to call for some help to get you on a wheelchair for transport. You will feel less pain while moving if your nerves are relaxed as much as possible."
    scene e2seth38 with longdissolve
    pp2 "Just relax...yeeeessss...shhhhh, relax..."
    pp2 "There we go, good job [pname4]."
    scene e2seth39 with longdissolve
    pp2 "Don't you worry [pname4], we are going to take such good care of you..."
    kk "Yes [pname4], you are in such loving hands now..."

    stop one fadeout 2

    jump outdoorsone

label outdoorsone:

    scene e2outdoors1 with longfade

    play five "<from 242 to 340>music/futuretracks.mp3" fadein 2

    p "(What the hell is [pname2] doing in the bathroom? He's sure taking a while.)"
    scene e2outdoors2 with longdissolve
    zach "Seventy two, seventy three, seventy four, seventy five..."
    p "(What the hell is he doing?)"
    scene e2outdoors3 with mediumdissolve
    p "What are you doing there Zach?"
    zach "Please! Just leave me alone, I don't want to talk to anyone!"
    scene e2outdoors4 with mediumdissolve
    p "You just seem...a little lost there. You ready for this?"
    zach "I've always been good, always listened, what is going to happen to me? What is going to happen!?"
    menu:
        "I can't let him fall apart. I should encourage Zach about everything and calm his nerves. [GoodPath] [SlavePath]":
            $ good += 1
            $ slavepoints += 1
            scene e2outdoors5 with mediumdissolve
            p "Hey man. Nothing bad is going to happen if you can keep it together right now."
            p "Look at this as a chance to get out of prison. Whatever happens next can't be worse than being stuck in here, right?"
            scene e2outdoors6 with mediumdissolve
            zach "Yyyy...yy...yes, maybe you are right. It...it can't be as bad as staying here."
            p "Sure I'm right. You'll see. Just keep it together and let's get through this today."
            scene e2outdoors7 with mediumdissolve
            zach "Thank you...I am sorry, I forgot your name."
            p "It's [pname]. No worries, and let's just do our best."
            jump outdoorstwo
        "I shouldn't get too involved with others. I have to worry about my own problems. Best to just quickly wish him luck and leave him on his own.":
            scene e2outdoors8 with mediumdissolve
            p "I don't know what is going to happen. Good luck out there today."
            zach "Yyyeeeeah...where was I...seventy..."
            p "(Hoo boy...)"
            jump outdoorstwo
        "It's every man for himself. Maybe testing today is by curve or slotted by rank and I do better if he does worse. I should try and needle him to be more scared and unfocused. [EvilPath]":
            $ evil += 1
            $ zachweak = True
            scene e2outdoors9 with mediumdissolve
            p "Unfortunately, I think it's going to be a very tough day. It's too bad you are smaller and weaker than my friend and I."
            p "I don't think you will be able to keep up with either of us, do you?"
            scene e2outdoors10 with mediumdissolve
            zach "Oh no...you're right! I'm so weak and small! How can I keep up or even survive!?!"
            zach "I'm going to fail and I'm going to be stuck here forever, or worse! I hear they do something else if you fail, oh my God!! Please...seventy...where was I?"
            p "(Oh boy. Mission accomplished I guess.)"
            jump outdoorstwo

label outdoorstwo:

    scene e2outdoors11 with longdissolve
    pbf "Hey [pname], is it time?"
    p "What the hell were you doing in the bathroom all that time?"
    scene e2outdoors12 with longdissolve
    pbf "Oh, I was masturbating thinking about [pname3] riding me and..."
    p "What the hell [pname2]! I do NOT need that shared at all!"
    scene e2outdoors13 with mediumdissolve
    pbf "You think they would let me have a conjugal visit with her?"
    p "I give up! You're terrible."
    scene e2outdoors14 with longdissolve

    stop five fadeout 2

    pp "*over intercom* Alright! It's time! Come on outside."
    pp "Oh. One more thing. Take off your shirts. Shorts only. And don't keep me waiting!"
    scene e2outdoors15 with mediumdissolve
    pbf "No shirts? Does Pat just want to get thirsty by looking at my chest?"
    p "Well, at least the test doesn't have any coded meaning with the shirts, right?"
    pbf "Oh that's right! I'm going to kick ass now!"
    scene e2outdoors16 with mediumdissolve
    p "Uh huh. In all seriousness, I hope we both end up in a good starting point after everything."
    pbf "All joking aside [pname], I hear you. Let's get it."
    jump finaltestone

label finaltestone:

    scene e2finaltest1 with longfade
    pp "Well, here we are at last. Welcome to the last portion of your testing for The Karlsson Group's prison inmate rehabilitation program."
    pp "Now, most of you have already been tested quietly even before today to even get this far, so make the most of your chance to get out of this prison."
    pp "You just need to do a few simple physical tasks right now to wrap everything up!"
    scene e2finaltest2 with longdissolve

    play five "<from 1 to 135>music/futuretracks.mp3" fadein 2

    pp "And at least none of you are worthless fatties because I would have surely taken it out on you! Men like that don't get to work for The Karlsson Group!"
    pp "You will only have a few simple physical tasks to perform to complete your testing. The first one is the simplest one of all -- just running!"
    scene e2finaltest3 with mediumdissolve
    pp "The others will be tougher as they will test...pain tolerance. You will need that skill in this program to do well."
    pbf "Why do we need pain tolerance for this program? What the hell?"
    pp "Did I say you could speak [pname2]? If you speak again without permission, you will be punished accordingly. Or would you just rather rot in this jail!?"
    scene e2finaltest4 with mediumdissolve
    pp "Now, every task you perform here will be combined with your computer test for a final rating. They are FAIL, Low, Pass, and High."
    pp "A Low rating means you will begin your employment as a K4 employee, a Pass means K5, and a High means K6."
    scene e2finaltest5 with mediumdissolve
    pp "And if you fail...well...let's hope you don't find out."
    scene e2finaltest5b with mediumdissolve
    pp "Now, I'm going to give each of you one by one a chance to ask questions before we start, but you better end everything you say with the word Mistress!"
    pp "And no, I'm not going to tell you the other tests ahead of time, so don't bother!"
    scene e2finaltest6 with mediumdissolve
    pp "Ah, Zach. You're not fat, but you look so weak and scrawny! I bet even I am stronger than you! Any last words?"
    zach "Err, please, what is going to happen? I don't know what to ask..."
    p "(Oh man...)"
    scene e2finaltest7 with mediumdissolve
    pp "Wrong! I'm docking extra points at the end because you apparently can't remember what I just said seconds ago!"
    scene e2finaltest8 with mediumdissolve
    pp "Ah, [pname]. I hope you are not as stupid as Zach here. Any last words or questions?"
    menu:
        "I have no questions. [SlavePath]":
            scene e2finaltest9 with mediumdissolve
            $ slavepoints += 1
            p "I have no questions."
            if patdealyes:
                pp "Oh [pname], you really must be an idiot to forget our time in your cell! Tsk tsk..."
                $ patdealyes = False
                pp "I guess you are more on your own than I thought."
                $ patdealno = True
                jump finaltesttwo
            else:
                $ slavepoints += 1
                pp "Oh [pname], you really must be an idiot. Did you not just hear what I said? Docking points for you too!"
                jump finaltesttwo
        "I have no questions, Mistress Patricia. [Recommend]":
            scene e2finaltest10 with mediumdissolve
            p "I have no questions, Mistress Patricia."
            if patdealyes:
                $ slavepoints -= 1
                pp "I am glad you understand your situation entirely. And I will...remember...our earlier conversation in your cell. Good."
                pbf "(What was that about?)"
                menu:
                    "Try to signal somehow to Patricia that Zach might be close to breaking. [EvilPath]":
                        scene e2finaltest10b with longdissolve
                        $ evil += 1
                        p "Thank you, Mistress Patricia."
                        pp "Oh, you are VERY welcome [pname]. I do see everything too."
                        jump finaltesttwo
                    "Don't take the risk of upsetting her by doing too much in front of the others.":
                        p "(Better not do anything rash...)"
                        jump finaltesttwo
            else:
                pp "Very well [pname], I guess you have all the answers don't you? We shall see."
                jump finaltesttwo
        "Say absolutely nothing. [SubPath]":
            $ slavepoints += 1
            $ sub += 1
            scene e2finaltest11 with mediumdissolve
            p "(........)"
            pp "Ah, nothing to say, eh? That's fine [pname], I guess you have all the answers already! Let's see it out there!"
            jump finaltesttwo

label finaltesttwo:

    scene e2finaltest12 with mediumdissolve
    pp "Ah, and last and maybe least? [pname2], always so talkative. Now's your chance! Anything you want to say?"
    pbf "No, Mistress Patricia."
    p "(Nice [pname2], all business...)"
    scene e2finaltest13 with mediumdissolve
    pp "All of the guards here think you are so stupid, but maybe you have more in your little head than they give you credit for...we shall see."
    scene e2finaltest14 with quickdissolve
    pp "But can you blame them? You were found with stolen tech in your car with an actual homing beacon turned on to find you!"
    pp "You were too stupid to bother to turn off the tracking device and it just required pushing a giant red glowing button to the off setting! Haha!"
    p "(Oh damn, he didn't mention that to me, they really did screw him over.)"
    scene e2finaltest15 with longdissolve
    pp "But let's start now! Your first task as I said is very simple. Just run! You have 45 minutes to do as many laps as you can around this yard."
    p "(Jeez, more barefoot bullshit, just have to hope the ground is smooth enough.)"
    pp "You will be judged on how many laps you can finish in that time. Run, walk, jog, I don't care but it's for 45 minutes. The more laps the better obviously!"

    stop five fadeout 2

    if selfisheater:
        scene e2finaltest16 with mediumdissolve
        $ strongjog = True
        p "(I feel really up for running. I think getting to eat that fruit instead of that energy draining slop really helped me! I should be able to do a strong jog the whole time.)"
        p "(Surely that will be good enough to do well. No way anyone here can run fast that long.)"
        jump finaltestthree
    else:
        scene e2finaltest16 with mediumdissolve
        menu:
            "I don't think I can jog for 45 straight minutes. I should run fast until I tire, then walk, then run fast, then walk in cycles for 45 minutes.":
                $ sprintwalk = True
                p "(I'll run fast then walk, then run fast, and keep doing this as best as I can for 45 minutes. Hopefully, that's enough.)"
                jump finaltestthree
            "I don't think I can jog for 45 straight minutes. I should jog until I tire, then walk, then jog, then walk in cycles for 45 minutes. [SlavePath]":
                $ jogwalk = True
                p "(I'll jog then walk, then jog, and keep doing this as best as I can for 45 minutes. Hope that's enough.)"
                jump finaltestthree

label finaltestthree:

    scene e2finaltest17 with longdissolve
    pp "Ok! You will be tracked by camera, and I will be back out for your additional tests in 45 minutes!"
    pp "Go ahead and get started, and run well you little worms!"
    scene e2finaltest18 with longfade
    p "(Here we go...I should still try and conserve some energy for after the run too...)"
    jump domqone

label domqone:

    scene e2domq1 with longfade

    play four "<from 598 to 780>music/futuretracks.mp3" fadein 2

    d "I did so much for you. The first local ever given a real management position at the mines. Against the wishes of the rest of the Board. A free and real education for your family."
    d "And think of the reforms I was able to make. Cutting the hours from twelve to ten hours a day. Better food. Providing actual shelter for the workers."
    d "I stuck my neck out to give you this chance. And this is how you repay me. Helping to incite a revolt."
    scene e2domq2 with longdissolve
    d "And look at you now. I don't know why you thought you could get anything past my sister. She's too smart about watching everyone."
    kw "All of us are caged slaves anyway. You only made the chains slightly looser, but they are still there."
    kw "And yes, we now have the luxury to dine on slightly better scraps and live in shitty tents while you and your corrupt family and company reap all the luxury and rewards on our backs."
    scene e2domq3 with mediumdissolve
    kw "You profit off our misery. I could not in good conscience just stand by and do nothing."
    d "I know the world isn't fair. And I know how hard it still is for everyone. But think of who you just hurt with your stunt. Did you really think you could change everything just like that?"
    scene e2domq4 with longdissolve
    d "What do you think the Board will do to the workers now? They will be able to easily argue that giving a little slack only caused more trouble, and that it's time to get harsher again."
    d "I'm only one vote out of seven. Any real chance for significant and permanent reform for the mines probably died with your stunt."
    d "Even if I end up winning control of the The Karlsson Group someday, I would still have a hard time with reform as it's such a radical change. But I was your only chance."
    scene e2domq5 with mediumdissolve
    d "Now the whispers that I am too soft hearted to run The Karlsson Group only grow louder again. You hurt your only possible ally and probably the only Karlsson with a moral compass."
    d "And imagine if someone like Juliette ends up in complete charge of the mines. You have no idea...she is literally a broken human being."
    d "I'm not going to lie and say I could have improved your own life so quickly. But your children's generation? Even after 5 years? 10? I bet you I could have made a huge difference."
    scene e2domq6 with mediumdissolve
    d "But that's probably over now. I have to show strength now to silence the whispers. It's for the greatest good long-term."
    d "And unfortunately, I have to make an example out of you."
    kw "What are you going to do?!!"
    scene e2domq7 with longdissolve
    d "I will have the decency to tell you face to face what is going to happen. The Board initially wanted to use our militia to publicly execute you and your entire family for your crime."
    d "It took every ounce of my power to convince Elena, Alessandra, and Juliette to vote with me on an alternative plan."
    kw "So what is going to happen to them? Dominique, they have done nothing! You can't take it out on them, please! Please Dominique..."
    scene e2domq8 with mediumdissolve
    d "Kwame, I'm going to get straight to the point. You are going to be transferred to a special inmate rehabilitation program for your crimes."
    d "The program will run for six months. If you successfully complete it, your family will be spared. If not, well..."
    scene e2domq9 with mediumdissolve
    kw "What? But what will I have to do, what is this program!!? You can't do this Dominique, they are innocent and pure and..."
    d "...I know what they are Kwame! You think I had a better choice? That I could convince three others on this Board to show actual compassion? Even you know that's impossible!"
    d "The only way I could get even get those three to vote with me was the idea of how entertained they would be watching you endure any suffering and humiliation for their lives!"
    scene e2domq10 with longdissolve
    d "You are lucky to even get this chance from me. You have hurt me quite badly, more than you know. I vouched for you. No one has ever doubted my talent and charisma to be the equal of my father."
    d "But this incident only amplifies their doubts about what I do lack. They say if I had Juliette's ruthlessness, there wouldn't even be a Gamb...never mind."
    scene e2domq11 with longfade
    d "Now, I suggest you get very calm and focused on what awaits you. You have a chance to save them. So do it. Wasting energy on anything else now is futile."

    stop four fadeout 2

    kw "I...Dominique, for what it's worth, I know you are not like the rest of your family. I really do believe that."
    scene e2domq12 with mediumdissolve
    d "Kwame, if you grew up with my father...almost...almost no one could survive that with a relatively clean soul."
    d "Even Juliette...I can't fully blame her being what she is today. She's not the sister that actually scares me anyway..."
    scene e2domq13 with mediumdissolve
    d "Kwame, I do wish you luck, but I can't help you. In fact, I will have to be cruel at times to ease doubts from the others."
    kw "I understand. I will do what I must."
    jump e2maidone

label e2maidone:

    scene e2maid1 with longfade
    jk "My Lady, I have completed everything you requested for today. How else can I serve you today?"
    d "That's all Junko. Take a break for the rest of the day."
    scene e2maid2 with mediumdissolve
    jk "My Lady? It's so early for you to relieve me. Is everything all right?"
    d "Yes. Just some tough decisions. But, now that you are here...Junko, I actually may have a new assignment for you soon. A much harder one."
    scene e2maid3 with mediumdissolve
    jk "What is it My Lady? I am here to serve you in any way I can but why it is much harder?"
    scene e2maid4 with mediumdissolve
    d "Don't worry so much Junko. You might actually enjoy it. But it would involve a specific man...I need to know if I am truly alone in this stupid Gambit..."
    jk "What do you mean and what man My Lady?"
    jump finaltestfour

label finaltestfour:

    scene e2finaltestfour1 with longfade
    p "(Well, that wasn't very fun...)"
    scene e2finaltestfour1b with mediumdissolve
    pp "Just one minute to rest and then we will start the last few little tests!"
    pp "The run was designed to wear you all out for the fun part so we can't let you get too much rest!"
    scene e2finaltestfour2 with longdissolve
    pbf "Damn [pname], prison got us a little more out of shape I think."
    p "Yeah..."
    if strongjog:
        scene e2finaltestfour3 with mediumdissolve
        p "(I definitely more than outpaced [pname2] and Zach. I've done well...on this part at least.)"
        jump finaltestfive
    elif sprintwalk:
        $ slavepoints += 2
        scene e2finaltestfour4 with mediumdissolve
        p "(I did okay and outran Zach, but [pname2] definitely outpaced me overall.)"
        jump finaltestfive
    elif jogwalk:
        $ slavepoints += 3
        scene e2finaltestfour5 with mediumdissolve
        p "(Damn. I did really shitty on this test. Both Zach and [pname2] outpaced me for sure.)"
        jump finaltestfive
    else:
        $ slavepoints += 2
        scene e2finaltestfour4 with mediumdissolve
        p "(I did okay and outran Zach, but [pname2] definitely outpaced me overall.)"
        jump finaltestfive

label finaltestfive:

    scene e2finaltestfour6 with longfade

    play music "<from 3180 to 3345>music/futuretracks.mp3" fadein 2

    pp "Time's up! We only have two little games to play and then you are all done! They will be so easy."
    p "(Yeah, sure.)"
    pp "I have to be honest and say you all have been tested 99 percent of the way already. This last little part is mostly just a job perk for us as guards!"
    pp "I want to call these games instead of tests because they are so fun to play! Oops, I guess it's just fun for me, sorry, haha!"
    scene e2finaltestfour7 with mediumdissolve
    pp "For this first game, I need all three of you to just stand straight up with your legs spread out a bit like an upside down V."
    pp "Make a three way square so I can reach all of you more easily. Hurry up you little worms!"
    scene e2finaltestfour8 with longfade
    pp "Very good. Now this game is very simple. You all need to just stay still and close your eyes with your arms spread out slightly with your hands facing down."
    pp "I'm then going to randomly select someone and deliver a wonderful and swift kick to your pathetic manhood."
    p "(What the...)"
    scene e2finaltestfour9 with mediumdissolve
    pp "To pass the test, you can't fall down. You can scream verbally all you want, but you need to stay standing up."
    pp "You can bend down a little for a few seconds to recover, but no touching anything with your hands! If I catch your eyes being open, you automatically fail everything, not just this test!"
    scene e2finaltestfour10 with mediumdissolve
    pp "I'm going to keep randomly kicking one of you until at least two of you fail by falling down."
    pp "The last one standing is the winner!"
    scene e2finaltestfour11 with longdissolve
    pp "This is your chance to escape jail, so bear the pain well!"
    pp "I'm going to start now. If you look sad and pathetic enough, maybe I will take it easy on you!"
    jump finaltestsix

label finaltestsix:

    if patdealyes:
        jump ballkickfake
    else:
        jump ballkickreal

label ballkickfake:

    scene e2finaltestfour12 with longdissolve
    pp "Ahh, who should I kick first? You all look so tempting, this is one of my favorite parts of my job!"
    pp "I'm just going to make you all wait in scared silence while I decide...I wouldn't make a sound if I were you."
    scene e2finaltestfour13 with longdissolve
    pp "*whispering* Feeling a little nervous [pname]? Thinking maybe I'll go back on my word? Or that I forgot?"
    pp "I haven't forgotten. But we have to keep up appearances don't we? If not, I'd have to abuse you for real."
    scene e2finaltestfour14 with mediumdissolve
    pp "So I'm going give you a nice slap on your dick with just my hand. It might hurt a tiny bit, but I don't think it will at all."
    pp "But I need the other two worms to stay nervous. So you have to do your part to sell them on your pain, or else it would look suspicious, wouldn't it?"
    scene e2finaltestfour15 with longdissolve
    pp "I haven't seen your computer test yet..."
    if strongjog:
        "...but you did really well on the run so I think you are in good shape to avoid a K4 employee level."
        jump ballkickfaketwo
    elif sprintwalk:
        "...but you did decent but not great on the run so you need all the help you can from me right now."
        jump ballkickfaketwo
    elif jogwalk:
        "...but you didn't do well on the run so you need all the help you can get right now. I thought you would do a little better on your own...tsk tsk [pname]."
        jump ballkickfaketwo
    else:
        "...but you did decent but not great on the run so you need all the help you can from me right now."
        jump ballkickfaketwo

label ballkickfaketwo:

    scene e2finaltestfour16 with longdissolve
    pp "It's showtime [pname]."
    scene e2finaltestfour17 with longdissolve
    pp "And my first victim today is going to be..."
    scene e2finaltestfour18 with quickdissolve
    pp "[pname]!"
    menu:
        "Show your acting chops and sell the pain with sounds and choice words. [_SlavePath]":
            scene e2finaltestfour19 with mediumdissolve
            p "Argh! Jeez, what the...fuckin...shit...!"
            pp "Oooh, looks like that hurt [pname], but you managed to stay standing! How wonderful for you!"
            jump ballkickrealtwo
        "Act out grunting in pain but don't verbalize any words.":
            scene e2finaltestfour20 with mediumdissolve
            $ slavepoints += 1
            p "Unghhhh!"
            pp "Oh, [pname] really toughed it out with that kick, guess I need to kick much harder to get more of a reaction, don't I?"
            jump ballkickrealtwo
        "Don't sell the pain at all. [SlavePath]":
            scene e2finaltestfour21 with mediumdissolve
            $ slavepoints += 5
            p "....."
            pp "Oh, [pname] is deciding to play the tough guy all of a sudden. Very well, but you made a very poor decision [pname]."
            jump ballkickrealtwo

label ballkickreal:

    scene e2finaltestfour22 with longfade
    pp "Ahh, who to kick first? You all look so tempting to me! The two that don't get kicked next better keep their eyes closed and body still no matter what!"
    pp "But right now you are all doing so well standing in silence. Maybe I'll go easy on you all for being such good little worms!"
    scene e2finaltestfour23 with mediumdissolve
    pp "But what fun would that be? We need to see who is tough here! You need it for this program."
    pp "So I think my first victim today is going to be..."
    scene e2finaltestfour24 with quickdissolve
    pp "[pname]!"
    scene e2finaltestfour25 with mediumdissolve
    p "(Holy shit...ouch!)"
    menu:
        "Just get things over with for this test and let yourself fall down.":
            $ kanefallone = True
            $ slavepoints += 2
            $ sub += 1
            scene e2finaltestfour26 with mediumdissolve
            p "Oh my...jeez! (Better to just get it over with...ugh)"
            pp "Down with one kick [pname]? I thought you were made of stronger stuff. Guess not."
            scene e2finaltestfour27 with mediumdissolve
            pp "I'm not letting you get by with just one kick, so a little stomp should satisfy me!"
            p "Urgh!"
            pp "Now you've lost, but you need to stand back up. I'm not letting you sit and rest for that pathetic display of toughness."
            jump ballkickrealtwo
        "Tough it out and try your hardest to keep standing.":
            scene e2finaltestfour28 with mediumdissolve
            p "Oh my God, ugh..."
            pp "Well [pname], you're still standing! And I gave you a little extra special love with my kick since I am so fond of you, haha!"
            scene e2finaltestfour29 with mediumdissolve
            pp "Good job, but it's only one kick!"
            pp "Maybe I am going to pick you again immediately. Or maybe one of these two other worms instead...yes, I think at least one kick for another worm first."
            jump ballkickrealtwo

label ballkickrealtwo:

    scene e2finaltestfour30 with longfade
    pp "Ah, stupid [pname2] next or little itty bitty Zachie poo...oh what to do."
    pp "And it's..."
    scene e2finaltestfour31 with longdissolve
    pp "...Zach!"
    if zachweak:
        scene e2finaltestfour32 with mediumdissolve
        zach "Nooooooo!"
        pp "Boo hoo Zach!"
        scene e2finaltestfour33 with longdissolve
        pp "I think we both knew you wouldn't last even one kick! How did you even get picked for this program?"
        pp "One of the Karlsson sisters must have a real fetish for someone with your weak body. Get back up worm."
        jump ballkickrealthree
    else:
        scene e2finaltestfour32b with mediumdissolve
        zach "Noooooo!"
        pp "Oh, you actually stayed up Zach! But I can't have a little guy like you actually win! Sam might tease me. So let's do a real kick now!"
        scene e2finaltestfour33b with mediumdissolve
        pp "Enjoy six years of hard training on how to kick worthless worms!"
        zach "Arrgh!"
        scene e2finaltestfour34 with mediumfade
        pp "Now lick my boot you worthless worm for daring to stay up even one time! And beg for me not to fail you!"
        zach "Please! Please..."
        pp "Pathetic...get back up worm."
        jump ballkickrealthree

label ballkickrealthree:

    scene e2finaltestfour35 with longfade
    if kanefallone:
        pp "Well, both [pname] and Zach have already fallen! But [pname2], you still have to survive my kicks too!"
        pp "But for you, let's try something different."
        jump ballkickrealthreeb
    else:
        pp "Well, let's see who is next...ah, I'm just going to tell you [pname2] that it's you."
        pp "That's because for you, I want to try something different."
        jump ballkickrealthreeb

label ballkickrealthreeb:

    stop music fadeout 3

    scene e2finaltestfour36 with mediumdissolve
    pp "Now [pname] is such a good friend to you, isn't he? So let's test your friendship."
    pp "If you get down right now and lick my boot, you will fail without suffering a kick. But, I'll guarantee that [pname] won't fail the overall testing."
    scene e2finaltestfour37 with mediumdissolve

    play seven "<from 3882 to 3934>music/futuretracks.mp3" fadein 2

    pp "So he is guaranteed to avoid staying in jail, but you will take on more risk for yourself."
    pp "Are you willing to do that for your friend? I am so interested in what you do."
    pbf "(Shit...)"
    if friend >= 2:
        scene e2finaltestfour38 with longdissolve
        pbf "Fine."
        pp "Wow, such a good friend! I wonder if [pname] would have done the same for you. But yes, now [pname] won't fail the overall testing."
        pp "But of course, that's just from me. Maybe a higher ranked employee could still overrule me, haha!"
        pbf "(Bitch...)"
        jump ballkickrealfour
    else:
        scene e2finaltestfour39 with longdissolve
        $ friend -= 1
        pbf "No, I won't get down."
        p "(Oh...)"
        pp "Oh wow [pname], I guess it's good you found out right before this program what kind of friend you have, haha!"
        scene e2finaltestfour40 with mediumdissolve
        pp "But you forgot to say Mistress at the end of your sentence! So down you go!"
        pp "Too bad for you, automatic fail from me!"
        pbf "Ugh!"
        scene e2finaltestfour41 with longdissolve
        pp "Either way you chose, you were going to be under my boot and failing. But maybe you should have tried harder for your friend, you might need him in this program."
        jump ballkickrealfour

label ballkickrealfour:

    stop seven fadeout 1

    scene e2finaltestfour42 with longfade
    pp "You can all relax and open your eyes now! This part is over!"
    if kanefallone:
        pp "Well, you all failed this one. Too bad. Hope you were all genius test takers on the computer!"
        jump secondtest
    else:
        pp "Well, I guess you survived this test [pname]. I could keep kicking your poor balls to make sure you all three of you fail..."
        pp "...but I do think that [pname2] and Zach are so much more pathetic so let's actually pass you for this test!"
        jump secondtest

label secondtest:

    scene e2secondtest1 with longfade

    play music "<from 3180 to 3345>music/futuretracks.mp3" fadein 3

    pp "One last thing for you worms. As part of your new initiation into this program, you no longer have need for shock collars like you did here."
    pp "As you all know now from your recent physicals, each of you have been injected with special chips that can administer pain in many different ways."
    scene e2secondtest2 with mediumdissolve
    pp "This is to ensure that you don't get any funny ideas about your lowly status in the grand scheme of The Karlsson Group."
    pp "Any disobedience or poor performance in the program could lead to severe...pain, so I would suggest being good little worms."
    scene e2secondtest3 with mediumdissolve
    pp "I don't know a lot about the ranks, but I do know you never, ever want to be at K1. Some end up back here with Sam. Wouldn't wish that on anyone and I'm a mean bitch saying that. Just trust me."
    pp "I can also tell you that K10s actually have their chips deactiviated, so there is always that possibility someday. I even know that one person went way beyond K10."
    scene e2secondtest4 with mediumdissolve
    pp "Anyway, these chips can be activated to inflict pain by specific superiors that are authorized by voice to do so. The overall manager of your training program will determine all of these details."
    pp "A lot of the work involved will be menial, but certainly not everything as it will greatly depend on your superior. Many of them will have different...err...needs."
    scene e2secondtest5 with mediumdissolve
    pp "You will have six months to prove yourself and finish the program. If you can tough it out, you can be a free man with a real job at one of the biggest and most powerful companies on the planet!"
    pp "And I can say personally that if you are loyal and trustworthy, The Karlsson Group does reward their best. So keep that in mind."
    scene e2secondtest6 with mediumdissolve
    pp "There is one final little bit of fun but before that, I will give each of you one question to ask about the program. You can relax and ask anything you want."
    pp "Believe it or not, I can understand being in your position right now. But try to remember I can't answer everything, so you might not be satisfied with my answer."
    pp "Zach?"
    scene e2secondtest7 with mediumdissolve
    zach "No questions, Mistress."
    pp "Ah, at least you learn quickly how to address your superior Zachie. Maybe you can last a little while."
    scene e2secondtest8 with longdissolve
    pp "[pname2]? Anything?"
    pbf "Mistress, will we be staying together as a group during this program, or will we be separated?"
    scene e2secondtest9 with mediumdissolve
    pp "That's actually a pretty decent question [pname2]."
    pp "I believe you generally will all be together as it's one program but at times you will working alone as well. Obviously, the experience won't be the exact same for each person."
    pp "A lot can depend on your own performance and rank, your assigned superiors, and I would guess many other variables."

    stop music fadeout 3

    scene e2secondtest10 with mediumdissolve
    pp "[pname]?"
    menu:
        "Don't ask any questions at all. [SubPath]":
            $ sub += 1
            scene e2secondtest11 with mediumdissolve
            p "No questions, Mistress."
            pp "Very well [pname], let's move on then."
            jump secondtestfork
        "Ask Patricia how often someone gets demoted to lower ranks during the program. [SubPath]":
            $ sub += 1
            scene e2secondtest12 with mediumdissolve
            p "Mistress Patricia, how often do people get demoted during this program? How does that usually happen?"
            pp "I don't know how it actually happens, but I think you can figure out that it's for poor performance."
            pp "But I do know no one in past programs started at K1, but I did see some end up back here as K1s at this jail. That should tell you something right there...but let's move on now."
            jump secondtestfork
        "Ask Patricia how often someone gets promoted to higher ranks during the program. [DomPath]":
            $ dom += 1
            scene e2secondtest13 with mediumdissolve
            p "Mistress Patricia, how often do people get promoted ranks during this program? How does that usually happen?"
            pp "I don't know this for sure [pname], but given the people involved that run this program, I'd guess it's probably rare to move up easily. But I know it does happen sometimes."
            pp "There is one man who did so well in this program many years ago that ultimately he even became a member of The Karlsson Group Board."
            scene e2secondtest14 with quickdissolve
            p "(Woah, someone rose that high? So maybe I can strive for more than survival...)"
            pp "But let's move on now."
            jump secondtestfork
        "Ask Patricia what percentage of people entering the program have actually successfully completed it after six months. [GambitPath]":
            $ gambitpoints += 1
            scene e2secondtest13 with mediumdissolve
            p "Mistress Patricia, over the years, what percentage of people entering the program have actually finished it?"
            pbf "(Damn, fucking good question dude...)"
            pp "That is a surprising question [pname]."
            scene e2secondtest15 with mediumdissolve
            pp "Unfortunately, I am not allowed to tell you that answer. But I can say that I was given that information by Elena before."
            p "(It's probably not a high percentage...)"
            scene e2secondtest16 with mediumdissolve
            pp "I do feel bad giving you nothing from such a smart question. So I will say that in this program, some do get demoted all the way to K1 and end up wishing they were dead."
            pp "But others do pass and do well with great jobs later. One did so well in the program many years ago that ultimately he even became a member of The Karlsson Group Board."
            scene e2secondtest14 with quickdissolve
            p "(Hmm, someone actually rose that high from this situation? Maybe I can strive for more than survival...)"
            pp "But let's move on now."
            jump secondtestfork


label secondtestfork:

if patdealyes:
    jump patsex
else:
    jump secondtestpain

label secondtestpain:

    scene e2secondtestpain1 with longfade
    pp "Unfortunately for you three, the last part of this test isn't really a test at all. It's just a reminder to make sure you know your place."
    pp "You're also being filmed from numerous angles so that your future superiors can enjoy seeing their new workers, servants, whatever."
    p "(Now no shirts make more sense to me...)"
    scene e2secondtestpain2 with mediumdissolve

    play five "music/death1.mp3" fadein 2

    pp "So you are just going to experience a few minutes of pain."
    pp "Sheep, Body Pain Level 5!"
    scene e2secondtestpain3 with mediumdissolve
    p "Arghggh! (oh my...)"
    zach "Nooo, aaaaagggggh!"
    pbf "Damn....uuggggh!"
    scene e2secondtestpain4 with mediumdissolve
    pp "(So glad it's not me.)"
    pp "Take in this pain and never forget the penalty for doing poorly. Hopefully this will motivate you to be obedient and serve your superiors well."
    scene e2secondtestpain5 with mediumdissolve
    pp "If any of you can manage to crawl to me, I'll turn off your pain early!"
    p "(Doesn't look like anyone else is moving...can I even?)"
    menu:
        "Attempt to crawl over to Patricia. [JuliettePath]":
            $ juliette_p += 1
            scene e2secondtestpain6 with mediumdissolve
            p "(Fuck it, let's give it a shot...arrgh...!)"
            pp "Oh, impressive [pname], but I'm afraid I was just joking and I actually can't end the pain early by order so [pname], Leg Pain Level 2!"
            scene e2secondtestpain6b with quickdissolve
            p "Ugh, alright turn that part off, I won't move anymore!"
            pp "Very good to understand right away. [pname], Leg Pain Off!"
            jump secondtestpaintwo
        "Don't do it.":
            $ juliette_p -= 1
            scene e2secondtestpain7 with mediumdissolve
            p "(I can barely move with this much pain as it is. Maybe don't make things worse.)"
            jump secondtestpaintwo

label secondtestpaintwo:

    scene e2secondtestpain8 with longfade
    pp "Awwww, poor poor little worms..."
    pp "But it's now been a few minutes, you're almost done. You are putting on a nice little show for your future bosses!"
    scene e2secondtestpain9 with mediumdissolve
    pp "Ok, I think that's enough! Sheep Body Pain Off!"
    scene e2secondtestpain10 with longdissolve

    stop five fadeout 3

    p "(Ugh, my damn life...)"
    pp "Good news worms! You are all done with your training for the inmate rehabilitation program!"
    scene e2secondtestpain11 with mediumdissolve
    pp "You can relax now and head back inside. You'll speak with Sam later about your final results."
    pp "That probably won't be until this evening, so rest up in the meantime. You are being given a break from any prisoner work, so relax while you can!"
    scene e2secondtestpain12 with mediumdissolve
    pbf "*whispering* Well, we survived. Wonder how it will go for us."
    p "*whispering back* Yeah..."
    jump sisnewhire

label patsex:

    scene e2patsex2 with longfade

    play five "music/death1.mp3" fadein 2

    pp "Now, unfortunately for two of you, there is one more pain test. It's quite simple. You will be shocked for a little bit of time to teach you early the price of disobedience in the program."
    pp "[pname] actually managed to do enough on his testing to avoid this punishment, so he will instead clean my boots during this time."
    p "(I did? How? Better to clean boots than get a lot of pain...)"
    scene e2patsex3 with mediumdissolve
    pp "You will both have to kneel towards the window there and stay still as you are shocked. You are also being filmed so that your new superiors can see you up close."
    pp "Now get over there and kneel."
    scene e2patsex4 with longfade
    pp "Very good! Maybe I will lower the pain a bit for being so obedient!"
    pp "I hope you two enjoy yourselves! [pname2], Zach, Body Pain Level 3!"
    scene e2patsex4b with mediumdissolve
    zach "Arrggh, oh!"
    pbf "Errgghghghghg!"
    scene e2patsex4c with mediumdissolve
    p "(Wow, lucked out I guess on this one.)"
    pp "Don't forget to stay still or I'm going to extend the time! Oh, your short little bit of time is five minutes! Have fun!"

    stop five fadeout 2

    jump patsextwo

label patsextwo:

    scene e2patsex5 with longfade
    pp "Follow me [pname]. I think you will enjoy my boot cleaning. A perk of your deal with me."
    p "(Why would I enjoy that?)"
    scene e2patsex6 with longfade

    play seven "<from 120 to 270>music/patbalcony.mp3" fadein 2

    pp "Ah, wonderful view from here isn't it?"
    if elena_mentor:
        pp "The last time you were on this stairwell, it led to an interesting experience in the limo didn't it?"
        p "Err, yes, definitely."
        pp "So I hear. Kitty was very excited to meet you again while I was driving her and Elena to the airport."
        jump patsexthree
    else:
        pp "Ah, wonderful view from here isn't it?"
        p "Yes it is."
        jump patsexthree

label patsexthree:

    scene e2patsex7 with longdissolve
    pp "So [pname], when Elena first hired me, she stood me right here on this exact spot and had me look down at all of the prisoners on their knees cleaning the entire yard."
    pp "And she asked me a very simple question..."
    scene e2patsex8 with mediumdissolve
    pp "...She pointed down at all of them and asked me whether I wanted to be on top looking down on the little people, or down on the ground as a little worthless nothing."
    pp "She taught me I had to do whatever it takes to stay on top, or else I deserved to stay on the ground. And I have learned that lesson well."
    scene e2patsex9 with mediumdissolve
    pp "So I stuck my neck out a little to help you. But I want to know if it will play out well for me."
    pp "Elena clearly gave you special attention for some reason. She met no other prisoner. To me, that alone means you might have chances to gain power the others will not."
    scene e2patsex10 with mediumdissolve
    pp "Now, look at those two down there. On their knees. Suffering. Pathetic. No power. I know [pname2] is your friend, but right now he's little people. A pitiful bug."
    pp "Are you going to end up that way too? A pathetic worm crawling in the dirt to survive?"
    scene e2patsex11 with longdissolve
    pp "Or do you have the balls to take what you want?"
    pp "Hmm, I'd like to do one small test just for you. Can you massage my shoulders while I enjoy the view below?"
    scene e2patsex12 with longfade
    pp "Thank you [pname]. Think about my question I just asked again...do you have the balls to take what you want?"
    menu:
        "Move your hands from her shoulders and down towards her breasts.":
            $ dom += 1
            $ pat_p += 1
            scene e2patsex13 with mediumdissolve
            p "Don't worry about my balls Patricia...they are more than willing to...take."
            pp "Mmmmm, very good. I'm becoming convinced. But I need a little more evidence."
            pp "Take your pants off. I'll put them inside real quick. Let's have some fun..."
            jump patsexfour
        "Tell her your balls are big enough to fuck her right now even with your friend suffering below. [DomPath] [EvilPath] [PatriciaPath]":
            $ evil += 1
            $ dom += 1
            $ pat_p += 3
            scene e2patsex14 with mediumdissolve
            p "I have enough balls to fuck you right now even with [pname2] suffering below us."
            pp "Oh [pname], that is very mean and cruel. Getting off while your good friend cries in pain."
            scene e2patsex15 with mediumdissolve
            pp "Good. You may have to discard all the little people in your life if you want to get big yourself."
            pp "But now you've turned me on...so I want to see your balls firsthand. Take your pants off. I'll put them inside real quick. Let's play."
            jump patsexfour
        "Just keep massaging her shoulders and say nothing. [SubPath]":
            $ sub += 1
            $ pat_p -= 2
            scene e2patsex16 with mediumdissolve
            p "....."
            pp "Hmm. I guess you aren't quite ready but I hope you can learn as you go. Don't let me down [pname]."
            jump patsexfive

label patsexfour:

    stop seven fadeout 2

    scene e2patsex17 with longfade

    play seven "<from 59 to 277>music/patsexfive1.mp3" fadein 2

    pp "You've only got less than five minutes. Those two could have permanent damage if they suffer too long that way."
    pp "So we need to get each other warmed up very quickly. No time for tons of foreplay, although maybe that works better for you?"
    scene e2patsex18 with longfade
    pp "There are very few powerful men around The Karlsson Group so it would be nice to have a strong and vibrant executive available someday for...career advice."
    scene e2patsex19 with mediumdissolve
    pp "Let's see what we have down here."
    pp "I saw this the first day you checked in. Even though Elena has been so good to me, one sad thing is that she hasn't let me play with you all this time."
    scene e2patsex20 with mediumdissolve
    pp "Mmmm, tasty. You would laugh at the pathetic dicks I have seen in this prison."
    scene e2patsex21 with longdissolve
    p "Just keep going!"
    pp "Oh, so loud now. Maybe [pname2] could even hear you."
    scene e2patsex22 with mediumdissolve
    pp "Mmmm, I think you are ready for me now and we don't have much time. How much pent up sexual energy do you have bottled up from being stuck here in jail?"
    scene e2patsex23 with longfade
    pp "Use it all right now...get behind me and don't be afraid to be rough, I'm not some weak little girl."
    scene e2patsex24 with mediumdissolve
    pp "Oh yeah...don't forget this feeling [pname] when you are out there. Take what you want but be smart."
    scene e2patsex25 with mediumdissolve
    pp "If you are strong enough, you can have so much for yourself. You could do almost anything you want...fuck almost anyone you want."
    scene e2patsex25b with mediumdissolve
    pp "Oh fuck! But I want you to give me a little taste too. I can help you a lot, trust me. You have no idea, oh yeah...right there!"
    scene e2patsex26 with mediumdissolve
    pp "Now look at those two bugs while you get off. Do you want to be down there suffering, or on top fucking who you like..."
    pp "You have no idea...oh fuck...harder...the Karlssons are all about having pleasure while others suffer around them."
    scene e2patsex27 with longfade
    pp "I want to look into your...oh my!"
    p "You talk too much. I'm almost..."
    scene e2patsex28 with mediumdissolve
    pp "Oh fuck yeah! That's how you shut me up...grab my fucking hair and just ravage my pussy! I said you could be a little rough with me..."
    scene e2patsex29 with mediumdissolve
    pp "Oh yes!"
    scene e2patsex30 with mediumflash
    p "I'm going to..."
    pp "Let all of it out [pname]!"
    scene e2patsex31 with mediumflash
    p "Fuck!"
    pp "Oh! You had a LOT of pent up frustration and tension didn't you, wow..."
    scene e2patsex32 with longfade
    pp "Mmm, not bad for a quickie [pname]. I actually understand you cumming so quickly, you were so deprived here."
    pp "I really hope we can work together more closely in the future. I have many...talents that would please you greatly."
    scene e2patsex33 with mediumdissolve
    pp "Remember, you need to be patient and cunning to get more chances like this. It won't happen so quickly for you, be smart and acquire power over time..."
    pp "But...as for just now...I wonder if they heard us. What would that be like...hearing our pleasure while suffering such pain?"
    pp "Let's get cleaned up. You're going to drip all over the floor maybe, haha!"
    jump patsexfive

label patsexfive:

    stop seven fadeout 3

    scene e2patsexfive1 with longfade
    pp "Now, we should go back down and relieve your poor fellow trainees."
    scene e2patsexfive2 with longfade
    pp "[pname2], Zach, Body Pain Off! Congratulations, you have finished all testing for the inmate rehabilitation program!"
    pbf "(Oh thank goodness!)"
    scene e2patsexfive3 with mediumdissolve
    pbf "(This whole thing feels like bullshit...rehabilitation my ass...)"
    pp "You all can just go back inside and wait until your results are finalized, probably this evening. You are relieved from any prisoner duties, so take advantage of it and relax!"
    pp "You will be speaking with Sam about your results and your initial employee level. Sometime after that, you will be transported out from our lovely home here!"
    scene e2patsexfive4 with mediumdissolve
    pp "Just remember to obey your new superiors well so you don't end up back here!"
    pp "Farewell worms."
    jump sisnewhire


label sisnewhire:

    scene e2sisnewhire1 with longfade

    play music "<from 8 to 90>music/cassandra.mp3" fadein 1

    p5 "Please, Mistress, have mercy! I can't take anymore! Where are you?"
    p5 "I'll do anything!"
    cass "Haha! Poor baby."
    scene e2sisnewhire2 with longdissolve
    p5 "Pleeeease don't leave me here alone anymore! Please!"
    cass "Mmmm...yes, beg you little bitch, haha!"
    scene e2sisnewhire3 with longdissolve
    p5 "No no no no...she's leaving me here forever...she's never coming back...please...please..."
    cass "Ohh, yes...."
    scene e2sisnewhire3b with mediumdissolve
    p5 "Help! Someone! Please help, help help!"
    cass "Poor Danny, you were so much fun...mmmm"
    scene e2sisnewhire4 with longfade
    a "And this will be your private theater where you can observe and watch..."
    sis "(Wow. Oops.)"

    stop music fadeout 2

    a "...Cassandra! You were supposed to just test the private theater, not use it for your own personal pleasure! Shut that off right now!!!"
    scene e2sisnewhire5 with longdissolve
    cass "Oh my God, I'm sorry Mistress Alessandra! I was just err...ok, you caught me."
    cass "I was getting off watching Prisoner Danny. I'm so sorry! I thought you were coming in another hour."
    scene e2sisnewhire6 with longdissolve
    a "[pname3], this is now two poor first impressions of us at The Karlsson Group, I am so sorry! I will be sure to...teach...her to listen better."
    cass "I'm really sorry, I just wanted to try this huge screen and..."
    a "Enough! You only use it if [pname3] allows you from now on! Get yourself together! We have a little business to discuss."
    scene e2sisnewhire7 with longfade
    a "Now, [pname3], this horny little thing is your executive assistant, Cassandra."
    a "Although her first impression was very poor, she in fact is extremely intelligent and very capable of assisting you with all aspects of running the prisoner program."
    scene e2sisnewhire8 with mediumdissolve
    cass "It's a pleasure to meet you, Mistress [pname3], I have been preparing diligently for your arrival. I am looking forward to working with you."
    sis "A pleasure to meet you too."
    menu:
        "(Show a little disapproval of her bad first impression.) [SisDomPath]":
            $ sisdom += 1
            $ sis_c_p -= 1
            scene e2sisnewhire9 with mediumdissolve
            sis "I hope you can show much more than your first impression Cassandra."
            cass "Yes! You will see, I will be an incredibly good employee for you Mistress [pname3]!"
            jump sisnewhire2
        "(Don't say anything about her first impression at all. Just greet her and move on.) [SisSubPath]":
            $ sissub += 1
            scene e2sisnewhire10 with mediumdissolve
            sis "I also am looking forward to working with you. I know we probably have a lot to go over."
            cass "Yes we do, but I have been preparing for months to get you ready. I will get you up to speed quickly so we can hit the ground running."
            jump sisnewhire2
        "(Express mild disapproval of her first impression unless she shows you the rest of the movie she was watching later.) [SisEvilPath] [SisCassPath]":
            $ sisevil += 1
            $ sis_c_p += 1
            scene e2sisnewhire11 with mediumdissolve
            sis "Well Cassandra, I am mildly unhappy at your first impression."
            sis "I think the only way you can make it up to me is to put that movie on later for me. I want to see how it ends."
            scene e2sisnewhire12 with mediumdissolve
            cass "Of course Mistress [pname3]...I'd love to show you more....it's very enjoyable."
            sis "Good. I look forward to it."
            jump sisnewhire2

label sisnewhire2:

    scene e2sisnewhire13 with longdissolve

    play seven "music/theatre.mp3" fadein 3

    a "Now, [pname3], as I was saying, this room will be your private theater during the program. You will be able to instantly feed any live camera or prior recording to this screen."
    a "Of course, you will have access to all of this in your own office as well, but being able to see it on this large of a screen can be...helpful."
    scene e2sisnewhire14 with mediumdissolve
    a "There are hundreds of security cameras that will be live and at your disposal. Only you and the Board will have full access to everything so it's a considerable level of trust for you."
    sis "Thank you Alessandra, I won't betray that trust."
    a "Oh, I'm not worried at all! I am confident you are one of us in all the best ways. You just had a very poor start in life, that's not your fault."
    a "Now let's take this back to the lobby, I am tired of this dark theatre. Cassandra can teach you more about this later."
    scene e2sisnewhire15 with longfade
    a "Now [pname3]...the power you are about to hold with this position...it's where you belong. Really. I truly want you to succeed and fit in right away."
    sis "I really appreciate the faith and hope you are showing me. I won't forget it. I'll do my best."
    scene e2sisnewhire16 with mediumdissolve
    a "I really...I really wish we had met earlier in life. We could have been so...anyway..."
    scene e2sisnewhire17 with mediumdissolve
    a "Oh, I forgot to add that sometimes the theater will be used during the program for private screenings with a small select group of people, but I will let you know much more about that later."
    cass "Oh Mistress [pname3], it's so much fun! It's just a nice little party to watch some poor..."
    a "...Cassandra, that can wait. We need to get her up to speed as soon as possible. I expect you to help her be ready when the prisoners arrive."
    scene e2sisnewhire18 with mediumdissolve
    cass "Of course Mistress Alessandra. I will make her the best manager this program has ever seen!"
    a "Now, I think that's enough for today. Let's tour more tomorrow. I'd love to take you out to a luxury dinner because you have been deprived of life's pleasures way too long [pname3]!"
    a "You can come too Cassandra. I expect all three of us to have a good working relationship to make this all work well."
    scene e2sisnewhire19 with longdissolve
    a "But I do want to settle one decision right now as I have to finalize some budget items after dinner. Sorry this will be a little dry and boring but it's necessary."
    a "[pname3], you have a set budget for six months for the prisoner program staff. Now I can't change the guards' pay as it's locked by a prior contract at 3000 dollars over six months for each of them."
    a "I think you want the guards happy anyway and that's great pay. Your own pay is roughly 208 thousand dollars for six months and you can earn more with bonuses but that's not important yet."
    a "Your other servant staff of about fifty people will make about twenty seven thousand dollars over six months combined, which is about 540 dollars over six months for each of them."
    scene e2sisnewhire20 with mediumdissolve
    a "The last two items are the actual prisoners' pay and Cassandra's overall pay and benefits."
    a "We need a set budget for these two things, and I think it should be your first decision."
    scene e2sisnewhire21 with mediumdissolve
    a "Prisoners in the past have made about 1 to 2 dollars per day in the program, a little less than the typical 3 per day for servants. They use that to buy food and other items from us."
    a "Now Cassandra's salary is set at 30000 dollars over six months. But she is also requesting a clothing allowance, a car, and a personal assistant as extras. Let's figure this out right now."
    scene e2sisnewhire22 with mediumdissolve
    a "You can give her these bonuses or instead use the money on the prisoners so they can have a little more for food and expenses."
    sis "How will their lives be different with the possible pay? I don't know the actual impact at all."
    a "Ok. Basically, giving Cassandra her wishes will force the lower ranks especially to eat mostly bread and very poor food. Not enough to hurt them, but they won't ever really enjoy mealtime."
    a "Denying her request likely gives them an occasional decent meal and better little comforts. This would mostly impact lower ranked prisoners as the higher ones have have set food guidelines."
    menu:
        "(Cassandra at 30000 dollars is making more than the entire help staff of fifty people combined at 27000! I think she can survive ok. Give the prisoners a full amount of extra money to survive better and don't give Cassandra any of her extras.) [SisGoodPath]":
            $ sisgood += 1
            $ sis_c_p -= 2
            $ richprisoners = True
            scene e2sisnewhire23 with mediumdissolve
            sis "Cassandra, I think you can survive on 30000 dollars. Maybe we can talk about the assistant later though."
            cass "Of course Mistress [pname3], I can make do with that pay."
            a "Of course she can. The average pay for even decently well off people now is only 2 thousand a year. The pay is more than generous."
            jump sisnewhire3
        "(I think Cassandra can survive without the car and this decision is balanced, maybe the safest choice for me without more understanding of this program. Give the prisoners a little extra money from her car request, but give Cassandra a clothing allowance and no assistant.)":
            $ sis_c_p -= 1
            scene e2sisnewhire24 with mediumdissolve
            sis "Cassandra, I'm going to give you a clothing allowance because I want you to always look good, but your car money will go to the prisoners overall fund."
            cass "Of course Mistress [pname3], I appreciate you giving me some of what I asked for."
            jump sisnewhire3
        "(I don't think I should show leniency to the prisoners right away and look weak. They probably want me to be tough on the prisoners. Give Cassandra her clothing and car, and condition giving her an assistant on her performance with no money for the prisoners.) [SisEvilPath] [SisCassPath]":
            $ sisevil += 1
            $ sis_c_p += 2
            $ poorprisoners = True
            scene e2sisnewhire25 with mediumdissolve
            sis "Cassandra, I want you to be happy as I need to rely on you, so I will give you the clothing allowance and car. But, getting an assistant will depend on future performance."
            sis "I don't want to just give you everything you ask for without knowing how you actually work for me."
            cass "Oh thank you Mistress [pname3]! I completely understand and I will earn it from you, you'll see!"
            jump sisnewhire3

label sisnewhire3:

    scene e2sisnewhire26 with longdissolve
    a "Good, glad that is all settled. Now I'm famished, and I'm going to take us to Decadance to enjoy our meal."
    scene e2sisnewhire27 with mediumdissolve
    cass "Oh wow! I've never had the chance to eat there, I'm so excited, Mistress [pname3], it's one of the most luxurious restaurants in the whole world!"
    cass "I hear it's like 1000 dollars or more to eat there!"
    sis "(Wow, that is what I was making in a whole year before.)"
    scene e2sisnewhire28 with mediumdissolve
    a "It's expensive, but I want you two girls to get a good reward to start as motivation to do well. We are all counting on you both."
    sis "We won't let you down Alessandra."
    cass "Definitely not! Let's go eat! I'm so excited!"

    stop seven fadeout 3

    scene e2sisnewhire29 with longfade
    a "*whispering* [pname3], Decadance is actually Karlsson owned so you and I can eat there anytime together for free, but don't tell Cassandra!"
    a "That's only a perk for executives all the way at the top of the food chain. Cassandra's very well paid and elite in this world compared to most, but she's still way below you and I."
    a "I can't wait to show you the true meaning of what decadance actually means..."
    jump elenapride

label elenapride:

    scene e2elenapride1 with longfade
    ec "(I need to at least tell her how I feel about this...)"
    scene e2elenapride2 with longfade

    play five "music/veronica.mp3" fadein 2

    ec "Veronica, I'm here."
    scene e2elenapride3 with mediumdissolve
    v "So you are. You've done well to help setup everything for the Gambit."
    v "I think things will move forward without much complication."
    scene e2elenapride3b with longdissolve
    ec "Oh my God, his penis is so huge! I don't even know if I want it that big...how does he work? Can you at least shrink it a little?"
    v "Yes, and he stays paralyzed as long as you wish. One can also make him feel pleasure, nothing, or pain during the act. His erection can last over six hours usually and of course he can't cum ever."
    v "You can attach a number of our add ons or morphs to his penis for vibration or other sensations while doing it. So many women could use him non-stop if it was the right kind of party I suppose."
    scene e2elenapride3c with longdissolve
    ec "Wow. I can only imagine the interest. This wretch must have been so desperate."
    v "As is always the case. I even wore this stupid dress to help with the early testing protocols. Oh, his hearing is deadened to deafness right now. We can talk freely."
    v "Because...you obviously came for another reason."

    stop five fadeout 3

    scene e2elenapride4 with mediumdissolve
    v "I can see you are still deeply troubled by what you discovered recently."

    play seven "music/sisintro2.mp3" fadein 3

    ec "Wouldn't you be in my shoes? Your father...what he did to me is..."
    scene e2elenapride5 with mediumdissolve
    v "Unconscionable. Horrible. Cruel. Yes, of course it's terrible what he did to you. Are you really shocked by my father doing what he did?"
    v "You know he would always do whatever he wanted for his own selfish interests at the expense of everyone else."
    scene e2elenapride6 with mediumdissolve
    v "Even at the expense of his own daughters. That was my father. You know this as well as I."
    ec "Yes. But still...it's...and now you are telling me to stay silent, that I can't talk to...I have a right to speak with..."
    scene e2elenapride7 with mediumdissolve
    v "...I didn't say you can't talk or do whatever you want, only that breaking your silence now will have consequences."
    tp "*weakly* plllllllssss...the pain..."
    v "Namely, it would impact one's ability to participate in and win the Gambit. Would you do that before it's even really started? Take that chance away?"
    scene e2elenapride8 with mediumdissolve
    ec "No, no, I don't want to spoil that chance. But surely I can do something to help quietly or..."
    v "No! You must trust me on this. I am making sure everyone, and I mean, everyone has their chance."
    ec "But why did he even do it? What's the point?"
    v "Think hard. Think about how my father thinks...and the idea of having a different experience than say my own...and with whom one would be around day after day."
    scene e2elenapride9 with mediumdissolve
    ec "Callista. I understand now. It's still horrible, but I see what his mind was thinking now. But why me?"
    v "You should feel complimented in a perverse way. You were always the smartest and strongest to him after her. And rememeber how my father grew up."
    scene e2elenapride10 with mediumdissolve
    ec "I see. Callista...did she know? She wouldn't have done this voluntarily, would she?"
    v "I don't know. Her goodness and purity could work either way for this question if you think about it. You also were apparently out of control in those days?"
    ec "Err...yes. I would agree with that. I was young and arrogant."
    scene e2elenapride11 with mediumdissolve
    ec "I am sure you know a lot more than you are telling me. Can you tell me anything else?"
    v "Not yet. But have some faith in me. And even in Callista."
    ec "I guess I do. And you are wrong about your father in one sense. He didn't always only follow his selfish interests at the expense of others. You didn't see this, but I did."
    ec "He would have done anything for Callista. Anything."
    scene e2elenapride12 with longdissolve
    v "I wish I had seen that version of my father and...I believe you. Isn't this Gambit proof of that in one sense?"
    ec "Yes, I suppose so."
    scene e2elenapride13 with mediumdissolve
    v "Now, we have a lot to do, so please prepare."
    ec "Ok. I have to trust you. I will do my part."

    stop seven fadeout 3

    jump kanetest

label kanetest:

    scene e2kanetest1 with longfade

    play seven "music/darkness.mp3" fadein 2

    p "(Always fun to have to sit and wait to find out if your life is going to take an even bigger crap on you or not.)"
    p "(There's no doubt in my mind that this whole thing is more than a mere rehabilitation program.)"
    scene e2kanetest2 with mediumdissolve
    p "(But what...I have no idea yet. I just have to survive as best as I can for now.)"
    p "(And that weird hacker...who is that, and what could everyone want from me? I don't have anything unique that I know of...)"
    scene e2kanetest3 with longdissolve
    pbf "You're up [pname]."
    p "[pname2]!"
    p "What happened?"
    scene e2kanetest4 with mediumdissolve
    pbf "I passed. But K4. It's the lowest we can start."
    p "It's just the start. We can adapt and move up I bet. I'm just glad you're not stuck here in prison. Look on the bright side."
    scene e2kanetest5 with mediumdissolve
    pbf "[pname], I'm not actually sure where we are going will be better than prison. I really don't know..."
    p "Look, we know how bad it is here. We also know it's six months wherever we are going versus a longer time here."
    p "We just have to make the best of it and hope it's better. We can do this."
    scene e2kanetest6 with mediumdissolve
    pbf "You're right [pname]! I can't get too down, gotta make the best of it."
    p "Alright then. I guess I better get in there and find out my fate."

    stop seven fadeout 2

    jump kaneresult

label kaneresult:

    scene e2kaneresult1 with longfade

    play seven "music/samintro.mp3" fadein 3
    pp2 "Ah, [pname], I've bet you have had quite the eventful day, haven't you? Have a seat."
    pp2 "Me too actually. I'm so sad I had to miss your training, and I so wish I could tell you what I did instead, but...orders are orders."
    scene e2kaneresult2 with mediumdissolve
    pp2 "Even I have to be a good little servant at times."
    pp "But I guess you are quite curious how you did on your testing today, aren't you?"
    menu:
        "(Ask her directly how you did.) [DomPath]":
            $ dom += 1
            scene e2kaneresult3 with longdissolve
            p "Just tell me how I did and get it over with."
            pp2 "Oh [pname], you have to let me build up some anticipation for it!"
            pp2 "But ok. I'll just tell you."
            jump kaneresult2
        "(Stay silent.) [SubPath]":
            $ sub += 1
            scene e2kaneresult4 with longdissolve
            pp2 "Ah, not so curious? Maybe I shouldn't tell you?"
            pp2 "But of course I will because I'm such a sweet girl!"
            jump kaneresult2

label kaneresult2:

    scene e2kaneresult5 with mediumdissolve
    pp2 "So overall [pname], it was pretty sad. Twelve of you tested, and out of the other eleven, two outright failed, and all nine of the others tested to K4 to start."
    pp2 "Not an impressive batch at all."
    pp2 "And in your case [pname]..."
    if slavepoints >= 10:
        $ pissboy = True
        $ k4 = True
        scene e2kaneresult6 with mediumdissolve
        pp2 "...I am kind of surprised to say that you were so pathetic that you would have failed the program if Elena didn't mandate you pass no matter what!"
        pp2 "But don't fret [pname], I may have a small treat for you later for doing so poorly."
        scene e2kaneresult7 with mediumdissolve
        pp2 "So you start as K4 for the program. I hope you can do a lot better than what you showed here during the actual program..."
        pp2 "...but then again, you can always come back and see if you really fail badly out there. That would be a lot of fun...for me."
        jump kaneresult3
    elif slavepoints >= 3:
        scene e2kaneresult6 with mediumdissolve
        $ k4 = True
        pp2 "...I am not surprised to say you tested at K4, same as almost everyone else. I was hopeful you could do a little better, but I guess not."
        pp2 "So that's where you will start under the program. I hope you can do a lot better than what you showed here during the actual program..."
        scene e2kaneresult7 with mediumdissolve
        pp2 "I'd just hate to see you back here, although that would be a lot of fun for me maybe, haha!"
        jump kaneresult3
    elif slavepoints >= 1:
        $ k5 = True
        scene e2kaneresult8 with mediumdissolve
        pp2 "...I am surprised to say that you ended up grading out to start as a K5 employee! That's pretty good!"
        pp2 "I think less than two percent of prisoners have ever tested this well, so you should feel proud! But you might have one small final test later..."
        jump kaneresult3
    else:
        $ k6 = True
        scene e2kaneresult9 with mediumdissolve
        pp2 "...I am stunned! You tested out to start as a K6 employee! That hasn't happened in years!"
        pp2 "Very impressive [pname]! And I'm not just bullshitting or being sarcastic! But, you might have one small final test later."
        jump kaneresult3

label kaneresult3:

    scene e2kaneresult10 with longfade
    pp2 "Now [pname], it sounds like your transportation is delayed until tomorrow, so it looks like you get one more night at our fancy hotel, haha!"
    pp2 "You'll leave I think first thing in the morning. I look forward to seeing how you do [pname]."
    jump sethwake

label sethwake:

    scene black with longfade

    play seven "<from 10 to 151>music/juliette2.mp3" fadein 1

    bro "(Ugh, oh no my head is in such pain again...but my body feels a lot more pain free?)"
    ky "Right there, yes! I'm about to...yeesssssss!"
    scene e2sethwake1 with longfade
    bro "(What the?)"
    ky "Perfect, good job Derek! I've been really stressed with all the recent demands by my Mistress, so this helped a lot. Rest your poor head and tongue."
    scene e2sethwake2 with longfade
    ky "Thanks again, that was so pleasant. But I'm afraid that your theft from Mistress Veronica is unforgivable."
    ky "So your usefulness is at an end and I have to..."
    bro "(Hey! Wait...I can't talk!)"
    scene e2sethwake3 with quickdissolve

    stop seven fadeout 3

    ky "...Oh, are you awake? Don't try to talk, you've been given something for that and don't ask what, I'm no science person."
    ky "I just know this poor soul here and you both were silenced with some weird orange drink, it sure didn't look like orange soda or something..."
    bro "(What the hell is happening?)"
    scene e2sethwake4 with longdissolve

    play eight "<from 81 to 131>/music/s1.mp3" fadein 2

    ky "I'm not really supposed to talk to you, but I didn't expect you to wake up right now. Someone screwed up as you should have been out for a few more hours."
    ky "Probably wondering where you are, huh? You'll have to get used to the tinted lighting, it's designed for some kind of scanning thing I have no clue on."
    bro "(Yes! Where am I??!?)"
    scene e2sethwake5 with mediumdissolve
    ky "Hopefully, you never meet me again alone in this room after today. If you do, it's probably over for you. I'd hate to have that happen."
    ky "You seem to have a kind face. I like it. I don't know why you are here, but I would suggest you quickly do anything Mistress Veronica says no matter what."
    bro "(Who is that? Hmm...Karlsson Group...Veronica Karlsson?? Why am I here? I thought I was going to a hospital!! Elena, Katherine, Sam...all in on a lie I bet...)"
    scene e2sethwake6 with mediumdissolve
    ky "I really shouldn't talk to you any further, but I feel a little sorry for you, so I'll say you are in a research facility."
    ky "Why you are here I have no idea, but I hope it works out for you. I really shouldn't say any more than I have already."
    scene e2sethwake7 with mediumdissolve
    ky "But Mistress Veronica clearly has told people here that you are a special case, so maybe that's good?"
    bro "(Research...am I in some kind of mad doctor's lab or something??? I don't know much about Veronica Karlsson...have to assume it's her...)"

    stop eight fadeout 3

    scene e2sethwake8 with mediumdissolve
    ky "Now I have to get going for a very important job, I get to meet a professor! Plus, I have to finish this one behind me here. He's so weak now...drugged, and I umm...wore out his last energy."

    play seven "music/death1.mp3" fadein 3

    ky "Hmm, maybe you want to close your eyes for a little bit? I don't think you want to see what I have to do here."
    bro "(What is she going to do? Torture him?)"
    scene e2sethwake9 with mediumdissolve
    ky "Unfortunately, this other man here has committed a crime against the Karlsson Group. And part of my job is to...clean up our staff so they don't do the wrong thing."
    ky "Sorry you are awake for this. I do suggest you close your eyes. You know what? I'll make it extremely quick since you are awake, but it's never good to see someone die if it can be avoided."
    menu:
        "(She's going to kill him? I think I don't want to see this at all.) [BroKiyomiPath]":
            $ bro_k_p += 1
            scene black with mediumdissolve
            bro "(No desire to see it...)"
            ky "You really do seem like a kind soul. I hope it works out for you here."
            ky "1...2...3...*sound of neck snapping*...ok, I'm done."
            jump sethwake2
        "(I need to see everything I can, even this unfortunately.)":
            scene e2sethwake10 with mediumdissolve
            ky "I really wish you wouldn't look, but I'm going to spare you a frontal view."
            ky "1...2...3...*sound of neck snapping*...ok, I'm finished."
            jump sethwake2

label sethwake2:

    scene e2sethwake11 with longfade
    ky "I'm sorry you had to be around for that unfortunate business. It's just work for me you know. I was trained as a killer from age 12 so I am what I am."
    bro "(Yeah, but I just saw you get off on the guy right before...doesn't seem all business all the time...)"

    stop seven fadeout 3

    scene e2sethwake12 with mediumdissolve
    ky "I have to go now. But I will tell one of the science people that you woke up early."
    ky "I wish you could talk so I could at least get your name. I never did hear it from anyone here. My name is Kiyomi. It was nice to meet you."
    scene e2sethwake13 with mediumdissolve
    ky "Take care of yourself, and remember what I said. Mistress Veronica is the Queen here. Make her happy."
    bro "(Obvious advice...but appreciated...why the hell was I brought here?)"
    scene e2sethwake14 with longfade
    bro "(Does this have anything to do with [pname] and [pname3] and is anything Elena said about either of them even true? Are they trapped here too somewhere?)"
    bro "(Even so, my pain right now is still so much lower than before today, so they have made me much stronger...why...just have to figure it out and survive somehow...another shitty day.)"
    jump oliviafinal

label oliviafinal:

    scene e2oliviafinal1 with longfade

    play seven "<from 75 to 197>music/oliviagood.mp3" fadein 3

    sis "(Oh my God...what a great day! That was the best dinner ever! I could get so used to this...what must it be like for Alessandra day to day who can do almost anything she wants...)"
    sis "(This is so amazing. I can't believe this has happened to me. Maybe I should be more suspicious that they are giving me so much power, money, and trust...)"
    scene e2oliviafinal2 with mediumdissolve
    sis "(But I genuinely feel like Alessandra is in my corner and wants me to do well. I don't know about anything else, but I trust my gut on her.)"
    sis "(I'll just have to figure things out as I go along and do great with the job. I know I have a very smart mind despite my lack of education, so I think I can manage everything ok.)"
    jump oliviafork

label oliviafork:
    if sisevil >= 3:
        jump oliviaevil
    else:
        jump oliviadefault

label oliviadefault:
    scene e2oliviadefault1 with longfade
    sis "Are you almost finished with the cleaning Nathan?"
    nath "Yes, Mistress [pname3], I wiped down everything in the entire room."
    scene e2oliviadefault2 with mediumdissolve
    sis "And the bathroom?"
    nath "Yes, Mistress. The entire tub, floor and toilet too."
    menu:
        "(Praise him for his work and give him a bonus of 5 dollars for his hard work.) [SisGoodPath]":
            $ sisgood += 1
            scene e2oliviadefault3 with mediumdissolve
            sis "Excellent Nathan. I'm going to give you a 5 dollar bonus for your hard work."
            sis "But don't expect a bonus every time, it's just because this is your first assignment for me."
            scene e2oliviadefault4 with mediumdissolve
            nath "Oh thank you Mistress [pname3]! I will always work my hardest for you!"
            sis "That's fine Nathan. Now please head out, I wish to relax now."
            nath "Yes, Mistress."
            jump oliviaend
        "(Just thank him for his work and send him on his way.)":
            scene e2oliviadefault5 with mediumdissolve
            sis "Fine. I hope everything is perfectly clean."
            sis "Now go, I wish to relax now."
            nath "Yes, Mistress [pname3]."
            jump oliviaend

label oliviaevil:

    stop seven fadeout 2

    scene e2oliviaevil1 with longfade

    play five "music/oliviaevilbath.mp3" fadein 3

    sis "Are you almost finished cleaning, servant nathan?"
    nath "Yes, Mistress, I brushed the entire room! I did my best...using a toothbrush is very hard but I..."
    sis "I don't care about your best, only that you do exactly what I want."
    scene e2oliviaevil2 with mediumdissolve
    nath "Of course Mistress [pname3], I will always do..."
    sis "...Enough talking. Don't speak again unless I tell you to. Let's see your cleaning skills. Follow me."
    scene e2oliviaevil3 with longfade
    sis "Now, I want you to lick the inside of this toilet to make sure it's perfectly clean."
    nath "Mistress? I..."
    scene e2oliviaevil4 with quickdissolve
    nath "Ugh!"
    sis "Didn't I say not to talk? Are you really this stupid? Now lick."
    scene e2oliviaevil5 with longdissolve
    sis "Very good nathan."
    sis "(I can't believe how exciting it is to humiliate someone...)"
    sis "Keep licking around the sides..."
    scene e2oliviaevil6 with longfade
    sis "Now I'm such a nice girl, so I'm going to give you a refreshing drink, so lick the water too! If you do, I won't push your head in the water, just use your tongue well!"
    scene e2oliviaevil7 with mediumdissolve
    sis "That's it...see how generous I can be? Fresh water after some hard work, haha!"
    jump oliviafork2

label oliviafork2:
    if poornath and sisevil >= 6:
        jump toilet
    else:
        jump oliviafootstool

label toilet:

    scene e2toilet1 with longfade
    sis "You know servant nathan, I just realized that your three dollar pay cut that is now part of my pay takes over six months to even hit 100 dollars."
    sis "What could 100 dollars do for you and your poor little brother? I wonder...stay here a second and don't move, be right back."
    scene e2toilet2 with longfade
    sis "One tiny little 100 dollar bill..."
    sis "With your new pay rate of $9 a week, that's almost three months of hard work. Wow."
    scene e2toilet2b with mediumdissolve
    sis "I have to work hard too for 100 dollars. Not quite three hours for me, haha!"
    scene e2toilet2bb with mediumdissolve
    sis "Oh, I dropped it..."
    scene e2toilet2c with mediumdissolve
    sis "It fell in the toilet...put your head in there and grab it with your mouth, not your hands. Now."
    scene e2toilet3 with mediumdissolve
    sis "*flushing sound* Oops."
    scene e2toilet4 with longdissolve
    sis "Oh, I guess you could have really, really, used that money, huh? Now you can get off your knees and stand up. I want to see your face better."
    scene e2toilet5 with longfade
    sis "So tragic. That could have helped you SO much I bet."
    sis "I would give something to help you a little, but I need to blow 5000 dollars, oops 4900 on clothes for my new position. You understand I'm sure."
    scene e2toilet6 with mediumdissolve
    sis "Now..maybe if you slave away perfectly for me this month, you can grovel for a few extra dollars from me. So you better work hard."
    jump oliviafootstool

label oliviafootstool:

    scene e2oliviafootstool1 with longfade
    sis "And...I guess you pass the cleaning check. But you have one more job. I want to relax now..."
    scene e2oliviafootstool2 with longfade
    sis "Ah, this is so wonderful isn't it servant nathan? We can watch a wonderful film together!"
    sis "I'll have to get comfortable with pillows and a blanket, but let's test how comfortable you are!"
    scene e2oliviafootstool3 with mediumdissolve
    sis "Oh I forgot, I wanted you to keep your head down the whole time. But you can still listen to the movie!"
    sis "And I expect you to not move a muscle for the next two or so hours or I will make you clean the entire room again!"
    scene e2oliviafootstool4 with mediumdissolve
    sis "Aren't you so happy that I am now your new boss? Lucky you!"

    stop five fadeout 3

    sis "We're going to have so much fun together!"
    jump kaneend

label oliviaend:
    scene e2oliviaend1 with longfade
    sis "(Ah, what a great day...!)"
    jump kaneend


label kaneend:

    scene black with longfade
    pp2 "Ah, we have a little bit of time for you [pname]!"
    scene e2kaneend1 with longfade
    pp2 "I couldn't let you leave without a last little visit with me!"
    if elena_mentor:
        kk "Good to see you again [pname]!"
        p "Hello. (Oh, she's here...)"
        jump kaneend2
    else:
        kk "Hello there [pname], my name is Kitty, I work for Elena. I've heard a lot about you."
        p "Err, hello there."
        jump kaneend2

label kaneend2:

    if k4:
        jump kanesubend
    elif k5 or k6:
        jump kanedomend
    else:
        jump kanesubend

label kanesubend:

    scene e2kanesubend1 with longfade
    pp2 "Well [pname], as a newly minted K4 employee, I think we should give you a small taste of what that means..."

    play seven "music/pattest2.mp3" fadein 3

    pp2 "You know, Kitty here was once a K4 a long time ago, but she managed to go way above that. Who knows [pname], maybe you can do the same."
    scene e2kanesubend2 with mediumdissolve
    pp2 "Although you have showed nothing but weak tendencies, so I have my doubts."
    scene e2kanesubend3 with mediumdissolve
    pp2 "Elena won't let me go all out on you, so consider yourself lucky. But this wooden toy here still might be fun for you. Well, ok more fun for me anyway."
    kk "Oh, I want to see that!"
    scene e2kanesubend4 with mediumdissolve
    pp2 "Strip and then get your ass in there, or I will shock you so bad you won't believe it. That does no permanent damage, so Elena would let me get away with that..."
    kk "Oh no, poor [pname]!"
    p "(Damnit...)"
    scene e2kanesubend5 with longfade
    pp2 "I can't destroy you, but I think a little light pain is more than appropriate for such a lowly employee. I have a little toy to help..."
    pp2 "This won't leave any permanent scars. Kitty, keep him busy on your end too."
    scene e2kanesubend6 with mediumdissolve
    pp2 "*thwack* Oh [pname], you do have a cute ass, I do wish I could make it bleed but we can at least give it a little more color! *thwack* *thwack*"
    if samsadist:
        p "(At least there's no red box with rats here I guess...urrgh)"
        jump kanesubend2
    else:
        p "(Urrrgh...)"
        jump kanesubend2

label kanesubend2:

    scene e2kanesubend7 with longdissolve
    kk "I hope my feet taste good for you, haha! Maybe you should lick them, I'll tell Sam to hit you softer then."
    scene e2kanesubend8 with mediumdissolve
    pp2 "*thwack* You're too nice Kitty, treat him a little rougher!"
    kk "Ok! Hmm, I have an idea!"
    scene e2kanesubend9 with mediumdissolve
    kk "How about a nice kick to your face, hee hee! I've never done this before, I want to savor every moment..."
    scene e2kanesubend9b with quickdissolve
    kk "Does it hurt?"
    scene e2kanesubend10 with mediumdissolve
    kk "Sam, can you ummm, penetrate him from behind with something?"
    pp2 "*thwack* *thwack* I wish, someone specifically wants to deflower him there, haha! Oh [pname], you're so screwed later, literally on that one!"
    scene e2kanesubend11 with longdissolve
    pp2 "Kitty, I'm done for now. Come on this side and paddle him. I want to see his face while you do it."
    kk "Ok Samantha! Poor [pname], maybe my foot can be nice too, see?"
    scene e2kanesubend12 with longfade
    kk "Here we go! *thwack* *thwack*"
    p "(Ugh, she's actually hitting me harder! Maybe she's just stronger naturally...)"
    scene e2kanesubend13 with mediumdissolve
    pp2 "Oh poor [pname], I could watch your face in pain all night. It really gets me hot. And do I think this is your life now."
    pp2 "To submit and serve. *thwack* *thwack* To endure the whims of sadistic superiors all around you."
    scene e2kanesubend14 with mediumdissolve
    kk "This is fun!"
    pp2 "Believe it or not, Elena has told me Kitty has a ton of natural sadism. Hard to believe as I think her face looks so innocent..."
    pp2 "Although I hear her sister is the worst of all...maybe worse than even Juliette Karlsson."
    scene e2kanesubend15 with mediumdissolve
    pp2 "*thwack* *thwack* If Kitty is really that cruel, that doesn't bode well for someone else you know, haha!"
    kk "Hey, I'm nice, hee hee!"
    p "What do you mean?!"
    pp2 "Oh, nothing [pname], you have to worry about yourself I think."
    scene e2kanesubend16 with mediumdissolve
    pp2 "We have to wrap this up Kitty, give him one last huge whack."
    kk "Ok, Samantha, his ass looks so nice right now! Maybe Elena will be mad at me for going a little too hard?"
    scene e2kanesubend17 with longdissolve
    kk "Oh well, I can't resist, never got to do this before, it's so fun! *thwack* [pname], ooohhh, don't sit too much tonight."
    pp2 "You should have done better on testing [pname], you're going to endure a lot during your...rehabilitation."
    scene e2kanesubend18 with longdissolve
    pp2 "Oh Kitty, I've recorded our little play session. I'll get you a copy. Why don't you play this for a certain someone, haha!"
    p "(What is she talking about!?)"
    kk "Oh, good idea, haha!"
    pp2 "Let's take this pathetic so called new employee back his to cell..."

    stop seven fadeout 3

    jump lastep2

label kanedomend:

    scene e2kanedomend1 with longfade
    pp2 "So [pname], you are only starting out as a mid-level employee, but believe me, to get anything over K4 right away is a huge deal."
    pp2 "You are already starting ahead of virtually anyone that has ever been in this position, so you will be especially watched for future potential."
    scene e2kanedomend2 with mediumdissolve
    pp2 "And by potential, I mean much more beyond a mere servant employee, but something greater. Much greater."
    scene e2kanedomend3 with mediumdissolve
    pp2 "Kitty here is a great example. She was basically in a similar position as you, no more than a prisoner and virtual slave."
    pp2 "And now, she has just been promoted by Elena to do much, much more. The floor is yours Kitty."
    scene e2kanedomend4 with mediumdissolve
    kk "So [pname], I do have one final little test for you. It's from Elena directly and only available because you went beyond K4 on your testing."
    if elena_mentor:
        kk "Consider this part of your mentoring from her. I can tell you that she is gratified that her first instinct on you was correct."
        jump kanedomend2
    else:
        kk "Although you failed to impress her completely during your very first interview with her, now you have done enough to warrant more attention from her."
        jump kanedomend2

label kanedomend2:

    scene e2kanedomend5 with longdissolve
    p "Ok, what is this final little test?"
    kk "I'm glad you asked [pname]. The reality you will learn quickly, like Sam and I did, is that you are either going to control your life or be controlled by others."
    scene e2kanedomend6 with mediumdissolve
    kk "Now there is no completely right and wrong answer for Elena, but she wants to see what kind of person you are when given certain choices."

    play seven "music/pattest2.mp3" fadein 3

    kk "So the test is that Sam here is going to be put in this nice wooden toy here. And I'm going to give you a paddle."
    pp2 "Be nice [pname], haha!"
    scene e2kanedomend7 with mediumdissolve
    kk "Then you just decide what to do with her. You can choose to paddle her ass or not. If so, hit her five times. That's it."
    p "Is she being punished for something she did?"
    kk "No. The test is not the same if she deserves the punishment."
    kk "So Sam, get in there...don't bother with your hands and wrists. They are so thin and tiny that they can just get out! Let's just trap her head."
    scene e2kanedomend8 with longfade
    pp2 "Are you going to be gentle [pname]?"
    kk "Here you go [pname]. I'm curious what you will do. By the way, I had a very similar test to this too."
    p "What did you do?"
    scene e2kanedomend9 with mediumdissolve
    kk "Oh no, that's not allowed [pname]! Ask me later. I am also going to go with you initially when you leave jail here, it's your reward for doing so well."
    kk "Maybe I'll have a little surprise for you...but it might depend on what you do here of course. So go ahead."
    menu:
        "(Is this a test on whether I would just punish someone who doesn't deserve it at all? Maybe Elena wants to see that I operate by some sort of moral code. I won't hit her.) [GoodPath]":
            $ good += 1
            scene e2kanedomend10 with mediumdissolve
            p "I don't want to hit her."
            kk "Why?"
            p "I'm not weak on punishing someone if that's what you are thinking, but I'd rather have an actual reason that makes sense to me, like maybe she did something that deserved it."
            scene e2kanedomend11 with mediumdissolve
            pp2 "Oh, my ass is relieved to hear that [pname], haha!"
            kk "That is an interesting answer. I will share it with Elena. Well...this test ended up a very short one as it turns out."
            pp2 "I'm going to take him back to his cell Kitty...err once you get me out of here please."
            jump lastep2
        "(I don't think Elena wants to see weakness, so I probably should hit her. But, I don't think she wants me to be extreme either without thinking, so I should hit her more normally than with hard force.) [ElenaPath]":
            $ elena_p += 1
            $ redass = True
            scene e2kanedomend12 with mediumdissolve
            p "Alright, I'll hit her."
            kk "How hard?"
            p "Hard enough, but I'm not going to go all out for no reason."
            kk "Ok [pname], go ahead."
            jump kanedomend3
        "(Maybe Elena wants to see that I am completely ruthless and able to do whatever it takes. I'm going to hit Sam really hard.) [KittyPath] [EvilPath]":
            $ kitty_p += 1
            $ evil += 1
            scene e2kanedomend13 with mediumdissolve
            p "Alright, I'll hit her."
            kk "How hard?"
            p "I'm not the type to hold back. So pretty hard."
            kk "Oh, poor Sam...I guess I'm glad it isn't me in there."
            jump kanedomend3

label kanedomend3:

    scene e2kanedomend14 with longdissolve
    kk "Ok, count it off Sam!"
    scene e2kanedomend15 with mediumdissolve
    pp2 "*thwack* Ouch! 1!"
    scene e2kanedomend16 with mediumdissolve
    pp2 "*thwack* 2! *thwack* 3!"
    scene e2kanedomend17 with mediumdissolve
    pp2 "*thwack* 4! *thwwack* 5!"
    scene e2kanedomend17b with mediumdissolve
    kk "Very good [pname], let's take a look at her ass as it sets in..."
    if redass:
        scene e2kanedomend18 with longfade
        kk "Wow, it looks ripe [pname]!"
        pp2 "Hmph..."
        jump kanedomend4
    else:
        scene e2kanedomend19 with longfade
        kk "Oh my goodness [pname], you beat her pretty hard! Maybe you better not sit very soon Sam!"
        pp2 "Hmph, you got me pretty good [pname], maybe you are tough enough for everything."
        jump kanedomend4

label kanedomend4:
    scene e2kanedomend20 with longfade

    stop seven fadeout 3

    pp2 "Well...I hope you had your fun [pname]. I'll take you back now, expect to leave I think first thing in the morning."
    kk "I'm looking forward to seeing you again tomorrow [pname]!"
    jump lastep2


label lastep2:

    scene black with longfade
    ec "(I still can't sleep. I thought complete and pitch blackness could help...but no.)"
    ec "(Did she know? Was she right all along about me?)"
    ec "Alicia activate please!"
    al "{i}Yes, Elena.{/i}"
    ec "When I transferred to your A.I. did you retain all music from the prior artificial intelligence program?"
    al "{i}Yes. All 7,214 tracks and...{/i}"
    ec "Never mind that. I'm only interested in one right now. It's called New Life, written by...written by Callista [pname_f]."
    al "{i}Yes, last played 22 years and...{/i}"
    ec "...just play it please."

    play music "music/thesong.mp3" fadein 2

    ec "Thank you Alicia. Alicia, deactivate to privacy mode."
    scene black with longfade
    ec "(Do I dare even...how could he...and Callista. Callista...we were so close once...but...)"
    ec "(I can't just sit by during the Gambit and stay completely neutral can I? I want to...I...I have some tough decisions to make...)"
    scene black with longfade
    ec "(...very tough decisions...)"
    jump endepisode2


label endepisode2:

    stop music fadeout 2

    play seven "music/zend.mp3" fadein 2

    scene black with longfade
    z "Save by the end of the next screen to preserve an End of Episode 2 save! Don't do it after the mask!"

    scene zendsavegame with longfade

    $ renpy.pause (10.0, hard=True)

    stop seven fadeout 3

    z "Episode 3 awaits! Enjoy yourself!"
    jump startepisode3

label startepisode3:

    scene chess2 with superfade

    play two "<from 178 to 184>music/darkness.mp3" fadein 1

    $ renpy.pause (6.0, hard=True)

    stop two fadeout 1

    jump mom

label mom:

    scene black with longfade
    p "(I wanted to play a lot longer...)"
    play seven "music/mom.mp3" fadein 2
    scene e3park1 with longfade
    p "Wait up Mom!"
    scene e3park2 with longfade
    mom "Oh sorry [pname], I didn't realize I was going so fast!"
    mom "I'll always wait for you. Always."
    scene e3park3 with longfade
    p "How come we couldn't stay at the playground longer? We were only there for like ten minutes!"
    mom "Sorry sweetie, we have to get back home and see your sister's recital."
    p "Aw man, piano is soooo boring!"
    scene e3park4 with longfade
    mom "It's fun for your sister. So be good."
    mom "Someday she will be a very strong woman, so you need to protect her while she is weak."
    p "I'm going to be strong too!"
    scene e3park5 with longfade
    mom "I know sweetie. And you can do so much in the future!"
    mom "Just remember this. No matter how tough it gets, I have always had a plan to help you. Don't ever, ever, give up."
    p "Ok Mom. Who was that mom and girl you were talking to? That's girl's hair was like a fire!"
    scene e3park6 with longfade
    mom "Just an old friend sweetie...a really old friend."

    stop seven fadeout 3

    jump kanewakeup

label kanewakeup:

    scene black with longflash
    pp2 "[pname]! Time to go!"

    play seven "music/darkness.mp3" fadein 3

    scene e3kanewakeup1 with longfade
    pp2 "C'mon [pname], get your ass up! I'm not even officially working yet, but I have to drag you out of here early!"
    pp2 "You're a free man...well sort of, haha!"
    p "(...)"
    scene e3kanewakeup2 with longfade
    p "(Ugh...I wouldn't mind a little more sleep.)"
    pp2 "We're heading to Room 2, and then you'll be heading out of here."
    p "Ok."
    scene e3kanewakeup3 with longfade
    pp2 "Aren't you excited to start your new life as a guinea pig instead of a rat?"
    menu:
        "(Tell Sam sarcastically that you will miss her so much.) [SamamthaPath]":
            scene e3kanewakeup4 with mediumdissolve
            $ sam_p += 1
            p "No Sam, I'm actually so sad I won't have the benefit of your charm every day!"
            pp2 "Hah, keep your wits [pname], and you may actually survive the Karlsson bitches."
            p "One can hope."
            jump kanewakeuptwo
        "(Don't say anything at all.) [SubPath]":
            scene e3kanewakeup5 with mediumdissolve
            $ sub += 1
            p "...."
            pp2 "Oh [pname], are you literally always so scared to even say one word? I'm not buying you at all as the strong and silent type..."
            pp2 "The Karlssons will just eat you alive more quickly if you are always silent."
            jump kanewakeuptwo
        "(Answer with little enthusiasm and general indifference about the situation.)":
            scene e3kanewakeup6 with mediumdissolve
            p "Hmm, I guess so."
            pp2 "Oh, you really sound so excited [pname]. Honestly, I guess I can't blame you. But you can change your fate if you work at it."
            jump kanewakeuptwo
        "(Tell her how unhappy you are that you never got to have sex with her.) [SamamthaPath] [DomPath]":
            $ dom += 1
            $ sam_p += 1
            scene e3kanewakeup7 with mediumdissolve
            p "I'm actually quite disappointed that we never got to fuck!"
            pp2 "Oh [pname], yell at Elena. I would have had my way with you a long time ago."
            pp2 "But...you never know. Don't be surprised if you run into me again sooner than you think."
            jump kanewakeuptwo

label kanewakeuptwo:

    scene e3kanewakeup8 with longfade
    pp2 "Ah, your last goodbye for your cell. Will you miss it?"
    if k4:
        pp2 "Anyway, let's get going now! Someone is waiting for you."
        jump kanewakeupthree
    else:
        pp2 "Anyway, let's get going! I'm just dropping you off as Kitty will be getting you out of here."
        pp2 "I'm sure we will run into each other soon [pname]."
        jump kanewakeupthree

label kanewakeupthree:
    p "(Great. I bet they have one more surprise for me...)"

    stop seven fadeout 3

    jump cellone

label cellone:

    if k4:
        jump celltwo
    if k5 or k6:
        jump celltwodom

label celltwo:

    scene e3cell1 with longfade

    play seven "music/prop.mp3" fadein 3

    kk "Ah, hello there [pname]! Such a pleasure to see you again!"
    p "(Oh, what the hell is this...)"
    scene e3cell2 with mediumdissolve
    kk "We're here to celebrate your new promotion to K4!"
    kk "I just got promoted too!"
    p "To what?"
    pp2 "Kitty here has gotten a rare promotion, way beyond K scale. It's called Z1. She's even got a special ceremony later for it. Why she dressed up too."
    scene e3cell3 with mediumdissolve
    pp2 "And at that level, she can do anything she wants to a lowly pig like you. Even have you killed."
    kk "Oh [pname], don't worry, I'm a nice girl!"
    menu:
        "(I'm curious if Sam has an employee rank. I should ask her what it is.) [KittyPath]":
            $ sam_p -= 1
            $ kitty_p += 1
            scene e3cell3b with mediumdissolve
            p "And what about you Sam? What rank are you?"
            pp2 "That's none of your business [pname]!"
            scene e3cell3c with mediumdissolve
            kk "Sam is a well paid employee but she can never go too high with The Karlsson Group because she's too short, haha!"
            p "(They discriminate based on height? Why?)"
            kk "Oh don't pout Sam, you still have so much fun with your job. Way more than I have had so far."
            jump celltwotwo
        "(Do they expect me to fit in that cage? Maybe I should try and object to it.) [gr]\[KittyScale +1\]":
            $ kitty_p -= 1
            $ kitty_scale += 1
            scene e3cell3d with mediumdissolve
            p "Do...do you expect me to get in that cage? Why can't I just walk out of here?"
            kk "Oh [pname]y poo...don't worry about that yet! I want to help congratulate you to your new rank!"
            p "(Great...)"
            jump celltwotwo
        "(I should try and please Kitty in her new position of power. I'll agree with her that she is a nice girl and try to compliment her.) [red]\[KittyScale -2\]":
            $ kitty_scale -= 2
            scene e3cell3e with mediumdissolve
            p "Yes, I am sure you are a nice girl Kitty. I know you deserved your promotion and will do great with it."
            pp2 "Oh, what is that political speech level bullshit [pname]? Such a kiss ass, you think that will help you?"
            kk "Oh no Sam! It's ok [pname], go ahead and be sweet all you want!"
            jump celltwotwo

label celltwotwo:

    scene e3cell4 with mediumdissolve
    kk "You know [pname], I had to do so many stupid things to get from K4 to where I am now. So I actually know how you might be feeling right now."
    kk "But now, I feel like a little girl that just got the keys to all the toys I could ever want."
    scene e3cell5 with mediumdissolve
    kk "And you're my first toy. And...I want to play with you a little."
    pp2 "I hope you let me have some fun too Kitty!"
    kk "We'll see. But I think it's time for [pname] to play with me!"
    scene e3cell6 with mediumdissolve
    kk "You'll be a good toy, won't you [pname]? I don't want to have to shock you or anything."
    kk "Sam, bring him over here so he can greet me properly."
    scene e3cell7 with mediumdissolve
    pp2 "Of course...by the way, what should I call you? Miss Kuromiya? Miss Kitty?"
    kk "Miss Kuromiya is fine Sam...when toys are around especially. I won't use Kitty anymore though. My real first name is Katsumi."
    kk2 "So use that from now on amongst ourselves."
    scene e3cell8 with mediumdissolve
    kk2 "Now [pname], you have to show extreme respect for someone at my level. What do you think you should do first every time you see me?"
    kk2 "Don't worry, I won't punish you for a wrong answer since it's the first time for both of us!"
    p "(Err, yeah I'm sure any guess will be perfect here.)"

    stop seven fadeout 2

    menu:
        "(I think she probably wants to hear something like I should greet her as Mistress Katsumi. That seems like a safe answer.) [KittyPath]":
            $ kitty_p += 1
            scene e3cell8b with mediumdissolve
            p "I guess I should address you as Mistress Kitty, I mean Katsumi? Or Mistress Kuromiya?"
            kk2 "Oh, that's not a bad guess [pname]! But that's not what I want...at least first."
            jump celltwothree
        "(I shouldn't even try to answer. I should just ask her what she wants me to do as a greeting for her.) [red]\[KittyScale -2\]":
            $ kitty_scale -= 2
            scene e3cell8c with mediumdissolve
            p "Could I just ask what you want to do as a greeting for you?"
            kk2 "Oh, such a willing little toy! But I do want you to try and think too, it's no fun if you are too much of a puppy!"
            jump celltwothree
        "(I have no clue. I should just tell her I don't know what to do.) [red]\[KittyScale -1\]":
            $ kitty_p -= 1
            $ kitty_scale -= 1
            scene e3cell8d with mediumdissolve
            p "I don't have any idea what I should do."
            kk2 "Oh no [pname], I don't like you not even trying that hard. I expect you to try and always think of an answer to my questions."
            jump celltwothree

label celltwothree:
    scene e3cell9 with longdissolve

    play seven "music/jail.mp3" fadein 3

    kk2 "What I want you to do first every time you see me is to get on your knees, bow down and kiss my feet or shoes."
    kk2 "And right now, you're just a toy pet to me so you don't get to talk to me like a real human until you earn it."
    scene e3cell10 with mediumdissolve
    kk2 "You can answer a direct question, but otherwise you don't talk on your own initiative."
    pp2 "Oh, this is interesting! You thought a lot about this didn't you, haha!"
    kk2 "I had time to think about this for a few years Sam! I've been waiting for this..."
    scene e3cell11 with mediumdissolve
    kk2 "[pname], I also want your head bowed down when you respond to any direction from me unless I say otherwise."
    kk2 "If you are a good toy for me, we'll see how nice I can be to you later."
    scene e3cell12 with mediumdissolve
    kk2 "Now you can answer this next question, but remember your head! Do you understand everything I expect?"
    menu:
        "(No fucking around here. I better just answer perfectly how she wants and bow my head too.) [KittyPath] [red]\[KittyScale -1\]":
            $ kitty_scale -= 1
            scene e3cell12b with mediumdissolve
            p "Yes, Mistress Katsumi. I understand everything you said."
            kk2 "Very good [pname]! I'm so glad we are each others' first in our new roles!"
            jump celltwofour
        "(I need to try and stand up a little for myself! I should at least object a little and try and appeal to her being in my position before.) [gr]\[Punished\]":
            $ kitty_p -= 2
            $ brotherpunish = True
            scene e3cell12c with mediumdissolve
            p "I can't believe you want to treat me like a pet or toy or something. You used to be where I am, I would think you would be a little more understanding!"
            pp2 "Oh you screwed up [pname]!"
            scene e3cell12d with mediumdissolve
            kk2 "If a toy doesn't play well, it may have to be thrown away...or broken."
            scene e3cell12e with quickdissolve
            kk2 "But [pname], I do like you. So I'll give you another chance. Try again to answer my question, or I may have to shock you. And I may punish others you know too."
            p "([pname2]?)"
            menu:
                "(She's probably not going to change her mind, and I likely have nothing to gain but a shocking at this point. May as well submit for now.)":
                    scene e3cell12f with mediumdissolve
                    p "Ok Mistress Katsumi. I understand."
                    kk2 "That's better. Now we can have a little fun."
                    jump celltwofour
                "(She may punish me either way with a shock now. I need to try and object being a toy or pet and hope she might respect that long-term.) [gr]\[KittyScale +1\]":
                    scene e3cell12g with mediumdissolve
                    $ kitty_scale += 1
                    p "I...just don't think you should treat me like some kind of toy or pet or something."
                    kk2 "This toy is malfunctioning right now, and it's no fun! [pname], Body Pain Level 5. Kick him too Sam."
                    scene e3cell12h with longflash
                    p "(Oh jeez, I had almost forgotten the pain!)"
                    kk2 "Oh, now my toy looks like it's working better!"
                    scene e3cell12i with mediumdissolve
                    p "(Oof!)"
                    kk2 "But no more games now. You say I understand Mistress Katsumi and the pain stops."
                    scene e3cell12j with mediumdissolve
                    p "Ok! I understand Mistress Katsumi!"
                    kk2 "Good. Kane Body Pain Off. Now get up so we can play a little."
                    p "(Whew...)"
                    scene e3cell12k with longfade
                    p "(Maybe still better her than Sam but ugh...)"
                    kk2 "I'm so sorry it had to come to that [pname]! I just wanted to play nicely, but you acted like a big meanie. Now we can have some fun!"
                    jump celltwofour

label celltwofour:

    scene e3cell13 with longdissolve
    kk2 "Sam, this is being recorded, right? Where can [pname] and I stand to get a nice photo as first timers together?"
    pp2 "Oh...umm, the best angle is standing facing the viewing window, your back to the outside window here."
    scene e3cell14 with mediumdissolve
    kk2 "Perfect! Come on [pname], I want to make a cute collection of photos and videos of every toy I get to use, and you're my first!"
    kk2 "Oh, this is so fun!"
    scene e3cell15 with mediumdissolve
    kk2 "This is going to be the before picture! We can do an after one much, much later when I've played with you a lot..."
    scene e3cell16 with longfade
    kk2 "Say please!"
    p "(She's both weird and scary...)"
    scene e3cell17 with mediumdissolve
    kk2 "Now Sam, make a great still photo of this and also send me the recording of everything so I can start my collection!"
    kk2 "Thank you [pname], and I did notice you didn't smile, but that's ok! It's more enjoyable for me to see scared or sad faces anyway, haha!"
    scene e3cell18 with longfade
    kk2 "But back to my greeting. Time to greet me properly, Toy Number One!"
    kk2 "On the ground. And kiss your superior's feet like a good little toy."
    menu:
        "(Kiss her toes.)":
            scene e3cell18b with mediumdissolve
            kk2 "Excellent [pname], I'm so happy with you right now. Let me take off my shoe for you too."
            scene e3cell18c with longfade
            kk2 "Maybe you'd like being my foot licker more often?"
            pp2 "He probably loves it down there, haha!"
            scene e3cell18d with mediumdissolve
            kk2 "Get in there and make sure every little bit is clean and perfect."
            scene e3cell18dd with mediumdissolve
            kk2 "Yes...good."
            scene e3cell18e with mediumdissolve
            kk2 "Are you actually enjoying this too much? That's ok for now...if you are always a good toy for me and do everything I say."
            jump celltwofive
        "(Kiss her shoes.)":
            scene e3cell18b with mediumdissolve
            kk2 "Such a good toy [pname]...do you like my new shoes? Look at the little glitter skulls on my heel too, so cute!"
            scene e3cell18g with mediumdissolve
            kk2 "I want the bottom of my heels to always be as clean as possible, so I appreciate a good toy that can help me with that!"
            scene e3cell18h with mediumdissolve
            kk2 "Why don't you suck on my back heel to get it nice and clean, mmmhmm, hee hee!"
            pp2 "Katsumi, I mean Miss Kuromiya, I don't think he's enjoying that very much!"
            scene e3cell18i with mediumdissolve
            kk2 "Well, his job as a toy is my enjoyment, not his own! Now lick the bottom of my dirty shoe too."
            kk2 "I've noticed you never have shoes yourself [pname]! Sam has been a little meanie hasn't she?"
            scene e3cell18j with mediumdissolve
            kk2 "Now lie down flat on your back, I always wanted to try this!"
            pp2 "Oh, you have me so curious!"
            scene e3cell18k with longfade
            p "Ouch! I!...ugh..."
            kk2 "Oh, stop whining like a little baby toy. I've got a cute and petite body, you can handle me!"
            p "(yeah but so tall...)"
            scene e3cell18l with longfade
            kk2 "This is so fun Sam! As for you [pname], never forget that if you are my toy, you have to play very well to make me happy."
            p "(Is that even possible...)"
            kk2 "But I think we should move on now, that's enough."
            jump celltwofive

label celltwofive:

    scene e3cell19 with longfade
    kk2 "Sam, take his clothes off to prepare him for his new home."
    pp2 "With pleasure!"
    stop seven fadeout 3
    scene e3cell20 with longfade
    kk2 "Oh, not too bad [pname]. I'm going to have so many toys to choose from, but I don't think too many will easily outclass you."
    kk2 "Why, it's maybe close to full size! I wonder what specific thing might be getting you excited."
    scene e3cell21 with mediumdissolve
    kk2 "Hmm...I wish I could keep you for a while, but my new duties are quite important so I can't for now."
    kk2 "But I hope we can get together again later."

    if pissboy:
        jump pissboy
    else:
        jump celltwosix

label pissboy:

    play nine "music/testresults1.mp3" fadein 3

    scene e3piss1 with longfade
    kk2 "Now Sam, I heard [pname] did so poorly on his testing that he actually failed?"
    pp2 "Yes. He was so pathetic. Pat was really disappointed too!"
    scene e3piss2 with mediumdissolve
    kk2 "[pname], I guess you are so lucky Elena had a Get out of Jail free card for you!"
    kk2 "You must be a little unhappy about that Sam, maybe you could have had him all to yourself..."
    scene e3piss3 with mediumdissolve
    pp2 "Yes, Miss Kuromiya, but that's ok. I have another failure caged up for later."
    kk2 "Oh! I wish I could see that. I think I could learn so much from you."
    pp2 "You can always visit at any time! Almost no one could say no to you if you wanted to visit the jail for...research haha!"
    scene e3piss4 with mediumdissolve
    kk2 "Yes, I definitely will! But...we need to finish all of this, I'm embarrassed to say that I really have to use the bathroom!"
    pp2 "You know...you have a perfectly good toilet right here in this room."
    scene e3piss5 with mediumdissolve
    kk2 "What do you mean I have...oh! Sam, maybe I really want to hire you as my personal assistant! So helpful!"
    kk2 "Maybe we can talk later without this toy around."
    pp2 "I'd be open to that...but I do have a pretty fun job right now!"
    scene e3piss6 with longdissolve
    kk2 "[pname], get on your knees and then open your mouth nice and wide for me. You're going to be my toy toilet for me, haha!"
    p "(She's going to piss in my mouth?)"
    kk2 "You do want to please me don't you?"
    menu:
        "(I really do want to serve Katsumi the best I can and please her even as her toilet. I should just obey and tell her the truth.) [KittyPath] [red]\[KittyScale -2\]":
            $ kitty_scale -= 2
            $ kitty_p += 1
            scene e3piss7 with mediumdissolve
            p "Mistress Katsumi, I want to please you. I will do as you ask."
            kk2 "Wonderful my little toy! If you are this obedient and helpful, I can be such a sweet Mistress you know!"
            kk2 "Now on your knees and get ready!"

            stop nine fadeout 2

            jump pissboytwo
        "(I really don't want to get pissed on to please her, but it's probably smart for me to answer that I do because she's probably doing it anyway. I should answer accordingly.) [KittyPath]":
            $ kitty_p += 1
            scene e3piss8 with mediumdissolve
            p "Yes, I guess I want to please you."
            kk2 "That's Mistress Katsumi little toy!"
            p "Yes, I want to please you Mistress Katsumi."
            scene e3piss9 with mediumdissolve
            kk2 "You don't sound too convincing, but you are still being obedient. That's a start."
            kk2 "Now on your knees and get ready for me!"

            stop nine fadeout 2

            jump pissboytwo
        "(I'm just not going to answer, anything I say could make it worse.)":
            $ kitty_p -= 1
            scene e3piss10 with mediumdissolve
            p "(...)"
            kk2 "It doesn't make me happy when you don't answer my questions [pname]."
            kk2 "But you're going to do what I want anyway. So get on your knees and be ready for me."

            stop nine fadeout 2

            jump pissboytwo
        "(I should be honest and tell her I don't want to get pissed on. She might do it anyway, but you never know...)":
            scene e3piss11 with mediumdissolve
            p "I...I mean Mistress, I really don't want to have to swallow your piss."
            kk2 "I see...are you saying my piss is too disgusting for you?"
            p "I didn't mean it like that...I only meant..."
            scene e3piss12 with quickdissolve
            kk2 "...It's ok [pname], I always want you to share your honest feelings with me. Especially if you don't want me to do something to you."
            kk2 "If you want to beg for me not to do it, I'll always give you that chance. So go ahead. Beg."
            menu:
                "(It may work to beg, and even if it doesn't, maybe I can avoid something else I don't want later...) [red]\[KittyScale -1\]":
                    $ kitty_scale -= 1
                    scene e3piss13 with mediumdissolve
                    p "Please Mistress Katsumi, I beg of you not to use me as a human toilet. Please."
                    scene e3piss14 with mediumdissolve
                    kk2 "Oh my God...Sam, I've fantasized about being in this position for soooo long..."
                    pp2 "Are you going to let him off the hook?"
                    scene e3piss15 with mediumdissolve
                    kk2 "Nope! I do have to pee, haha! On your knees [pname]!"
                    jump pissboytwo
                "(Begging probably won't work. She might piss on me more often too if I make her upset...better just suck it up and allow this to happen.)":
                    scene e3piss16 with mediumdissolve
                    p "It's ok Mistress Katsumi...I'll...be your toilet."
                    scene e3piss17 with longdissolve
                    kk2 "Oh, you poor thing. You really don't want to do it...but you know you have to...awwwww."
                    kk2 "You poor poor baby."
                    scene e3piss18 with mediumdissolve
                    kk2 "On your knees. Get ready for me little toy..."

                    stop nine fadeout 2

                    jump pissboytwo

label pissboytwo:

    scene e3pissed0 with longfade

    play seven "music/lick.mp3"

    kk2 "Since it's my first recording, I think I want to be naked!"
    kk2 "Sam, can you put my dress away for now in the observation room? I need to keep it clean. I'll wait for you so you don't miss my fun!"
    pp2 "Of course!"
    scene e3pissed1 with longfade
    kk2 "Ah, I feel so lucky! You should feel lucky too [pname], I bet my pee tastes so sweet like me!"
    kk2 "And look at my body [pname]! Wouldn't you like to please me and get a taste of it someday?"
    pp2 "Maybe [pname] would have failed the testing on purpose anyway if he knew this would happen!"
    scene e3pissed2 with mediumdissolve
    kk2 "Oh, maybe you are right Sam."
    kk2 "And pleassseeee make sure that this is recorded later for me too, this is my first human toilet!"
    scene e3pissed3 with mediumdissolve
    pp2 "Of course Miss Kuromiya, I will make sure you have the best angles too."
    kk2 "Thank you Sam."
    scene e3pissed4 with mediumdissolve
    kk2 "Now look up into my eyes [pname]. I want you to think about what you are right now."
    kk2 "Just a little toilet. Exactly where you belong. You better lie down actually, you're kind of tall for kneeling!"
    scene e3pissed5 with mediumdissolve
    kk2 "Now open wide and enjoy!"
    scene e3pissed6 with mediumdissolve
    kk2 "Ahhh, there we go. Drink it all up."
    kk2 "It's so hard to pee standing like this! I need to squat down for you [pname]!"
    scene e3pissed7 with mediumdissolve
    kk2 "I think I'm going to have to order a human toilet for every room of my new home."
    kk2 "Push his head down Sam so I can get more comfortable too."
    scene e3pissed8 with longdissolve
    kk2 "There we go...keep swallowing..."
    kk2 "Can you tell I am holding back a little to make it last longer, hee hee!"
    scene e3pissed9 with mediumdissolve
    kk2 "Almost done...such a relief."
    scene e3pissed9b with mediumdissolve
    kk2 "How does it feel to be a toilet [pname]? I never actually had to do that for Elena."
    scene e3pissed10 with longdissolve
    kk2 "Ah, I'm so relieved! That felt so good."
    kk2 "Oops, I still have a little left right around my pussy."
    scene e3pissed11 with mediumdissolve
    kk2 "Why don't you lick up the rest like a good little toilet."
    menu:
        "(Lick everything up.) [KittyPath]":
            $ kitty_scale -= 1
            scene e3pissed11b with mediumdissolve
            kk2 "That's it toilet...good!"
            kk2 "I think I'm finally done now."
            jump pissboythree
        "(Hesitate to lick it up.)":
            $ kitty_p -= 1
            scene e3pissed11c with mediumdissolve
            p "I...I mean..."
            kk2 "I said lick it!"
            scene e3pissed11d with mediumdissolve
            kk2 "Get your toilet face in there [pname]!"
            kk2 "Hahaha, so pitiful! I think I'm finally done now."
            jump pissboythree

label pissboythree:

    scene e3pissed12 with longfade

    stop seven fadeout 3

    kk2 "Well, that was wonderful [pname]."
    kk2 "I feel so relieved and fresh. You'll always be my first toy and toilet. Sam, can you get my clothes now?"
    pp2 "Yes, Miss Kuromiya. Right away."
    jump cellthree

label celltwosix:

    scene e3face1 with longfade

    play nine "music/testresults1.mp3" fadein 3

    kk2 "Now Sam, on the bright side, he didn't actually fail the testing, right?"
    pp2 "Nope, he wasn't quite that pathetic. Just another run of the mill K4."
    scene e3face2 with mediumdissolve
    kk2 "Well [pname], don't feel too depressed about it, I was a K4 too once! In my case, I didn't test or anything. Elena just put me there."
    kk2 "Maybe you can get lucky and find a great Mistress that can help you like Elena helped me."
    scene e3face3 with mediumdissolve
    kk2 "Maybe...if you really please me, I could also help you. If you're a good little toy."
    menu:
        "(I should try and get on her good side as she might be able to help me. I can promise to serve her well. Maybe she likes that and helps me later.) [red]\[KittyScale -2\]":
            $ kitty_scale -= 2
            $ kitty_p += 1
            scene e3face4 with mediumdissolve
            p "I'd appreciate any help you can give me, Mistress Katsumi. I'm sure I can serve you well."
            pp2 "[pname]..."
            kk2 "I hope you can [pname]. And since you seem so willing, let me tell you what I did to escape K4."
            scene e3face5 with quickdissolve
            kk2 "I made sure Elena was happy. No matter what. And I learned as much as I could from her."
            kk2 "Do the same with any Mistress you serve. You might have a chance to move up if you have the right Mistress."
            jump celltwosixtwo
        "(Is she expecting me to say something to that? She said before she doesn't want me speaking. I don't know what to say...better just say thanks I guess.)":
            $ kitty_p -= 1
            scene e3face6 with mediumdissolve
            p "Err, thanks."
            kk2 "Very eloquent there [pname], and a man of many words. That's ok, most of the time I don't want to hear you speak anyway."
            jump celltwosixtwo
        "(Maybe she doesn't want me to totally kiss her ass but show some indepedence. I should answer that I want to serve her well because I think she can help me without sounding too weak.) [KittyPath]":
            $ kitty_scale += 1
            $ kitty_p += 2
            scene e3face7 with mediumdissolve
            p "Mistress Katsumi, I do think I want to serve you. But that's because I think you might help me too as Elena did for you."
            kk2 "Very good [pname]! Know your place, but also strive to gain something from me too. I can understand completely being in your shoes before."
            kk2 "We shall see if you are tough enough like I had to be..."
            jump celltwosixtwo

label celltwosixtwo:

    scene e3face8 with longfade
    kk2 "Now it's almost time for you to go [pname]. But I actually want to talk to Sam here a little before I go."
    pp2 "You do? What about?"
    scene e3face9 with mediumdissolve
    kk2 "About you. Your work. I just feel like we are kindred spirits."
    pp2 "What do you mean?"
    scene e3face10 with mediumdissolve
    kk2 "I just think...deep down, you and I are very similar with what we...really enjoy. But I don't have a lot of experience with certain things. And you do."
    pp2 "I think I understand Miss Kuromiya. And I agree. I think we are similar."
    scene e3face11 with mediumdissolve
    kk2 "Good. Now [pname], I'm a little tired. I want you to lean your head back over this cage so I can have a face seat to continue this conversation."
    p "(Wait...what...face seat...)"
    kk2 "[pname], I mean right now."

    stop nine fadeout 3

    menu:
        "(I better be very obedient right now. One face seat coming right up...) [KittyPath]":
            $ kitty_scale -= 1
            scene e3face12 with longfade
            p "As you wish, Mistress Katsumi."
            kk2 "Perfect [pname], thank you for being such a good toy!"
            jump kittyass
        "(I think I'm kind of stuck on this one, but maybe I can be a little passive aggressive in doing it.)":
            $ kitty_p -= 1
            scene e3face13 with mediumdissolve
            p "Whatever you say Mistress Katsumi."
            kk2 "I'm not very happy with your attitude there [pname], but I'll let it go since it's your first day."
            kk2 "But, you will suffer very badly from not just me but everyone else too if that doesn't change."
            jump kittyass

label kittyass:

    scene e3ass1 with longfade

    play seven "music/kittyass1.mp3" fadein 2

    kk2 "Ah, this looks very comfortable! Let me try and test the seat..."
    scene e3ass2 with mediumdissolve
    kk2 "Seems..."
    scene e3ass3 with quickdissolve
    kk2 "...Nice and soft! Wonderful!"
    p "(Ugh this metal bar...)"
    kk2 "Now don't yell into my ass or anything [pname], it might tickle me, haha!"
    scene e3ass4 with mediumdissolve
    kk2 "Now Sam, I do want to talk to you about your job here. Is it your goal to become the Warden of this prison?"
    pp2 "I wouldn't mind that job. It would pay very well and..."
    kk2 "...and you would get to have even more fun with the prisoners."
    scene e3ass5 with mediumdissolve
    pp2 "Yes. That would be a perk of course."
    kk2 "You know, I've had to come here a few times with Elena for client visits...I can imagine the appeal for you."
    scene e3ass6 with mediumdissolve
    pp2 "It would be a great job for me, and I see that as my best future right now."
    kk2 "Ok. I would like to at least open your mind to other possibilities. I may really want you working with me later."
    scene e3ass7 with mediumdissolve
    pp2 "Doing what?"
    kk2 "That answer will have to wait for now. Oh, this seat is so nice, you can just move so comfortably!"
    p "(Errghh...)"
    scene e3ass8 with mediumdissolve
    kk2 "But as you know, I have a special assignment with a nice little man first before I can try my idea. But I am pitching an idea to one of the Karlsson sisters soon."
    kk2 "I think you would really want to be a part of it. And I need very...sadistic assistants for it."
    scene e3ass9 with mediumdissolve
    pp2 "Sounds interesting! Since it needs sadistic people, I assume you are meeting with Juliette Karlsson about it?"
    kk2 "No. Elena told me Alessandra was the best one to talk to..."
    pp2 "Oh, well she would know better than us! So what's the idea?"
    scene e3ass10 with mediumdissolve
    kk2 "That will have to wait with Mr. Chair here. We can talk later after my assignment."
    pp2 "I look forward to it, and I'm very intrigued."
    kk2 "Good. Just keep an open mind. I think we could be great friends!"
    scene e3ass11 with longfade
    kk2 "Are you doing ok down there [pname]?"
    kk2 "I do appreciate you serving as my seat. Maybe you want to be a piece of human furniture in my new home?"
    scene e3ass12 with mediumdissolve
    kk2 "Ah, I can't take you. Your six month program. But I'm going to be sure to visit you a lot!"
    kk2 "After all, I'm going to be a customer of yours!"
    p "(Customer? What does that mean...)"
    scene e3ass13 with mediumdissolve
    kk2 "Sadly, it's time. I wouldn't have minded relaxing a bit longer."
    kk2 "I guess your seat duties are over [pname]. For now."

    stop seven fadeout 2

    jump cellthree


label celltwodom:

    scene e3celldom1 with longfade
    kk "Why hello there [pname], it's such a pleasure to see you again so soon!"

    play seven "music/prop.mp3" fadein 2

    p "(Oh what the hell is this...and [pname2].)"
    scene e3celldom2 with mediumdissolve
    if k5:
        kk "I'd like to congratulate you on acheiving a K5 rating from your testing. I hear that is very hard to do!"
        p "Err, thanks."
        jump celltwodomtwo
    else:
        kk "I'd like to congratulate you on getting a K6 rating! I've been told it's been years since anyone else got that result from the testing here!"
        kk "Maybe you have a huge future here at The Karlsson Group!"
        p "Err, thanks."
        jump celltwodomtwo

label celltwodomtwo:

    scene e3celldom3 with longdissolve
    p "(What does she expect me to...)"
    kk "Oh, don't fret about [pname2] yet."
    scene e3celldom3a with mediumdissolve
    kk "If he talks at all, he gets shocked by me! A lesson he already learned before you got here."
    kk "But let's talk about you first! How did you so do well on your testing?"
    menu:
        "(I think I should show strength here. I'll answer confidently that I was determined to excel at the testing and do whatever it took.) [gr]\[KittyScale +1\]":
            scene e3celldom3b with mediumdissolve
            $ kitty_scale += 1
            p "I knew I wanted to do the best I could, so I just did whatever I had to do to make sure I did well."
            kk "Such bravado and confidence. Good for you, but will you be tough enough when it counts? I started even lower than you and had to claw my way up."
            kk "You will need a lot more strength soon. I know what I am talking about, believe me."
            jump celltwodomthree
        "(Maybe it isn't good to sound too arrogant. I should be a little careful and be a little humble by saying I got lucky and made the best of things.)":
            scene e3celldom3c with mediumdissolve
            p "Well, I got a little lucky and just made the best of a tough situation and did well enough."
            kk "Hmmm, I don't think you got lucky personally. But a friendly tip [pname], don't be too humble."
            kk "You will also need a lot more than you showed here in the days ahead."
            jump celltwodomthree
        "(Maybe I can't trust anyone. I shouldn't volunteer anything I don't have to without knowing for sure it's to my advantage to do so. I'll just say it's my own business.) [gr]\[KittyScale +2\]":
            scene e3celldom3d with mediumdissolve
            $ kitty_scale += 2
            p "My own strategy to do the best I could is my own business. I would rather not share how I think without good reason."
            kk "That's fine [pname], it was just a friendly conversation starter! I get what you are saying completely."
            kk "And [pname], Elena could never read my thoughts either. But I wouldn't recommend ever lying or hiding so much that it upsets whoever is your superior."
            jump celltwodomthree

label celltwodomthree:

    scene e3celldom4 with longdissolve
    kk "So [pname], I actually just got a huge promotion myself! So I guess we are both celebrating some happy changes."
    p "What kind of promotion?"
    scene e3celldom5 with mediumdissolve
    kk "I have been promoted to a rank called Z1. It's the highest scale of the entire company. Even the Board members have Z ratings."
    menu:
        "(I should probably congratulate her. I don't think that makes me look too weak and she might genuinely appreciate it as she's no doubt excited about it.) [gr]\[KittyScale +1\]":
            scene e3celldom5b with mediumdissolve
            $ kitty_scale += 1
            p "That's great Kitty. I have no doubt that it was very hard to get this high in the company."
            if elena_mentor:
                p "You've come a long way from err...our first meeting in the limo."
                kk "Yes I have [pname], now if I want to play with you...I can just do it, hee hee!"
                jump celltwodomfour
            else:
                p "You must have come a long way."
                kk "It was a long road [pname]. But I hope to see you do well too."
                jump celltwodomfour
        "(Maybe I should show some ambition right away. I should compliment her but also say that I intend to join her at that lofty scale too.) [gr]\[KittyScale +1\]":
            scene e3celldom5c with mediumdissolve
            $ kitty_scale += 1
            p "That's great Kitty. I intend to join you there too down the road."
            if elena_mentor:
                kk "Oh, did one blowjob from me make your balls grow too? Very ballsy to just come right out and say that!"
                kk "But I really will be curious how you fare with everything."
                jump celltwodomfour
            else:
                kk "Well, you just came right out and said it didn't you?"
                kk "Just remember to back it up with action. I am really curious how you will fare with everything."
                jump celltwodomfour
        "(I should always try and take any opportunity to gather information to my advantage. I'll ask how she got promoted and what the rank means.) [VeronicaPath]":
            $ elena_meeting = True
            scene e3celldom5d with mediumdissolve
            p "So Kitty, how did you get promoted? And what are your actual duties at your new rank?"
            kk "Oh, good question [pname]. I think that's the first thing I would have asked too."
            scene e3celldom5e with mediumdissolve
            $ veronica_p += 1
            kk "At least two other Z ranked employees must nominate you for the possible promotion. I was nominated by Elena, Alessandra, and Veronica."
            p "(Very useful fact. Perhaps those three are allies.)"
            kk "But I can't really share any specifics about my position. It's beyond your clearance anyway [pname]."
            jump celltwodomfour

label celltwodomfour:

    scene e3celldom6 with longdissolve

    stop seven fadeout 3

    kk "Oh [pname], a few more quick things while I remember. First of all, I am now able to stop using Elena's nickname for me."
    p "So what should I call you?"
    scene e3celldom7 with mediumdissolve

    play seven "music/jail.mp3" fadein 3

    kk "My real name is Katsumi Kuromiya. But I think we are friends right now, so you can just call me Katsumi!"
    p "Ok, Katsumi it is."
    scene e3celldom8 with mediumdissolve
    kk2 "Later today, I have a special ceremony to be promoted. I have to deck out in this white dress for some reason too."
    kk2 "But enough of that, we have other things to do."
    scene e3celldom9 with mediumdissolve
    kk2 "[pname], we do have to transport you out of jail here and to your rehabilitation location. We will be traveling by plane and I'm here to escort you initially."
    kk2 "It should be a nice little trip, but don't get too comfortable. You did impress, but you are still a lowly prisoner with a long way to go."
    scene e3celldom10 with mediumdissolve
    kk2 "As for your poor silent friend [pname2] here, he didn't quite make the cut like you did on testing. As you probably know, he's just a K4."
    kk2 "So he has to be transported in this lovely little stroller here."
    p "(damn...this sucks for him...)"
    scene e3celldom11 with mediumdissolve
    kk2 "Don't ever forget [pname], even one little rank can be a world of difference for you. And one bad mistake can cost you."
    kk2 "But as for now, I just want to have a big strong man like you help me push your little friend here in his baby stroller, hee hee!"
    scene e3celldom12 with mediumdissolve
    kk2 "But before that, why can't I have a little fun?"
    p "(I knew something was coming...)"
    scene e3celldom13 with mediumdissolve
    kk2 "[pname], could you be a dear and grab a little toy I brought under the err blanket in [pname2]'s stroller?"
    p "Ok."
    scene e3celldom14 with mediumdissolve
    p "(What does she have in mind?)"
    scene e3celldom15 with longdissolve
    p "(Oh...)"
    kk2 "Wonderful, you found it [pname]! Can you help me by putting it on him for me?"
    menu:
        "(It might not help, but maybe I should try and object as to whether this is necessary. He's apparently already going to be caged after all.) [FriendPath] [DominquePath]":
            $ friend += 1
            $ dmeet += 1
            $ kitty_scale -= 1
            scene e3celldom15b with mediumdissolve
            p "Is this really necessary to do this to him? He's already going to be caged, and I am sure you can also shock him too any time you want."
            kk2 "Oh, are you worried about your little friend? That's so sweet."
            scene e3celldom15c with mediumdissolve
            kk2 "But...I want it on him. Don't fret [pname], I'm not going to beat him or something right here in this room."
            kk2 "I just want to see it on him. And [pname], I wouldn't recommend defying someone in my position on something this small."
            p "(Fine...)"
            jump celltwodomfive
        "(I don't think it's worth it to defy her on something like this, and it may make it much worse for [pname2] too. Probably better to say nothing for his sake.) [DominquePath]":
            $ dmeet += 1
            scene e3celldom15d with mediumdissolve
            p "Alright."
            kk2 "So cooperative [pname]! I'm very happy about that...and don't forget, you are still my primary candidate to deflower me. Pleasing me might please you later."
            jump celltwodomfive
        "(I'm not sticking my neck out on the line for [pname2]. Friendship only goes far, and better him than me.) [JuliettePath]":
            $ friend -= 1
            $ jmeet += 1
            scene e3celldom15e with mediumdissolve
            p "Sure thing Katsumi."
            kk2 "I'm so pleased with your cooperation [pname]. Maybe you really will get to deflower me if you keep making me happy."
            jump celltwodomfive

label celltwodomfive:

    scene e3celldom16 with longfade
    kk2 "Oh [pname], [pname2] looks so lovely! Now I can take my photo!"
    p "Wait, what?"
    scene e3celldom17 with mediumdissolve
    kk2 "Now that I have the opportunity, I want to make a cute collection of photos and videos of all my toys...and other things I do over time."
    kk2 "So this will be [pname2]'s before picture as part of my collection."
    p "(Before picture?)"
    scene e3celldom18 with mediumdissolve
    kk2 "This is so fun! You just wait there on the side [pname], but don't block the shot. We have to face the viewing window for the best angle."
    p "Sure..."
    scene e3celldom19 with longfade
    kk2 "Say please! Oops, you can't, poor baby, haha!"
    pbf "(...)"
    scene e3celldom20 with mediumdissolve
    kk2 "Let's get him in his baby stroller now [pname]! I've just unlocked his chains for you."
    p "If you say so."
    scene e3celldom21 with mediumdissolve
    p "(Ok...here we go...)"
    menu:
        "(I should try and give [pname2] a word of encouragement as I move him. He probably needs the moral support but I better be subtle and quiet about it.) [FriendPath] [DominquePath]":
            $ friend += 1
            $ dmeet += 1
            $ kitty_p -= 1
            scene e3celldom22 with mediumdissolve
            p "Hang in there man, I know it's got to be tough. Just hang in there."
            kk2 "[pname], it's not polite to try and do that right in front of me."
            p "(Shit.)"
            jump celltwodomsix
        "(I better just keep my mouth shut and just move [pname2] efficiently.) [KittyPath]":
            scene e3celldom23 with mediumdissolve
            kk2 "Thank you so much for helping me with this [pname]!"
            p "Sure."
            jump celltwodomsix

label celltwodomsix:

    scene e3celldom24 with longfade
    kk2 "Oh, he looks so adorable doesn't he?"
    kk2 "[pname2], I think you should have done a little better on testing! Too bad!"
    scene e3celldom25 with mediumdissolve
    kk2 "You're going to have to ride in the belly of the plane but I'm sure it's not too cold, haha!"
    kk2 "I'll be thinking of you while I relax above you."
    scene e3celldom26 with mediumdissolve
    kk2 "And you [pname], you've earned the right to at least ride in the plane normally."
    if kitty_p >= 1:
        scene e3celldom27 with mediumdissolve
        kk2 "And I haven't forgotten how well you beat on Samantha's ass. That greatly impressed me and also turned me on."
        kk2 "So I think we are going to be very good friends [pname], but you still need to prove yourself in this program."
        jump celltwodomseven
    else:
        scene e3celldom28 with mediumdissolve
        kk2 "I think you're hot and interesting [pname], but I'm still not sure what you are all about yet."
        kk2 "I'm now in a position of tremendous power, but I also have a great deal of pressure to prove myself. Like you have to prove yourself with your own program."
        jump celltwodomseven

label celltwodomseven:

    scene e3celldom29 with longdissolve
    kk2 "But your poor friend [pname2] is probably already doomed. Don't sacrifice yourself for him [pname]."
    scene e3celldom30 with mediumdissolve
    kk2 "Sooner or later, you will have to decide what you are willing to do to survive and even thrive. I had to do the same you know."
    p "(I wonder what she had to endure...)"
    scene e3celldom31 with mediumdissolve
    kk2 "But enough of that, let's get going! Your paradise awaits!"
    scene e3celldom32 with longfade

    stop seven fadeout 3

    kk2 "It's a long flight, but luckily for me, I have a lot of things I can do, haha!"
    jump jet

label jet:

    scene e3jet1 with longfade
    kk2 "Well, I think we can move around now, let me show you a little of this private plane!"
    kk2 "You may be assigned here in the future for whatever reason, so I would take this chance to become familiar with the airplane's rooms and layout."
    scene e3jet2 with longfade

    play seven "music/dominiqueintro.mp3" fadein 3

    kk2 "So this plane is used by Dominique Karlsson primarily, but she sometimes lends it out like right now. It's incredibly stable in the air, and quite comfortable for sleeping and relaxing."
    kk2 "It has two decks, some normal seating and lounge areas, a sleeping cabin area with elongated chairbeds, two conference rooms, three bedrooms, and one penthouse suite."
    scene e3jet3 with mediumdissolve
    kk2 "Employees can use the bottom level here while the upper deck is for top level executives only. Pretty nice though, isn't it?"
    p "Yes. It has a very spacious interior for a plane, and it looks great."
    scene e3jet4 with mediumdissolve
    kk2 "Do those shoes fit you ok? I know they aren't too fashionable, but it's all we had available. I bet it's been a long time since you even wore shoes, hasn't it?"
    p "Too long."
    kk2 "Well, keep doing well and nicer things will be possible for you."
    scene e3jet5 with mediumdissolve
    p "Is anyone else even on the plane right now?"
    kk2 "Of course [pname]! The pilots have to fly the plane! But we are the only passengers right now in here."
    kk2 "I think there might be one staff here, plus your fellow prisoners. This was a special flight just for us. But let's keep moving."
    scene e3jet6 with longdissolve
    kk2 "About the other prisoners...you're the only one from the prison who didn't test at K4, so all the rest are down below in the cargo hold."
    kk2 "Even with you prisoners, there are haves and have nots right away. Don't fall into the have nots [pname]."
    scene e3jet7 with mediumdissolve
    kk2 "Moving on up...the first room on the second floor will be a little private bar for executive level employees only."
    kk2 "It even has a little DJ booth for music, and once in a while very small shows are done up there."
    scene e3jet8 with longdissolve
    kk2 "Speaking of prisoners, do you want to hear one right now? I have a live audio feed of one of them."
    p "What? What do you mean?"
    scene e3jet9 with mediumdissolve
    kk2 "Well, I put a little recorder in one of the prisoners' boxes, so we can hear him clearly from his little transport in the cargo hold."
    p "Who? [pname2]? And why even have a live feed available of it?"
    kk2 "Oh no, not [pname2]. The little guy, Zach? He's such a whiner and I bet he's so scared, haha! So do you want to hear a live audio feed?"
    menu:
        "(Is she serious? I don't need to hear some prisoner whining down there, I'm no sadist or anything. Screw that.) [GoodPath] [DominquePath]":
            scene e3jet9b with mediumdissolve
            $ dmeet += 1
            $ good += 3
            p "No thanks. I don't need to hear that."
            kk2 "That's fine [pname]. That kind of thing is not for everyone. But I would suggest you carefully pick your allies later."
            jump jet2
        "(I really don't want to hear this, but I think Kitty wants to, so I should just pretend to want to as well.) [VeronicaPath]":
            scene e3jet9c with mediumdissolve
            $ vmeet += 2
            $ good += 1
            p "Sure, I guess I'm a little curious to hear what's going on down there."
            kk2 "Ok [pname], hold on...we have to go to Juliette's study room so I can turn it on..."
            scene e3jet9d with longfade
            kk2 "And...there we go!"
            zach "noooooo....*sniff*....please....where...where are....help"
            p "(That's...Katsumi is damn cruel...)"
            scene e3jet9e with mediumdissolve
            kk2 "Poor thing. He's still got a few more hours to go too, haha! But that's enough of that audio for now."
            jump jet2
        "(I never liked Zach anyway. I should enjoy what little chances I have to feel superior and maybe that impresses Kitty too.) [JuliettePath]":
            $ jmeet += 1
            scene e3jet9f with mediumdissolve
            p "Sure, let's hear it!"
            kk2 "Oh, you actually sound interested. Ok, we have to go Juliette's study room to turn it on!"
            scene e3jet9g with longfade
            kk2 "Here we go..."
            zach "nooooo....*sniff*....please....where....where are....where....please....help..."
            kk2 "Awww, the poor thing is crying. He still a few hours to go too...such a shame. But I'll turn off the audio for now."
            scene e3jet9h with mediumdissolve
            kk2 "Why you little sick bastard [pname]. I suspect you were enjoying his fear and suffering."
            kk2 "Don't try and trick me either with a fake answer. This is a very serious question. Were you in fact enjoying it?"
            menu:
                "(Hmm, I better not try and fake an answer here. I should tell her the truth that after hearing it, I didn't like it at all.) [DominquePath] [GoodPath]":
                    scene e3jet9i with mediumdissolve
                    $ dmeet += 1
                    $ good += 3
                    p "Honestly, I didn't like hearing it at all. It kind of bothered me, and I'm not sure why you would play it."
                    kk2 "Thank you for being honest [pname]. I do believe you."
                    jump jet2
                "(Hmm, I better not try and lie here. I should tell her the truth that I didn't really care either way.) [VeronicaPath]":
                    scene e3jet9j with mediumdissolve
                    $ vmeet += 2
                    p "To be honest, I wasn't bothered a lot by it, but it didn't do anything for me either."
                    kk2 "Hmm, I actually believe you. I think a few other times you might have been giving me lip service, but not here. I actually appreciate it."
                    jump jet2
                "(I better not lie here. I am sadistically enjoying it a little. I also suspect Kitty does too, so I'll just risk it and tell her my feelings.) [JuliettePath] [EvilPath]":
                    scene e3jet9k with mediumdissolve
                    $ jmeet += 3
                    $ kittyoffer = True
                    $ evil += 3
                    p "I can't lie...I guess I am enjoying it a little. Maybe I'm not such a nice guy."
                    kk2 "Hmm, I actually believe you."
                    scene e3jet9l with mediumdissolve
                    kk2 "And don't feel bad [pname], you should be embracing your darker desires."
                    scene e3jet9m with mediumdissolve
                    kk2 "That can lead to a lot more rewards...and fun. After all, what kind of people do you think mostly run The Karlsson Group?"
                    kk2 "And I certainly can give you chances myself to...indulge. If you have what it takes."
                    scene e3jet9n with mediumdissolve
                    kk2 "But for now, let's turn our attention to other things."
                    jump jet2

label jet2:

    scene e3jet10 with longfade
    kk2 "A few last things on the upper deck...a private little dining area for the executives."
    kk2 "Serving executives in this room could definitely be a future duty for you as part of your program. I know they have used prisoners here before."
    scene e3jet11 with longdissolve
    kk2 "A nice little private gym for the penthouse room only. Just a treadmill, cycle, and a mat there."
    kk2 "Of course, the penthouse bedroom I have to keep off limits for the likes of you."
    scene e3jet12 with longdissolve
    kk2 "A cool little jacuzzi as well for the penthouse. I bet you'd like to have some fun in there while flying almost 40,000 feet in the air."
    p "Looks relaxing...and yes, fun too."
    kk2 "Alright, let's go back downstairs, that's enough for now."
    scene e3jet13 with longfade
    kk2 "Now, we have quite a bit of time before we arrive, so I need to check on a few things."
    kk2 "But don't get too used to being in a luxury plane, this will not be your typical experience with the program. At least not yet."
    p "I understand."
    scene e3jet14 with mediumdissolve
    kk2 "Excellent. Just remember what I showed you, because if you are lucky, you might get to work here."

    stop seven fadeout 3

    kk2 "Now just relax a bit and let a little bit of this blue vibe chill you out. I'll be back soon."
    p "(Ok, guess I'm actually free on my own a bit...)"
    scene e3jet15 with longfade
    p "(This is pretty nice. But maybe lucky too. To think that possibly just one missed question or screw up, and I'm stuck in a cargo hold...)"
    scene e3jet16 with mediumdissolve
    p "(But I'm exhausted. Months in jail and even this couch looks so comfortable. It wouldn't hurt to just relax a little...yeah...)"
    jump junko

label junko:

    scene e3junko1 with longfade
    jk "Mr. [pname_f], I'm here to show you your room."
    jk "Mr. [pname_f]?"
    scene e3junko2 with mediumdissolve

    play seven "music/junkointro.mp3" fadein 3

    p "Wha...oh, hello there. Who are you?"
    jk "My name is Junko. I work for Dominque Karlsson, and she wanted to make sure you were given a nice room on your flight since you did so well on your testing."
    p "Thank you, I really appreciate it. Do I need to wait for Kitty at all?"
    scene e3junko3 with mediumdissolve
    jk "No, sir. She's a little indisposed for now, she will speak to you later. Please follow me and we can get you settled."
    p "Sure thing."
    scene e3junko4 with longfade
    jk "You can rest here during the remainder of your flight. It's quite comfortable and spacious."
    p "It really is quite nice. I appreciate Dominique arranging such a nice room."
    scene e3junko5 with mediumdissolve
    jk "I would suggest you get used to calling her my Lady or Lady Dominique if you do see her in person. It would be wise on your part...at least until you gain her trust."
    p "Ok, I'll keep that in mind."
    scene e3junko6 with mediumdissolve
    jk "Unfortunately, you do not have online access to news, games, or other...entertainment in your room."
    jk "She did realize it has been months since you have had any such access, but this is a privilege only afforded to program participants ranked K7 or higher."
    if k6:
        p "(Hmm, only one more rank on that one, good to know each rank gives more privileges and online access is a nice perk for sure.)"
        jump junko2
    else:
        p "(Hmm, just a few ranks away, but good to know that each higher rank gives more privileges. Online access would be nice.)"
        jump junko2

label junko2:

    scene e3junko7 with mediumdissolve
    jk "Now, as a reward for your test results, Lady Dominique has also authorized me to help you relax..."
    scene e3junko8 with longdissolve
    jk "...with a nice massage."
    jk "So you learn and understand the rewards of good performance...but remember that everything you do is always under evaluation too..."
    scene e3junko9 with mediumdissolve
    jk "I think I can make you feel better."
    jk "It must have been very tough being stuck in prison..."

    stop seven fadeout 3

    menu:
        "(I really could use some release, but her comment about evaluation makes me pause. Maybe I shouldn't take advantage of her, and just get to know her first by talking.) [DominquePath] \[JunkoRomance\]":
            $ jromanceopen = True
            $ dmeet += 3
            if kittyoffer:
                $ kittyoffer = False
            scene e3junko10 with mediumdissolve

            play seven "music/junkoromance2.mp3" fadein 2

            p "I really am tempted and appreciate the offer Junko, but maybe I'd like to relax by just talking first."
            scene e3junko11 with mediumdissolve
            jk "I'm honestly shocked at your answer. I did not expect that."
            scene e3junko12 with mediumdissolve
            jk "What...what would you like to talk about?"
            p "I'd just like to know anything I can about what to expect, and maybe a little about yourself and working with Dominique."
            scene e3junko13 with mediumdissolve
            jk "I'm afraid I can't help you about your program much, but I know it's not just for rehabiliation. You need to be careful."
            p "What do you mean by that?"
            jk "I haven't seen it much personally, but I know it's entertainment for rich people and it can be dangerous. I don't really know any more than that."
            scene e3junko14 with mediumdissolve
            p "And what about yourself? How did you end up working for Dominique? What is she like?"
            jk "Like most, I had no real chance to go to school and started working as a maid, and eventually Dominique found and hired me."
            scene e3junko15 with mediumdissolve
            jk "Lady Dominique can be a bit hard on me at times, but I know I am lucky to serve her instead of the other Karlsson sisters."
            jk "She does have a taste for women as well as men, so sometimes she...enjoys me. But it could be so much worse so I don't complain too much."
            p "I see. What do you know about the other sisters? Err, you can cover yourself you know."
            scene e3junko16 with mediumdissolve
            jk "Oh, thank you! I have met them only a few times. Veronica seems very intelligent but cold and Juliette I have heard is quite cruel."
            jk "Alessandra was the nicest sister to me, but I think she had her own motives for me. I think my Lady protected me from her."
            p "Ok. I read earlier on a report that Dominique might be a strong person to take over the whole company?"
            scene e3junko17 with mediumdissolve
            jk "I don't know about such things. I only know that my Lady is not perfect, but she is mostly a good person. She just doesn't understand basic life for most people."
            p "I can believe that if she grew up super rich, and without any exposure to real people struggling day to day."
            scene e3junko18 with mediumdissolve
            jk "I...I am glad you didn't just take advantage of me, and I like talking with you."
            jk "Can I ask you something?"
            p "Sure, what is it?"
            scene e3junko19 with mediumdissolve
            jk "I know this might sound strange, but can I just get a hug and...maybe...we can just lie down and rest on the bed for a bit?"
            jk "It's been so long since I have just been able to feel close to anyone even for a moment...I'd just like some real human contact...I understand if that's too much to ask."
            menu:
                "(I think I can give her a hug at least, but it's a bit much to ask to rest together on the bed.) [red]\[JunkoRomance\]":
                    scene e3junko19b with mediumdissolve
                    $ jromanceopen = False
                    $ jfriendopen = True
                    p "Sure, happy to hug you but maybe it's a bit much to lie down together."
                    jk "That's ok, I understand that's asking a lot."
                    scene e3junko19c with mediumdissolve
                    jk "Thank you for doing this. I really hope everything works out well for you."
                    p "(So do I...so do I...)"

                    stop seven fadeout 2

                    jump vapmeeting
                "(It sounds like she is really lonely and deprived, without a lot of happiness in life. I'd like to make her feel good even for a little bit, so I'll do what she asks.)":
                    scene e3junko19d with mediumdissolve
                    p "Sure, happy to do all that for you. I actually am really glad I met you here. Maybe the only nice woman I have met in this crazy Karlsson world."
                    jk "Thank you. I'm glad too."
                    scene e3junko19c with mediumdissolve
                    p "(Wow, she smells so good. This is nice...)"
                    jk "Come on [pname], let's lie down just for a little bit..."
                    scene e3junko19e with longfade
                    p "(Woah, she just came right on top of me...her body is actually shaking a little...)"
                    jk "Thank you [pname], I'm so tired, I'm just going to rest a little...just rest..."
                    scene e3junko19f with mediumdissolve
                    p "(Never would have guessed waking up that my day would be like this so far...)"

                    stop seven fadeout 2

                    jump vapmeeting
        "(Maybe I shouldn't just take advantage of her, but I really could use a massage. I think that is a reasonable thing to receive and maybe it's bad for her if I refuse.) [gr]\[JunkoFriend\]":
            scene e3junko20 with mediumdissolve
            $ jfriendopen = True
            p "I honestly could really use a massage. My body hurts a lot from sleeping on a hard mattress nightly for months."
            jk "Of course [pname], I'm actually happy to help you feel better that way."
            p "Thanks."
            scene e3junko21 with mediumdissolve

            play seven "music/massage2.mp3" fadein 2

            jk "Why don't you take off your shirt and shoes and lie down on your back first?"
            p "Ok, will do."
            scene e3junko22 with longfade
            jk "Just try and relax, I'll see if I can make you feel better..."
            jk "I can't comfortably massage you in this tight dress."
            p "(Oh...)"
            scene e3junko23 with longfade
            jk "There we go. Hmm, your body is incredibly tense. You really do need a massage."
            p "Yeah, I guess so."
            scene e3junko24 with mediumdissolve
            p "Do you mind if I ask you a few things, or will it distract you from what you are doing?"
            jk "No, I don't mind. What do you want to ask me?"
            p "(Wow, she is so good at this...I feel so relaxed...)"
            scene e3junko25 with mediumdissolve
            p "Do you know anything about this rehabilitation program I am a part of now?"
            jk "I'm afraid I don't know that much, but I do know it's not just about rehabilitation. You need to be careful."
            scene e3junko26 with mediumdissolve
            p "What do you mean by that?"
            jk "I don't know a lot more, but I know it involves entertainment for rich people and can be dangerous."
            p "How about you? How did you end up working for Dominique?"
            scene e3junko27 with mediumdissolve
            jk "Like most, I had no chance to go to school, so I found work as a maid and eventually my Lady found me."
            jk "Why don't you turn over now and lie down on your back."
            scene e3junko28 with longfade
            p "(Oh my...she's...)"
            jk "My Lady treats me well, but she does...enjoy me sometimes. But it could be a lot worse for me, so I don't complain too much."
            jk "So many can't even find work and just starve and struggle to survive, so I know I am a little lucky."
            p "I understand. It's harsh out there."
            scene e3junko29 with mediumdissolve
            jk "I do like talking to you. I never get to talk to anyone and you have been very nice to me."
            scene e3junko30b with mediumdissolve
            jk "You know, I'm going to take off your pants and give you a special massage."
            p "Oh, you..."
            jk "Shhh...it's ok. I don't mind with you. Just relax and let go of your troubles for a little while..."
            scene e3junko31 with longfade
            p "(Oh wow.)"
            jk "I hope you can do well in the program, a few men have done very well from what I hear."
            scene e3junko32 with mediumdissolve
            jk "I do think some of the girls will like you. You're pretty nice down here."
            jk "But be careful. A few of the women you will meet are truly wicked."
            scene e3junko33 with mediumdissolve
            p "(Her hands are like magic...) Like who?"
            jk "My Lady's sisters are in general quite cruel."
            scene e3junko34 with mediumdissolve
            jk "And I know they like to hire sadistic women as employees for this program. I am sure you met some at the jail too."
            p "Yes, I definitely did."
            scene e3junko35 with longdissolve
            jk "Hmm, are you almost ready to finish here?"
            p "Yes, I am pretty close."
            jk "Good. I'll give you a little extra for being so nice to me."
            scene e3junko36 with mediumdissolve
            p "(Oh yes! Good girl...)"
            scene e3junko37 with mediumdissolve
            p "(So good...)"
            scene e3junko38 with mediumflash
            p "(Oh...I'm going to!)"
            scene e3junko39 with mediumflash
            p "(Yeeess!)"
            scene e3junko40 with longfade
            jk "I hope I helped you relax [pname]. I did enjoy talking with you a lot."
            p "I am very relaxed. I enjoyed talking too. (I definitely could get used to that...)"
            scene e3junko41 with mediumdissolve
            jk "I do suggest you get some rest. I don't think it will be quite this nice for you when you arrive."
            p "I understand, and thanks."

            stop seven fadeout 2

            jump vapmeeting

label cellthree:

    scene e3leave1 with longfade

    play seven "music/prop.mp3" fadein 3

    kk2 "That was great [pname]."
    kk2 "But I've had enough fun with you. It's time to go now."
    kk2 "Sam, under [pname]'s...umm blanket in his cage is a special little gift for him."
    scene e3leave2 with mediumdissolve
    pp2 "Let's see what's here!"
    scene e3leave3 with longdissolve
    pp2 "Oh, a gag for his mouth, so smart! No one has to hear [pname] crying or whining when we move him."
    scene e3leave3b with mediumdissolve
    kk2 "Let's put it on and get him ready to move."
    pp2 "With pleasure!"
    scene e3leave4 with longfade
    kk2 "Oh, so cute [pname]!"
    kk2 "Maybe now you regret not doing a little better during your testing? Or maybe you love this?"
    scene e3leave5 with longdissolve
    kk2 "Now get inside of the cage and we'll get you to your new home very soon!"
    p "(...home...just another cage I bet...)"
    scene e3leave6 with longfade
    kk2 "It is a little tight, but I'm sure you can manage [pname]! What do you think Sam?"
    pp2 "I think the cage should be much smaller."
    scene e3leave7 with mediumdissolve
    kk2 "Oh Sam, I really do like you! I am looking forward to talking to you again soon."
    kk2 "See how nice we are though [pname]? You can stick your head out the top, like...maybe a dog sticking his head out of the car window."
    scene e3leave8 with mediumdissolve
    kk2 "Don't worry [pname], the gag is coming off right after I have to leave you. I'll even have Sam put your clothes on you again so you don't freeze in the plane."
    kk2 "I just wanted to talk to you a second while you can't respond to me."
    scene e3leave9 with mediumdissolve
    kk2 "You might get a little upset at what I share after all."
    pp2 "Oh, are you going to?"

    stop seven fadeout 3

    kk2 "Yes, Sam. Now I want you absolutely silent so [pname] and I can have a quality conversation here."
    scene e3leave10 with longfade

    play five "music/death1.mp3" fadein 2

    kk2 "Now Sam wasn't allowed to share this, but I can. I met the most wonderful little man yesterday."
    kk2 "His name was [pname4]."
    scene e3leave11 with mediumdissolve
    p "(What the fuck?! It has to be him...shit...[pname4]?!)"
    kk2 "Yes, he's so weak, small, and scared. He so badly needs help from someone. Anyone."
    scene e3leave12 with mediumdissolve
    kk2 "And just maybe he might come to trust and rely on a sweet girl like me."
    p "(Oh no, what is she going to do...and waiting until I am stuck and speechless too...I have to...!)"
    kk2 "I can help him feel comfortable. Safe. Maybe even loved."
    scene e3leave13 with mediumdissolve
    kk2 "But...the best part is trying to figure out how I'm going to stomp on his poor little heart."
    kk2 "Mmm, I'm getting so wet thinking about his sad little face when I betray him."
    scene e3leave14 with mediumdissolve
    kk2 "Can't you just imagine his crushed face? Suffering so much physical pain constantly, and then adding this too...just when he was feeling a little hope."
    kk2 "It might be enough to just completely kill him inside. How wonderfully delicious..."
    scene e3leave15 with longdissolve
    p "(Kitty, damn you...)"
    kk2 "I learned very well from Elena that you don't need any physical violence to be cruel."
    kk2 "Aren't I a good student?"
    scene e3leave16 with mediumdissolve
    kk2 "I just wanted to tell you this so you can worry about it while you struggle with your own problems!"
    scene e3leave17 with longfade

    stop five fadeout 2

    kk2 "Time to go [pname]. You were a wonderful first for me. But I bet I have way more fun with my second."
    kk2 "Sam, take him away. I'm done with this toy."
    jump cargohold

label cargohold:

    scene e3jet1 with longfade
    p "(I wonder if I damaged my ears from that brutal takeoff, they still hurt from the sound.)"
    scene e3cargo1 with longfade
    p "(Hmm...we've been flying a few hours. We were facing north when I saw the plane on the runway. Based on the turns, I think we are heading east.)"
    p "(If so, we're over the ocean right now.)"
    scene e3cargo2 with longdissolve
    if samsadist:
        p "(I guess I better be glad I wasn't put in this box by Sam. No desire to be rat food...)"
        jump cargo2
    else:
        p "(And this is so great. Another day, another tiny cage. Maybe jail wasn't so bad in some ways.)"
        jump cargo2

label cargo2:

    scene e3cargo3 with mediumdissolve
    p "(Couldn't even bother to put us in the cabin of the plane...trying to show us our place right away I guess...)"
    scene e3cargo4 with mediumdissolve

    play seven "music/cargohold1.mp3" fadein 3

    sc "Which one is [pname] inside of right now?"
    jk "It's the one on your left side."
    scene e3cargo5 with mediumdissolve
    sc "And who are the other two stored in this section?"
    jk "They were his two testing partners, [pname2] and Zach I believe are their names."
    scene e3cargo6 with mediumdissolve
    sc "Hello there [pname]! I trust you are comfortable?"
    sc "Can they all hear us in there?"
    jk "I believe so, but I'm not sure you can hear them. I think only our red boxes work that way."
    scene e3cargo7 with mediumdissolve
    sc "Well, we can't have that. I need to hear some begging."
    sc "Let me open one of these little doors on the middle box, and you get ready with [pname]'s box here."
    jk "Yes, Miss Scarlett."
    scene e3cargo8 with longdissolve
    sc "Let's hear who is in this little box here..."
    zach "Please! Let me out! I'll do anything! Please....please!"
    sc "Oh yeah, beg you little bitch..."
    p "(He never stops does he...)"
    scene e3cargo9 with mediumdissolve
    sc "Junko, I have heard about this one already! Poor little bug, he's going to get squashed so quickly isn't he."
    sc "But private time with him will have to wait, he's way too loud and distracting right now."
    zach "I'll be quiet, please just please..."
    scene e3cargo10 with mediumdissolve
    sc "Bye bye little one! I hope there is enough air in there for the whole flight! Maybe best not to think about it, hmm?"
    zach "Wait! Don't close the window, please!!!"
    scene e3cargo11 with mediumdissolve
    sc "Ah, much better. Let's open up [pname]'s box."
    jk "As you wish, Miss Scarlett."
    scene e3cargo12 with longfade
    sc "Hello there! Hmm, you don't look so bad there [pname]."
    sc "Sam was definitely right about you, what do you think Junko?"
    jk "He looks very nice."
    scene e3cargo13 with mediumdissolve
    sc "Why don't you get up out of that box so we can talk [pname]."
    p "(What now...)"
    scene e3cargo14 with mediumdissolve
    sc "You can take your time, it must have been very uncomfortable for you."
    sc "Maybe if you are an obedient little dog, I could try and get you a nicer cage next time."
    scene e3cargo15 with mediumdissolve
    sc "Junko, please help [pname] out and stand him up in front of his box here."
    sc "And let's move a little away from the boxes so these two others don't hear us."
    jk "Yes, Miss Scarlett."
    scene e3cargo16 with longfade
    sc "I hope you are excited about your upcoming program [pname]! How are you feeling about it?"

    stop seven fadeout 3

    menu:
        "(I shouldn't even bother faking that I am enthuiastic about it. I should be truthful and just say I'm not excited about it.) [JunkoPath]":
            $ junko_p += 1
            scene e3cargo16b with mediumdissolve
            p "I don't think anyone in my position would be that excited about this situation."
            sc "That's true, but at least you have a chance to not be stuck in a jail cell, right?"
            jump cargo3
        "(I should definitely answer very sarcastically. I mean does she seriously expect me to answer this question positively?) [ScarlettPath]":
            $ scarlett_p += 1
            scene e3cargo16c with mediumdissolve
            p "Oh yes, I'm super excited about it! Even sexually. I was even masturbating in my cell last night thinking about being...you know...rehabiliated."
            sc "You are lucky I enjoyed hearing that [pname]! That kind of answer with the wrong person could go badly for you. But for me that works fine, haha!"
            jump cargo3
        "(Maybe I should try and fake some kind of enthusiasm for everything. I certainly can say it's great getting out of a jail cell.) [red]\[ScarlettScale -1\]":
            $ scarlett_scale -= 1
            scene e3cargo16d with mediumdissolve
            p "Well, I'm happy to be out of a jail cell. Maybe this program can be a positive experience for me and I'll be...err...rehabilitated."
            sc "Maybe this program can be a positive experience for me? I'm not sure whether you are just stupid or trolling me right now."
            jump cargo3

label cargo3:

    scene e3cargo17 with mediumdissolve

    play seven "<from 50 to 215>music/cargohold1.mp3" fadein 1

    sc "Now [pname], we decided to let you out of your little box so we could meet you!"
    sc "We'd like to talk to you about something before you start your program."
    p "What's that?"
    scene e3cargo18 with mediumdissolve
    sc "Well, you're going to be in a world of shit soon. I'm guessing you have a pretty good idea by now that the rehabilitation program is pure bullshit."
    p "It doesn't surprise me."
    scene e3cargo19 with mediumdissolve
    sc "The truth is that this program is pure entertainment and spectacle for rich people that want to see all of you squirm and dance like good little puppets."
    sc "So you could use any friend or ally you can get to help you survive."
    scene e3cargo20 with mediumdissolve
    sc "And even though Junko and I are so different, we are actually long time friends and protect each other."
    sc "And either one of us can help you survive in different ways during your program."
    p "What's the catch? I know you want something in return."
    scene e3cargo21 with mediumdissolve
    sc "Of course. We both have our own desires and things we enjoy. You'd have to indulge our kinks and desires at times for our protection and information."
    p "What kinds of...kinks?"
    scene e3cargo22 with mediumdissolve
    sc "Well...for me, there are many things...but for example, I enjoy taking a man from behind and just having my way with him. I like being a little rough and..."
    p "...Wait, from behind...you mean with a strap-on..."
    sc "Yes...and as for Junko here..."
    scene e3cargo23 with mediumdissolve
    sc "Why don't you tell [pname] what you like to do to relieve your stress from working for your precious Lady Dominique."
    scene e3cargo24 with mediumdissolve
    jk "I like...having a pet, and also being worshipped and taken care of..."
    sc "Hmph, so soft Junko, I need to teach you the real pleasures of having a man under your power."
    scene e3cargo25 with mediumdissolve
    sc "If you agree to please us, we could what we can to help you survive better in your program. It might be information or something very specific to help you."
    sc "I have never had any of my bitch bo...I mean helpers fail or die during the program."
    p "(Wait, did she say die and bitch what??)"
    scene e3cargo26 with mediumdissolve
    sc "You're only getting this offer because we both agree you are acceptable. But really think about this before deciding."
    sc "You will rarely have any power to make decisions at your lowly K4 status. This might be the only chance you have to make a major choice so think carefully."
    scene e3cargo27 with mediumdissolve
    sc "You can have either Junko or I as a protector and confidant at times. It could give you an advantage with information and certain help, but nothing is ever that simple."
    sc "You could also miss an opportunity for an advantage with someone else, or lose valuable time to train or rest in order to please one of us. So what do you think?"

    stop seven fadeout 3

    scene e3cargo28 with mediumdissolve
    p "(Shit, I've literally just met them and I'm expected to try and figure out if they really can help me...or even keep their word)"
    p "(But this might truly be a legitimate thing that can help me too.)"
    menu:
        "(I think Junko seems a little more gentle and nice. It seems like a safer choice to rely on her, and she works for Dominique directly too. Scarlett seems more rough to me, and a strap on??) [JunkoPath]":
            $ junko_scale -= 2
            $ junkopet = True
            scene e3cargo28b with mediumdissolve
            p "I guess if I am going to pick someone, I am going to go with Junko."
            sc "Interesting choice. I guess you like being a little doggie then? But, I am happy for you Junko, you won this one."
            scene e3cargo28c with mediumdissolve
            jk "Yes, I guess I did. Why don't you take another one like Zach?"
            sc "No thanks! Did you hear him? Plenty of better bitch boys will be there I bet..."
            jump junkokneel
        "(Scarlett seems rougher and might be worse on me, but I feel like maybe I want to be dominated that way. Maybe she also can be a more helpful person to please, and she seems stronger than Junko.) [ScarlettPath]":
            $ scarlett_scale -= 2
            $ scarlettpeg = True
            scene e3cargo28d with mediumdissolve
            p "I guess if I am going to pick someone, I'm going to go with you Scarlett."
            sc "Oh! How delightful for me. If you can keep up with me, you might benefit from it, but we'll have to see."
            scene e3cargo28e with mediumdissolve
            sc "Sorry Junko, but I guess you're out of luck on this one! I'll help you find someone else to play with, promise!"
            jk "I hope so..."
            jump scarlettkneel
        "(This might be a crazy thought, but why can't I serve both? It doesn't hurt to please as many people as possible...although am I giving up future chances too quickly?) [gr]\[BusyBoy\]":
            $ busyboy = True
            scene e3cargo28f with mediumdissolve
            p "It's actually really hard to pick just one of you. What if I serve both of you?"
            sc "Are you serious [pname]? You want to try and handle both of us?"
            scene e3cargo28g with mediumdissolve
            p "Sure. I'd like to please both of you, and I would hope you can help me too."
            sc "What do you think, Junko? We've never had this possibility offered before."
            scene e3cargo28h with mediumdissolve
            jk "I'm ok with that, but can you let me use him first? I am afraid he will be too...tired after you."
            sc "Haha, you mean you are worried I'll abuse him too much for you to have any fun afterwards. Ok, I don't mind Junko! Let's do it!"
            jump dualkneel
        "(I'm not sure I should commit anything just yet, and I know almost nothing about them. Maybe I should turn both of them down gracefully if possible and see what else might happen first.) [ScarlettPath] \[FreeAgent\]":
            $ freeagent = True
            $ scarlett_p += 2
            $ junko_p -= 2
            scene e3cargo28i with mediumdissolve
            p "I appreciate the offer from both of you, but I barely know anything about what is happening, much less how much I can trust and rely on your help."
            p "I think I should wait and figure out a little more about what is happening before making big decisions so early."
            scene e3cargo28j with mediumdissolve
            sc "It's your funeral [pname], although I can actually respect what you said. Just remember that later on it might be too late to beg for our help."
            p "I understand."
            scene e3cargo28k with mediumdissolve
            sc "Oh well Junko! I guess we don't get to have some easy fun right away at the start of the program. We'll have to find some other meat..."
            jk "Yes, I suppose so."
            sc "Since you're not going to be either of our close friends right now, I think it's back into the box for you for the remainder of the flight!"
            p "(Oh joy...)"
            jump vapmeeting

label junkokneel:

    scene e3junkokneel1 with mediumdissolve

    play seven "<from 129 to 488>music/kneel.mp3" fadein 3

    sc "Since you picked Junko, you need to devote yourself to her right now to show your obedience."
    p "How?"
    scene e3junkokneel2 with mediumdissolve
    sc "That's up to her. What do you want him to do Junko?"
    jk "Can he...can he just get on his knees and look at my body?"
    scene e3junkokneel3 with mediumdissolve
    sc "This again? [pname], she likes to just have her pets look at her body first."
    sc "And then she'll deprive you of her body and any relief for a while until you beg enough for it like a good dog."
    scene e3junkokneel4 with mediumdissolve
    jk "Scarlett! This one is mine! Don't spoil my fun!"
    sc "Ok...ok Junko. Well, go ahead and get on your knees [pname] and enjoy the show."
    scene e3junkokneel5 with longfade
    sc "I love your tits Junko, so juicy looking, haha!"
    sc "Go ahead and look up at your new owner [pname]!"
    scene e3junkokneel6 with mediumdissolve
    p "(Wow....nice.)"
    jk "I might have to lock you up at first [pname], but I hope you learn to please me."
    menu:
        "(I want to please her and should tell her so. I think I want this...) [red]\[JunkoScale -1\]":
            $ junko_scale -= 1
            scene e3junkokneel7b with mediumdissolve
            p "I want to please you and do what you want. I will be diligent and obedient for your needs."
            jk "Good! That's a very...wonderful attitude. I think I will be very happy with you."
            jump junkokneel2
        "(I'm not super enthusiastic about this without knowing more about her. I should play it a little cool for now and see how she actually treats me.)":
            scene e3junkokneel7c with mediumdissolve
            p "I understand."
            jk "I think you will find I can be a sweet owner if you are obedient. I'm not a cruel sadist like so many other women around here."
            p "(I guess that might be good...)"
            jump junkokneel2

label junkokneel2:

    scene e3junkokneel8 with longdissolve
    sc "Well, I'm glad we have that all figured out now. I am looking forward to seeing you in the program [pname]."

    stop seven fadeout 3

    sc "But for now, back into the box you go. We'll be arriving at your new home in a few hours. Try and rest, you will need it!"
    jump vapmeeting

label scarlettkneel:

    scene e3scarlettkneel1 with mediumdissolve

    play seven "<from 129 to 488>music/kneel.mp3" fadein 3

    sc "Since you picked me as your special friend, I think you need to show me some immediate devotion and obedience."
    p "How?"
    scene e3scarlettkneel2 with mediumdissolve
    sc "You can start by getting on your knees, you little bitch."
    p "(Great...)"
    scene e3scarlettkneel3 with longdissolve
    sc "That's not bad [pname], but when I say kneel, I mean I want your head much, much, lower to the ground."
    sc "You should get much lower where you belong."
    scene e3scarlettkneel4 with longdissolve
    sc "That's being a good little [pname], much better."
    sc "I need to know if you are even worth my time to even try and help at all. So I want to see if you are tough enough for me. If you aren't, how do you expect to survive the Karlssons?"
    scene e3scarlettkneel5 with longfade
    sc "There we go! I am so happy we will get to know each other so much better!"
    p "(Ugh!)"
    sc "And I can help you...if you are helpful to me of course."
    scene e3scarlettkneel6 with mediumdissolve
    sc "Like everyone else in The Karlsson Group except maybe Junko here, I am always striving for more power and influence."
    sc "So I'll have some tasks for you too, and maybe then, and only then, can I help you get a small taste too."
    scene e3scarlettkneel7 with mediumdissolve
    sc "But as for your first night in the program, I hope you won't be bleeding out of your ass when I am done with you."
    scene e3scarlettkneel8 with mediumdissolve
    sc "But for now, back into the box you go. We should be arriving in a few hours. Let's put him back in his coffin Junko!"

    stop seven fadeout 3

    jk "Yes, Miss Scarlett."
    jump vapmeeting

label dualkneel:

    scene e3dualkneel1 with mediumdissolve

    play seven "<from 129 to 488>music/kneel.mp3" fadein 3

    sc "So you can really think you can handle serving both of us [pname]? This should be very interesting. Are we going to fight over him Junko?"
    jk "Just don't damage him so we can relax with him properly."
    scene e3dualkneel2 with mediumdissolve
    sc "You might want to relax, but I want something else from [pname], and he's going to give it to me."
    scene e3dualkneel3 with mediumdissolve
    sc "You're going to give me exactly what I want, won't you [pname]?"
    menu:
        "(I don't think there is any point not saying what she wants to hear right now. I should say I'm fine doing what she wants.) [ScarlettPath] [red]\[ScarlettScale\]":
            $ scarlett_scale -= 1
            scene e3dualkneel3b with mediumdissolve
            p "I'll give you what you want. I want to be able to please you."
            jk "What about me? I hope you want to do what I want too!"
            sc "Don't worry Junko, I am sure [pname] will be very fun for both of us...if he can handle it."
            jump dualkneel2
        "(I think I should state I want to please her, but I better include Junko in that statement because I did offer to please both of them.) [JunkoPath]":
            $ junko_p += 1
            scene e3dualkneel3c with mediumdissolve
            p "I don't have a problem doing what I need to with pleasing you and Junko."
            jk "Oh, I'm glad you didn't forget about me [pname]. I will treat you well if you can do a good job with me."
            sc "Mmm hmm, well I for one don't want to just relax and relieve stress with you [pname]. I want to feel excited and get off...so you better deliver."
            jump dualkneel2
        "(I don't feel like just constantly begging and saying exactly what she wants. I'll just keep quiet and see what happens.)":
            $ scarlett_p -= 1
            scene e3dualkneel3d with mediumdissolve
            p "....."
            sc "Oh, so you're too good to answer a simple question from me, are you?"
            scene e3dualkneel3e with mediumdissolve
            sc "*slap* I expect an answer when I ask a question! So will every other woman above your pathetic ass!"
            jk "I'm sure he wants to listen us Miss Scarlett. No need to rough him up."
            sc "If he won't obey well, I'll rough him up any way I like!"
            jump dualkneel2

label dualkneel2:

    scene e3dualkneel4 with longdissolve
    sc "Now get on your knees [pname]. I want to be very clear where you stand in life right now."
    scene e3dualkneel5 with longfade
    sc "That's better [pname]. Get this through your head right now. You are nothing but a little bug to both of us."
    sc "If you don't make us happy, you will know nothing but pain and suffering...day...after...day. We both can make your life so much worse than it should be."
    sc "But if you are a good boy...Junko, why don't you show him what he can get from you at least."
    scene e3dualkneel6 with mediumdissolve
    sc "This body has only been ravished by Dominique Karlsson herself. No one else has been allowed to touch her."
    sc "But for some reason, Dominique has now allowed her precious servant Junko the freedom to do anything she wants with you. And I mean anything. And only for you."
    scene e3dualkneel7 with mediumdissolve
    sc "I am so curious why that is...I believe she has other orders from Dominique about you, but of course Junko would never tell me."
    jk "No, and you wouldn't either..."
    sc "So go ahead [pname], get a good look at what you might be able to have if you are obedient."
    scene e3dualkneel8 with mediumdissolve
    sc "And you are going to be a busy boy with both of us and all the work for your program too. I hope you can keep up, haha!"

    stop seven fadeout 3

    sc "But for now, back into the box you go. We should be arriving in a few hours."
    sc "I am quite sure you will be seeing both of us again very soon..."
    jump vapmeeting

label vapmeeting:

    play seven "music/sisintro.mp3" fadein 3

    scene e3vap1 with longfade
    pp "I'm reporting as requested to meet with Veronica Karlsson. Oh, hey...Sonya!"
    sy "...Good to see you Patricia, have you still been training with all the moves I taught you?"
    scene e3vap2 with longfade
    pp "I'm still doing everything three times a week to maintain and improve my skills."
    sy "Glad to hear it. You were a great student. You sure you don't want to be a part of our little team?"
    sy "I could put in a good word with Kiyomi for you..."
    scene e3vap3 with mediumdissolve
    pp "I've got other goals in mind, but I appreciate the offer Sonya."
    sy "Suit yourself. I think you would be really good at it though."
    scene e3vap4 with mediumdissolve
    sy "Veronica wanted to meet you in the side pool area, so let's have you wait out there for her."
    pp "Sounds good."
    scene e3vap4b with longfade
    sy "Hey Delilah, come meet an old friend of mine, Patricia."
    sy "She trained under me a while and really developed lethal power with her legs!"
    scene e3vap4c with longdissolve
    de "Nice to meet you! You do have such long and pretty legs, I bet they are quite effective!"
    pp "Nice to meet you too, and thanks."
    scene e3vap5 with mediumdissolve
    sy "Delilah here is the newest member of our little group now. Don't let her size and youth fool you, she's a very talented asset. Especially seduction and stealth."
    pp "How many of you are there now?"
    sy "Five. A lot of busy bee staff and underlings of course, but just five heavy hitters. Kiyomi keeps it tight to ensure everything is secure."
    scene e3vap6 with mediumdissolve
    pp "I can imagine. She's the best."
    sy "Yes she is. I hate to break our reunion short, but we both have an assignment and need to go right away. Let's catch up later when we are both free!"
    scene e3vap7 with mediumdissolve
    pp "Sounds good. Do I need to let Veronica know I am here?"
    sy "No need. She probably already tracked you while you were still twenty minutes away from here with her millions of surveillance tools. She knows."
    sy "Just relax. She's probably waiting for us to leave so you can talk privately."
    scene e3vap8 with mediumdissolve
    pp "Ok. Good luck on your assignment."
    de "It's going to be so fun, we can..."
    scene e3vap9 with mediumdissolve
    sy "...uh uh, she's a friendly, but doesn't have our clearance. But the door is always open for you Patricia..."
    de "Right right, sorry."
    scene e3vap10 with longdissolve
    sy "Let's really catch up later. It would be nice."
    pp "Agreed. I'll make sure. Talk you to soon."
    sy "Great, talk soon."
    de "Bye!"

    stop seven fadeout 3

    jump vapmeetingtwo

label vapmeetingtwo:

    scene e3vap11 with longfade
    pp "(I really could use a massage...)"
    v "You look like you could just fall asleep out here."
    scene e3vap12 with longdissolve

    play seven "music/jail.mp3" fadein 2

    pp "Mistress Veronica! Sorry, it's just been a long few days and..."
    v "It's quite alright Patricia."
    scene e3vap13 with longfade
    pp "Oh, Mistress Alessandra, I didn't know you would be here too!"
    v "Yes, we both want to talk to you. Now my legs are a bit tired so..."
    scene e3vap14 with mediumdissolve
    pp "Yes, Mistress. I will serve you."
    v "Good."
    scene e3vap15 with longfade
    v "So Patricia, before we get to why you are here, I am curious to hear about your experience with [pname]."
    pp "Of course Mistress, what would you like to know?"
    scene e3vap16 with mediumdissolve
    a "Make sure you serve me too while listening to my sister."
    pp "Yes, Mistress."
    v "Just tell me a little about him. Your own thoughts."
    scene e3vap17 with mediumdissolve
    if good >= 4:
        pp "Mistress Veronica, [pname] seems to have a very strong moral conscience, it showed in how he reacted to his situation."
        v "That's good to know, and that will certainly please one of my sisters."
        a "Yes it will."
        stop seven fadeout 2
        jump vapmeetingthree
    elif evil >= 4:
        pp "Mistress Veronica, [pname] has shown flashes of darkness. I believe he can be corrupted quite easily."
        v "That's useful to know. But I wonder what specific temptations will work best."
        a "Hopefully he likes what I do!"

        stop seven fadeout 2

        jump vapmeetingthree
    else:
        pp "[pname] is a little hard to read. I think he is keeping things a little to himself without being obvious. I'm sorry I don't know a whole lot."
        v "That's ok Patricia. Certainly we will all have our chance to evaluate him in time."

        stop seven fadeout 2

        jump vapmeetingthree

label vapmeetingthree:

    scene e3vap18 with mediumdissolve

    play nine "<from 42 to 190>music/hospital2.mp3" fadein 3

    v "I actually did want to ask you a little more about [pname], but we can do that later. We need to discuss why you are here."
    pp "Yes, Mistress."
    scene e3vap19 with mediumdissolve
    v "Patricia, I have been watching you very carefully recently. In short, I have been impressed with you."
    v "In particular, I am pleased that you have shown both ruthlessness but also restraint in your actions. Such balance is quite important."
    pp "Thank you, Mistress."
    scene e3vap20 with mediumdissolve
    v "It has not escaped both of us that unlike any other guard at your jail, no prisoners have suffered permanent injury or death under your care. Quite efficient not to waste resources needlessly."
    v "And yet, you also did not hesitate in killing the prisoner that tried to attack Sam three months ago. And, you made it very painful and lasting to scare the other prisoners very effectively."
    scene e3vap21 with mediumdissolve
    v "I was reluctant to use you for higher purposes given your average intelligence ratings, but it is quite clear that you are cunning and intelligent in ways our tests didn't catch."
    v "You also pass the obvious physical requirements we like as well. And both Elena and Alessandra feel you can do more with us despite your humble background."
    v "So with that in mind, we are offering you a new position."
    scene e3vap22 with mediumdissolve
    pp "I'm ready to do whatever you and Mistress Alessandra ask."
    v "Good. But it is an offer. You don't have to take this job, but it would be a great chance for you to impress us."
    scene e3vap23 with mediumdissolve
    v "My sister here has been preparing the logistics of the rehabilitation program, and she has almost completed everything for the prisoners when they arrive."
    v "Alessa, why won't you fill in the rest."
    scene e3vap24 with mediumdissolve
    a "Patricia, I would like you to transfer to our prisoner rehabilitation program. It would be a big promotion for you."
    a "You would be in charge of the daily needs and scheduling of the prisoners. They will also be doing some training, but that will fall under Kiyomi's group."
    scene e3vap25 with quickdissolve
    a "You would be reporting directly to a woman named [pname3], along with her primary assistant."
    a "But you would also have an additional special task from us as well."
    scene e3vap26 with mediumdissolve
    a "The program manager, [pname3], is actually [pname]'s sister, and there will be a late arriving prisoner named [pname4] that is also her brother."
    pp "Wait, they are all like brother and sister, but she's managing them for this program? Why?"
    scene e3vap27 with mediumdissolve
    v "Don't worry about that, but trust there is good reason we are doing it."
    a "Now, for everything else, you obey [pname3] without question. Don't you dare ever cross or displease her as she can and will punish you."
    scene e3vap28 with longdissolve
    a "But the secret task for you, and for only this, you must remain silent to everyone but us. That even includes our two other sisters."
    pp "I...I understand, Mistress."
    v "Patricia, I'm done with you as a footrest. Get up so you can listen very carefully to what Alessa says here."
    scene e3vap29 with longfade
    a "The special task is very simple. If you observe or feel [pname3] is playing favorites with either of her two brothers, I want you to let me know immediately."
    scene e3vap30 with mediumdissolve
    a "Otherwise, just do whatever [pname3] asks. I emphasize again, that no else...not Elena, not Juliette, not Dominique...no one else is to know about this special task."
    a "If you fail at keeping silent on this, you will suffer severe consequences. Do you understand?"
    scene e3vap31 with mediumdissolve
    pp "I understand, Mistress Alessandra."
    a "Good. Your current pay will be multiplied by five times as a reward for both your prior performance and this new assignment if you accept. I will update your employee rank later when I have time."
    pp "(Oh wow! Five times...)"
    a "Now, do you accept the position? I need an answer right away because you need to start immediately if so."
    scene e3vap32 with mediumdissolve
    pp "I accept. I want to serve the company and both of you better."
    a "A very wise decision. Excellent."
    v "Patricia, since you have accepted, I already have a car ready to take you to the facility. So go to the garage and have Franklin drive you, he is expecting you."
    scene e3vap33 with mediumdissolve
    pp "Thank you for the opportunity. I will make sure to please both of you!"
    v "Let's hope so."

    stop nine fadeout 3

    jump vbase

label vbase:

    scene e3vase1 with longfade

    play seven "music/vawalk.mp3" fadein 3

    a "Shouldn't we change? Might be too cold down there."
    v "Don't worry, I've made it a lot more comfortable."
    scene e3vase2 with mediumdissolve
    v "Alessa, I'm still not 100 percent sold on Patricia, are you sure about her?"
    a "She's hungry, ambitious, and cunning. I think she will be fine."
    scene e3vase3 with mediumdissolve
    v "I know, but I am worried about the next best offer dividing her loyalty."
    a "You just have to trust me on her. She's under control, believe me."
    v "Ok."
    scene e3vase4 with mediumdissolve
    v "And what about [pname3]? Just give me your gut feeling on her."
    if sisdom >= 4:
        a "I think she might be strong enough to handle Dominique and Juliette."
        a "But she has so little understanding of our world. It might be a steep learning curve."
        v "Given her very humble upbringing and being shoved so quickly into this situation, I'd say that is a very good sign. Just keep on her and see how she develops."
        jump velevator
    elif sissub >= 4:
        a "I am worried she is too submissive right now. She might get run over by Dominique and Juliette."
        v "Don't fret too soon. Remember how she grew up. How strong would you be at first growing up with no power or money, and then just being thrust into this situation?"
        a "True. It's too early to say. I will keep working on her."
        jump velevator
    else:
        a "It's too early to say. She seems a little uncomfortable at everything, but also adjusting fairly well considering how fast we moved on her."
        v "That's pretty much within reasonable expectations I would say. Just keep on her and see how she develops."
        a "I hope she is strong enough..."
        jump velevator

label velevator:

    scene e3elevator1 with longfade
    a "You know, it wouldn't kill you to upgrade this elevator to something more luxurious. This is still so sad that I have to ride this piece of junk."
    v "You always were too posh and pampered compared to the rest of us. This is perfectly functional, and barely anyone goes down here."
    a "I'm coming here! You seriously need to let me bring in some interior designers to spruce up your stuff."
    v "..."
    scene e3elevator2 with longdissolve
    v "Isn't [pname3] going to be meeting Juliette today?"
    a "Yes, Cassandra is doing a little more orientation with her this morning, and then they are meeting Juliette later in the day."
    v "That should be interesting."
    scene e3elevator3 with mediumdissolve
    a "I kind of wish I was going with her for that one. Maybe it's too much too soon."
    v "No, remember that Cassandra is more than qualified to assist [pname3]. And Juliette loves meeting with Cassandra too."
    a "You're right. I am worrying too much."
    scene e3elevator4 with mediumdissolve
    a "The prisoners should be arriving today as well. [pname4] is going to be delayed I take it?"
    v "Yes, I need to do some additional testing. I have synthesized a compound to help with his condition, but I need a little more time."
    v "I want to be sure he is reasonably strong and healthy before throwing him to the wolves."
    scene e3elevator5 with mediumdissolve
    cman "ppppllleaseee...a little water...food...I beg of you..."
    a "Awwwww, don't make him too healthy. It might be fun to see him struggling to move with such severe pain."
    v "You're so bad Alessa...let's just go see your present."

    stop seven fadeout 2

    jump vbroom

label vbroom:

    scene e3broom1 with longfade

    play seven "music/broom.mp3" fadein 3

    a "Oh Veronica! What a wonderful present you gave me, is that who I think it is?"
    v "Yes, it's Diana. I thought you might appreciate the gesture."
    a "The poor thing. How ever did she get herself in this situation?"
    scene e3broom2 with mediumdissolve
    a "I guess you fell on such hard times after I destroyed your business. I did offer to buy you out and bring you on my team...so sad isn't it?"
    a "You could have at least been working under me and surviving, but I guess you'll be under me...in other ways soon hmmm?"
    scene e3broom3 with mediumdissolve
    a "How did you ever get her here dear sister?"
    v "I hired her under a shell company after you destroyed her own business. And...she had to allow this possibility to survive at that time."
    a "How delightful! We're going to have so much fun..."
    scene e3broom4 with mediumdissolve
    a "Don't you have anything to say Diana?"
    di "No...you're going to do whatever you want anyway. I know better with you. I...I know my life is...is basically over."
    a "No, it's just beginning. You have a lot of good years of...service left, haha!"
    scene e3broom5 with longdissolve
    v "There's actually one more thing for you."
    a "More? What is it?"
    scene e3broom6 with mediumdissolve
    v "It's over here. Let me show you..."
    scene e3broom7 with longdissolve
    a "Wow, it's an invisible slut! You really are the best scientist in the world Veronica!"
    v "Err, I swear I left him in here. Wait, maybe that was...let's check the other side."
    scene e3broom8 with longdissolve
    v "Let's see...he must be in this one."
    scene e3broom9 with longdissolve
    a "Wow, you even ensnared poor Brad? Diana, how you could let the love of your life get mixed up with your trouble?"
    di "You fucking evil bitch..."
    a "Poor Diana, I'm only going to take it out on him more if you aren't nice to me. And Brad, if you even speak, little Diana suffers for it."
    scene e3broom10 with mediumdissolve
    a "Veronica, Brad must be so lonely in the dark there! That's a little cruel keeping him in there."
    scene e3broom11 with mediumdissolve
    a "But you know Brad, it's partially your fault. You should have taught little Diana to know her place."
    scene e3broom12 with mediumdissolve
    a "Maybe it would have saved you the pain you are going to suffer. And you are both going to suffer. Oh yes...so sad isn't it..."
    a "I just can't decide which of you I will ravage first in front of the other...mmmm"
    scene e3broom13 with mediumdissolve
    a "Hmm, I actually have a special idea for Brad, Veronica."
    v "You don't want to just keep him?"
    scene e3broom14 with mediumdissolve
    a "Oh no. I'll just keep Diana, and then she can watch her beloved man participate in our program...up close and personal."
    v "The program? He hasn't even been tested or vetted at all."
    scene e3broom15 with mediumdissolve
    a "Who cares? It will be fun to see how he does. He certainly will be motivated."
    a "Can you send Diana to me for some fun later, and place Brad in the program?"
    scene e3broom16 with mediumdissolve
    v "It's your present. But I insist on at least a little testing for him before he gets there. Just to be sure."
    a "Of course, I don't want to endanger the program either. We'll start without him, and I guess [pname4] too."
    scene e3broom17 with longfade
    a "Thank you sis! Oh, can I have a little water? I noticed your poor wall decoration out there was thirsty..."
    v "Really Alessa? Fine, have a little fun down here, but you need to hurry back too don't you?"
    a "You're right. I'll be quick and see myself out. And...bye bye Diana!"
    di "(you evil...)"

    stop seven fadeout 3

    jump e3water

label e3water:

    scene e3water1 with longfade

    play seven "<from 383 to 455>music/evilmix3.mp3" fadein 2

    a "Hello there! I noticed you were so thirsty! My sister hasn't been treating you well, has she?"
    cman "No..."
    scene e3water2 with mediumdissolve
    a "Well, I do have a little water here..."
    a "But you know, I'm a little thirsty too. So maybe you can have some of what's left after I am done?"
    cman "Ok..."
    scene e3water3 with mediumdissolve
    a "Mmmmmm...this is so refreshing. Nothing like the taste of fresh water...sooooooo yummmmmy."
    a "I can feel it going down my throat...mmm feels soooo gooood."
    scene e3water4 with mediumdissolve
    a "Ahhhh, I just can't stop, it's soooooooo goooooood..."
    a "I'll try to leave you a little...does it hurt more seeing water so close to you when you are soooooo desperate for it?"
    scene e3water5 with mediumdissolve
    a "Oops, I drank it all. So sorry."
    cman "I..."
    scene e3water6 with mediumdissolve
    a "I have to go right now, but I could be back later. I can bring you some fresh water then if you want."
    cman "Please..."
    scene e3water7 with mediumdissolve
    a "Ok, but you need to play a game for me. This room is constantly being recorded, and I would like you to do something while I am gone."
    a "I want you to count out loud from the number 1 to the number 20,000. If you can do that, I promise to bring you some water."
    a "But if you make a mistake or don't say each number loudly and clearly to the camera, you lose."
    scene e3water8 with mediumdissolve
    cman "Why...why do I have to do that?"
    a "Because I want you to. You aren't in any position to argue, are you? I want to see if you can count to 20,000 within four hours."
    a "There is a clock there on the far wall if you can see it. So try your best and maybe you can do it!"
    scene e3water9 with mediumdissolve
    cman "Fffour hours, but I'm so thirsty and...oh my God..."
    a "....I suggest you begin immediately because I'm starting the clock right now! Have fun!"
    scene e3water10 with longdissolve
    cman "1,2,3,4,5,6,7,8..."
    a "(Life is so sweet...haha!)"

    stop seven fadeout 3

    jump parking

label parking:

    scene e3parking1 with longfade

    play seven "music/jakechill.mp3" fadein 2

    cass "I'm sorry if you are still a little tired from traveling yesterday. Mistress Alessandra's garden is a great place to start though for this place..."
    sis "No, I'm ok. Let's keep going."
    cass "Ok. Well, this garage houses all of your company cars that are available for use. I apologize but we are actually missing two additional vehicles for you right now."
    cass "One is a luxury SUV and another is a motorcycle if that is your thing. But we do have four vehicles available right now for you."
    if poorprisoners:
        sis "And what about your own car that I approved for you? Is that here as well?"
        cass "No, I still have to get one approved for purchase! I hope you let me get a nice red sports car!"
    else:
        sis "Six vehicles, wow! Now I feel bad that I didn't approve a vehicle for you right away, perhaps I should rethink that idea."
        cass "It's ok Mistress [pname3]. I do have my own little car. Plus, I have the use of a limo at times, and free driver service with a normal car."
    scene e3parking2 with mediumdissolve
    cass "Of course, you have also have unlimited use of a limo and you can even request a helicopter or plane if you need it. Mistress Alessandra would approve that kind of request."
    sis "Wow, some of these vehicles are pretty nice! I'm not a car expert, but I bet these are incredibly rare and expensive!"
    cass "Of course they are! You're now one of the top executives in the entire company! You deserve every luxury you desire!"
    scene e3parking3 with mediumdissolve
    sis "Alessandra checked up on me last night, and one thing she told me was that my employee rank was Z3. What does that mean in this company?"
    cass "Z3?!!? Oh wow, I thought you would be a Z1 as it normally is for this program position! That's...incredible Mistress [pname3]!"
    sis "Why?"
    scene e3parking4 with mediumdissolve
    cass "That means they must really like you! I think there are about a dozen Z1s in The Karlsson Group, but I have not heard of a Z3 or even Z2 existing since I started working here."
    sis "Really? I guess I can't complain, wow, look at this red car!"
    cass "I'm really serious Mistress [pname3], this is a big deal! The Board members are Z4 employees, so you are literally right under them. And you are brand new too...amazing."
    scene e3parking5 with mediumdissolve
    sis "I guess I better do a great job to maintain their trust. And I hope you will help me as well."
    if sis_c_p >= 3:
        $ cassandraloyal = True
        cass "Mistress [pname3], you have treated me perfectly in our short time together, and I want to help you succeed with everything I have. I will make sure you do well!"
    else:
        cass "I will do what I can to help you do well with your new role. My main job is to help make yours easier and more successful. You can count on me!"
    scene e3parking6 with mediumdissolve
    sis "Thank you, Cassandra. Now, I have to ask, do I really have use of a police car? Why?"
    cass "Ah, I don't know if now is the time to talk about this, but the company of course employs its own police force on this private country so to speak."
    scene e3parking7 with mediumdissolve
    cass "So...if you want...just for fun, you can dress up in uniform and just go out on the town with this car...and find anyone to...arrest and you know...have fun with and all."
    cass "Of course, we might want to take someone that's a pro to go with us just in case there is trouble. You will have a few trained people like that under your supervision."
    scene e3parking8 with mediumdissolve
    sis "Wait! Are you telling me we can play as policewomen and literally just go out on the street and grab anyone just like that? Do they have to be guilty of a crime?"
    cass "Of course not. You can prey on anyone weak and helpless out there. It doesn't matter if they are guilty or innocent. We can go out and try that later if you like..."
    scene e3parking9 with mediumdissolve
    sis "(Inviting me to participate in something like that...Oh my God, I am starting to finally understand the extreme power that seems to be at my fingertips...)"
    sis "(It seems I can do almost anything...why so much for me so quickly? And this is just a side activity being offered! What can I do in the actual program itself with prisoners?)"
    scene e3parking10 with mediumdissolve
    sis "(And Cassandra seems wired to be cruel and sadistic. Her theater masturbation is strong evidence to me...and I can walk down this road too...)"
    cass "Mistress [pname3]? Did you hear what I said about playing police sometime?"

    stop seven fadeout 3

    menu:
        "(I don't think I have any desire to go outside as a fake policewoman to just harass people. It feels wrong, and I have enough to handle with just this situation right now.) [SisGoodPath]":
            $ sisgood += 1
            $ moralityone = True
            scene e3parking10b with mediumdissolve
            sis "Cassandra, I don't think that I should be spending time on that kind of thing right now. I think I better focus on the new position first."
            cass "Of course Mistress [pname3]! That should always take priority, and I understand that what I offered isn't for everyone."
            jump parking2
        "(I'm not against exploring some of my new power that way, but I should be patient with everything. I need to wait on that kind of stuff until I have a better handle on my new job.) [SisVeronicaPath]":
            $ sis_v_p += 1
            scene e3parking10c with mediumdissolve
            sis "Cassandra, I'm kind of interested in maybe having some fun like that, but for now, I think I need to focus on getting ready for my new position."
            cass "Of course Mistress [pname3]! That should always be the first priority for all of us! Perhaps we will have time down the road for some fun..."
            jump parking2
        "(I want this. I want to enjoy having power and doing what I want to anyone...weaker than me. Why not have some fun with some unfortunate people out there?) [SisEvilPath]":
            $ sisevil += 1
            $ evilpolice = True
            scene e3parking10d with mediumdissolve
            sis "Cassandra, it sounds like a lot of fun. I want you to arrange it sometime, but of course the program work has to come first."
            cass "Oh wow, really? You are like the best Boss...I mean Mistress ever! I can have our best agent Kiyomi take us out for some fun!"
            if cassandraloyal == False:
                $ cassandraloyal = True
            cass "I have the best uniforms we can wear too! They look so hot, and the boots and police batons I have are so good! It'll be so fun!"
            jump parking2

label parking2:

    scene e3parking11 with longdissolve

    play seven "music/jakechill.mp3" fadein 2

    cass "So we have a lot to do today to get you ready for everything, but our first order of business is to pick your outfit!"
    sis "My outfit?"
    cass "Yes, we need to find you the best outfit for when you meet the prisoners for the first time."
    scene e3parking12 with mediumdissolve
    cass "The right look can set a tone and very strong first impression with prisoners right away so we want to get this right!"
    cass "How you want to appear to the prisoners is up to you...but I can give you my suggestions of course."
    scene e3parking13 with mediumdissolve
    sis "I appreciate that, Cassandra. I do want to make a good first impression."
    cass "Great! Now...which car are we taking?"
    scene e3parking14 with longdissolve
    sis "Oh...I have to take the red one here. It's just too tempting to pass up the chance to drive it."
    cass "Great choice! You know, Alessandra and Juliette Karlsson actually race these super cars for fun on private tracks so maybe you can try that with them later. But for now, let's go!"
    scene e3parking15 with longfade
    cass "I know the best private little store we can go to pick your look. Mistress Alessandra uses it all the time so you should too."
    sis "Sounds great, let's see what this car can do, haha!"

    stop seven fadeout 2

    jump store1

label store1:

    scene e3store1 with longfade

    play seven "music/clothing2.mp3" fadein 2

    cass "Let me just unlock the door...ah here we are!"
    sis "I thought we were going to an open store like at a shopping center? What is this place?"
    scene e3store2 with mediumdissolve
    cass "This is a private corporate store for employees, but it's usually only open by appointment."
    cass "There should be a few items in the back you can try on to see what you like."
    sis "Ok, sounds great."
    scene e3store3 with longdissolve
    cass "Actually, I have to confess something now Mistress [pname3]."
    sis "What's that?"
    cass "Mistress Alessandra already prepared two outfits for you to consider for your first day, and made sure they fit your size. She wanted it to be a surprise."
    scene e3store4 with mediumdissolve
    sis "Is that right? I bet she has got some great selections for me!"
    cass "She made sure that the outfits were really luxurious materials but she also wanted to give you more than one choice. They should be in the large dressing room in the back."
    sis "I'm kind of curious to see what Alessandra picked! Let's go see what she has for me!"
    scene e3store5 with longfade
    cass "I'll wait here for you while you change. First door on your right."
    sis "Sounds good, be right back."
    scene e3store5b with longfade
    sis "Ok, Cassandra, this is the first of them. What is your first impression?"
    cass "This outfit looks very professional but also sexy. I think it will set a tone that you are all business. This is also how most of the top executives dress at The Karlsson Group."
    cass "Some on the Board will like you keeping it professional, but some might not considering your position."
    scene e3store6 with mediumdissolve
    sis "What is the weakness of this outfit in your opinion?"
    cass "For your first day, you might want to look a little more intimidating since you are dealing with prisoners. I think it might help to have them fear you a little."
    scene e3store7 with mediumdissolve
    sis "Hmm, that's a good perspective with your feedback Cassandra. I'll definitely have to keep this in mind."
    sis "Ok, I'll go try the second one now."
    scene e3store8 with longfade
    sis "How about this one? Definitely a very different look!"
    cass "Oh wow, you definitely look intimidating with this outfit! The whip is a nice touch too."
    scene e3store9 with mediumdissolve
    sis "Alessandra didn't even bother to give me a skirt for this outfit. I guess she thinks the boots are enough?"
    sis "I do wonder if this is a bit too much right away. I feel like a dominatrix. What do you think?"
    scene e3store10 with mediumdissolve
    cass "I think you are projecting a message of power and confidence in a different way with this outfit. But you have to back up this look with action."
    cass "And to be totally honest Mistress [pname3], I would guess some on the Board will love this and some won't. But for the prisoners, it could set a good tone."
    scene e3store11 with mediumdissolve
    sis "Hmm, should I worry more about the prisoners or the Board?"
    cass "Always the Board. But I know Mistress Alessandra likes you a lot, so that's a big start."
    scene e3store12 with mediumdissolve
    cass "So which outfit do you want to wear when you meet the prisoners for the first time?"
    cass "We'll probably set up one on one meetings initially with them if that matters to you."
    scene e3store13 with mediumdissolve
    sis "(It's important I set the right first impression on both the Board and the prisoners. Can I do both at once?)"
    if sissub >= 2:
        sis "(I don't know if I can handle being in charge easily, but I have to try my best anyway. Which outfit is better?)"
    else:
        sis "(I need to make sure to stay on top of everything by making smart decisions. Which outfit is better?)"
    menu:
        "(I feel like picking the more professional outfit is the safer choice. Until I know more about everything, perhaps I should play it safe, and would a top executive really wear that other outfit?) [SisDominquePath] [SisJuliettePath]":
            $ proboss = True
            $ sis_d_p += 2
            $ sis_j_p += 2
            scene e3store13b with mediumdissolve
            sis "Cassandra, I think I am going to wear the first outfit for the initial meetings, but I'd like to save both of them just in case I need them down the road."
            cass "Very good Mistress [pname3], I will wrap both outfits for you and take them to the car."
            sis "Thank you, Cassandra."
            jump store2
        "(They did pick me to manage prisoners for clearly illegal or at best questionable practices. I think they gave me the choice of an aggressive red outfit for a reason, and I think I should wear that one.) [SisAlessandraPath][SisVeronicaPath]":
            $ reddevil = True
            $ sis_a_p += 2
            $ sis_v_p += 2
            scene e3store13c with mediumdissolve
            sis "Cassandra, I am going to wear this current outfit for the initial meetings, but I want you to save both of them so I can use them at my leisure."
            cass "Right away Mistress [pname3]. I will wrap both outfits for you and take them to the car."
            sis "Thank you, Cassandra."
            jump store2

label store2:

    scene e3store14 with mediumdissolve
    cass "You're very welcome! I'm glad we figured this out so quickly!"
    cass "But don't worry. You have a gigantic clothing allowance! You will be able to get any clothes or accessories you want as you should with your position."
    sis "That sounds great, I still can't believe all of this..."

    stop seven fadeout 3

    scene e3store15 with mediumdissolve
    cass "Believe it, and I hope you embrace it. But...Mistress [pname3], we do need to get moving again right now. A very important person wants to meet you today."
    sis "Who?"
    scene e3store16 with mediumdissolve
    cass "Juliette Karlsson..."
    jump queen

label queen:

    scene e3queen1 with longfade

    play seven "music/temple1.mp3" fadein 2

    $ renpy.pause (4.0, hard=True)

    scene e3queen2 with longfade

    $ renpy.pause (4.0, hard=True)

    scene e3queen3 with longfade
    xx "I'm here. Why did you ask me to come here? Isn't it too soon?"
    queen "Nice costume there."
    xx "You still hide your voice with me, even now. And of course you're not here in person. More speaker fun."
    xx "And by the way, for my look, you're the one who taught me the need for absolute stealth and secrecy for our communications. I thought others might possibly be around."
    scene e3queen4 with mediumdissolve
    queen "Yes of course you're right. I know it's too soon to meet in person, but I really do appreciate you coming here."
    queen "I wanted you to see this temple for yourself today."
    xx "Why?"
    scene e3queen5 with mediumdissolve
    queen "Well Ms. Grym Gudinna, this temple will be where the winner of the Gambit will receive their prize."

    stop seven fadeout 3

    xx "I thought this place was abandoned years ago. I remember being here once when I was a child..."


    scene e3queen6 with longfade

    play seven "<from 8 to 189>music/FarewellAlexander.mp3" fadein 1

    queen "This temple..."

    pause 3

    queen "Your father ensured this temple would be protected and taken care of forever."
    queen "It had special meaning for him. Right here on these steps just outside, he had maybe his only moment of real happiness."
    queen "It was here that he fell in love. But he didn't have the courage to give up his darkness to keep this woman."
    queen "So he lost her. And then he truly lost himself. That reflected in the lack of love he showed to his daughters."
    scene e3queen7 with longfade
    queen "And what kind of daughters will a cruel and sadistic man without love create?"
    xx "I...I...yeah..."
    queen "I know it's impossible for you to believe, but once upon a time, your father was an amazing man full of love and courage."
    queen "You never met that man. He died before you were even born."
    queen "The shell left behind was merely a shadow...and the whole world suffered for it."
    scene e3queen8 with longfade
    queen "But I didn't bring you here for a history lesson. I wanted to update you on what to expect next, and make sure you understand the significance of this place later."
    queen "I want you to study this temple carefully before leaving. There will be trials and tribulations here too. So learn it well and explore the area around it."

    stop seven fadeout 2

    xx "I will."

    scene e3queen9 with mediumdissolve

    play seven "music/temple1.mp3" fadein 3
    queen "In your next Board meeting, a huge part of the Gambit will finally be revealed. Take everything in stride and be patient. A lot depends on [pname],[pname3], and [pname4] too."
    queen "We all have to see how they respond to their situations. But, you are doing an excellent job building allies."
    xx "I am."
    scene e3queen10 with mediumdissolve
    queen "And I think it is safe to say that you probably have three Board votes right now."
    xx "Yes. I agree."
    queen "But probably three against."
    scene e3queen11 with mediumdissolve
    xx "Yes, which leaves..."
    queen "...Elena."
    scene e3queen12 with mediumdissolve
    queen "You must not let her sabotage the Gambit. If it is not deemed fair and feels tainted, it could destroy everything."
    xx "But she knows now...how can she not try to help her own child?"
    queen "I really do understand the temptation. But it's the way your father set it up. I think it's possible Elena gets what she wants without helping as it is."
    scene e3queen13 with mediumdissolve
    queen "But you must ensure that [pname3] is given the chance to run the program well with her own tests, and that [pname] and [pname4] are tested harshly but fairly. That is what is required."
    xx "Elena may suppport us anyway if it turns out..."
    queen "...yes, but that might not happen. We just don't know yet. And...I know how strong the darkness is inside you, but you can always change who you are. Your father doesn't define you."
    scene e3queen14 with mediumdissolve
    xx "I...I don't think I can change who I am...I know I'm an evil person, but I enjoy my life too much right now."
    queen "You never know...you just never know..."
    xx "What will be revealed about the Gambit next?"

    stop seven fadeout 3

    queen "You will learn what your father truly wanted from the person that will inherit his entire empire...for that, you must turn [pname] in your direction...you will see that he is the final key."
    jump elenad

label elenad:

    scene e3elenad0 with longfade

    $ renpy.pause (4.0, hard=True)

    scene e3elenad1 with longfade

    play seven "music/elenadomi.mp3" fadein 3

    d "Elena, are you ready to get going? We need to get to Joy now."
    d "And why did you request to catch a flight with me? You could have gone on Kiyomi's plane only a few hours ago and gotten there early."
    scene e3elenad2 with mediumdissolve
    ec "I'll explain, please hold on. On your knees...get to work cleaning the ground."
    scene e3elenad2b with mediumdissolve
    ec "Dominique, I really want to have a talk with you during the flight. About a lot of things."
    d "Such as?"
    scene e3elenad3 with mediumdissolve
    ec "I know...you don't see eye to eye with me, but I really want to sit down with you and talk."
    d "Of course I don't trust you. You're an evil and selfish bitch, maybe worse than all of my sisters."
    d "And you still haven't told me what you want to discuss."
    scene e3elenad4 with mediumdissolve
    ec "I understand your perception of me. But, you have some information I want, and I think I have something you desire in return."
    ec "I know you don't trust me, so I will in good faith share something useful to you first. I trust you will help me in return."
    scene e3elenad5 with mediumdissolve
    d "That is a leap of faith for you, but how can I know that I want what you have, or even that I can return the favor?"
    ec "You can't yet, but I am confident on both counts. I know you are an honorable woman and will return the favor if what I provide is helpful for you."
    d "Yes, I will. If it's actually helpful, and the value of information being exchanged is a reasonable trade."
    scene e3elenad6 with mediumdissolve
    ec "Fair enough. Here's what I can share with you...you still have a mole at the Swakopmund Mine that is trying to sabotage your operations."
    d "Who?"
    ec "The more interesting issue is who he is reporting to...I can tell you both things, but I want to first know if you can provide what I ask too."
    scene e3elenad7 with mediumdissolve
    d "Alright. What do you want?"
    ec "I understand only you and Veronica have access to all of the surveillance of [pname], [pname3], and [pname4] over the years."
    d "Wait a minute, we've been sharing the most relevant information with everyone. We're not hiding anything."
    scene e3elenad8 with mediumdissolve
    ec "I'm not implying that you are at all. I am just interested in seeing surveillance of their normal activities during their pasts."
    d "Why?"
    ec "I have my reasons, and it's nothing nefarious as you might think. I simply am curious to see moments of how...err...they grew up."
    scene e3elenad9 with mediumdissolve
    d "Or perhaps you think we missed something?"
    ec "No, I really just want to see...them in earlier times."
    scene e3elenad10 with mediumdissolve
    d "That's twice now."
    ec "What?"
    d "You really want to see one person, not all three. I have listened to you speak for years Elena. You are mentally stopping yourself to say they and them instead of he or she."
    scene e3elenad11 with mediumdissolve
    d "What do you really want? And why just one of them? Now you have me very curious."
    ec "I agreed to share information with you, not why I want what I want from you. Are you willing to trade or not?"
    scene e3elenad12 with mediumdissolve
    d "Perhaps I could find the mole myself now that I know one exists, but I will be honorable and trade information. Let's discuss this in detail on the plane..."
    d "...away from your servant here."
    ec "Agreed."
    scene e3elenad13 with longdissolve
    d "Good. It will be nice to get there a little early, so we both can relax a little tonight."
    ec "Sounds great."
    d "By the way, your niece is doing really well under Kiyomi..."
    ec "Good to hear..."

    stop seven fadeout 3

    jump white


label white:

    scene e3white1 with longfade

    play two "<from 70 to 300>music/longhall.mp3" fadein 2

    sis "This is the longest hallway I have ever seen in my life! Is this the only way into the facility?"
    cass "This is the only secure public route into the underground program area. This is to ensure it is impossible for prisoners to escape back outside."
    cass "This hallway is the only way in and out. It has numerous security functions that can incapacitate anyone trying to escape and it's very private and secure."
    cass "You have already seen a little of the above ground facilities like your private theater and office, but this area is very restricted for obvious reasons."
    sis "So we're going to have to walk this long hallway every day to go below?"
    scene e3white2 with longdissolve
    cass "Actually, you have an alternate route from directly above only for executives. But, if you need to use this hallway, we will have golf carts to transport people during operating hours."
    cass "Most of the prisoners should be arriving tonight, so security should be heavy here in a few hours. I will have you meet the Security Chief when she arrives."
    scene e3white3 with mediumdissolve
    cass "By the way, it sounds like we may have about roughly fifteen participants."
    cass "Your orientation materials will have detailed profiles on each of the prisoners."
    sis "Ok."
    scene e3white4 with mediumdissolve
    sis "And what's this?"
    cass "Ah, this is a security system to allow entry. You place your eyes and hand on each sensor and it will scan your identity for elevator access to the facility."
    cass "In fact, let's test your identity now. Go ahead and see if it works."
    scene e3white5 with mediumdissolve
    sis "Here we go..."
    anne "{i}Identity confirmed. Welcome [pname3] [pname_f], Senior Executive Vice President of The Karlsson Group and current Head Warden of The Joy Facility.{/i}"
    sis "(The Joy Facility??)"
    scene e3white6 with mediumdissolve
    cass "This is A.N.N.E. and the letters for her name stand for Advanced Neural Network Entity. She is one of the most advanced artificial intelligence programs in the world."
    cass "You will find her invaluable for your work, as she controls numerous functions within this facility."
    scene e3white7 with longdissolve
    cass "Let's head down to the basic prisoner wing first. Now about Juliette...would you like some advice and info on her, or would you rather get your own first impression?"
    menu:
        "(I bet Cassandra has useful information about her. I should utilize her as often as I can if she can be helpful.) [SisCassPath]":
            $ sis_c_p += 1
            scene e3white7b with mediumdissolve
            sis "As my Executive Assistant, I absolutely would value your input ahead of time. Anything you can tell me about her would be helpful."
            if cassandraloyal:
                cass "You have to strike a delicate balance with her. You need to show confidence and strength because if she senses weakness she will bully and push you around."
                cass "But you also don't want to say or try and show that you are actually stronger than her, at least on the surface. She will feel threatened and react negatively towards you."
                jump white2
            else:
                cass "You can't let her push you around. Show some confidence and strength because if she senses weakness she will bully you."
                jump white2
        "(I wouldn't mind Cassandra's advice, but maybe I need to form my own impression first when meeting her. It might be a risk to meet her this way, but I think I want do to that.) [SisDomPath]":
            $ sisdom += 1
            scene e3white7c with mediumdissolve
            sis "I appreciate the offer Cassandra, but I think I want to get my own first impressions about her with no preconceived notions or prior information."
            sis "But I do want you to offer to share advice as often as you can, I do appreciate it."
            cass "Of course Mistress [pname3], I completely understand why you want to meet Juliette that way."
            jump white2

label white2:

    scene e3white8 with mediumdissolve

    stop two fadeout 3

    cass "Here we go..."
    jump pod

label pod:

    scene e3pod1 with longfade

    play seven "music/jail.mp3" fadein 2

    cass "So this area is Level 3 of 5, where the prisoners are housed. We have five pod rooms, and each pod holds six little cells."
    cass "Level 3 is quite secure with numerous protective safeguards, and clients are typically allowed only on Level 2 where the majority of activity will take place."
    scene e3pod2 with mediumdissolve
    sis "The cells are quite tiny. Do they come with anything else at all like a bed?"
    cass "These cells are for K4 rated prisoners, so they are given nothing for comfort at all. Higher rated prisoners do receive beds and other amenities in different cells."
    sis "How do they even go to the bathroom?"
    scene e3pod3 with mediumdissolve
    cass "They have a few chances at different times, but if they are stuck in there and have to go...I guess they have to beg a guard or just do it in there, haha!"
    cass "We place two prisoners per cell in these pods. We don't like to give anyone privacy with their own cell as that right is for higher ranked prisoners only."
    scene e3pod4 with mediumdissolve
    sis "And how many prisoners coming are K4 and other ranks? From my initial glance at my orientation materials, I read that they all start between K4 and K6?"
    if k4:
        cass "Almost every prisoner coming is a K4, along with one K5. Of course, you already know that [pname] is coming as a K4."
        sis "Yes."
        jump pod2
    elif k5:
        cass "Almost every prisoner arriving is a K4, although there are two K5s as well. [pname] being one of them is a pretty big accomplishment Mistress [pname3]."
        sis "I suppose so with that breakdown."
        jump pod2
    elif k6:
        cass "Almost every prisoner arriving is a K4, but we do have one K5 and one K6 coming as well. [pname] being K6 is a big deal Mistress [pname3]! That's very hard to do!"
        sis "I believe it seeing that everyone else is below him to start the program."
        jump pod2
    else:
        cass "Almost every prisoner coming is a K4, along with one K5. Of course, you already know that [pname] is coming as a K4."
        sis "Yes."
        jump pod2

label pod2:

    scene e3pod5 with mediumdissolve
    cass "Let's get up to Level 2 and have you see Juliette now. I think she is in one of the stage rooms above us."

    stop seven fadeout 3

    sis "Sounds good."

label nightclub:

    scene e3nightclub1 with longfade
    cass "Hmm, she isn't here. Really quickly Mistress, this is a little night club style room where patrons can have some fun. We are still adding furniture and other things."
    sis "Oh, very nice."
    cass "Let's find Juliette."

label stagea:

    scene e3stagea1 with longfade
    cass "Shit, oops sorry for being unprofessional Mistress, she's not here either. A little display room where patrons can inspect prisoners up close...I can go over this more later."
    sis "Ok..."

label stageb:

    scene e3stageb1 with longfade

    play seven "music/ojmeet.mp3" fadein 3

    cass "Mistress Juliette! We're here!"
    j "It's about time! What took you so long!"
    cass "I'm sorry, I was just showing Mistress [pname3] around and..."
    scene e3stageb2 with quickdissolve
    j "Save it. Now get out. I want to meet [pname3] alone."
    cass "Mistress Juliette?"
    scene e3stageb3 with mediumdissolve
    j "You dare make me repeat myself? You heard me. Now!"
    cass "Yes Mistress!"
    scene e3stageb4 with longfade
    j "Welcome [pname3], I'm so happy to finally meet you. I've been looking forward to it. As I am sure you have deduced by now, my name is Juliette Karlsson."
    sis "Thank you, nice to meet you. Is there a particular way you want me to address you, since you are one of my bosses?"
    scene e3stageb5 with mediumdissolve
    j "Oh no! Just use my name, that kind of formality is for the lessers amongst us. You have to always remind the little people of their lot in life."
    j "Even Cassandra. I actually adore her, but she's just the best of the cockroaches that have crawled up to their own little top. But she can never be like me...and I hope you."
    scene e3stageb6 with mediumdissolve
    j "Now come on up on the platform here, this will be a very important part of your job very soon."
    sis "Sure."
    scene e3stageb7 with longfade
    sis "(Glad I am tall...no stairs up to here...)"
    j "So one thing you will be expected to do early is host a little show here where people can view the prisoners ahead of the fun and games. You need to be a great hostess and have fun with it!"
    sis "Like a fashion show?"
    j "In a sense. But they will be mostly naked. You will be expected to give them some discomfort and pain to liven it up at times, but we can get more specific later."
    scene e3stageb8 with mediumdissolve
    j "This will include of course [pname]. How do you feel about that?"

    stop seven fadeout 3

    sis "(I wonder how many times I will be asked about this...it has to be important overall to everything...how I handle [pname]...but definitely foolish to say I want to protect him.)"
    menu:
        "(I think I shouldn't say anything about being protective of [pname] on my end, but I can at least show confidence that he can survive this situation ok.) [SisBroPath]":
            $ sis_bro_p += 1
            scene e3stageb8b with mediumdissolve
            sis "He'll have to do his best like anyone else, but I think he is a pretty strong guy and might survive just fine."
            j "Hmm, you don't even know what we have in store for everyone yet, but let's see if you end up right. I do hope you won't treat him better than the others."
            jump stagebtwo
        "(I don't think it hurts to say it might be a little awkward having [pname] here, but I can still say I will treat everyone the same.) [SisVeronicaPath]":
            $ sis_v_p += 1
            scene e3stageb8c with mediumdissolve
            sis "I can't lie. It might be a little awkward, but I have a job to do and will treat everyone the same."
            j "I certainly hope so, it's very important that you don't play favorites."
            jump stagebtwo
        "(I need to show that I won't be soft on [pname] if necessary and Juliette might like that too. I'm supposed to be managing prisoners and there is no doubt punishment will be part of my job description.) [SisJuliettePath]":
            $ sis_j_p += 1
            scene e3stageb8d with mediumdissolve
            sis "[pname] is just a prisoner like anyone else here. I know I might have to punish him. If he gets out of line...I will."
            j "I'm so happy to hear you say that [pname3]! Now I want to make sure [pname] does something wrong just so I can see you in action!"
            jump stagebtwo

label stagebtwo:

    scene e3stageb9 with longdissolve

    play seven "music/stage222.mp3" fadein 3

    j "Tomorrow, you will formally start your duties as Warden of this facility. There will be a whirlwind of things to learn, but rest assured we will get you ready."
    sis "I have read up on some of my stuff, but I could use a little more time tonight if possible."
    j "Of course. Don't fret too much about knowing everything right away. Just focus on being ready to meet the prisoners first, the entire Board has great hope for you."
    scene e3stageb10 with mediumdissolve
    j "But I also wanted to give you a welcome gift for your new position here. Come with me."
    sis "(I wonder what this could be...)"
    j "Come on out!"
    scene e3stageb11 with longfade
    j "Now get on your knees you pathetic shitstain. Your day of reckoning has arrived. And don't make a sound of any kind until I say so."
    sis "Wait! I think I recognize him, is that??? And his hair is pink?"
    scene e3stageb12 with mediumdissolve
    j "Yes. This is Daniel, the nice man who tried to get you fired from your dead end job when you turned him down for a date. I changed his hair color since he hates pink so much, haha!"
    j "You weren't very nice to [pname3] were you? You first tried to take advantage of her, and then you tried to ruin her livelihood. Now look at you...tsk tsk Danny boy..."
    scene e3stageb13 with mediumdissolve
    sis "Wait, how do you even know about this? This happened a few years ago."
    j "[pname3], do you think you would even be here if you had not been watched for quite a while? You've been observed for a long time..."
    scene e3stageb14 with mediumdissolve
    sis "How long?"
    j "Long enough...but let's worry about what we are going to do with your gift here! I think he really needs to pay for trying to ruin your life."
    j "Without that job, and how hard it is to find work out there...maybe you could have been homeless and starving..."
    scene e3stageb15 with mediumdissolve
    j "That would have been such a painful and slow process...maybe he needs the same kind of punishment..."
    j "Hmm, what ever shall you do with him?"
    scene e3stageb16 with mediumdissolve
    j "I can give you some suggestions if you would like [pname3], just to give you a hint of what you can do to anyone under your power here."
    sis "Actually, I would appreciate some options."
    sis "(It's probably pretty safe to pick any of her suggestions unless she is trying to trap or trick me...)"
    scene e3stageb17 with mediumdissolve
    j "Let's have him beg you for mercy first though. It might make it easier to discuss ideas."
    j "So go ahead Daniel! Now I give you permission to speak! Maybe [pname3] is nicer than I am. You know if it was me you would be suffering so much..."
    scene e3stageb18 with mediumdissolve
    dan "Please [pname3]! There is no way I deserve this! I admit...I...I did try to get you fired, but this woman is crazy! She gets off on seeing me suffer and..."
    j "I don't think [pname3] needs to hear about our time together. You need to focus on convincing her to punish you lightly."
    scene e3stageb19 with mediumdissolve
    dan "Yes, I'm sorry! Please have mercy, this is way beyond what I deserve! I just want to be left alone..."
    j "Hmm, [pname3], I have to give you one order right now. I promise it won't be a habit if you can take care of yourself."
    sis "What do you want me to do?"

    stop seven fadeout 3

    scene e3stageb20 with mediumdissolve
    j "I need you to let this pitiful excuse for a man lick your pussy so you can decide his fate under a more...pleasurable state of mind. He has had a little...training recently for that task."
    j "Just relax and enjoy it...while you think about what to do..."
    sis "(This doesn't seem optional...way too early to test defying her...)"
    j "Get in there Daniel, show how much you've learned."
    scene e3stageb21 with longfade

    play seven "music/oliviaeaten.mp3" fadein 2

    j "So how is he [pname3]?"
    sis "Ohhh, not bad..."
    scene e3stageb22 with longdissolve
    sis "Not too bad at all..."
    scene e3stageb23 with longdissolve
    j "I wonder if you are feeling a little more merciful now that he's servicing you? Or maybe it's more pleasure for you knowing you are going to punish him anyway?"
    j "And [pname3]...you can do anything you want if you play your cards right..."
    scene e3stageb23b with longdissolve
    j "You can just throw anyone away when you feel like it...and get another...and another...and another...again...and again...anytime you want."
    scene e3stageb24 with longdissolve
    j "Feel how eagerly he is licking you...the desperation of a man fighting for his survival...he's scared and helpless not knowing what you will do...he is completely at your mercy."
    scene e3stageb24b with longdissolve
    j "I like to imagine what I am going to do to someone afterwards while they are pleasing me...knowing their efforts will make no difference gets me off even more..."
    scene e3stageb25 with longdissolve
    j "But are you different? What will you do with him after you get off? You could just lock him in a cell and throw away the key...you could make him a human pet or even toilet..."
    scene e3stageb25b with longdissolve
    j "Maybe turn him into human furniture in your office or home...forever stuck and watching you silently...or just give him to all of our guards to have fun with him over and over..."
    if sisevil >= 7:
        j "You could even have him killed...right in front of you...quickly with a single word that would shock his heart...or a slow and painful one too...embrace what we are offering you..."
    else:
        j "You can do anything you want...embrace what we are offering you..."
    scene e3stageb26 with mediumdissolve
    j "You can even free him. I won't stop you if that's what you want."
    scene e3stageb27 with mediumdissolve
    sis "Oh my God, I'm going to!!!"
    scene e3stageb28 with longflash
    sis "Oh yes!!"

    stop seven fadeout 3

    scene e3stageb29 with longdissolve
    j "Good...now you get down on the floor Dickless Daniel..."
    dan "Ugh!"
    scene e3stageb30 with longfade
    j "Savor how it felt...I hope you enjoyed my welcome gift."
    sis "(Ahhh, what a great orgasm...)"

    play seven "music/oliviachoice.mp3" fadein 3

    j "But, I do need you to focus now [pname3]. I was quite serious when I said that you have to decide Daniel's fate."
    scene e3stageb31 with mediumdissolve
    j "So now let me help you with some options."
    if sisevil >= 7:
        jump evilmenu
    else:
        jump goodmenu

label evilmenu:
    j "My suggested punishments are locking him in a cell for a very long time, using him as a human pet, a human toilet, or human furniture for your amusement."
    scene e3stageb31b with mediumdissolve
    j "The most extreme option is you can even have him killed. There is a kill command attached to one of the chips embedded in his body, it will instantly shock his heart and cause death."
    j "I guess this is your very first decision as Head Warden of our wonderful Joy Facility."
    sis "(I better consider my first major decision carefully...)"
    menu:
        "(I do want to punish him, but I think just locking him up for now is a safe option. Plus, if I do that, I can always change my mind later too.) [gr]\[DanielJailed\]":
            $ danieljailed = True
            $ sis_v_p += 1
            scene e3stageb31c with mediumdissolve
            sis "Juliette, I think I want to lock him up in a cell for now. He needs some time to think about what he did to me."
            dan "Please [pname3]! Please..."
            j "If you speak again Daniel, I will just kill you myself...shhhh..."
            scene e3stageb31d with mediumdissolve
            j "I actually do hope you change your mind to something more vicious later, but he's under your charge. We'll do what you want."
            j "So I hope you enjoy your new cell Daniel! Now come [pname3], let's meet Cassandra and get you more ready for tomorrow..."
            stop seven fadeout 2
            jump clinic
        "(A human pet?? It sounds so strange, but the thought of having Daniel trapped in a cage for my amusement is somehow exciting to me...) [gr]\[DanielPet\]":
            $ danielpet = True
            $ sis_d_p += 1
            scene e3stageb31e with mediumdissolve
            sis "Juliette, I think I want to turn him into a human pet. That seems like a fun way to punish poor Daniel."
            dan "Please [pname3]! Don't...please..."
            j "If you speak again Daniel, I will just kill you myself!"
            scene e3stageb31d with mediumdissolve
            j "I was hoping you would be a little more vicious, but you are in charge of him. We will make him a nice little pet for you."
            j "Poor Daniel, I hope you can be a good little puppy for your new Mistress. Now [pname3], let's take care of this and then go meet Cassandra and get you more ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(A human toilet? It seems so strange and can I really piss and...oh maybe it's disgusting...but even so it sounds exciting to me. Maybe I want to do that as a punishment.) [gr]\[DanielToilet\]":
            $ danieltoilet = True
            $ sis_d_p += 1
            scene e3stageb31g with mediumdissolve
            sis "Juliette, I can't help but be excited at the thought of turning him into a human toilet. That seems like a very good punishment for poor Daniel."
            dan "Please [pname3], you can't be serious? A fucking toilet?! That's just..."
            j "...silence Daniel! If you speak again, I will just kill you myself. Toilets don't get to talk anyway, so be quiet!"
            scene e3stageb31h with mediumdissolve
            j "I was hoping you would be a little more vicious, but this is certainly a very humiliating and cruel punishment. It is your decision, so a toilet he shall be!"
            j "Poor Daniel, I bet it's going to feel soooo good being at the bottom of Olivia's toilet needs, hahaha! So pitiful...but it's where you belong I guess."
            j "Now [pname3], let's take care of this and then meet Cassandra. We need to get you more ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(Human furniture?? I don't even know what that exactly entails...but the thought of him just trapped and suffering while I can just relax is...exciting) [gr]\[DanielFurniture\]":
            $ danielfurniture = True
            $ sis_j_p += 1
            $ sis_a_p += 1
            scene e3stageb31i with mediumdissolve
            sis "Juliette, I'm not too familiar with this, but the thought of him being a piece of human furniture seems like a very fitting punishment."
            dan "Wait, what? Please, you can't...!"
            j "Be quiet Daniel, or I will just kill you myself! And [pname3]! I am genuinely surprised you picked that option. I can't wait to show you what we can do with him..."
            scene e3stageb31h with mediumdissolve
            j "I will turn him into a wonderful piece of furniture for you, haha! Now, we should get poor Daniel ready for that...and then meet Cassandra, as we need to get you ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(I...I want to go all the way and embrace my power. I want him killed...and maybe it shows strength and ruthlessness to Juliette and others...) [gr]\[Murderess\]":
            $ murderess = True
            $ sisgambitqueen -= 2
            $ julietteworried = True
            scene e3stageb31k with mediumdissolve
            sis "Juliette, I think he needs the ultimate punishment. I want him killed."

            stop seven fadeout 2

            dan "What?? [pname3], you can't be serious! Oh my God...please please!!!!"


            scene e3stageb31l with mediumdissolve

            play seven "music/death1.mp3" fadein 2

            dan "Wait, don't!!!"
            j "I'll make it very quick since it's your first time [pname3]...Daniel, Killswitch Karlsson 555."
            dan "Arrgggh! uck......."
            scene e3stageb31m with longfade
            j "Very ruthless of you [pname3], I'm surprised you could do this so quickly. You are much more than I expected, especially so early."
            scene e3stageb31o with mediumdissolve
            j "I'll have someone take away this trash, but we should meet Cassandra and continue to get you ready for tomorrow."
            stop seven fadeout 2
            jump clinic

label goodmenu:
    j "My suggested punishments are locking him in a cell for a very long time, using him as a human pet, a human toilet, or even human furniture for your amusement."
    scene e3stageb31b with mediumdissolve
    j "Of course, as I said before, you can always be merciful and allow him to leave here a free man."
    j "I guess this is your very first decision as Head Warden of our wonderful Joy Facility."
    menu:
        "(I do want to punish him, but I think just locking him up for now is a safe option. Plus, if I do that, I can always change my mind later too.) [gr]\[DanielJailed\]":
            $ danieljailed = True
            $ sis_v_p += 1
            scene e3stageb31c with mediumdissolve
            sis "Juliette, I think I want to lock him up in a cell for now. He needs some time to think about what he did to me."
            dan "Please [pname3]! Please..."
            j "If you speak again Daniel, I will just kill you myself. Shhhhh..."
            scene e3stageb31d with mediumdissolve
            j "I actually do hope you change your mind to something more vicious later, but you are in charge of him. We will do what you want."
            j "So I hope you enjoy your new cell Daniel! Now come [pname3], let's meet Cassandra and get you more ready for tomorrow..."
            stop seven fadeout 2
            jump clinic
        "(A human pet?? It sounds so strange, but the thought of having Daniel trapped in a cage for my amusement is somehow exciting to me...) [gr]\[DanielPet\]":
            $ danielpet = True
            $ sis_d_p += 1
            scene e3stageb31e with mediumdissolve
            sis "Juliette, I think I want to turn him into a human pet. That seems like a fun way to punish poor Daniel."
            dan "Please [pname3]! Don't...please..."
            j "If you speak again Daniel, I will just kill you myself!"
            scene e3stageb31d with mediumdissolve
            j "I was hoping you would be a little more vicious, but you are in charge of him. We will make him a nice little pet for you."
            j "Poor Daniel, I hope you can be a good little puppy for your new Mistress. Now [pname3], let's take care of this and then go meet Cassandra and get you more ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(A human toilet? It seems so strange and can I really piss and...oh maybe it's disgusting...but even so it sounds exciting to me. Maybe I want to do that as a punishment.) [gr]\[DanielToilet\]":
            $ danieltoilet = True
            $ sis_d_p += 1
            scene e3stageb31g with mediumdissolve
            sis "Juliette, I can't help but be excited at the thought of turning him into a human toilet. That seems like a very good punishment for poor Daniel."
            dan "Please [pname3], you can't be serious? A fucking toilet?! That's just..."
            j "...silence Daniel! If you speak again, I will just kill you myself. Toilets don't get to talk anyway, so be quiet!"
            scene e3stageb31h with mediumdissolve
            j "I was hoping you would be a little more vicious, but this is certainly a very humiliating and cruel punishment. It is your decision, so a toilet he shall be!"
            j "Poor Daniel, I bet it's going to feel soooo good being at the bottom of Olivia's toilet needs, hahaha! So pitiful...but it's where you belong I guess."
            j "Now [pname3], let's take care of this and then meet Cassandra. we need to get you more ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(Human furniture?? I don't even know what that exactly entails...but the thought of him just trapped and suffering while I can just relax is...exciting) [gr]\[DanielFurniture\]":
            $ danielfurniture = True
            $ sis_j_p += 1
            $ sis_a_p += 1
            scene e3stageb31i with mediumdissolve
            sis "Juliette, I'm not too familiar with this, but the thought of him being a piece of human furniture seems like a very fitting punishment."
            dan "Wait, what? Please, you can't...!"
            j "Be quiet Daniel, or I will just kill you myself! And [pname3]! I am genuinely surprised you picked that option. I can't wait to show you what we can do with him..."
            scene e3stageb31h with mediumdissolve
            j "I will turn him into a wonderful piece of furniture for you, haha! Now, we should get poor Daniel ready for that...and then meet Cassandra, as we need to get you ready for tomorrow."
            stop seven fadeout 2
            jump clinic
        "(I...I can't just punish him in one of these ways. He really didn't hurt me at all since he failed. I think I am going to let him go and hope showing mercy can be a positive here.) [gr]\[Morality\]":
            $ moralitytwo = True
            $ sisgambitqueen += 2
            scene e3stageb31n with mediumdissolve

            stop seven fadeout 2
            sis "You know Juliette, he really didn't hurt me at all in the end since he failed. I think I'm just going to let him go as I think he's learned his lesson."

            play seven "music/forgive.mp3" fadein 2

            dan "Oh my God, thank you [pname3]! I am so sorry about everything, and I'm so thankful you..."
            j "Enough blubbering Daniel! Get in the back and wait there. I'll arrange for you to leave here soon."
            scene e3stageb31p with mediumdissolve
            j "[pname3], I am surprised you didn't punish him at all. However, I did place him under your power and will respect your decision. I hope you aren't too soft on the prisoners."
            j "Still...we should go see Cassandra and get you ready for tomorrow. Let's go..."
            stop seven fadeout 2
            jump clinic

label clinic:

    if k5 or k6:
        jump clinicb
    else:
        jump clinica

label clinica:

    scene e3clinica1 with longfade
    p "(It's been a while since I heard someone take out [pname2] and Zach from their boxes.)"
    scene e3clinica2 with mediumdissolve
    p "(Are they just going to leave me in here?)"
    scene e3clinica3 with mediumdissolve

    play seven "music/kiyomiplane.mp3" fadein 3

    p "(Wonderful...another shining moment in my life...)"
    scene e3clinica4 with mediumdissolve
    ky "Time to come out there [pname]."
    ky "I have a few things you need to wear, so I suggest you cooperate for your own good."
    scene e3clinica5 with mediumdissolve
    ky "Welcome to your new home."
    p "Who are you? And where are we?"
    scene e3clinica6 with mediumdissolve
    ky "My name is Kiyomi, and ask someone else further questions. And...don't be foolish and test me. I don't need to use a shock to deal with you instantly."
    p "(Shit...I think I believe her, she seems very...dangerous.)"
    ky "I'll take you to your check-in room where you'll do a physical examination. Come on out."
    scene e3clinica7 with longfade
    ky "Good. Now let's get moving."
    p "(Why make me wear this?)"
    scene e3clinica8 with longfade
    ky "[pname], I will be the lead trainer for all of you during your stay here."
    p "Training for what?"
    scene e3clinica9 with mediumdissolve
    ky "For..."
    scene e3clinica10 with mediumdissolve
    ky "...learning to take care of yourself among other things."
    scene e3clinica10b with mediumdissolve
    p "(Oh shit, did she trip me on...!)"
    scene e3clinica11 with mediumdissolve
    p "(Ugh!)"
    ky "In the future, you'll be able to prevent me from doing that to you again. If you listen well."
    ky "It can be do or die in here. So you might want to carefully listen to everything I say. Now get up."
    scene e3clinica12 with longfade
    ky "Almost there [pname]..."
    scene black with longfade
    ky "We're here. Let's get your eyes uncovered."

    stop seven fadeout 3

    scene e3clinica13 with longfade
    ky "This is a medical checkup room where they will process you formally into this program. I'll take your cuffs too now since you are here."
    if busyboy:
        ky "I have to run now, so good luck. It's a shame you decided to serve Scarlett and Junko so quickly. You didn't even see all the other options out there..."
        p "(Oh...)"
        ky "Until the next time [pname]."
        jump clinicatwo
    elif scarlettpeg:
        ky "I have to run now, so good luck. It's a shame you have already capitulated to Scarlett. Maybe you missed another opportunity out there..."
        p "(Oh...)"
        ky "Take care [pname]."
        jump clinicatwo
    elif junkopet:
        ky "I have to run now, so good luck. It's a shame you wanted to be Junko's pet so badly. Maybe you missed another opportunity out there..."
        p "(Oh...)"
        ky "Take care [pname]."
        jump clinicatwo
    elif freeagent:
        ky "I have to run now, but I think I will see you again very soon. I am pleased you turned down both Scarlett and Junko's offers."
        p "(Oh...)"
        ky "Take care [pname]."
        jump clinicatwo
    else:
        ky "I have to run now, so good luck [pname]."
        jump clinicatwo

label clinicatwo:

    scene e3clinicatwo1 with longfade
    p "(Well, I guess I just wait...)"
    scene e3clinicatwo2 with longfade
    v "Well, it appears you are one of the last arrivals [pname]."

    play seven "music/clinica3.mp3" fadein 2

    v "Welcome to the Joy Facility. My name is Veronica Karlsson."
    p "(Joy Facility?)"
    scene e3clinicatwo3 with mediumdissolve
    v "You are not dealing with a guard or servant here, so I expect you to listen very carefully and follow every instruction precisely."
    v "Any lack of complete obedience on your part will result in punishment. Do you understand?"
    menu:
        "(She seems all business and she's maybe at the very top of the food chain here. I better be very to the point and just say yes.)":
            $ veronica_scale -= 1
            scene e3clinicatwo3b with mediumdissolve
            p "Yes, I understand."
            v "Very good. You should also get used to calling everyone above you Mistress."
            v "I'll let it go this first time since you literally just arrived. Let's proceed to your physical examination."
            jump clinicathree
        "(I doubt I can just disobey her, but maybe I need to try and at least show a little strength in how I answer. Maybe I should be a little passive aggressive in my tone.)":
            $ veronica_p -= 2
            scene e3clinicatwo3c with mediumdissolve
            p "Yes, whatever you say."
            v "Perhaps some of our staff are too stupid to notice subtle things from you, but I am not of them. That kind of attitude will only cause great suffering for you."
            v "You should also get used to calling everyone above you Mistress. Let's proceed to your physical examination."
            jump clinicathree
        "(I better just answer yes, but maybe I can ask permission to ask a question too.) [VeronicaPath]":
            scene e3clinicatwo3d with mediumdissolve
            p "Yes, I understand. Is it ok if I ask a question?"
            v "Why yes [pname], I certainly don't mind, but I can't promise you will receive an answer. What do you want to ask?"
            menu:
                "(I should just ask her bottom line what the program actually does, and what I can expect.) [red]\[VeronicaScale -1\]":
                    scene e3clinicbtwo4b with mediumdissolve
                    $ veronica_scale -= 1
                    p "This prisoner rehabilitation program. Can you just tell me what it exactly entails?"
                    v "You'll have to wait on that. Be patient, answers will be forthcoming as the days proceed. Let's get to your physical examination."
                    p "(It was worth a try.)"
                    jump clinicathree
                "(I doubt she will divulge information so quickly or easily. Maybe I should ask her about herself.) [VeronicaPath]":
                    scene e3clinicbtwo4c with mediumdissolve
                    $ veronica_p += 2
                    p "I'm sure you already know a lot about me. Would you mind telling me a little about yourself?"
                    v "Interesting question. You didn't ask me about the program or what you will be doing in this room."
                    p "I figure I'll find that out soon enough without having to ask you. But I might not get another chance to ask you this kind of question."
                    scene e3clinicbtwo4d with mediumdissolve
                    v "Excellent thought process. I'm a little surprised now that you tested at K4. I can at least share a very tiny bit about myself."
                    v "I'm the second oldest of my sisters, and I am generally a quiet and reserved person. My favorite activities are reading and basically doing experiments."
                    v "I am a scientist and inventor, and greatly enjoy my work."
                    p "What have you invented?"
                    scene e3clinicbtwo4e with mediumdissolve
                    v "Oh, many, many things. But I think that is a discussion for another time. We must get to your physical examination."
                    p "(She oozes intelligence, but something seems funny about her too. She also seems familiar to me somehow.)"
                    jump clinicathree
                "(I should ask about her the immediate business at hand. Why am I in this room?) [red]\[VeronicaScale -1\]":
                    scene e3clinicbtwo4f with mediumdissolve
                    $ veronica_scale -= 1
                    p "Why am in this room? It seems more like a medical room versus say a place to check in..."
                    v "Quite a reasonable if not predictable question. We have to give you a very short physical examination as your first step here upon arrival."
                    v "Let's proceed."
                    jump clinicathree


label clinicathree:

    scene e3clinicathree1 with longfade
    v "Now, I'll need you to remove all of your clothing [pname]. My assistant, Nurse Reyes, will store your clothes for now."
    v "I'll come out there too after I adjust some settings in here that we will be using for your exam."
    scene e3clinicathree2 with longfade
    v "Nurse Reyes, please help the prisoner undress."
    nurse "Yes, Mistress Veronica."
    scene e3clinicathree3 with mediumdissolve
    nurse "My name is Nurse Reyes, I'll be assisting Mistress Veronica."
    p "(Oh sure, this seems like a normal nurse...)"
    scene e3clinicathree4 with mediumdissolve
    v "[pname], Nurse Reyes will be giving you a shot that will allow us to examine you better."
    v "Cooperate fully and there will be no need for a shock or other punishment."
    nurse "Hurry up loser. Strip. I'll take your clothes for now and be right back."
    scene e3clinicathree5 with longfade
    nurse "Are you ready Mistress?"
    v "Yes, I'm coming out now."
    scene e3clinicathree6 with longdissolve
    nurse "Get on your knees and then hold out your right arm so I can give you this shot."
    p "Why do I have to kneel?"
    nurse "Because I like looking down at a worthless man like you while I do it. Now get down."
    scene e3clinicathree7 with mediumdissolve
    p "(...)"
    nurse "Ahhh, there we go."
    scene e3clinicathree8 with mediumdissolve
    nurse "You know...if you beg me, I might the make shot much less painful for you."

    stop seven fadeout 3

    menu:
        "(Maybe she'll actually do what she says if I do beg. Why not?) [red]\[NurseScale -1\]":
            $ nurse_scale -= 1
            scene e3clinicathree8b with mediumdissolve
            p "Alright...please make my shot less painful. I beg of you."
            nurse "That was actually kind of a pathetic beg. But I'll do it slightly quicker for you."
            jump clinicafour
        "(I'm not going to give her the satisfication. She might do the exact same thing anyway.)":
            scene e3clinicathree8c with mediumdissolve
            p "No, that's fine. Go ahead and give the shot."
            nurse "Ah, maybe there is a tiny speak of a strong man in there. But the shot is still going to hurt."
            jump clinicafour

label clinicafour:

    scene e3clinicafour1 with longdissolve

    play seven "music/clinicafour3.mp3" fadein 3

    nurse "The middle part of your arm is fine. There you go."
    p "(Wow, that does hurt!)"
    scene e3clinicafour2 with mediumdissolve
    v "Try and stay still a few seconds in case you get dizzy."
    p "I'm feeling very dizzy, I think I need to lie down."
    scene e3clinicafour3 with mediumdissolve
    v "Go ahead and lie down slowly [pname]. Reyes, can you put the needle in my office and take my shoes too. I think I'd like them off right now."
    nurse "Yes, Mistress."
    scene e3clinicafour4 with longfade
    v "What are you feeling now [pname]? Describe it as specifically as you can if possible."
    p "I feel lightheaded, but my body also feels extremely sensitive. It's hard to describe."
    v "I understand. It seems your dick has woken up too."
    scene e3clinicafour5 with mediumdissolve
    p "But it feels funny. It feels...backed up somehow painfully."
    nurse "Shall we try and move him up now Mistress?"
    scene e3clinicafour6 with mediumdissolve
    v "No, I want to test something first. Let me just..."
    scene e3clinicafour7 with mediumdissolve
    v "...get on top of him."
    p "Aggghh, that really hurts!"
    v "Yes, it should. Your body is quite sensitive to pain now. Even normal physical touch can stimulate your pain receptors to respond at a very high level."
    scene e3clinicafour8 with mediumdissolve
    v "As part of checking in to our facility, you need to learn your first lesson [pname]."
    v "Our current positions are the nature of your reality right now. You're like a little worm crawling in the mud trying to survive."
    scene e3clinicafour9 with mediumdissolve
    v "While someone like me can walk above and even on you comfortably to stay clean from the mud without a care in the world."
    v "And every little speck of mud that actually touches me has to be licked off by a lesser being like you."
    scene e3clinicafour10 with mediumdissolve
    v "It's up to you to change your destiny, but right now, you only get to crawl."
    v "I think he is ready to be moved Nurse Reyes."
    nurse "Yes, Mistress."
    scene e3clinicafour11 with mediumdissolve
    nurse "I think you should be able to stand up now [pname]."
    nurse "Give it a try...slowly."
    scene e3clinicafour12 with mediumdissolve
    nurse "There we go. You can lie down much more comfortably here than on the floor."
    nurse "We just want to test one thing as we check you into the program [pname]."
    scene e3clinicafour13 with longfade
    nurse "There there, doesn't it feel so much better here? Nice and comfortable for your back."
    p "No, my whole body actually feels so sensitive and everything hurts a little."
    scene e3clinicafour14 with mediumdissolve
    nurse "Oh no, you poor baby. Pooor poooor baby. Can I get more comfortable Mistress?"
    v "Fine. But don't get distracted from being on task by trying to get off. Just test his dick so we can finish. I have quite a bit to do after we're done here."
    scene e3clinicafour14b with longdissolve
    nurse "Starting now Mistress."
    nurse "Let's just try this...how does it feel [pname]?"
    scene e3clinicafour15 with mediumdissolve
    p "Oh my...it hurts a lot! How can just that cause so much pain??!?"
    nurse "Let me just get comfortable here...and squeeze it a little harder."
    scene e3clinicafour16 with mediumdissolve
    p "Arrrgh, please! The pain...it's!! Please..."
    scene e3clinicafour17 with mediumdissolve
    p "Please stop!"
    scene e3clinicafour18 with mediumdissolve
    v "[pname], can you describe the feeling of pain on a scale of one to ten. I suggest you answer clearly to make this experience a shorter one."

    stop seven fadeout 3

    menu:
        "(It feels like a seven out of ten, it really hurts! But maybe I should say five to not sound too weak.) [gr]\[ToughPain\]":
            $ toughpain = True
            p "It hurts, it's like a five out of ten!"
            v "Curious answer. No one else has responded that way. It might speak to your pain tolerance, but more likely it says something about your mind."
            jump clinicafive
        "(It feels like a seven out of ten, it really hurts! I think I better just answer honestly on this one!) [VeronicaPath]":
            $ veronica_p += 1
            p "It hurts. A lot! It's about a seven out of ten."
            v "Good. I believe you. I appreciate honest feedback, and am very fair and do reward useful prisoners to me. Keep that in mind."
            jump clinicafive
        "(It feels like a seven out of ten, it really hurts! I think I should say it's like a nine out of ten, maybe they will take it easier on me then...)":
            $ weakpain = True
            p "It hurts a lot! It's like a nine out of ten!"
            v "Really? Your answer is a curious one. I'm not sure if it speaks to your pain tolerance or your mind, but I'll find out. [gr]\[WeakPain\]"
            jump clinicafive

label clinicafive:

    scene e3clinicafive1 with mediumdissolve
    v "That's enough Reyes. Let's finish this off and get him to his cell."

    play seven "<from 18 to 280>music/clinicafivealive3.mp3" fadein 2

    nurse "Yes, Mistress."
    scene e3clinicafive2 with mediumdissolve
    v "Nurse Reyes is going to stroke you a little more [pname]. Unfortunately for you, this will worsen your pain."
    v "But I want you to understand the power I have over your body."
    scene e3clinicafive3 with mediumdissolve
    v "Another Mistress in here might want to lock up your dick for their own needs, but I have no need for cages."
    v "The compound I gave you makes it basically impossible for you to experience a good orgasm, and you will feel extreme edging as I see fit."
    scene e3clinicafive4 with mediumdissolve
    p "(Oh jeez, she's right. The pain is awful, plus this is also the worst blue balls feeling ever...shit...)"
    v "Be glad I am not making it even more painful because it is quite easy for me to do so."
    scene e3clinicafive5 with mediumdissolve
    v "I could have you strapped down to fuck a dozen women, and it would be nothing but agony for you...but an endless loop of pleasure for all of them."
    v "Learn fast who you need to obey. This program could be your salvation...or doom."
    scene e3clinicafive6 with mediumdissolve
    v "You'll be a good little worm and obey me well, won't you [pname]?"
    menu:
        "(Shit...this fucking sucks...just say yes and maybe it will stop!)":
            $ veronica_scale -= 2
            scene e3clinicafive6b with mediumdissolve
            p "Yes! I will, just stop!"
            v "Good. We'll see what transpires during your stay here."
            jump clinicasix
        "(Screw her! I'm not going to answer just like that...I need to stand up for myself and tell her what I think of just using pain to get obedience...) [VeronicaPath]":
            $ veronica_p += 3
            scene e3clinicafive6c with mediumdissolve
            p "Yeah, so easy to get someone to obey with just pain, pain, pain! I guess using your mind to gain obedience is off the table!"
            v "I was using my mind [pname]...by testing yours. And I have learned something useful now."
            jump clinicasix

label clinicasix:

    scene e3clinicasix1 with mediumdissolve
    v "Now then, can you feel if anything will come out Nurse?"
    nurse "I'm not sure, but I think it's possible."
    v "Very well, finish it off and let's see what happens."
    scene e3clinicasix2 with mediumdissolve
    nurse "I bet it hurts a lot, doesn't it [pname]?"
    nurse "You know, Mistress Veronica could have made your body feel extreme pleasure instead. Too bad for you."
    scene e3clinicasix3 with mediumdissolve
    v "Has the level of pain increased [pname]?"
    p "Yeess. This...why are you being so cruel?"
    scene e3clinicasix4 with mediumdissolve
    v "It's nothing personal [pname], it's a necessary test to prepare for some of your possible activities during the program."
    v "Now, it will hurt quite a lot when your body actually tries to orgasm, but it will then subside for you very quickly."
    nurse "Almost..."
    scene e3clinicasix5 with mediumdissolve
    nurse "I can feel you want to [pname]...and I think it's about to..."
    scene e3clinicasix6 with mediumflash
    nurse "oops...almost nothing came out, haha!"
    p "Ugggghh! (Ow, so awful!)"
    scene e3clinicasix7 with longfade
    nurse "I think everything went great Mistress!"
    v "Yes, I would agree at first glance, but I want to analyze all of the data to be sure. Please prepare everything and wait for me at the lab."
    nurse "Yes, Mistress, I'll go right now."
    scene e3clinicasix8 with longfade

    stop seven fadeout 3

    v "And as for you [pname], I think you could be an excellent performer in here."
    p "(Performer?)"
    v "And I do believe you have earned a little rest. I do empathize a little that it might have been a little rough for you."
    scene e3clinicasix9 with mediumdissolve
    v "Feel free to relax here a bit and even shut your eyes as you wish. I would suggest taking advantage of this opportunity as your cell is not nearly as comfortable."
    v "I'll be in contact with you again in the near future."
    p "(I guess I'll try and rest...)"
    jump sethkitty

label clinicb:

    scene e3clinicb1 with longfade
    kk2 "Wow [pname], you slept through the plane landing! You're lucky we didn't hit a rough patch."
    p "(Wha...)"
    if jromanceopen:
        p "(Hmm, where did Junko go?)"
    else:
        p "(I guess we're here...)"

    scene e3clinicb2 with mediumdissolve

    play seven "music/vawalk.mp3" fadein 3

    kk2 "Let's go! I'll take you in for processing."
    p "Alright, lead the way."
    scene e3clinicb3 with longfade
    p "Where are we exactly?"
    kk2 "Your new home is a private Karlsson facility. It's also the home base so to speak of the entire corporation."
    scene e3clinicb4 with mediumdissolve
    p "Ok, but where exactly are we? In the world I mean?"
    kk2 "That's not for you to know yet. But rest assured, it's a very private place...away from prying eyes of any kind. Almost there..."
    scene e3clinicb5 with longfade
    kk2 "This walkway is the formal entrance to the facility where you will be staying for a few months."
    p "I thought this program was for six months?"
    kk2 "Err, yes, my mistake. Sorry."
    p "(Was it?)"
    scene e3clinicb6 with mediumdissolve
    kk2 "This facility has multiple levels, but the primary areas for you will be Levels Two and Three. Maybe in rare instances Level Four. I sincerely hope you don't go to Level Five."
    p "Why?"
    kk2 "I can't talk about that with you, but just take my word for it. You don't want to be down there."
    scene e3clinicb7 with mediumdissolve
    kk2 "Level Three is the main living area for the prison program participants."
    kk2 "No one is at the elevator at all, maybe we are a bit early. Hmm...let's get you in there though..."
    p "Ok."
    stop seven fadeout 3
    scene e3clinicb8 with longfade
    kk2 "Here we are [pname]! This is just a little medical checkup room where they will get you all set for everything."
    kk2 "I have another assignment to go to right away, but I am sure I will see you again soon."
    if kittyoffer:
        scene e3clinicb8b with mediumdissolve
        kk2 "In fact, I have an offer for you that I want you to consider, but it will have to wait for now. But until then, keep your wits about you. Good luck [pname]!"
        p "Thanks."
        jump clinicbtwo
    else:
        kk2 "Keep your wits about you, and do your best. Good luck [pname]."
        p "Thanks."
        jump clinicbtwo

label clinicbtwo:

    scene e3clinicbtwo1 with longfade
    p "(Err, I guess I just wait?)"
    scene e3clinicbtwo2 with longdissolve

    play seven "music/clinicbtwo1.mp3" fadein 3

    v "Hello there [pname], my name is Veronica Karlsson. It's a pleasure to meet you."
    v "I want to welcome you to our facility. I know you must have a lot of questions and concerns, but I first want to congratulate you on testing very well so far."
    scene e3clinicbtwo3 with mediumdissolve
    p "Thank you."
    v "I do want to assure you that you really do have a chance to do well in here. Perhaps you may have heard rumors about the true nature of the program, but I want to allay some of those fears."
    v "It's true that the program is not entirely what it seems and can be...hazardous to some. But despite that, you personally can come out of this with a great position and a new life."
    scene e3clinicbtwo4 with mediumdissolve
    p "(The word hazardous sounds ominous...but she seems almost reasonable for a first impression, perhaps I should try and ask her a question...)"
    menu:
        "(I should just ask her bottom line what the program actually does, and what I can expect.)":
            scene e3clinicbtwo4b with mediumdissolve
            $ veronica_scale -= 1
            p "If you say the program is not all it seems to be, can you just tell me what it exactly entails?"
            v "You'll have to wait on that. Be patient, answers will be forthcoming as the days proceed. Let's get to your physical examination."
            p "(It was worth a try.)"
            jump clinicbthree
        "(I doubt she will divulge information so quickly or easily. Maybe I should ask her about herself.) [VeronicaPath]":
            scene e3clinicbtwo4c with mediumdissolve
            $ veronica_p += 2
            p "I'm sure you already know a lot about me. Would you mind telling me a little about yourself?"
            v "Interesting question. You didn't ask me about the program or what you will be doing in this room."
            p "I figure I'll find that out soon enough without having to ask you. But I might not get another chance to ask you this kind of question."
            scene e3clinicbtwo4d with mediumdissolve
            v "Excellent thought process. Good. I can at least share a very tiny bit about myself."
            v "I'm the second oldest of my sisters, and I am generally a quiet and reserved person. My favorite activities are reading and basically doing experiments."
            v "I am a scientist and inventor, and greatly enjoy my work."
            p "What have you invented?"
            scene e3clinicbtwo4e with mediumdissolve
            v "Oh, many, many things. But I think that is a discussion for another time. We must get to your physical examination."
            p "(She oozes intelligence, but something seems funny about her too. She also seems familiar to me somehow.)"
            jump clinicbthree
        "(I should ask about her the immediate business at hand. Why am I in this room?)":
            scene e3clinicbtwo4f with mediumdissolve
            $ veronica_scale -= 1
            p "Why am in this room? It seems more like a medical room versus say a place to check in..."
            v "Quite a reasonable if not predictable question. We have to give you a very short physical examination as your first step here upon arrival."
            v "Let's proceed."
            jump clinicbthree

label clinicbthree:

    scene e3clinicbtwo5 with longfade
    v "I'll need you to remove all of your clothing. My assistant Nurse Reyes will store your clothes for a bit."
    p "(Hmm....)"
    scene e3clinicbtwo6 with longfade
    v "Nurse Reyes, please help the examinee undress."
    nurse "Yes, Mistress Veronica."
    p "(Not Doctor or Miss...)"
    scene e3clinicbtwo7 with mediumdissolve
    p "(Yeah, this totally seems like a normal nurse...)"
    nurse "Nice to meet you. I'll be helping with your check-in examination."
    scene e3clinicbtwo8 with mediumdissolve
    nurse "I heard you did really well on your testing. I hope you can do well in the program."
    v "Enough chit chat Nurse Reyes, just get him started please."
    scene e3clinicbtwo9 with mediumdissolve
    nurse "Yes, Mistress Veronica."
    nurse "Well [pname], please strip and then wait here. I'll take your clothes and be right back."
    scene e3clinicbtwo10 with longdissolve
    v "[pname], Nurse Reyes will be giving you a small shot. Don't be alarmed, I think you will actually be quite happy with it."
    stop seven fadeout 3
    menu:
        "(Wait a minute. I need to know what the hell is going into my body! I should object to this.)":
            $ veronica_p -= 1
            scene e3clinicbtwo10b with mediumdissolve
            p "Wait a minute! What the hell are you going to inject into me? I should know what the hell is going into my body!"
            v "[pname], I am being more than reasonable with you given your promising start."
            scene e3clinicbtwo10c with mediumdissolve
            v "But don't misunderstand your position. You are still a prisoner, and you will comply with our requirements under this program."
            v "But as I said, I think you will be pleased with its effect. Have a little faith [pname]."
            jump clinicbfour
        "(I'm worried about what this shot is, but I'm going to guess it's not in her interest to harm me literally on the first day here.) [VeronicaPath]":
            scene e3clinicbtwo10d with mediumdissolve
            p "I'm a little apprehensive what are you are sticking in my body, but it also doesn't make sense to me that you would try and harm me on the very first day."
            v "I'm not [pname]. I really do think you will be pleased with its effect."
            jump clinicbfour

label clinicbfour:

    scene e3clinicbtwo11 with longdissolve

    play seven "<from 48 to 193>music/clinicbthree.mp3" fadein 2

    nurse "This might hurt just a tad, but be glad you are not a lowly prisoner coming in this room. Maybe a different shot."
    scene e3clinicbfour1 with mediumdissolve
    nurse "Just relax...I'll make it as gentle as possible."
    nurse "You might feel a tad lightheaded for a few seconds, but after that you should quickly start to feel very good."
    p "Alright."
    scene e3clinicbfour2 with mediumdissolve
    nurse "There we go...get ready for a really good feeling."
    p "(I am feeling lightheaded...)"
    scene e3clinicbfour3 with mediumdissolve
    nurse "Let me just put this needle away, try and move your arms and legs a bit to take away the initial lightheadedness."
    nurse "I'll be right back."
    scene e3clinicbfour4 with mediumdissolve
    p "(Wow, this feels...great! My whole body is tingling with pleasure...)"
    v "Don't forget to stretch a bit to let your body adapt [pname]."
    scene e3clinicbfour5 with mediumdissolve
    p "Right. Sorry, it kind of surprised me with how it feels."
    v "It's to be expected for such a potent mixture. But don't worry about long-term issues or side effects. I tested this compound for quite a long time before finalizing it."
    scene e3clinicbfour6 with longdissolve
    nurse "So...how are you feeling [pname]?"
    v "Make sure he's ok first."
    nurse "Yes Mistress."
    scene e3clinicbfour7 with mediumdissolve
    nurse "Feels good, doesn't it? Like you're in a wave of smooth rolling pleasure..."
    nurse "But it gets so much better."
    scene e3clinicbfour8 with mediumdissolve
    nurse "Why don't you take a closer look at me. I can be a test subject for you..."
    nurse "Even feeling my body will cause some sensations of pleasure in your hands...go ahead."
    scene e3clinicbfour9 with mediumdissolve
    nurse "Mmm yeah, that's great [pname]."
    p "(Woah, what the hell is this stuff? My hands are sending feelings to the rest of my body...wow!)"
    nurse "I'm a little...enhanced too right now...so yeah..."
    scene e3clinicbfour10 with mediumdissolve
    v "Stick to your task. I want to see how his body responds."
    nurse "Of course Mistress."
    scene e3clinicbfour11 with mediumdissolve
    nurse "Come lie down here [pname]."
    p "Sure thing."
    nurse "Good. Let me get more comfortable too, I'll be right back."
    scene e3clinicbfour12 with longfade
    nurse "Now, are you comfortable?"
    p "Yeah, but my body is literally tingling everywhere, I feel so...I guess sensitive."
    scene e3clinicbfour13 with mediumdissolve
    p "Is this table going to slide me like a normal MRI machine?"
    nurse "It does that, but it's not needed right now. The room itself can scan your body just fine, and the MRI is specially designed for other functions."
    scene e3clinicbfour14 with mediumdissolve
    nurse "Is your dick normally this size? Sometimes this stuff does a little extra for men."
    p "I'm...I'm not sure. Maybe."
    scene e3clinicbfour15 with mediumdissolve
    nurse "Not bad [pname], it's making me quite thirsty."
    p "(Holy shit, just her touching it lightly feels so good.)"
    scene e3clinicbfour16 with mediumdissolve
    nurse "Mistress Veronica, please let me fuck him."

    stop seven fadeout 3

    v "Not on his first day! I want some data first on everything."
    nurse "Yes, Mistress..."
    scene e3clinicbfour17 with mediumdissolve

    play seven "<from 1 to 126>music/limo.mp3" fadein 3

    v "Now [pname], you might be surprised at the intensity of this, but just relax."
    p "Mmmmhmmmm..."
    scene e3clinicbfour18 with mediumdissolve
    p "(Oh. My. God. It's so intense, I feel like I'm already about to go!)"
    nurse "He's responding very well Mistress."
    scene e3clinicbfour19 with mediumdissolve
    v "Good. I'm getting excellent...feedback. Keep at it and see what happens next."
    nurse "Yes, Mistress."
    scene e3clinicbfour20 with mediumdissolve
    nurse "Feels so strong doesn't it [pname]? Just imagine fucking me with this sensitive thing."
    p "Oh fuck...yeah."
    scene e3clinicbfour21 with mediumdissolve
    nurse "You have no idea [pname]. So much more is possible with enhanced pleasure. My Mistress is truly a genius."
    p "I'm already about to...!"
    scene e3clinicbfour22 with longflash
    p "...cum!"
    nurse "There we go! Let me just clean you off a little..."
    scene e3clinicbfour23 with longfade
    nurse "Now...time for some more fun!"
    p "Wait, what you do mean?"
    scene e3clinicbfour24 with mediumdissolve
    nurse "You can feel your own body [pname]. Aren't you still as hard and sensitive as it was before you had an orgasm?"
    p "Holy sh...you're right. How?"
    scene e3clinicbfour25 with mediumdissolve
    v "Enough chatter! See how long it takes for his second one."
    nurse "Yes, Mistress. But this time, let's do something a little different."
    v "I know what you want to do. No pussy stimulation. Keep on task."
    nurse "*whispering* Oh well. Let me just take off my boots too..."
    scene e3clinicbfour26 with longfade
    nurse "Go ahead and enjoy the view while you get a little more pleasure."
    nurse "I'm very curious how you do for Round Two."
    scene e3clinicbfour27 with mediumdissolve
    nurse "And of course Round 3..."
    p "(Round 3? How long does this stuff last? Oh jeez, the feeling is so strong throughout my whole body even...)"
    scene e3clinicbfour28 with mediumdissolve
    nurse "I bet this doesn't take too long, does it feel even stronger this time around?"
    p "Yes!"
    scene e3clinicbfour29 with mediumdissolve
    nurse "Try and imagine having an orgy with all of the staff here [pname], you really might be able to fuck a lot of women at once with barely any rest...inbetween."
    p "(Oh my God, so strong...)"
    scene e3clinicbfour30 with mediumdissolve
    nurse "He's close again Mistress, it's amazing how you can tell so easily while he's..."
    v "...Stop talking, I can see for myself what is happening."
    scene e3clinicbfour31 with mediumdissolve
    nurse "Ahh, here we go again I think!"
    scene e3clinicbfour32 with longflash
    nurse "There he blows again! Even thicker!"
    p "Yeeesss, oh my..."
    scene e3clinicbfour33 with mediumdissolve
    v "No break this time."
    nurse "Yes, Mistress."
    p "(again...)"
    scene e3clinicbfour34 with longfade
    p "(Her mouth this time...oh oh...)"
    scene e3clinicbfour35 with longdissolve
    v "See if you can do it within a minute."
    scene e3clinicbfour36 with longdissolve
    p "(She's pushed it even deeper in her mouth...fuck...I've never felt this good in my entire life...)"
    scene e3clinicbfour37 with longdissolve
    p "(So good...)"
    scene e3clinicbfour38 with longdissolve
    p "(I'm going to cum again, I can't believe it's so fas..)"
    scene e3clinicbfour39 with longflash
    p "(Yesss...!)"
    stop seven fadeout 3
    v "Excellent! Very good data, well done to both of you, I'm quite pleased."
    scene e3clinicbfour39b with longdissolve
    p "(Three...oh wow she's sucking me dry...fuuuuccckkk...)"
    scene e3clinicbfour40 with longfade
    nurse "Hope you had fun. Next time, I expect you to eat me during Rounds 4...and 5."
    nurse "And then we can fuck for another 3-4 rounds...it could be a lot of fun."
    v "That's enough Reyes, get out."
    scene e3clinicbfour41 with longfade
    v "You did quite well [pname]. It was an excellent physical examination and I think you will adapt well here. Welcome again to the Joy Facility."
    p "Yeah, an examination. Sure. But what you shot me up with...it's crazy. Incredible. You really are a genius."
    v "Yes."
    scene e3clinicbfour42 with mediumdissolve
    v "But [pname], a word of warning. Just as I can give extreme pleasure, I can also give extreme pain and agony as well."
    v "Don't make an enemy of me. Use your wits and instincts to thrive here, and maybe we can see about more...testing. Consider my words carefully."
    scene e3clinicbfour43 with mediumdissolve
    p "I will."
    v "Good. You should only last another half hour this juiced up so to speak. After that, you should feel perfectly fine with some mild side effects."
    v "Those effects should go away relatively quickly, but let a guard know if it persists."
    scene e3clinicbfour44 with mediumdissolve
    v "Now, just relax. You can even sleep here a bit if you wish. You'll be placed in your new room soon."
    p "I understand."
    jump sethkitty

label sethkitty:

    scene e3sethkitty1 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3sethkitty2 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3sethkitty3 with longdissolve
    kk2 "Hello there [pname4], I hope you are doing ok in there."

    play seven "music/seth.mp3" fadein 3

    bro "Katherine??"
    scene e3sethkitty4 with mediumdissolve
    kk2 "Actually, my name is Katsumi and I..."
    bro "...and you lied and tricked me into getting sent here! Hanging by chains, prodded and poked, and trapped! Yeah, real nice hospital!"
    scene e3sethkitty5 with mediumdissolve
    kk2 "[pname4], I understand your anger. But you don't understand what it's like to be in this world...my family was sold into this life."
    kk2 "There was nothing I could do for you, and I'm basically in the same boat as you...a slave to the Karlsson Group."
    scene e3sethkitty6 with mediumdissolve
    kk2 "I mean, look at the skimpy nurse outfit they make me wear! Clearly very professional..."
    kk2 "And...you're being treated much better than most here. Look outside at those boxes for example on the floor."
    scene e3sethkitty7 with mediumdissolve
    kk2 "Each of those boxes has a person trapped inside suffering far worse than you. Consider yourself lucky so far."
    kk2 "I do what I have to for survival. So will you. But maybe I can help you quietly if you can do the same for me."
    scene e3sethkitty8 with mediumdissolve
    bro "Alright...what are you proposing?"
    kk2 "[pname4], you are going to be undergoing some further testing on your body and mind for your condition."
    kk2 "Obviously, just the fact you can even stand like this is already proof that some things have already worked for you, right?"
    scene e3sethkitty9 with mediumdissolve
    bro "Yes, I've never felt better in years. But why am I here, and where are we?"
    kk2 "You're in an underground lab area in a compound called the Joy Facility. I don't know exactly why you specifically were sent here. Perhaps it was just random...perhaps not."
    scene e3sethkitty10 with mediumdissolve
    kk2 "Now, what I am proposing is that you help me look good to my Mistress, Veronica Karlsson, by being very obedient and cooperative to me in all testing."
    kk2 "In return, I can secretly make your testing compounds less painful on your body. They do intend to test your pain tolerance so this will help you a lot."
    bro "Why do you need me to be obedient? You could just force me to do anything."
    scene e3sethkitty11 with mediumdissolve
    kk2 "It looks good for me if you are cooperative versus being forced against your will. I also have one last request as a special condition to get my help."
    bro "Ok, what is it?"
    scene e3sethkitty12 with mediumdissolve
    kk2 "Veronica Karlsson will ask you a question later with a set of choices. These choices will be about selecting a woman for testing with the two of us in a room."
    bro "What specific type of testing, and how do you know that?"
    kk2 "Don't worry about that yet. But when she asks that question, you will have the ability to actually make a real choice. I want you to pick someone specific."
    scene e3sethkitty13 with mediumdissolve
    kk2 "I believe you have already met her briefly...the Head of a special assasination group called The Deadly Vipers. Her name is Kiyomi."
    bro "Wait...Kiyomi...I have met her. She...killed...someone right in front of me."
    kk2 "Yes. That's her job. But she was captured and dropped in this world just like me, so don't assume anything about her just because she kills people."
    scene e3sethkitty14 with mediumdissolve
    bro "Why her?"
    kk2 "I know I can trust her. She's also my sister."
    bro "I...I see."
    scene e3sethkitty15 with mediumdissolve
    kk2 "Having the two of us with you alone will get the...best outcome for you."
    kk2 "I realize I already lied to you once and you have no reason to trust me yet. So you don't have to decide anything right now. Wait and see to be sure if you wish."
    scene e3sethkitty16 with mediumdissolve
    kk2 "But you will feel the difference in pain if I am your nurse versus someone else. I think over time you will come to trust me once it's clear I am helping you."
    kk2 "I can also tell that your heart seems good and pure...and you seem like such a sweet man."
    scene e3sethkitty17 with mediumdissolve
    kk2 "And that's...attractive to me."
    bro "(Is she...)"
    scene e3sethkitty18 with mediumdissolve
    kk2 "But I have one specific request I need you to do on good faith. It's a very simple one. I need to you stand still near the wall and pose together with me for a moment."
    bro "Why?"
    kk2 "It's just a picture to signify the start of your testing and it will help me look good for my boss. It might show we are ready to work well together!"
    scene e3sethkitty19 with mediumdissolve
    kk2 "And I hope someday we can pose together for a great after picture, where you are strong and healthy, and who knows...maybe we are more free than we are today."

    stop seven fadeout 3

    bro "Ok. I guess there's no harm."
    scene e3sethkitty20 with longfade

    play seven "<from 665 to 700>music/darkmix7.mp3" fadein 2

    kk2 "Ok, let's pose here, there is actually a hidden camera in that wall just video recording...but I can make a photo out of it. I appreciate this [pname4]."
    bro "No problem."
    kk2 "Ok, just focus straight ahead for the camera! You need to stay really still and only look straight ahead...good job [pname4]..."
    scene e3sethkitty21 with longfade
    if k4:
        kk2 "(Toy Number Two...)"
        kk2 "Great...just hold it another few seconds."
        stop seven fadeout 3
    else:
        kk2 "(A great before picture...Kiyomi will love this...)"
        kk2 "Great, just hold it another few seconds."
        stop seven fadeout 3
    scene e3sethkitty22 with longfade
    kk2 "Thank you [pname4]. I have to run now, but I really do want you to think hard about how to survive in here. Be careful trusting anyone else."
    kk2 "You don't see it yet but I hope you will later...I really am the nicest person in this whole crazy place. I will see you again soon [pname4]."
    jump clinic2

label clinic2:

    if k4:
        jump k4cell
    elif k5:
        jump k5cell
    elif k6:
        jump k6cell
    else:
        jump k4cell


label k4cell:

    scene e3k4cell1 with longfade
    p "(Ugh, what the hell...where am I...)"
    scene e3k4cell2 with longfade
    p "(Whatever she gave me, it also packs a little bit of a vicious hangover effect...my damn head...)"
    scene e3k4cell3 with mediumdissolve

    play seven "music/k4cell1.mp3" fadein 2

    pbf "[pname], take it nice and slow. Whatever they gave us takes a bit to recover from, but it seems to help to stand up and move around."
    pbf "But stand up slowly to make sure you don't pass out or get too dizzy."
    scene e3k4cell4 with longfade
    p "[pname2]! Where are we? And what the hell is going on, last I remember, I was in a medical room and..."
    pbf "Yeah, me too. The shot probably drugged both of us a little too much, and then they just dumped us in here."
    scene e3k4cell5 with mediumdissolve
    p "What the hell is this tiny little room? Is this supposed to be our cell, or are they going to move us later? No bed, toilet, even a mattress?"
    pbf "I don't know. I'm just as much in the dark as you are right now."
    scene e3k4cell6 with mediumdissolve
    pbf "What the hell have we gotten ourselves into this time [pname]? I definitely feel like this shit could be worse than the prison."
    p "You may be right, but we're stuck for now. We just have to hope we actually can get out of here in six months ok."
    scene e3k4cell7 with mediumdissolve
    if friend >= 2:
        pbf "[pname], we've had each other's backs for a long time. But we're going to need each other more than ever I think in here."
        menu:
            "(I definitely agree with [pname2] here. We need to completely trust and rely on each other in this situation. I'll tell him that now.) [FriendPath]":
                scene e3k4cell7b with mediumdissolve
                $ bestfriendloyalopen = True
                $ friend += 2
                p "I'll always have your back [pname2]. We'll get through this together somehow. If you promise never to hit on [pname3] again, right?"
                pbf "Wait a minute! I know she loves it, how can you deprive her of my charm and wit?"
                pbf "But yeah...I got your back too. Fuck these bitches and fuck this place, we're going to get out of this one way or another!"
                stop seven fadeout 2
                jump k4celltwo
            "(I think we need to help each other too, but I'm not sure I can trust anyone completely after what has happened so far. I'll say it's all good but keep my options open.)":
                scene e3k4cell7c with mediumdissolve
                p "Hey, we've always had each other's backs. We'll get through this somehow."
                pbf "You know it [pname]. Screw this damn place and their crazy women, we'll figure out something one way or another."
                stop seven fadeout 2
                jump k4celltwo
    else:
        pbf "I know we haven't totally been in sync together since we were put in jail, but I think we're going to need each other more than ever."
        menu:
            "(I definitely agree with [pname2] here. Despite some bumps between us, who else can I trust in here? I'll let him know how I feel.) [FriendPath]":
                $ friend += 2
                scene e3k4cell7d with mediumdissolve
                p "I think you're right [pname2]. We have to be able to trust each other. Who knows what could happen in here?"
                p "We'll get through this...of course, you're never going to hit on [pname3] again, right?"
                scene e3k4cell7e with mediumdissolve
                pbf "Wait a second [pname]! You know [pname3] secretly loves me and is just playing hard to get! How can I deprive her of her joy?"
                p "Uh huh...sure."
                pbf "But you know I got your back too [pname]. Screw this place and screw these sadistic bitches, we'll get out of this somehow."
                stop seven fadeout 2
                jump k4celltwo
            "(I haven't forgotten that he hasn't always stood up for me. But maybe I have some blame too. Either way, I can tell him something good but keep my options open.)":
                scene e3k4cell7f with mediumdissolve
                p "Hey, we've always had each other's backs. We'll get through this somehow."
                pbf "You know it [pname]. Screwn this damn place and their crazy women, we'll figure it all out."
                stop seven fadeout 2
                jump k4celltwo

label k4celltwo:

    scene e3k4celltwo1 with mediumdissolve

    play nine "<from 10 to 165.5>music/hallway2.mp3" fadein 1

    chan "[pname] and [pname2]! I'm opening the door! Both of you get on your knees with your heads down facing the door so I don't have to shock you!"
    p "(Great...what's next...)"
    scene e3k4celltwo2 with longfade
    chan "My name is Mistress Chanel. And you both are pathetic excuses of human beings. I just want to throw both of you in the trash and let you rot."
    chan "You both can barely even stretch your legs out in this little pig pen of a home, haha!"
    scene e3k4celltwo2b with longdissolve
    chan "You better learn to do exactly what everyone wants, or you will pay the price."
    scene e3k4celltwo3 with mediumdissolve
    chan "Now both of you lick my boots like the worthless sluts you are."
    scene e3k4celltwo4 with mediumdissolve
    chan "Very good sluts. I'm looking forward to seeing you both begging day after day from all of us."
    chan "Poor poor [pname]...a worthless piece of trash, but you're doing a better job than your friend here licking. I think he needs a little help."
    pbf "(Ugh what is she...!)"
    scene e3k4celltwo4b with mediumdissolve
    chan "And [pname2], just another piece of garbage...You two pathetic so called men are barely even human beings to me, so you better earn some respect somehow during the program."
    chan "I think that's enough sluts. I'll let you both just kneel again."
    scene e3k4celltwo5 with mediumdissolve
    chan "I wish I had more time to introduce myself but I'll have to torment you both later. I'm here to take [pname] out for a bit."
    p "What for?"
    scene e3k4celltwo6 with mediumdissolve
    chan "Did I say you could talk slut? You don't speak unless allowed!"
    chan "Now let's go...someone wants to see you."

    stop nine fadeout 3

    jump k4abuse

label k4abuse:

    if busyboy:
        jump pet
    elif junkopet:
        jump pet
    elif scarlettpeg:
        jump pegging
    elif freeagent:
        jump freeagent
    else:
        jump pet

label k5cell:

    scene e3k5cell1 with longfade
    p "(What the hell was...)"
    scene e3k5cell2 with longfade
    p "(Whatever she gave me...definitely has a vicious hangover effect...what a headache...)"
    scene e3k5cell3 with longdissolve

    play seven "music/kwame2.mp3" fadein 3

    kw "Hey there, take it easy for a second. It does help to stand and move a bit around...but slowly."
    scene e3k5cell4 with longdissolve
    p "Where are we? And who are you?"
    p "And jeez, what the hell did they give me? It felt great before but now my head feels like shit..."
    scene e3k5cell5 with longdissolve
    kw "Whatever it was, it got us both here now. My name is Kwame, and it appears we are cellmates in this so called program. We are apparently the only two K5 prisoners."
    p "Right...K5...I heard that too. ...[pname], my name is [pname]. Nice to meet you."
    scene e3k5cell6 with mediumdissolve
    p "Ah, great amenities I see. A shared toilet and sink. A little less space than my prior cell."
    p "Speaking of cells, I don't recall ever seeing you at the prison at all."
    scene e3k5cell7 with longdissolve
    kw "Is that where most of you came from, a prison? Maybe Dominique was being truthful about this being a prisoner rehabiliation program."
    p "I doubt this program is legit at all. But I guess we will see. Where did you come from then if not some kind of prison?"
    scene e3k5cell8 with mediumdissolve
    kw "I was an Operations Senior Foreman for one of the biggest Karlsson mining facilities in the world. It's located in what used to be called Namibia."
    p "It sounds like an important position, and you definitely sound educated when you speak. How did you end up here?"
    scene e3k5cell9 with mediumdissolve
    kw "I was doing quite well, and I was working directly for Dominique Karlsson. But...my people...they are basically slave labor, and I...I...helped plan a revolt."
    kw "But I was discovered before anything could go forward, and sent here as a punishment."
    scene e3k5cell10 with mediumdissolve
    p "Damn, sorry to hear that. Nothing this company does shocks me, and especially it seems that all of the Karlsson sisters are incredibly nasty and evil people."
    scene e3k5cell11 with mediumdissolve
    kw "No...not one at least. I don't believe Dominique Karlsson is really an evil person...she actually did improve conditions for the workers, but I was...impatient."
    kw "And she...stopped the Board from executing my family for my deeds. But I have to do well in this program to save them. Whatever that may entail, I don't know."

    p "(Damn. His family was going to be killed? And he has to finish this program to save their lives?? Holy shit...talk about pressure.)"
    menu:
        "(Kwame seems very intelligent and highly motivated. I should try and work with him as an ally, and support his goal of saving his family too. That's the right thing to do.) [GoodPath]":
            $ good += 2
            $ kwamefriendopen = True
            scene e3k5cell11b with mediumdissolve
            p "Hey look Kwame, I know we just met. But the bottom line is that we are in this together. We should make sure we help each other to survive this experience."
            p "I'd also like you help you save your family. That's horrible that you have that added pressure too."
            scene e3k5cell11c with mediumdissolve
            kw "Thank you [pname]. I'd like that too. We are also the only two prisoners not ranked K4, so perhaps that gives us a leg up somehow."
            p "Perhaps it does. By the way, do you know why we have no clothes?"
            kw "I don't know. Perhaps they give will give us uniforms when we start tomorrow..."
            jump k5celltwo
        "(I should try and gain Kwame's trust, but I also need to be careful in case only one person can actually come out of this ok. I need to be smart and pragmatic about things.)":
            scene e3k5cell11d with mediumdissolve
            p "Look Kwame, I know we just met. But we are stuck in this together. We should try and support one another to survive this experience."
            p "I think we can definitely help each other out to try and get through whatever the hell this is as best as we can."
            scene e3k5cell11e with mediumdissolve
            kw "Thank you [pname], I'd like that too. We are also the only prisoners not ranked K4, so perhaps that is an advantage somehow."
            p "Hmm, perhaps it is. By the way, do you know why we have no clothes yet?"
            kw "I don't know. Perhaps they will give us uniforms when we start tomorrow."
            jump k5celltwo
        "(I have to look out for myself. Still, I should try and offer to work with Kwame while it's in my interest to do so. I can always drop him later when it's best for me.) [EvilPath]":
            $ evil += 2
            scene e3k5cell11f with mediumdissolve
            p "Kwame, I know we just met. But, I think should help each other out to survive this experience."
            p "Maybe we can both get out of this ok, and we can also help your family as well."
            scene e3k5cell11g with mediumdissolve
            kw "Thank you [pname], you are very kind. I'd like us to help each other too. We are also the only prisoners not ranked K4, so perhaps that is an advantage somehow."
            p "(Hmm, it may be important that I make sure I am the highest rank over Kwame and everyone else...)"
            p "Hmm, perhaps it is. Let's hope so. By the way, why don't we have any clothes?"
            kw "I don't know. Perhaps they will give us uniforms when we start tomorrow."
            jump k5celltwo

label k5celltwo:

    scene e3k5celltwo1 with longdissolve
    chan "[pname] and Kwame, I'm coming in! Stand at attention by your beds, hands on your sides!"
    p "(What's next...)"
    scene e3k5celltwo2 with longfade
    chan "Welcome to the Joy Facility. My name is Chanel, and I'm one of your program supervisors in here."
    chan "I'll be one of the main people you deal with if you are at this prisoner rank or higher."
    scene e3k5celltwo2b with mediumdissolve
    chan "You two have done well to start at K5. Everyone else is at K4, so take advantage of your fast start."
    chan "If you don't, you will end up regretting it. Take everything seriously."
    scene e3k5celltwo2c with mediumdissolve
    chan "I may meet with you both tomorrow morning before formally starting the program."
    chan "And...you will have some early advantages. However, you still will have to deal with some difficult situations to survive here."
    scene e3k5celltwo3 with mediumdissolve
    stop seven fadeout 3
    chan "But for right now, I'm simply here to pick you up [pname]."
    p "What for?"
    chan "Someone wants to see you. Let's go!"
    jump dompaths

label k6cell:

    scene e3k6cell1 with longfade
    p "(Ugh, what the hell?)"
    scene e3k6cell2 with longfade
    p "(Whatever she put in me...it gives a rough hangover effect...damn...my head)"
    scene e3k6cell3 with longfade

    play seven "music/k6cell2.mp3" fadein 3

    chan "Hey there, you need to take it easy a few seconds and get your bearings."
    chan "Then try to get up slowly and move around. It will help lessen the effect of the compound more quickly."
    scene e3k6cell4 with mediumdissolve
    p "Where am I now? And who are you?"
    scene e3k6cell5 with mediumdissolve
    chan "My name is Chanel. I'm a program supervisor here and also liasion and advisor for the most promising prisoners in the program."
    chan "Right now, that's basically just you and one other prisoner starting at K5. No one else tested at K6, so you should feel pretty good about your performance so far."
    scene e3k6cell6 with mediumdissolve
    p "Hmm, I can see that I'm basically in another cell."
    p "But, I have a little bit better amenities this time around. Does this shower work?"
    scene e3k6cell6b with mediumdissolve
    chan "Yes, and you also have a nice laptop you can use for your leisure and work, although you don't have online access yet."
    p "So I heard. K7 right?"
    chan "Oh...yes, that's right."
    scene e3k6cell7 with longdissolve
    p "So what's next? What is happening? Why do I have no shirt and of course no shoes again?"
    chan "Relax [pname]. I'm not going to lie and say you won't have some rough patches here and there, but believe it or not, you are in a good situation right now."
    scene e3k6cell8 with longdissolve
    chan "Just your private shower alone is huge. A lot of bad...things happen in the public shower rooms, believe me."
    chan "Most of the others that didn't do as well as you are sleeping in tiny concrete rooms with no bed, no toilet, not even a mattress."
    p "(Shit...that sounds bad.)"
    chan "You are living like a king compared to them, so take advantage of your good fortune right now."
    scene e3k6cell9 with mediumdissolve
    chan "Now, you will have do some shitty tasks like the other prisoners, but you will also be able to avoid the most demeaning and humiliating things given your status."
    chan "Don't. Lose. Your. Rank. I can't be more clear. Got it?"
    p "Got it."
    scene e3k6cell10 with mediumdissolve
    chan "You know...if you do really well, you can even...party with the staff here a bit. We are open to having some...fun with the right guy..."
    chan "Do well, and we can see about that. It's not like there are male staff here, and some of us can only get off abusing prisoners so much."
    scene e3k6cell11 with longdissolve
    chan "Sometimes, a woman just wants to...fuck. We're allowed to play with...high performing prisoners too. So get motivated to do well. Some of us get very thirsty after working all day..."
    chan "And after all, on rare occasions, a man can rise up and end up an executive after this program. So in theory, you could be our boss someday. Is that someone going to be you?"
    menu:
        "(No time to be fucking timid. I need to answer that with a resounding yes.) [ChanelPath]":
            $ chanel_p += 1
            scene e3k6cell11b with mediumdissolve
            p "Absolutely. I'm going to do whatever it takes to do well here."
            chan "Good. Good! Keep that attitude, and do your best. Maybe some of us will help you...maybe. It's a huge risk for us to back a loser, so you need to show you're worth it."
            jump k6celltwo
        "(I don't want to sound too arrogant. I should just say I'll do my best.)":
            $ chanel_scale -= 1
            scene e3k6cell11c with mediumdissolve
            p "I'm certainly going to try my best here. We'll see how it goes."
            chan "Don't think you are going do well, KNOW you are going to do well. Don't blow this chance you have here."
            jump k6celltwo
        "(This might be risky, but screw it. She's teasing me, and I'm going to tease her right back.) [ChanelPath] [JuliettePath]":
            $ chanel_scale += 1
            $ chanel_p += 1
            $ jmeet += 1
            scene e3k6cell11d with mediumdissolve
            p "I think you want to help me get to K7 as soon as possible...I definitely can..."
            p "...fill your need for extra pleasure."
            chan "Mmm, good...maybe you have what it takes..."
            jump k6celltwo

label k6celltwo:

    scene e3k6celltwo1 with longfade

    stop seven fadeout 3

    chan "But...back to business. I actually stopped by because someone wants to see you. So we need to go."
    p "Who?"
    chan "You'll see."
    jump dompaths

label dompaths:

    if vmeet >= 2:
        jump vmeet
    elif evil >=3 and jmeet >= 3:
        jump jmeet
    else:
        jump dmeet

label pet:

    scene e3pet1 with longfade
    chan "Junko! It's been too long. I'm so glad you got assigned here with us."

    play seven "music/hospital.mp3" fadein 3

    jk "Hi Chanel. It's good to see you too. I hope Kiyomi is treating you well."
    chan "Oh yes, she is. It's a lot of fun working with her!"
    scene e3pet2 with mediumdissolve
    jk "Happy to hear it. And thank you for bringing [pname] to me."
    chan "No problem. I hope you enjoy your new pet."
    scene e3pet3 with mediumdissolve
    chan "[pname], don't you dare get any ideas about doing anything stupid around Junko."
    chan "If I hear you did anything that displeased her, I will end you...painfully and slowly."
    scene e3pet4 with mediumdissolve
    chan "So don't fuck it up [pname]."
    jk "I'll be ok Chanel. I'm sure [pname] knows it's to his advantage to be obedient to me."
    scene e3pet5 with mediumdissolve
    chan "Alright. Make sure to shock him or call me if he gets out of line at all. Let's get together when things get a little settled!"
    jk "Sounds good. Thank you Chanel!"
    chan "Have fun with him...and don't forget what I said [pname]."
    scene e3pet6 with longfade

    play seven "music/clinicbthree.mp3" fadein 3

    jk "Come over here so I can see you up close."
    jk "Don't look so stressed [pname], I don't bite too hard. Especially compared to everyone else here."
    scene e3pet7 with mediumdissolve
    jk "But I do expect you to listen me. If you do, I think you will find I can be quite generous with you."
    jk "I can also recommend quite a few things to my boss, Dominique Karlsson. Obeying me well might get her attention...which you do want in here."
    if good >= 3:
        $ dominiqueinterest = True
    scene e3pet8 with mediumdissolve
    jk "Now...I'd like you to get on your knees, and I'll get more comfortable."
    jk "I hope you are ready to take care of your Mistress."
    scene e3pet9 with longfade
    jk "Now, I'm ready to relax. Your job as my pet is to always take care of my body any way I wish."
    jk "And right now, I want you to take care of my feet first...then you can work your way up."
    scene e3pet10 with mediumdissolve
    jk "You do want to be a good pet for me, don't you [pname]?"
    menu:
        "(I think I do want to obey Junko, she seems like a Mistress I want to please. I'll answer very positively.) [JunkoPath]":
            $ junko_scale -= 1
            scene e3pet10b with mediumdissolve
            p "Yes, Mistress Junko. I'd like to be a good pet for you."
            jk "Excellent, I am so happy to hear that from you. Why don't you get started now."
            jump pettwo
        "(I don't want to do everything she says automatically, but I should say so for now.)":
            scene e3pet10b with mediumdissolve
            p "Yes, Mistress Junko. I'd like to be a good pet for you."
            jk "Excellent, I am so happy to hear that from you. Now, why don't you get started."
            jump pettwo
        "(I don't feel like just rolling over like a little dog for her so easily. I'll answer, but not very positively...)":
            $ junko_p -= 1
            scene e3pet10c with mediumdissolve
            p "I suppose so."
            jk "Not a very good answer [pname]. But I think you will end up listening anyway, unless you'd rather have a much crueler woman all over you?"
            jump pettwo

label pettwo:

    scene e3pettwo1 with longdissolve
    jk "Since it's your first night here, I'll take it a little easy on you. I just want you to learn my body a little."
    jk "Start here and lick and kiss your way up."
    scene e3pettwo2 with mediumdissolve
    jk "There you go...that's being a good pet. Catering to the needs of your owner..."
    jk "I really do have empathy for you too [pname]. What do you think I have to do with my own boss sometimes?"
    scene e3pettwo3 with mediumdissolve
    jk "Now move on up...there you go."
    jk "You're doing so well so I'll share some early information in good faith."
    scene e3pettwo4 with mediumdissolve
    jk "I believe my own boss Dominique is the only Karlsson sister with any trace of compassion and morality."
    jk "She lacks understanding of the harsh day to day realities of normal people, but she is not an evil person."
    scene e3pettwo5 with mediumdissolve
    jk "Oh good...keep going."
    jk "If you are honorable and don't fall prey to acts of darkness, she may protect you as she has me."
    scene e3pettwo6 with mediumdissolve
    jk "Just kiss my pussy once and then move up. I'm not warmed up enough yet."
    scene e3pettwo7 with mediumdissolve
    jk "Good job my pet...I'm getting hotter now."
    scene e3pettwo8 with mediumdissolve
    jk "This program you have entered...it's nothing but entertainment for a small group of mostly rich women."
    jk "So don't worry about rehabilitation at all. Worry about finding the right sponsor to make your life as painless as possible."
    scene e3pettwo9 with mediumdissolve
    jk "I have very sensitive nipples, so be gentle with your tongue."
    jk "Mmm, lick it after a soft kiss..."
    scene e3pettwo10 with mediumdissolve
    jk "Just right, good job [pname]."
    jk "I think I'm warmed up now. I'm almost ready to cum."
    scene e3pettwo11 with mediumdissolve
    jk "I want you to now get in the cage behind you. But first, take your pants off."
    p "What? I thought..."
    jk "Now."
    jump cageman

label cageman:

    scene e3cageman1 with longfade
    jk "Go ahead, crawl in there. It's a tight fit, but you can squeeze in there."
    jk "Make sure I have a good view of your dick too."
    scene e3cageman2 with longdissolve
    p "(This cage is too small to even sit comfortably...)"
    jk "Perfect. Let me just take a look at it."
    jk "Now, I want you to beg me to allow you to cum. And call me Mistress Junko."
    scene e3cageman3 with mediumdissolve
    p "(What is she trying to do?)"
    menu:
        "(I guess I want to please her, but maybe she will let me get off.) [JunkoPath]":
            $ junko_scale -= 1
            scene e3cageman3b with mediumdissolve
            p "Please let me cum, Mistress Junko."
            jk "Good...call yourself a worthless dog."
            scene e3cageman3c with mediumdissolve
            p "I'm...I'm a worthless dog."
            jk "A dog that needs to be obedient before getting anything from it's owner. You'll have to please me more before getting any rewards."
            jump cagemantwo
        "(She's just teasing me. I don't feel like begging for something she probably doesn't even give me.)":
            $ junko_p -= 3
            if dominiqueinterest:
                $ dominiqueinterest = False
            scene e3cageman3d with mediumdissolve
            p "I...I don't feel like just begging like this. You're going to do what you want anyway."
            jk "[pname], a good pet doesn't ruin their owner's fun. I'm very unhappy with your answer."
            scene e3cageman3e with mediumdissolve
            $ chanelpunish = True
            jk "I'm going to have to let your trainers know you haven't performed well for me."
            p "(I don't even know who she means...)"
            jump cagemantwo

label cagemantwo:

    scene e3cagemantwo1 with longdissolve
    jk "Now here's what I think I am going to do with you [pname]."
    jk "I'm going to really make you my little pet."
    scene e3cagemantwo2 with mediumdissolve
    jk "I'm going to make you crawl on all fours everywhere...and of course you'll have to eat like a little animal in your cage."
    jk "And you'll have to beg to come out of the cage for a little taste of freedom. And I can walk you on a leash."
    scene e3cagemantwo3 with mediumdissolve
    p "(She said she's so nice compared to the others but...)"
    jk "Maybe I'll even get you a cute little collar. Perhaps a lovely pink one!"
    scene e3cagemantwo4 with mediumdissolve
    jk "And you can just lie down there in your cage, like a good little pet..."
    scene e3cagemantwo5 with mediumdissolve
    jk "And you'll have to beg me to even use the bathroom."
    jk "Because you'll have to be punished if you can't hold it in your little cage there."
    scene e3cagemantwo6 with mediumdissolve
    jk "Yes, you'll be so good for me..."
    jk "Oh my...I'm going to..."
    scene e3cagemantwo7 with mediumflash
    jk "Oh yes!!"
    scene e3cagemantwo8 with longfade
    jk "I feel so much better now [pname], thank you!"
    jk "We'll get to know each other a lot more later, and I will help you survive if you are a good pet for me."
    scene e3cagemantwo9 with mediumdissolve
    stop seven fadeout 3
    jk "And we'll see if later you can get a real reward from me..."
    if busyboy:
        jk "But I do believe you have another appointment with Scarlett, don't you?"
        jk "Chanel will take you to her in a bit. I'll be seeing you again real soon."
        jump pegging
    else:
        jk "But for now, I think we're done."
        jk "I'll be seeing you again real soon. Chanel will take you to your next appointment."
        p "(More?)"
        jump k4endpath

label pegging:

    scene e3pegging1 with longfade

    play seven "music/samintro.mp3" fadein 3

    sc "Well, there you are [pname]. Welcome to the shower room. I'm so glad we could see each other so soon after your arrival here."
    if busyboy:
        sc "I hope Junko saved enough of you for me. She's so sweet isn't she?"
        sc "I'm not sweet [pname]. And I want to have some fun...at your expense."
    else:
        sc "I'm looking so forward to...welcoming you to my world."
        sc "But if you are obedient and please me, I really am a wise choice for protection. You'll survive this place if you listen to me."
    scene e3pegging2 with mediumdissolve
    sc "But don't get any foolish notions looking at my body [pname]. You are a long way away from getting to play with me that way."
    sc "Right now, I just want to...sample my merchandise."
    scene e3pegging3 with mediumdissolve
    sc "I also want to make sure you understand who you are dealing with right now. Have you seen the snake accessories a few of us wear?"
    sc "I have some, as does Chanel here."
    p "Yes, I have noticed them. What about them?"
    scene e3pegging4 with mediumdissolve
    sc "It signifies a special job. For the program, we will be assisting in numerous ways, but our real work is serving as spies and assassins for The Karlsson Group."
    sc "And we all share a common trait. All of us...greatly enjoy destroying anyone that crosses our path. It gets us very hot and thirsty for...release."
    chan "Very hot..."
    scene e3pegging5 with mediumdissolve
    sc "And I don't want you getting any bright ideas that you can handle us. We are not ordinary guards, but highly trained killers with years of training."
    sc "Any of us could literally kill you quite quickly and easily. Keep that in mind if you get any foolish thoughts about being disobedient."
    scene e3pegging6 with mediumdissolve
    sc "Now, you're here to pay your tribute to me for some of my knowledge and protection. And I'm ready to have some fun. So strip."
    sc "I want to get comfortable as well, so I'll be right back. Chanel, please take care of my bitch."
    scene e3pegging7 with mediumdissolve
    chan "[pname], your dick isn't even awake! But you were with Veronica Karlsson recently, yes?"
    p "Yes. She..."
    chan "...I know. Maybe your poor little weenie still hasn't recovered from her testing. Not that you need it right now."
    scene e3pegging8 with mediumdissolve
    chan "I'm almost sad I didn't get first crack at you. But it was Scarlett and Junko's turn to go first. Oh well."
    chan "You should feel complimented in a way. They both wanted you over quite a few other candidates. So that's something, right?"
    scene e3pegging9 with mediumdissolve
    chan "But enough chit chat."
    chan "I think it's time to get down on the floor where you belong. Let me just help you get down faster!"
    p "Wait, what the...!"
    scene e3pegging10 with mediumdissolve
    chan "Oh [pname], we really need to teach you a lot about balance, haha!"
    scene e3pegging11 with mediumdissolve
    chan "You know [pname], if I had a dollar for every time I had a slut like you on the ground below me..."
    chan "I think I want to try and wake your dick up!"
    scene e3pegging12 with mediumdissolve
    chan "Maybe this will help!"
    p "Ow!"
    scene e3pegging13 with mediumdissolve
    sc "Thanks for keeping [pname] warm for me Chanel. I think I'm ready to have some fun now."
    chan "Can I stay and watch?"
    sc "Of course! It's always more fun to have an audience."
    scene e3pegging14 with mediumdissolve
    sc "This isn't my favorite way to play [pname], but I feel it best allows you to quickly understand your position here. As my bitch."
    sc "Consider yourself lucky too. This is the smallest dildo I have. Now get up on your knees."
    scene e3pegging15 with longdissolve
    sc "Now, I'm going to use this little toy on your ass. But, if you want...I'm giving you a chance to suck on it right now."
    sc "Think hard about this. You might want some of your saliva on it. If you don't, I'm going in on you dry...very dry."
    stop seven fadeout 3
    p "(Shit...)"
    menu:
        "(It's going to hurt a lot more if I don't get it a little wet somehow. I better suck on it.)":
            scene e3pegging15b with mediumdissolve
            p "Mmmppgfff"
            sc "Ah, did your fear of feeling gay for sucking on a cock not overcome your fear of a dry ass reaming? Good job, [pname]!"
            scene e3pegging15c with mediumdissolve
            chan "Scarlett, he might be better at sucking dick than we are, haha!"
            sc "Lucky for you there aren't many male clients at this facility, or maybe you'd be a popular little thing!"
            jump peggingtwo
        "(I am not going to suck on even a fake dick. I'll take my chances.) [gr]\[InjuredAss\]":
            scene e3pegging15d with mediumdissolve
            $ injuredass = True
            p "I'll take my chances I guess."
            sc "Oh good! I'll make sure to make it hurt as much as possible."
            jump peggingtwo

label peggingtwo:

    scene e3peggingtwo1 with mediumdissolve

    play seven "<from 60 to 188>music/femdom2.mp3" fadein 3

    sc "Now I want you to get in a kneeling position for me, and stick your ass nice and wide for me!"
    chan "I want to see his pathetic face from the front!"
    sc "Be my guest Chanel!"
    scene e3peggingtwo2 with longfade
    sc "You have a cute ass [pname]. I'm glad you're so worthless so that you have to turn to me for protection."
    sc "Are you ready [pname]?"
    chan "He looks so scared Scarlett. But maybe he likes being your bitch!"
    scene e3peggingtwo3 with mediumdissolve
    sc "Some men do Chanel..."
    sc "...but let's take this in and see how it feels."
    scene e3peggingtwo4 with mediumdissolve
    p "Woah, oh shit...!"
    sc "Oh sweetie, you're so tight! I wonder how many times you've said that to a woman!"
    scene e3peggingtwo5 with mediumdissolve
    sc "It never gets old fucking a virgin ass. At least I'm pretty sure it's a virgin ass, haha! This must be quite a shock to you [pname]."
    chan "You should see his face too! Poor thing...poor poor [pname]. And this is only your first night here."
    sc "Next time I need to do it in front of a mirror so I can see his face too!"
    scene e3peggingtwo6 with mediumdissolve
    chan "How does it feel [pname]?"
    chan "Maybe it's too late for you but you can always try and get a different sponsor later. But let me distract you from your ass..."
    scene e3peggingtwo7 with mediumdissolve
    chan "...by giving you some additional stimulation...*slap*...on your pathetic face...*slap* *slap*..."
    chan "Maybe you should fuck his mouth Scarlett!"
    scene e3peggingtwo8 with longdissolve
    sc "Maybe next time, I'm really getting into a nice rhythm here!"
    sc "It's so much better pulling him arms this way. I can really get all the way in so easily!"
    scene e3peggingtwo9 with mediumdissolve
    sc "So easy to go..."
    scene e3peggingtwo10 with quickdissolve
    sc "in...and..."
    scene e3peggingtwo9 with quickdissolve
    sc "out and back..."
    scene e3peggingtwo10 with quickdissolve
    sc "in..."
    scene e3peggingtwo11 with mediumdissolve
    sc "Chanel, remind me to punish him later for my knees being a little uncomfortable on this hard floor. It's his fault after all!"
    chan "Yes, that's so inconsiderate of you [pname]. Making Scarlett experience such painful discomfort..."
    scene e3peggingtwo12 with mediumdissolve
    chan "I think I need a session with you too [pname]. You hurt my feelings by making my dear friend Scarlett suffer."
    sc "Uh uh, he's taken for now. Wait your turn."
    scene e3peggingtwo13 with mediumdissolve
    sc "I think it's time to really...drive my last point home. You'll do whatever I say if you know what's good for you."
    sc "If you don't, imagine if I pass you off to...every...single...person...down here..."
    scene e3peggingtwo14 with mediumdissolve
    sc "You'll be a good boy won't you [pname]?"
    p "Yes! I got it! Just wrap it up please!"
    scene e3peggingtwo15 with mediumdissolve
    chan "Aww, maybe he's going to cry?"
    sc "Just a few more hard thrusts [pname], I really want your first night here to be memorable."
    scene e3peggingtwo16 with mediumdissolve
    sc "Oh yeah, just about done..."
    scene e3peggingtwo17 with mediumdissolve
    sc "I think that's enough! Say thank you [pname]!"
    p "...thank you..."
    stop seven fadeout 3
    scene e3peggingtwo18 with longfade
    sc "You held up pretty well [pname], but I also took it pretty easy on you."
    sc "If you make me happy, then maybe...just maybe, you'll be ok. I'll have Chanel take you now to your next appointment."
    p "(More?)"
    jump k4endpath

label freeagent:

    scene e3freeagent1 with longfade
    chan "Almost there [pname]..."
    scene e3freeagent2 with longfade
    chan "Ah, here we are!"

    play seven "music/freeagent.mp3" fadein 2

    p "What is this place and oh..."
    scene e3freeagent3 with mediumdissolve
    ky "Welcome [pname], I've been expecting you."
    ky "Come on down so we can have a nice chat. I'm hoping we can get to know each other a little better."
    p "(...)"
    scene e3freeagent4 with mediumdissolve
    ky "You know [pname], I'll at least give you this...you might be the only slut in recent memory here that is close in height to Chanel and myself."
    ky "Without our heels, you're right there with us. That's honestly a little refreshing, as the two of us are so used to looking down figuratively and literally on men."
    scene e3freeagent5 with mediumdissolve
    ky "But enough of that. I want to show you what awaits you if you get demoted to K3 during your stay here."
    ky "This is one of the main areas for the lucky sluts that manage to achieve such an exalted rank."
    scene e3freeagent6 with mediumdissolve
    ky "This area is also very popular with us, because this is the first area we are allowed to...indulge ourselves in ways we can't with higher rated prisoners...sorry...participants."
    ky "There are actually three areas for this rank, but these are their living facilities."
    scene e3freeagent7 with mediumdissolve
    ky "Come take a look at their rooms. At least they get their own space versus having to share like you do now."
    ky "Why don't you open one of them?"
    p "(Ok...)"
    scene e3freeagent8 with mediumdissolve
    ky "Not very comfortable looking is it?"
    p "No."
    ky "This could be your home [pname]...if you don't make the ones who control your fate happy."
    scene e3freeagent9 with mediumdissolve
    ky "The Karlsson sisters and the Head Warden are at the top of the food chain here, and can control your fate the most."
    ky "But practically, someone like me will have much more day to day control over your life...and your rank."
    ky "Now you're going to get into a more comfortable position so I can discuss what I want from you."
    scene e3freeagent10 with mediumdissolve
    ky "Chanel, let's stretch him a little lying down, and [pname], I highly suggest you comply and not resist."

    stop seven fadeout 2
    menu:
        "(I don't think I better mess with these two of all people. I better just comply.) [ChanelPath] [KiyomiPath]":
            scene e3freeagent10b with mediumdissolve
            p "Alright. I guess I have no choice."
            ky "[pname], we're just going to have a short chat for now! Relax."
            jump freeagent2
        "(Maybe I should assert myself a little by resisting and see how they respond.)":
            scene e3freeagent10c with mediumdissolve
            $ chanel_p -= 1
            $ kiyomi_p -= 1
            p "Now wait a minute...I don't think..."
            scene e3freeagent10d with quickdissolve
            p "Ugh!"
            ky "I was not making a suggestion [pname]. Don't test me again as I could have kicked you a lot harder just now."
            jump freeagent2

label freeagent2:

    scene e3freeagent11 with longfade
    ky "That's better. I hope you have a strong back [pname]."

    play seven "music/freeagent2.mp3" fadein 3

    ky "I'm trying to decide if I should go heels or feet for him. What do you think Chanel?"
    chan "He looks tough enough. Heels shouldn't bother him too much."
    scene e3freeagent12 with mediumdissolve
    ky "Perhaps."
    ky "You look like you have a strong back...let's see if your shoulders are strong enough too [pname]."
    p "(Wait is she going to...)"
    scene e3freeagent13 with mediumdissolve
    p "(Shit!)"
    ky "So [pname], I am pleased you turned down both Scarlett and Junko earlier. I do get along with both of them, and while Scarlett is a part of my team, she's always been a loose cannon."
    ky "I have three other girls on my team that I need to keep happy. Now they have so much passion and joy for their work, but they do need play time too."
    scene e3freeagent14 with mediumdissolve
    ky "So consider making yourself available to my...I should say...our needs. You make us happy, and maybe life for you in here won't be so bad."
    ky "I may be a ruthless killer [pname], but I am also very honorable and my word, unlike many here, is never broken."
    ky "Now...I could just force you to do a lot of things, but it's so much better if you quietly please us so as not to draw attention from the highest executives here."
    scene e3freeagent15 with mediumdissolve
    ky "Your life will be considerably easier if I am happy with you. Our team is also training...and grading many aspects of your performance here."
    ky "So just listen to what I want from you, and then I'll leave it up to you how you want to proceed."
    scene e3freeagent16 with mediumdissolve
    ky "The first and most obvious thing I will want is for you to indulge my team when they are feeling the itch."
    ky "We won't overload you all at once. I understand you will have a lot to deal with soon in here."
    ky "But I will expect you to be at our beck and call most of the time. Think of yourself as being like the...mascot of our group, The Deadly Vipers."
    scene e3freeagent17 with mediumdissolve
    ky "The other thing I want from you is information on the other prisoners. No specific thing, I just want to be able to pick your brain at times."
    p "You want me to be a snitch."
    scene e3freeagent18 with longdissolve
    ky "You should think of your survival more than what your fellow prisoners will think. Most of them are nothing but tools for cruel and sadistic fantasies."
    ky "Chanel, let's get him up now. I can tell he's very close to being in trouble with me on him. See how nice I am [pname]?"
    scene e3freeagent19 with longfade
    ky "There we go. One more thing [pname]. It is almost impossible for a person starting at K4 to move up ranks here."
    ky "Once you are tagged a certain way, you are already kind of on the loser track. But...I am uniquely qualified to help you with that too."
    ky "So even though you have had a very poor start, you may be able to move up the ranks with my help."
    scene e3freeagent20 with mediumdissolve
    ky "So the bottom line is if you make me happy, I can do a lot for you too. But I want to know how you feel about it now, because otherwise I need to find someone else."
    ky "So what will it be?"
    scene e3freeagent21 with mediumdissolve
    p "(Having to make a major decision like this on the fly again with no guarantees or knowledge if she will even keep her word...)"
    p "(She says she is a killer but yet is an honorable person with her word being unbreakable? And how will they really treat me?)"
    ky "Well?"
    menu:
        "(Somehow, I feel like the best decision is to accept Kiyomi's proposal. I think her offer could end up helping me in the long run.) [KiyomiPath]":
            $ kiyomi_p += 1
            $ vipertoy = True
            $ freeagent = False
            scene e3freeagent21b with mediumdissolve
            p "It's hard for me to just trust anyone, but it's not like I have a lot of options right now either. I'll have to hope you will actually help me."
            ky "Wise decision [pname]. You will see I am a woman of my word. But, we are a lot to handle as well. We wanted you because you look tough enough."
            scene e3freeagent21c with mediumdissolve
            p "I see."
            ky "Oh don't whine [pname]. Any of us could permanently hurt you if we wanted...you aren't that kind of target...if you're a good mascot for us."
            ky "But I am pleased you will be a friend of our little team."
            scene e3freeagent21d with mediumdissolve
            ky "I'll be seeing you tomorrow. Get some rest, as training will not be easy."
            ky "Chanel, why don't you take him to his last appointment for today?"
            p "(More??)"
            stop seven fadeout 3
            jump k4endpath
        "(I...I just can't risk accepting any kind of offer without knowing more safely that it is a wise decision. Perhaps it's also wise to not be tied to anyone on literally the first day.) [VeronicaPath]":
            $ veronica_p += 1
            $ kiyomi_p -= 2
            scene e3freeagent21e with mediumdissolve
            p "I...I just can't accept your offer. I just can't right now."
            ky "I did leave it up to you. I thought you would be smart, but instead you've annoyed me. Now we will have to force some things on you."
            scene e3freeagent21f with mediumdissolve
            ky "And your training and how you are graded will be so so so much tougher for you..."
            stop seven fadeout 3
            ky "Oh...let me show you one more thing too. Let me just get it out..."

            play seven "<from 665 to 700>music/darkmix7.mp3" fadein 2

            scene e3freeagent21g with longfade
            ky "Look..."
            p "[pname4]!"
            ky "I believe you know Katsumi. Did you know she's my sister? We are so close. And we do a lot...together. Including tormenting weak and pathetic men."
            scene e3freeagent21h with mediumdissolve
            ky "I wonder how much your precious [pname4] will suffer under the expert care of the two of us? He's so small, sick, and helpless isn't he?"
            p "You can't..."
            ky "...Oh, but I can. And now, I will. With extra special love and care courtesy of his big brother. You blew it [pname]."
            chan "Kiyomi, I bet he's a good screamer..."
            stop seven fadeout 3
            scene e3freeagent21i with longdissolve
            ky "Chanel, take him to his last appointment for today. I'm looking forward to seeing you tomorrow [pname]. You better get some rest with what I have in store for you..."
            p "(Shit...[pname4]...)"
            jump k4endpath

label k4endpath:

    scene e3k4endpath1 with longfade
    chan "I bet you had so much fun today already...poor baby."

    play seven "music/k4endpath.mp3" fadein 3

    chan "Now, one last stop [pname], and then you can go back to your miserable little pig pen with [pname2]."
    chan "I hope you have a strong back for sleeping on concrete, haha!"
    scene e3k4endpath2 with longfade
    p "What is this place?"
    chan "You don't get to ask questions without permission [pname]!"
    chan "But I will say there are lots of strange rooms and places down here. You have no idea how huge this facility actually is..."
    scene e3k4endpath3 with mediumdissolve
    chan "Now, I need you to stay right where you are and not move towards the middle of the room."
    p "Ok."
    scene e3k4endpath4 with mediumdissolve
    chan "Alright, here we go."
    scene e3k4endpath5 with longfade
    p "(Woah...)"
    chan "Let's head down now. You have one last person waiting to see you today."
    scene e3k4endpath6 with mediumdissolve
    chan "When we get down to the bottom, we will be going left."
    chan "Believe me, you don't want to go right. Even I'm scared of that place."
    p "(What could have even her spooked?)"
    scene e3k4endpath7 with longfade
    chan "You'll be meeting just past this door."
    p "(Did not expect that kind of changed environment...)"
    scene e3k4endpath8 with longfade
    chan "Here we are. Not many sluts like you get to see this room. Now...I'm going to go and let your requestor know that you are here."
    chan "She's a very high level executive, so I expect you to get on your knees right now with your head straight down and stay that way until she arrives!"
    scene e3k4endpath9 with longdissolve
    chan "Good. I think I'm going to enjoy this...and you better stay exactly like that."
    chan "I'll be back."
    stop seven fadeout 3
    scene e3k4endpath10 with longfade
    p "(Oh, I hear them coming...)"

    play seven "music/k4ending.mp3" fadein 3

    if proboss:
        scene e3k4endpath11 with longfade
        chan "[pname]...I'm so glad to be able to be here for this introduction."
        chan "Meet the Head Warden of the prisoner program...you can lift your pathetic head now."
        scene e3k4endpath11b with mediumdissolve
        p "(Great...another cruel bitch...)"
        scene e3k4endpath11c with longfade
        p "(What??!)"
        sis "Hello [pname]."
        scene e3k4endpath11d with mediumdissolve
        p "[pname3]????"
        stop seven fadeout 2
        scene black with mediumflash

        pause 2

        jump episodethreeend
    else:

        scene e3k4endpath12 with longfade
        chan "[pname]...I'm so glad that I can see your face for this introduction."
        chan "Meet the Head Warden of the prisoner program...you can lift your worthless head now."
        scene e3k4endpath12b with mediumdissolve
        p "(These boots...another cruel bitch...)"
        scene e3k4endpath12c with longfade
        p "(What the hell?!?)"
        sis "Hello [pname]."
        scene e3k4endpath11d with mediumdissolve
        p "[pname3]????"
        stop seven fadeout 2
        scene black with mediumflash

        pause 2

        jump episodethreeend

label vmeet:

    scene e3vmeet0 with longfade
    p "(Wow, what is this place? Very high tech...and it looks like chambers...for people?)"
    chan "Mistress Veronica, I've arrived as instructed."
    scene e3vmeet1 with longfade

    play seven "music/vmeet2.mp3" fadein 3

    v "Ah, Chanel. I appreciate you bringing [pname] down here to see me."
    chan "You're welcome, Mistress."
    scene e3vmeet2 with mediumdissolve
    v "I've heard great things about you from Kiyomi. Elena should be very proud of you."
    chan "Thank you, Mistress. I am really enjoying being a part of her team."
    v "I trust [pname] has seen his quarters and is ready for the start of the program?"
    scene e3vmeet3 with mediumdissolve
    if k5:
        chan "Yes, Mistress. [pname] is rooming with Prisoner Kwame for the start of the program."
        v "Of course. Our saboteur in the mines. He was actually quite clever in covering his tracks, but unfortunately for him...I did discover his activities."
        jump vmeettwo
    else:
        chan "Yes, Mistress. [pname] has been given a proper room befitting his K6 status to start the program."
        v "Very good. I trust you will do an exemplary job as his liasion during his stay here."
        chan "Of course, Mistress Veronica. I will serve with distinction."
        jump vmeettwo

label vmeettwo:

    scene e3vmeet4 with mediumdissolve
    v "I'd like you to report to Alessandra and update her on what we discussed earlier today."
    chan "Of course, Mistress."
    scene e3vmeet5 with mediumdissolve
    chan "[pname], don't get any funny ideas down here. Mistress Veronica is more than capable of handling herself."
    v "Chanel, there is no need for that. I know that [pname] is an intelligent man, and I am confident he will act accordingly. Get to your task and I will call for you later."
    scene e3vmeet6 with longfade
    v "So...here we are again [pname]. It's certainly intriguing that you ended up with me instead of one of my sisters."
    v "I was definitely the most picky and critical in terms of standards for possible sponsorship, and yet here you are..."
    p "(Sponsorship?)"
    scene e3vmeet7 with mediumdissolve
    v "This room is an area for experimentation. I've been testing numerous theories on the human body and mind."
    p "I see. And these chambers? What do they do? It says Virtual Reality on them too?"
    v "They were originally designed for that purpose, but it is now a minor function of the overall capabilities of these testing chambers."
    scene e3vmeet8 with mediumdissolve
    v "But for now, I'd like to move on as to why you are actually in a position to speak to me right now. Surely you are quite curious as well?"
    p "Yes, of course. This entire situation for me is a complete...well to be frank...a complete shitshow."
    v "I certainly can imagine that is the case. Having to function with little to no information and only a modicum of control must be quite frustrating."
    scene e3vmeet9 with mediumdissolve
    v "Let me ask you [pname]...why do you think you were given the offer to come here by Elena?"
    v "Do you realize you are the only prisoner she personally invited to participate in this program?"
    p "Yes, I do."
    scene e3vmeet10 with mediumdissolve
    v "Out of all the people in the world, she decides to approach you. A top executive of the most powerful corporation on the planet..."
    v "You may have been able to deduce that she was ordered to do so by someone even above her. But why you...do you have a theory as to why?"
    scene e3vmeet11 with mediumdissolve
    p "(I've thought it strange from the very beginning that Elena only approached me. Also...my unique cell and treatment in jail. It always felt targeted to me...)"
    p "(She expects a decent theory...I think I have one...)"
    stop seven fadeout 3
    menu:
        "(I think there was something about the combination of my behavior, brains, and looks during my stay in prison that garnered their attention...)":
            $ veronica_p += 1
            scene e3vmeet11b with mediumdissolve
            p "Well...one guess I have is that during my prison stay, I was carefully evaluated for a combination of desired variables."
            p "Things like mental toughness, brains, looks...and that I tested very favorably for the goals of this program."
            v "That's not a bad guess [pname]. Quite logical, and a reasonable theory based on what little information you have at your disposal."
            scene e3vmeet11c with mediumdissolve
            v "But that doesn't really adequately explain why they would send Elena to meet you specifically. They could have easily treated you the same as any other program participant."
            p "That's a good point. But I don't really have a better theory right now. Why did Elena come to talk to me specifically?"
            v "Ah, now that is the question, isn't it [pname]?"
            jump vmeetthree
        "(I still believe I was set up when I was trying to defend [pname4]. I think I was railroaded into jail in the first place by someone with a grudge against me.)":
            scene e3vmeet11d with mediumdissolve
            p "Well...I believe I was deliberately targeted and set up when I was arrested and ultimately sent to jail. Perhaps someone has a grudge agaisnt me and is taking revenge."
            v "Hmm, that's certainly plausible, but it would take a very powerful person to arrange something of that nature."
            scene e3vmeet11e with mediumdissolve
            v "And logically, is it likely you interacted with someone with that kind of power in your everyday life?"
            p "True, but I don't really have a lot of information. What happened to me makes sense with someone with an extreme grudge against me...even if I don't know how or why..."
            v "Fair enough. And obviously, what happened to you did happen. For some reason. The actual reason...now that is the question, isn't it?"
            jump vmeetthree
        "(I'm convinced there is something about me specifically that is important. I think Elena hinted at it...and then there's my mom...a lot doesn't make sense with her.) [VeronicaPath]":
            $ veronica_p += 1
            $ veronica_scale += 1
            scene e3vmeet11f with mediumdissolve
            p "I...I have a thought on this...I think there is something about me specifically that is important as to why I am here. Not just how I have tested so far..."
            p "...but even who I am. I never knew my father, and my mother...a lot doesn't add up to me."
            v "A very interesting thought process. I would encourage you to continue this train of thought...please elaborate on what doesn't add up to you."
            scene e3vmeet11g with mediumdissolve
            p "Well, like...my mother. It's so clear to me she was way too smart to be stuck where she was...even in our crazy world today."
            p "She was clearly a brilliant person...but also mysterious. I know in my heart she did the best she could with us...but I also feel like I missed a part of her somehow..."
            v "You are very correct on all counts. But what are the missing pieces about your mother, and did that bring you here? Now that is the question, isn't it?"
            jump vmeetthree

label vmeetthree:

    scene e3vmeetthree1 with longfade
    v "So let's discuss this further. [pname], you are here for who you are...and it's for far more than just this program. Let me fill in at least one blank for you..."

    play seven "music/vmeet2.mp3" fadein 3

    v "...but don't expect all of the answers to your questions either."
    $ momknowledge = True
    v "Your mother and my father were once a couple and apparently very much in love. I don't really know the details as I wasn't there obviously...but it seems to be the case."
    p "My mother...and Alexander Karlsson? Holy..."
    scene e3vmeetthree2 with mediumdissolve
    v "But something happened. I don't know what that was...but your mother fled the Karlsson world and hid from my father."
    v "I probably can't blame her. My father was a monster when I was growing up. Maybe she saw the start of that..."
    scene e3vmeetthree3 with mediumdissolve
    v "And the bottom line [pname] is that you are here...because of your mother. That's all I will say for now."
    p "Wow...I'm a little speechless right now..."
    v "...And since you have made the cut so to speak to get in this room with me, I am willing to help you."
    scene e3vmeetthree4 with mediumdissolve
    v "But I want to be clear that I will stop if you displease me. I expect you to be worth my help."
    p "Ok...what do you want from me?"
    scene e3vmeetthree5 with mediumdissolve
    v "You got this meeting with me because you have displayed some level of intelligent and pragmatic thinking so far."
    v "You are not bound completely by a strict moral code of right and wrong, but you are also not needlessly cruel or evil either."
    v "I believe one needs this approach to handle the immense power possible in this environment. Rational and balanced thinking. So I want you to continue this pattern of behavior."
    scene e3vmeetthree6 with mediumdissolve
    v "Now others you may meet may offer help with say information, but I can immediately offer you practical help. This chamber right here can do that."
    p "How?"
    v "It will enhance your body and mind just enough to give you a little bit of an advantage during this program. It doesn't guarantee success, as your effort and willpower matters a great deal."
    v "But, this will give you a little bit of an edge in physical and mental performance if you can harness it properly. You can also come in more than once for it as it does wear off over time."
    scene e3vmeetthree7 with mediumdissolve
    p "(Sure...let's just get in there and not be suspicious at all...)"
    v "[pname], it's clear that you do not trust me yet. I certainly understand that...so let me show you personally there is nothing to fear from me...today."
    scene e3vmeetthree8 with mediumdissolve
    p "Hey, what are you doing?"
    v "I'll get in there first and use it on myself as a show of good faith."
    scene e3vmeetthree9 with longdissolve
    v "You can see the start setting yourself. Just activate it on the screen."
    v "It only takes less than thirty seconds in here to administer a full battery."
    scene e3vmeetthree10 with longfade
    p "(Hmm, no fancy light show, but it's humming quite loudly...)"
    scene e3vmeetthree11 with longdissolve
    v "Ahh, that always feels great. I'm already a genius [pname], but this only helps me that much more with mental clarity."
    p "And so humble."
    v "[pname], it is not my ego talking. I am not that kind of person. I deal with facts, and what I said is objectively true."
    scene e3vmeetthree12 with longfade
    v "Now, your turn. Go ahead and get in. Keep in mind [pname] that if I really wanted you harmed, I wouldn't need to resort to subterfuge to do so."
    p "Fair enough...ok..."
    scene e3vmeetthree13 with longdissolve
    v "Just hold still."
    p "(Here goes nothing...)"
    scene e3vmeetthree14 with mediumdissolve
    p "(It really tingles. But wow, it does feel really good.)"
    v "There we go. You can come out now. Let me grab my coat too, and don't rush out."
    stop seven fadeout 3
    scene e3vmeetthree15 with longfade
    v "How do you feel?"
    p "Wow. I do feel great. It's like I am wide awake but also really focused. You weren't kidding. How long does this last?"
    v "It depends for each individual. We'll have to see how you react to it, but we can figure that out over multiple sessions."
    scene e3vmeetthree16 with longdissolve
    $ veronica_sponsor = True
    v "Now, we'll talk again soon, but I have other things to attend to right now. I can and will share information with you as it suits me. Use it well."
    v "But for now, I'll have Chanel take you back to your room."
    p "Ok..."
    jump epthreedomend


label jmeet:

    scene e3jmeet1 with longfade
    j "Chanel, so good to see you again. I trust Kiyomi is treating you well?"
    play seven "music/juliettemeet2.mp3" fadein 3
    chan "Yes, Mistress. I am really enjoying being a part of her team."
    j "Wonderful. I appreciate you bringing [pname] here. I trust he has been processed and settled into his room?"
    scene e3jmeet2 with mediumdissolve
    if k5:
        chan "Yes Mistress. [pname] is rooming with Prisoner Kwame for the start of the program."
        j "Ahh, Dominique's little rebel. He caused a lot of trouble for our mining operations."
        jump jmeettwo
    else:
        chan "Yes, Mistress. [pname] has been given a proper room as a K6 prisoner starting the program."
        j "Yes, that's quite impressive. The only other person to ever start as a K6 eventually was on our Board. Maybe you'll have to grovel at his feet someday Chanel."
        p "(Hmmm...)"
        jump jmeettwo

label jmeettwo:

    scene e3jmeet3 with mediumdissolve
    j "How many people has your team dealt with this month?"
    chan "About twenty. Kiyomi has been really busy."
    j "Excellent. Sometimes I think she has the best job in the entire company."
    scene e3jmeet4 with mediumdissolve
    j "Now, I think it's time you left us alone Chanel. I have some things to discuss with our new program participant."
    chan "Yes, Mistress. And [pname], don't get any ideas about doing anything stupid around Mistress Juliette. That would be an instant death sentence for you."
    j "Chanel, there is no need to threaten [pname]. If he's smart enough to get a meeting with me, I am confident he knows it's to his advantage to endear himself to me."
    scene e3jmeet5 with mediumdissolve
    j "Now, leave us alone, and send for Dumbo. I will need him here."
    chan "Yes, Mistress."
    j "And [pname], come on up here so I can get a better look at you..."
    scene e3jmeet6 with longfade
    j "Well, you interrupted my bath time, but that's ok. I've been looking forward to meeting you for a long time [pname]."
    j "You're not so bad on the eyes. But is your mind attractive enough to play with the likes of me? We shall see."
    j "And what about me? When you look at me, what is your first impression?"
    scene e3jmeet7 with mediumdissolve
    p "(How do I want to handle this one...)"
    menu:
        "(My gut is that she wants to hear an aggressive answer. I should just flat out say I want to fuck her brains out and take my chances it won't upset her) [JuliettePath]":
            $ juliette_p += 2
            scene e3jmeet7b with mediumdissolve
            p "I'll be blunt. When I look at you, I just want to fuck your brains out."
            j "Good. Blunt honesty is fine with me [pname]. Only that kind of man might actually get to fuck me...but you need more than bluntness to get me horny."
            jump jmeetthree
        "(I think I should focus on more than just her appearance. I should tell her she's hot but that I am intrigued by her mind as well.)":
            $ juliette_p += 1
            $ juliette_scale += 1
            scene e3jmeet7c with mediumdissolve
            p "You're definitely super hot. Very desirable. But, I want to know what makes your mind tick too. That can be just as hot as one's looks."
            j "Oh you're in for a treat [pname]. My mind is very unique and I hope you can handle it. We'll see."
            jump jmeetthree
        "(Truth be told, I'm both a little intimidated and curious about her. It might be smart for me to respect her position, but also try and learn more about her.)":
            $ juliette_p += 1
            $ juliette_scale -= 1
            scene e3jmeet7d with mediumdissolve
            p "I understand how much power you have, and it does intimidate me a little. But I really want to get to know someone like you and learn more."
            j "I appreciate your honesty, and if you learn to please me...I will be more than happy to teach you the true pleasure of power."
            jump jmeetthree

label jmeetthree:

    scene e3jmeet8 with mediumdissolve
    j "Now, do you know why you have managed to get into a room with me tonight?"
    p "No."
    j "It's because you have shown some tendencies very early in being...a very naughty boy. And bad boys get to talk with me..."
    j "But I'm not a big believer in waiting to find out something. I want to know right away just how bad you really are."
    scene e3jmeet9 with mediumdissolve
    j "So I'll keep this very blunt as well [pname]. Program participants can benefit in here from having sponsors quietly helping them do well in here."
    j "If you show you have the traits I want, then I may decide to help you. If you don't show that, then you'll have to find someone else."
    stop seven fadeout 3
    j "And, if I really like you...sponsorship may only be the start of our...interactions together."
    jump dumbotime

label dumbotime:

    scene e3dumbo1 with longdissolve
    play seven "music/dumbotime.mp3" fadein 3
    j "Ah, there you are Dumbo. I'm so glad you are able to join us. I have a new task for you."
    db "Yyyyyyyyyeeeeeeeeeesssssss........Mmmmmmmiiiisssssstresssssss....."
    p "(What the hell is wrong with him? His speech and especially his eyes, is he on something?)"
    scene e3dumbo2 with mediumdissolve
    j "I can see you noticed right away that Dumbo's name is very accurate. The poor thing has had his brain essentially turned into mush."
    j "But he's a very functional servant for me. He does everything I ask and has been nothing but perfect for me."
    p "I see. What made him like this?"
    scene e3dumbo3 with mediumdissolve
    j "Oh, he just drank something that wasn't too helpful for his mental state. Very bad luck for him..."
    p "(Uh huh...)"
    scene e3dumbo4 with mediumdissolve
    j "Now Dumbo, come on up here. I want you to lie down next to my bath here. Nice and flat."
    db "Yyyyeeesssss......Mmmmiiissstttrreessss."
    scene e3dumbo5 with longdissolve
    j "There we are. You look so wonderful Dumbo, and you've been such a good servant. Maybe it's time for a reward."
    j "But...I'm ready to test you now [pname]. I want to see how naughty you really are..."
    p "How?"
    scene e3dumbo6 with mediumdissolve
    j "Let me just grab something here behind me. A nice little cocktail for my man servant."
    scene e3dumbo7 with mediumdissolve
    j "I want you to inject this into Dumbo."
    p "What does it do?"
    j "It will cause most of his body to become paralyzed, especially his lower extremities. He may be able to still move his head, but likely nothing else."
    scene e3dumbo8 with mediumdissolve
    p "Is this my test? Is the paralysis permanent?"
    j "No to both [pname], this is just the start. Your real test is my second needle. Don't fret about this shot [pname], it does nothing permanent."
    p "(Ok...)"
    j "Inject it anywhere you like, it doesn't really matter."
    scene e3dumbo9 with longdissolve
    p "Alright, here we go..."
    j "Good...now let's just wait about a minute or so. You can place that needle down somewhere too."
    scene e3dumbo10 with longfade
    j "Perfect. He's completely helpless now."
    j "Dumbo, you've been such a good servant. But I'm bored of you now. So I think I need someone new."
    scene e3dumbo11 with mediumdissolve
    j "[pname], I have a second shot below you. This is your test. Put simply, this shot will cause his breathing to shut immediately down, and he will suffocate to death."
    j "And don't get any funny ideas about trying something. I am quite immune to this shot, as are all of my sisters."
    j "The bottom line to win in this environment, and especially with me...you must be willing to be ruthless and even kill to get what you want. Are you that type of man?"
    scene e3dumbo12 with mediumdissolve
    stop seven fadeout 3
    p "(Holy shit, she wants me to...this is a big decision...)"
    menu:
        "(I...there's just no way I can actually kill anyone. That's going way too far with being ruthless. I'll have to take my chances that Juliette is ok with that...) [GoodPath]":
            $ good += 3
            $ juliette_p -= 5
            scene e3dumbo12b with mediumdissolve
            p "I'm sorry...there's just no way I can kill someone for no reason. I guess I'm not as ruthless as you would like."
            j "Yes. It seems so."
            scene e3dumbo12c with mediumdissolve
            j "You'll have to find someone else to help you in this place [pname]. It won't come from me."
            j "I'll have Chanel take you back to your room."
            jump epthreedomend
        "(I'm willing to be ruthless, but I want to know what I get out of it too. She's probably going to kill him if I don't anyway, but I should still ask...) [JuliettePath]":
            $ juliette_p += 1
            $ juliette_scale += 1
            scene e3dumbo12d with mediumdissolve
            p "I'm willing to do what it takes, but not without a reason. What will I get out of this if I do what you ask?"
            j "Very fair question [pname]. Put simply, you will pass my first test for you. That will get you some help from me directly in here."
            scene e3dumbo12e with mediumdissolve
            j "That's not a guarantee forever, because you could screw up later, but for now...you'd have my support. It's up to you what you want to do."
            menu:
                "(I'm willing to kill. I have to survive in here, and better him than me.) [JuliettePath] [EvilPath]":
                    $ evil += 3
                    $ juliette_p += 3
                    $ juliettesponsor = True
                    scene e3dumbo12f with mediumdissolve
                    p "Alright...I'll do it."
                    play seven "music/murder.mp3" fadein 3
                    j "Excellent! Go ahead then..."
                    jump murderer
                "(I...I can't do it. I can't kill someone.) [GoodPath]":
                    $ good += 3
                    $ juliette_p -= 5
                    scene e3dumbo12b with mediumdissolve
                    p "I'm sorry...there's just no way I can kill someone like this...I guess I'm not as ruthless as you would like."
                    j "Yes. It seems I misjudged you."
                    scene e3dumbo12c with mediumdissolve
                    j "You'll have to find someone else to help you in this place [pname]."
                    j "I'll have Chanel take you back to your room."
                    jump epthreedomend

label murderer:

    scene e3murderer1 with longfade
    p "Ok..."
    j "Let me get a nice close look...I'm impressed [pname]. Maybe you can go all the way here."
    p "(This isn't all the way already?)"
    scene e3murderer2 with longdissolve
    j "Poor poor Dumbo. You were a good stud...but it's for you to go."
    db "Mmmmmmmm...kkgdgjkgdkkkkk...ccocicc"
    scene e3murderer3 with mediumdissolve
    j "Look on the bright side...no more shock sessions for you, right?"
    j "Bye bye...now you can join your wife...she was so much louder than you as she died..."
    p "(She's so depraved...)"
    stop seven fadeout 3
    scene e3murderer4 with longfade
    j "Well...he's gone. You've done well for yourself [pname]."
    j "Chanel will take you back now, but I will be in contact again very soon."
    jump epthreedomend

label dmeet:

    scene e3dmeet1 with longfade
    chan "Mistress Dominique, I've arrived as instructed."
    d "Come."
    p "(What is this place?)"
    scene e3dmeet2 with mediumdissolve

    play seven "music/dmeetfour.mp3" fadein 3

    d "Thank you, Chanel. I appreciate you bringing [pname] down here to see me."
    chan "My pleasure, Mistress Dominique."
    scene e3dmeet3 with mediumdissolve
    d "I've been hearing great things about you from Kiyomi. Elena should be very proud of you."
    chan "Thank you, Mistress. I am really enjoying being a part of her team."
    d "I trust [pname] has seen his quarters and is ready for the start of the program?"
    scene e3dmeet4 with mediumdissolve
    if k5:
        chan "Yes, Mistress. [pname] is rooming with Prisoner Kwame."
        d "Yes. Kwame...he was such a good manager at the mines...until he wasn't. Such a shame."
        jump dmeettwo
    else:
        chan "Yes, Mistress. [pname] has been given a proper room befitting his K6 status to start the program."
        d "Very good. I trust you will do an excellent job as his liasion during his stay here."
        chan "Of course, Mistress. I will make sure to do a great job for all of you."
        jump dmeettwo

label dmeettwo:

    scene e3dmeet5 with mediumdissolve
    stop seven fadeout 3
    d "Now, I do want to meet [pname] alone, so please leave us and I will send for you when I have finished with him."
    chan "As you command."
    scene e3dmeet6 with longfade

    play seven "music/dmeetone.mp3" fadein 3

    d "It's a pleasure to meet you [pname]. My name is Dominique Karlsson. I've been expecting you for quite a while now."
    d "Let's have a little discussion together before you start the program tomorrow morning."
    p "Sure thing."
    scene e3dmeet7 with mediumdissolve
    d "So let me show you something our company is working on right now."
    d "This plant and a few others in here are being grown with a special new soil developed by my sister, Veronica."
    scene e3dmeet8 with mediumdissolve
    d "It is hoped that this soil will be quite resistant to the pathogens and environmental hazards due to the Great Collapse."
    d "If all goes well, perhaps it will even be possible over time to grow real crops en masse on the surface again, and feed millions of people more effectively."
    d "We have a larger greenhouse in the facility where we will further test these samples if initial trials prove fruitful."
    p "Wow...I'm speechless. A little shocked too."
    scene e3dmeet9 with mediumdissolve
    d "Why?"
    p "Your company is doing a lot more than I thought...and this facility...this room feels something out of a science fiction novel."
    d "This facility was designed in response to the Great Collapse as a survival bunker, so it is a very large underground area. And quite advanced technologically."
    scene e3dmeet10 with mediumdissolve
    d "But, I actually think you were really shocked that I mentioned feeding millions of people? Isn't that right?"
    p "Yeah...I just assumed The Karlsson Group was...I don't know, like an evil empire of the worst kind."
    scene e3dmeet11 with mediumdissolve
    d "That is true [pname]. This company is doing many things that most would consider quite evil."
    d "But not everyone in this company agrees with the current policies and strategies of The Karlsson Group."
    p "(Hmm...)"
    scene e3dmeet12 with mediumdissolve
    d "Now, let's discuss why you are here right now. The program you are starting tomorrow can be quite taxing, and very dangerous under the wrong circumstances."
    d "But sometimes, prisoners in your position can get a little help with sponsors that give information, advice, and other helpful things."
    d "You are here because I am considering sponsoring you. That would be a significant help to you considering my position and influence."
    p "Why me?"
    scene e3dmeet13 with mediumdissolve
    d "You are with me right now primarily because of your behavior since you were first jailed."
    d "You display some level of a moral compass, and even appear to have the potential to resist the cruel temptations of power."
    d "In laymen's terms, it appears you might be a man full of goodness and morality, a trait sorely lacking at this company."
    scene e3dmeet14 with mediumdissolve
    d "But I am still curious to learn more about you."
    d "If you were in control of The Karlsson Group entirely...and you knew the company could feed millions of people quite easily and even with little cost..."
    d "...what would you do?"
    scene e3dmeet15 with mediumdissolve
    p "(Another choice...or test perhaps.)"
    menu:
        "(I mean...if there is a way to feed that many people, why wouldn't you do it? I'd try and just give it away if possible. It's the right thing to do.) [DominquePath]":
            $ dominique_p += 2
            scene e3dmeet15b with mediumdissolve
            p "I mean...if there is way to do that much good for such a little cost, I think you have to try and make it happen by giving it away if possible."
            d "That's a noble sentiment, but it's usually not so simple to do the right thing...especially here at The Karlsson Group."
            jump dmeetthree
        "(I'd want to try and do the right thing, but I think you would want to control the supply too and have a careful plan...just in case.)":
            $ dominique_scale += 1
            $ dominique_p += 1
            scene e3dmeet15c with mediumdissolve
            p "I think I would want to do the right thing, but I think you would still want to control supply, and not just give it away...just in case."
            d "I generally agree with you. You have to be smart and patient at times to ensure the greatest impact long term."
            jump dmeetthree
        "(If I was in charge, I think it's smart to let the company control this technology and maximize control and profit over just giving it away.)":
            $ dominique_p -= 1
            scene e3dmeet15d with mediumdissolve
            p "I think it's smart to make sure the company controls any important technology, and maximizes control and profit over just giving it away."
            d "I can understand that perspective, and it's probably a safe answer in this environment."
            jump dmeetthree

label dmeetthree:

    scene e3dmeet16 with mediumdissolve
    $ dominiquesponsor = True
    d "To tell you the truth [pname], I am still not quite sure about you in the grand scheme of things."
    d "However, I am a believer in hope, and I do feel a little bit of that for you."
    d "So I think I am going to initially help by sponsoring you in this program."
    p "What does that really mean?"
    scene e3dmeet17 with mediumdissolve
    d "What it actually ends up meaning will depend on you. If you act in ways I find appropriate, I will provide you with information and even practical help."
    p "What kind of practical help, and what is appropriate to you?"
    scene e3dmeet18 with mediumdissolve
    d "Keep your mind and actions in the light...the greater good...and as for the help, you'll just have to wait and see. I offer no promises, only possibilities."
    d "And we will talk soon again. I just wanted to get an initial gut feeling meeting you for the first time."
    p "And what does your gut tell you?"
    scene e3dmeet19 with mediumdissolve
    d "It tells me that you are a risk...but...a risk worth taking right now."
    stop seven fadeout 3
    d "I'll have Chanel take you back to your room. Take care [pname], and be prepared for what comes next..."
    jump epthreedomend

label epthreedomend:

    if k5:
        jump epthreek5end
    else:
        jump epthreek6end

label epthreek5end:

    scene e3k5end1 with longfade
    kw "[pname]! You're back, what happened?"
    if kwamefriendopen:
        if vmeet:
            p "I met with one of the Karlsson sisters, Veronica, and..."
            jump epthreek5endtwo
        elif jmeet:
            p "I met with one of the Karlsson sisters, Juliette, and..."
            jump epthreek5endtwo
        else:
            p "I met with your old boss, Dominique Karlsson, and..."
            jump epthreek5endtwo
    else:
        p "Nothing special, it was just a waste of time.."
        jump epthreek5endtwo

label epthreek5endtwo:

    scene e3k5end2 with quickdissolve
    anne "{i}Attention all Joy Facility participants. Please prepare for Lights Out commencing in thirty seconds.{/i}"
    p " Ordered by a computer intercom...and participants versus prisoners...sure...hmph. I guess we should rest up. We have no clue what is happening tomorrow."
    scene e3k5end3 with mediumdissolve
    kw "Yes, rest would be wise. We should also devise a strategy moving forward of sharing useful information and tips to maximize our chances to do well here."
    p "Definitely agree. Let's figure it out together. Hopefully, it can work out for your family as well."
    kw "Thank you [pname], I really appreciate the sentiment."
    scene e3k5end4 with longdissolve
    p "Well...I guess that's that. Until tomorrow..."
    kw "Until tomorrow..."
    scene black with longdissolve

    play seven "music/k4ending.mp3" fadein 2

    $ renpy.pause (3.0, hard=True)

    scene e3k5end5 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3k5end6 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3k5end7 with longfade

    $ renpy.pause (3.0, hard=True)

    scene black with mediumflash

    stop seven fadeout 2

    pause 2

    jump episodethreeend

label epthreek6end:

    scene e3k6end1 with longfade
    p "(What a start to this place...)"
    play seven "music/k6cell2.mp3" fadein 3
    p "(I really could use some rest.)"
    scene e3k6end2 with longdissolve
    chan "Glad you can relax so easily."
    p "Back so soon after dropping me off? How can you just get in here without me hearing you?"
    chan "Your door is very quiet when opening, and don't forget I've been trained in many skills for years, incuding stealth. You are not hard to sneak up on at all [pname]."
    scene e3k6end3 with mediumdissolve
    p "Fair enough. What do you want?"
    chan "I just wanted to make sure your first day here was ok so far. Tomorrow is when the real fun starts."
    p "It was fine I guess. Just forcing yourself to perform your duties as a liason?"
    scene e3k6end4 with mediumdissolve
    chan "You wound me [pname]! I come here clearly concerned about your well-being and you treat me with such disrespect."
    p "Uh huh...what do you really want from me right now?"
    chan "I want to be able to...relax with you. Let me just get more comfortable..."
    scene e3k6end5 with longdissolve
    p "Wait...what are you...(damn...she's got big...)"
    chan "Relax, I told you we can't quite fuck yet. You need to hold up your end of the bargain first."
    chan "But I want to show you that I am so so so rooting for you to do well. I've seen some of the other men that arrived with you. Total trash...only useful to torment for fun."
    scene e3k6end6 with mediumdissolve
    chan "But you...you get my pussy and tits so excited...I'll be thinking of you as I beat some of the other men in here. So do well...and get some rest. You'll need it."
    stop seven fadeout 3
    chan "Sweet dreams [pname]..."

    scene black with longfade

    play seven "music/k4ending.mp3" fadein 2

    $ renpy.pause (3.0, hard=True)

    scene e3k6end7 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3k6end8 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3k6end9 with longfade

    $ renpy.pause (3.0, hard=True)

    scene e3k6end10 with longfade

    $ renpy.pause (3.0, hard=True)

    scene black with mediumflash

    stop seven fadeout 3

    pause 2

    jump episodethreeend

label episodethreeend:

    if renpy.has_label("episodefourstart"):
        jump episodefourstart
    else:
        play seven "music/zend.mp3" fadein 2

        scene black with longfade
        z "Save by the end of the next screen to preserve a save right at end of Episode 3! Don't do it after the mask!"
        scene zendsavegame with longfade

        $ renpy.pause (10.0, hard=True)

        stop seven fadeout 3

        if renpy.has_label("episodefourstart"):
            jump episodefourstart
        else:
            jump endthree

label endthree:

    scene e3endthree1 with longfade

    play seven "music/happyend3.mp3" fadein 2

    z "Hi there! I hope you enjoyed Episode 3!"
    scene e3endthree2 with mediumdissolve
    z "I want to take the time to thank all of my supporters, but in particular my biggest ones that are true slaves in the best way..."
    z "Their pathetic need to please me makes the game possible for many others to enjoy!"
    scene e3endthree3 with mediumdissolve
    z "So thank you to my biggest supporters like slave piggy failninja, slave thomas, beggar james, and one Mistress, Femme Fatale Di!"
    scene e3endthree4 with mediumdissolve
    z "Please check out my Patreon page if you would like to access bonus images like the one on the screen right now! And, you can also vote on future story content and characters!"
    z "I think I currently have about twenty to thirty bonus pictures so far, and I create more every month!"
    stop seven fadeout 3
    scene e3endthree5 with longfade
    z "Lastly, I want you all to meet the game's biggest supporter...he's a little stuck behind this table here..."

    play seven "music/evilend3.mp3" fadein 2

    z "My very special little slut...slave nathan."
    scene e3endthree6 with mediumdissolve
    z "Every single day, he suffers for me in real life, and I savor ordering his pain and humiliation."
    z "After all, that's his job now. To endure cruelty for my pleasure and amusement."
    scene e3endthree6b with mediumdissolve
    z "And...only he really knows the depths of my true sadistic nature...personally."
    scene e3endthree6c with longdissolve
    z "It really is so so tragic to hear him begging all the time."
    z "Especially listening to his sad little voice while fucking a real man...oh...so good..."
    stop seven fadeout 3
    scene e3endthree7 with longfade
    z "For almost everyone else though...this is just a fun game to enjoy, and thank you for playing it!"
    z "Bye bye! Hope to see you for Episode 4!"














return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
