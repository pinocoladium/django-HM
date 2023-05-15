from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def calc_recipes_omlet(request):
    servings = int(request.GET.get('serving', 1))
    context = {
        'recipe': {ing: am * servings for ing, am in DATA['omlet'].items()}
    }
    return render(request, 'calculator/index.html', context)

def calc_recipes_pasta(request):
    servings = int(request.GET.get('serving', 1))
    context = {
        'recipe': {ing: am * servings for ing, am in DATA['pasta'].items()}
    }
    return render(request, 'calculator/index.html', context)

def calc_recipes_buter(request):
    servings = int(request.GET.get('serving', 1))
    context = {
        'recipe': {ing: am * servings for ing, am in DATA['buter'].items()}
    }
    return render(request, 'calculator/index.html', context)