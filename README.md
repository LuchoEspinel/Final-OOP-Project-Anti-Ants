# Final-OOP-Project-Anti-Ants
Diagrama UML

@startuml Final_UML_OOP
class "User" as user{
    username: string
    password: string   

    validar()
}

abstract class "Entrada" as entrada{
    categoria: string
    Concepto: string
    Valor: int

    guardarDia()
}
class "Inicio del dia" as inicio{
    Concepto: String

    guardarDia()
}
class "Final del dia" as final{
    -Concepto: "Final del dia"

    guardarDia()
}
class "Notificación" as noti{
    name: string
    date: string

    Mostrar()
}
class "Sugerencias Diarias" as sugd{
    name: string
    date: string

    Mostrar()
}
class recorrido {
    concepto: string
    guardarDia()
}
user *-- entrada
user<--noti
noti<--sugd
entrada-->inicio
entrada-->recorrido
entrada-->final
@enduml
