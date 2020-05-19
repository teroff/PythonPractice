# coding: utf-8

import os
import subprocess
path = 'results.txt'

correct_answer_html = "<p style='font-size: 48'>👍</p><span style='font-size: 24'><p>Congratulations, you got it!</p></span>"
bad_answer_template = "<div style='font-size: 24'><p style = 'font-size: 48'>🤔</p><p>{}</p></div>"

def display_report(info_dict):
	html = open("assets/answer_template.html", "r").read()
	output_path = "assets/answer_result.html"

	if not info_dict['analysis']:
		info_dict['analysis'] = "Hmm not sure what's up...please ask the instructor to check this out!"

	html = html.format(info_dict)

	with open(output_path, "w") as output_file:
		output_file.write(html)

	subprocess.call(["open", output_path])

def check_results_file():
	analysis = ''
	if not os.path.exists(path):
		analysis = bad_answer_template.format("Couldn't find a {} file...".format(path))
	else:
		results = open(path).readlines()
		try:
			first = results[0].strip()
		except:
			analysis = bad_answer_template.format("Nothing in the file when I look at it...did you close() it?")
	return analysis

def review_numbers_total():
	info = {'name': "What's the total of the numbers in numbers.txt?"}
	analysis = ''
	a = 6.25
	results = ''
	b = 9600

	analysis = check_results_file()
	if not analysis:
		results = open(path).readlines()
		total = None
		try:
			total = int(results[0].strip())
		except:
			analysis = bad_answer_template.format("That's not an int...".format(total))

		if not analysis:
			if total == 0:
				analysis = bad_answer_template.format("0 is a good starting point, but it's a bit low to be the answer!")
			elif total < int((a*2) * (b*2)):
				analysis = bad_answer_template.format("{} is still a bit low to be the answer...".format(total))
			elif total > int((a*2) * (b*2)):
				analysis = bad_answer_template.format("Getting there, but {} is actually too high!".format(total))
			else:
				analysis = correct_answer_html
				results = str(total)

	info['analysis'] = analysis
	info['results'] = results
	display_report(info)

review_numbers_total()