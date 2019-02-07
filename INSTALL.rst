This instruction works for Linux Mint 18.1 (and probably for most Debian-based Linuxes)

Development environment
=======================

#. Install prerequisites::

    apt update
    apt install git

#. Fork `<https://github.com/dmugtasimov/collections-micro-optimizations>`_ repository

#. Clone forked repository (replace <username> with your github account name)::

    git clone git@github.com:<username>/collections-micro-optimizations.git
    cd collections-micro-optimizations

#. Configure git user name and email if you have not done it yet::

    git config user.name 'Firstname Lastname'
    git config user.email 'youremail@youremail_domain.com'

#. Install and configure `pyenv` according to https://github.com/pyenv/pyenv#basic-github-checkout
#. Install Python 3.7.2::

    pyenv install 3.7.2

#. Install `pipenv`::

    pip install --user pipenv==2018.11.26

#. Create virtualenv with all required dependencies::

    pipenv install

#. Switch to virtualenv::

    pipenv shell

#. Install Collections Micro-optimizations in development mode::

    pip install -e .
