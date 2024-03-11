import tkinter
import tkinter as tk
from PIL import Image, ImageTk
from src.helpers import clear_widgets, place_welcome_page, place_cities_on_homescreen, \
    place_gender_on_homescreen, place_ages_on_homescreen, \
    background_pics1, background_pics2, background_pics3, background_pics4, background_pics5, \
    background_pics6, background_pics7, background_pics8, background_pics9, background_pics10, \
    background_pics11, background_pics12, labels_for_group_suggestions_pages, \
    labels_for_individual_group_pages, chatbot_page, \
    mdm_girls_page, choir_page, runners_page, youthgroup_page, golfers_page, dogs_page, \
    latinos_page, moms_page, hikers_page, mexicans_page, paint_page, cooking_page

# Above you find all definitions imported from the helpers file
# These are definitions such as the 16 backgrounds for all pages including
#   the city, age and gender page as well as the 12 different suggested
#   groups pages once the user chooses their filters.
# Additionally, all individual group pages are defined in order to import them as a whole page in this code



# creates the gui frame
root = tk.Tk()
root.title("https://www.newmeet.com")
# size the size of the frame
screen_width = 750
screen_height = 550

# adjusts to frame size
root.minsize(screen_width, screen_height)

#defines what the send button does (found on all individual group pages + chatbot)
def send():
    message = tkinter.Label(text= "Your Message has been sent successfully!",
                             font='lucida 12 bold',
                             fg="white",
                             bg="darkslategray")
    message.place(x=220, y=290)


# Following are the definitions of the 12 individual groups (line 39 - 364)
# These are the group pages that include their description and a possibility
#   for the user to contact the group
def mdm_girls_group(root, width, height):
# Group 1
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    mdm_girls_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def runners_group(root, width,height):
# Group 2
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    runners_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)
def choir_group(root, width, height):
# Group 3
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    choir_page(root, width,height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command = lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def youthgroup_group(root, width, height):
# Group 4
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    youthgroup_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def golfers_group(root, width, height):
# Group 5
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    golfers_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def dogs_group(root, width, height):
# Group 6
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    dogs_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def latinos_group(root, width, height):
# Group 7
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    latinos_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def moms_group(root, width, height):
# Group 8
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    moms_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def hikers_group(root, width, height):
# Group 9
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    hikers_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def mexicans_group(root, width, height):
# Group 10
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    mexicans_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)


def paint_group(root, width, height):
# Group 11
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    paint_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)

def cooking_group(root, width, height):
# Group 12
    global back_button

    clear_widgets(root)
    # Full group page called from helpers file.
    cooking_page(root, width, height)
    # Calls the fixed labels for the individual group pages onto the page.
    labels_for_individual_group_pages(root)

    send_contact = tk.Button(text="SEND",
                             font="arial 10 ",
                             height="1",
                             width="5",
                             bg="white",
                             fg="black",
                             command=lambda: send()
                             )
    send_contact.place(x=667, y=419)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="salmon",
                            bg="white")
    back_button.place(x=600, y=475)


