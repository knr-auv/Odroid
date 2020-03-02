import Adafruit_PCA9685
class Servo:
    
    def __init__(self,channel):
        self.servofreq = 333
        self.motorfreq = 526
        self.channel=channel
        self.min_angle = 0
        self.max_angle = 165
        self.min_out = 584
        self.max_out = 4093
        self.pwm=Adafruit_PCA9685.PCA9685()
##silniki działają na innej częstotliwości niż serwa więc nie wiem kiedy zmieniać częstotliwość...
                
    def map(self,input,in_min,in_max,out_min,out_max):
        return int((input-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)
    
    def set_servo_frequency(self):
        self.pwm.set_pwm_freq(self.servofreq)
        
    def set_motor_frequency(self):
        self.pwm.set_pwm_freq(self.motorfreq)

    def wpisz_obrot(self):          #spoko do testów
        angle=int(input())
        angle=self.map(angle,self.min_angle,self.max_angle,self.min_out,self.max_out)
        pwm.set_pwm(self.channel,0,angle)
        
    def set_angle(self,angle):      
        self.set_servo_frequency()
        angle=self.map(angle,self.min_angle,self.max_angle,self.min_out,self.max_out)
        pwm.set_pwm(self.channel,0,angle)

    
        

