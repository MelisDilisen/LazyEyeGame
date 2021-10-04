# LAZY EYE GAME

## INTRODUCTION

This is a project that I’ve done as part of my master’s graduation project “Amblyopia (Lazy Eye) Treatment with Video Games Using Anaglyph 3D Glasses”. This project consists of a space shooting game and aims to act as an auxiliary treatment method to cure amblyopia. Along with the code, all the images used in this game are also painted by me, in GIMP, in bitmap format.

The game is supposed to be played with the use of an Anaglyph 3D glasses, to get the full benefit of the eye treatment. ‘The Lazy Eye Game’, is a medical “serious game”, designed to treat amblyopia condition, by enforcing the player to use his/her weaker eye more actively than the stronger eye. This game achieved this by showing the most dynamic game elements only to the weaker eye. This treatment method is based on the lazy eye treatment literature’s findings that encouraging the weaker eye to act more by showing certain dynamic figures to only weaker eye is an effective method of treatment of lazy eye. ‘The Lazy Eye Game’ replicates this treatment by using an affordable tool, Anaglyph 3D glasses, unlike large chunk of the literature that uses VR headsets. Hence, ‘The Lazy Eye Game’ aspires to create a fun, engaging, and affordable game, while offering medical benefits to its players.

The intended audience of this project can mostly be children suffering from amblyopia as their brain plasticity is still higher and learn things faster, but adults who have lazy eye condition can also be the beneficiaries of this game, as the lazy eye can still be treated at old ages, albeit marginally. Also, since kids in the early childhood would be easily bored with the long and repetitive conventional treatment methods of amblyopia, the game I created would offer them a fun alternative, that would be able to capture attention for an extended duration of time.

## METHODS

The lazy eye treatment generally consists of conventional methods that proved successful, such as cover therapy, where the patient covers his/her strong eye with a patch, and forces his/her weaker eye to work. This treatment generally yields successful results; however, since the patients of this treatment generally consist of small children, there are some downsides to this treatment method, such as punishment of the strong eye by covering it, and resistance that can come from children for how distressing the treatment method is. In many eye-strengthening exercises, the subjects are expected to cover one of their eye and follow the movement of an object that they hold in their hand while waving it from side to side, or up and down, for extended durations of time. However, since the exercise is long and repetitive, children may not really give this exercise the required time and devotion to show a significant improvement. On this matter, video-game aided methods can be a fun alternative to keep the attention of the young children, and maintain the treatment.
After an extensive investigation on the literature, I concluded that the patients need a method where they do not cover their eye to avoid a punishing method. This project is based on these existing solutions and assumptions in the literature, where they force the weaker eye to work more, by projecting the weaker eye more dynamic images with more stimulus, while presenting the strong eye still images. However, without the tools, such as VR headset that can easily create disparity in vision between two eyes, it is challenging to project two different images to different eye. For that reason, I chose to use anaglyph glasses as it filters out different visuals in each eye, depending on their color. To create that disparity, the game of this project offers two options to the player. In the ‘Options’ part of the game, the player is asked to select the part of his/her eye that is weaker: right or left. According to the answer, the enemies, which are the most dynamic parts of the game, is given a certain color: blue (RGB : 0,0,255) or red (RGB : 255,0,0). The red and blue filters block the opposite color. This way, only the weaker eye sees the enemies, which are quite dynamic components of the game; while the strong eye is only presented with an un-distracting background and the player image. In the meantime, the most part of the user interface and menu are aimed to be visible to both eyes.
As a result, the player of the game is encouraged to use his/her weaker eye; in addition to also being able to see his/her current scores compared with his/her previous scores to track his/her progress. Overall, the project gives a more entertaining way to exercise for the treatment of lazy eye.

Below are photos from the game, with red enemy option. After the neutral image without the anaglyph glasses on is provided, the photos that taken from each filter of the anaglyph glass is presented, to better see how a person using that glass will view the game.

![View of the game without anaglyph glasses on](/readme_images/withoutGlasses.png)

