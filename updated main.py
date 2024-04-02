import pygame
import button
import songlist
from songlist import playlist, current_selection
from pygame import mixer

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption('Audio Unearth')
pygame.mixer.init()

#load button images
discover_img = pygame.image.load('assets/discover_btn.png').convert_alpha()
playlist_img = pygame.image.load('assets/playlist_btn.png').convert_alpha()
quit_img = pygame.image.load('assets/quit_btn.png').convert_alpha()
no_img = pygame.image.load('assets/no_btn.png').convert_alpha()
yes_img = pygame.image.load('assets/yes_btn.png').convert_alpha()
discplaylist_img = pygame.image.load('assets/playlist_btnn.png').convert_alpha()
discback_img = pygame.image.load('assets/back_btnn.png').convert_alpha()
next_img = pygame.image.load('assets/next_btn.png').convert_alpha()
previous_img = pygame.image.load('assets/previous_btn.png').convert_alpha()
menu_img = pygame.image.load('assets/menu_btn.png').convert_alpha()
play_img = pygame.image.load('assets/play_btn.png').convert_alpha()
pause_img = pygame.image.load('assets/pause_btn.png').convert_alpha()

#add images
bg=pygame.image.load('assets/bg.png')
title=pygame.image.load('assets/title.png')

#add banners
Foot_img=pygame.image.load('banners/6Foot_img.png')
Something_img=pygame.image.load('banners/Something_img.png')
Lonely_img=pygame.image.load('banners/911Lonely_img.png')
AllIAsk_img=pygame.image.load('banners/AllIAsk_img.png')
Alright_img=pygame.image.load('banners/Alright_img.png')
Always_img=pygame.image.load('banners/Always_img.png')
ApplyingPressure_img=pygame.image.load('banners/applyingpressure_img.png')
Awkward_img=pygame.image.load('banners/Awkward_img.png')
BeatingDown_img=pygame.image.load('banners/BeatingDown_img.png')
BeatIt_img=pygame.image.load('banners/BeatIt_img.png')
BeforeHeCheats_img=pygame.image.load('banners/BeforeHeCheats_img.png')
BigPoppa_img=pygame.image.load('banners/BigPoppa_img.png')
BluntBlowin_img=pygame.image.load('banners/BluntBlowin_img.png')
Chicago_img=pygame.image.load('banners/Chicago_img.png')
CouldveBeen_img=pygame.image.load('banners/CouldveBeen_img.png')
DeadtoMe_img=pygame.image.load('banners/DeadtoMe_img.png')
Despues_img=pygame.image.load('banners/Despues_img.png')
FamilyTies_img=pygame.image.load('banners/familyties_img.png')
Fancy_img=pygame.image.load('banners/Fancy_img.png')
Faneto_img=pygame.image.load('banners/Faneto_img.png')
FirstPersonShooter_img=pygame.image.load('banners/FirstPersonShooter_img.png')
Gangsta_img=pygame.image.load('banners/Gangsta_img.png')
Garden_img=pygame.image.load('banners/Garden_img.png')
GetAlongBetter_img=pygame.image.load('banners/GetAlongBetter_img.png')
Gravity_img=pygame.image.load('banners/Gravity_img.png')
HellNBack_img=pygame.image.load('banners/HellNBack_img.png')
Her_img=pygame.image.load('banners/Her_img.png')
HowMuch_img=pygame.image.load('banners/HowMuch_img.png')
IfIAintGotYou_img=pygame.image.load('banners/IfIAintGotYou_img.png')
IfIWereABoy_img=pygame.image.load('banners/IfIWereABoy_img.png')
Insane_img=pygame.image.load('banners/Insane_img.png')
IThink_img=pygame.image.load('banners/ITHINK_img.png')
JealousyJealousy_img=pygame.image.load('banners/Jealousy, Jealousy_img.png')
JimmyCooks_img=pygame.image.load('banners/JimmyCooks_img.png')
KevinsHeart_img=pygame.image.load('banners/KevinsHeart_img.png')
LemmeSee_img=pygame.image.load('banners/LemmeSee_img.png')
Les_img=pygame.image.load('banners/Les_img.png')
LongWay2Go_img=pygame.image.load('banners/LongWay2Go_img.png')
LoversRock_img=pygame.image.load('banners/LoversRock_img.png')
Low_img=pygame.image.load('banners/Low_img.png')
Loyalty_img=pygame.image.load('banners/LOYALTY_img.png')
MeandYourMama_img=pygame.image.load('banners/MeandYourMama_img.png')
MyLife_img=pygame.image.load('banners/mylife_img.png')
MyLove_img=pygame.image.load('banners/MyLove_img.png')
NeverLoseMe_img=pygame.image.load('banners/NeverLoseMe_img.png')
NoLimit_img=pygame.image.load('banners/NoLimit_img.png')
NoLove_img=pygame.image.load('banners/NoLove_img.png')
NoOneKnows_img=pygame.image.load('banners/NoOneKnows_img.png')
OpenArms_img=pygame.image.load('banners/OpenArms_img.png')
PinkMatter_img=pygame.image.load('banners/PinkMatter_img.png')
PlayingGames_img=pygame.image.load('banners/PlayingGames_img.png')
Poison_img=pygame.image.load('banners/Poison_img.png')
Pyramids_img=pygame.image.load('banners/Pyramids_img.png')
Remember_img=pygame.image.load('banners/Remember_img.png')
Reminder_img=pygame.image.load('banners/Reminder_img.png')
RightThere_img=pygame.image.load('banners/RightThere_img.png')
Running_img=pygame.image.load('banners/RUNNING_img.png')
She_img=pygame.image.load('banners/She_img.png')
SmokingOut_img=pygame.image.load('banners/SmokingOut_img.png')
SomeoneLikeYou_img=pygame.image.load('banners/SomeoneLikeYou_img.png')
Strange_img=pygame.image.load('banners/Strange_img.png')
Summer_img=pygame.image.load('banners/SUMMER_img.png')
SuperRichKids_img=pygame.image.load('banners/SuperRichKids_img.png')
Sweet_img=pygame.image.load('banners/SWEET_img.png')
Telekinesis_img=pygame.image.load('banners/TELEKINESIS_img.png')
Television_img=pygame.image.load('banners/Television_img.png')
TheArtofPeer_img=pygame.image.load('banners/TheArtofPeer_img.png')
TitoMe_img=pygame.image.load('banners/TitoMe_img.png')
United_img=pygame.image.load('banners/United_img.png')
Used_img=pygame.image.load('banners/Used_img.png')
VSOP_img=pygame.image.load('banners/VSOP_img.png')
Wesleys_img=pygame.image.load('banners/Wesleys_img.png')
YouBroke_img=pygame.image.load('banners/YouBroke_img.png')