# Following are the definitions for the pages that show up depending
#   on what filters the user chooses (line 371-769).
# There are 12 possible suggested groups pages as well as the chatbot,
#   that is found in line 772 -799.
def lüneburg_and_young_adults_1(root, width, height):
    global mdm_girls, runners, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics1(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    mdm_girls = tk.Button(text="MDM Girls",
                            font="arial 12 bold",
                            height=1,
                            width=12,
                            bg="darksalmon",
                            command=lambda: mdm_girls_group(root, width, height)
                            )
    mdm_girls.place(x=180, y=380)


    runners = tk.Button(text="LüneRunners",
                          font="arial 12 bold",
                          height=1,
                          width=12,
                          bg="darksalmon",
                         command=lambda: runners_group(root, width, height)
                          )
    runners.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def lüneburg_and_young_adults_2(root, width, height):
    global runners, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics2(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    runners = tk.Button(text="LüneRunners",
                          font="arial 12 bold",
                          height=1,
                          width=12,
                          bg="darksalmon",
                         command=lambda: runners_group(root, width, height)
                          )
    runners.place(x=315, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def lüneburg_and_adults(root, width, height):
    global choir, runners, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics3(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    choir = tk.Button(text="LüneChoir",
                          font="arial 12 bold",
                          height=1,
                          width=12,
                          bg="darksalmon",
                          command=lambda: choir_group(root, width, height)
                          )
    choir.place(x=180, y=380)

    runners = tk.Button(text="LüneRunners",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: runners_group(root, width, height)
                        )
    runners.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def hamburg_and_teens(root, width, height):
    global youthgroup, dogs, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics4(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    youthgroup = tk.Button(text="Young and Faithful",
                      font="arial 12 bold",
                      height=1,
                      width=17,
                      bg="darksalmon",
                      command=lambda: youthgroup_group(root, width, height)
                      )
    youthgroup.place(x=160, y=380)

    dogs = tk.Button(text="Dog Lovers",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: dogs_group(root, width, height)
                        )
    dogs.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)


def hamburg_and_young_adults(root, width, height):
    global youthgroup, golfers, dogs, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics5(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    youthgroup = tk.Button(text="Young and Faithful",
                      font="arial 12 bold",
                      height=1,
                      width=17,
                      bg="darksalmon",
                      command=lambda: youthgroup_group(root, width, height)
                      )
    youthgroup.place(x=45, y=340)

    golfers = tk.Button(text="Golfers Hamburg",
                      font="arial 12 bold",
                      height=1,
                      width=13,
                      bg="darksalmon",
                      command=lambda: golfers_group(root, width, height)
                      )
    golfers.place(x=310, y=340)

    dogs = tk.Button(text="Dog Lovers",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: dogs_group(root, width, height)
                        )
    dogs.place(x=560, y=340)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def hamburg_and_adults(root, width, height):
    global dogs, golfers, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics6(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    golfers = tk.Button(text="Golfers Hamburg",
                      font="arial 12 bold",
                      height=1,
                      width=13,
                      bg="darksalmon",
                      command=lambda: golfers_group(root, width, height)
                      )
    golfers.place(x=180, y=380)

    dogs = tk.Button(text="Dog Lovers",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: dogs_group(root, width, height)
                        )
    dogs.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def berlin_and_teens(root, width, height):
    global latinos, moms, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics7(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    latinos = tk.Button(text="Berlin Latinos",
                        font="arial 12 bold",
                        height=1,
                        width=13,
                        bg="darksalmon",
                        command=lambda: latinos_group(root, width, height)
                        )
    latinos.place(x=180, y=380)

    moms = tk.Button(text="Moms and Kids",
                     font="arial 12 bold",
                     height=1,
                     width=13,
                     bg="darksalmon",
                     command=lambda: moms_group(root, width, height)
                     )
    moms.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def berlin_and_young_adults1(root, width, height):
    global latinos, hikers, moms, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics8(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    latinos = tk.Button(text="Berlin Latinos",
                           font="arial 12 bold",
                           height=1,
                           width=12,
                           bg="darksalmon",
                           command=lambda: latinos_group(root, width, height)
                           )
    latinos.place(x=72, y=340)

    hikers = tk.Button(text="Berlin Harz Hikers",
                        font="arial 12 bold",
                        height=1,
                        width=14,
                        bg="darksalmon",
                        command=lambda: hikers_group(root, width, height)
                        )
    hikers.place(x=300, y=340)

    moms = tk.Button(text="Moms and Kids",
                     font="arial 12 bold",
                     height=1,
                     width=12,
                     bg="darksalmon",
                     command=lambda: moms_group(root, width, height)
                     )
    moms.place(x=550, y=340)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def berlin_and_young_adults2(root, width, height):
    global latinos, hikers, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics9(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    latinos = tk.Button(text="Berlin Latinos",
                        font="arial 12 bold",
                        height=1,
                        width=13,
                        bg="darksalmon",
                        command=lambda: latinos_group(root, width, height)
                        )
    latinos.place(x=180, y=380)

    hikers = tk.Button(text="Berlin Harz Hikers",
                     font="arial 12 bold",
                     height=1,
                     width=14,
                     bg="darksalmon",
                     command=lambda: hikers_group(root, width, height)
                     )
    hikers.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def hamburg_and_seniors(root, width, height):
    global latinos, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics10(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    # hier kommen die möglichen gruppen hin con vorherigem final

    latinos = tk.Button(text="Berlin Latinos",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: latinos_group(root, width, height)
                        )
    latinos.place(x=315, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def wolfsburg_and_teens(root, width, height):
    global mexicans, paint, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics11(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    mexicans = tk.Button(text="Mexicanos Unidos",
                        font="arial 12 bold",
                        height=1,
                        width=15,
                        bg="darksalmon",
                        command=lambda: mexicans_group(root, width, height)
                        )
    mexicans.place(x=180, y=380)

    paint = tk.Button(text="Paint and Read",
                       font="arial 12 bold",
                       height=1,
                       width=14,
                       bg="darksalmon",
                       command=lambda: paint_group(root, width, height)
                       )
    paint.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

def wolfsburg_and_all_adults(root, width, height):
    global mexicans, cooking, back_button

    clear_widgets(root)
    # Calls the corresponding background and fixed labels onto the page.
    background_pics12(root, width, height)
    labels_for_group_suggestions_pages(root, width, height)

    mexicans = tk.Button(text="Mexicanos Unidos",
                        font="arial 12 bold",
                        height=1,
                        width=15,
                        bg="darksalmon",
                        command=lambda: mexicans_group(root, width, height)
                        )
    mexicans.place(x=180, y=380)

    cooking = tk.Button(text="Paint and Read",
                       font="arial 12 bold",
                       height=1,
                       width=14,
                       bg="darksalmon",
                       command=lambda: cooking_group(root, width, height)
                       )
    cooking.place(x=460, y=380)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="darksalmon")
    back_button.place(x=600, y=500)

# Page that opens, if there is no possible group found for the filters chosen.
def chatbot(root, width, height):
    global back_button

    clear_widgets(root)
    # Full chatbot called from helpers file (excluding send_ and back_button).
    chatbot_page(root, width, height)

    send_button = tk.Button(root,
                            text="Send",
                            font="Helvetica 13 bold",
                            bg="#ABB2B9",
                            width=10,
                            command=lambda: send()
                            )
    send_button.place(relx=0.82,
                      rely=0.925)

    back_button = tk.Button(text="Back to homepage",
                            font='lucida 10 bold',
                            command=lambda: back_homepage(root, width, height),
                            fg="black",
                            bg="#ABB2B9")
    back_button.place(x=2, y=1)

# Following in the definition is the if-else-Statement, in which the chosen
#   filter combination(s) define which groups (/suggested group pages)
#   will be suggested to the user. (line 806-863)
# This also saves the previous age filter selection.
def suggestions(age_selection, width, height):
    global user_age_selection

    user_age_selection = age_selection

#Lüneburg Young Adults
    if user_city_selection == "Lüneburg" and user_gender_selection == "Female" and user_age_selection =="Young Adults" :
        lüneburg_and_young_adults_1(root, width, height)
    elif user_city_selection == "Lüneburg" and user_gender_selection == "Non-Binary" and user_age_selection =="Young Adults" :
        lüneburg_and_young_adults_1(root, width, height)
    elif user_city_selection == "Lüneburg" and user_gender_selection == "Male" and user_age_selection =="Young Adults" :
        lüneburg_and_young_adults_2(root, width, height)
# Lüneburg Adults
    elif user_city_selection == "Lüneburg" and user_age_selection =="Adults":
        lüneburg_and_adults(root, width, height)
#Lüneburg Seniors
    elif user_city_selection == "Lüneburg" and user_age_selection =="Seniors":
        lüneburg_and_adults(root, width, height)

# Hamburg all ages
    elif user_city_selection == "Hamburg" and user_age_selection =="Teens" :
        hamburg_and_teens(root, width, height)
    elif user_city_selection == "Hamburg" and user_age_selection == "Young Adults":
        hamburg_and_young_adults(root, width, height)
    elif user_city_selection == "Hamburg" and user_age_selection == "Adults":
        hamburg_and_adults(root, width, height)
    elif user_city_selection == "Hamburg" and user_age_selection == "Seniors":
        hamburg_and_adults(root, width, height)

# Berlin Teens
    elif user_city_selection == "Berlin" and user_gender_selection == "Female" and user_age_selection =="Teens" :
        berlin_and_teens(root, width, height)
    elif user_city_selection == "Berlin" and user_gender_selection == "Non-Binary" and user_age_selection =="Teens" :
        berlin_and_teens(root, width, height)
# Berlin Young Adults
    elif user_city_selection == "Berlin" and user_gender_selection == "Female" and user_age_selection == "Young Adults":
        berlin_and_young_adults1(root, width, height)
    elif user_city_selection == "Berlin" and user_gender_selection == "Non-Binary" and user_age_selection == "Young Adults":
        berlin_and_young_adults1(root, width, height)
    elif user_city_selection == "Berlin" and user_gender_selection == "Male" and user_age_selection == "Young Adults":
        berlin_and_young_adults2(root, width, height)
# Berlin Adults
    elif user_city_selection == "Berlin" and user_gender_selection == "Female" and user_age_selection == "Adults":
        berlin_and_young_adults1(root, width, height)
    elif user_city_selection == "Berlin" and user_gender_selection == "Non-Binary" and user_age_selection == "Adults":
        berlin_and_young_adults1(root, width, height)
    elif user_city_selection == "Berlin" and user_gender_selection == "Male" and user_age_selection == "Adults":
        berlin_and_young_adults2(root, width, height)
# Berlin Seniors
    elif user_city_selection == "Berlin" and user_age_selection == "Seniors":
        hamburg_and_seniors(root, width, height)

# Wolfsburg all ages
    elif user_city_selection == "Wolfsburg" and user_age_selection =="Teens" :
        wolfsburg_and_teens(root, width, height)
    elif user_city_selection == "Wolfsburg" and user_age_selection == "Young Adults":
        wolfsburg_and_all_adults(root, width, height)
    elif user_city_selection == "Wolfsburg" and user_age_selection == "Adults":
        wolfsburg_and_all_adults(root, width, height)
    elif user_city_selection == "Wolfsburg" and user_age_selection == "Seniors":
        wolfsburg_and_all_adults(root, width, height)

    else:
        chatbot(root, width, height)

# This saves the gender filter selection and shows age group page with 4 options for user to choose from.
def create_age_page(root, width, height, gender_selection):
    global user_gender_selection

    clear_widgets(root)

    user_gender_selection = gender_selection
    #calls the corresponding background of page
    place_ages_on_homescreen(root, width, height)

    welcome = tk.Label(text="FIND YOUR AGE GROUP",
                       font="arial 20 ",
                       height="1",
                       width="40",
                       bg="darkslategray",
                       fg="white"
                       )
    welcome.place(x=50, y=15)

    second_message = tk.Label(text=" Please choose your age group.",
                              font="arial 15 italic",
                              bg="darkslategray",
                              fg="white"
                              )
    second_message.place(x=230, y=490)

    age_button1 = tk.Button(text="Teens",
                         font="arial 12 bold",
                         height=1,
                         width=12,
                         bg="darksalmon",
                         command=lambda: suggestions("Teens", width, height)
                         )
    age_button1.place(x=145, y=240)

    age_button2 = tk.Button(text="Young Adults",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: suggestions("Young Adults", width, height)
                        )
    age_button2.place(x=480, y=240)

    age_button3 = tk.Button(text="Adults",
                       font="arial 12 bold",
                       height=1,
                       width=12,
                       bg="darksalmon",
                       command=lambda: suggestions("Adults", width, height)
                       )
    age_button3.place(x=145, y=440)

    age_button4 = tk.Button(text="Seniors",
                          font="arial 12 bold",
                          height=1,
                          width=12,
                          bg="darksalmon",
                          command=lambda: suggestions("Seniors", width, height)
                          )
    age_button4.place(x=480, y=440)

# This saves the city filter selection and shows gender page with 3 options for user to choose from.
def create_gender_page(root, width, height, city_selection):
    global user_city_selection

    clear_widgets(root)

    user_city_selection = city_selection
    #calls the corresponding background of page
    place_gender_on_homescreen(root, width, height)

    gender = tk.Label(text="FIND YOUR GENDER GROUP",
                       font="arial 20 ",
                       height="1",
                       width="40",
                       bg="darkslategray",
                       fg="white"
                       )
    gender.place(x=50, y=15)

    second_message = tk.Label(text=" Please choose the gender you identify with.",
                              font="arial 15 italic",
                              bg="darkslategray",
                              fg="white"
                              )
    second_message.place(x=180, y=490)

    female = tk.Button(text="Female",
                         font="arial 12 bold",
                         height=1,
                         width=12,
                         bg="darksalmon",
                         command=lambda: create_age_page(root, width, height, "Female")
                         )
    female.place(x=100, y=355)

    male = tk.Button(text="Male",
                       font="arial 12 bold",
                       height=1,
                       width=12,
                       bg="darksalmon",
                       command=lambda: create_age_page(root, width, height, "Male")
                       )
    male.place(x=310, y=355)

    non_binary = tk.Button(text="Non-Binary",
                     font="arial 12 bold",
                     height=1,
                     width=12,
                     bg="darksalmon",
                     command=lambda: create_age_page(root, width, height, "Non-Binary")
                     )
    non_binary.place(x=520, y=355)

# City page with 4 options to choose from.
# Creates the homepage, places pictures and buttons to choose from.
def create_homepage(root, width, height):
    clear_widgets(root)

    # calls the corresponding background of page
    place_cities_on_homescreen(root, width, height)

    welcome = tk.Label(text="FIND MY CITY",
                       font="arial 20 ",
                       height="1",
                       width="40",
                       bg="darkslategray",
                       fg="white"
                       )
    welcome.place(x=50, y=15)

    second_message = tk.Label(text=" Please choose your city.",
                              font="arial 15 italic",
                              bg="darkslategray",
                              fg="white"
                              )
    second_message.place(x=260, y=490)

    lüneburg = tk.Button(text="Lüneburg",
                         font="arial 12 bold",
                         height=1,
                         width=12,
                         bg="darksalmon",
                         command=lambda: create_gender_page(root, width, height, "Lüneburg")
                         )
    lüneburg.place(x=145, y=240)

    hamburg = tk.Button(text="Hamburg",
                        font="arial 12 bold",
                        height=1,
                        width=12,
                        bg="darksalmon",
                        command=lambda: create_gender_page(root, width, height, "Hamburg")
                        )
    hamburg.place(x=480, y=240)

    berlin = tk.Button(text="Berlin",
                       font="arial 12 bold",
                       height=1,
                       width=12,
                       bg="darksalmon",
                       command=lambda: create_gender_page(root, width, height, "Berlin")
                       )
    berlin.place(x=145, y=440)

    wolfsburg = tk.Button(text="Wolfsburg",
                          font="arial 12 bold",
                          height=1,
                          width=12,
                          bg="darksalmon",
                          command= lambda: create_gender_page(root, width, height, "Wolfsburg")
                          )
    wolfsburg.place(x=480, y=440)

# Creates the first page, the welcoming page that includes the button to start.
def welcome_page(root, width, height):

    place_welcome_page(root, width, height)

    first_box = tk.Label(root,
                         text="WELCOME TO NEW MEET!",
                         font="Arial 23",
                         bg="white",
                         fg="black")
    first_box.place(x=170, y=260)

    sec_box = tk.Label(root,
                       text="The new and easy way to connect!",
                       font="arial 15 italic")
    sec_box.place(x=222, y=220)


    welcome_button = tk.Button(text="Click here to look for groups!",
                                 font='lucida 11 bold',
                                 command= lambda: create_homepage(root, width, height)
                                )
    welcome_button.place(x=260, y=310)


# This calls the very first page that opens the gui and to the user
welcome_page(root, screen_width,screen_height)

# This creates the back buttons function,to go back to the city page and restart.
def back_homepage(root, width, height):
    clear_widgets(root)

    create_homepage(root, screen_width, screen_height)


# this code launches and runs the gui
root.mainloop()