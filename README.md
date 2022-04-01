# MR GREEN JEANS

## What is Mr Green Jeans?

Mr Green Jeans is an add-on for Blender that helps you manage add-ons through a single tab in the side panel, eliminating the need to handle multiple tabs at once.  

## Features

* Once an add-on is registered with the Mr Green Jeans API, a user can access that add-on from the MR GREEN JEANS side panel.
* The add-on API registration is designed to be simple and similar to Blender's built in registration process.
* The example add-on packaged here shows how to use the API and how to design the add-on so that it does not error if MR GREEN JEANS is not installed.
* Recently User Add-ons and Favorites are all managed by the MR GREEN JEANS add-on itself.

## How to use

1. Download this MR GREEN JEANS repository.
2. Optionally use the linux based build.sh file to build both the main add-on and the example code. In Windows, this can be ran from a shell program such as Ubuntu
3. Look at the *green_jeans_template.py* in the example add-on folder which demonstrates how to register an existing add-on using a similar class in your own code.
