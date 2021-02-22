# by Kami Bigdely
# Consolidate conditional expressions
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)


def is_missing_an_ingredient(ingredients):
    return 'cucumber' in ingredients and 'tomato' in ingredients and 'onion' in ingredients and 'lemon juice' in ingredients

    
def make_shirazi_salad(ingredients):
    # if 'cucumber' not in ingredients:
    #     print('lacks ingredients.')
    #     return
    # if 'tomato' not in ingredients:
    #     print('lacks ingredients.')
    #     return
    # if 'onion' not in ingredients:
    #     print('lacks ingredients.')
    #     return
    # if 'lemon juice' not in ingredients:
    #     print('lacks ingredients.')
    #     return

    if is_missing_an_ingredient(ingredients) == False:
        print('lacks ingredients.')
        return

    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['tomato', 'lemon juice', 'onion'])
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])