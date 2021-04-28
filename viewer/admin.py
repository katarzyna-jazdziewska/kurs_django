from django.contrib.admin import ModelAdmin, site

from viewer.models import Genre, Movie


class MovieAdmin(ModelAdmin):

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description='')

    @staticmethod
    def set_rating_to_one(modeladmin, request, queryset):
        # print(request.user)
        # print(modeladmin)
        queryset.update(rating=1)

    ordering = ['-genre__name', 'title']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 5
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description', 'set_rating_to_one']

    # fieldsets = [
    #     ('Main info', {'fields': ['title', 'created'],
    #                    'description': 'It is main information about movie.'
    #                    }),
    #     (
    #         'External Information',
    #         {
    #             'fields': ['genre', 'released'],
    #             'description': (
    #                 'These fields are going to be filled with data parsed from external databases.'
    #             )
    #         }
    #     ),
    #     (
    #         'User Information',
    #         {
    #             'fields': ['rating', 'description'],
    #             'description': (
    #                 'These fields are intended to be filled by our users.'
    #             )
    #         }
    #     )
    # ]
    # readonly_fields = ['created'] # można tu dopisać 'description' i wtedy nie będzie można edytować opisu


site.register(Genre)
site.register(Movie, MovieAdmin)
