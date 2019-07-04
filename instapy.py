# ########################## InstaPy ########################################
#
# this is a config script to run InstaPy, a python bot to automate your Insta
# interactions
# Check the install & docs here: https://github.com/timgrossmann/InstaPy
# The numbers of interactions max are changing pretty freq, please use
# carefully or you'll be ban :/
#
# It works pretty well to grow an account pretty quickly tho (70follow/day)
#
# ##########################################################################

# imports
from instapy import InstaPy
from instapy.util import smart_run


# login credentials
insta_username = ''
insta_password = ''

# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # Interact only with real users - not too big nor too small
    session.set_relationship_bounds(enabled=True,
            delimit_by_numbers=True,
            potency_ratio=0.4,
            max_followers=7590,
            min_followers=15,
            min_posts=3)
    
    # Unfollow ppl randomly, based on the log file. 
    session.unfollow_users(amount=490, nonFollowers=True, style="RANDOM",
            unfollow_after=3*60*60, sleep_delay=150)

    #activity
    amount_number=400

    # We want to interact w/ ppl, likes only. I don't want to make fake
    # comments 
    session.set_user_interact(amount=3, randomize=True, percentage=70, media='Photo')

    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=False, percentage=0)
    session.set_do_follow(enabled=False, percentage=0)

    # Follow users based on the tags they use
    session.follow_by_tags(['tag1', 'tag2', 'tag3'], amount=250)
    # Follow the followers of your competitor
    session.follow_user_followers(['user1', 'user2', 'user3'],
             amount=amount_number, randomize=True, interact=True,
             sleep_delay=300)
