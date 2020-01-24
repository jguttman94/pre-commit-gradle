pre-commit-gradle
================

Some custom gradle hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit-hooks


### Using pre-commit-gradle with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/jguttman94/pre-commit-gradle
        rev: v1.0.0  # Use the ref you want to point at
        hooks:
        -   id: gradle-check
        # -   id: ...


### Hooks available

- `gradle-check` - Run gradle unit test tasks
    - Use gradlew (gradle wrapper) `args: ['-w', --wrapper]`.
- `gradle-build` - Run gradle build tasks
    - Use gradlew (gradle wrapper) `args: ['-w', --wrapper]`.
- `gradle-spotless` - Run gradle spotless tasks for java linting
    - Require spotless plugin: [github](https://github.com/diffplug/spotless/tree/master/plugin-gradle)
    - Use gradlew (gradle wrapper) `args: ['-w', --wrapper]`.
- `gradle-other` - Run arbitrary gradle commands
    - Use gradlew (gradle wrapper) `args: ['-w', --wrapper]`.
