#Created by Calum McCallion
#Date: 11/03/22 (dd/mm/yy)
#Version: v1.0

from graphics import *
import speedtest
import time

def main():


    win = GraphWin("Speed Test by Calum McCallion", 1000,400)
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(440,30),"W")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(460,30),"E")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(480,30),"L")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(500,30),"C")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(520,30),"O")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(540,30),"M")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(0.5)
    txt = Text(Point(560,30),"E")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(30)
    txt.draw(win)
    txt.setFace('courier')
    time.sleep(3)

    test = speedtest.Speedtest()
    
    txt = Text(Point(500,80),"Loading server list...")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    test.get_servers()

    txt = Text(Point(500,110),"Choosing best server...")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    best = test.get_best_server()

    txt = Text(Point(500,140),f"Found: {best['host']} located in {best['country']}")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    download_result = test.download()

    txt = Text(Point(500,170),"Performing download test...")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')


    txt = Text(Point(500,200),f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    upload_result = test.upload()

    txt = Text(Point(500,230),"Performing upload test...")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    txt = Text(Point(500,260),f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    ping_result = test.results.ping

    txt = Text(Point(500,290),"Performing ping test...")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    txt = Text(Point(500,320),f"Ping: {download_result:.2f} ms")
    txt.setTextColor(color_rgb(0,128,0))
    txt.setSize(20)
    txt.draw(win)
    txt.setFace('courier')

    win.getMouse()
    win.close()

    

main()

