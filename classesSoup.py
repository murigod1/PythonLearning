import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

class ParsedItemLocators:
    """
    Locaitors for an item in HTML page

    This allows us to easly see what our code will be loking at
    as well as change it quickly if we notice it is now different
    """

    name_locaitor = 'article.product_pod h3 a'
    price_locaitor = 'article.product_pod div.product_price p.price_color'
    rating_locaitor = 'article.product_pod p.star-rating'

class ParsedItem:

    """"
    A class to take in an HTML page (or part of it). and find properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locaitor = ParsedItemLocators.name_locaitor
        item_link = self.soup.select_one(locaitor)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locaitor = ParsedItemLocators.name_locaitor
        item_link = self.soup.select_one(locaitor)
        item_name = item_link.attrs['href']
        return item_name
    
    @property
    def price(self):
        locaitor = ParsedItemLocators.price_locaitor
        item_price = self.soup.select_one(locaitor).string
        parttens = '£([0-9]+\.[0-9]+)'
        matcher = re.search(parttens, item_price)
        # print(matcher.group(0)) #£51.77
        return float(matcher.group(1)) #51.77

    @property
    def rating(self):
        locaitor = 'article.product_pod p.star-rating'
        item_link = self.soup.select_one(locaitor)
        item_name = item_link.attrs['class']
        rating_classes = [r for r in item_name if r != 'star-rating']
        # rating_classes = filter(lambda x: x != 'star-rating', item_name)
        return rating_classes[0]

item = ParsedItem(ITEM_HTML)
print(item.rating)