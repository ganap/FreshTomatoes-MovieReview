from django.core.management.base import BaseCommand

from freshTomatoes.api.models import Movie

from django.contrib.auth.models import User

import logging
south_logger=logging.getLogger()
south_logger.setLevel(logging.INFO)

movies = [
            ['Avengers - Age of Ultron', 'http://resizing.flixster.com/s8kIQtOhr36lGPkcUGCVeqVWw9Y=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/01/11190143_ori.jpg', 4.5, 'When Tony Stark jumpstarts a dormant peacekeeping program, things go awry and Earth\'s Mightiest Heroes, including Iron Man, Captain America, Thor, The Incredible Hulk, Black Widow and Hawkeye, are put to the ultimate test as they battle to save the planet from destruction at the hands of the villainous Ultron.'],
            ['Furious 7', 'http://resizing.flixster.com/tBSZ6CjTf-YkvC4o-VC0JFIY-vk=/170x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/18/14/11181482_ori.jpg', 4.0, 'Continuing the global exploits in the unstoppable franchise built on speed, Vin Diesel, Paul Walker and Dwayne Johnson lead the returning cast of Fast & Furious 7. James Wan directs this chapter of the hugely successful series that also welcomes back favorites Michelle Rodriguez, Jordana Brewster, Tyrese Gibson, Chris Ludacris Bridges, Elsa Pataky and Lucas Black. They are joined by international action stars new to the franchise including Jason Statham, Djimon Hounsou, Tony Jaa, Ronda Rousey and Kurt Russell.'],
            ['Tomorrowland', 'http://resizing.flixster.com/dH2TEhqdJ5A6xxV3mQBPZ_1yEac=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/06/11190666_ori.jpg', 3.5, 'From Disney comes two-time Oscar (R) winner Brad Bird\'s riveting, mystery adventure Tomorrowland, starring Academy Award (R) winner George Clooney. Bound by a shared destiny, former boy-genius Frank (Clooney), jaded by disillusionment, and Casey (Britt Robertson), a bright, optimistic teen bursting with scientific curiosity, embark on a danger-filled mission to unearth the secrets of an enigmatic place somewhere in time and space known only as Tomorrowland. What they must do there changes the world-and them-forever. Featuring a screenplay by Lost writer and co-creator Damon Lindelof and Brad Bird, from a story by Lindelof & Bird & Jeff Jensen, Tomorrowland promises to take audiences on a thrill ride of nonstop adventures through new dimensions that have only been dreamed of.(C) Walt Disney'],
            ['Pitch Perfect 2','http://resizing.flixster.com/CSaptdyboc7JUz266OumNJHeAl4=/180x257/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191224_ori.jpg', 3.0, 'Surprise hit Pitch Perfect gets sequelized in this Universal Pictures production once again scripted by Kay Cannon. ~ Jeremy Wheeler, Rovi'],
            ['Mad Max: Fury Road', 'http://resizing.flixster.com/GbDqFVUc_9VBNAnanZVQxlYD0ZM=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg', 4.0, 'Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi'],
            ['Far From The Madding Crowd', 'http://resizing.flixster.com/c8g2_ZQY4dBR7lxc9zWgzQnA01U=/180x267/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/09/11190928_ori.jpg', 4.5, 'Based on the literary classic by Thomas Hardy, FAR FROM THE MADDING CROWD is the story of independent, beautiful and headstrong Bathsheba Everdene (Carey Mulligan), who attracts three very different suitors: Gabriel Oak (Matthias Schoenaerts), a sheep farmer, captivated by her fetching willfulness; Frank Troy (Tom Sturridge), a handsome and reckless Sergeant; and William Boldwood (Michael Sheen), a prosperous and mature bachelor. This timeless story of Bathsheba\'s choices and passions explores the nature of relationships and love - as well as the human ability to overcome hardships through resilience and perseverance. (C) Fox Searchlight']
        ]




class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()

        for i, movie in enumerate(movies):
            name = movie[0]
            image = movie[1]
            rating = movie[2]
            description = movie[3]


            Movie.objects.create(name=name, image_url=image, rating=rating, description=description)
