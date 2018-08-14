1. in app.py
@app.route('/download-files/')
def return_files_tut():
	try:
		return send_file('./static/pbs/template&instruction.zip', as_attachment=True, attachment_filename='template&instruction.zip')
        #right path is important, using ./
    except Exception as e:
		return str(e)

2. in html
<a href="/download-files/"><button type="button" class="btn btn-primary">Download Template and Introduction</button></a>
