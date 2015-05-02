	#Basic Image
FROM ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
RUN apt-get install -y --force-yes nginx
RUN apt-get install -y --force-yes build-essential
RUN apt-get install -y --force-yes python-pip
RUN apt-get install -y --force-yes libblas-dev liblapack-dev gfortran libfreetype6-dev libpng-dev python-dev libxft-dev libpq-dev

#Create the folder where app lives
#Assumes the entirety of my app is there
RUN mkdir /var/www
RUN mkdir /var/www/ask-firehouse
ADD ./requirements.txt /var/www/ask-firehouse/requirements.txt
WORKDIR /var/www/ask-firehouse
RUN pip install -r requirements.txt
ADD ./app /var/www/ask-firehouse/app
ADD ./run.py /var/www/ask-firehouse/run.py
ADD ./config /var/www/ask-firehouse/config

#install Supervisor
RUN apt-get install -y --force-yes supervisor

#Set nginx and uwsgi configs
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /var/www/ask-firehouse/config/nginx.conf /etc/nginx/conf.d
RUN mkdir -p /var/log/uwsgi
RUN mkdir /etc/uwsgi
RUN mkdir /etc/uwsgi/vassals
RUN ln -s /var/www/ask-firehouse/config/uwsgi.ini /etc/uwsgi/vassals
RUN cp /var/www/ask-firehouse/config/uwsgi.conf /etc/init
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/log/uwsgi
RUN chown -R www-data:www-data /var/www
RUN ln -s /var/www/ask-firehouse/config/supervisor-app.conf /etc/supervisor/conf.d/
EXPOSE 80	
CMD ["supervisord", "-n"]