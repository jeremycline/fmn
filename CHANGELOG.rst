fmn.consumer
============

1.0.3
-----

Pull Requests

- (@pypingou)       #84, Miscellaneous fixes to the backend and worker
  https://github.com/fedora-infra/fmn.consumer/pull/84

Commits

- 4dafdfe76 Drop the connection.close() line since we no longer use a connection
  https://github.com/fedora-infra/fmn.consumer/commit/4dafdfe76
- 11ae139e9 Drop debugging prints
  https://github.com/fedora-infra/fmn.consumer/commit/11ae139e9
- d6caee588 Replace logging with print statements
  https://github.com/fedora-infra/fmn.consumer/commit/d6caee588
- 7e9b594ba Replace logging with print statements in the worker
  https://github.com/fedora-infra/fmn.consumer/commit/7e9b594ba
- 5214234d8 If there is an error when processing a message, put it back in the queue and bail
  https://github.com/fedora-infra/fmn.consumer/commit/5214234d8

1.0.2
-----

Pull Requests

- (@pypingou)       #79, Specify the dependency on redis
  https://github.com/fedora-infra/fmn.consumer/pull/79
- (@pypingou)       #80, Adjust the systemd service files to call python2 directly
  https://github.com/fedora-infra/fmn.consumer/pull/80
- (@puiterwijk)     #81, Ignore some very high pressure COPR repos
  https://github.com/fedora-infra/fmn.consumer/pull/81
- (@pypingou)       #82, Open/Close the connection to rabbitmq every time we need one
  https://github.com/fedora-infra/fmn.consumer/pull/82

Commits

- 998726d69 Specify the dependency on redis
  https://github.com/fedora-infra/fmn.consumer/commit/998726d69
- 5e364e8db Adjust the systemd service files to call python2 directly
  https://github.com/fedora-infra/fmn.consumer/commit/5e364e8db
- ee2f4d6d7 Ignore some very high pressure COPR repos
  https://github.com/fedora-infra/fmn.consumer/commit/ee2f4d6d7
- 38f59ab22 Open/Close the connection to rabbitmq every time we need one
  https://github.com/fedora-infra/fmn.consumer/commit/38f59ab22
