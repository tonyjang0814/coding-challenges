class Solution(object):
    def angleClock(self, hour, minutes):
        min_in_an_hour = 60
        angle_in_an_hour = 30
        temp = float(minutes)/min_in_an_hour
        
        if(hour == 12):
            hour = 0
        
        hour_angle = (hour * angle_in_an_hour) + (temp * angle_in_an_hour)
        min_angle = (float(minutes)/min_in_an_hour) * 360
        
        temp_angle = abs(hour_angle - min_angle)
        a = min(temp_angle,(360-temp_angle))
        return a