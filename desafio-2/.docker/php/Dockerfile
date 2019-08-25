FROM php:7.3-fpm

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    unzip \
    git \
    unzip \
    zip && \
    rm -rf /var/lib/apt/lists/*

ADD https://raw.githubusercontent.com/mlocati/docker-php-extension-installer/master/install-php-extensions /usr/local/bin/

RUN \
    # Instalar extensões PHP
    chmod uga+x /usr/local/bin/install-php-extensions && sync && install-php-extensions \
    zip \
    mysqli
    
RUN curl -sS https://getcomposer.org/installer | \
        php -- --install-dir=/usr/bin/ --filename=composer && \
    # Evitar o erro 'cannot create cache directory' quando rodar com usuário 1000
    mkdir -p /.composer/cache && \
    chown 1000:1000 /.composer/cache

# Configurar FPM
RUN \
    echo "pm.max_children = 10" >> /usr/local/etc/php-fpm.d/zz-docker.conf && \
    echo "pm.start_servers=5" >> /usr/local/etc/php-fpm.d/zz-docker.conf && \
    echo "pm.max_spare_servers=6" >> /usr/local/etc/php-fpm.d/zz-docker.conf
    
