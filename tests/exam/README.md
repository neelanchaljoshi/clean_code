This was a very fun exercise. I managed to write the logic and tests in about 2.5 hours and the rest I spent trying to refine it a bit.

Followed the naming rules as closely as I could. The classes talk about the responsibility while methods are all verbs.
I tried my best to Keep the Logic as simple as possible (KISS) while still preserving functionality.

As suggested, I tried to segregate the database read logic from the game logic (SRP). The functionality of the Database class is to a minimum by design. I don't know if its a *GOOD* design, but I would like to hear your thoughts.

I tried my best to follow IOSP but it reaalllllyyy difficult to do properly. I am sure this comes with practice, and later I would try to see how better I can improve this code. I would like to refactor the play_game method to allow to properly follow IOSP but this was the best I could manage with 3 working brain cells. I also want to refactor the update_game_state method to remove the dependency on check_if_letter_is_present_in_word, but I do not know how.

The test cases work fine. It took me a while to get a hang of how to use a mocker for this but I'm happy that I know how to use this tool now. 