#scale images
title= pygame.transform.scale(title, (500, 500))

#create button instances
discover_button = button.Button(135, 185, discover_img, 0.95)
playlist_button = button.Button(153, 285, playlist_img, 0.95)
quit_button = button.Button(225, 375, quit_img, 0.9)
yes_button = button.Button(475, 200, yes_img, 0.2)
no_button = button.Button(10, 200, no_img, 0.2)
discplaylist_button = button.Button(175, 330, discplaylist_img, 0.23)
discback_button = button.Button(15, 10, discback_img, 0.05)
next_button = button.Button(400, 415, next_img, 0.135)
previous_button = button.Button(100, 415, previous_img, 0.135)
menu_button = button.Button(15, 10, menu_img, 0.2)
play_button = button.Button(400, 300, play_img, 0.2)
pause_button = button.Button(250, 415, pause_img, 0.135)


#other declarations
discover_executed = False
run = True
menu_state = "main"
playlist_printed = False
current_song_index = 0
firstsong_played = False
paused = False


def play(filename):
  pygame.mixer.music.load(filename)
  pygame.mixer.music.play(loops= -1, fade_ms=20000)

def main_menu():
    global menu_state, discover_executed
    screen.blit(bg, (0,0))
    screen.blit(title, (45,-155))
    pygame.mixer.music.unload()

    if discover_button.draw(screen) and menu_state == "main":
        menu_state = "discover"
          
    if playlist_button.draw(screen) and menu_state == "main":
        menu_state = "playlist"
          
    if quit_button.draw(screen) and menu_state == "main":
        menu_state = "quit"
          
    pygame.display.update()
    discover_executed = False

