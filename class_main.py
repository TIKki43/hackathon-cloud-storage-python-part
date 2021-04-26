#!/usr/bin/env python3

import os
import zipfile
import tkinter
import os
import subprocess
from tkinter import messagebox
from PyPreviewGenerator.manager import PreviewManager
from tkinter import simpledialog



class Main():

	def create_dir(self, new_dir_name):
		command = "mkdir {0}".format(new_dir_name).split(' ')
		process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



	def create_file(self, new_file_name):
		command = "touch {0}".format(new_file_name).split(' ')
		process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	def insert_to_dir(self, copy_obj, path_to_dir_cp):
		if os.path.isdir(path_to_dir_cp):
			process = subprocess.Popen(['cp', '-r', copy_obj, path_to_dir_cp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			process = subprocess.Popen(['cp', '-n', copy_obj, path_to_dir_cp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	def open_file(self, full_path, ext):
		if ext in ['txt', 'py', 'html', 'css', 'js']:
			subprocess.Popen(["mousepad", full_path], start_new_session = True)
		elif ext == 'pdf':
			subprocess.run(["evince", full_path], start_new_session = True)
		elif ext in ['png', 'jpeg', 'jpg', 'gif']:
			subprocess.run(["ristretto", full_path], start_new_session = True)


	def delete_file(self, path_to_trash, full_path):
		if True:
			process = subprocess.Popen(['rm', full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			trash = subprocess.Popen(['mv', path_to_trash], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	def rename_file(self, old_file, new_file):
		# old_file=path to dir + name of old fl, new_file=path to dir + name of new fl
		process = subprocess.Popen(['mv', old_file, new_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	def delete_dir(self, full_path):
		process = subprocess.Popen(['rm', '-rf', full_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	def rename_dir(self, old_dir, new_dir):
		# old_dir=path to dir + old name, new_file=path to dir + new name
		process = subprocess.Popen(['mv', old_dir, new_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


	def archiving(self, path_to_file, path_to_dir):
		fantasy_zip = zipfile.ZipFile(path_to_file, 'w')
		for folder, subfolders, files in os.walk(path_to_dir):
			for file in files:
				if file:
					fantasy_zip.write(os.path.join(folder, file),
									  os.path.relpath(os.path.join(folder, file), path_to_dir),
									  compress_type=zipfile.ZIP_DEFLATED)
		fantasy_zip.close()

	def unzip(self, path_to_dir, path_to_file):
		fantasy_zip = zipfile.ZipFile(path_to_file)
		fantasy_zip.extractall(path_to_dir)
		fantasy_zip.close()

	def get_preview_path(self, path_to, save_dir):
		manager = PreviewManager(save_dir)
		path_to_preview = manager.get_jpeg_preview(path_to)
		return path_to_preview


	def path_to(self, path_to_dir):
		for obj in os.listdir(path_to_dir):
			yield obj

	def inf_obj(self, path_to, path_review_to):
		dict = {}
		try:
			dict['ext'] = path_to.split('.')[1]
		except:
			dict['ext'] = 'It is a dir'
		dict['size'] = os.path.getsize(path_to)
		path1 = path_to.split('\\')
		try:
			dict['name'] = path1[-1].split('.')[0]
		except:
			dict['name'] = path1[-1]
		dict['preview'] = self.get_preview_path(self, path_review_to)
		dict['user'] = path_to.split('\\')[1]
		dict1 = dict
		dict.clear()
		return dict1