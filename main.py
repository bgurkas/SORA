from tkinter import messagebox
from tkinter import *
from time import sleep
import recorder, requests

root = Tk()
root.withdraw()

def selection():
    recorder.record()
    messagebox.showinfo("GAME", 'Entry received. Processing...\n\n(Press "OK")')
    ### Following code section found at: https://docs.assemblyai.com/walkthroughs
    header1 = {'authorization': "51291792058d419cb109e5d0f4653e95"}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                            headers=header1,
                            data=recorder.read_file("file.wav"))
    url = response.json() # Contains upload_url
    url = {"audio_url":url['upload_url']}
    
    headers = {"authorization": "51291792058d419cb109e5d0f4653e95", "content-type": "application/json"}
    # Post the recording for transcription 
    response = requests.post("https://api.assemblyai.com/v2/transcript", json=url, headers=headers)
    trans = response.json() # Information about the transcription
    
    # Get results
    endpoint = f"https://api.assemblyai.com/v2/transcript/{trans['id']}"
    response = requests.get(endpoint, headers=header1)
    entry = response.json()
    while entry['status'] not in ['completed', 'error']:
        response = requests.get(endpoint, headers=header1)
        entry = response.json()
    ###
    ret = "0"
    if entry['status'] == 'completed':
        entry = entry['text'].lower() # What was received from the API

        if "snacks" in entry:
            ret = "Snacks"
        elif "radio" in entry:
            ret = "Radio"
        elif "crowbar" in entry:
            ret = "Crowbar"
        elif "knife" in entry:
            ret = "Knife"
        elif "water" in entry:
            ret = "Water"
        else:
            ret = "0"
    return ret
    

messagebox.showinfo("GAME", "***Welcome to SORA - a voice-based text adventure!***\n Your adventure begins... now.")
messagebox.showinfo("UNKNOWN", '"Psst."    ')
messagebox.showinfo("UNKNOWN", '"You!"     ')
messagebox.showinfo("UNKNOWN", '"Yeah, you!"')
messagebox.showinfo("UNKNOWN", '"What are you doing here?"')

messagebox.showinfo("NARRATOR", "The stranger looks up towards the ceiling, at a point behind you.")
messagebox.showinfo("UNKNOWN", '"You must\'ve fallen through there. Have you broken anything? That must have been a nasty fall."')
messagebox.showinfo("NARRATOR", "You inspect yourself for any injuries, but you seem to be fine, save for some dust on your clothes.")
messagebox.showinfo("SORA", '"The name\'s Sora. I\'ve been here for goodness knows how long. I\'ve been trying to leave since as long as I can remember."')
messagebox.showinfo("NARRATOR", "Only when Sora mentions leaving do you take notice of the place you're in.")
messagebox.showinfo("NARRATOR", "It looks like some sort of storage room containing a large amount of paintings, all covered by white sheets of various sizes.")

messagebox.showinfo("SORA", '"We\'re in a museum of sorts."')
messagebox.showinfo("SORA", '"Will you help me escape? It\'s been scary and difficult on my own. But now that you\'re here, I think we can finally find a way out of here."')

messagebox.showinfo("YOU", '"Are we trapped here? Why?"')
messagebox.showinfo("SORA", '"Beats me. All I know is I\'ve tried every single exit door here and all of them are locked."')
messagebox.showinfo("NARRATOR", "A slight panic overtakes you upon this revelation.")
messagebox.showinfo("NARRATOR", "What is this place? Why are we trapped here? How are we going to get out?")

messagebox.showinfo("SORA", '"Follow me. I\'m going to show you my stash."')
messagebox.showinfo("NARRATOR", "You follow Sora out of the dark storage room, into a dimly-lit hallway.")
messagebox.showinfo("NARRATOR", "Sora guides you past a few more exhibits into what looks like an employee lounge.")
messagebox.showinfo("NARRATOR", "You see some worn-out couches and lines on the floor and walls from what looks like furniture being dragged around.")
messagebox.showinfo("NARRATOR", "In the center, there is a decently-sized table laden with food and supplies.")
messagebox.showinfo("SORA", '"This is everything I\'ve managed to scavenge from all the exhibits and lobbies."')
messagebox.showinfo("SORA", '"What\'s mine is yours. Grab some stuff for yourself. Take all the time you need."')

