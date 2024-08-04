current_hour = int(input("Enter the current hour (0-23): "))

if current_hour == 11 or current_hour < 5:
    print("What are you doing up so late?")
elif current_hour < 10:
    print('Good morning!')
elif current_hour < 17:
    print('Good day!')
else:
    print('Good evening!')


