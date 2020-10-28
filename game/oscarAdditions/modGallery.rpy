init python:
    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

default galleryPageNumber = 1

define sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Juliette", "/images/ship3.jpg"],
    ["Elena", "/images/tcc1.jpg"],
    ["Sister", "/images/e2sisjoboffer6.jpg"],
    ["Cassandra", "/images/e2sisnewhire24.jpg"],
    ["Samantha", "/images/samp4.jpg"],
    ["Patrcia", "/images/prop5.jpg"],
    ],
    "Juliette": {
    1: [
    ["sisters1", {}, "/images/ship20.jpg"],
    ["julietteone", {}, "/images/e2juliette1.jpg"],
    ],
    },
    "Elena": {
    1: [
    ["lick", "/images/lick2.jpg"],
    ["elenavisit3b", "/images/limo14.jpg"],
    ]
    },
    "Sister": {
    1: [
    ["oliviaevil", "/images/e2oliviaevil3.jpg"],
    ],
    },
    "Cassandra": {
    1: [
    ["sisnewhire", "/images/e2sisnewhire2.jpg"],
    ]
    },
    "Samantha": {
    1: [
    ["sampunishthree", "/images/samp10.jpg"],
    ["solitarytwo", "/images/solitary7b.jpg"],
    ["kanedomend2", "/images/e2kanedomend8.jpg"],
    ["kanesubend", "/images/e2kanesubend5.jpg"],
    ]
    },
    "Patrcia": {
    1: [
    ["patpunish", "/images/pat2b.jpg"],
    ["pattermstwo", "/images/e2patworship5d.jpg"],
    ["patsexfour", "/images/e2patsex17.jpg"],
    ]
    },
    }

label galleryNameChange:
    default persistent.pname = ""
    default persistent.pname_f = ""
    default persistent.pname2 = ""
    default persistent.pname_f2 = ""
    default persistent.pname3 = ""
    default persistent.pname4 = ""
    if persistent.pname = "":
        $ persistent.pname = renpy.input("My first name is...", default="Kane")
    if persistent.pname_f = "":
        $ persistent.pname_f = renpy.input("My last name is...", default="Jacobs")
    if persistent.pname2 = "":
        $ persistent.pname2 = renpy.input("My best friend's first name is...", default="Jake")
    if persistent.pname_f2 = "":
        $ persistent.pname_f2 = renpy.input("My best friend's last name is...", default="Robertson")
    if persistent.pname3 = "":
        $ persistent.pname3 = renpy.input("My sister's first name is...", default="Olivia")
    if persistent.pname4 = "":
        $ persistent.pname3 = renpy.input("My brother's first name is...", default="Seth")
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="All"):
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "modTextHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "modTextBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "modTextBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"pname":persistent.pname, "pname_f":persistent.pname_f, "pname2":persistent.pname2, "pname_f2":persistent.pname_f2, "pname3":persistent.pname3, "pname4":persistent.pname4}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)
