import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    running = True
    while running:
        city = input('First, lets pick a city to work with: [Chicago, Washington, New York City]: ')
        if city == 'chicago':
            print('city: {}'.format(city).lower())
        elif city == 'washington':
            print('city: {}'.format(city).lower())
        elif city == 'new york city':
            print('city: {}'.format(city).lower())
        elif city == 'all':
            city = 'all'
        user = input('Next, would you like to filter by month (m), day (d), or both (b)?: ')
        if user == 'b':
            month = input('What month would you like to see information for?: ')
            if month == 'january':
                print('month: {}'.format(month))
            elif month == 'february':
                print('month: {}'.format(month))
            elif month == 'march':
                print('month: {}'.format(month))
            elif month == 'april':
                print('month: {}'.format(month))
            elif month == 'may':
                print('month: {}'.format(month))
            elif month == 'june':
                print('month: {}'.format(month))
            else:
                print('Please enter a valid month')

            day = input('What day would you like to see info for?: ')
            if day == 'sunday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'monday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'tuesday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'wednesday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'thursday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'friday':
                print('month: {}, day: {}'.format(month, city))
            if day == 'saturday':
                print('month: {}, day: {}'.format(month, city))
            else:
                print('Please enter a valid day')
            return city, month, day

        if user == 'm':
            month = input('What month would you like to see information for?: ')
            day = 'all'
            if month == 'january':
                print('month: {}'.format(month))
            elif month == 'february':
                print('month: {}'.format(month))
            elif month == 'march':
                print('month: {}'.format(month))
            elif month == 'april':
                print('month: {}'.format(month))
            elif month == 'may':
                print('month: {}'.format(month))
            elif month == 'june':
                print('month: {}'.format(month))
            else:
                print('Please enter a valid month')
            return city, month, day
        if user == 'd':
            day = input('What day would you like to see info for?: ')
            month = 'all'
            if day == 'sunday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'monday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'tuesday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'wednesday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'thursday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'friday':
                print('month: {}, day: {}'.format(month, city))
            elif day == 'saturday':
                print('month: {}, day: {}'.format(month, city))
            else:
                print('Please enter a valid day')
            return city, month, day

        print('-'*40)


def load_data(city, month, day):


    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if city != 'all':
        print(df)

    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    df['day_of_week'] = df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    print(df.iloc[0:5])

    while view_data != 'no':
        start_loc += 5
        print(df.iloc[0:5])
        user_continue = input('\nWould you like to see 5 more rows of data?\n')
        while user_continue != 'no':
            start_loc += 5
            print(df.iloc[0:5])


        return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("DATA FRAME: ", df)
    popular_month = df['month'].mode()[0]
    print("most popular month: {}".format(popular_month).lower())

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("most common day: {}".format(common_day).lower())

    # display the most common start hour
    common_start_time = df['Start Time'].mode([0])
    print("common start time: {}".format(common_start_time).lower)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print("Start Time: {}".format(start_time).lower())

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("common_start_station: {}".format(common_start_station).lower())

    # display most commonly used end station
    common_end_station = df['End Station'].mode()
    print("common end station: {}".format(common_end_station).lower())

    # display most frequent combination of start station and end station trip
    most_freq = common_start_station + common_end_station
    print("Most frequent combination of start stations and stop stations: {}".format(most_freq).lower())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df["Trip Duration"]
    print("travel time: {}".format(travel_time).lower())

    # display mean travel time
    mean_travel_time = travel_time.mean()
    print(f"mean travel time: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("user types: {}".format(user_types).lower())

    # Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("gender count: {}".format(gender_count).lower())
    except:
        print('accepted')

    try:
        # Display earliest, most recent, and most common year of birth
        earliest_year = df["Birth Year"].min()
        most_recent_year = df["Birth Year"].max()
        most_common_year = df["Birth Year"].mode()
        print("The earliest birth year is: {}".format(earliest_year).lower())
        print("The most recent birth year is: {}".format(most_recent_year).lower())
        print("The most common birth year is: {}".format(most_common_year).lower())
    except:
        print("No birth year available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()