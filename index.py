from bottle import route, run, template, error, request, response, get, static_file
import requests
import json


@route('/')
def home():
    user_search = 'https://api.github.com/search/users?q=followers:1..10000000&per_page=100'
    user_searches = [user_search, '%s%s' % (user_search, '&page=2')]
    loads = []
    names = []
    urls = []
    for api_search in user_searches:
        page = requests.get(api_search)
        loads.append(json.loads(page.content))
    for i, each_json in enumerate(loads):
        for j, person in enumerate(each_json['items'], 1):
            #print(person)     #k = i * 100 + j
            names.append(person['login'])
            urls.append(person['html_url'])
    info = {'title': 'Welcome Home!',
            'names': names,
            'urls': urls}
    return template('templates/simple.tpl', info)


@error(404)
def error404(error):
    return 'Nothing to see here, move along.'


# Static Routes
@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")


@get("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return static_file(filepath, root="static/font")


@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="static/img")


@get("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")


run()