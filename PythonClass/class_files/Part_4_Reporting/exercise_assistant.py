# coding: utf-8

'''
TODO: Try displaying the result with the congratulations, might make for a nice screenshot
      for students.
'''
import os
import subprocess
path = 'results.txt'

correct_answer_html = "<p style='font-size: 48'>👍</p><span style='font-size: 24'><p>Congratulations, you got it.</p><p>You're an official Python Programmer!</p></span>"
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

def review_world_stores():
	info = {'name': 'Final Exercise: How many stores in each country?'}
	analysis = ''
	results = ''

	analysis = check_results_file()
	if not analysis:
		results = open(path).readlines()
		first = results[0].strip()
		last = results[-1].strip()

		for line in results:
			if line.startswith('Country'):
				analysis = bad_answer_template.format("<p>Oops, you have a country called 'Country' in the list...</p>")

		if not analysis:
			if not first.startswith('Australia'):
				analysis = bad_answer_template.format("<p>Are the results sorted?</p><p>The first entry should start with Australia, but I found: '{}'</p>".format(first))
			elif not first.endswith('22'):
				analysis = bad_answer_template.format("<p>There should be 22 stores in Australia, but I found: '{}'</p>".format(first))
			elif not last.startswith('United States'):
				analysis = bad_answer_template.format("<p>Are the results sorted?</p><p>The last entry should start with United States, but I found: '{}'</p>".format(last))
			elif not last.endswith('272'):
				analysis = bad_answer_template.format("<p>There should be 272 stores in the United States, but I found: '{}'</p>".format(last))
			else:
				analysis = correct_answer_html
		results = open(path).read()

	info['analysis'] = analysis
	info['results'] = results
	display_report(info)

review_world_stores()
