import datetime
import random
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from win10toast import ToastNotifier

tip1 = "Did you know drinking a cup of water supports the function of your cells and organs"
tip2 = "Did you know drinking a cup of water regulates body temperature"
tip3 = "Did you know drinking a cup of water keeps your skin healthy"
tip4 = "Did you know drinking a cup of water boosts alertness and supports brain function"
tip5 = "Did you know drinking a cup of water aids in digestion"
tip6 = "Did you know drinking a cup of water makes up about 60% of your body"
tip7 = "Keep a reusable water bottle with you to drink water regularly"
tip8 = "Drinking a glass of water before eating can help you discern whether you are feeling true hunger"
tip9 = "Use a bit of flavor to help you drink more"
tip10 = "Sipping on water consistently throughout the day is another easy way to help you meet your fluid goals"
tip11 = "One simple way to get more water is to eat more foods that are high in water"
tip12 = "A glass of cold water in the morning may help wake you up and boost your alertness"
tip13 = "Drinking water can improve physical performance"
tip14 = "Drinking water can keep your kidneys healthy"
tip15 = "Drinking water can prevent headaches"
tip16 = "Drinking water improves your complexion"
tip17 = "Eat more fruits and vegetables, as food provides 20 percent of your fluid intake"
tip18 = "It's time to take in your next cup of H₂O"

def destroy():
    newWindow1.destroy()


def tip():
    random_tip = [tip1, tip2, tip3, tip4, tip5, tip6, tip7, tip8, tip9, tip10, tip11, tip12, tip13, tip14, tip15, tip16, tip17, tip18]
    tip = random.choice(random_tip)
    return tip

def getInterval():
    hour = int(input("Interval Hours: "))
    minutes = int(input("Interval Minutes: "))
    seconds = int(input("Interval Seconds: "))
    interval = seconds+(minutes*60)+(hour*3600)
    print("Interval is set to", interval,"seconds")
    start()
    return interval

def start():
    start = ToastNotifier()
    start.show_toast("H₂O",
                      "Alert has been enabled!",
                      icon_path="logo.ico",
                      duration=8)
    print("You have been alerted!")
    log()
    return 0


def alert():
    alert = ToastNotifier()
    alert.show_toast("Alert! \nIt's time for your next glass of water",
                      tip(),
                      icon_path="logo.ico",
                      duration=8)
    print("You have been alerted!")
    log()
    return 0


def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"You have been alerted at {now} \n")
    print("The alert has been logged into log.txt")
    return 0


def starttime(interval):
    while True:
        time.sleep(interval)
        alert()

def benifit1():
    newWindow1 = Toplevel(gui)
    newWindow1.title("H₂O - Advantage 1")
    Label(newWindow1, text="1. Prevents constipation", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow1, text="", background="#d4f1f9").pack()
    Label(newWindow1, text="If you do not drink enough water, you are more likely to experience", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="constipation. On the other hand, if you constipated, drinking plain water and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="carbonated water can help ease symptoms. If you are eating balanced foods", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="without taking adequate water, you will regularly suffer constipation. Drinking", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="water regularly also helps to prevent constipation by ensuring unconstrained", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="bowel movements.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow1, text="", background="#d4f1f9").pack()
    Button(newWindow1, text= "Continue",command=benifit2).pack()
    Button(newWindow1, text="Delete this gui", command=newWindow1.destroy).pack()
    newWindow1.state("zoomed")
    newWindow1.configure(bg="#d4f1f9")
    newWindow1.mainloop()

