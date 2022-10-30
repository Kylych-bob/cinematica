from django.contrib import admin
from .models import (Category, Genre, Movie, MovieShots, 
                     Actor, Rating, RatingStar, Reviews)


# admin.site.register(Category)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'description', 'poster', 
                    'year', 'country', 'world_premiere', 'budget', 
                    'fees_in_USA', 'fees_in_world', 'category',
                    'url', 'draft')
    list_display_links = ('title', 'tagline', 'description', 'poster', 
                          'year', 'country','world_premiere', 'budget',
                          'fees_in_USA', 'fees_in_world', 'category',
                          'url', 'draft')
    search_fields = ('title', 'tagline', 'description', 'poster', 
                     'year', 'country', 'world_premiere', 'budget',
                     'fees_in_USA', 'fees_in_world', 'category',
                     'url', 'draft')

admin.site.register(Movie, MovieAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description')
    list_display_links = ('name', 'url', 'description')
    search_fields = ('name', 'url', 'description')

admin.site.register(Category, CategoryAdmin)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'image')
    list_display_links = ('name', 'description', 'image')
    search_fields = ('name', 'description', 'image')

admin.site.register(Actor, ActorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')
    list_display_links = ('name', 'description', 'url')
    search_fields = ('name', 'description', 'url')

admin.site.register(Genre, GenreAdmin)


class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'movie')
    list_display_links = ('title', 'description', 'image', 'movie')
    search_fields = ('title', 'description', 'image', 'movie')

admin.site.register(MovieShots, MovieShotsAdmin)

class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_display_links = ('value',)
    search_fields = ('value',)

admin.site.register(RatingStar, RatingStarAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'start', 'movie')
    list_display_links = ('ip', 'start', 'movie')
    search_fields = ('ip', 'start', 'movie')

admin.site.register(Rating, RatingAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'message', 'text', 'movie')
    list_display_links = ('email', 'name', 'message', 'text', 'movie')
    search_fields = ('email', 'name', 'message', 'text', 'movie')

admin.site.register(Reviews, ReviewAdmin)