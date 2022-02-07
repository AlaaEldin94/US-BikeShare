import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please Enter which city u want to investigate(new york city/chicago/washington):\n').lower()
    while city not in CITY_DATA.keys() :
        print("Invalid input / check the spilling \n")
        city = input('Please Enter which city u want to investigate(new york city/chicago/washington):\n').lower()
        
    # get user input for month (all, january, february, ... , june)
    while True :
        month=input("please enter the required month from january to june or type 'all'if u need all the six month:\n").lower()
        months =['january','feburary','march','april','may','june','all']
        if month not in months:
            print('please select from a Determined period/check the spilling ')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input("please enter the required day of the week or type 'all' for the whole week ").lower()
        days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
        if day not in days:
            print('please enter the right day / check the spilling')
        else :
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Loading the choosen city(file)
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month and day from 'Start Time'
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    # filter by month 
    if month != 'all':
        months=['january','feburary','march','april','may','june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by Day 
    if day!= 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # display the most common month
    df['month']=df['Start Time'].dt.month_name()
    m = input('Do u need to ask about the most common month? y/n \n').lower()
    if m != 'n' :
        popular_month = df['month'].mode()[0]
        print('The most common month is : ',popular_month)
    

    # display the most common day of week
    df['day']=df['Start Time'].dt.day_name()
    d = input('Do u need to ask about the most common day of the week ? y/n \n').lower()
    if d != 'n' :
        popular_Day = df['day'].mode()[0]
        print('The most common day is : ',popular_Day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    h = input('Do u need to ask about the most common hour? y/n \n').lower()
    if h != 'n':
        popular_hour = df['hour'].mode()[0]
        print('The most common Hour is :  ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    s_station = input('Do u want to ask about common start station ? y/n').lower()
    if s_station != 'n' :
        common_s_station = df['Start Station'].mode()[0]
        print('The common start station is :  ',common_s_station)
        
    # display most commonly used end station
    e_station = input('Do u want to ask about common end station ? y/n').lower()
    if e_station != 'n':
        common_e_station = df['End Station'].mode()[0]
        print('The common end station is :  ',common_e_station)
        
    # display most frequent combination of start station and end station trip
    combination_station = input('Do u need to ask about combination of start station and end station trip? y/n').lower()
    if combination_station != 'n':
        df['comb_rout']=df['Start Station']+','+df['End Station']
        startend_combination = df['comb_rout'].mode()[0]
        print('The most frequent combinatio of start and end station trip  : ',startend_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = input('Do you need to know total trip duration ? y/n \n').lower()
    if total_duration != 'n':
        total_Trip_duration = df['Trip Duration'].sum()
        print('The total travel time :  ',total_Trip_duration ,'s\n' ,total_Trip_duration/3600,' h')

    # display mean travel time
    mean_time = input('Do u need to know the Average of travel time ? y/n \n').lower()
    if mean_time != 'n':
        Average_time = df['Trip Duration'].mean()
        print('The Average time travel :  ',Average_time , 'Seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users = input("Do you need to know about user type ? y/n \n").lower()
    if users != 'n':
        user_types = df['User Type'].value_counts()
        print('the counts of the user types : \n',user_types)

    # Display counts of gender
    if 'Gender' not in df:
        print('Invalid Gender Data......')
    else :
        mf = input ('Do you need to count the Gender ? y/n').lower()
        if mf != 'n':
            count_gender = df['Gender'].value_counts()
            print('The counts of Gender :  \n',count_gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Invalid Birth Year Data ......')
    else :
        birth_year = input('Do you want to know the statistic of Birth Year ? y/n \n').lower()
        if birth_year!='n':
            most_common = df['Birth Year'].mode()[0]
            print('The most common year :  ',most_common)
            print()
            most_recent = df['Birth Year'].min()
            print('The most recent year : ',most_recent)
            print()
            earliest = df['Birth Year'].max()
            print('The most earlist year of birth : ',earliest)
            print()
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    
    #Displaying the rows of the Data 
    i = 0
    dis_request = input('Do u want to display some raws ? y/n \n').lower()
    if dis_request != 'n':
        while i < df.shape[0]:
            print(df.head(i+5))
            i+=5
            dis_request = input('Do u want to print 5 more rows ? y/n \n').lower()
            if dis_request != 'y':
                 break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Peace....')
            break


if __name__ == "__main__":
	main()
