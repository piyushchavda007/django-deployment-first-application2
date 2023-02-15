from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request): #view-function
	#ss ----> is html-data/code
	ss = '''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
				<hr />
			</center>
		'''
	
	return HttpResponse(ss)

def show(request): 
    ss='''
     <html>
         <head>
            <title>****Welcome****</title>
            <style>
                h1{color: blue;}
                h2{color: blue;}
                h3{color: blue;}
                h4{color: blue;}
                h5{color: blue;}
                h6{color: blue;}
                h1,h3,h5{background-color:yellow;}
                h2,h4,h6{background-color: lightblue;}
                hr{border:double; border-width:7px;}
            </style>
         </head>
     <body>
        <center>
            <h1>Welcome To DJango HTML WebPage</h1>
            <hr color="brown" width="95%"/>
            <h2>Welcome To DJango HTML WebPage</h2>
            <hr color="brown" width="85%"/>
            <h3>Welcome To DJango HTML WebPage</h3>
            <hr color="brown" width="75%"/>
            <h4>Welcome To DJango HTML WebPage</h4>
            <hr color="brown" width="65%"/>
            <h5>Welcome To DJango HTML WebPage</h5>
            <hr color="brown" width="55%"/>
            <h6>Welcome To DJango HTML WebPage</h6>
            <hr color="brown" width="45%"/>
        </center>
     </body>
     </html>
    '''
    return HttpResponse(ss)
def hello(request):
    print("hello/url is request & hello() is executed")
    ss='''
        <html>
            <head>
                <title>Hello WebPage</title>
                <style>
                    h1{color:blue; width:90%;}
                    h2{color:blue; width:80%;}
                    h3{color:blue; width:70%;}
                    h1,h2,h3{background-color:lightblue; border:4px solid brown;}
                </style>
            </head>
            <body>
                <center>
                    <h1>Hello User Hi</h1>
                    <hr color='brown' width='80%'/>
                    <h2>Hello User Welcome to Django-App</h2>
                    <hr color='brown' width='60%'/>
                    <h3>Hello User Have a nice day</h3>
                    <hr color='brown' width='40%'/>
                </center>
        
        </body
        </html>
    '''
    return HttpResponse(ss)


#Write Django application to send server date&time as response-webpage 
import time
def senddatetime(request):
    print("dtime/url is request & senddatetime() is executed")
    ct=time.ctime()
    print("Client Request Data & Time on server :: ",ct)
    ss='''
        <html>
            <head>
                <title>Data-time WebPage</title>
                <style>
                    h1{color:blue;width:90%;}
                    h2{color:green;width:80%;}
                    h3{color:red;width:70%;}
                </style>
                <body>
                    <center>
                        <h1>Welcome to DJango-User..</h1>
                        <hr color='brown' width='80%'/>
                        <h2>Server-Data & Time..</h2>
                        <hr color='brown' width='70%'/>
                        <h3> ''',ct,''' </h3>
                        <hr color='brown' width='60%'/>
                    </center>
                </body>
            </head>
        </html>
    '''
    return HttpResponse(ss)
def demo(request):
    print("mulitple-Request-URLS same response")
    htmldata='''
    <center>
        <h1>Welcome Demo User...!</h1>
        <hr/>
        <h2>This is Same-Output for diff-mulitple-Request-URLS...!</h2>
        <hr/>
        <h3>Have a Great Day...!</h3>
        <hr/>
    </center>
    '''
    return HttpResponse(htmldata)

def homepage(request):
    htmldata='''
    <center>
        <h1>Welcome To Default Home-Page ...!</h1>
        <hr/>
        <h2>You Request Page is Note-Found...</h2>
        <hr/>
        <h3>Plz try other URL or Link ...!</h3>
        <hr/>
    </center>
    '''
    return HttpResponse(htmldata)
    