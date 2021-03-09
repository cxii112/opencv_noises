# Эффекты
Здесь описан полный список эффектов с примерами изображений. 
В будущем он может расшириться, а некоторые эффекты измениться.
Навигация: 
* [Генерация](#генерация)
* [Изменение](#изменение). 

Для лучшего понимания прочитайте [руководство][full-usage], если еще не сделали это.

## Генерация
Все сгенерированные изображения будут со стандартными значениями высоты, ширины, количества шагов, 
поэтому будем рассматривать только эффекты.

### alpha
```
alpha simple
```
![Результат](./examples/gen__alpha__simple.png)
```
alpha lines
```
![Результат](./examples/gen__alpha__lines.png)

### color
```
color simple
```
![Результат](./examples/gen__color__simple.png)
```
color levels
```
![Результат](./examples/gen__color__levels.png)

### grayscale
```
grayscale simple
```
![Результат](./examples/gen__grayscale__simple.png)
```
grayscale lines
```
![Результат](./examples/gen__grayscale__lines.png)
```
grayscale lines-many
```
Для стандартного шага эффект близок к обычному шуму, вот пример для `-s 50`.
![Результат](./examples/gen__grayscale__lines-many.png)
```
grayscale simple-reverse
```
![Результат](./examples/gen__grayscale__simple-reverse.png)
```
grayscale sin
```
![Результат](./examples/gen__grayscale__sin.png)

## Изменение
Все измененные изображения будут со стандартными параметрами, в качестве исходного изображения использовать [`source_image1.jpg`][source-image].

### channels
```
channels levels-rbg
```
![Результат](./examples/edit__channels__levels-rgb.png)
```
channels levels-ymc
```
![Результат](./examples/edit__channels__levels-ymc.png)
```
channels levels-bmc
```
![Результат](./examples/edit__channels__levels-bmc.png)

[full-usage]: ./USAGE.md
[source-image]: ./examples/source_image1.jpg