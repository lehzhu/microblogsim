import random

#For users, 1 user = 100k in real life
#Friend means friend who actually uses the app a lot

NUM_THREADS_USERS = 1000
AVG_FRIENDS_PER_THREAD_USER = 10
BASE_CHANCE_OF_USING_THREADS_PER_DAY = 0.5
CHANCE_OF_A_THREAD_FRIEND_JOINING = 0.05

NUM_TWITTER_USERS = 3000
AVG_FRIENDS_PER_TWITTER_USER = 20
BASE_CHANCE_OF_USING_TWITTER_PER_DAY = 0.6
CHANCE_OF_A_TWITTER_FRIEND_JOINING = 0.01

## Helper function to adjust daily usage chance based on friend count
def adjust_daily_chance(base_chance, avg_friends, friend_scaling_factor=0.001):
    return base_chance + (avg_friends * friend_scaling_factor)

# Simulation for 30 Days
print("Starting 30-day Simulation...")

threads_activity = []
twitter_activity = []
total_threads_installs = NUM_THREADS_USERS  # Initialize with starting users
total_twitter_installs = NUM_TWITTER_USERS  # Initialize with starting users

for day in range(1, 31):
    print(f"Running simulation for Day {day}...")

    # Adjusted daily usage chances
    adjusted_chance_threads = adjust_daily_chance(BASE_CHANCE_OF_USING_THREADS_PER_DAY, AVG_FRIENDS_PER_THREAD_USER)
    adjusted_chance_twitter = adjust_daily_chance(BASE_CHANCE_OF_USING_TWITTER_PER_DAY, AVG_FRIENDS_PER_TWITTER_USER)

    # Threads Simulation
    active_threads_users = sum([random.random() < adjusted_chance_threads for _ in range(NUM_THREADS_USERS)])
    new_threads_users = sum([random.random() < CHANCE_OF_A_THREAD_FRIEND_JOINING for _ in range(active_threads_users * AVG_FRIENDS_PER_THREAD_USER)])
    total_threads_installs += new_threads_users
    NUM_THREADS_USERS += new_threads_users
    threads_activity.append((active_threads_users, NUM_THREADS_USERS))

    # Twitter Simulation
    active_twitter_users = sum([random.random() < adjusted_chance_twitter for _ in range(NUM_TWITTER_USERS)])
    new_twitter_users = sum([random.random() < CHANCE_OF_A_TWITTER_FRIEND_JOINING for _ in range(active_twitter_users * AVG_FRIENDS_PER_TWITTER_USER)])
    total_twitter_installs += new_twitter_users
    NUM_TWITTER_USERS += new_twitter_users
    twitter_activity.append((active_twitter_users, NUM_TWITTER_USERS))

# Calculate Retention Rate
# Retention Rate = (Number of Active Users on last day / Total number of installs over 30 days) * 100
threads_retention_rate = (threads_activity[-1][0] / total_threads_installs) * 100
twitter_retention_rate = (twitter_activity[-1][0] / total_twitter_installs) * 100

print("-" * 80)
print("Day | Active Threads Users | Total Threads Users | Active Twitter Users | Total Twitter Users")
print("-" * 80)
for day in range(30):
    print(f"{day + 1:3} | {threads_activity[day][0]:20} | {threads_activity[day][1]:19} | {twitter_activity[day][0]:20} | {twitter_activity[day][1]:18}")

print("-" * 80)
print(f"Threads Retention Rate: {threads_retention_rate:.2f}%")
print(f"Twitter Retention Rate: {twitter_retention_rate:.2f}%")
