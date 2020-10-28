define gr = "{color=#0f0}"
define red = "{color=#f00}"

define DomPath = "{color=#0f0}[Dom Path]"
define GoodPath = "{color=#0f0}[Good Path]"
define SubPath = "{color=#0f0}[Sub Path]"
define EvilPath = "{color=#0f0}[Evil Path]"
define ElenaPath = "{color=#0f0}[Elena Path]"
define Shock = "{color=#0f0}[Shock +1]"
define PatriciaPath = "{color=#0f0}[Patricia Path]"
define FriendPath = "{color=#0f0}[Friend Path]"
define SamanthaPath = "{color=#0f0}[Samamtha Path]"
define SisDomPath = "{color=#0f0}[Sis Dom Path]"
define SisSubPath = "{color=#0f0}[Sis Sub Path]"
define SisPath = "{color=#0f0}[Sis Path]"
define SisGoodPath = "{color=#0f0}[Sis Good Path]"
define SisEvilPath = "{color=#0f0}[Sis Evil Path]"
define SisBroPath = "{color=#0f0}[Sis Bro Path]"
define SlavePath = "{color=#0f0}[Slave Path]"
define VeronicaPath = "{color=#0f0}[Veronica Path]"
define _SlavePath = "{color=#f00}[Slave Path]"
define DominquePath = "{color=#0f0}[Dominque Path]"
define AlessandraPath = "{color=#0f0}[Alessandra Path]"
define JuliettePath = "{color=#0f0}[Juliette Path]"
define GambitPath = "{color=#0f0}[Gambit Path]"
define SisCassPath = "{color=#0f0}[Sis+Cassandra Path]"
define BroKiyomiPath = "{color=#0f0}[Bro+Kiyomi Path]"
define KittyPath = "{color=#0f0}[Kitty Path]"
define JunkoPath = "{color=#0f0}[Junko Path]"
define ScarlettPath = "{color=#0f0}[Scarlett Path]"
define SisVeronicaPath = "{color=#0f0}[Sis+Veronica Path]"
define SisJuliettePath = "{color=#0f0}[Sis+Juliette Path]"
define ChanelPath = "{color=#0f0}[Chanel Path]"
define KiyomiPath = "{color=#0f0}[Kiyomi Path]"

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
        persistent.y = renpy.input("Answer with your name.", default="Kyle")
    mod "Gallery names successful changed"
    return

label changeIngameNames:
    mod "Make sure to do this in the save you wish to change names for."
    python:
        y = renpy.input("Answer with your name.", default="Kyle")
    mod "Names successful changed"
    return
