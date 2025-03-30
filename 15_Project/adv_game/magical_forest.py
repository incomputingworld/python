# Magical Forest Adventure - Project.

"""
Forest_Path()
    Choice#1 - Narrow path to left

        Choice#1 - Cave option
            collect "rusty key"
        Choice#2 - Continue the path

    Choice#2 - Wide Path in the middle
        Collect "magical amulet"

    Choice#3 - Overgrown path on right
        Use "magical amulet" to cross a hurdle
"""

"""
Treasure_Room()
    If "rusty key" in inventory
        Found treasure - game over**

    else - look for a key
        Choice#1 - Search around temple
            Found treasure - game over**

        Choice#2 - break the door
            Not able to find treasure - game over**

        Choice#3 - Return to forest to look for key
            Guardian options
            Choice#1 - Tell truth about seeking treasure
                Collect "ancient key"
                Found treasure - game over**
            Choice#2 - Make a story
                Not able to find treasure - game over*

            Choice#3 - Offer something from inventory
                If inventory > 0 - Select one of the item from inventory to give
                    Choice#1 - you give "magical amulet"
                        collect "Golden key"
                        Found treasure - game over**
                    else - for any other inventory
                        Not able to find treasure - game over*
                else
                    Not able to find treasure - game over*
"""

"""
River Path()
    Choice#1 - Look for Bridge
    
    Choice#2 - Swim across
        Use "magical amulet" to walk on water

    Choice#3 - Search for another way
        Collect "rowboat"
"""