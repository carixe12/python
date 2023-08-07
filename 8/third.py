import copy

initial_site = {
    'html': {
        'head': {
            'title': 'I will buy/sell a cheap phone'
        },
        'body': {
            'h2': 'We have the lowest price on iPhone',
            'div': ' Buy',
            'p': 'Sell '
        }
    }
}

sites = []


num_sites = int(input('How many sites: '))


for i in range(num_sites):
    product_name = input('Enter a product name for the new site: ')
    site = copy.deepcopy(initial_site)
    site['html']['head']['title'] = site['html']['head']['title'].replace('phone', product_name)
    sites.append(site)
    

    print(f"\nSite for {product_name}:")
    for site in sites:
        print(f"\n{site}\n")