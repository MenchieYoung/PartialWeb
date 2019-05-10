#**********************************************************************************************
# * Copyright (C) 2015-2016 Sareena Abdul Razak sta2378@columbia.edu
# * 
# * This file is part of New-York-MTA-Subway-Trip-Planner.
# * 
# * New-York-MTA-Subway-Trip-Planner can not be copied and/or distributed without the express
# * permission of Sareena Abdul Razak
# *********************************************************************************************

# Contains all functions needed to get a aws client or resource
# Used in ../dataAnalysis/S3.py and ../dataAnalysis/createAMLModel.py

import boto3


def getCredentials():
	return credentials


def getResource(resourceName,region = "us-east-1"):
	return resource

def getClient(clientName,region = "us-east-1"):
	return client

