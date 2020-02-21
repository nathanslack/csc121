import random
def main():

    def print_intro():
        print("""
        Welcome to the Desert. You must escape.
        """)

        done = False

        miles_traveled = 0
        thirst = 0
        camel_tiredness = 0
        locals_distance = -20
        canteen = 5
    
        while not done:
            print("""
                A. Drink from your canteen.
                B. Ahead moderate speed.
                C. Ahead full speed.
                D. Stop for the night.
                E. Status check.
                Q. Quit.
            """)

            choice = input("What would you like to do? ")


            if choice == 'Quit':
                done = True


            # Status check
            elif choice == 'Status' or choice =='Status check':
                print(f"""
                Miles traveled: {miles_traveled}
                Drinks in canteen: {canteen}
                The natives are {miles_traveled - locals_distance} mile behind you.
                """)


            # Stopping for the night
            elif choice == 'Stop for the night':
                camel_tiredness = 0
                print("""
                The camel is very happy.
                """)
                locals_distance += random.randrange(7,14)


            # Ahead full speed
            elif choice == 'Ahead full speed':
                miles_traveled += random.randrange(10,20)
                print(f"""
                You have traveled {miles_traveled} miles.
                """)
                thirst += 1
                camel_tiredness += random.randrange(1,3)
                locals_distance += random.randrange(7, 14)
                oasis = random.randrange(20)
                if oasis == 2:
                    thirst = 0
                    camel_tiredness = 0
                    canteen = 10
                    print("""
                    You found an oasis!
                    Your canteen has been filled.
                    You camel is no longer tired.
                    """)
                else:
                    print("""
                    You continue onward!
                    You thirst has increased.
                    The natives continue their chase.
                    """)


            # Ahead moderate speed
            elif choice == 'Ahead moderate speed':
                miles_traveled += random.randrange(5, 12)
                print(f"""
                You have traveled {miles_traveled} miles.
                """)
                thirst += 1
                camel_tiredness += 1
                locals_distance += random.randrange(7,14)
                oasis = random.randrange(20)
                if oasis == 2:
                    thirst = 0
                    camel_tiredness = 0
                    canteen = 10
                    print("""
                    You found an oasis!
                    Your canteen has been filled.
                    You camel is no longer tired.
                    """)
                else:
                    print("""
                    You continue onward!
                    You thirst has increased.
                    The natives continue their chase.
                    """)
                    

            # Drink from canteen
            elif choice == 'Drink from your canteen':
                if canteen >= 1:
                    canteen -= 1
                    thirst = 0
                    print("""
                    You took a drink.
                    """)
                else:
                    print("""
                    Your canteen is empty.
                    """)


            elif thirst > 4:
                print("""
                You are thirsty!
                """)


            elif thirst > 6:
                print("""
                You died of thirst!
                """)
                done = True


            elif camel_tiredness > 5:
                print("""
                Your camel is very tired!
                """)


            elif camel_tiredness > 8:
                print("""
                Your camel is dead!
                """)


            elif miles_traveled <= locals_distance:
                print("""
                The locals have caught up to you.
                You are killed!
                """)
                done = True


            elif miles_traveled < 15:
                print("""
                The locals are getting close!
                """)


            elif miles_traveled >= 200:
                print("""
                You did it!
                You have escaped the locals!
                Thanks for playing.
                """)
                done = True


            else:
                print("""
                I don't understand what you just said.
                """)
            

        

    print_intro()

if __name__ == "__main__":
    main()