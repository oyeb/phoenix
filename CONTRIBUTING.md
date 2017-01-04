# Contribution Guidelines

You must fork this repository and _clone your fork_. Please make sure you know how to sync your fork with the upstream repo.
See [this](https://help.github.com/articles/syncing-a-fork/) and [this](https://ginsys.eu/git-and-github-keeping-a-feature-branch-updated-with-upstream/).

### If you are not a collaborator...

To add new features,

* First branch out from `development` into a "`topic-branch`".
* Add your changes.
* Push to your fork.
* Then on github.com, open a PR to merge "`topic-branch`" into `upstream/development`
    - Do not forget to tick **Allow edits from maintainers**! (See [why](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/#enabling-repository-maintainer-permissions-on-existing-pull-requests))
    - **Do not merge this `topic-branch` into your local `development` branch!**
* Wait for reviews and the eventual merge :1st_place_medal: or rejection :x:.

### If you are a collaborator

then you can:

1. choose to make a fork or,
2. just clone the original. ***(THIS IS THE BEST*** :cake: :100: ***METHOD!!)***

And to add new features,

#### 1. if you have a fork,

* Make sure you keep the `master` and `development` branches synced.
* First branch out from `development` into a "`topic-branch`".
* Add your changes.
* Push to your fork.
* Then on github.com, you go to **[this repo](https://www.github.com/arrow-/phoenix)** and create a new branch called, you guessed it... `topic-branch` from, you guessed it... `development`.
* Then you can open a PR from `your-fork:topic-branch` to `upstream:topic-branch`. **Simple**.
* Wait for reviews and the eventual merge :1st_place_medal: or rejection :x:.

#### 2. without the extra hassle of maintaining a fork,

* Clone **[this repo](https://www.github.com/arrow-/phoenix)**
* Then branch out from `development` into a "`topic-branch`".
* Add your changes.
* Then on github.com, you go to **[this repo](https://www.github.com/arrow-/phoenix)** and create a new branch called, you guessed it... `topic-branch` from, you guessed it... `development`.
* Push to **[this repo](https://www.github.com/arrow-/phoenix)** repo's `topic-branch`.
* On github.com, open a PR to merge the `topic-branch` into `development`.
* Wait for reviews and the eventual merge :1st_place_medal: or rejection :x:.

Eventually, the `topic-branch` will be merged into `development` by the owner and then you can sync `your-local:development` _(and `your-fork:development`)_ with `upstream-development`.
