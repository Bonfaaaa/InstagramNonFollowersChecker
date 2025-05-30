# Instagram Non-Followers Checker

This Python script compares your **followers** and **following** lists on Instagram to identify users you **follow but who don't follow you back**.

## Purpose

If you want to:

* Clean up your following list
* See who is not following you back
* Analyze your Instagram relationships

...this script is for you.

## What It Does

1. Reads two JSON files exported from Instagram:

   * `followers_1.json`: list of users who follow you
   * `following.json`: list of users you follow
2. Extracts the usernames (`value`) from each list.
3. Compares the two sets.
4. Prints the usernames of people you **follow** but who **don't follow you back**.

## How to Get the Files from Instagram

1. Go to [https://www.instagram.com](https://www.instagram.com) and log into your account.
2. Go to **Settings > Privacy and Security > Download Your Data**.
3. Request a copy of your data by entering your email address.
4. You'll receive an email with a link to download a `.zip` archive.
5. Extract the contents and locate the files:

   * `followers_1.json` is in `followers_and_following/followers_1.json`
   * `following.json` is in `followers_and_following/following.json`

## Requirements

* Python 3.x

## How to Use

1. Place the `followers_1.json` and `following.json` files in the same directory as the script.
2. Run the script with:

```bash
python main.py
```

3. The script will print the usernames of users you follow but who don't follow you back.

## Notes

* The script removes duplicates using sets.
* Matching is based solely on the username (`value`).