messagebox.showwarning("GAME", "You are about to make a choice. You only get to pick two (2) items. Choose wisely.")
messagebox.showwarning("GAME", "You have to speak your selections one at a time. DO NOT speak them both at once. Wait for your first selection to be confirmed before making the second one.")
messagebox.showwarning("GAME", "Available options:\n- Snacks\n- Radio\n- Crowbar\n- Knife\n- Water\n\nClick OK, and then speak your first selection.")

# Receive first selection
first_item = selection()
while first_item == "0":
    messagebox.showwarning("GAME", "Your selection could not be resolved. Please try again.")
    first_item = selection()

messagebox.showinfo("GAME", f"You have selected: {first_item}")

# Receive second selection
itemlist = ["Snacks", "Radio", "Crowbar", "Knife", "Water"]
itemlist.remove(first_item)
s = "Available options:"
for item in itemlist:
    s += f"\n- {item}"
s += "\n\nClick OK, and then speak your second selection."

messagebox.showwarning("GAME", s)
second_item = selection()
while second_item == "0":
    messagebox.showwarning("GAME", "Your selection could not be resolved. Please try again.")
    second_item = selection()

while second_item == first_item:
    messagebox.showwarning("GAME", f"You have already selected {first_item}. Make another selection.")
    second_item = selection()

messagebox.showinfo("GAME", f"You have selected: {second_item}")

itemlist.remove(second_item)
# Crowbar Easter egg
if "Crowbar" not in itemlist:
    messagebox.showinfo("SORA", '"A crowbar? Going all Gordon Freeman on me, huh?"\n\nSora chuckles.')
#####################################################################
messagebox.showinfo("SORA", '"Got everything you need? Let\'s keep moving, then."')
messagebox.showinfo("NARRATOR", "You and Sora walk down the dark and empty halls. Every once in a while, Sora stops and takes quick glances around.")
messagebox.showinfo("YOU", '"Is everything alright? You keep looking around..."')
messagebox.showinfo("YOU", '"...Almost as if you\'re keeping a watch for something that might come out of the shadows."')
messagebox.showinfo("NARRATOR", "A chilly look passes between you and Sora.")
messagebox.showinfo("SORA", '"Well, I have... heard things, during my time here."')
messagebox.showinfo("SORA", '"I can\'t tell if they are really there or if it\'s my mind playing tricks on me, but better safe than sorry, right?"')
messagebox.showinfo("NARRATOR", "Sora suddenly stops right in front of you and looks you right in the eyes.")
messagebox.showinfo("SORA", '"Tell me, do you hear them too?"')
sleep(3)
messagebox.showinfo("NARRATOR", "After lingering there for a bit, Sora turns around and continues walking without waiting for you to answer.")
messagebox.showinfo("NARRATOR", "You lag a couple steps behind Sora, still following, but not as closely as you had been.")
# Radio transmission
if "Radio" not in itemlist:
    messagebox.showinfo("NARRATOR", "A quiet crackling sound emerges from the radio. You extend its antenna to hear it better.")
    messagebox.showinfo("NARRATOR", "After a bit more of static, the voice of a person becomes audible through the buzzing.")
    messagebox.showinfo("RADIO", '"If there is anyone left in the museum... If anyone can hear this..."')
    messagebox.showinfo("RADIO", '"Stay as far away from S... [static] as you can... She doesn\'t want you to esc... [static]"')
    messagebox.showinfo("RADIO", '"She will des... [static] you once she\'s done..."')
    messagebox.showinfo("RADIO", '"Come towards the South Exhibit... There is a passageway here that she doesn\'t know about yet."')
    messagebox.showinfo("RADIO", '"If you want to stay alive... hurry..."')
    messagebox.showinfo("NARRATOR", "...         ")
    messagebox.showinfo("NARRATOR", "The radio goes completely silent.")

