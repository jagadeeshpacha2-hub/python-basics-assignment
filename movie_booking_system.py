total_seats = 350
min_age = 12
min_tickets = 1
max_tickets = 15

remaining_seats = total_seats
total_bookings = 0
total_rejections = 0
total_sold_tickets = 0


while remaining_seats>0:
    num_tickets = int(input("Enter number of tickets:"))
    
    if num_tickets==0:
        print("Tickets are sold out! Exiting")
        break
    
    if num_tickets<min_tickets or num_tickets > max_tickets:
        print("Rejected. Tickets must be between 1 and 15")
        total_rejections +=1
        continue
    
    if num_tickets> remaining_seats:
        print(f"Rejected. Only {remaining_seats} seats are available")
        total_rejections +=1
        continue
    
    age_list = input(f"Enter the ages of {num_tickets} persons with comma separated").split(",")
    
    is_valid_booking = True
    for i in range(num_tickets):
        if int(age_list[i])<12:
            is_valid_booking = False
            break
        
    if is_valid_booking:
        total_bookings +=1
        total_sold_tickets += num_tickets
        remaining_seats -= num_tickets
    else:
        total_rejections+=1


print(f" Final Report: Total Bookings: {total_bookings}, Total Tickets Sold: {total_sold_tickets}, Rejected Bookings: {total_rejections}, Remaining Seats: {remaining_seats} ")