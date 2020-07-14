# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        #12 hrs 360=>1hr 30=>1min 0.5
        h_a = ((hour*60+minutes)*0.5)%360
        #60min 360=>1min 6
        m_a = minutes*6
        if abs(h_a-m_a)<=180 :
            return abs(h_a-m_a) 
        else :
            return 360-abs(h_a-m_a)
        
        
