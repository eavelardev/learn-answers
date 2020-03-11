# learn-answers
Program to learn the answers of a set of questions

I think that one of the best ways to learn new things is through repetition, for that reason I did this program to learn the answers of a set of questions in a fun way, importing that information from a JSON file.

## Using

```
./learn_answers -f <my json file>
```

example

```
./learn_answers -f handson-ml2/chapter1_The\ Machine\ Learning\ Landscape.json
```

to choosing random questions add `-r` argument

```
./learn_answers -rf handson-ml2/chapter1_The\ Machine\ Learning\ Landscape.json
```

to ask questions forever add `-l` argument

```
./learn_answers -lf handson-ml2/chapter1_The\ Machine\ Learning\ Landscape.json
```

to choosing random questions and to ask questions forever add `-rl` argument

```
./learn_answers -rlf handson-ml2/chapter1_The\ Machine\ Learning\ Landscape.json
```

## Mobile apps

I use [Termux](https://play.google.com/store/apps/details?id=com.termux) for android to run this Python app.

For IOS you can use [iSH](https://ish.app/).
