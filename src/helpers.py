from PIL import Image,ImageTk
import tkinter as tk

def clear_widgets(root):
    #This function destroys any created widgets
    for i in root.winfo_children():
        i.destroy()

#chatbot for when there are no matching groups to the filters chosen by the user
def chatbot_page (root, width, height):
    # create variables to format
    bg_colour = "#E6C0B3"
    text_colour = "#EAECEE"
    font = "Helvetica 14"
    font_bold = "Helvetica 13 bold"

    # place a welcome label
    welcome_label = tk.Label(root,
                             text="Welcome to the ChatBot",
                             bg="#D9A693",
                             fg=text_colour,
                             font=font_bold,
                             # pady=10,
                             width=30,
                             height=1)

    welcome_label.place(relx=0.5,
                        y=17,
                        anchor=tk.CENTER)  # place in center

    # create the text box
    text_box = tk.Text(root,
                       bg="#E6C0B3",
                       fg="black",
                       font=font,
                       width=60)
    text_box.place(x=0, y=30, relwidth=1, relheight=1)  # these attributes ensure it takes up the entire screen
    text_box.insert(tk.END, "Bot: Hi there! Unfortunately, there are currently no groups found for your filters. "
                            "We will      gladly inform you, once new groups that fit your filters join."
                            "If you have questions or we      can help with anything in the meantime, we are happy "
                            "to help!"
                            )

    # create a scrollbar for the textbox
    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1,
                     relx=0.974)

    # create an entry box for user to enter message
    entry_box = tk.Entry(root,
                         bg="lightgray",
                         fg="black",
                         font=font,
                         width=55
                         )
    entry_box.place(x=5, rely=0.925)

    send_button = tk.Button(root,
                            text="Send",
                            font=font_bold,
                            bg="#ABB2B9",
                            width=10)
    send_button.place(relx=0.82, rely=0.925)

# This creates the background of the first page, the welcome page.
def place_welcome_page(root,screen_width,screen_height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)

    img1 = Image.open("images/intro_pic.jpg")
    img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

