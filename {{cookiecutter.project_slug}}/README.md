# {{cookiecutter.project_name}}

## Author

Written by {{cookiecutter.author_name}} ([@{{cookiecutter.twitter_handle}}](https://twitter.com/{{cookiecutter.twitter_handle.to_lower()}}))

## Description

{{cookiecutter.project_short_description}}

## Building Instructions

Make sure you have `gradle` installed

```bash
brew install gradle
```

Navigate to base of directory, you should see `build.gradle` file.

```bash
gradle build
```

You should have a `{{cookiecutter.project_slug}}-VERSION.jar` file in the
`build/libs/` folder.  Load it within Burp and you are good to go.

## Loading Instructions
Launch BurpSuite, go to the Extender tab and then open the Extensions tab and
click on "Add". In the dialog window, select "java" as Extension Type and select
the burp-template.jar. For further details about BurpSuite extensions, refer
to their [documentation](https://portswigger.net/burp/help/extender.html#loading).