- f4b498dc4 converting unicode to str so dogpile cache wont complain anymore (#83)
  https://github.com/fedora-infra/fmn.consumer/commit/f4b498dc4

1.0.1
-----

Pull Requests

- (@pypingou)       #78, Fix missing dependencies and files
  https://github.com/fedora-infra/fmn.consumer/pull/78

Commits

- 2b190b54c Include pika in the list of dependencies
  https://github.com/fedora-infra/fmn.consumer/commit/2b190b54c
- 4569803be Include the systemd files in the release tarballs
  https://github.com/fedora-infra/fmn.consumer/commit/4569803be

1.0.0
-----

Pull Requests

- (@ralphbean)      #72, Fix some typoes in this summary construction.
  https://github.com/fedora-infra/fmn.consumer/pull/72
- (@pypingou)       #73, Add a debug backend
  https://github.com/fedora-infra/fmn.consumer/pull/73
- (@sayanchowdhury) #74, Add missing CONFIRMATION_TEMPLATE for DebugBackend
  https://github.com/fedora-infra/fmn.consumer/pull/74
- (@skrzepto)       #75, Adding faq content to the readme
  https://github.com/fedora-infra/fmn.consumer/pull/75
- (@pypingou)       #76, Redesign the architecture of fmn.consumer
  https://github.com/fedora-infra/fmn.consumer/pull/76

Commits

- c7b358838 Fix some typoes in this summary construction.
  https://github.com/fedora-infra/fmn.consumer/commit/c7b358838
- ffeedbaab Access the message property of the QueuedMessage object.
  https://github.com/fedora-infra/fmn.consumer/commit/ffeedbaab
- a326caa24 Add a debug backend
  https://github.com/fedora-infra/fmn.consumer/commit/a326caa24
- 0a79df82b Make fmn.backends.debug to False by default in the config file as well
  https://github.com/fedora-infra/fmn.consumer/commit/0a79df82b
- 46312764a Add missing CONFIRMATION_TEMPLATE for DebugBackend
  https://github.com/fedora-infra/fmn.consumer/commit/46312764a
- 90aca5102 Add a load_preferences method in the util module
  https://github.com/fedora-infra/fmn.consumer/commit/90aca5102
- ffd192f9b Adjust the consumer so that all it does is sending messages to the workers
  https://github.com/fedora-infra/fmn.consumer/commit/ffd192f9b
- a8266c9ff Add the workers which compute who receive which notification and where
  https://github.com/fedora-infra/fmn.consumer/commit/a8266c9ff
- d34fe8c2d Add the backend process receiving messages from the workers and doing the IO
  https://github.com/fedora-infra/fmn.consumer/commit/d34fe8c2d
- 70057bbb6 Fix setting and getting the preferences from the cache
  https://github.com/fedora-infra/fmn.consumer/commit/70057bbb6
- 507c9c686 Drop load_preferences from the util module, not used, no longer needed
  https://github.com/fedora-infra/fmn.consumer/commit/507c9c686
- 5c9f69772 Declare the get_preferences method before calling it
  https://github.com/fedora-infra/fmn.consumer/commit/5c9f69772
- 80e5753fc Document the different part of fmn.consumer now and how to run them
  https://github.com/fedora-infra/fmn.consumer/commit/80e5753fc
- 0eca50870 Add a local, customized fasshim
  https://github.com/fedora-infra/fmn.consumer/commit/0eca50870
- 81c812a0f Rework the worker
  https://github.com/fedora-infra/fmn.consumer/commit/81c812a0f
- 360636cb6 Let the consumer inform the workers when someone's preferences have changed
  https://github.com/fedora-infra/fmn.consumer/commit/360636cb6
- cf9ba5563 Update the backend to work with the same principal as the workers
  https://github.com/fedora-infra/fmn.consumer/commit/cf9ba5563
- a9f284f39 Define the backend for the producer
  https://github.com/fedora-infra/fmn.consumer/commit/a9f284f39
- ef3a66180 Fix listening to two exchanges allowing to refresh the prefs when needed
  https://github.com/fedora-infra/fmn.consumer/commit/ef3a66180
- ef6316a11 Fix our local fasshim module
  https://github.com/fedora-infra/fmn.consumer/commit/ef6316a11
- c6291c92e Let the consumer send messages to either the workers or to signal prefs change
  https://github.com/fedora-infra/fmn.consumer/commit/c6291c92e
- ea13f7bf7 Let the backend listen to two exchanges one from the workers one from the consumer
  https://github.com/fedora-infra/fmn.consumer/commit/ea13f7bf7
- b13ff38d7 Adjust the backend
  https://github.com/fedora-infra/fmn.consumer/commit/b13ff38d7
- 75f2b7909 Let's only retrieve active accounts from FAS to speed things up
  https://github.com/fedora-infra/fmn.consumer/commit/75f2b7909
- 8114ae56e Fix sending messages to the backend from the worker
  https://github.com/fedora-infra/fmn.consumer/commit/8114ae56e
- de395699c Fix retrieving user's info by their email
  https://github.com/fedora-infra/fmn.consumer/commit/de395699c
- 3758e16e3 Fix syntax
  https://github.com/fedora-infra/fmn.consumer/commit/3758e16e3
- 6a5d3d2e4 Document the new architecture in the readme of fmn.consumer
  https://github.com/fedora-infra/fmn.consumer/commit/6a5d3d2e4
- 46e7cbda4 Try make the arch diagram narrower
  https://github.com/fedora-infra/fmn.consumer/commit/46e7cbda4
- 222619acf Try make the arch diagram narrower attempt #2
  https://github.com/fedora-infra/fmn.consumer/commit/222619acf
- 1f6235826 Make it clear the backends are sending messages
  https://github.com/fedora-infra/fmn.consumer/commit/1f6235826
- 1f2159f7d Small fix in the arch diagram
  https://github.com/fedora-infra/fmn.consumer/commit/1f2159f7d
- 24fa1561f Move the backend to a twisted reactor instead of what we had
  https://github.com/fedora-infra/fmn.consumer/commit/24fa1561f
- d7d0a61b8 Use the openid from the original message in the new message
  https://github.com/fedora-infra/fmn.consumer/commit/d7d0a61b8
- ab15200a8 Store something is redis even when we find nothing in FAS
  https://github.com/fedora-infra/fmn.consumer/commit/ab15200a8
- 2e4315ea0 Simplify the producers
  https://github.com/fedora-infra/fmn.consumer/commit/2e4315ea0
- 367341c81 Disable the heartbeat to rabbitmq
  https://github.com/fedora-infra/fmn.consumer/commit/367341c81
- 391136259 Drop the producers from the setup.py
  https://github.com/fedora-infra/fmn.consumer/commit/391136259
- 7a8dd8eab Add the producers to the backend
  https://github.com/fedora-infra/fmn.consumer/commit/7a8dd8eab
- da528604c Fix typo, nick is undefined while username isn't
  https://github.com/fedora-infra/fmn.consumer/commit/da528604c
- e5fa31f3e adding faq content to the readme
  https://github.com/fedora-infra/fmn.consumer/commit/e5fa31f3e
- 5f2a80ced Add systemd files to start the workers and the backend
  https://github.com/fedora-infra/fmn.consumer/commit/5f2a80ced
- 881ec55c5 Adjust documentations and instructions based on @puiterwijk's feedback
  https://github.com/fedora-infra/fmn.consumer/commit/881ec55c5
- e1ee451c7 Do not hard-code the year, retrieve it based on the UTC time
  https://github.com/fedora-infra/fmn.consumer/commit/e1ee451c7

0.8.1
-----

Pull Requests

-                   #68, Merge pull request #68 from fedora-infra/feature/selfie
  https://github.com/fedora-infra/fmn.consumer/pull/68
-                   #69, Merge pull request #69 from mattiaverga/develop
  https://github.com/fedora-infra/fmn.consumer/pull/69
-                   #70, Merge pull request #70 from fedora-infra/feature/fail-whale
  https://github.com/fedora-infra/fmn.consumer/pull/70
-                   #71, Merge pull request #71 from mattiaverga/feature/summary
  https://github.com/fedora-infra/fmn.consumer/pull/71

Commits

- c5bb5b24e Typofix.
  https://github.com/fedora-infra/fmn.consumer/commit/c5bb5b24e
- 176fa27e1 Yet another typo.
  https://github.com/fedora-infra/fmn.consumer/commit/176fa27e1
- c63f884e5 Add separator between messages in digest
  https://github.com/fedora-infra/fmn.consumer/commit/c63f884e5
- ffa9b02ec Reduce separator length to 79 cols
  https://github.com/fedora-infra/fmn.consumer/commit/ffa9b02ec
- 03b3dd365 Gracefully handle link-shortening failures.
  https://github.com/fedora-infra/fmn.consumer/commit/03b3dd365
- 0c81dfe5e Add a short summary at the start of the digest
  https://github.com/fedora-infra/fmn.consumer/commit/0c81dfe5e
- 47c7c8159 Merge branch 'develop' into feature/summary
  https://github.com/fedora-infra/fmn.consumer/commit/47c7c8159

0.6.3
-----

Pull Requests

- (@ralphbean)      #66, Add a handy script for debugging message matching.
  https://github.com/fedora-infra/fmn.consumer/pull/66
- (@ralphbean)      #67, Try a few times to connect to bastion.
  https://github.com/fedora-infra/fmn.consumer/pull/67

Commits

- c90be0547 Add a handy script for debugging message matching.
  https://github.com/fedora-infra/fmn.consumer/commit/c90be0547
- 6f1e5263d Try a few times to connect to bastion.
  https://github.com/fedora-infra/fmn.consumer/commit/6f1e5263d
Changelog
=========

0.6.2
-----

- Add Content-Transfer-Encoding header `740740d6e <https://github.com/fedora-infra/fmn.consumer/commit/740740d6e0f46200742c4941bdcaf131da534995>`_
- Remove unneeded header `a13dc037b <https://github.com/fedora-infra/fmn.consumer/commit/a13dc037b89fcc6a1839ea0ec3891131f26a48c5>`_
- Merge pull request #65 from fedora-infra/fix/transfer-encoding `f6b953aea <https://github.com/fedora-infra/fmn.consumer/commit/f6b953aeabb7b474ee5ae4988cab3d87f909953d>`_
- Delete uneeded comments. `4d0ee5bb8 <https://github.com/fedora-infra/fmn.consumer/commit/4d0ee5bb86399451a550be57f5d46f992ae048e3>`_

0.6.1
-----

- Declare encoding for emails in their headers. `25194edb3 <https://github.com/fedora-infra/fmn.consumer/commit/25194edb35476bdbc0090309e25accb63efe896c>`_
- Drop batched messages if disabled. `1f63f6144 <https://github.com/fedora-infra/fmn.consumer/commit/1f63f61446ae59132440961f5c410e1288939f21>`_
- Merge pull request #64 from fedora-infra/feature/drop-batch-if-disabled `aef5f9feb <https://github.com/fedora-infra/fmn.consumer/commit/aef5f9feb6475629a5c73d038f90b1c3525eb992>`_
- Remove the transfer encoding declaration, since we're not doing base64. `89408018a <https://github.com/fedora-infra/fmn.consumer/commit/89408018a05207de381e64b0aad6f0236c3b753f>`_
- Fix typo and protect against KeyError. `f6f9eff3f <https://github.com/fedora-infra/fmn.consumer/commit/f6f9eff3f941ab9bf8d1191bd57df39d9ad3141c>`_
- Merge pull request #63 from fedora-infra/feature/email-encoding `c1268034b <https://github.com/fedora-infra/fmn.consumer/commit/c1268034bf8d108eb62565aa5bfacad1c97a6af1>`_
- 0.6.0 `e8f5e22dd <https://github.com/fedora-infra/fmn.consumer/commit/e8f5e22dd0c48b62d75bf830a7d72279f5e310e0>`_

0.6.0
-----

- add list categories command in irc backend `c18fda1c8 <https://github.com/fedora-infra/fmn.consumer/commit/c18fda1c8bbdfcdd52d7504d2b3d9b4ee0b944fb>`_
- add list rules commands to list all the rules `67402154d <https://github.com/fedora-infra/fmn.consumer/commit/67402154d39cd54667a3985e79c1f76572a6393b>`_
- add command `list preferences` to list all the preferences `dae7d8db3 <https://github.com/fedora-infra/fmn.consumer/commit/dae7d8db39a7304c03a9f0827294df0ed1779a95>`_
- minor cosmetic fixes to the messages sent in IRC `da9430ab8 <https://github.com/fedora-infra/fmn.consumer/commit/da9430ab83decdfe460edf1ef4fc7096d8ebb300>`_
- add functionality to see filter, rule details `f52b7b04c <https://github.com/fedora-infra/fmn.consumer/commit/f52b7b04cfbf1f5f69dc87a870f8e6ac220ecb85>`_
- check if the nick is configured `d42ca7ea5 <https://github.com/fedora-infra/fmn.consumer/commit/d42ca7ea5166728b77bad06cd6a7e6c6ca5940e6>`_
- add bleach to setup `504768bfc <https://github.com/fedora-infra/fmn.consumer/commit/504768bfc13f4d8fd76c8145f44bc3e8e2f7aebd>`_
- add documentation and appropriate help text `cd7fda60d <https://github.com/fedora-infra/fmn.consumer/commit/cd7fda60d4cad12b1991e5a626231441b4c162c2>`_
- PEP8 fixes and fix to catch an exception for get_filter_name `c8fac6813 <https://github.com/fedora-infra/fmn.consumer/commit/c8fac68130505daf2c05093c9b97463377f3e7e3>`_
- close session and fix grammar `56720fff5 <https://github.com/fedora-infra/fmn.consumer/commit/56720fff5d2ee2442decef4c5da0926e800540a3>`_
- Because if they don't have an email, then they don't have an email. `95a6b9bce <https://github.com/fedora-infra/fmn.consumer/commit/95a6b9bce783497d5c1565fd746bbf62450ea5d5>`_
- fix to include filters with multiple words and quotation marks `4a736f671 <https://github.com/fedora-infra/fmn.consumer/commit/4a736f671114264645cd0e2fdd6b6b851f3bf2ea>`_
- Merge pull request #54 from sayanchowdhury/irc-notifications `f75c57181 <https://github.com/fedora-infra/fmn.consumer/commit/f75c57181847b7d049bc8d61675b6ee94d7de079>`_
- Ignore desktop client preferences in the fmn.consumer code. `fcb470d7b <https://github.com/fedora-infra/fmn.consumer/commit/fcb470d7b7c7d40966191a1903b1bba1095b331c>`_
- Merge pull request #61 from fedora-infra/feature/desktop `b49bf2277 <https://github.com/fedora-infra/fmn.consumer/commit/b49bf2277472b83b660088d794db4f489fea98af>`_
- Standardize the streamline=False argument. `c28721f5f <https://github.com/fedora-infra/fmn.consumer/commit/c28721f5f2e04471561d511d0473c556c3b499bf>`_
- Use regular handling when batch contains only one message. `ddda2ce2d <https://github.com/fedora-infra/fmn.consumer/commit/ddda2ce2d44601c3dabbb7a6cfd43bb4bbb472d3>`_
- Merge pull request #62 from fedora-infra/feature/one-is-exceptional `4992f7770 <https://github.com/fedora-infra/fmn.consumer/commit/4992f7770ae8ee08a06285ab9ad2d733c014a122>`_

0.5.2
-----

- Typofix. `75c8b6945 <https://github.com/fedora-infra/fmn.consumer/commit/75c8b6945d4cf3c7114f29ffd12eee3cf3a1fa7b>`_
- Merge pull request #59 from fedora-infra/feature/typofix `ab230258f <https://github.com/fedora-infra/fmn.consumer/commit/ab230258f53ca0bb92cf5a507facc60823677454>`_
- Another typofix. `4cde6763e <https://github.com/fedora-infra/fmn.consumer/commit/4cde6763e8e670873534d23fed887c178eef644d>`_
- A third typofix. `823c18d51 <https://github.com/fedora-infra/fmn.consumer/commit/823c18d51d5a602b8bf5ffe077e9952a7a5f6051>`_
- Use dict interface to bunch. `6c891692c <https://github.com/fedora-infra/fmn.consumer/commit/6c891692c5595f4cf9822bee6b42a33f141af5ed>`_
- The base url has a trailing slash already. `6c1b6a0a5 <https://github.com/fedora-infra/fmn.consumer/commit/6c1b6a0a5c4cc15b693657edbfee0b0ed4315a27>`_
- Merge pull request #60 from fedora-infra/feature/typofix2 `b9dfff68e <https://github.com/fedora-infra/fmn.consumer/commit/b9dfff68e0e1805e96916e7a47eae81ecfd9a666>`_

0.5.1
-----

- Oneshot bugfix. `cf777fe26 <https://github.com/fedora-infra/fmn.consumer/commit/cf777fe26bd38dba03b28e8d08f830066f152d86>`_
- Merge pull request #57 from fedora-infra/feature/oneshot-bugfix `c412a46e4 <https://github.com/fedora-infra/fmn.consumer/commit/c412a46e47f16e12c1d7902a55752473089c2905>`_
- When constructing fake recipient dict, make sure to populate all needed values. `ba1491709 <https://github.com/fedora-infra/fmn.consumer/commit/ba1491709709030c93c2068a9603ebf3820500b9>`_
- Merge pull request #58 from fedora-infra/feature/flesh-out `be328ad72 <https://github.com/fedora-infra/fmn.consumer/commit/be328ad72d7f205b2c1bb0b47b48a0b33b734fa5>`_

0.5.0
-----

- Make the help and confirmation templates for IRC configurable. `700b4da3f <https://github.com/fedora-infra/fmn.consumer/commit/700b4da3fd9f0182394178e1423cf6d8feeef489>`_
- Make the help and confirmation templates for email configurable. `5a6223568 <https://github.com/fedora-infra/fmn.consumer/commit/5a62235682db75a851e2d84d435d070600729e98>`_
- Merge pull request #47 from fedora-infra/feature/configurable-help-message `95b06b47d <https://github.com/fedora-infra/fmn.consumer/commit/95b06b47d0ce33794ef034f44316f26bb78c1e03>`_
- Use a better default email address... `3b38543d3 <https://github.com/fedora-infra/fmn.consumer/commit/3b38543d35bba1a3fa42f571bb33f2bca4972854>`_
- Merge pull request #48 from fedora-infra/feature/better-default-email `173804c4b <https://github.com/fedora-infra/fmn.consumer/commit/173804c4ba87b92cea38e895a512a34a541ab901>`_
- Implement one-shot filters in the consumer `32b701b02 <https://github.com/fedora-infra/fmn.consumer/commit/32b701b0234b145dd418fd642d632563ded90a75>`_
- Improve findability of the hacking document `e6b38542c <https://github.com/fedora-infra/fmn.consumer/commit/e6b38542ca360d32587d8526e17518d8fe18507c>`_
- Merge pull request #49 from fedora-infra/oneshot `02d064d07 <https://github.com/fedora-infra/fmn.consumer/commit/02d064d07ef7b2f73feebd0cd6700a2749efafa9>`_
- Merge pull request #50 from fedora-infra/docs `98f93a3d0 <https://github.com/fedora-infra/fmn.consumer/commit/98f93a3d00165d31f09bc10da94b81373468fd80>`_
- Employ the verbose value to send more or less details in a digest email. `f932a05cf <https://github.com/fedora-infra/fmn.consumer/commit/f932a05cf9a017ba87f7e0501e335ac731185b8b>`_
- Merge pull request #51 from fedora-infra/feature/verbosity `65f9e9bf8 <https://github.com/fedora-infra/fmn.consumer/commit/65f9e9bf8da4a8bd7d4d47986d3b5d644ccbe7bc>`_
- Queued messages won't have this at first. `b97a8c05c <https://github.com/fedora-infra/fmn.consumer/commit/b97a8c05cee141cf30f9c951c8bb486db9c5ee20>`_
- Default to True. `b7c656541 <https://github.com/fedora-infra/fmn.consumer/commit/b7c6565415fd34c0c7880adc55c93c08c6981562>`_
- Move utils to their own file for re-use. `118ce38d1 <https://github.com/fedora-infra/fmn.consumer/commit/118ce38d103c1c14374fa24d0550de09f37db77b>`_
- Make mail handler deal with bad emails. `e5716e65e <https://github.com/fedora-infra/fmn.consumer/commit/e5716e65e657a10ab138fe17db3e5c3b01739d5a>`_
- Only prefix irc messages with topic if we're 'marking up' messages. `a7d71f540 <https://github.com/fedora-infra/fmn.consumer/commit/a7d71f5401ae0b6f9d2fd3cd8d9018e6295cbe07>`_
- Merge pull request #52 from fedora-infra/feature/deal-with-bad-emails `1bafaea91 <https://github.com/fedora-infra/fmn.consumer/commit/1bafaea91505250721b95c7079eee47703f99e13>`_
- Merge pull request #53 from fedora-infra/feature/simpler-irc-format `496b70148 <https://github.com/fedora-infra/fmn.consumer/commit/496b7014845995693992f44459228ab72f1b7bb0>`_
- Only append the "triggered by" link to emails if the user wants it. `53a1a13f3 <https://github.com/fedora-infra/fmn.consumer/commit/53a1a13f30034843089802c55941a15c735ba143>`_
- Merge pull request #55 from fedora-infra/feature/mail-footer `a58b5d736 <https://github.com/fedora-infra/fmn.consumer/commit/a58b5d736ac4ec560d565e70766cb587159b8460>`_
- Manually prepend the subtitle to the longform `27740a6b5 <https://github.com/fedora-infra/fmn.consumer/commit/27740a6b5c618c71948367667e8159816c41d032>`_
- Merge pull request #56 from fedora-infra/feature/de-duplicate-subtitle `6ba39eba0 <https://github.com/fedora-infra/fmn.consumer/commit/6ba39eba022ce8421cb1deccd1da202f252b59fe>`_

0.4.5
-----

- Randomize preference list per-thread. `2aa92ed0d <https://github.com/fedora-infra/fmn.consumer/commit/2aa92ed0dd8004df33b3c6de62b047caa895f96a>`_
- Merge pull request #43 from fedora-infra/feature/randomize `fab6f4dd5 <https://github.com/fedora-infra/fmn.consumer/commit/fab6f4dd54b0cc58546cff8c83eab97cbbbdbb94>`_
- Use the first portion of the hostname here. `79ada97ae <https://github.com/fedora-infra/fmn.consumer/commit/79ada97ae9560ea1ba424c22cef76e52114d883e>`_
- Add a zoo of X-Fedmsg-* headers to email messages. `1b5822dd4 <https://github.com/fedora-infra/fmn.consumer/commit/1b5822dd4079fc714a98d8487c742a39dc8c4f4f>`_
- Merge pull request #45 from fedora-infra/feature/fedmsg-email-headers `025fa1667 <https://github.com/fedora-infra/fmn.consumer/commit/025fa1667304077d22bc59498f236247e52e54d0>`_
- Drop junk suffixes and add some performance debugging. `9f7a1f3aa <https://github.com/fedora-infra/fmn.consumer/commit/9f7a1f3aaab0f43af3a3c9551a62b019499df90b>`_
- Merge pull request #46 from fedora-infra/feature/debugging `89ae2c441 <https://github.com/fedora-infra/fmn.consumer/commit/89ae2c4418d64f95cad9d22cd23df2726a72b0d7>`_
- Also junk. `5d62ff231 <https://github.com/fedora-infra/fmn.consumer/commit/5d62ff231a917dd673379b43621941a900bcf4ed>`_

0.4.4
-----

- Initialize the cache at startup. `e9d5cdcff <https://github.com/fedora-infra/fmn.consumer/commit/e9d5cdcff1f6cc2f1df428466f3e889a37c8ac59>`_
- Only refresh the prefs cache for single users when we can. `b8af37260 <https://github.com/fedora-infra/fmn.consumer/commit/b8af3726026cb9bf3a637abb69a38e9b7cecb3d6>`_
- Merge pull request #42 from fedora-infra/feature/per-person-cache-refresh `34774c5ca <https://github.com/fedora-infra/fmn.consumer/commit/34774c5cac62ec27d5389a1aa4a78701a6d8684f>`_

0.4.3
-----

- Remove extra lines from desc on PyPI `5610bbe15 <https://github.com/fedora-infra/fmn.consumer/commit/5610bbe153b756cc55f68fa031768cf649390bd7>`_
- Remove extra newlines. `021d2d68f <https://github.com/fedora-infra/fmn.consumer/commit/021d2d68fbc0dd7bb407f5ba64ad6e5e219552c0>`_
- Merge pull request #39 from msabramo/remove_extra_lines_from_desc_on_PyPI `d3829e77e <https://github.com/fedora-infra/fmn.consumer/commit/d3829e77e8045d1af9896dabcd7e8b59941a86a9>`_
- Convert Nones to empty strings here. `a58edbf0e <https://github.com/fedora-infra/fmn.consumer/commit/a58edbf0e16095ac730d1038f18d2ccd983e4fe4>`_
- Merge branch 'develop' of github.com:fedora-infra/fmn.consumer into develop `ae5fba089 <https://github.com/fedora-infra/fmn.consumer/commit/ae5fba0891e66e7fde45b85ac6d0652fb0ed2966>`_
- Include anitya messages, which start with org.release-monitoring.* `9e30e4283 <https://github.com/fedora-infra/fmn.consumer/commit/9e30e4283db9633f4ca4987050f7042c3fc0ee87>`_
- Merge pull request #40 from fedora-infra/feature/include-anitya `884e922ad <https://github.com/fedora-infra/fmn.consumer/commit/884e922ad580d4c58067408a31e6ccee26ebbd11>`_

0.4.1
-----

- Add forgotten import. `42f0f0460 <https://github.com/fedora-infra/fmn.consumer/commit/42f0f0460c46a06b54c5c558e59755c1f896d9cf>`_
- Undo tuple arguments to email module. `21e6ba0cf <https://github.com/fedora-infra/fmn.consumer/commit/21e6ba0cf3eb28d5215a5db40e522c61f7cccb7a>`_
- Merge pull request #33 from fedora-infra/feature/further-email-fixes `bf2505232 <https://github.com/fedora-infra/fmn.consumer/commit/bf25052325d6dc1117ee0695177aae466a2850bf>`_
- Make autocreate configurable for staging.  Fixes #34. `02d000ad8 <https://github.com/fedora-infra/fmn.consumer/commit/02d000ad81b121ff82a2988cfc6b2f504ae761e4>`_
- Only create account for sponsee. `be3043ea6 <https://github.com/fedora-infra/fmn.consumer/commit/be3043ea6b6acdfd913f94f294cb96bee26b397d>`_
- Merge pull request #35 from fedora-infra/feature/autocreate `e89f298b1 <https://github.com/fedora-infra/fmn.consumer/commit/e89f298b169243862d8f41cb71f337f1722d6df8>`_
- Merge pull request #36 from fedora-infra/feature/distinguish `40f293182 <https://github.com/fedora-infra/fmn.consumer/commit/40f2931829bdc004291d0b0910f6569b1c3a2b26>`_
- Create new accounts for new fedbadges users. `d6515106a <https://github.com/fedora-infra/fmn.consumer/commit/d6515106a87f7cafe4cc9561f37b484383815e2b>`_
- Merge branch 'feature/distinguish' into develop `16f7ba50c <https://github.com/fedora-infra/fmn.consumer/commit/16f7ba50c8e6b17d112423abb8d7a918c4510952>`_
- Log about it. `c226b87f2 <https://github.com/fedora-infra/fmn.consumer/commit/c226b87f296b4e76c9398ca8107ba93d8d895112>`_
- Use the new msg2long_form API. `20fa62aa0 <https://github.com/fedora-infra/fmn.consumer/commit/20fa62aa08639a0337ebabc295798eef01d74cc5>`_
- Also use long_form for batch emails. `67b43f1f1 <https://github.com/fedora-infra/fmn.consumer/commit/67b43f1f158262071a2c0d914d6bda90eb12d7dc>`_
- Include link with long_form. `f3dfa33e2 <https://github.com/fedora-infra/fmn.consumer/commit/f3dfa33e29651347b86754eb7a78ce37ba279cf5>`_
- Digest for IRC messages. `1e81bdf12 <https://github.com/fedora-infra/fmn.consumer/commit/1e81bdf12f78464311c4f4d18264c6218be89c8f>`_
- Merge pull request #37 from fedora-infra/feature/long-form `be92413d3 <https://github.com/fedora-infra/fmn.consumer/commit/be92413d36543f239121c39b96806efa45a22f30>`_
- Further comment. `8cc18db11 <https://github.com/fedora-infra/fmn.consumer/commit/8cc18db11b36893882d9b875b217d284ad797b6c>`_
- Merge pull request #38 from fedora-infra/feature/irc-digest `9abaea8e4 <https://github.com/fedora-infra/fmn.consumer/commit/9abaea8e489097b42aedaead73829065e741df08>`_

0.3.1
-----

- Log errors from the routine polling producers. `a00e51c10 <https://github.com/fedora-infra/fmn.consumer/commit/a00e51c1026d33a4bf925397f2e20b5823f4249c>`_
- Try to get encoding right with email messages. `1b604dbe6 <https://github.com/fedora-infra/fmn.consumer/commit/1b604dbe6855a9c82134c74c498944fd872412bc>`_
- Use to_bytes. `580bac101 <https://github.com/fedora-infra/fmn.consumer/commit/580bac101be0b44065140a39ffdf91fd66703462>`_
- The unicode sandwich is king. `ec40383c7 <https://github.com/fedora-infra/fmn.consumer/commit/ec40383c79442f9e9628b75faeb922042fd6cc35>`_
- Somehow we got this backwards. `0024b43ae <https://github.com/fedora-infra/fmn.consumer/commit/0024b43ae81933e8df7768c47847cd7fbb6ca905>`_
- Merge pull request #32 from fedora-infra/feature/consumer-errors `fe20ca060 <https://github.com/fedora-infra/fmn.consumer/commit/fe20ca0601f768c8eb05ea74233cb978885538fb>`_
- Merge pull request #31 from fedora-infra/feature/producer-errors `a138144e9 <https://github.com/fedora-infra/fmn.consumer/commit/a138144e9a253667b089ef9f5bf435616e50112a>`_

0.3.0
-----

- I want to know about this. `91c56fa82 <https://github.com/fedora-infra/fmn.consumer/commit/91c56fa82a60b20d31d8da4e1b8a10fc306dcb68>`_
- This gives a 2.5x speedup in production. `8c74fa5ce <https://github.com/fedora-infra/fmn.consumer/commit/8c74fa5cecb01fa031d6725f25f869818d157dc1>`_
- This probably shouldn't be turned off by default.  It makes development harder. `92a1531fe <https://github.com/fedora-infra/fmn.consumer/commit/92a1531fe87f07d049d65026c2e8306d5cb7ddb5>`_
- Add some fas credentials at startup. `1991e2a9e <https://github.com/fedora-infra/fmn.consumer/commit/1991e2a9ed4c9428a5b2ba67abb60d50b55ec04b>`_
- long live threebot! `982b2fed1 <https://github.com/fedora-infra/fmn.consumer/commit/982b2fed1bc883722408b0a8c03914fad82772f6>`_
- Invalidate cache for group membership. `6e672c64a <https://github.com/fedora-infra/fmn.consumer/commit/6e672c64a26a1e64538767e409a441cadab66404>`_
- Merge pull request #26 from fedora-infra/feature/group_maintainer `f3706f142 <https://github.com/fedora-infra/fmn.consumer/commit/f3706f142a77cf3dd8c7395c4a495c4e18f9b9f7>`_
- When someone is added to the packager group create its user locally with the default rules `2ed504e2a <https://github.com/fedora-infra/fmn.consumer/commit/2ed504e2a71a9e95c0b4fb3e7dc149827a729d93>`_
- Refresh FMN's cache and pep8 fixes `10070e118 <https://github.com/fedora-infra/fmn.consumer/commit/10070e1186adca7cf4cc40919c024f2a938e9fa6>`_
- Merge pull request #27 from fedora-infra/rules_for_new_packagers `58349cdf4 <https://github.com/fedora-infra/fmn.consumer/commit/58349cdf47baaa01e4400da8054765a8946cb0c1>`_
- Throw a lock around cached preference refresh. `c58bbcbb3 <https://github.com/fedora-infra/fmn.consumer/commit/c58bbcbb3352b2079b6816e3184271d3a0995258>`_
- Merge pull request #28 from fedora-infra/feature/lock-on-pref-update `1c6a1271a <https://github.com/fedora-infra/fmn.consumer/commit/1c6a1271a48d10900a79c4b0661bbc10f11cf059>`_
- Fix bugs introduced in 2ed504e2a71a9e95c0b4fb3e7dc149827a729d93 `02fd14d53 <https://github.com/fedora-infra/fmn.consumer/commit/02fd14d5394c87acccf13c71d81ba14c22171f37>`_
- Fix incorrect fas message structure. `750148bcc <https://github.com/fedora-infra/fmn.consumer/commit/750148bccfebba0a4f00eb4617f828432d7d0272>`_
- pep8 `c8069b98b <https://github.com/fedora-infra/fmn.consumer/commit/c8069b98b1b5adb3a90b1feaa1512a09c64f06c6>`_
- When creating new Fedora users, enable by default. `dc4544ea1 <https://github.com/fedora-infra/fmn.consumer/commit/dc4544ea181f88b3eba6409ef46ae89b80a9fc27>`_
- Merge pull request #29 from fedora-infra/feature/possibly-active-by-default `bb4b183c8 <https://github.com/fedora-infra/fmn.consumer/commit/bb4b183c827231d606a94f3bc8557552480b4dca>`_
- Don't tack on delta if its in the future :clock1: :heavy_dollar_sign: `860d6a8a6 <https://github.com/fedora-infra/fmn.consumer/commit/860d6a8a665a9e9781c8e8b6256011d9216dcbdd>`_
- Merge pull request #30 from fedora-infra/feature/futuro `b435dbb05 <https://github.com/fedora-infra/fmn.consumer/commit/b435dbb05c158f460be1c87842a7d383b4d6908e>`_

0.2.7
-----

- Typofix. `a759ebc2d <https://github.com/fedora-infra/fmn.consumer/commit/a759ebc2d033e6cc7d1b92757b10fe76df68170f>`_

0.2.6
-----

- This thing doesn't actually have access to the config. `44b0bf075 <https://github.com/fedora-infra/fmn.consumer/commit/44b0bf075d1c1263b60a6bb43a3cd55cb89d134f>`_
- Merge pull request #23 from fedora-infra/feature/irc-bugfix `97effdc52 <https://github.com/fedora-infra/fmn.consumer/commit/97effdc52dd3b9b41827e56a314216f11072133b>`_
- Typofix. `a3cf9477f <https://github.com/fedora-infra/fmn.consumer/commit/a3cf9477f61139bc3bc250b62b752315d411f2b2>`_
- Merge pull request #24 from fedora-infra/feature/typofix `37ceca209 <https://github.com/fedora-infra/fmn.consumer/commit/37ceca209df200ead054edf0d93b28b3d29b108d>`_
- fix: updated IRC message formatting `528eaf619 <https://github.com/fedora-infra/fmn.consumer/commit/528eaf619cbd6a990395788a3fe91ff1033c2ea1>`_
- fix: added whitespace as requested by upstream `f157a3308 <https://github.com/fedora-infra/fmn.consumer/commit/f157a3308a6d92d945d13080f6e4991296ae7e88>`_
- Merge pull request #25 from Rorosha/develop `d42317d75 <https://github.com/fedora-infra/fmn.consumer/commit/d42317d75458b9922be140ba483d95be90b49933>`_

0.2.5
-----

- Fix missed session in the email backend. `2935d2c2d <https://github.com/fedora-infra/fmn.consumer/commit/2935d2c2dae72361ad55898920f27ab4db2deb18>`_
- Intelligent pkgdb2 cache invalidation. `b31f56223 <https://github.com/fedora-infra/fmn.consumer/commit/b31f562236ea8334ce5bfe210209b90c4d470523>`_
- Merge pull request #22 from fedora-infra/feature/pkgdb2-cache-invalidation `0a8bbc930 <https://github.com/fedora-infra/fmn.consumer/commit/0a8bbc930f103f1a90aa9a02d717198febe1210f>`_

0.2.4
-----

- Tweak config for development. `8843a4cde <https://github.com/fedora-infra/fmn.consumer/commit/8843a4cde486337c4a89d80c72624de7bf195efc>`_
- Only reconnect to IRC if not shutting down. `e9f0caf7f <https://github.com/fedora-infra/fmn.consumer/commit/e9f0caf7f9b3cf8e75c88165255cb604346754f4>`_
- Merge pull request #19 from fedora-infra/feature/careful-with-the-irc-reconnects `69b4522f4 <https://github.com/fedora-infra/fmn.consumer/commit/69b4522f4dacb2fe03281c7fcdd0fe419b41d9c0>`_
- Avoid logging so much unnecessarily. `c3d59803d <https://github.com/fedora-infra/fmn.consumer/commit/c3d59803d3e20c7c3731280fe6daf7213f173b23>`_
- Use the new caching mechanism from fmn.lib. `0239451cc <https://github.com/fedora-infra/fmn.consumer/commit/0239451ccd8dffca2cec22916aaa6dc34940af56>`_
- Merge pull request #20 from fedora-infra/feature/cream `716e54d6c <https://github.com/fedora-infra/fmn.consumer/commit/716e54d6cd63e1b373a9549d0263f53754f2d923>`_
- Add a relative arrow date to the irc message `296868357 <https://github.com/fedora-infra/fmn.consumer/commit/29686835749e1106bf4360606d0b922fc4abe5bd>`_
- Merge pull request #21 from fedora-infra/feature/relative-date `7ca396cf0 <https://github.com/fedora-infra/fmn.consumer/commit/7ca396cf02ed96a991eeb9a2ef947eba3d979aca>`_
- Link to dev instructions from the README. `2a35183f2 <https://github.com/fedora-infra/fmn.consumer/commit/2a35183f223f0a7c6dabec1a4c91cb12335ee1d3>`_
- Add a way to disable a backend alltogether. `6e4fa1287 <https://github.com/fedora-infra/fmn.consumer/commit/6e4fa12879f50c4b1f9fa6bfb18d3f1d0d110b36>`_
- Reorganize backend to not keep session as a state attribute. `67fbd80ac <https://github.com/fedora-infra/fmn.consumer/commit/67fbd80ac49b2f982dc1e73fc9f20e23550b4a2b>`_
- Employ new presentation bools. `7d039fb78 <https://github.com/fedora-infra/fmn.consumer/commit/7d039fb78c3be94c457049e7dadbcf898464bc92>`_
- Handle colorizing IRC messages. `7c5df91d8 <https://github.com/fedora-infra/fmn.consumer/commit/7c5df91d8370d0eb904e74516004a10fbc00146b>`_

0.2.3
-----

- Adapt to the new url scheme. `deded804b <https://github.com/fedora-infra/fmn.consumer/commit/deded804b9caa38e54dbe5e3cc0b1149b17bf112>`_
- .total_seconds compat for python 2.6. `3590f0166 <https://github.com/fedora-infra/fmn.consumer/commit/3590f0166bed474881d7d8a03feecb46e160a837>`_
- Fix typo in mail backend. `751112c43 <https://github.com/fedora-infra/fmn.consumer/commit/751112c43316bcd0382643b1534e34f44523223a>`_
- Update handle_batch to use the new detail model. `627cb8d2c <https://github.com/fedora-infra/fmn.consumer/commit/627cb8d2cba533c8aedc8682202257a609685c52>`_
- Continue on if we happen to send a message batch. `62c700053 <https://github.com/fedora-infra/fmn.consumer/commit/62c700053ea0bad85dec42b9412c1dd349145275>`_
- Make digest emails a little bit nicer. `63c775402 <https://github.com/fedora-infra/fmn.consumer/commit/63c775402c9339d0f7f0af865e5c7645966c4a8c>`_
- Try to reconnect if irc connection fails. `0e2792dd1 <https://github.com/fedora-infra/fmn.consumer/commit/0e2792dd156b69ae74c324dd04d2ce8032aa23e6>`_
- Shorten links with dagd for irc. `b0ff7e84c <https://github.com/fedora-infra/fmn.consumer/commit/b0ff7e84cf5a1acfbada18a506943f653f548b37>`_
- Merge pull request #10 from fedora-infra/feature/retry-irc-connect `42b009840 <https://github.com/fedora-infra/fmn.consumer/commit/42b009840fe6cf002adf9a4e8cce6d80effa66e0>`_
- Merge pull request #11 from fedora-infra/feature/shorten-with-dagd `708b7089d <https://github.com/fedora-infra/fmn.consumer/commit/708b7089dcc59fee29f4944bfeeb1b09199565c1>`_
- Provide shortlinks back to filters that trigger messages. `80bf02ac5 <https://github.com/fedora-infra/fmn.consumer/commit/80bf02ac5dbb8350b9159e573915d4b415350fdc>`_
- Merge pull request #13 from fedora-infra/feature/short-backlinks `27b1cfbff <https://github.com/fedora-infra/fmn.consumer/commit/27b1cfbffed8a0353a53fbd3c88d3f7a5a26f290>`_
- Queue and flush messages when lost client. `ccf3ca741 <https://github.com/fedora-infra/fmn.consumer/commit/ccf3ca74135eecc0308f276ee583a5e572fb7cf8>`_
- Merge branch 'develop' into feature/queue-when-no-clients `5474d3460 <https://github.com/fedora-infra/fmn.consumer/commit/5474d346063f02c8edc759c782f22e7481fbfc2d>`_
- Handle incomplete recipient dict. `23cd5dea3 <https://github.com/fedora-infra/fmn.consumer/commit/23cd5dea3134a129cbd2a54073818981d7ace281>`_
- Merge pull request #14 from fedora-infra/feature/queue-when-no-clients `c4f0879c5 <https://github.com/fedora-infra/fmn.consumer/commit/c4f0879c57398fdb5475ee3d8c6dd47fd6e7f9a4>`_

0.2.2
-----

- Some prep work for Android `de2c03ba5 <https://github.com/fedora-infra/fmn.consumer/commit/de2c03ba5782adf14ee3a804bef29e19c70f3225>`_
- Attempt to add registration id updating `7e12c86ab <https://github.com/fedora-infra/fmn.consumer/commit/7e12c86ab5159d3aa7e23815d9bf2263b8c27f06>`_
- Add base_url to all messages, nuke unused vars `d6c68b84a <https://github.com/fedora-infra/fmn.consumer/commit/d6c68b84a1a9a1eca5b32b2aa03aad52f4eb71d3>`_
- Merge pull request #4 from fedora-infra/android `d2acbf84f <https://github.com/fedora-infra/fmn.consumer/commit/d2acbf84f86c420dbb794bd55d0bc2e53a729b1b>`_

0.2.1
-----

- Shorten string. `d614743fc <https://github.com/fedora-infra/fmn.consumer/commit/d614743fcc256364871206c6b40d6f556e5f2d5d>`_

0.2.0
-----

- And that's why it wasn't working in stg. `011cec80d <https://github.com/fedora-infra/fmn.consumer/commit/011cec80db0393d25755986428e5935bd2c81bf5>`_
- Add forgotten import. `ae164330e <https://github.com/fedora-infra/fmn.consumer/commit/ae164330e92a6058b27c21a78e6f0cf9218fa91c>`_
- Protect against nonexistant preference. `e18cadcf5 <https://github.com/fedora-infra/fmn.consumer/commit/e18cadcf54e0e97f8e37e9d53ef8e1ddb86567a0>`_
- config for pkgdb queries. `00965738e <https://github.com/fedora-infra/fmn.consumer/commit/00965738eb0045b0a08d2bb0ff42e84a4bc5f13d>`_
- Some defaults for dogpile cache. `a1a375898 <https://github.com/fedora-infra/fmn.consumer/commit/a1a375898cb6afb9a4677f2a443479b663747a39>`_

0.1.3
-----

- Include the forgotten fmn.consumer.backends module. `3ec8712e0 <https://github.com/fedora-infra/fmn.consumer/commit/3ec8712e08ebeeb641ab52a10c5414b146cd02a6>`_

0.1.2
-----

- Include license and changelog. `5b05968e7 <https://github.com/fedora-infra/fmn.consumer/commit/5b05968e7a99187a19469b14ee642234770528f3>`_

0.1.1
-----

- Add fedmsg config stuff. `a6e444bc3 <https://github.com/fedora-infra/fmn.consumer/commit/a6e444bc3664099bc3f5a424f354c7b0e302e876>`_

fmn.rules
=========

0.9.1
-----

Pull Requests

- (@sayanchowdhury) #85, Add rules for Autocloud
  https://github.com/fedora-infra/fmn.rules/pull/85

Commits

- 6191e4910 Add rules for Autocloud
  https://github.com/fedora-infra/fmn.rules/commit/6191e4910
- 5e448f324 Merge branch 'master' into develop
  https://github.com/fedora-infra/fmn.rules/commit/5e448f324

0.9.0
-----

Pull Requests

- (@ralphbean)      #75, rST syntax typofix.
  https://github.com/fedora-infra/fmn.rules/pull/75
- (@mkrizek)        #77, Update taskotron rules to reflect recent changes
  https://github.com/fedora-infra/fmn.rules/pull/77
- (@pypingou)       #79, For some reasons it seems that sometime we do not have 'msg' in some messages
  https://github.com/fedora-infra/fmn.rules/pull/79
- (@pypingou)       #80, Let get_user_of_group return a set()
  https://github.com/fedora-infra/fmn.rules/pull/80
- (@mkrizek)        #78, Update taskotron tasks namespace
  https://github.com/fedora-infra/fmn.rules/pull/78
- (@pypingou)       #82, When retrieving the users in a group we're only interested in their username
  https://github.com/fedora-infra/fmn.rules/pull/82
- (@pypingou)       #81, Fix processing messages from anitya
  https://github.com/fedora-infra/fmn.rules/pull/81

Commits

- 89f6778e6 rST syntax typofix.
  https://github.com/fedora-infra/fmn.rules/commit/89f6778e6
- 8f5e6d0a8 Update taskotron rules to reflect recent changes
  https://github.com/fedora-infra/fmn.rules/commit/8f5e6d0a8
- bc7f19152 taskotron rules: make docstring more clear
  https://github.com/fedora-infra/fmn.rules/commit/bc7f19152
- ff74799ef Update taskotron tasks namespace
  https://github.com/fedora-infra/fmn.rules/commit/ff74799ef
- 47687c2d4 For some reasons it seems that sometime we do not have 'msg' in some messages
  https://github.com/fedora-infra/fmn.rules/commit/47687c2d4
- f6cf87065 Let get_user_of_group return a set()
  https://github.com/fedora-infra/fmn.rules/commit/f6cf87065
- 0374f3313 When retrieving the users in a group we're only interested in their username
  https://github.com/fedora-infra/fmn.rules/commit/0374f3313
- ac974ebc0 Fix processing messages from anitya
  https://github.com/fedora-infra/fmn.rules/commit/ac974ebc0

0.8.2
-----

Pull Requests

- (@ralphbean)      #73, Make FAS optional here.
  https://github.com/fedora-infra/fmn.rules/pull/73

Commits

- bfa43e926 Remove html from this header.
  https://github.com/fedora-infra/fmn.rules/commit/bfa43e926
- 50dafe9ff Make FAS optional here.
  https://github.com/fedora-infra/fmn.rules/commit/50dafe9ff

0.8.1
-----

Pull Requests

-                   #70, Merge pull request #70 from fedora-infra/feature/only-taskotron
  https://github.com/fedora-infra/fmn.rules/pull/70
-                   #71, Merge pull request #71 from fedora-infra/feature/nagios
  https://github.com/fedora-infra/fmn.rules/pull/71
-                   #72, Merge pull request #72 from fedora-infra/feature/anitya-by-project
  https://github.com/fedora-infra/fmn.rules/pull/72

Commits

- 0c0b98777 Only consider taskotron messages in the special taskotron rules.
  https://github.com/fedora-infra/fmn.rules/commit/0c0b98777
- 36f87e8a3 Add kwargs to this rule.
  https://github.com/fedora-infra/fmn.rules/commit/36f87e8a3
- 7ff5860a6 Add a nagios rule.
  https://github.com/fedora-infra/fmn.rules/commit/7ff5860a6
- 519bfa2cd Add a rule to allow filtering by anitya project.
  https://github.com/fedora-infra/fmn.rules/commit/519bfa2cd

0.8.0
-----

Pull Requests

- (@mkrizek)        #68, Add more taskotron rules
  https://github.com/fedora-infra/fmn.rules/pull/68
- (@pypingou)       #69, Add the pagure rules so they are taken into account
  https://github.com/fedora-infra/fmn.rules/pull/69

Commits

- 412303f54 Add more taskotron rules
  https://github.com/fedora-infra/fmn.rules/commit/412303f54
- a37aab19f taskotron: fix release-critical tasks
  https://github.com/fedora-infra/fmn.rules/commit/a37aab19f
- 62c68b889 Fix taskotron_task_particular_or_changed_outcome rule
  https://github.com/fedora-infra/fmn.rules/commit/62c68b889
- 95a1b1f54 taskotron: Proceed with the rule even if outcome is cleared
  https://github.com/fedora-infra/fmn.rules/commit/95a1b1f54
- a8d3c4cca Make one of taskotron rules a combination of other two
  https://github.com/fedora-infra/fmn.rules/commit/a8d3c4cca
- 80d236f62 Add the pagure rules so they are taken into account
  https://github.com/fedora-infra/fmn.rules/commit/80d236f62

0.7.5
-----

Pull Requests

- (@ralphbean)      #64, Add a rule for infragit repos.
  https://github.com/fedora-infra/fmn.rules/pull/64
- (@mkrizek)        #66, Fix taskotron link
  https://github.com/fedora-infra/fmn.rules/pull/66
- (@ralphbean)      #67, Cache calls to fedmsg.meta.msg2packages.
  https://github.com/fedora-infra/fmn.rules/pull/67

Commits

- af6d47859 No more irc, travis...
  https://github.com/fedora-infra/fmn.rules/commit/af6d47859
- 20be5c836 Add a rule for infragit repos.
  https://github.com/fedora-infra/fmn.rules/commit/20be5c836
- 56f7b7f99 Fix taskotron link
  https://github.com/fedora-infra/fmn.rules/commit/56f7b7f99
- 17afad28f Cache calls to fedmsg.meta.msg2packages.
  https://github.com/fedora-infra/fmn.rules/commit/17afad28f
- 248a85938 Imports.
  https://github.com/fedora-infra/fmn.rules/commit/248a85938

0.7.4
-----

Pull Requests

- (@puiterwijk)     #61, Work with broken Koschei rules
  https://github.com/fedora-infra/fmn.rules/pull/61
- (@mkrizek)        #62, Add taskotron
  https://github.com/fedora-infra/fmn.rules/pull/62
- (@ralphbean)      #63, Add mdapi rule.
  https://github.com/fedora-infra/fmn.rules/pull/63

Commits

- 6977b25fa Work with broken Koschei rules
  https://github.com/fedora-infra/fmn.rules/commit/6977b25fa
- e53c8aaee Default to a list in case it is ever absent again.
  https://github.com/fedora-infra/fmn.rules/commit/e53c8aaee
- 9db78ed27 Add taskotron
  https://github.com/fedora-infra/fmn.rules/commit/9db78ed27
- f7a9791e8 Add mdapi rule.
  https://github.com/fedora-infra/fmn.rules/commit/f7a9791e8
Changelog
=========

0.7.3
-----

- Need fmn.lib for the test suite. `143a16e9c <https://github.com/fedora-infra/fmn.rules/commit/143a16e9c95dd92a401733507901f67f65fd3d46>`_
- Fix another syntax error in pagure rule. `b6deee0d2 <https://github.com/fedora-infra/fmn.rules/commit/b6deee0d238c76dc717f841b5036c7429b1e335a>`_

0.7.2
-----

- Fix syntax error in pagure rule. `409b7bec7 <https://github.com/fedora-infra/fmn.rules/commit/409b7bec755b7b7be128c795c6e90bb4e4f2c20f>`_

0.7.1
-----

- Update Koschei URL `3662f3c3b <https://github.com/fedora-infra/fmn.rules/commit/3662f3c3b05af6a4b96685f9be6407a8014c6285>`_
- Merge pull request #57 from mizdebsk/koschei `dc6f0753b <https://github.com/fedora-infra/fmn.rules/commit/dc6f0753b2994bee50b140bb8ac8db3c252d9976>`_
- Add a new FMN rule to get notification about a project on pagure based on its tags `7f66b829e <https://github.com/fedora-infra/fmn.rules/commit/7f66b829e275e0f56b7792736d9520cf877bcb23>`_
- Adjust title as per @ralphbean's suggestions `e995454bc <https://github.com/fedora-infra/fmn.rules/commit/e995454bcfe9ec418dfcb49e5e9b3e692efc0b27>`_
- Merge pull request #59 from fedora-infra/pagure_project_tags `68dbc7ba1 <https://github.com/fedora-infra/fmn.rules/commit/68dbc7ba126c0da1b8b560f962f564712b04b458>`_
- Add FMN rules for new bodhi2 messages. `bc44e0806 <https://github.com/fedora-infra/fmn.rules/commit/bc44e080608c32e2619a59522c07aa604090930e>`_
- Merge pull request #60 from fedora-infra/feature/mash-rules `d6bd70a67 <https://github.com/fedora-infra/fmn.rules/commit/d6bd70a672983be4e42130b0fab6c34b267bb079>`_

0.7.0
-----

- Cache slow python-re2 compilation. `7f891427a <https://github.com/fedora-infra/fmn.rules/commit/7f891427a53bd11c4683d05ecbc8ee4a5b31778c>`_
- Merge pull request #54 from fedora-infra/feature/cache-slow-re2-compilation `d1298c854 <https://github.com/fedora-infra/fmn.rules/commit/d1298c8545a0b8664b208ae51c7d83b22a9babad>`_
- Add pagure rules. `5937d88dc <https://github.com/fedora-infra/fmn.rules/commit/5937d88dc4f061f2feb5a0cd1869dc48b5cf1900>`_
- Include a filter for particular pagure projects. `e9835b63f <https://github.com/fedora-infra/fmn.rules/commit/e9835b63f7e7245eb336f0dff150547fc9ba18b0>`_
- Fix incorrect ternary. `1dcd0bdbe <https://github.com/fedora-infra/fmn.rules/commit/1dcd0bdbe287798f4013b83bcc78bb531c1087c7>`_
- Merge pull request #55 from fedora-infra/feature/pagure `4f924af1f <https://github.com/fedora-infra/fmn.rules/commit/4f924af1f064da12d093b1260a3692588cbea171>`_
- Python3 support (for integration with fedora-hubs). `fcd2cd1d6 <https://github.com/fedora-infra/fmn.rules/commit/fcd2cd1d6a446fa836eafd4c3aa40e94f12b6fa8>`_
- Merge pull request #56 from fedora-infra/feature/py3 `999bfe004 <https://github.com/fedora-infra/fmn.rules/commit/999bfe0041fc95ef68712c8e5d9e73e53455ab19>`_

0.6.2
-----

- Ditch old re2 warning hook. `cd809bb5a <https://github.com/fedora-infra/fmn.rules/commit/cd809bb5aa487e10360e75e677d4897783a979d2>`_
- Pass only bytes to re2 (no unicode allowed). `1abb56192 <https://github.com/fedora-infra/fmn.rules/commit/1abb56192523b31db961bdcdea5c8afbf42ea588>`_
- Merge pull request #53 from fedora-infra/feature/re2-compat `ad4971943 <https://github.com/fedora-infra/fmn.rules/commit/ad4971943b8bd87d82848dfd71c960b96af121e1>`_

0.6.1
-----

- Bugfix. `941a9e238 <https://github.com/fedora-infra/fmn.rules/commit/941a9e238eeadbb8dd664b6d31cc89816a0d0fae>`_
- Add a rule to match specific anitya distros. `0ada1ed31 <https://github.com/fedora-infra/fmn.rules/commit/0ada1ed31279f0aa78401d95e0bd19164a0d5385>`_
- Use .lower() for distro comparisons, just like anitya does. `9417c9b6b <https://github.com/fedora-infra/fmn.rules/commit/9417c9b6bafa8e19785b3b98755f718eb6ed034b>`_
- Merge pull request #51 from fedora-infra/feature/anitya-distro `c1f6f5cb6 <https://github.com/fedora-infra/fmn.rules/commit/c1f6f5cb6c2b95660b587f92913afe4afab6733b>`_

0.6.0
-----

- Fix watchcommits text. `bedff651c <https://github.com/fedora-infra/fmn.rules/commit/bedff651ce6a60b16eef2fc28c378799aeb335d8>`_
- Add rules for FAF (ABRT server) `bf829d71e <https://github.com/fedora-infra/fmn.rules/commit/bf829d71e17e9a641f7b1b9b1afc3cf4828f570f>`_
- Merge pull request #48 from mbrysa/faf `1483c7661 <https://github.com/fedora-infra/fmn.rules/commit/1483c766110da0aa378fb69c9d7f21a25d8c6309>`_
- Allow our pkgdb query to be more flexible. `996059f00 <https://github.com/fedora-infra/fmn.rules/commit/996059f00998ee70b3832aa9bfca9fc1b51be3be>`_
- Add two new rules.  One for watching packages with the acl commit and another for watching packages with the watchcommits flag. `2dc58bf6c <https://github.com/fedora-infra/fmn.rules/commit/2dc58bf6c641bd49480da6f15c02ef28fa6c81a1>`_
- Merge pull request #49 from fedora-infra/feature/separate-ownership-rules `e1162935b <https://github.com/fedora-infra/fmn.rules/commit/e1162935b5b61be8fb2b565c748ecf53e8111d81>`_
- Handle all the new line-item meetbot messages. `c31a82bfc <https://github.com/fedora-infra/fmn.rules/commit/c31a82bfc84ad10d124ada299bd166ef51c4daa5>`_
- Merge pull request #50 from fedora-infra/feature/line-items `f52f29c5a <https://github.com/fedora-infra/fmn.rules/commit/f52f29c5ae70e8eb4a060fd69c47fb200083756e>`_

0.5.1
-----

- Add watchcommits/watchbugs to the package-ownership fmn rule. `5c9cee74f <https://github.com/fedora-infra/fmn.rules/commit/5c9cee74febea828db214333a4c39a6aaf0d3df1>`_
- Merge pull request #47 from fedora-infra/feature/watchcommits `015d84019 <https://github.com/fedora-infra/fmn.rules/commit/015d84019de458c8db89624d6a496f0c1bea669e>`_

0.5.0
-----

- Order of operations matters. `bb4e4d428 <https://github.com/fedora-infra/fmn.rules/commit/bb4e4d42882672080629f6ee6202ee2700c1c805>`_
- Merge pull request #40 from fedora-infra/feature/bugfix `219f0c560 <https://github.com/fedora-infra/fmn.rules/commit/219f0c56041bb0aa27a8eb51dc7fa6e518dda70b>`_
- Add a rule for finding unmapped anitya projects. `df6d5a809 <https://github.com/fedora-infra/fmn.rules/commit/df6d5a80928810122d3718fea61e57c1bf05ec4f>`_
- Fix syntax error. `96ab24bfa <https://github.com/fedora-infra/fmn.rules/commit/96ab24bfa09412398a4fa05d5dc7d7554f82b74e>`_
- Merge pull request #41 from fedora-infra/feature/unmapped-anitya-projects `f0000618f <https://github.com/fedora-infra/fmn.rules/commit/f0000618f1c033751ade024d1e01a8b2a4337234>`_
- Improve findability of the hacking document `a7ab83219 <https://github.com/fedora-infra/fmn.rules/commit/a7ab832194db9e7ac30693f1ceebffea977f6f38>`_
- Merge pull request #42 from fedora-infra/docs `ac68ccf18 <https://github.com/fedora-infra/fmn.rules/commit/ac68ccf18f5b0a1b9181ff98e777e94b5c3ffb71>`_
- typofix. `ffc71ca99 <https://github.com/fedora-infra/fmn.rules/commit/ffc71ca991ddee5dbb02f610fb52972ad45e3213>`_
- Add a rule to match members of a FAS group. `efcc105d2 <https://github.com/fedora-infra/fmn.rules/commit/efcc105d2c240e1d19a47cf3a1a4a12c61117b8c>`_
- Merge pull request #43 from fedora-infra/feature/typofix `ed33664ec <https://github.com/fedora-infra/fmn.rules/commit/ed33664ec46b178ff1a84c75dfe587393d0cb4c2>`_
- Merge pull request #44 from fedora-infra/feature/fas-group-member-rule `01d05566c <https://github.com/fedora-infra/fmn.rules/commit/01d05566c766524a88536bebf7181cb952762594>`_
- Fix anitya links. `7d01fbae4 <https://github.com/fedora-infra/fmn.rules/commit/7d01fbae488d24443694b2b8a4ee525c66e301ae>`_
- Merge pull request #45 from fedora-infra/feature/fix-anitya-links `fa9bef8c0 <https://github.com/fedora-infra/fmn.rules/commit/fa9bef8c0ff259b1c33b8532a2402fdf7bad3d3c>`_
- Typofix. `46f2d97d7 <https://github.com/fedora-infra/fmn.rules/commit/46f2d97d7284b857288a1f0b630407b8ef22b631>`_
- Disambiguate git messages. `8d9a282dd <https://github.com/fedora-infra/fmn.rules/commit/8d9a282ddb4f589d5ee25a78e07a1894d3da5c6c>`_
- Merge pull request #46 from fedora-infra/feature/disambiguate-git `2688be1c8 <https://github.com/fedora-infra/fmn.rules/commit/2688be1c80d87b2b04a37562055c8a1ca93b5d0f>`_

0.4.7
-----

- Apply new callable hinting. `aa191dfdd <https://github.com/fedora-infra/fmn.rules/commit/aa191dfddbf1aeb9e80c268ae488ffb4457c9ea2>`_
- The config argument needs to be named explicitly. `0ff84ddb6 <https://github.com/fedora-infra/fmn.rules/commit/0ff84ddb6b5835db5b038caff501546f3f57ee3d>`_
- Datanommer's `grep` method is expecting `users` `c8974e756 <https://github.com/fedora-infra/fmn.rules/commit/c8974e75685a5984f17694de65ae4e15e808e444>`_
- Merge pull request #39 from fedora-infra/feature/callable-hinting `a765b9228 <https://github.com/fedora-infra/fmn.rules/commit/a765b9228ec485500ebbe7229aab60385b524fdc>`_

0.4.6
-----

- Use re2 if available. `60d4e2293 <https://github.com/fedora-infra/fmn.rules/commit/60d4e2293483dff8ab2b000ef6d1a1bf1bbfe4d9>`_
- Add a filter to get all messages related to ansible `4313a044b <https://github.com/fedora-infra/fmn.rules/commit/4313a044b2fc064213cb1f24ff5dd54b2a2bec35>`_
- Merge pull request #37 from fedora-infra/feature/use-re2-if-available `aa13a468e <https://github.com/fedora-infra/fmn.rules/commit/aa13a468e121f395ad46ee8e45797c4bd3cd184b>`_
- Warn if RE2 falls back. `8f5af8615 <https://github.com/fedora-infra/fmn.rules/commit/8f5af861578db48ad3342d7892e7b05c6d4f4c1c>`_
- Remove unused import. `fc37e1dfd <https://github.com/fedora-infra/fmn.rules/commit/fc37e1dfd5bf0a1a7eb957ccac6b42526ca6b2aa>`_
- Typofix. `b07f8e2a7 <https://github.com/fedora-infra/fmn.rules/commit/b07f8e2a7507f37a988bd052f71fa9501f0345b8>`_
- Log how long pkgdb2 queries take. `38c18657c <https://github.com/fedora-infra/fmn.rules/commit/38c18657c6be9ea217dc41c1a825dd88df92e64b>`_
- Add a hint to the rule matching all ansible messages `e7ce96aa6 <https://github.com/fedora-infra/fmn.rules/commit/e7ce96aa627bd1c3333c0927d3a72522435b43ee>`_
- Merge pull request #38 from fedora-infra/ansible_all `1dad3176f <https://github.com/fedora-infra/fmn.rules/commit/1dad3176fc6c7969b03e2055761e67613e2315ea>`_
- Merge branch 'develop' of github.com:fedora-infra/fmn.rules into develop `68e5f0fbd <https://github.com/fedora-infra/fmn.rules/commit/68e5f0fbddd097716e61a60f8f004ab1daaadda2>`_

0.4.5
-----

- Add a new rule for the new koji rpm sign message. `6790673fb <https://github.com/fedora-infra/fmn.rules/commit/6790673fb3a1699d633f10b9c22ea192bc9d2c5c>`_
- Merge pull request #36 from fedora-infra/feature/rpm-sign `e360a3df4 <https://github.com/fedora-infra/fmn.rules/commit/e360a3df476296a8edd6b82860c18e07da448367>`_

0.4.4
-----

- Fix regex. `1b9b2ee95 <https://github.com/fedora-infra/fmn.rules/commit/1b9b2ee95401051b23eb28dae7b6bf9d4c57d961>`_
- Merge pull request #34 from fedora-infra/feature/fix-regex `00e8f4adc <https://github.com/fedora-infra/fmn.rules/commit/00e8f4adce65286c5b76468154486adccb8d8582>`_
- Don't search certificate and signature with regex. `4b5cdee0b <https://github.com/fedora-infra/fmn.rules/commit/4b5cdee0b98b6b3c9a805fdd1397e1400f3f4e88>`_
- Merge pull request #35 from fedora-infra/feature/one-thousand-percent `e4ffa62aa <https://github.com/fedora-infra/fmn.rules/commit/e4ffa62aa72b1854b54ed727d2d65224ba69907f>`_

0.4.3
-----

- Avoid calling pkgdb when we don't have to. `e3701471d <https://github.com/fedora-infra/fmn.rules/commit/e3701471df0c599bd8f06719b86c3cf75a319b41>`_
- Actually add rules for the-new-hotness. `d8b6ca63d <https://github.com/fedora-infra/fmn.rules/commit/d8b6ca63d4ac596cb8b6dd6eac60b2c638ea8d48>`_
- Fix stray search/replace. `7cfe56383 <https://github.com/fedora-infra/fmn.rules/commit/7cfe56383fdd67d5b03fc823d9eac2dda5cf8860>`_
- Merge pull request #31 from fedora-infra/feature/hotness2 `bb1f1f0d2 <https://github.com/fedora-infra/fmn.rules/commit/bb1f1f0d256eae12af21f2da03a65fa42ca242b2>`_
- Merge pull request #30 from fedora-infra/feature/mini-optimization `d8d5763c1 <https://github.com/fedora-infra/fmn.rules/commit/d8d5763c183e2c734ce4a8d78cdc848b2a66a719>`_
- Add a few more catchall rules. `c1f5d61bb <https://github.com/fedora-infra/fmn.rules/commit/c1f5d61bb7cb0cdfc3ee4c0960f0eb9bea69b6f5>`_
- Fix some links in the docstrings. `71893a4c1 <https://github.com/fedora-infra/fmn.rules/commit/71893a4c1a11eae9acf372874afe9cbad47d9c68>`_
- Careful with encoding for regex match. `ad0dd1b86 <https://github.com/fedora-infra/fmn.rules/commit/ad0dd1b86930db9fcc689e71a847c28a442a4786>`_
- Merge pull request #33 from fedora-infra/feature/special-encoding `f29f52ca6 <https://github.com/fedora-infra/fmn.rules/commit/f29f52ca6b73a865b1bc5179b362274ccb23b372>`_
- Merge pull request #32 from fedora-infra/feature/more-catchall `b784aef95 <https://github.com/fedora-infra/fmn.rules/commit/b784aef9513526f87cc690356849581840c287a1>`_

0.4.2
-----

- Remove extra newlines. `610afeff9 <https://github.com/fedora-infra/fmn.rules/commit/610afeff91658ee542e5cfa8597c356debe2fdbf>`_
- Include rules for the-new-hotness. `45a13621d <https://github.com/fedora-infra/fmn.rules/commit/45a13621d6336c306dabaeeaaf640fcee72ffac6>`_
- Add some new "catchall" rules to try and simplify the giant list of defaults. `2f93288ae <https://github.com/fedora-infra/fmn.rules/commit/2f93288ae723557bd2cc53a6286bfb5c23a0cade>`_
- Merge pull request #28 from fedora-infra/feature/hotness `cdeb6299d <https://github.com/fedora-infra/fmn.rules/commit/cdeb6299d08c41a4808e766b8251075c2470c941>`_
- s/trigger/match/ `777f5a408 <https://github.com/fedora-infra/fmn.rules/commit/777f5a40807b93df214db506afd54d6a283f61ac>`_
- Test specifically the category field. `fbaf35901 <https://github.com/fedora-infra/fmn.rules/commit/fbaf35901772d9fabf82daba33dc120da35afa33>`_
- Merge pull request #29 from fedora-infra/feature/consolidate `b46d2fee0 <https://github.com/fedora-infra/fmn.rules/commit/b46d2fee04358b8057da543c7952e3ed8edcbbb0>`_

0.4.1
-----

- Only check pkgdb ownership of pkgdb groups (instead of *all* groups). `873dff49b <https://github.com/fedora-infra/fmn.rules/commit/873dff49b8fc2a89479a9226807a44a9a96e9b12>`_
- Merge pull request #23 from fedora-infra/feature/pkgdb-groups `cbfc37d05 <https://github.com/fedora-infra/fmn.rules/commit/cbfc37d0506aad0bd3eb34d6b5f8b157d9b802b9>`_
- Add rules for summershum messages. `3844335d5 <https://github.com/fedora-infra/fmn.rules/commit/3844335d59e804e728603e34325887fadfca7c96>`_
- Add a rule to select only critpath updates from bodhi. `aaca4f4d1 <https://github.com/fedora-infra/fmn.rules/commit/aaca4f4d17987ca3cd16fcf72d34f3290f058c33>`_
- Merge pull request #24 from fedora-infra/feature/summershum `d99ea4252 <https://github.com/fedora-infra/fmn.rules/commit/d99ea4252a13535fa0ee112919a29823d3dbded8>`_
- Merge pull request #25 from fedora-infra/feature/critical-path `a1adb3ee3 <https://github.com/fedora-infra/fmn.rules/commit/a1adb3ee33664daa0804c71c70679bfebd93d520>`_
- datanommer hints for bodhi rules `5e791a464 <https://github.com/fedora-infra/fmn.rules/commit/5e791a464aa52fb3e969ae0faa4685c1e864e889>`_
- Make a bunch of topic-specific hints. `c74bfd577 <https://github.com/fedora-infra/fmn.rules/commit/c74bfd57788a92960f46967b2e46641ccdfdd167>`_
- All the rest of the hinting. `4800247ad <https://github.com/fedora-infra/fmn.rules/commit/4800247ad8de35d04f99ee366dc26bef137e9de1>`_
- Merge pull request #26 from fedora-infra/feature/datanommer-hinting `1ec8389b2 <https://github.com/fedora-infra/fmn.rules/commit/1ec8389b204c76185e32345d6d1c621317796495>`_
- Less formal short-descriptions for rules. `8d5735c9e <https://github.com/fedora-infra/fmn.rules/commit/8d5735c9e332a708a6c0feff2a5b43e7728e8bb8>`_
- Update some text based on code review. `0e2fdcf27 <https://github.com/fedora-infra/fmn.rules/commit/0e2fdcf27916a879939fdc31d79305622b33b18b>`_
- Merge pull request #27 from fedora-infra/feature/less-formal `f673b694a <https://github.com/fedora-infra/fmn.rules/commit/f673b694ada32e9f7a929ae0a6ee718590ae3aee>`_

0.4.0
-----

- Add the first rules for anitya integration in FMN `f409289c7 <https://github.com/fedora-infra/fmn.rules/commit/f409289c75a3ff63d8f4d18ffc4be912011d7979>`_
- Import the anitya rules at the module level `89a71d5c4 <https://github.com/fedora-infra/fmn.rules/commit/89a71d5c499514afcc21425e1c07bd93e9d62273>`_
- Change from Anitya:.. to Upstream:.. to be a little more user-friendly `aec962486 <https://github.com/fedora-infra/fmn.rules/commit/aec9624863122e8fc2dc6471a7662913ec00d4a6>`_
- Merge pull request #18 from fedora-infra/feature/anitya `9fa5cec2a <https://github.com/fedora-infra/fmn.rules/commit/9fa5cec2a2aaab7ec190b37e832bee552960ec76>`_
- Rules for Koschei state change and groups `ba0dfd910 <https://github.com/fedora-infra/fmn.rules/commit/ba0dfd910efddb87ce6bb10fcac56df6c5fe2d0a>`_
- Use links in docstrings `a7b954859 <https://github.com/fedora-infra/fmn.rules/commit/a7b95485980e50b47959b89f83b5cfd78b3e1899>`_
- Merge pull request #19 from msimacek/feature/koschei `26c6838f0 <https://github.com/fedora-infra/fmn.rules/commit/26c6838f0d4cf0bcdcda9992ecca81eb534ff2d6>`_
- fix topic name on project update `86f68de3c <https://github.com/fedora-infra/fmn.rules/commit/86f68de3cb314e7abfdb70c38006dfa6bcdd26a4>`_
- Merge pull request #20 from sayanchowdhury/topic-fix `ac1d39f85 <https://github.com/fedora-infra/fmn.rules/commit/ac1d39f8568597a23fe50c534b908200f26063bf>`_
- update the rules for anitya `e3ceacdae <https://github.com/fedora-infra/fmn.rules/commit/e3ceacdae0c9851a625fa193b22ea093c5ae2fbd>`_
- update the rules for bodhi `059ebb859 <https://github.com/fedora-infra/fmn.rules/commit/059ebb8593578598ac2d5f685c305cfed5f935de>`_
- add rules for bugzilla `56ddd8f31 <https://github.com/fedora-infra/fmn.rules/commit/56ddd8f3189271c1463179926caa3e4b7ec59be7>`_
- update the rules for buildsys `88ffe3b6e <https://github.com/fedora-infra/fmn.rules/commit/88ffe3b6e812578474527171bc55c11cc8f90011>`_
- update the rules for compose `ac603ecac <https://github.com/fedora-infra/fmn.rules/commit/ac603ecaca2f28dc6f127db8d0214fd4d63bb1fa>`_
- update rules for fedbadges `215b8b7ac <https://github.com/fedora-infra/fmn.rules/commit/215b8b7ac92403ff94adbc7c47ed75252755447d>`_
- create rules for fedimg `6cbb43cb3 <https://github.com/fedora-infra/fmn.rules/commit/6cbb43cb32c836ceb61e1408c1e70c3ec0cd0eeb>`_
- update the rules of fedimg `c9bdbb98c <https://github.com/fedora-infra/fmn.rules/commit/c9bdbb98c6c86737bf15fe870100e5112084c0c0>`_
- create the rules for fedora_elections `ceb793db5 <https://github.com/fedora-infra/fmn.rules/commit/ceb793db57d19bafa2dcd7c64cd555e8de5145a2>`_
- update the rules for fedoratagger `e50456a8d <https://github.com/fedora-infra/fmn.rules/commit/e50456a8d8a35a35c760447a1f5e60ae8b74bab6>`_
- create rules for nuancier `9412c6b98 <https://github.com/fedora-infra/fmn.rules/commit/9412c6b9894396c721ee9fa46ac39fbb49d85ac2>`_
- Add the new rules for kerneltest `b609809c5 <https://github.com/fedora-infra/fmn.rules/commit/b609809c561dd550445559bfef14160063cda576>`_
- create the rules for jenkins `592544f01 <https://github.com/fedora-infra/fmn.rules/commit/592544f010d5665b033424f4e567ea14b5fc9b79>`_
- Create rules for github `aec4444e5 <https://github.com/fedora-infra/fmn.rules/commit/aec4444e5574339ca54c9a1cead5b7598df5353c>`_
- create rules for fmn `b98c44c9e <https://github.com/fedora-infra/fmn.rules/commit/b98c44c9e3cd64ca8318e2a77b62f1231d9d12fe>`_
- update and add news for Fedora Package DB `2097c15c0 <https://github.com/fedora-infra/fmn.rules/commit/2097c15c06ed47a1222ddc4d90786cebadb43e4f>`_
- fix typo in fedora_elections `7e59dd3c6 <https://github.com/fedora-infra/fmn.rules/commit/7e59dd3c636b6d3df3aefb6ae8500c569faf7f0c>`_
- add the removed function for anitya info update `2a76d03a2 <https://github.com/fedora-infra/fmn.rules/commit/2a76d03a2f98bb42e15cf9c48fea49c6401f52c6>`_
- fix topic description in bodhi `227441b1f <https://github.com/fedora-infra/fmn.rules/commit/227441b1fca53bbbc1cff982038d90b150effb27>`_
- fix topic descriptions in fedimg `f6fd09a26 <https://github.com/fedora-infra/fmn.rules/commit/f6fd09a269d14182981ca94addf00127b0cf602c>`_
- change topic description in tagger `8dd722df2 <https://github.com/fedora-infra/fmn.rules/commit/8dd722df27cc117eac294910a79d613fdb89cb79>`_
- remove duplicate redundant method in github `939114bc6 <https://github.com/fedora-infra/fmn.rules/commit/939114bc696483da67bb75c593ba1f0434d8ff87>`_
- update the topic description in pkgdb `eecd8d5ec <https://github.com/fedora-infra/fmn.rules/commit/eecd8d5ec59e4835a2307bb48078cd09166bb7e4>`_
- fix topic name in pkgdb `291e4ae5f <https://github.com/fedora-infra/fmn.rules/commit/291e4ae5fe962fc57ad08f5a4b74a1d43db5c8e0>`_
- fix description in pkgdb acl delete `02876f511 <https://github.com/fedora-infra/fmn.rules/commit/02876f511bfbc0f0f8d35c1d3ae7f55da9be31b2>`_
- update description for topics in fedoratagger `b4014518f <https://github.com/fedora-infra/fmn.rules/commit/b4014518f3c80d7702718987e2ab9e92714d16f3>`_
- rename fmn to fmn_notifications `16cce9b7b <https://github.com/fedora-infra/fmn.rules/commit/16cce9b7b78d35f3e65917c1fd31a38b7c253acb>`_
- Merge pull request #21 from sayanchowdhury/gh-31 `8cb2ca696 <https://github.com/fedora-infra/fmn.rules/commit/8cb2ca696cffb31fe4e0f46cb717d730325dc50a>`_
- update the init file with the new modules `a40226143 <https://github.com/fedora-infra/fmn.rules/commit/a40226143c268756a256c532543fb9831a805ea0>`_
- Merge pull request #22 from sayanchowdhury/update_init `923fc8d32 <https://github.com/fedora-infra/fmn.rules/commit/923fc8d3273bcd8004ed3b039fe5ff07c95cde17>`_

0.3.0
-----

- Add forgotten import. `d1b0ab33d <https://github.com/fedora-infra/fmn.rules/commit/d1b0ab33dee0e9f6a654a6ab02543279037d5169>`_
- Start an utility method to retrieve the member of a group `get_user_of_group` `ae0e02c9c <https://github.com/fedora-infra/fmn.rules/commit/ae0e02c9c2d7b49e535a8fe8e9d3b7e82e56937f>`_
- Expand _get_pkgdb2_packagers_for to include the members of a group if the group has ACLs `d04966c17 <https://github.com/fedora-infra/fmn.rules/commit/d04966c17c8a33d95a94055365b699d0158e4351>`_
- get_user_of_group requires access to the fedmsg config `4663e3954 <https://github.com/fedora-infra/fmn.rules/commit/4663e3954885a5660959eae30efa78631f405dff>`_
- Add logic to instantiate an AccountSystem object if there isn't already one `f7ac04f40 <https://github.com/fedora-infra/fmn.rules/commit/f7ac04f40fc750cc78cca0c54f22a4256279641c>`_
- If the package has a group with some ACL, get the AccountSystem client and forward the configuration `fb75e310c <https://github.com/fedora-infra/fmn.rules/commit/fb75e310c9e091cc6b3d3435fed769f03d003492>`_
- Adjust the structure of the FAS credential per @ralphbean's advice `ccbea668e <https://github.com/fedora-infra/fmn.rules/commit/ccbea668e28ff6c9df21f881081af034d9867fe5>`_
- pep8. `89b22b5d6 <https://github.com/fedora-infra/fmn.rules/commit/89b22b5d6a189fe06169e6c7f6f31012d73b9b8d>`_
- Typofix. `7d50e5751 <https://github.com/fedora-infra/fmn.rules/commit/7d50e5751e423f6f4cc7b3601984e1d8089fd855>`_
- Apply group-ownership stuff to packages-of-user in addition to packagers-of-package. `23a469e91 <https://github.com/fedora-infra/fmn.rules/commit/23a469e91afa77a72d2187833ebcee7f5a86bf67>`_
- Merge pull request #16 from fedora-infra/feature/group_maintainer `ea438e745 <https://github.com/fedora-infra/fmn.rules/commit/ea438e7457fc8514fb2478ce5ee7d1ac1e426e4c>`_
- Add a rule that lets you filter by koji instance(s). `9b9e6b963 <https://github.com/fedora-infra/fmn.rules/commit/9b9e6b96386ed56c63778c2b05d3fd078fe3e2a2>`_
- Strip instances. `07b8cb64e <https://github.com/fedora-infra/fmn.rules/commit/07b8cb64e71f55f1fd77ecea3281ff9b58385189>`_
- Merge pull request #17 from fedora-infra/feature/koji-instances `8c77c2648 <https://github.com/fedora-infra/fmn.rules/commit/8c77c2648f603145ec8466329e5213a777d2f047>`_

0.2.5
-----

- Add a rule for matching a generic regex. `07276649c <https://github.com/fedora-infra/fmn.rules/commit/07276649c5d1479d80ead5e3ec3171b87cd53ce1>`_
- Merge pull request #15 from fedora-infra/feature/generic-regex `063d5fc46 <https://github.com/fedora-infra/fmn.rules/commit/063d5fc46327f5cb872e390b23ad8269266b3e8f>`_

0.2.4
-----

- More Copr messages: success, failed, skipped `c7004cd1f <https://github.com/fedora-infra/fmn.rules/commit/c7004cd1fb50acb94ef6f991e375fbfa7c2a6352>`_
- Merge pull request #14 from hroncok/copr_status `e3b6ebe9e <https://github.com/fedora-infra/fmn.rules/commit/e3b6ebe9e6c84539af40d37ca32ffd7b5fd20e38>`_

0.2.3
-----

- Switch back to using user-centric caching. `664a27fd8 <https://github.com/fedora-infra/fmn.rules/commit/664a27fd82f26dbcc288900096eecc9dbe60c519>`_
- Use our own cache keys for dogpile.cache. `a197a39ed <https://github.com/fedora-infra/fmn.rules/commit/a197a39ed4d8288a713a53e63d1c6271bde930a9>`_
- Add a cache invalidation function. `08afda487 <https://github.com/fedora-infra/fmn.rules/commit/08afda48728864ade9a033bef5f1008e97980adc>`_
- Typofixes. `12d7f5bd8 <https://github.com/fedora-infra/fmn.rules/commit/12d7f5bd88e9f5f39f0c76257f5ccf9a5f6a7783>`_
- Merge pull request #13 from fedora-infra/feature/whats-old-is-new-again `9e6b00e5f <https://github.com/fedora-infra/fmn.rules/commit/9e6b00e5f9615fc4a1ba78b6f99644d2cfe228ec>`_

0.2.2
-----

- Double check we retrieved  data `b2b5c27e0 <https://github.com/fedora-infra/fmn.rules/commit/b2b5c27e02a036672a48ce66dd925861ae94f93a>`_
- Typofix. `07f618ec6 <https://github.com/fedora-infra/fmn.rules/commit/07f618ec67fe4c59c757d88cba2fc20735dcc09c>`_
- Typofix Mark II. `0d4035a94 <https://github.com/fedora-infra/fmn.rules/commit/0d4035a9421d6b138f97169cc29949badd07cc42>`_
- Merge pull request #9 from fedora-infra/be_safe `f8fbf543c <https://github.com/fedora-infra/fmn.rules/commit/f8fbf543c569bc2be1a8aea4723468ed2881b7a9>`_
- Try 3 times before failing to talk to pkgdb2. `6ce5d9052 <https://github.com/fedora-infra/fmn.rules/commit/6ce5d90527945eed1a4c524db4080cea70cc8772>`_
- Link to dev instructions from the README. `96ace35fe <https://github.com/fedora-infra/fmn.rules/commit/96ace35fe5abe3908a2d872d68728ee09c14ddb6>`_
- Merge pull request #12 from fedora-infra/feature/careful-with-the-pkgdb2-plz `fb3dc02ae <https://github.com/fedora-infra/fmn.rules/commit/fb3dc02aeb527cc258da90dde37190911c4da9aa>`_

0.2.1
-----

- Add package-centric caching routines to fmn.rules.utils. `2c3901c24 <https://github.com/fedora-infra/fmn.rules/commit/2c3901c243fdbb902057ed0f52ae9b7f238afbf8>`_
- Use package-centric caching routines. `c0e0fc2c4 <https://github.com/fedora-infra/fmn.rules/commit/c0e0fc2c445288b750050bd8e95118cbfe11157e>`_
- Safety first. `ec26c9aeb <https://github.com/fedora-infra/fmn.rules/commit/ec26c9aebb9508389bbd5c934099cb8f2ea289a3>`_
- Merge pull request #10 from fedora-infra/feature/package-centric-caching `89009d55e <https://github.com/fedora-infra/fmn.rules/commit/89009d55e78cd21de83eba1995c579e50706981c>`_

0.2.0
-----

- Typofix. `30d0e1eb8 <https://github.com/fedora-infra/fmn.rules/commit/30d0e1eb84b335813a0efecf2f0faac43a131d21>`_
- Travis.yml `69f30367a <https://github.com/fedora-infra/fmn.rules/commit/69f30367ab554ba0e679961b1562c41a9b51c16c>`_
- If the pkgdb call fails, return an empty list of packages `44a746471 <https://github.com/fedora-infra/fmn.rules/commit/44a74647142869b3d8e9a9ee347f135f059c3f40>`_
- Add debugging log if the pkgdb call fails `86139c9a6 <https://github.com/fedora-infra/fmn.rules/commit/86139c9a6f00c480f90524b9161d3c2b4b5fcc1c>`_
- Generate the URL before calling it, and log it `1a20b0201 <https://github.com/fedora-infra/fmn.rules/commit/1a20b02010e973ddecebb0bc038a4fb93dfc3c88>`_
- Merge pull request #8 from fedora-infra/fix_pkgdb2 `805714bf3 <https://github.com/fedora-infra/fmn.rules/commit/805714bf3c603dfbcaf39bc53064a2534b93a912>`_
- Remove old pkgdb1 code.  :yolo: `5f5278e38 <https://github.com/fedora-infra/fmn.rules/commit/5f5278e38e36bffdddffabdedb955c2b687486aa>`_
- Use None as the sentinnel value here. `f106a4de6 <https://github.com/fedora-infra/fmn.rules/commit/f106a4de6989eb6f833ab074d77cf35593c9cbb1>`_

0.1.6
-----

- Pass the config obj along to fedmsg.meta. `aa0ad36c1 <https://github.com/fedora-infra/fmn.rules/commit/aa0ad36c1e04f052721b1e824362cb61a6233c38>`_
- Always return a set here. `70f4f589f <https://github.com/fedora-infra/fmn.rules/commit/70f4f589fe1672bf99ece68b6ae81621c8f6930a>`_
- Add a generic filter to get the message of a specific fedoraproject project `ff49c7c3f <https://github.com/fedora-infra/fmn.rules/commit/ff49c7c3f2b16945cf542feeb23642bdeea7b18f>`_
- Enable the generic fedorahosted per project filter to support multiple projects `b39e003f4 <https://github.com/fedora-infra/fmn.rules/commit/b39e003f4a76faed56297dcedb0e3eee8e869490>`_
- Update the generic filter for Fedora Hosted projects `b18b568d7 <https://github.com/fedora-infra/fmn.rules/commit/b18b568d78ecb73ae3c687e85ad2992db06a850b>`_
- Add filter to exclude notifications about one or more users `9def8f908 <https://github.com/fedora-infra/fmn.rules/commit/9def8f90822f2e36ca3206df7b223300848cffeb>`_
- Make sure there is no un-desired spaces `621be6aa0 <https://github.com/fedora-infra/fmn.rules/commit/621be6aa011ecd5996a12ecf7abfd5396a80e092>`_
- Fix the docstring to be more accurate about the function's action `f792b874e <https://github.com/fedora-infra/fmn.rules/commit/f792b874ee835ed06edaa660f13b56972412f1c0>`_
- Pep8 fix and be consistent about docstring formating `56c1ea56a <https://github.com/fedora-infra/fmn.rules/commit/56c1ea56a3675ea87e6f682f286dd56cc62a1b7c>`_
- Here we exclude message so the logic is reversed `5efd4a25f <https://github.com/fedora-infra/fmn.rules/commit/5efd4a25fba4143aced4e1f9dc8fdc1a5540029f>`_
- Handle case where project or fasnick is None `3764f5813 <https://github.com/fedora-infra/fmn.rules/commit/3764f58130cf5c4c952993190504ed6a05c1c004>`_
- Merge pull request #4 from fedora-infra/filter_hosted `249692094 <https://github.com/fedora-infra/fmn.rules/commit/2496920946cac6559a5e6ac5c937e37458a19df8>`_
- Merge pull request #5 from fedora-infra/filter_no_users `593e1bd95 <https://github.com/fedora-infra/fmn.rules/commit/593e1bd95ff059d0af689b31d3c6311897181d2d>`_
- Typofix. `a6de307b0 <https://github.com/fedora-infra/fmn.rules/commit/a6de307b038fa43cbf8199d361f1886fc072a9b9>`_
- Merge branch 'develop' of github.com:fedora-infra/fmn.rules into develop `6b6f7b83e <https://github.com/fedora-infra/fmn.rules/commit/6b6f7b83e19466ea5847881dfbc9cec97cfdf28a>`_
- Copy over pkgdb pagination fixes... `a872277f2 <https://github.com/fedora-infra/fmn.rules/commit/a872277f28145e2f0f78e0f75bc87f34478b7a50>`_
- Merge pull request #6 from fedora-infra/feature/pkgdb-pagination `5ff78cf45 <https://github.com/fedora-infra/fmn.rules/commit/5ff78cf455e9e64ca06744217c2b15b74c9b28c6>`_
- Add a rule for matching packages by regex. `38efb1366 <https://github.com/fedora-infra/fmn.rules/commit/38efb136609b645b0076c0aa1481330f9e28ee51>`_
- Merge pull request #7 from fedora-infra/feature/package-name-regex `4e2d8b327 <https://github.com/fedora-infra/fmn.rules/commit/4e2d8b3276bfec0db9968d795b51a3b668c3ee79>`_

0.1.5
-----

- Fix koji rules. `739bf99f7 <https://github.com/fedora-infra/fmn.rules/commit/739bf99f7903699360dae982a3ec079bff5afc88>`_
- Add rules for scratch builds. `36e749fe1 <https://github.com/fedora-infra/fmn.rules/commit/36e749fe1f83339893f17e00d43142e0abd700ba>`_

0.1.4
-----

- Add a rule for logger.log test messages. `c59765101 <https://github.com/fedora-infra/fmn.rules/commit/c5976510158ff8b5947fe832b7588889aac71be8>`_
- Merge pull request #1 from fedora-infra/logger.log `cfe70273b <https://github.com/fedora-infra/fmn.rules/commit/cfe70273bf11faf2f93c7fc7eda5ec0904b71957>`_
- COPR rules. `d95c5648c <https://github.com/fedora-infra/fmn.rules/commit/d95c5648c7580f1e423ea83fc3be148f39523d48>`_
- Merge branch 'develop' of github.com:fedora-infra/fmn.rules into develop `7b0a19536 <https://github.com/fedora-infra/fmn.rules/commit/7b0a195369e784f6abc6775b114c9e8cc7869641>`_
- Add fedocal rules. `0369a65ec <https://github.com/fedora-infra/fmn.rules/commit/0369a65ec48e482fccc421199d123ed643dda2a6>`_
- PEP8. `f8d0874e8 <https://github.com/fedora-infra/fmn.rules/commit/f8d0874e85d3b5ccc4fbe56a2fe890bd6d2179ce>`_
- Add forgotten fedocal rules for realsies this time. `2a1f68695 <https://github.com/fedora-infra/fmn.rules/commit/2a1f6869535950a8f033645ee2936596f32a1a4d>`_
- Adjust english. `4769df0d4 <https://github.com/fedora-infra/fmn.rules/commit/4769df0d48f35e4de1786a2d0df49ba1499a8a59>`_
- Add some debug statements. `31fe928ee <https://github.com/fedora-infra/fmn.rules/commit/31fe928eec181de67eea62a6bd7da95df63ffb2b>`_
- Pass the fedmsg config to the pkgdb query function. `a8a5f5b13 <https://github.com/fedora-infra/fmn.rules/commit/a8a5f5b1310a295b28e060b7a37f28b6287404f0>`_
- Provide option to use pkgdb1 or pkgdb2 API. `cbe70f5c1 <https://github.com/fedora-infra/fmn.rules/commit/cbe70f5c177c09f715403f6e407cb801d3e6089e>`_
- Use dogpile.cache to cache pkgdb queries. `e061b21a3 <https://github.com/fedora-infra/fmn.rules/commit/e061b21a3aea719781c1aa219776a8daa8816e14>`_

0.1.3
-----

- Add missing deps. `388893ee9 <https://github.com/fedora-infra/fmn.rules/commit/388893ee9b3e2388ccc84c2207ffedc619b9851e>`_
- Move pkgdb interface in from fmn.lib. `4cbb225ad <https://github.com/fedora-infra/fmn.rules/commit/4cbb225ad552b0b2e45c0bbf92ea9b77b4d43c59>`_
- 0.1.2 `e6a33d57d <https://github.com/fedora-infra/fmn.rules/commit/e6a33d57d96e9bade9db6b6a0d24f43f504f7642>`_

0.1.2
-----

- Ignore stuff. `aa9dc15d1 <https://github.com/fedora-infra/fmn.rules/commit/aa9dc15d11fe20a433ac5b0735267f6a95294f37>`_
- Include license files. `249006670 <https://github.com/fedora-infra/fmn.rules/commit/24900667070173f8cb2568a1dc6700973114f1c7>`_
- Include changelog. `37ff6dc8d <https://github.com/fedora-infra/fmn.rules/commit/37ff6dc8d311bae5cbe60e402bf7eb1ea35c80e3>`_

0.1.1
-----

- Update URL for pypi. `e628ef0c2 <https://github.com/fedora-infra/fmn.rules/commit/e628ef0c2623d1c3eaec9d5577bde71532f2a9a0>`_
