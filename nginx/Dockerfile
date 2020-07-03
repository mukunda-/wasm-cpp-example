FROM nginx

# Create a symlink from the nginx public folder to our working directory 
# html folder.
RUN rm -rf /usr/share/nginx/html && ln -s /wd/html /usr/share/nginx/html