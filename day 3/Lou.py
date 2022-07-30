print("Every year a total of 58 children go missing from the children's orphanage on Elm's Street.");
print("No investsigations are carried out. No one goes looking for the children. No one cares.");
print("---------------------------------------------------------------------------------------------");
print("Lou! Lou! LOUUU!!!");
print("Lou: huh, wha? ");
print("""
A tiny head pops from under a little bundle of covers. The red of her hair is undistinguishable from that of 
the curtains hanging on the windows.\n
""");

awake = input("wake up / sleep? ");
if awake == "wake up":
    print("Lou: I'm up. i'm up. what?\n");
else:
    print("Lizzie: Wake up! she's almost here.\n");

print("Lizzie truts toward Lou and helps her off her feet. what ever will i do with you.");
print("""
The two girls help make the bed as the other girls quitely watch on. They stand and stare at the door
as sounds of footsteps approach.\n
The door burst open and every girl stood rooted beside her bed and looked straight ahead. A woman being escorted 
by a girl a little older than the ones standing in the room.
""");

print("""
Madame: Good morning 
Girls(chorus): Good morning Madame!

Madame walks up to Lou's bed and starts to remove the covers from the bed. Lou's face springs from sleepy to
terrified. Madame shakes the covers and not finding what she is looking for drops the covers on the ground.

Madame: Cindy, look under the bed.
""");

voice = input("say something / say nothing? ");
if voice == "say something":
    print("""
    Lou: Whatever you're looking for you won't find it there.
    """);
    print("""
    Madame: Whatever i'm looking for? You little wench were's the money i left on the counter?
    """)

voice = input("what money / I didn't take it!");
if voice == "what money":
    print("""
    Madame: You little
    Madame walks up to Lou and strikes her accross the face. Lou's fragile body twists sharply and tumbles on
    the floor.

    Madame: Lucy, put Lou in the carboard downstairs. She won't be eating today.
    """);
elif voice == "i didn't take it!":
    print("""
    Madame: No one asked you if took it or not.
    Lou: Then stop looking for it in my things.
    """)