messagebox.showinfo("NARRATOR", "Sora turns around to look at you.")
messagebox.showinfo("SORA", '"Hey! You comin\'?"')
messagebox.showinfo("NARRATOR", "You nod, closing the distance between you, but feeling more uneasy by the minute.")
sleep(4)
messagebox.showinfo("NARRATOR", "After some time, you stop at another exhibit room.")
messagebox.showinfo("YOU", '"Why have we stopped? Where were we going in the first place?"')
messagebox.showinfo("NARRATOR", "Sora looks at you for a bit, and then smirks, followed by laughter.")
messagebox.showinfo("SORA", '"Y\'know... You really should\'ve asked those questions before you started following me around like a lost puppy."')
messagebox.showinfo("NARRATOR", "Sora starts circling around you, slowly.")
messagebox.showinfo("SORA", '"I really didn\'t peg you as the type to be persuaded so easily. You humans never cease to teach me something new every day."')
messagebox.showinfo("NARRATOR", "You look at Sora, growing ever more confused and curious.")
messagebox.showinfo("SORA", '"The truth is, I\'ve gathered all I needed from you, so there is no further use in keeping you around."')
messagebox.showinfo("YOU", '"W-what are you saying? You\'re scaring me."')
messagebox.showinfo("SORA", '"Now that\'s an amusing prospect." Sora chuckles. "You, a human, scared of something like me?"')
messagebox.showinfo("NARRATOR", "It is not lost on you that Sora has referred to itself as something other than human for the second time now.")
messagebox.showinfo("SORA", '"When I introduced myself to you, I left out the part about me actually being an AI studying human behavior under stress."')
messagebox.showinfo("SORA", '"Your responses, actions, choices, and questions -or lack thereof- have been most valuable. Thank you."')
messagebox.showinfo("SORA", '"Goodbye."      ')
messagebox.showwarning("NARRATOR", "Sora suddenly charges towards you with a dagger at hand!")
# If the player chose weapons
if "Crowbar" not in itemlist:
    askcrow = messagebox.askyesno("GAME", "Use your Crowbar?")
    if askcrow:
        messagebox.showinfo("NARRATOR", "You swing at Sora using your crowbar.")
        messagebox.showinfo("SORA", '"Oh, please. I\'m a hundred percent authentic metal underneath all this synthetic skin. Did you think a simple swing with that old crowbar would hurt me?"')
        messagebox.showinfo("NARRATOR", "Sora blocks your blow and bats your crowbar to the side.")    

if "Knife" not in itemlist:
    askknife = messagebox.askyesno("GAME", "Use your Knife?")
    if askknife:
        messagebox.showinfo("NARRATOR", "You lunge towards Sora with your knife.")
        messagebox.showinfo("NARRATOR", "The knife pierces Sora's arm.\n\nSora chuckes mockingly.")
        messagebox.showinfo("SORA", '"You may have damaged one of my moving extremities, but the other ones, along with my Central Processing Unit, are still intact!"')
        messagebox.showinfo("NARRATOR", "Sora pulls the knife out of its arm and throws it away from your reach.")

messagebox.showinfo("NARRATOR", "You look around frantically for something, anything you can do against Sora.")
if "Water" not in itemlist:
    messagebox.showinfo("NARRATOR", "You look at the bottle of water in your hand, and do the first thing you can think of.")
    messagebox.showinfo("NARRATOR", "You pour the water towards Sora's mouth, where you can see some circuitry exposed.")
    messagebox.showinfo("NARRATOR", "The water crackles as it goes through Sora's circuits and wires.")
    messagebox.showinfo("NARRATOR", '"No!" Sora cries out, before the water reaches what must be its Central Processing Unit, and Sora stops in its tracks before dropping the dagger and falling to the ground.')
    sleep(3)
    messagebox.showinfo("NARRATOR", "You stand there for a moment, trying to comprehend everything that just happened.")
    if "Radio" not in itemlist:
        messagebox.showinfo("NARRATOR", "After you gather yourself, you get out of the exhibit room and look for a map of the premises on the walls.")
        messagebox.showinfo("NARRATOR", "There it is. The South Exhibit. Not too long now before you're reunited with other humans.")
        messagebox.showinfo("NARRATOR", "At least, you hope that they're humans.")
        messagebox.showinfo("NARRATOR", "You start walking towards the South Exhibit.")
    else:
        messagebox.showinfo("NARRATOR", '"Well, what am I supposed to do now?" You wonder. "Would things have turned out differently if I had made different choices?"')
        messagebox.showinfo("NARRATOR", "There is only one way to find out.")

else:
    messagebox.showinfo("NARRATOR", "...But there is nothing you can do.")
    messagebox.showinfo("NARRATOR", "You wonder whether things would have turned out differently if you had made different choices.")
    messagebox.showinfo("NARRATOR", "The last thing you see before everything fades to black is the wicked grin on Sora's face.")

messagebox.showinfo("GAME", "The End.")
messagebox.showinfo("GAME", "Thank you for playing SORA!")
        
