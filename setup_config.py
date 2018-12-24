
"""
Automates creation of Media Composer project and ancillary storage path based on the name of the Avid bin containing the final sequence and the template project. Backs up the bin in multiple places and dispatches an email. Minimal user configuration is required.
Igor Ridanovic, igor@hdhead.com
Use at your own risk.
"""

# Version 1.0

#---------User configuration.---------

# Define OS and environment specific paths.
client = 'ClientName'
projBasePath	= '/Users/yourname/Desktop'
templatePath	= '/Users/yourname/scripts/MCprojectsetup/Template/TemplateProj'
mediaBasePath	= '/Volumes/media/'avid Mediafiles'/MXF'
storageBasePath = '/Users/yourname/storage'

# Define custom ancillary storage directories
dirs = ['bin',
		'credits',
		'audio']

# SMTP email setup
receivers	= ['recipient1@yourcompany.com','recipient2@yourcompany.com']
username	= 'yourname@gmail.com'
password	= 'password'
sender		= 'yourname@gmail.com'

#-------End user configuration.--------
