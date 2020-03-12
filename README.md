# learn-answers
Program to learn the answers of a set of questions

I think that one of the best ways to learn new things is through repetition, for that reason I did this program to learn the answers of a set of questions in a fun way, importing that information from a JSON file.

![](/imgs/app.png)

## Using

```
./learn_answers -f <my json file>
```

example

```
./learn_answers -f aws_cloud_practitioner_\(clf-c01\)/chapter1_the_cloud.json
```

to choosing random questions add `-r` argument

```
./learn_answers -rf aws_cloud_practitioner_\(clf-c01\)/chapter1_the_cloud.json
```

to ask questions forever add `-l` argument

```
./learn_answers -lf aws_cloud_practitioner_\(clf-c01\)/chapter1_the_cloud.json
```

to choosing random questions and to ask questions forever add `-rl` argument

```
./learn_answers -rlf aws_cloud_practitioner_\(clf-c01\)/chapter1_the_cloud.json
```

## Mobile apps

I use [Termux](https://play.google.com/store/apps/details?id=com.termux) for android to run this Python app.

For IOS you can use [iSH](https://ish.app/).