def discover_menu():
    global discover_executed, menu_state
    if menu_state == "discover":
      if yes_button.draw(screen) and menu_state == "discover":
          add_to_playlist()
          discover_executed = False
      if no_button.draw(screen) and menu_state == "discover":
        discover_executed = False
      if discplaylist_button.draw(screen) and menu_state == "discover":
        menu_state = "playlist"
      if discback_button.draw(screen) and menu_state == "discover":
        menu_state = "main"
 
  
    if not discover_executed:
        pygame.mixer.music.unload()
        discover()
        discover_executed = True  
    pygame.display.update()

def playlist_menu():
      global menu_state, playlist_printed, firstsong_played, paused
      if menu_state == "playlist":
        if previous_button.draw(screen) and menu_state == "playlist":
          print_previous_song()
        if next_button.draw(screen) and menu_state == "playlist":
          print_next_song()
        if pause_button.draw(screen) and menu_state == "playlist":
          if paused == False:
            pygame.mixer.music.pause()
            paused = True
          elif paused == True:
            pygame.mixer.music.unpause()
            paused = False

        if not playlist_printed:
            print("Current Playlist:", playlist)  # Print the playlist for debugging
            playlist_printed = True
        if not firstsong_played:
          print("Playing first song from the playlist:", playlist[0])
          playlist_check()
          firstsong_played = True

        if discback_button.draw(screen) and menu_state == "playlist":
          menu_state = "main"
          firstsong_played = False
          playlist_printed = False




      pygame.display.update()

def add_to_playlist():
    if current_selection:
        playlist.extend(current_selection)

def print_next_song():
    global current_song_index, next_song
    if current_song_index < len(playlist) - 1:
        next_song = playlist[current_song_index + 1]
        current_song_index += 1
        playlist_check()
        print("Next song:", next_song)
    else:
        current_song_index = 0
        next_song = playlist[0]
        playlist_check()
        print("Next song:", next_song)

def print_previous_song():
    global current_song_index, previous_song
    if current_song_index > 0:
        previous_song = playlist[current_song_index - 1]
        current_song_index -= 1
        playlist_check()
        print("Previous song:", previous_song)
    else:
        current_song_index = len(playlist) - 1  # Go to the end of the playlist
        previous_song = playlist[-1]
        playlist_check()
        print("Previous song:", previous_song)

