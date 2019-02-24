#!/bin/bash

set -e
set -o history -o histexpand

function show_description {
  cat <<EOD
  Usage: docker-clean.sh [OPTION]...

  Help script to stop all of containers and clean up all of docker dummy files.
  No Option arguments are required.
  
  OPTIONS
    -h --help          shows descriptions. cannot be combined with the others.
    -i --image         clean up all of dummy images
    -v --volume        clean up all of dummy volumes
    -c --container     clean up all of dummy containers
  
  USAGE
    You can mix of all of options.
  
  EXAMPLES
    bash docker-clean.sh -h : shows description
    bash docker-clean.sh -c : clean up all of docker containers
    bash docker-clean.sh -civ : clean up all of docker containers, images, and volumes together.
    base docker-clean.sh --container --image --volume: clean up all of docker containers and images, and volumes together.
EOD
}

function remove_containers {
  echo "Cleaning containers..."
  if [[ ! $(docker container prune -f) ]]; then
    echo 'Failed to execute docker container prune -f' >&2
    exit $?
  fi
}

function remove_images {
  echo "Cleaning images..."
  if [[ ! $(docker image prune -f) ]]; then
    echo 'Failed to execute docker image prune -f' >&2
    exit $?
  fi
}

function remove_volumes {
  echo "Cleaning volumes..."
  if [[ ! $(docker volume prune -f) ]]; then
    echo 'Failed to execute docker volume prune -f' >&2
    exit $?
  fi
}

for arg in $@; do
  refined_args=()
  
  if [[ ${arg} =~ ^-[^\-]+ ]]; then
    for index in $(seq 1 ${#arg}); do
      refined_args+=("${arg:$index:1}")
    done
  elif [[ ${arg} =~ ^--.+ ]]; then
    refined_args+=("${arg}")
  else
    echo "No or Wrong Arguments to execute this script" >&2
    exit $?
  fi
  for refined_arg in ${refined_args[@]}; do
    case ${refined_arg} in
      h | --help ) 
        show_description 
        ;;
      c | --container )
        remove_containers
        ;;
      i | --image )
        remove_images
        ;;
      v | --volume ) 
        remove_volumes
        ;;
      * )
        echo "Invalid argument => ${refined_arg}, Do nothing."
    esac
  done
done

echo "END"
