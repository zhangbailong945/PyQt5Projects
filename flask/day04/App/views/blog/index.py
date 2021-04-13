from flask import Blueprint,render_template
indexView=Blueprint('indexView',__name__)

@indexView.route('/blog/index')
def main():
   return render_template('/blog/index.html')

@indexView.route('/')
def main2():
   return main()