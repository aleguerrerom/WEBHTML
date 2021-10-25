import re

import soupsieve
from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html><head></head> <body>
 </form>
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

</body></html>'''

class ParsedItemLocator:
    """
    qqqqqqq
    """
    NAME_LOCATOR = 'acticle.product_pod h3 a'
    LINK_LOCATOR = 'acticle.product_pod h3 a'
    PRICE_LOCATOR = 'acticle.product_pod p.price_color'
    RATING_LOCATOR = 'acticle.product_pod h3 p.star-rating'

class ParseItem:
    """
    qweeeeeeeeeee
    """


    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocator.NAME_LOCATOR  # CSS locator
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        print(item_name)

    @property
    def link(self):
        locator = ParsedItemLocator.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']
        print(item_link)

    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        print(matcher.group(0))
        print(float(matcher.group(1)))

    @property
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        print(rating_classes[0])


item = ParseItem(SIMPLE_HTML)
print(item.name)

