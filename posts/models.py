from django.contrib.auth.models import User
from django.db import models
import re, random, string, unicodedata 
from django.db.models.signals import pre_save

from categorias.models import Categoria

class Post(models.Model):
  titulo_post = models.CharField(max_length=150, verbose_name='Título post')
  slug = models.SlugField(max_length=150, null=True, blank=True, unique=True)
  categoria_post = models.ForeignKey(Categoria, blank=True, null=True,
                                      on_delete=models.DO_NOTHING, verbose_name='Categoria post')
  autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor do post')
  data_post = models.DateTimeField(auto_now_add=True, verbose_name='Data do post')
  excerto_post = models.CharField(max_length=200, verbose_name='Excerto')
  conteudo_post = models.TextField(verbose_name='Conteúdo do post')
  imagem_post = models.CharField(max_length=255, verbose_name='Link da imagem do post', blank=True, null=True)    
  publicado_post = models.BooleanField(default=False, verbose_name='Publicado')
  posts = models.Manager()

  def __str__(self):
    return self.titulo_post

def pre_salvamento(sender, instance, *args, **kwargs):
  value = instance.titulo_post
  value = remove_acentos(value)

  instance.slug = gerar_slug(value)
  instance.slug = verificar_existentes(instance.slug)

pre_save.connect(pre_salvamento, sender=Post)

def gerar_slug(txt):
  txt = txt.strip() # remove trailing whitespace
  txt = re.sub('\s*-\s*','-', txt, re.UNICODE) # remove spaces before and after dashes
  txt = re.sub('[\s/]', '-', txt, re.UNICODE) # replace remaining spaces with underscores
  txt = re.sub('(\d):(\d)', r'\1-\2', txt, re.UNICODE) # replace colons between numbers with dashes
  txt = re.sub('"', "'", txt, re.UNICODE) # replace double quotes with single quotes
  txt = re.sub(r'[?,.:!@#~`+=$%^&\\*()\[\]{}<>]','',txt, re.UNICODE) # remove some characters altogether
  return txt.lower()

def verificar_existentes(slug):
  verificador = Post.posts.filter(slug=slug)
  if verificador:
    randstr = random_string_generator(size=4)
    new_slug = f"{slug}-{randstr}"
    return new_slug

  return slug

def remove_acentos(input_str):
  nfkd_form = unicodedata.normalize('NFKD', input_str)
  return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))