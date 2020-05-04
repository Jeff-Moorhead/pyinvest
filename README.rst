Pyinvest
========

Pyinvest is a simple set of command line tools designed to facilitate interacting with TD Ameritrade's API.
The project provides three scripts: tda_allocations, tdaorders, and tdapositions to allow the user to manage
their TD Ameritrade accounts.

In order to use the scripts, the user must create a configuration file. By default, each script will search
for the config file in $HOME/config/pyinvest.json (note that this project is only officially supported on Linux).
Any functionality provided has not been tested on any other platform. Each script takes a `-c` or `--config``
command line argument that accepts an alternative filepath to the user's config file, but the config file must
be JSON-serialized. The basic layout of the config file is::

   {
	"account_id": "",
	"client_id": "",
	"redirect": "",
	"username": "",
	"allocations": {}
   }
   
The user's account number should be used in the account_id field. The client_id field is the user's individual client ID.
For information on generating a client_id, see this `Reddit post <https://www.reddit.com/r/algotrading/comments/914q22/successful_access_to_td_ameritrade_api/>`_.
You can also review the `TD Ameritrade docs <https://developer.tdameritrade.com/apis>`_, but I personally find them cumbersome
and unclear.

In general the redirect field should be set to http://localhost.

The username field is the user's TD Ameritrade login username.

Finally, the allocations field should be used to provide a desired portfolio allocation, e.g. {"VOO": 0.5, "VWO": 0.3, "BND": 0.2}


Installation
++++++++++++

To install the package, you should clone this repository and run `python3 setup.py --install` from the project root.
The project is currently not hosted on PyPI, but may in the future.


Contact
+++++++

Please feel free to email me at Jeff.Moorhead1@gmail.com if you encounter any issues.
