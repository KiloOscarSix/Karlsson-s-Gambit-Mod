init python:
    galleryItems = []

    class GalleryItem:
        def __init__(self, char="", pageNum=1, label="", thumbnail="", scope=None):
            self.char = char
            self.pageNum = pageNum
            self.label = label
            if scope is None:
                scope = {}
            self.scope = scope
            self.thumbnail = "/images/{}".format(thumbnail)
            galleryItems.append(self)

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

define galleryMenu = [
["Samantha", "/images/samp4.jpg"],
["Katsumi", "/images/e3cell6.jpg"],
["Juliette", "/images/ship3.jpg"],
["Patrcia", "/images/prop5.jpg"],
["Junko", "/images/e3pet8.jpg"],
# ["Elena", "/images/tcc1.jpg"],
["Sister", "/images/e2sisjoboffer6.jpg"],
["Veronica", "/images/e3clinicathree1.jpg"],
["Other", "/images/e3broom2.jpg"],
]

define samamtha1 = GalleryItem("Samantha", 1, "sampunishthree", "samp10.jpg") # Samantha
define samamtha1 = GalleryItem("Samantha", 1, "solitarytwo", "solitary7b.jpg") # Samantha
define samamtha1 = GalleryItem("Samantha", 1, "kanedomend2", "e2kanedomend8.jpg") # Samantha
define samamtha1 = GalleryItem("Samantha", 1, "kanesubend", "e2kanesubend5.jpg") # Samantha

define juliette1 = GalleryItem("Juliette", 1, "sister1", "ship20.jpg") # Juliette
define juliette2 = GalleryItem("Juliette", 1, "julietteone", "e2juliette1.jpg") # Juliette
define julietteSister1 = GalleryItem("Juliette", 1, "stagebtwo", "e3stageb21.jpg") # Juliette + Sister 8367

define patrcia1 = GalleryItem("Patrcia", 1, "patpunish", "pat2b.jpg") # Patrcia
define patrcia2 = GalleryItem("Patrcia", 1, "pattermstwo", "e2patworship5d.jpg") # Patrcia
define patrcia3 = GalleryItem("Patrcia", 1, "patsexfour", "e2patsex17.jpg") # Patrcia

define elena2 = GalleryItem("Katsumi", 1, "elenavisit3b", "limo14.jpg") # Katsumi
define katsumi3 = GalleryItem("Katsumi", 1, "pissboy", "e3pissed6.jpg") # Katsumi 6282
define katsumi1 = GalleryItem("Katsumi", 1, "kittyass", "e3ass7.jpg") # Katsumi 6517
define katsumi2 = GalleryItem("Katsumi", 1, "celltwofour", "e3cell18dd.jpg") # Katsumi 7745

define unknown6 = GalleryItem("Junko", 1, "junko2", "e3junko23.jpg") # Junko 6960
define unknown8 = GalleryItem("Junko", 1, "pet", "e3pet10c.jpg") # Junko 9640
define unknown3 = GalleryItem("Junko", 1, "cagemantwo", "e3cagemantwo2.jpg") # Junko 9770

define sister1 = GalleryItem("Sister", 1, "oliviaevil", "e2oliviaevil3.jpg") # Sister
define julietteSister1 = GalleryItem("Sister", 1, "stagebtwo", "e3stageb21.jpg") # Juliette + Sister 8367

define alessandraVeronica1 = GalleryItem("Veronica", 1, "vbroom", "e3broom1.jpg") # Alessandra + Veronica
define veronicaReyes1 = GalleryItem("Veronica", 1, "clinicafive", "e3clinicafive2.jpg") # Veronica + Nurse Reyes 8890

define elena1 = GalleryItem("Other", 1, "lick", "lick2.jpg") # Elena
define cassandra1 = GalleryItem("Other", 1, "sisnewhire", "e2sisnewhire2.jpg") # Cassandra
define scarlett1 = GalleryItem("Other", 1, "pegging", "e3peggingtwo4.jpg") # Scarlett 9884


default galleryPageNumber = 1
default scopeDict = {}

label galleryNameChange:
    default persistent.pname = ""
    default persistent.pname_f = ""
    default persistent.pname2 = ""
    default persistent.pname_f2 = ""
    default persistent.pname3 = ""
    default persistent.pname4 = ""
    if persistent.pname == "":
        $ persistent.pname = renpy.input("My first name is...", default="Kane")
    if persistent.pname_f == "":
        $ persistent.pname_f = renpy.input("My last name is...", default="Jacobs")
    if persistent.pname2 == "":
        $ persistent.pname2 = renpy.input("My best friend's first name is...", default="Jake")
    if persistent.pname_f2 == "":
        $ persistent.pname_f2 = renpy.input("My best friend's last name is...", default="Robertson")
    if persistent.pname3 == "":
        $ persistent.pname3 = renpy.input("My sister's first name is...", default="Olivia")
    if persistent.pname4 == "":
        $ persistent.pname4 = renpy.input("My brother's first name is...", default="Seth")

    $ scopeDict = {"pname":persistent.pname, "pname_f":persistent.pname_f, "pname2":persistent.pname2, "pname_f2":persistent.pname_f2, "pname3":persistent.pname3, "pname4":persistent.pname4}
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

        for i in galleryMenu:
            vbox:
                imagebutton:
                    action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "modTextBody"
                    xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="Juliette"):
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

            if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
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

        for galleryItem in galleryItems:
            if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                imagebutton:
                    action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                    idle Transform(galleryItem.thumbnail, zoom=0.2)
                    hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
