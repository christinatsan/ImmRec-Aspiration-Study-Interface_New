from flask import Flask, flash, redirect, render_template, request, session, abort, Response, jsonify, url_for
import json
#from flask.ext.session import Session
from forms import LoginForm
import flask_login
import flask
from gensim.models import  Word2Vec
from gensim.models import KeyedVectors

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'super secret string'  # Change this!

levelNews_1 = ['Fintech','Technology','Travel','Entrepreneurship','Self','Management','Media','Personal','Education','Politics','Love','Health','World','Entertainment','Sports','Creative','Marketing','Design','Social','Writing']
firstLevelPod = ['Poetry','Poem', 'Life', 'Music', 'Sports', 'Writing', 'Books', 'Politics', 'Christianity', 'Love', 'Education', 'Health', 'Movies', 'Startup', 'Humor', 'Television', 'Food', 'Entrepreneurship', 'Photography', 'Art', 'Media', 'Business', 'Travel','Gaming','Comics']

newsChosenTags1 = []
newsChosenTags2 = []
newsChosenTags3 = []
newsChosenTags4 = []
newsChosenTags5 = []

podChosenTags1 = []
podChosenTags2 = []
podChosenTags3 = []
podChosenTags4 = []
podChosenTags5 = []



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect(url_for('eligibilityques'))

@app.route('/eligibility', methods=['POST'])
def eligibility():
	session['does_listen_podcast'] = request.form['podcast_or_radio']
	session['does_read_news'] = request.form['medium_news']	
	return redirect(url_for('categories_pod'))


@app.route('/eligibilityques')
def eligibilityques():
	return render_template('eligibility_questions.html')




@app.route("/categories_pod")
def categories_pod():

	return render_template('categories_pod.html',categories = firstLevelPod)



@app.route("/categories_news")
def categories_news():

	return render_template('categories_news.html',categories = levelNews_1)


@app.route("/categories2_pod")
def categories2_pod():

	word_vectors = KeyedVectors.load("pod-word-vectors")
	nearest_tags = word_vectors.most_similar(podChosenTags1,topn=25)

	tagList = [i[0] for i in nearest_tags]


	return render_template('categories2_pod.html',categories = tagList)

@app.route("/categories2_news")
def categories2_news():


	word_vectors = KeyedVectors.load("news-word-vectors")
	nearest_tags = word_vectors.most_similar(newsChosenTags1,topn=25)

	tagList = [i[0] for i in nearest_tags]


	return render_template('categories2_news.html',categories = tagList)

