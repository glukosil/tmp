package main

import (
    "fmt"
    "strings"
    "os"
    "math/rand"
)

const (
    cons int	= 4	// Разрядность строки
    pitka int	= 20	// Количество попыток
)

var (
    skaz = [3] string{"НЕ УГАДАНО", "УГАДАНО", "РЯДОМ" }	// Статусы угадывания букв
    ugad = [cons] int{}	// Массив со статусом каждой буквы секретного слова
    sec, buk, old, hid, hide string	// sec - секретное слово, buk - использованные буквы, old - предыдущий ход, hide - подсказка со скрытыми буквами
)

func UpYesNo(txt string) bool {
    for _, r := range txt {
       if r < 'A' || r > 'Z' { return false }
    }
    return len(txt) > 0
}

// Функция ввоад числа с проверкой
func Num(txt string) string {
    var p string
    fmt.Printf("%s: ", txt)
    fmt.Scanln(&p)
    p = strings.ToUpper(p)
    if p == "0" { fmt.Println("\nВы завершили игру. До встречи!"); os.Exit(0) }
    if len(p) == cons && UpYesNo(p) { return p } else { fmt.Printf("Ошибка ввода! Нужно ввести %d-значную строку из букв A-Z!", cons); return Num(txt) }
}

// Проверка хода
func Proverka(txt string, ind int) {
    if txt == sec { fmt.Printf("\n\nВЫ ВЫИГРАЛИ!\nУгаданное слово: %s\nЧисло попыток: %d", sec, ind); os.Exit(0) }
    txt1 := []rune(txt)
    sec1 := []rune(sec)
    hide1 := []rune(hide)
    for i := 0; i < cons; i++ {
       if txt1[i] == sec1[i] { ugad[i] = 1; hide1[i] = txt1[i] } else if strings.Contains(sec, string(txt1[i])) { ugad[i] = 2 } else { ugad[i] = 0 }
       if !strings.Contains(buk, string(txt1[i])) { buk += fmt.Sprintf(" %s", string(txt1[i])) }
    }
    old = txt
    hide = string(hide1)
}

// Игрооой процесс
func main() {
    for i := 0; i < cons; i++ {
       hide += "#"
       sec += string(rune(rand.Intn(25) + 65))
    }
    for x := 0; x < pitka; x ++ {
       fmt.Printf("\033[H\033[2JКонсольная игра 'БЕЙЗЛ 2.0'!\n\nЗагаданная %d-значная последовательность букв A-Z: %s\nПопыток: %d\n\nПОДСКАЗКА:\nИспользованные буквы: %s\nПредыдущий ход: %s\n\nРЕЗУЛЬТАТ ХОДА:\n|", cons, hide, pitka, buk, old)
       for i := 0; i < cons; i++ { fmt.Printf(" %s |", skaz[ugad[i]]) }
       Proverka(Num(fmt.Sprintf("\n\nПОПЫТКА %d:\nВведите предполагаемую %d-значную последовательность (0 - для выхода)", x + 1, cons)), x)
    fmt.Println("\n\nВЫ ПРОИГРАЛИ!\nЗакончились попытки!\nБыло загадано слово: ", sec)
    }
}