def playlist_check():
  global current_song_index
  if current_song_index < len(playlist):
    song = playlist[current_song_index]
    pygame.display.update()
    if song == '6 FOOT 7 FOOT':
      screen.blit(Foot_img, (0,0))
      play("music/6 FOOT 7 FOOT.mp3")
    elif song == '20 SOMETHING':
      screen.blit(Something_img,(0,0))
      play("music/20 SOMETHING.mp3")
    elif song == 'APPLYING PRESSURE':
      screen.blit(ApplyingPressure_img,(0,0))
      play("music/APPLYING PRESSURE.mp3")
    elif song == 'ALL I ASK':
      screen.blit(AllIAsk_img,(0,0))
      play("music/ALL I ASK.mp3")
    elif song == 'ALRIGHT':
      screen.blit(Alright_img,(0,0))
      play("music/ALRIGHT.mp3")
    elif song == 'ALWAYS':
      screen.blit(Always_img,(0,0))
      play("music/ALWAYS.mp3")
    elif song == 'AWKWARD':
      screen.blit(Awkward_img,(0,0))
      play("music/AWKWARD.mp3")
    elif song == 'BEAT IT':
      screen.blit(BeatIt_img,(0,0))
      play("music/BEAT IT.mp3")
    elif song == 'BEATING DOWN YO BLOCK':
      screen.blit(BeatingDown_img,(0,0))
      play("music/BEATING DOWN YO BLOCK.mp3")
    elif song == 'BEFORE HE CHEATS':
      screen.blit(BeforeHeCheats_img,(0,0))
      play("music/BEFORE HE CHEATS.mp3")
    elif song == 'BIG POPPA':
      screen.blit(BigPoppa_img,(0,0))
      play("music/BIG POPPA.mp3")
    elif song == 'BLUNT BLOWIN':
      screen.blit(BluntBlowin_img,(0,0))
      play("music/BLUNT BLOWIN.mp3")
    elif song == 'CHICAGO':
      screen.blit(Chicago_img,(0,0))
      play("music/CHICAGO.mp3")
    elif song == 'COULDVE BEEN':
      screen.blit(CouldveBeen_img,(0,0))
      play("music/COULDVE BEEN.mp3")
    elif song == 'DEAD TO ME':
      screen.blit(DeadtoMe_img, (0,0))
      play("music/DEAD TO ME.mp3")
    elif song == 'DESPUES DE LA PLAYA':
      screen.blit(Despues_img,(0,0))
      play("music/DESPUES DE LA PLAYA.mp3")
    elif song == 'FAMILY TIES':
      screen.blit(FamilyTies_img,(0,0))
      play("music/FAMILY TIES.mp3")
    elif song == 'FANCY':
      screen.blit(Fancy_img,(0,0))
      play("music/FANCY.mp3")
    elif song == 'FANETO':
      screen.blit(Faneto_img,(0,0))
      play("music/FANETO.mp3")
    elif song == 'FIRST PERSON SHOOTER':
      screen.blit(FirstPersonShooter_img,(0,0))
      play("music/FIRST PERSON SHOOTER.mp3")
    elif song == 'GANGSTA':
      screen.blit(Gangsta_img,(0,0))
      play("music/GANGSTA.mp3")
    elif song == 'GARDEN':
      screen.blit(Garden_img,(0,0))
      play("music/GARDEN.mp3")
    elif song == 'GET ALONG BETTER':
      screen.blit(GetAlongBetter_img,(0,0))
      play("music/GET ALONG BETTER.mp3")
    elif song == 'GRAVITY':
      screen.blit(Gravity_img,(0,0))
      play("music/GRAVITY.mp3")
    elif song == 'HELL N BACK':
      screen.blit(HellNBack_img,(0,0))
      play("music/HELL N BACK.mp3")
    elif song == 'HER':
      screen.blit(Her_img,(0,0))
      play("music/HER.mp3")
    elif song == 'HOW MUCH A DOLLAR COST':
      screen.blit(HowMuch_img,(0,0))
      play("music/HOW MUCH A DOLLAR COST.mp3")
    elif song == 'I THINK':
      screen.blit(IThink_img,(0,0))
      play("music/I THINK.mp3")
    elif song == 'I THOUGHT YOU WANTED TO DANCE':
      screen.blit(Sweet_img,(0,0))
      play("music/I THOUGHT YOU WANTED TO DANCE.mp3")
    elif song == 'IF I AINT GOT YOU':
      screen.blit(IfIAintGotYou_img,(0,0))
      play("music/IF I AINT GOT YOU.mp3")
    elif song == 'IF I WERE A BOY':
      screen.blit(IfIWereABoy_img,(0,0))
      play("music/IF I WERE A BOY.mp3")
    elif song == 'INSANE IN THE BRAIN':
      screen.blit(Insane_img,(0,0))
      play("music/INSANE IN THE BRAIN.mp3")
    elif song == 'JEALOUSY, JEALOUSY':
      screen.blit(JealousyJealousy_img, (0,0))
      play("music/JEALOUSY, JEALOUSY.mp3")
    elif song == 'JIMMY COOKS':
      screen.blit(JimmyCooks_img,(0,0))
      play("music/JIMMY COOKS.mp3")
    elif song == 'KEVINS HEART':
      screen.blit(KevinsHeart_img,(0,0))
      play("music/KEVINS HEART.mp3")
    elif song == 'LEMME SEE':
      screen.blit(LemmeSee_img,(0,0))
      play("music/LEMME SEE.mp3")
    elif song == 'LES':
      screen.blit(Les_img,(0,0))
      play("music/LES.mp3")
    elif song == 'LONG WAY 2 GO':
      screen.blit(LongWay2Go_img,(0,0))
      play("music/LONG WAY 2 GO.mp3")
    elif song == 'LOVERS ROCK':
      screen.blit(LoversRock_img,(0,0))
      play("music/LOVERS ROCK.mp3")
    elif song == 'LOW':
      screen.blit(Low_img,(0,0))
      play("music/LOW.mp3")
    elif song == 'LOYALTY':
      screen.blit(Loyalty_img,(0,0))
      play("music/LOYALTY.mp3")
    elif song == 'MY LIFE':
      screen.blit(MyLife_img,(0,0))
      play("music/MY LIFE.mp3")
    elif song == 'ME AND YOUR MAMA':
      screen.blit(MeandYourMama_img,(0,0))
      play("music/ME AND YOUR MAMA.mp3")
    elif song == '911':
      screen.blit(Lonely_img,(0,0))
      play("music/911.mp3")
    elif song == 'MY LOVE MINE ALL MINE':
      screen.blit(MyLove_img,(0,0))
      play("music/MY LOVE MINE ALL MINE.mp3")
    elif song == 'NEVER LOSE ME':
      screen.blit(NeverLoseMe_img,(0,0))
      play("music/NEVER LOSE ME.mp3")
    elif song == 'NO LIMIT':
      screen.blit(NoLimit_img,(0,0))
      play("music/NO LIMIT.mp3")
    elif song == 'NO LOVE':
      screen.blit(NoLove_img,(0,0))
      play("music/NO LOVE.mp3")
    elif song == 'NO ONE KNOWS':
      screen.blit(NoOneKnows_img,(0,0))
      play("music/NO ONE KNOWS.mp3")
    elif song == 'OPEN ARMS':
      screen.blit(OpenArms_img,(0,0))
      play("music/OPEN ARMS.mp3")
    elif song == 'PINK MATTER':
      screen.blit(PinkMatter_img,(0,0))
      play("music/PINK MATTER.mp3")
    elif song == 'PLAYING GAMES':
      screen.blit(PlayingGames_img,(0,0))
      play("music/PLAYING GAMES.mp3")
    elif song == 'POISON':
      screen.blit(Poison_img,(0,0))
      play("music/POISON.mp3")
    elif song == 'PYRAMIDS':
      screen.blit(Pyramids_img,(0,0))
      play("music/PYRAMIDS.mp3")
    elif song == 'REMEMBER THE TIME':
      screen.blit(Remember_img,(0,0))
      play("music/REMEMBER THE TIME.mp3")
    elif song == 'REMINDER':
      screen.blit(Reminder_img,(0,0))
      play("music/REMINDER.mp3")
    elif song == 'RIGHT THERE':
      screen.blit(RightThere_img,(0,0))
      play("music/RIGHT THERE.mp3")
    elif song == 'RUNNING OUT OF TIME':
      screen.blit(Running_img,(0,0))
      play("music/RUNNING OUT OF TIME.mp3")
    elif song == 'SHE':
      screen.blit(She_img,(0,0))
      play("music/SHE.mp3")
    elif song == 'SMOKING OUT THE WINDOW':
      screen.blit(SmokingOut_img,(0,0))
      play("music/SMOKING OUT THE WINDOW.mp3")
    elif song == 'TELEVISION':
      screen.blit(Television_img,(0,0))
      play("music/TELEVISION.mp3")
    elif song == 'SOMEONE LIKE YOU':
      screen.blit(SomeoneLikeYou_img,(0,0))
      play("music/SOMEONE LIKE YOU.mp3")
    elif song == 'STRANGE':
      screen.blit(Strange_img,(0,0))
      play("music/STRANGE.mp3")
    elif song == 'SUMMER':
      screen.blit(Summer_img,(0,0))
      play("music/SUMMER.mp3")
    elif song == 'SUPER RICH KIDS':
      screen.blit(SuperRichKids_img,(0,0))
      play("music/SUPER RICH KIDS.mp3")
    elif song == 'TELEKINESIS':
      screen.blit(Telekinesis_img,(0,0))
      play("music/TELEKINESIS.mp3")
    elif song == 'THE ART OF PEER PRESSURE':
      screen.blit(TheArtofPeer_img,(0,0))
      play("music/THE ART OF PEER PRESSURE.mp3")
    elif song == 'TITI ME PREGUNTO':
      screen.blit(TitoMe_img,(0,0))
      play("music/TITI ME PREGUNTO.mp3")
    elif song == 'UNITED IN GRIEF':
      screen.blit(United_img,(0,0))
      play("music/UNITED IN GRIEF.mp3")
    elif song == 'USED':
      screen.blit(Used_img,(0,0))
      play("music/USED.mp3")
    elif song == 'VSOP':
      screen.blit(VSOP_img,(0,0))
      play("music/VSOP.mp3")
    elif song == 'WESLEYS THEORY':
      screen.blit(Wesleys_img,(0,0))
      play("music/WESLEYS THEORY.mp3")
    elif song == 'YOU BROKE MY HEART':
      screen.blit(YouBroke_img,(0,0))
      play("music/YOU BROKE MY HEART.mp3")
  pygame.display.update()

