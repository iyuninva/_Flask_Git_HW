from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def main():
    with open('file.txt', 'r', encoding = 'UTF-8') as file:
        resultData = list()
        for line in file.readlines():
            resultData.append(tuple(line.split('\n')[0].split(';')))

    return render_template('base.html', data = resultData)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()


# a - режим добавления
# a+ - если такого файла нет то он создается
# w - режим запись (очищает файл перед записью)
# w+ -  
# r - режим считывания






