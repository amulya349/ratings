import requests
import json
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True

names = list()
result = list()
def deriveratings(name):
	l = len(name)
	for i in range(l):
		url = 'http://www.omdbapi.com/?t='+name[i]+'&y=&plot=short&r=json';
		r = requests.get(url)
		if(r.status_code == 200):
			# print r.text
			u = json.loads(r.text)
			if u['Response'] == 'True':
				print(u['Title'] + ': '+u['imdbRating'])
				result.append(u['Title'] + ': '+u['imdbRating'])

def requestdata(url):
	print "Requesting Data !!"
	r = requests.get(url)
	if(r.status_code == 200):
		print "data received!!"
		print 'Processing!'
		y = r.text.split('>')
		s = ''
		for i in range(len(y)-4):
			if(y[i][0].isalnum()):
				temp = str(y[i])
				z = temp.split('<')
				if '/' not in z[0]:
					year = z[0].find('0')
					if(z[0][year-1] == '2'):
						names.append(z[0][0 : year-2])
			# print y[i][0]
		print "data is fed in names list!"
		deriveratings(names)
		print "Finished !!"			


#url = "http://5.9.88.26/Movie/2015/"

@app.route('/')
def indexpage():
    return app.send_static_file('index.html')


@app.route('/ratings', methods = ['GET','POST'])
def getratings():
	if request.method == 'POST':
		print request
		url = request.form['link']
		print 'URL = ', url
		requestdata(url)
		
		return '\n'.join(result)


if __name__ == '__main__':
    app.run()



