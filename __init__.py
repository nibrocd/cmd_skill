import subprocess
from mycroft.util.log import LOG
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler

class CmdSkill(MycroftSkill):
    def __init__(self):
        super(CmdSkill, self).__init__('CmdSkill')
 

    @intent_handler(IntentBuilder("").require("Play").require("Cd").require("Playlist").optionally("Spotify"))
    def handle_playlist_cdd_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/cdd.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Play").require("Softies").optionally("Playlist").optionally("Spotify"))
    def handle_playlist_softies_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/softies.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Play").require("Vibes").optionally("Playlist").optionally("Spotify"))
    def handle_playlist_vibes_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/vibes.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Play").require("Ajr").optionally("Playlist").optionally("Spotify"))
    def handle_playlist_ajr_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/ajr.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Play").require("Indies").optionally("Playlist").optionally("Spotify"))
    def handle_playlist_indies_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/mixed_vibes.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Play").require("Mixed").require("Vibes").optionally("Playlist").optionally("Spotify"))
    def handle_playlist_mixedVibes_intent(self, message):
            self.speak_dialog("confirm")
            subprocess.call('/home/pi/scripts/mixed_vibes.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Stop").require("Music").optionally("Spotify"))
    def handle_stop_music_intent(self, message):
            self.speak_dialog("off")
            subprocess.call('/home/pi/scripts/stop-mpc.sh', shell=True)

    @intent_handler(IntentBuilder("").require("Skip").require("Song").require("Spotify"))
    def handle_skip_song_intent(self, message):
            self.speak_dialog("next")
            subprocess.call("mpc next", shell=True)

    @intent_handler(IntentBuilder("").require("Turn").require("Volume").require("Up").require("Spotify"))
    def handle_volume_up_intent(self, message):
            self.speak_dialog("up")
            subprocess.call('mpc volume +15', shell=True)


    @intent_handler(IntentBuilder("").require("Turn").require("Volume").require("Down").require("Spotify"))
    def handle_volume_down_intent(self, message):
            self.speak_dialog("down")
            subprocess.call('mpc volume -15', shell=True)


def create_skill():
    return CmdSkill()