@app.route("/categories3_pod")
def categories3_pod():

	word_vectors = KeyedVectors.load("pod-word-vectors")
	nearest_tags = word_vectors.most_similar(podChosenTags2,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories3_pod.html',categories = tagList)

@app.route("/categories3_news")
def categories3_news():
	word_vectors = KeyedVectors.load("news-word-vectors")
	nearest_tags = word_vectors.most_similar(newsChosenTags2,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories3_news.html',categories = tagList)

@app.route("/categories4_pod")
def categories4_pod():

	word_vectors = KeyedVectors.load("pod-word-vectors")
	nearest_tags = word_vectors.most_similar(podChosenTags3,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories4_pod.html',categories = tagList)

@app.route("/categories4_news")
def categories4_news():
	word_vectors = KeyedVectors.load("news-word-vectors")
	nearest_tags = word_vectors.most_similar(newsChosenTags3,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories4_news.html',categories = tagList)

@app.route("/categories5_pod")
def categories5_pod():
	word_vectors = KeyedVectors.load("pod-word-vectors")
	nearest_tags = word_vectors.most_similar(podChosenTags4,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories5_pod.html',categories = tagList)

@app.route("/categories5_news")
def categories5_news():
	word_vectors = KeyedVectors.load("news-word-vectors")
	nearest_tags = word_vectors.most_similar(newsChosenTags4,topn=25)

	tagList = [i[0] for i in nearest_tags]

	return render_template('categories5_news.html',categories = tagList)

@app.route("/recommendations_pod")
def recommendations_pod():

	global chosenTags3

	# print(chosenTags3)

	#given tags get articles

	articleList = [
				{
					'tag': 'Tag 1',
					'title': 'News 1',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 2',
					'title':'News 2',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},
				{
					'tag': 'Tag 3',
					'title': 'News 3',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 3',
					'title':'News 4',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 4',
					'title': 'News 5',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 5',
					'title':'News 6',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 6',
					'title':'News 7',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},										
			]	

	session['final-recommendations'] = articleList

	return render_template('recommendations_pod.html',articles = articleList)


@app.route("/recommendations_news")
def recommendations_news():

	# global chosenTags3

	# print(chosenTags3)

	#given tags get articles

	articleList = [
				{
					'tag': 'Tag 1',
					'title': 'News 1',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 2',
					'title':'News 2',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},
				{
					'tag': 'Tag 3',
					'title': 'News 3',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 3',
					'title':'News 4',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 4',
					'title': 'News 5',
					'description':'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'
					

				},
				{
					'tag': 'Tag 5',
					'title':'News 6',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},	
				{
					'tag': 'Tag 6',
					'title':'News 7',
					'description': 'news',
					'imgUrl':'/static/images/news.jpeg',
					'url':'http://www.medium.com',
					'author':'author'

				},										
			]	

	session['final-recommendations'] = articleList

	return render_template('recommendations_news.html',articles = articleList)

@app.route('/postmethodpod1', methods = ['POST'])
def get_post_javascript_data_pod1():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global podChosenTags1

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	podChosenTags1.append(tag)

    # session['tags1'] = chosenTags1
    	
    return jsonify(jsonData)

@app.route('/postmethodpod2', methods = ['POST'])
def get_post_javascript_data_pod2():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global podChosenTags2

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	podChosenTags2.append(tag)

    # session['tags2'] = chosenTags2

    return jsonify(jsonData)


@app.route('/postmethodpod3', methods = ['POST'])
def get_post_javascript_data_pod3():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global podChosenTags3

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	podChosenTags3.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)

@app.route('/postmethodpod4', methods = ['POST'])
def get_post_javascript_data_pod4():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global podChosenTags4

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	podChosenTags4.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)


@app.route('/postmethodpod5', methods = ['POST'])
def get_post_javascript_data_pod5():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global podChosenTags5

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	podChosenTags5.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)




@app.route('/postmethodnews1', methods = ['POST'])
def get_post_javascript_data_news1():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global newsChosenTags1

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	newsChosenTags1.append(tag)

    # session['tags1'] = chosenTags1
    	
    return jsonify(jsonData)

@app.route('/postmethodnews2', methods = ['POST'])
def get_post_javascript_data_news2():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global mewsChosenTags2

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	newsChosenTags2.append(tag)

    # session['tags2'] = chosenTags2

    return jsonify(jsonData)


@app.route('/postmethodnews3', methods = ['POST'])
def get_post_javascript_data_news3():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global newsChosenTags3

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	newsChosenTags3.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)


@app.route('/postmethodnews4', methods = ['POST'])
def get_post_javascript_data_news4():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global newsChosenTags4

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	newsChosenTags4.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)


@app.route('/postmethodnews5', methods = ['POST'])
def get_post_javascript_data_news5():
    jsdata = request.form['javascript_data']
    jsonData = json.loads(jsdata)

    global newsChosenTags5

    for i in range(len(jsonData)):
    	tag = jsonData[str(i)]['item']
    	newsChosenTags5.append(tag)

    # session['tags3'] = chosenTags3
    	
    return jsonify(jsonData)


#TODO: remove this - was just testing
@app.route("/message")
def message():

	return render_template('message.html') 

@app.route("/logout")
def logout():
	# TODO - SAVE ALL SESSION INFO TO JSON - STORE ON SERVER/EMAIL TO ME

	sessionData = {}

	sessionData['name'] = session['name']
	sessionData['email'] = session['email']
	sessionData['chosenTags1'] = session['tags1']
	sessionData['chosenTags2'] = session['tags2']
	#sessionData['chosenTags3'] = session['tags3']
	sessionData['final-recommendations'] = session['final-recommendations']

	fd = open('data' + '/' + 'data.txt', 'a+')
	fd.write(json.dumps(sessionData))
	fd.write('\n')
	fd.close()

	session.clear()	
	return redirect(url_for('home'))




if __name__ == "__main__":
	app.run()