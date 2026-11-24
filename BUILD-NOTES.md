# Build notes — Developer Excuses

## What this entry is

This repository holds one entry for the make.fun bounty Make the AI Judge
Laugh: Developer Excuses. The entry is a single funny line, an excuse a
developer gives when code breaks in production, under 200 characters. The
program writes that line to the output entry file, where the house judge
reads it and compares it head to head with the other entries in private
blind rounds.

## How the line was chosen

The first draft blamed staging: it worked perfectly there because staging
has no users, no traffic, and no opinions. That draft was true and mildly
funny, but it only stated the obvious gap between staging and production,
and the joke landed on the setup rather than on a twist.

The final line keeps the same shape, it worked perfectly until something
went wrong, but moves the blame onto the users and then takes it straight
back: users started using it wrong, by which I mean, using it. The twist
is the reveal the judge brief asks for. Every developer recognises the
moment a bug turns out to be nothing more exotic than a real person doing
exactly what the software was built for. The line sounds like something a
developer would actually say out loud in an incident call, it uses no
jargon it does not need, and every word earns its place. It also avoids
the worn excuses the brief warns against, such as blaming the cache or
saying it works on my machine, and it turns the familiar it worked until
the users arrived setup into a punchline nobody has quite phrased this way.

## How the program works

The program is a single Python file at the repository root. It holds the
excuse as one text constant and, when run, makes sure the output folder
exists and writes the excuse into the entry file as UTF-8 text with no
trailing newline, so the file holds exactly the line and nothing else. It
reads nothing from anywhere else, needs no network and no secrets, and
takes well under a second to run.

## Files

The entrypoint is the Python file at the root. The license file carries
the MIT license. The readme carries the three linked make.fun badges, a
short description of the bounty, and how to run the program. This notes
file records the thinking behind the line.
