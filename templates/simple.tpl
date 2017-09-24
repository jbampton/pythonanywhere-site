<!DOCTYPE html>
<html>
    <head><title>{{title}}</title></head>
    <body>
        <div>
            <a href="https://www.python.org/" target="_blank">
                <img src="static/img/python-powered.png" alt="This website is powered by Python.">
            </a>
            <a id="top" style="float:right;">{{title}}</a>
        </div>
        <ul>
        % for i, name in enumerate(names):
            <li><a href="{{urls[i]}}" target="_blank">{{name}}</a></li>
        % end
        </ul>
        <span class="typer" id="main" data-words="Beast:Beauty and the Beast...!??!!??:Bring out the Beast...?!??!!?:A powerful Beast...?!?!!!!:Beast is tested daily, and is trained by and even more powerful Beast...!?!?!?!!?!:Beast wants to be the most powerful Beast......??!?!!" data-colors="black" data-delim=":" data-delay="100" data-deleteDelay="1000"></span>
        <span class="cursor" data-owner="main"></span>
        <br>
        <a href="#top">Back to top</a>
        <script src="static/js/typer.js"></script>
    </body>
</html>