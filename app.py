from flask import Flask,render_template,request,redirect,url_for
import datetime
import pyperclip
app = Flask(__name__)
entries=[]
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))

        if request.form.get('action1') == 'Noise/Vibration':
            return render_template('tl/noise.html') # do something
        elif  request.form.get('action1') == 'Clothing Issue':
            return render_template('tl/clothing.html') # do something
        elif  request.form.get('action1') == 'Cycle/Operation':
            return render_template('tl/cycle.html') # do something
        elif  request.form.get('action1') == 'Leaking':
            return render_template('tl/leaking.html') # do something
        elif  request.form.get('action1') == 'Error Code':
            return render_template('tl/error.html') # do something'
        elif  request.form.get('action1') == 'Filling':
            return render_template('tl/filling.html') # do something
        elif  request.form.get('action1') == 'Drainage':
            return render_template('tl/drainage.html') # do something
        elif  request.form.get('action2') == 'Dispenser':
            return render_template('tl/dispenser.html') # do something
        elif  request.form.get('action1') == 'Door Issue':
            return render_template('tl/door.html') # do something
        elif  request.form.get('action1') == 'Not Working':
            return render_template('tl/power.html') # do something
        elif  request.form.get('action1') == 'Smell/Odor':
            return render_template('tl/smell.html') # do something
        elif  request.form.get('action1') == 'ThinQ App':           
            return render_template('tl/thinq.html') # do something

        elif  request.form.get('action2') == 'Clothing Issue':
            return render_template('fl/clothing.html') # do something            
        elif  request.form.get('action2') == 'Not Working':
            return render_template('fl/power.html') # do something
        elif  request.form.get('action2') == 'Dispenser':
            return render_template('fl/dispenser.html') # do something
        elif  request.form.get('action2') == 'Door Issue':
            return render_template('fl/door.html') # do something
        elif  request.form.get('action2') == 'Drainage':
            return render_template('fl/drain.html') # do something'
        elif  request.form.get('action2') == 'Cycle/Operation':
            return render_template('fl/cycle.html') # do something
        elif  request.form.get('action2') == 'Leaking':
            return render_template('fl/leak.html') # do something
        elif  request.form.get('action2') == 'Error Code':
            return render_template('fl/error.html') # do something
        elif  request.form.get('action2') == 'Noise/Vibration':
            return render_template('fl/noise.html') # do something
        elif  request.form.get('action2') == 'Smell/Odor':
            return render_template('fl/smell.html') # do something
        elif  request.form.get('action2') == 'Water Level':
            return render_template('fl/water.html') # do something
        elif  request.form.get('action2') == 'ThinQ App':
            return render_template('fl/thinq.html') # do something

        elif  request.form.get('action3') == 'Homepage':
            return render_template('index.html') # do something  
        elif  request.form.get('action3') == 'TLclothinglink1':
            pyperclip.copy('https://www.youtube.com/embed/SITuQXneVvg')
            return render_template('tl/clothing.html')
        elif  request.form.get('action3') == 'TLclothinglink2':
            pyperclip.copy('https://www.youtube.com/embed/3kY0YUZhw2c')
            return render_template('tl/clothing.html')
        elif  request.form.get('action3') == 'TLclothinglink3':
            pyperclip.copy('https://www.youtube.com/embed/-GjX91DxOxg')
            return render_template('tl/clothing.html')
        elif  request.form.get('action3') == 'TLclothinglink4':
            pyperclip.copy('https://www.youtube.com/embed/OZ9HgYKkod8')
            return render_template('tl/clothing.html')       
        elif  request.form.get('action3') == 'TLclothinglink5':
            pyperclip.copy('https://www.youtube.com/embed/j0qKK6ipjNg')
            return render_template('tl/clothing.html')
        elif  request.form.get('action3') == 'TLclothinglink6':
            pyperclip.copy('https://www.youtube.com/embed/fcf1N-JuOAM')
            return render_template('tl/clothing.html') 
        else:
            pass # unknown
    return render_template("index.html", entries=entries)
 

if __name__ == '__main__':
    app.run()