define gr = "{color=#006400}"
define red = "{color=#f00}"

define DomPath = "{color=#006400}[Dom Path]"
define GoodPath = "{color=#006400}[Good Path]"
define SubPath = "{color=#006400}[Sub Path]"
define EvilPath = "{color=#006400}[Evil Path]"
define ElenaPath = "{color=#006400}[Elena Path]"
define Shock = "{color=#006400}[Shock +1]"
define PatriciaPath = "{color=#006400}[Patricia Path]"
define FriendPath = "{color=#006400}[Friend Path]"
define SamanthaPath = "{color=#006400}[Samantha Path]"
define SisDomPath = "{color=#006400}[Sis Dom Path]"
define SisSubPath = "{color=#006400}[Sis Sub Path]"
define SisPath = "{color=#006400}[Sis Path]"
define SisGoodPath = "{color=#006400}[Sis Good Path]"
define SisEvilPath = "{color=#006400}[Sis Evil Path]"
define SisBroPath = "{color=#006400}[Sis Bro Path]"
define SlavePath = "{color=#006400}[Slave Path]"
define VeronicaPath = "{color=#006400}[Veronica Path]"
define _SlavePath = "{color=#f00}[Slave Path]"
define DominquePath = "{color=#006400}[Dominque Path]"
define AlessandraPath = "{color=#006400}[Alessandra Path]"
define JuliettePath = "{color=#006400}[Juliette Path]"
define GambitPath = "{color=#006400}[Gambit Path]"
define SisCassPath = "{color=#006400}[Sis+Cassandra Path]"
define BroKiyomiPath = "{color=#006400}[Bro+Kiyomi Path]"
define KittyPath = "{color=#006400}[Kitty Path]"
define JunkoPath = "{color=#006400}[Junko Path]"
define ScarlettPath = "{color=#006400}[Scarlett Path]"
define SisVeronicaPath = "{color=#006400}[Sis+Veronica Path]"
define SisJuliettePath = "{color=#006400}[Sis+Juliette Path]"
define SisDominquePath = "{color=#006400}[Sis+Dominque Path]"
define SisAlessandraPath = "{color=#006400}[Sis+Alessandra Path]"
define ChanelPath = "{color=#006400}[Chanel Path]"
define KiyomiPath = "{color=#006400}[Kiyomi Path]"

define mod = Character("OscarSix", color="#0f0")

screen modOptions():
    modal True

    add "#23272a"

    vbox:
        xcenter 0.5
        ypos 33
        spacing 33

        text "Mod Options" style "modTextHeader"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("changeIngameNames") text_style "modTextButtonHeader"

        textbutton "Change Gallery Names" action ui.callsinnewcontext("changeGalleryNames") text_style "modTextButtonHeader"

    textbutton _("Return") action Hide("modOptions"):
        text_style "modTextButtonHeader"
        yanchor 1.0
        align (0.1, 0.9)

label changeGalleryNames:
    python:
        persistent.pname = renpy.input("My first name is...", default="Kane")
        persistent.pname_f = renpy.input("My last name is...", default="Jacobs")
        persistent.pname2 = renpy.input("My best friend's first name is...", default="Jake")
        persistent.pname_f2 = renpy.input("My best friend's last name is...", default="Robertson")
        persistent.pname3 = renpy.input("My sister's first name is...", default="Olivia")
        persistent.pname3 = renpy.input("My brother's first name is...", default="Seth")
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        pname = renpy.input("My first name is...", default="Kane")
        pname_f = renpy.input("My last name is...", default="Jacobs")
        pname2 = renpy.input("My best friend's first name is...", default="Jake")
        pname_f2 = renpy.input("My best friend's last name is...", default="Robertson")
        pname3 = renpy.input("My sister's first name is...", default="Olivia")
        pname3 = renpy.input("My brother's first name is...", default="Seth")
    mod "Names successful changed"
    return
