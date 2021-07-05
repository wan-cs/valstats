from django.shortcuts import render

posts = [
    {
        'author': 'jagon',
        'title': 'VCT Stats Post 1',
        'content': 'Phantom > Vandal',
        'date_posted': 'July 5, 2021'
    },
    {
        'author': '马大牛',
        'title': 'VCT Stats Post 2',
        'content': 'Why I main Reyna',
        'date_posted': 'July 5, 2021'
    },
    {
        'author': 'lance chungus',
        'title': 'VCT Stats Post 3',
        'content': 'How I almost reached plat but got held back by my teammates',
        'date_posted': 'July 5, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'visualize/home.html', context)

def about(request):
    return render(request, 'visualize/about.html', {'title': 'About Us'})