# This creates the background of the city filter page, while placing the city pictures
#   onto the primary background.
def place_cities_on_homescreen(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 180
    img2 = Image.open("images/pic_lüni.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/pic_hamburg.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img4 = Image.open("images/pic_berlin.jpg")
    img4 = img4.resize((resized_width, resized_height), Image.LANCZOS)

    img5 = Image.open("images/pic_wob.jpg")
    img5 = img5.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (85, 80))
    img1.paste(img3, (415, 80))
    img1.paste(img4, (85, 280))
    img1.paste(img5, (415, 280))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

# This creates the background of the gender filter page, while placing the gender pictures
#   onto the primary background.
def place_gender_on_homescreen(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 200
    resized_height = 180
    img2 = Image.open("images/female_pink.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/male_pink.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img4 = Image.open("images/non_b_pink.jpg")
    img4 = img4.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (60, 180))
    img1.paste(img3, (270, 180))
    img1.paste(img4, (480, 180))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()


# This creates the background of the age group filter page, while placing the age group pictures
#   onto the primary background.
def place_ages_on_homescreen(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 180
    img2 = Image.open("images/teens_pic.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/y.adults_pic.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img4 = Image.open("images/adults_pic.jpg")
    img4 = img4.resize((resized_width, resized_height), Image.LANCZOS)

    img5 = Image.open("images/seniors_pic.jpg")
    img5 = img5.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (85, 80))
    img1.paste(img3, (415, 80))
    img1.paste(img4, (85, 280))
    img1.paste(img5, (415, 280))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

# This definition includes the labels that are always needed on the group suggestion pages
#   label such as the header, and messages that invites the user to read through the groups.
def labels_for_group_suggestions_pages(root, width, height):
    global message, second_message

    message = tk.Label(text="YOUR POSSIBLE GROUPS",
                      font="arial 20 ",
                      height="1",
                      width="40",
                      bg="darkslategray",
                      fg="white"
                      )
    message.place(x=50, y=15)

    second_message = tk.Label(text="Here are possible groups you might like to join!",
                              font="arial 15 italic",
                              bg="darkslategray",
                              fg="white"
                              )
    second_message.place(x=165, y=450)

    second_message = tk.Label(text="Feel free to check out different groups\n and their description!",
                              font="arial 13 italic",
                              bg="darkslategray",
                              fg="white"
                              )
    second_message.place(x=240, y=490)

def labels_for_individual_group_pages(root):
    global info_data, conact, write_contact

    info_data = tk.Label(
        text="""If you are interested in joining,\n send us a message or leave your contact below.\n We cannot wait to meet you!""",
        font="arial 10",
        height="3",
        width="36",
        bg="rosybrown2",
        fg="black"
    )
    info_data.place(x=430, y=320)

    contact = tk.StringVar()
    contact_box = tk.Entry(root,
                           font="arial 15 italic",
                           width="19",
                           fg="rosybrown",
                           bg="white")
    contact_box.place(x=450, y=420)

    write_contact = tk.Label(text="chat here:",
                             font="arial 9 ",
                             height="1",
                             width="8",
                             bg="mistyrose"
                             )
    write_contact.place(x=450, y=393)


# Following are the 12 backgrounds for the suggested groups pages (line 213-495).
# The possible group pictures are placed onto the primary background.
def background_pics1(root,  width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/girlspic_lüni.JPG")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/runningpic.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics2(root,  width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250

    img2 = Image.open("images/runningpic.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (250, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()
def background_pics3(root,  width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/pic_choir.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/runningpic.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics4(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/pic_youthgroup.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/pic_dogs.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics5(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 210
    resized_height = 210
    img2 = Image.open("images/pic_youthgroup.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/golferpic.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img4 = Image.open("images/pic_dogs.jpg")
    img4 = img4.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (30, 140))
    img1.paste(img3, (270, 140))
    img1.paste(img4, (510, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics6(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/golferpic.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/pic_dogs.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics7(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/culture_group_latinos.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/momgroup.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()
def background_pics8(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 210
    resized_height = 210
    img2 = Image.open("images/culture_group_latinos.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/hikinggroup.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img4 = Image.open("images/momgroup.jpg")
    img4 = img4.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (30, 140))
    img1.paste(img3, (270, 140))
    img1.paste(img4, (510, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics9(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/culture_group_latinos.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/hikinggroup.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics10(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250

    img2 = Image.open("images/culture_group_latinos.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (250, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics11(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/pic_mexicanas.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/pic_paint.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def background_pics12(root, width, height):
    global f1, pic, img, Lab

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 250
    resized_height = 250
    img2 = Image.open("images/pic_mexicanas.jpg")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img3 = Image.open("images/pic_cooking.jpg")
    img3 = img3.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (120, 140))
    img1.paste(img3, (400, 140))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

# Following are only the full 12 individual group pages with detailed information about them (line 500-1122/End)
#   All of these follow the same structure and in the order of the cities they are in:
#       1. Lüneburg, 2. Hamburg, 3. Berlin, 4. Wolfsburg.
def mdm_girls_page(root, width, height):
    global f1, pic, img, Lab, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((width, height), Image.LANCZOS)

    resized_width = 220
    resized_height = 200
    img2 = Image.open("images/girlspic_lüni.JPG")
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (450, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="MDM Girls:)",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
    Hey you!:)
    Welcome to our New Meet page! Let´s introduce ourselves to you.
    We are a group of girls that study Digital Media at the Leuphana
    University in Lüneburg. All of us started last year and have
    grown our friendships over that last year. We like to hang out a lot
    during the week or also on the weekends. Since we are all from
    other cities, that we like to visit occasionally, its usually
    only a couple of the friends hanging out! We like to have
    dinner nights, either eating out or cooking together. We love
    having picknicks in the park or also going to the lake swimming.
    Sometimes we also do things very spontaneously, like getting some
    ice cream or going to the cinema! We just text in our group chat
    and see who’s in town and down to spend time together!
    If there are any events near us, we are most likely to go together
    and have a lot of fun😊""",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def runners_page(root, width, height):
    global f1, pic, img, Lab, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/runningpic.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="LüneRunners",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""Hi there!
    We are a group of women that love to go running together!
    We also train for the marathon, which we run twice a year.
    for that we meet every Monday and Thursday at 5 PM. Our 
    runs are usually about 2 hours and we like to switch our 
    routes as often as we can! It is also important for us
    to have checkpoints to see if we all want keep going or 
    if there are a a couple of us who´d prefer to run back!
    It is important for us to know how everyone is feeling 
    and that no one feels pressured to run more than they would
    like. Even if you are not interested in running a marathon 
    but want to go running with a friendly group, this is for you!
    We go running for our health and our fun. Not to pressure 
    ourselves or to be the best at it! It´s all about the fun
    and experience we get to have together!!

    We usually go run on Mondays and Thursdays at 5PM. If our
    schedules change, we also adapt our runs! We love getting to
    know new faces of amazing women! So come join us and lets
    have great runs together!
    """,
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def choir_page(root, width,height):
    global f1, pic, img, Lab, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_choir.jpg")
    img2 = img2.resize((240, 220), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="LüneChoir",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""Good day our friend!
    We are the LüneChoir and we just love to sing. This choir was 
    started in the late 1920´s by original lüneburgers. Since then
    the tradition of making music together was hold onto and enjoyed.
    In our choir we sing a lot of classical pieces, as well as opera
    and sometimes acapella. Throughout the year we give concerts at 
    the church and local events. For that we practice every tuesday 
    at 7PM in the community hall of the central church. 
    In the winter we also celebrate our annual christmas celebration 
    in which everyone´s family can come and enjoy.
    Everyone is welcome to come to this choir to let our history
    keep going! See you on tuesday.
            """,
                         anchor="w",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def youthgroup_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_youthgroup.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Young and Faithful",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
    Hey there, young hearts in Hamburg! 
    Join our dynamic church youth group as we come together
    for fellowship, fun, and faith. We're a welcoming and spirited 
    community that meets regularly to build friendships, share meals, 
    participate in exciting activities, and explore the teachings of Jesus.
    Whether you're new to the area or looking to connect with 
    like-minded young people, our group is a safe space for open 
    conversations, laughter, and spiritual growth. Come for the great 
    company, stay for the adventures, and leave with a deeper 
    understanding of the message of Jesus. If you're seeking to 
    form lasting connections, enjoy memorable moments, and 
    strengthen your faith journey, we invite you to be a part of 
    our vibrant youth group. Come join us to discover more about 
    our upcoming events and how you can join us on this exciting 
    and spiritual journey. Be blessed!""",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def golfers_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/golferpic.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Golfers Hamburg",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
    If you're looking for a fun and relaxed golfing group, 
    you've found your tribe. We're a small, close-knit community 
    of golfers who gather every two weeks to enjoy the greens, 
    great company, and delicious post-game lunches. Whether you're
    a seasoned pro or new to the game, our group is all about 
    sharing the love for golf in a friendly and welcoming 
    atmosphere. Swing by for a round of golf, catch up with fellow 
    golfers, and savor a tasty lunch together. Join us to perfect 
    your putt and make lasting connections. If you want to become 
    part of our golfing family in Hamburg, just send us a message!""",

                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def dogs_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_dogs.jpg")
    img2 = img2.resize((240, 220), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Dog Lovers",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text=""" 
    Calling all Hamburg dog lovers!
    Join our vibrant community of dog owners as we gather three 
    times a week at our beloved dog playground. Our group is a 
    passionate and welcoming bunch of canine enthusiasts who share 
    a common bond - the love for our furry companions. Whether you 
    have a playful pup or a seasoned senior, our diverse group of 
    members celebrates the joy and companionship that dogs bring 
    to our lives. Come and connect with like-minded individuals, 
    let your furry friends run free, and enjoy quality time with 
    fellow dog enthusiasts. Whether you're a seasoned local or new 
    to Hamburg, we invite you to be a part of our pack! Explore our 
    website to find out more and join us in making every visit to 
    the dog park an unforgettable experience.""",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def latinos_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pic_bgp.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/culture_group_latinos.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Berlin Latinos",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""¡Bienvenidos a Latinos en Berlín!
    We are a vibrant and close-knit community of Latinos living in the 
    heart of Berlin. Every two weeks, we come together for exciting 
    gatherings that celebrate our rich culture and foster connections 
    within our diverse group. Our website is the central hub for our 
    community, where we extend a warm invitation to all Latinos in 
    Berlin to join us in our adventures. Whether you're from Mexico, 
    Argentina, Colombia, or any other Latin American country, you'll
    find a place here with us.
    Our gatherings are a blend of camaraderie, delicious cuisine, and 
    fun activities. We explore the city's culinary treasures, savoring
    the flavors of home at local Latin American restaurants. We also 
    organize various activities, from dance lessons to movie nights,
    ensuring there's something for everyone to enjoy.
    So, if you're looking to connect with fellow Latinos, experience 
    the best of Berlin's culture, and create lasting memories, come 
    buy to join us!
    ¡Nos vemos pronto!
    -this text was written by Chat GPT-
    """,
                         anchor="w",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def moms_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/momgroup.jpg")
    img2 = img2.resize((240, 220), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Moms and Kids",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""Introducing Berlin Moms & Kids Connect!
    We understand that being a mom doesn't mean you have to 
    Give up on friendships and fun. In the bustling city of Berlin, 
    our group thrives on creating a space where moms and their 
    little ones can come together to bond, socialize, and enjoy
    the journey of parenthood while nurturing meaningful friendships. 
    We believe in the power of community and the importance of 
    having a support network while raising children. 
    Our group organizes a variety of family-friendly events and 
    Activities around Berlin, from playdates at local parks to exploring
    the city's museums, cafés, and more.
    At Berlin Moms & Kids Connect, you'll find a warm and
    welcoming community of mothers who understand the need for
    balance in life.  We're here to help you build lasting friendships for
    both you and your children, ensuring that your journey through 
    motherhood is filled with cherished moments and a support 
    system you can rely on.
    Join us today and discover a fantastic way to stay connected with 
    fellow moms and cultivate meaningful friendships while still 
    enjoying all that Berlin has to offer!
    -this text was generated by chat GPT-

    """,
                         anchor="w",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def hikers_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/hikinggroup.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Berlin Harz Hikers",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""Welcome to the Berlin Harz Hikers! 
    Our vibrant group is composed of adventurous individuals aged
    20 to 40, all hailing from the bustling  city of Berlin, Germany. 
    We share a deep passion for the great outdoors and love to 
    explore the stunning landscapes of the Harz region together. Our
    group is all about fostering a sense of camaraderie and adventure. 
    Whether you're a seasoned hiker or just starting out on your 
    outdoor journey, you'll find a warm and welcoming community
    here. We organize regular hikes in the breathtaking Harz 
    Mountains, offering a variety of trails and challenges to suit 
    different skill levels. 
    Join us for thrilling hikes through lush forests,
    along picturesque rivers, and up to scenic mountain peaks. As we
    trek through the Harz, we not only enjoy the beauty of nature but
    also build lasting friendships and create unforgettable memories. 

    If you're looking to connect with like-minded individuals in Berlin 
    who share your love for hiking and the great outdoors, our group 
    is the perfect place for you. Join the Berlin Harz Hikers today and 
    embark on incredible adventures in one of Germany's most
    captivating natural landscapes!
    -this text was generated by chat GPT-
    """,
                         anchor="w",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def mexicans_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_mexicanas.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Mexicanos Unidos",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
    ¡Bienvenidos a nuestra comunidad mexicana en Wolfsburg!
    Join us every week as we come together to celebrate our Mexican 
    heritage and create a home away from home. Most of us have 
    relocated to Germany, following a family member's work 
    opportunity, and we've found strength and solace in forming this
    tight-knit group. Our gatherings are a taste of Mexico in the 
    heart of Wolfsburg - from the aroma of authentic Mexican cuisine 
    to the vibrant sounds of our music and the warmth of our 
    conversations. Whether you're missing the flavors of home, 
    seeking connections with fellow expats, or simply looking to 
    share your experiences, we invite you to be part of our Mexican 
    family in Wolfsburg. We would love for you to come to our next 
    get together and become a part of our growing community! 
    ¡Nos vemos pronto!""",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def paint_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_paint.jpg")
    img2 = img2.resize((220, 200), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Paint and Read",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
    Calling all art and book lovers in Wolfsburg!!
    Join our creative community as we gather every three weeks 
    to explore the beauty of painting and the magic of literature.
    Our group is a perfect blend of artistic expression and 
    literary appreciation. We meet in a cozy and inspiring setting
    to paint, read, and share our favorite book recommendations.
    Whether you're an experienced painter or simply have a passion
    for the written word, our group welcomes all skill levels. 
    Discover the joy of artistic expression, engage in lively 
    discussions about the latest books, and get lost in the world 
    of storytelling with like-minded individuals. If you're looking
    to infuse your life with art and literature, we invite you to 
    become a part of our harmonious blend of creativity and 
    culture. Visit our instagram or send a message on new meet
    to find out more about our upcoming gatherings and how you 
    can join us in our artistic and literary adventures!""",

                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)

def cooking_page(root, width, height):
    global f1, pic, Lab, titel_gruppe, info_text

    f1 = tk.Frame(root)
    img1 = Image.open("images/pink.bg.jpg")
    img1 = img1.resize((750, 550), Image.LANCZOS)

    img2 = Image.open("images/pic_cooking.jpg")
    img2 = img2.resize((240, 220), Image.LANCZOS)

    img1.paste(img2, (460, 80))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

    titel_gruppe = tk.Label(text="Cooking to explore!",
                            font="arial 20",
                            height="1",
                            width="40",
                            bg="darksalmon",
                            fg="white"
                            )
    titel_gruppe.place(x=60, y=15)

    info_text = tk.Label(text="""
            Hey Friend!
    Lets discover the joy of culinary exploration together!
    Join our diverse group of food enthusiasts as we come together 
    every two weeks to embark on a delicious journey of cooking 
    something new and exciting. We gather at the welcoming 
    community room and kitchen of our local church, turning 
    it into a lively hub of creativity and flavor. 
    Whether you're a seasoned chef or a complete beginner,
    our group is all about sharing our passion for cooking 
    and discovering new dishes. We take turns choosing recipes,
    learning from each other, and savoring the delectable 
    results together. If you're eager to expand your culinary 
    horizons and connect with fellow food lovers in Wolfsburg, 
    we invite you to become a part of our kitchen adventures. 
    Send us a message to receive the information for our next 
    get together! We are more than happy to send it to you!!""",
                         height=28,
                         width=50,
                         bg="mistyrose1",
                         fg="black"
                         )
    info_text.place(x=60, y=80)