def song_check():
  for song in songlist.current_selection:
    pygame.display.update()
    if song == '6 FOOT 7 FOOT':
      screen.blit(Foot_img, (0,0))
      play("music/6 FOOT 7 FOOT.mp3")
    elif song == '20 SOMETHING':
      screen.blit(Something_img,(0,0))
      play("music/20 SOMETHING.mp3")
    elif song == 'APPLYING PRESSURE':
      screen.blit(ApplyingPressure_img,(0,0))
      play("music/APPLYING PRESSURE.mp3")
    elif song == 'ALL I ASK':
      screen.blit(AllIAsk_img,(0,0))
      play("music/ALL I ASK.mp3")
    elif song == 'ALRIGHT':
      screen.blit(Alright_img,(0,0))
      play("music/ALRIGHT.mp3")
    elif song == 'ALWAYS':
      screen.blit(Always_img,(0,0))
      play("music/ALWAYS.mp3")
    elif song == 'AWKWARD':
      screen.blit(Awkward_img,(0,0))
      play("music/AWKWARD.mp3")
    elif song == 'BEAT IT':
      screen.blit(BeatIt_img,(0,0))
      play("music/BEAT IT.mp3")
    elif song == 'BEATING DOWN YO BLOCK':
      screen.blit(BeatingDown_img,(0,0))
      play("music/BEATING DOWN YO BLOCK.mp3")
    elif song == 'BEFORE HE CHEATS':
      screen.blit(BeforeHeCheats_img,(0,0))
      play("music/BEFORE HE CHEATS.mp3")
    elif song == 'BIG POPPA':
      screen.blit(BigPoppa_img,(0,0))
      play("music/BIG POPPA.mp3")
    elif song == 'BLUNT BLOWIN':
      screen.blit(BluntBlowin_img,(0,0))
      play("music/BLUNT BLOWIN.mp3")
    elif song == 'CHICAGO':
      screen.blit(Chicago_img,(0,0))
      play("music/CHICAGO.mp3")
    elif song == 'COULDVE BEEN':
      screen.blit(CouldveBeen_img,(0,0))
      play("music/COULDVE BEEN.mp3")
    elif song == 'DEAD TO ME':
      screen.blit(DeadtoMe_img, (0,0))
      play("music/DEAD TO ME.mp3")
    elif song == 'DESPUES DE LA PLAYA':
      screen.blit(Despues_img,(0,0))
      play("music/DESPUES DE LA PLAYA.mp3")
    elif song == 'FAMILY TIES':
      screen.blit(FamilyTies_img,(0,0))
      play("music/FAMILY TIES.mp3")
    elif song == 'FANCY':
      screen.blit(Fancy_img,(0,0))
      play("music/FANCY.mp3")
    elif song == 'FANETO':
      screen.blit(Faneto_img,(0,0))
      play("music/FANETO.mp3")
    elif song == 'FIRST PERSON SHOOTER':
      screen.blit(FirstPersonShooter_img,(0,0))
      play("music/FIRST PERSON SHOOTER.mp3")
    elif song == 'GANGSTA':
      screen.blit(Gangsta_img,(0,0))
      play("music/GANGSTA.mp3")
    elif song == 'GARDEN':
      screen.blit(Garden_img,(0,0))
      play("music/GARDEN.mp3")
    elif song == 'GET ALONG BETTER':
      screen.blit(GetAlongBetter_img,(0,0))
      play("music/GET ALONG BETTER.mp3")
    elif song == 'GRAVITY':
      screen.blit(Gravity_img,(0,0))
      play("music/GRAVITY.mp3")
    elif song == 'HELL N BACK':
      screen.blit(HellNBack_img,(0,0))
      play("music/HELL N BACK.mp3")
    elif song == 'HER':
      screen.blit(Her_img,(0,0))
      play("music/HER.mp3")
    elif song == 'HOW MUCH A DOLLAR COST':
      screen.blit(HowMuch_img,(0,0))
      play("music/HOW MUCH A DOLLAR COST.mp3")
    elif song == 'I THINK':
      screen.blit(IThink_img,(0,0))
      play("music/I THINK.mp3")
    elif song == 'I THOUGHT YOU WANTED TO DANCE':
      screen.blit(Sweet_img,(0,0))
      play("music/I THOUGHT YOU WANTED TO DANCE.mp3")
    elif song == 'IF I AINT GOT YOU':
      screen.blit(IfIAintGotYou_img,(0,0))
      play("music/IF I AINT GOT YOU.mp3")
    elif song == 'IF I WERE A BOY':
      screen.blit(IfIWereABoy_img,(0,0))
      play("music/IF I WERE A BOY.mp3")
    elif song == 'INSANE IN THE BRAIN':
      screen.blit(Insane_img,(0,0))
      play("music/INSANE IN THE BRAIN.mp3")
    elif song == 'JEALOUSY, JEALOUSY':
      screen.blit(JealousyJealousy_img, (0,0))
      play("music/JEALOUSY, JEALOUSY.mp3")
    elif song == 'JIMMY COOKS':
      screen.blit(JimmyCooks_img,(0,0))
      play("music/JIMMY COOKS.mp3")
    elif song == 'KEVINS HEART':
      screen.blit(KevinsHeart_img,(0,0))
      play("music/KEVINS HEART.mp3")
    elif song == 'LEMME SEE':
      screen.blit(LemmeSee_img,(0,0))
      play("music/LEMME SEE.mp3")
    elif song == 'LES':
      screen.blit(Les_img,(0,0))
      play("music/LES.mp3")
    elif song == 'LONG WAY 2 GO':
      screen.blit(LongWay2Go_img,(0,0))
      play("music/LONG WAY 2 GO.mp3")
    elif song == 'LOVERS ROCK':
      screen.blit(LoversRock_img,(0,0))
      play("music/LOVERS ROCK.mp3")
    elif song == 'LOW':
      screen.blit(Low_img,(0,0))
      play("music/LOW.mp3")
    elif song == 'LOYALTY':
      screen.blit(Loyalty_img,(0,0))
      play("music/LOYALTY.mp3")
    elif song == 'MY LIFE':
      screen.blit(MyLife_img,(0,0))
      play("music/MY LIFE.mp3")
    elif song == 'ME AND YOUR MAMA':
      screen.blit(MeandYourMama_img,(0,0))
      play("music/ME AND YOUR MAMA.mp3")
    elif song == '911':
      screen.blit(Lonely_img,(0,0))
      play("music/911.mp3")
    elif song == 'MY LOVE MINE ALL MINE':
      screen.blit(MyLove_img,(0,0))
      play("music/MY LOVE MINE ALL MINE.mp3")
    elif song == 'NEVER LOSE ME':
      screen.blit(NeverLoseMe_img,(0,0))
      play("music/NEVER LOSE ME.mp3")
    elif song == 'NO LIMIT':
      screen.blit(NoLimit_img,(0,0))
      play("music/NO LIMIT.mp3")
    elif song == 'NO LOVE':
      screen.blit(NoLove_img,(0,0))
      play("music/NO LOVE.mp3")
    elif song == 'NO ONE KNOWS':
      screen.blit(NoOneKnows_img,(0,0))
      play("music/NO ONE KNOWS.mp3")
    elif song == 'OPEN ARMS':
      screen.blit(OpenArms_img,(0,0))
      play("music/OPEN ARMS.mp3")
    elif song == 'PINK MATTER':
      screen.blit(PinkMatter_img,(0,0))
      play("music/PINK MATTER.mp3")
    elif song == 'PLAYING GAMES':
      screen.blit(PlayingGames_img,(0,0))
      play("music/PLAYING GAMES.mp3")
    elif song == 'POISON':
      screen.blit(Poison_img,(0,0))
      play("music/POISON.mp3")
    elif song == 'PYRAMIDS':
      screen.blit(Pyramids_img,(0,0))
      play("music/PYRAMIDS.mp3")
    elif song == 'REMEMBER THE TIME':
      screen.blit(Remember_img,(0,0))
      play("music/REMEMBER THE TIME.mp3")
    elif song == 'REMINDER':
      screen.blit(Reminder_img,(0,0))
      play("music/REMINDER.mp3")
    elif song == 'RIGHT THERE':
      screen.blit(RightThere_img,(0,0))
      play("music/RIGHT THERE.mp3")
    elif song == 'RUNNING OUT OF TIME':
      screen.blit(Running_img,(0,0))
      play("music/RUNNING OUT OF TIME.mp3")
    elif song == 'SHE':
      screen.blit(She_img,(0,0))
      play("music/SHE.mp3")
    elif song == 'SMOKING OUT THE WINDOW':
      screen.blit(SmokingOut_img,(0,0))
      play("music/SMOKING OUT THE WINDOW.mp3")
    elif song == 'TELEVISION':
      screen.blit(Television_img,(0,0))
      play("music/TELEVISION.mp3")
    elif song == 'SOMEONE LIKE YOU':
      screen.blit(SomeoneLikeYou_img,(0,0))
      play("music/SOMEONE LIKE YOU.mp3")
    elif song == 'STRANGE':
      screen.blit(Strange_img,(0,0))
      play("music/STRANGE.mp3")
    elif song == 'SUMMER':
      screen.blit(Summer_img,(0,0))
      play("music/SUMMER.mp3")
    elif song == 'SUPER RICH KIDS':
      screen.blit(SuperRichKids_img,(0,0))
      play("music/SUPER RICH KIDS.mp3")
    elif song == 'TELEKINESIS':
      screen.blit(Telekinesis_img,(0,0))
      play("music/TELEKINESIS.mp3")
    elif song == 'THE ART OF PEER PRESSURE':
      screen.blit(TheArtofPeer_img,(0,0))
      play("music/THE ART OF PEER PRESSURE.mp3")
    elif song == 'TITI ME PREGUNTO':
      screen.blit(TitoMe_img,(0,0))
      play("music/TITI ME PREGUNTO.mp3")
    elif song == 'UNITED IN GRIEF':
      screen.blit(United_img,(0,0))
      play("music/UNITED IN GRIEF.mp3")
    elif song == 'USED':
      screen.blit(Used_img,(0,0))
      play("music/USED.mp3")
    elif song == 'VSOP':
      screen.blit(VSOP_img,(0,0))
      play("music/VSOP.mp3")
    elif song == 'WESLEYS THEORY':
      screen.blit(Wesleys_img,(0,0))
      play("music/WESLEYS THEORY.mp3")
    elif song == 'YOU BROKE MY HEART':
      screen.blit(YouBroke_img,(0,0))
      play("music/YOU BROKE MY HEART.mp3")
  pygame.display.update()

def discover():
    songlist.song_change()
    song_check()

#game loop
pygame.init()

while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False
      if event.type == pygame.KEYDOWN and menu_state == "playlist":
        if event.key == pygame.K_SPACE:
          if paused == False:
            pygame.mixer.music.pause()
            paused = True
          elif paused == True:
            pygame.mixer.music.unpause()
            paused = False

    if menu_state == "main":
        main_menu()
    elif menu_state == "discover":
        discover_menu()
    elif menu_state == "playlist":
        playlist_menu()
    elif menu_state == "quit":
        run = False
    pygame.display.update()

pygame.quit()