def benifit2():
    newWindow2 = Toplevel(gui)
    newWindow2.title("H₂O - Advantage 2")
    newWindow2.state("zoomed")
    Label(newWindow2, text="2. Aids digestion", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow2, text="", background="#d4f1f9").pack()
    Label(newWindow2, text="Taking water before, during, and after a meal helps your digestive system to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="break down the food you eat more easily. Therefore, if you frequently", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="experience digestive system problems, you should drink water immediately you", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="eat. Consuming too much sodium or fiber without drinking adequate water can", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="cause bloating. Bloating, for instance, can be treated by drinking a lot of water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="or peppermint tea.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow2, text="", background="#d4f1f9").pack()
    Button(newWindow2, text= "Continue",command=benifit3).pack()
    Button(newWindow2, text="Delete this gui", command=newWindow2.destroy).pack()
    newWindow2.configure(bg="#d4f1f9")
    newWindow2.mainloop()

def benifit3():
    newWindow3 = Toplevel(gui)
    newWindow3.title("H₂O - Advantage 3")
    newWindow3.geometry("1280x600")
    newWindow3.state("zoomed")
    Label(newWindow3, text="3. Supports kidneys health", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow3, text="", background="#d4f1f9").pack()
    Label(newWindow3, text="Individuals struggling with kidney stones are increasingly becoming a big", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow3, text="problem in the health industry. More people are becoming victims of the deadly", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow3, text="disease, but you can keep it at bay by drinking water. Water dilutes minerals and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow3, text="salts that can concentrate in the kidneys to become stones.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow3, text="", background="#d4f1f9").pack()
    Button(newWindow3, text= "Continue",command=benifit4).pack()
    Button(newWindow3, text="Delete this gui", command=newWindow3.destroy).pack()
    newWindow3.configure(bg="#d4f1f9")
    newWindow3.mainloop()

def benifit4():
    newWindow4 = Toplevel(gui)
    newWindow4.title("H₂O - Advantage 4")
    newWindow4.geometry("1280x600")
    Label(newWindow4, text="4. Boosts skin health", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow4, text="", background="#d4f1f9").pack()
    Label(newWindow4, text="If you want to look younger, you should drink adequate water. Drinking water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="plumps up your skin cells, minimizing the appearance of wrinkles and fine lines,", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="which keeps you looking younger. Drinking water also keeps your skin glowing", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="by flushing out impurities and toxins that dull your skin from the body. Drinking", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="warm, vitamin c rich lemon water on a daily basis is a perfect remedy that will", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="keep your skin glowing.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow4, text="", background="#d4f1f9").pack()
    Button(newWindow4, text= "Continue",command=benifit5).pack()
    Button(newWindow4, text="Delete this gui", command=newWindow4.destroy).pack()
    newWindow4.configure(bg="#d4f1f9")
    newWindow4.state("zoomed")
    newWindow4.mainloop()

def benifit5():
    newWindow5 = Toplevel(gui)
    newWindow5.title("H₂O - Advantage 5")
    newWindow5.geometry("1280x600")
    Label(newWindow5, text="5. Makes you work out better", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow5, text="", background="#d4f1f9").pack()
    Label(newWindow5, text="Before hitting the gym or starting your home workouts, you should always strive", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="to first consume adequate water. Although most people tend to drink water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="during workout sessions, experts advise that you should take adequate water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="before, during and after workouts. Drinking adequate water before workouts", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="make you workout longer and avoid muscle cramps.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="Although the adequate amount of water that you should drink depends on", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="various factors such as weather, activity level and how much you sweat, you", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="should drink at least two cups of water about two hours before working out and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="five to ten ounces of water every 20 minutes during your workout sessions.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow5, text="", background="#d4f1f9").pack()
    Button(newWindow5, text= "Continue",command=benifit6).pack()
    Button(newWindow5, text="Delete this gui", command=newWindow5.destroy).pack()
    newWindow5.configure(bg="#d4f1f9")
    newWindow5.state("zoomed")
    newWindow5.mainloop()

def benifit6():
    newWindow6 = Toplevel(gui)
    newWindow6.title("H₂O - Advantage 6")
    Label(newWindow6, text="6. Improves mood", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow6, text="", background="#d4f1f9").pack()
    Label(newWindow6, text="If your mood is low, you should consider taking a glass of water. Dehydration", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="triggers stress and thus, drinking water on a regular basis makes you less prone", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="to feeling stressed. It has been proven that cognitive problems, negative mood,", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="fatigue and anger increase when you are dehydrated. To avoid stress and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="improve your mood, you should not wait until you are thirsty to drink water.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="Thirst is a symptom of dehydration.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow6, text="", background="#d4f1f9").pack()
    Button(newWindow6, text= "Continue",command=benifit7).pack()
    Button(newWindow6, text="Delete this gui", command=newWindow6.destroy).pack()
    newWindow6.configure(bg="#d4f1f9")
    newWindow6.state("zoomed")
    newWindow6.mainloop()

def benifit7():
    newWindow7 = Toplevel(gui)
    newWindow7.title("H₂O - Advantage 7")
    newWindow7.state("zoomed")
    Label(newWindow7, text="7. Keeps you energized", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow7, text="", background="#d4f1f9").pack()
    Label(newWindow7, text="With the two-thirds of the human body comprising of water, any form of", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="dehydration negatively affects the functionality of most body organs.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="Dehydration is associated with increased anger, fatigue, and confusion, as well", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="as decreased vigor. You need to drink adequate water for your body organs to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="work properly. Drinking water also helps to maintain healthy blood pressure and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="heart rate.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="Your immune system also needs adequate fluid to produce lymph, which plays", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="an essential role in keeping you healthy. If your body organs are not functioning", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="effectively, you will feel fatigued and weak. Drinking water ensures that your", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="body organs are functioning optimally, which keeps you energized.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow7, text="", background="#d4f1f9").pack()
    Button(newWindow7, text= "Continue",command=benifit8).pack()
    Button(newWindow7, text="Delete this gui", command=newWindow7.destroy).pack()
    newWindow7.configure(bg="#d4f1f9")
    newWindow7.mainloop()

def benifit8():
    newWindow8 = Toplevel(gui)
    newWindow8.title("H₂O - Advantage 8")
    newWindow8.state("zoomed")
    Label(newWindow8, text="8. Helps you lose weight", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow8, text="", background="#d4f1f9").pack()
    Label(newWindow8, text="Drinking water helps your body maintain healthy body weight. In an era where", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="people are highly concerned about their appearance, drinking adequate water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="can help you achieve your dream appearance.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="Drinking cold water helps to raise metabolism as the body must produce more", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="energy to increase temperature, which makes your body burn more calories.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="Drinking water also eliminates the need to take beverages high in sugar that can", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="make you gain weight.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow8, text="", background="#d4f1f9").pack()
    newWindow8.configure(bg="#d4f1f9")
    Button(newWindow8, text= "Continue",command=benifit9).pack()
    Button(newWindow8, text="Delete this gui", command=newWindow8.destroy).pack()
    newWindow8.mainloop()

def benifit9():
    newWindow9 = Toplevel(gui)
    newWindow9.title("H₂O - Advantage 9")
    newWindow9.state("zoomed")
    Label(newWindow9, text="9. Boosts the immune system", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow9, text="", background="#d4f1f9").pack()
    Label(newWindow9, text="The importance of drinking water on your health cannot be better highlighted", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow9, text="by the fact that drinking water helps fight the flu and its symptoms. Water plays", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow9, text="a vital role in boosting the immune system in several ways that include flushing", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow9, text="harmful toxins from your body and transporting oxygen to the body cells,", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow9, text="ensuring proper functioning of the body.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow9, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow9, text= "Continue",command=benifit10).pack()
    Button(newWindow9, text="Delete this gui", command=newWindow9.destroy).pack()
    newWindow9.configure(bg="#d4f1f9")
    newWindow9.mainloop()

def benifit10():
    newWindow10 = Toplevel(gui)
    newWindow10.title("H₂O - Advantage 10")
    newWindow10.state("zoomed")
    Label(newWindow10, text="10. Flushes out toxins", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow10, text="", background="#d4f1f9").pack()
    Label(newWindow10, text="Water plays a critical role in keeping your body healthy and skin attractive. The", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="most noticeable and identified role played by water in the body according to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="scientists is flushing out toxins. Water helps your body get rid of harmful toxins", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="through sweat and urine. And by getting rid of toxins, water helps to keep the", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="kidneys and urinary tract healthy.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="Your body is a fully functioning machine that uses the lung, kidneys, and liver to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="detoxify. Furthermore, after the organs have detoxed the body, they heavily rely", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="on water to get the toxins out of the body. For this reason, you should always", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="ensure that you are drinking adequate water to get rid of toxins from your body", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="fully.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow10, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow10, text= "Continue",command=benifit11).pack()
    Button(newWindow10, text="Delete this gui", command=newWindow10.destroy).pack()
    newWindow10.configure(bg="#d4f1f9")
    newWindow10.mainloop()

def benifit11():
    newWindow11 = Toplevel(gui)
    newWindow11.title("H₂O - Advantage 11")
    newWindow11.state("zoomed")
    Label(newWindow11, text="11. Boosts your brain power", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow11, text="", background="#d4f1f9").pack()
    Label(newWindow11, text="People tend to drink a cup of coffee when they are looking for a mental", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="performance boost. However, what they do not understand is that taking a glass", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="of water is more beneficial to your brain than taking a cup of coffee. With 73-", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="percent of your brain made up of water, drinking water regularly helps you", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="focus, think, concentrate, and stay alert.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="Moreover, studies have shown that being dehydrated by just two-percent", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="affects your performance in tasks that require psychomotor, attention, and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="immediate memory skills. Dehydration negatively affects your brainpower by", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="reducing your cognitive and motor skills, increase your sensitivity to pain,", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="reduce your memory power and affect your mood.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow11, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow11, text= "Continue",command=benifit12).pack()
    Button(newWindow11, text="Delete this gui", command=newWindow11.destroy).pack()
    newWindow11.configure(bg="#d4f1f9")
    newWindow11.mainloop()

def benifit12():
    newWindow12 = Toplevel(gui)
    newWindow12.title("H₂O - Advantage 12")
    newWindow12.state("zoomed")
    Label(newWindow12, text="12. Prevents headaches", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow12, text="", background="#d4f1f9").pack()
    Label(newWindow12, text="Dehydration causes headaches, and this is because of the influence of", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="dehydration on brain function. In other words, water is an essential component", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="in the functionality of your brain. In addition to boosting brainpower, drinking", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="water also helps to prevent and relieve headaches caused by dehydration.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="According to Medical News Today, dehydration headache occurs when your", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="body loses essential fluids affecting brain functionality. When dehydration", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="occurs, the brain loses essential fluids resulting in a temporary shrink. The shrink", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="causes the brain to pull away from the skull causing pain!", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow12, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow12, text= "Continue",command=benifit13).pack()
    Button(newWindow12, text="Delete this gui", command=newWindow12.destroy).pack()
    newWindow12.configure(bg="#d4f1f9")
    newWindow12.mainloop()

def benifit13():
    newWindow13 = Toplevel(gui)
    newWindow13.title("H₂O - Advantage 13")
    newWindow13.state("zoomed")
    Label(newWindow13, text="13. Prevents cramps and sprains", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow13, text="", background="#d4f1f9").pack()
    Label(newWindow13, text="Dehydration is also associated with cramping and can lead to sprains. Water", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow13, text="acts as a natural lubricant for your joints and muscles making them less prone to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow13, text="sprains and injuries. By drinking water, it makes your muscles and joints more", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow13, text="flexible reducing the likeliness of experiencing sprains and injuries.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow13, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow13, text= "Continue",command=benifit14).pack()
    Button(newWindow13, text="Delete this gui", command=newWindow13.destroy).pack()
    newWindow13.configure(bg="#d4f1f9")
    newWindow13.mainloop()

def benifit14():
    newWindow14 = Toplevel(gui)
    newWindow14.title("H₂O - Advantage 14")
    newWindow14.state("zoomed")
    Label(newWindow14, text="14. Regulates body temperature", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow14, text="", background="#d4f1f9").pack()
    Label(newWindow14, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow14, text="Water is essential in regulating your body temperature. When it gets hot, your", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow14, text="body uses sweat to cool down. Drinking water replenishes the lost fluid through", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow14, text="sweat ensuring that you are comfortable in a hot environment.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow14, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow14, text= "Continue",command=benifit15).pack()
    Button(newWindow14, text="Delete this gui", command=newWindow14.destroy).pack()
    newWindow14.configure(bg="#d4f1f9")
    newWindow14.mainloop()

def benifit15():
    newWindow15 = Toplevel(gui)
    newWindow15.title("H₂O - Advantage 15")
    newWindow15.state("zoomed")
    Label(newWindow15, text="15. Prevents bad breath", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow15, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="Surprisingly, and something that most people don’t know is that in addition to", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="the kind of food you eat, bad breath is usually a sign of depriving yourself", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="enough drinking water. Drinking water frequently and after easting significantly", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="aids in washing away oral bacteria and leftover food particles that cause bad", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="breath.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow15, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow15, text= "Continue",command=benifit16).pack()
    Button(newWindow15, text="Delete this gui", command=newWindow15.destroy).pack()
    newWindow15.configure(bg="#d4f1f9")
    newWindow15.mainloop()

def benifit16():
    newWindow16 = Toplevel(gui)
    newWindow16.title("H₂O - Advantage 16")
    newWindow16.state("zoomed")
    Label(newWindow16, text="16. Good for your heart", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow16, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow16, text="Drinking a sufficient amount of water helps to maintain the proper viscosity of", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow16, text="blood and plasma as well as the distribution of fibrinogen thereby ensuring", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow16, text="good heart health.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow16, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow16, text= "Continue",command=benifit17).pack()
    Button(newWindow16, text="Delete this gui", command=newWindow16.destroy).pack()
    newWindow16.configure(bg="#d4f1f9")
    newWindow16.mainloop()

def benifit17():
    newWindow17 = Toplevel(gui)
    newWindow17.title("H₂O - Advantage 17")
    newWindow17.state("zoomed")
    Label(newWindow17, text="17. Ensures efficient transportation of minerals and", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow17, text="nutrients throughout the body", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow17, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow17, text="Without water, it would be impossible for nutrients and minerals to reach all", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow17, text="your cells. The minerals and nutrients dissolve in the water making it possible for", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow17, text="them to reach all your body parts.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow17, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow17, text= "Continue",command=benifit18).pack()
    Button(newWindow17, text="Delete this gui", command=newWindow17.destroy).pack()
    newWindow17.configure(bg="#d4f1f9")
    newWindow17.mainloop()

def benifit18():
    newWindow18 = Toplevel(gui)
    newWindow18.title("H₂O - Advantage 18")
    newWindow18.state("zoomed")
    Label(newWindow18, text="18. It aids in forming saliva and mucus that keeps your", font=("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow18, text="eyes, nose, and mouth moist", font=("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow18, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="Water is a major component of human saliva and mucus. Saliva and mucus play", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="very vital roles in the body by keeping the mouth, eyes, and nose moist thus", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="preventing friction and cell damage. If one gets constantly dehydrated, it can", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="make the body incapable of producing enough saliva and mucus, which can", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="result in cell damage and friction in the eyes, nose, and mouth. Dry mouth and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="itchy eyes, for instance, can be exacerbated by the lack of drinking adequate", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="water on a daily basis.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow18, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow18, text= "Continue",command=benifit19).pack()
    Button(newWindow18, text="Delete this gui", command=newWindow18.destroy).pack()
    newWindow18.configure(bg="#d4f1f9")
    newWindow18.mainloop()

def benifit19():
    newWindow19 = Toplevel(gui)
    newWindow19.title("H₂O - Advantage 19")
    newWindow19.state("zoomed")
    Label(newWindow19, text="19. Helps fight sickness", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow19, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="Drinking adequate water can help fight off major diseases because water helps", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="in keeping various body nutrients and minerals in balance. If you are drinking", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="enough water daily, you are hence less likely to suffer discomforts and illnesses", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="such as constipation, migraines, urinary tract infection, kidney stones, exercise-", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="induced asthma, hypertension, and even diabetes.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow19, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow19, text= "Continue",command=benifit20).pack()
    Button(newWindow19, text="Delete this gui", command=newWindow19.destroy).pack()
    newWindow19.configure(bg="#d4f1f9")
    newWindow19.mainloop()

def benifit20():
    newWindow20 = Toplevel(gui)
    newWindow20.title("H₂O - Advantage 20")
    newWindow20.state("zoomed")
    Label(newWindow20, text="20. Improves oxygen circulation", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(newWindow20, text="", background="#d4f1f9").pack()
    Label(newWindow20, text="To improve the circulation of oxygen in your body, you should always drink", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="water throughout the day. Water as an essential component of your blood and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="helps to transport oxygen to every part of the body. As such, it ensures one is", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="happy, energized, and in good health as oxygen aids in oxidation and", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="metabolism.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="Furthermore, if some parts of your body such as the brain, nerves, or body cells", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="fail to get adequate oxygen, it can lead to serious illnesses or even death.", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="These are just a few advantages of drinking water!", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(newWindow20, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(newWindow20, text= "Delete this gui",command=newWindow20.destroy).pack()
    newWindow20.configure(bg="#d4f1f9")
    newWindow20.mainloop()

def update():
    update = Toplevel(gui)
    update.title("H₂O - Upcoming updates!")
    update.state("zoomed")
    Label(update, text="The upcoming updates that will be in v2 are listed below!", font = ("Arial Black", 28), background="#d4f1f9").pack()
    Label(update, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="Better Logo", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="User preference gui", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="Complete recode on guis to make it look better", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="Automatically returning to the Home gui after completing advantages menu/update menu", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="v2 coming soon!", font=("Arial Black", 16), background="#d4f1f9").pack()
    Label(update, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
    Button(update, text="Delete this gui", command=update.destroy).pack()
    update.configure(bg="#d4f1f9")
    update.mainloop()

def upcomingUpdate():
    messagebox.showinfo("Under development!", "Sorry this is menu is currently under development.")


gui = Tk()
gui.title("H₂O - Home")
gui.state("zoomed")

Label(gui, text="Amazing Health Benefits of Drinking Water", font=("Arial Black", 36), background="#d4f1f9").pack()
Button(gui, text="Continue", command=benifit1).pack()

Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()

Label(gui, text="Advantages of using this app!", font=("Arial Black", 36), background="#d4f1f9").pack()
Button(gui, text="Comming soon!", command=upcomingUpdate).pack()

Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()

Label(gui, text="Upcoming features!", font=("Arial Black", 36), background="#d4f1f9").pack()
Button(gui, text="Continue", command=update).pack()

Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="You will have to close this gui to set the interval time for getting alert", font=("Arial Black", 16), background="#d4f1f9").pack()
Label(gui, text="Project by Akarsh Shyn X-L", font=("Arial Black", 8), background="#d4f1f9").pack()
gui.configure(bg="#d4f1f9")
gui.mainloop()


if __name__ == '__main__':
    interval = getInterval()
    starttime(interval)