![View of the game from red filter](/readme_images/redFilter.png)![View of the game from blue filter](/readme_images/blueFilter.png))

Below, there are GIFs that I prepared, showing the gameplay through each filter, with both red and blue enemies.

![View of the game with red enemies without anaglyph glasses on](/readme_images/Animation2.gif)![Red Filter](/readme_images/Animation3.gif)

## IMPLEMENTATION
For the implementation of the code, I used pygame as the main module in Python programming language.
For the most important part of the game, an option menu is created, in a function called “game_selection”. This menu option is called with the visual button function created in the game.

'''Python
def game_selection():

    gameselection = True
    while gameselection:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameselection = False
                pygame.quit()


        game_screen.blit(backgroundmenu, (0,0))
        selectiontext = menu_font2.render('WHICH SIDE OF YOUR EYES IS LAZY?', 1, PINK)
        game_screen.blit(selectiontext, (SCREEN_WIDTH / 2 - selectiontext.get_width() / 2, 255))
        button("LEFT", 250, 350, 300, 65, PURPLE, PINK, red_en)
        button("RIGHT", 250, 425, 300, 65, PURPLE, PINK, blue_en)
        button("<< BACK", 10, 520, 250, 65, PURPLE, PINK, game_intro)
        pygame.display.update()
        clock.tick(FPS)'''

![Option Menu](/readme_images/Options.png)

As can be observed in the code snippet above, the user is asked to select the side of their eye that is lazy: right or left. Then with the button option, they call the appropriate function “red_en” (turn enemies into red color) or “blue_en” (turn enemies into blue color).


As to the game mechanics, every game element has an abstract hitbox. In cases where they collide with other element, they either are assumed to be collided with the function (collision) that looks into enemy and player collusion, or be shot with the function (isShot) that deals with enemy and bullet collusion. As can be observed in below code snippet, the X and Y numbers are fine-tuned according to image’s position’s in the hitbox.

![Collusion Mechanics](/readme_images/Collusion.png)

As to the background, I tried to make as un-distracting background as possible, because that’s what has been suggested in the literature, because the researchers want the patients to just concentrate on the game elements that would be only reflected to the one eye. So, I did not want to have busy textures in the background. However, I did not also want to make the game too dull, by having a pitch-black background. Since this is a space shooting game, I made the design as a side scrolling game, moving vertically. Therefore, I wanted to give an illusion that the spaceship is moving forward in space. To do that, I created an 800x1200 pixel background image, for a display screen of 800x600. As shown below in the code, I put two images back-to-back. So that when the window scrolls, it will give the illusion that the spaceship is moving.

![Scroller](/readme_images/Animation.gif)

## USER REQUIREMENTS
As mentioned in the introduction section, the intended audience was described mainly as young children, although a wider age-group of audience can use the game. The age group in which such eye treatments are mostly exercised at, children does not yet usually obtain the reading and writing skills. For that reason, if the child subject is illiterate, the game is recommended to be used under adult’s supervision. Although the game is quite intuitive to understand and play, if the child subject cannot pick the right eye option that has the lazy eye condition, the scores can be misleading in measuring the child’s improvement in the game.

Since the users are generally young, usability aspect of user requirement is important. More specifically, the system should be easy to learn and simple to use. Interface elements such as main menu should be intuitive, easy to understand and navigate. Another usability requirement that the project aimed for is to create an attractive interface, where the screen layout, colors and other interaction components would be appealing to the user. This attractive design should also be done, while maintaining the legibility of the text on the screen.

Moreover, since the aim of this project is to offer lazy eye patients an entertaining way to approach the treatment, the game should be successful in entertaining the player over a long duration of time without getting bored. This is because lazy eye treatment requires long durations of exercises as shown in the literature review part, and the game is not intended for just few days of usage. Therefore, the game should be engaging to maintain the exercises.
Below is the use case diagram of the game.

### USE CASE DIAGRAM

![Use Case Diagram](/readme_images/UseCase.png)
