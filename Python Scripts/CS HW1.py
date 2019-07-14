# Author: Anthony Cunningham Section A01
def bestVehicleFor(distance, veh1Name, veh1Speed, veh1MPG, veh2Name, veh2Speed, veh2MPG, gasCostPerGallon, nightlyHotelCost): # Need to type vehicle names as strings when calling the function.
    costOfGas1 = (distance/veh1MPG)
    costOfGas2 = (distance/veh2MPG)
    timeInHours1 = (distance/veh1Speed)
    timeInHours2 = (distance/veh2Speed)
    timeInDays1 = ((distance/veh1Speed)*(1/8))
    timeInDays2 = ((distance/veh2Speed)*(1/8))
    nightsInHotel1 = (timeInHours1//8.001)     # Divide by 8.001 since 8 hours exactly doesn't constitute a night in a hotel.
    nightsInHotel2 = (timeInHours2//8.001)     # Same reason as specified above.
    totalCostOfHotel1 = (nightlyHotelCost*nightsInHotel1)
    totalCostOfHotel2 = (nightlyHotelCost*nightsInHotel2)
    costOfTrip1 = costOfGas1 + totalCostOfHotel1
    costOfTrip2 = costOfGas2 + totalCostOfHotel2
    print(str(distance) + ' miles in vehicle ' + veh1Name + ' will take ' + str(timeInDays1) + ' day(s) ' + '(' + str(nightsInHotel1) + ' night(s))' + ' and cost $' + str(costOfTrip1) + '.')
    print(str(distance) + ' miles in vehicle ' + veh2Name + ' will take ' + str(timeInDays2) + ' day(s) ' + '(' + str(nightsInHotel2) + ' night(s))' + ' and cost $' + str(costOfTrip2) + '.')
    if (costOfTrip1 > costOfTrip2):
        print('Using ' + veh2Name + ' will cost less.')
    if (costOfTrip1 < costOfTrip2):
        print('Using ' + veh1Name + ' will cost less.')
    if (costOfTrip1 == costOfTrip2):
        print('Using either ' + veh1Name + ' or ' + veh2Name + ' will cost the same.')
    
