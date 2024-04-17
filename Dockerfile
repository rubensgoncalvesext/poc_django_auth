###########
# BUILDER #
###########

# pull official base image
FROM python:3.11.4-slim-buster as build

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    ACCEPT_EULA=Y \
    POETRY_VERSION=1.5.1 \
    # Prevents Python from writing pyc files to disc
    PYTHONDONTWRITEBYTECODE=1 

# Configure user
ENV USERNAME=user_app

# set work directory
ENV HOME=/home/$USERNAME \
    APP_HOME=/home/$USERNAME/web

RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/mediafiles

RUN addgroup --group $USERNAME \
    && adduser --disabled-password --disabled-login --home $APP_HOME --ingroup $USERNAME $USERNAME

RUN chown -R $USERNAME:$USERNAME $HOME

# Configure Virtual Env
ENV PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" 

# Configure PATH 
ENV PATH="$VENV_PATH/bin:$PATH"

RUN apt-get update -y && apt-get install -y curl gnupg2

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get install -y curl gnupg2

# install dependencies
RUN pip install --upgrade pip && pip install poetry==$POETRY_VERSION 
RUN pip install django psycopg2-binary djangorestframework


##############
# STAGE PROD #
##############

# FROM build as prod

# Copy in the venv
# COPY --from=build --chown=$USERNAME $PYSETUP_PATH $PYSETUP_PATH

WORKDIR $APP_HOME