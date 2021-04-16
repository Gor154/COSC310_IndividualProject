from flickrapi import FlickrAPI as api


def getimage(text):
    flickpublic = "0f80f78ace54609d87049841dd857685"
    flicksecret = "fdfa6533678fed71"
    flickr = api(flickpublic, flicksecret, format='parsed-json')
    urls = 'url_t,url_s,url_n,url_z,url_c,url_sq,url_q,url_m,url_l,url_o'
    images = flickr.photos.search(text='kitten', per_page=5, extras=urls)
    photos = images['photos']
    from pprint import pprint
    pprint(photos)

if __name__ == '__main__':
    getimage("star")