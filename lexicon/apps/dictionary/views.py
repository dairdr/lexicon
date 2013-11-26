# -*- encoding: utf-8 -*-
"""Defines all views using Class Base Views."""
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.mail import BadHeaderError
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from smtplib import SMTPException
from forms import ContactForm
from models import Word, FLC, SLC, WordHasSkill
from mixing import CacheMixin
from utils import get_alphabet

class IndexView(CacheMixin, TemplateView):
	"""Represents index page."""
	http_method_names = ['get']
	template_name = 'dictionary/index.html'
	cache_timeout = 60 * 60

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet()})
		return context

class ProjectView(CacheMixin, TemplateView):
	"""Represents Project page."""
	http_method_names = ['get']
	template_name = 'dictionary/project.html'
	cache_timeout = 60 * 60

	def get_context_data(self, **kwargs):
		context = super(ProjectView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet()})
		return context

class ContactView(FormView):
	"""Represents Contact page."""
	template_name = 'dictionary/contact.html'
	form_class = ContactForm
	success_url = 'dictionary:dictionary-thanks'

	def get_context_data(self, **kwargs):
		context = super(ContactView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet()})
		return context

	def form_valid(self, form):
		super(ContactView, self).form_valid(form)
		
		try:
			form.send_form(subject='Mensaje de Words Project')
			pass
		except BadHeaderError as e:
			# redireccionar a una pagina de error
			pass
		except SMTPException as e:
			# redireccionar a una pagina de error
			pass
		return HttpResponseRedirect(reverse(self.success_url))

class ThanksView(CacheMixin, TemplateView):
	"""Represents Thanks page after sent a email."""
	http_method_names = ['get']
	template_name = 'dictionary/thanks.html'
	cache_timeout = 60 * 60

	def get_context_data(self, **kwargs):
		context = super(ThanksView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet()})
		return context

class ResultView(ListView):
	"""Searchs a word and shows the results on screen."""
	template_name = 'dictionary/list.html'
	http_method_names = ['get']
	model = Word

	def get_queryset(self):
		self.word = self.request.GET.get('w', '')
		self.words = []
		try:
			self.words = Word.objects.filter(name=self.word)
		except:
			pass
		return self.words

	def get_context_data(self, **kwargs):
		context = super(ResultView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet(), 'needle':self.word, 'words':self.words})
		return context

class ResultByIndexView(ListView):
	"""Searchs words by first letter and shows the results on screen."""
	template_name = 'dictionary/list.html'
	http_method_names = ['get']
	model = Word

	def get_queryset(self):
		self.letter = self.kwargs['letter']
		self.words = []
		try:
			self.words = Word.objects.filter(Q(name__startswith=self.letter) | Q(name__startswith=self.letter.upper()))
		except:
			pass
		return self.words

	def get_context_data(self, **kwargs):
		context = super(ResultByIndexView, self).get_context_data(**kwargs)
		context.update({'alphabeth':get_alphabet(), 'needle':self.letter, 'words':self.words})
		return context

class WordView(TemplateView):
	"""Searchs words and shows the results on screen."""
	http_method_names = ['get']
	template_name = 'dictionary/result.html'

	def get_context_data(self, **kwargs):
		context = super(WordView, self).get_context_data(**kwargs)
		word = kwargs['word']
		# conseguir los datos de la palabra buscada
		try:
			result = Word.objects.get(id=word)
		except ObjectDoesNotExist as e:
			# show error 403 page, redirect or whatever
			pass
		except MultipleObjectsReturned as e:
			# show error 403 page, redirect or whatever
			pass

		if 'result' in locals():
			context.update({'word': result})
			# traer las otras palabras que estan en la misma categoria
			words = []
			try:
				words = Word.objects.filter(category=result.category)
			except:
				pass
			
			context.update({'words': words})

			# obtener todo lo de primer nivel que tenga la misma categoria de la palabra
			flcs = []
			try:
				flcs = FLC.objects.filter(category=result.category)
			except:
				pass

			f = []
			for flc in flcs:
				# obtener todo lo de segundo nivel que tengan los elementos de primer nivel
				slcs = []
				try:
					slcs = SLC.objects.filter(flc=flc)
				except:
					pass

				s = []
				for slc in slcs:
					# traer todas las caracteristicas y sus valores que esten del segundo nivel
					skills = []
					try:
						skills = WordHasSkill.objects.filter(word=result, skill__slc=slc)
					except:
						pass
					sk = []
					for skill in skills:
						sk.append({'id': skill.skill.id, 'name': skill.skill.name, 'value': skill.value})
					del skills
					s.append({'id': slc.id, 'name': slc.name, 'skill': sk})
				del slcs
				f.append({'id': flc.id, 'name': flc.name, 'slc': s})
			context.update({'f': f})
			del flcs
		context.update({'alphabeth': get_alphabet()})
		return context