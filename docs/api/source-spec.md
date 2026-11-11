# Pyinject public API — Plan

## Задачи в Linear

| Этап | Задача | Зависит от |
| -- | -- | -- |
| API и типизация | [SOR-5 — U1 · Зафиксировать поверхность API и матрицу проверки](<https://linear.app/sorvihead/issue/SOR-5/u1-zafiksirovat-poverhnost-api-i-matricu-proverki>) | — |
| API и типизация | [SOR-6 — U2 · Спроектировать базовые providers и .ref](<https://linear.app/sorvihead/issue/SOR-6/u2-sproektirovat-bazovye-providers-i-ref>) | <issue id="64b92a8a-cc9e-4cc5-a1fb-f111adbd1889" label="SOR-5" href="https://linear.app/sorvihead/issue/SOR-5/u1-zafiksirovat-poverhnost-api-i-matricu-proverki" /> |
| API и типизация | [SOR-7 — U3 · Спроектировать декларативный контейнер и контекст](<https://linear.app/sorvihead/issue/SOR-7/u3-sproektirovat-deklarativnyj-kontejner-i-kontekst>) | <issue id="cb2c649d-4e8b-4c3d-a240-2a07545d4380" label="SOR-6" href="https://linear.app/sorvihead/issue/SOR-6/u2-sproektirovat-bazovye-providers-i-ref" /> |
| API и типизация | [SOR-8 — U4 · Спроектировать типизированную композицию](<https://linear.app/sorvihead/issue/SOR-8/u4-sproektirovat-tipizirovannuyu-kompoziciyu>) | <issue id="7d204799-49ae-4b82-8244-2c92faea8cd0" label="SOR-7" href="https://linear.app/sorvihead/issue/SOR-7/u3-sproektirovat-deklarativnyj-kontejner-i-kontekst" /> |
| API и типизация | [SOR-9 — U5 · Спроектировать FactoryAggregate](<https://linear.app/sorvihead/issue/SOR-9/u5-sproektirovat-factoryaggregate>) | <issue id="8f7b56ec-409b-47d4-9775-bc5fec1f0bc3" label="SOR-8" href="https://linear.app/sorvihead/issue/SOR-8/u4-sproektirovat-tipizirovannuyu-kompoziciyu" /> |
| API и типизация | [SOR-10 — U6 · Спроектировать маркеры и wiring обычных функций](<https://linear.app/sorvihead/issue/SOR-10/u6-sproektirovat-markery-i-wiring-obychnyh-funkcij>) | <issue id="7d204799-49ae-4b82-8244-2c92faea8cd0" label="SOR-7" href="https://linear.app/sorvihead/issue/SOR-7/u3-sproektirovat-deklarativnyj-kontejner-i-kontekst" /> |
| API и типизация | [SOR-11 — U7 · Спроектировать FastAPI-путь без клиентского адаптера](<https://linear.app/sorvihead/issue/SOR-11/u7-sproektirovat-fastapi-put-bez-klientskogo-adaptera>) | <issue id="2ebb0760-6b6d-427f-8815-e8148f1145b1" label="SOR-10" href="https://linear.app/sorvihead/issue/SOR-10/u6-sproektirovat-markery-i-wiring-obychnyh-funkcij" /> |
| API и типизация | [SOR-12 — U8 · Заморозить public API v0](<https://linear.app/sorvihead/issue/SOR-12/u8-zamorozit-public-api-v0>) | <issue id="8f7b56ec-409b-47d4-9775-bc5fec1f0bc3" label="SOR-8" href="https://linear.app/sorvihead/issue/SOR-8/u4-sproektirovat-tipizirovannuyu-kompoziciyu" />, <issue id="75c5ce0a-b10b-4a6e-b04a-1c58ea48ae39" label="SOR-9" href="https://linear.app/sorvihead/issue/SOR-9/u5-sproektirovat-factoryaggregate" />, <issue id="7f29898c-b545-4b9f-8b60-17b94e41060a" label="SOR-11" href="https://linear.app/sorvihead/issue/SOR-11/u7-sproektirovat-fastapi-put-bez-klientskogo-adaptera" /> |
| Runtime | [SOR-13 — U9 · Реализовать базовое исполнение графа](<https://linear.app/sorvihead/issue/SOR-13/u9-realizovat-bazovoe-ispolnenie-grafa>) | <issue id="3b48dd81-0d8c-4475-ae4b-8dee0acd64ca" label="SOR-12" href="https://linear.app/sorvihead/issue/SOR-12/u8-zamorozit-public-api-v0" /> |
| Runtime | [SOR-14 — U10 · Реализовать композицию и aggregate](<https://linear.app/sorvihead/issue/SOR-14/u10-realizovat-kompoziciyu-i-aggregate>) | <issue id="942ea39c-6543-4ff9-8251-105c2e2d3c97" label="SOR-13" href="https://linear.app/sorvihead/issue/SOR-13/u9-realizovat-bazovoe-ispolnenie-grafa" /> |
| Runtime | [SOR-15 — U11 · Реализовать wiring и подтвердить FastAPI](<https://linear.app/sorvihead/issue/SOR-15/u11-realizovat-wiring-i-podtverdit-fastapi>) | <issue id="3db72f5e-2ade-4863-8c12-6e6391cb2cb1" label="SOR-14" href="https://linear.app/sorvihead/issue/SOR-14/u10-realizovat-kompoziciyu-i-aggregate" /> |
| PEP 827 | [SOR-16 — U12 · Исследовать PEP 827 в отдельной ветке](<https://linear.app/sorvihead/issue/SOR-16/u12-issledovat-pep-827-v-otdelnoj-vetke>) | <issue id="3b48dd81-0d8c-4475-ae4b-8dee0acd64ca" label="SOR-12" href="https://linear.app/sorvihead/issue/SOR-12/u8-zamorozit-public-api-v0" /> |

## Goal Capsule

**Цель:** разработчик может описать типизированный граф зависимостей в стиле dependency-injector и заранее увидеть, какие ошибки обнаруживаются статически, а какие проверяются при wiring и исполнении.

**Текущий результат работы:** согласованный public API, декларации типов, примеры и проверяемые контракты. Сначала выполняются U1–U8 без реализации resolver, кэшей и инъекции. U9–U11 — последующая runtime-реализация после API gate. U12 — отдельная экспериментальная ветка.

**Приоритет источников:** явные решения пользователя → требования R → технические решения KTD → задачи U. Не подменять согласованный API более удобным для реализации. Если сигнатура не проходит проверку типов, сохранить минимальный контрпример и вынести конкретное изменение API на обсуждение.

## Product Contract

### Summary

Базовый pyinject использует декларативные контейнеры как макеты графа. Factory и Singleton получают все аргументы при объявлении, а ссылки на результаты других провайдеров передаются через .ref. Контекст исполнения принадлежит экземпляру контейнера. Поддерживаются композиция через Dependency и DependenciesContainer, FactoryAggregate, wiring обычных функций и стандартный FastAPI Depends.

### Problem Frame

Динамический DI позволяет объявить некорректную связь и обнаружить ошибку только при запуске. Нам нужен знакомый декларативный синтаксис с проверяемой границей типизации. До реализации графа необходимо проверить эту границу: отсутствие ошибок type checker само по себе не доказывает корректность runtime-маркеров и Annotated metadata.

### Requirements

**Объявление провайдеров**

* R1. Сохранить стиль dependency-injector: атрибуты класса контейнера, providers.Factory / Singleton и вызов связанного провайдера через экземпляр контейнера.
* R2. Factory и Singleton полностью сконфигурированы при объявлении; partial initialization, overrides и передача дополнительных аргументов при разрешении отсутствуют в базовой версии.
* R3. В DSL свойство provider.ref статически представляет результат T, но в runtime является символическим Ref. В публичных примерах не нужны cast, Any или type: ignore; внутренние приведения локализованы.
* R4. Ошибочные имена аргументов, пропущенные обязательные параметры и несовместимые типы аргументов должны выявляться поддерживаемыми type checker. Ограничения для generic callable и overload определяются явно, без обещания универсальной поддержки.

**Контейнеры и композиция**

* R5. Атрибуты класса образуют макет графа без контекста исполнения. Объявление и создание экземпляра контейнера не должны создавать прикладные зависимости; получение результата происходит по вызову связанного провайдера.
* R6. Factory создаёт новый результат при разрешении, Singleton сохраняет результат в контексте экземпляра контейнера; разные экземпляры контейнера изолированы.
* R7. Допускаются прямые наследники DeclarativeContainer; наследование от конкретного контейнера запрещено. Композиция заменяет наследование.
* R8. Dependency — полностью настроенный прокси другого провайдера. Обязательный пример: Application.repository = providers.Dependency(Infrastructure.repository), затем Factory(Service, repo=repository.ref). Это не незаполненный слот и не передача зависимостей в конструктор Application.
* R9. Предусмотреть DependenciesContainer, параметризованный конкретным DeclarativeContainer, для композиции группы провайдеров с сохранением типов атрибутов. Точный синтаксис доступа и доказательство типизируемости — результат U4.
* R10. FactoryAggregate выбирает настроенную фабрику по ключу. В базовом контракте задаётся общий тип результата T; не обещается выведение отдельного типа для каждого строкового ключа. Его ссылка представляет callable выбора фабрики, а не готовый T.

**Wiring**

* R11. Обычные функции используют параметр с default-маркером: service: Service = Provide\[Container.service\]. Аргумент можно опустить; явный аргумент имеет приоритет и проверяется статически. Декоратор inject сохраняет сигнатуру.
* R12. FastAPI использует Annotated\[Service, Depends(Provider\[Container.service\])\]. Provider здесь — wiring-маркер callable, а не класс providers.Provider. Контроллер получает Service; при прямом вызове Python аргумент остаётся обязательным.
* R13. Использовать стандартный FastAPI Depends и привычный module wiring. На клиенте не появляется обязательный setup(app), собственный Depends или отдельный интеграционный адаптер.
* R14. Честно описать границы: .ref не является настоящим T вне DSL; type checker не связывает Annotated\[T, Depends(...)\] с типом результата зависимости. Стандартная ветка не заявляет доказанную soundness этих границ.

**Порядок разработки**

* R15. Сначала зафиксировать public API и проверить типы без runtime-реализации, затем реализовывать отдельными этапами.
* R16. Эксперимент с PEP 827 вести в отдельной ветке. Его инструменты и возможности не являются зависимостью базового пакета.

### Key Decisions

* D1. Governs R1–R4. Декларативный синтаксис и .ref (session-settled: user-directed — выбран вместо альтернативного builder/lambda API: сохранить стиль dependency-injector).
* D2. Governs R2, R15–R16. Полные привязки в базе и отдельный эксперимент (session-settled: user-directed — выбран вместо partial initialization и overrides в стандартной версии: ограничить API возможностями текущей типизации).
* D3. Governs R5–R9. Макет графа и композиция (session-settled: user-directed — выбраны вместо наследования контейнеров и незаполненных Dependency: прокси указывает на объявление, исполнение живёт в экземпляре).
* D4. Governs R10. FactoryAggregate включён в public API (session-settled: user-approved — выбран как дополнительный механизм выбора настроенной фабрики).
* D5. Governs R11–R13. Два вида wiring (session-settled: user-directed — выбраны вместо единого синтаксиса для всех функций: обычные функции допускают пропуск аргументов, контроллеры вызываются FastAPI).

### API sketches

Эти примеры фиксируют клиентскую форму, но не являются уже проверенной реализацией.

```python
class Infrastructure(DeclarativeContainer):
    repository = providers.Singleton(Repository, dsn="...")

class Application(DeclarativeContainer):
    repository = providers.Dependency(Infrastructure.repository)
    service = providers.Factory(Service, repo=repository.ref)

app = Application()
service = app.service()
```

```python
@inject
def process(*, service: Service = Provide[Application.service]) -> None:
    ...

@router.get("/items")
@inject
def endpoint(
    service: Annotated[Service, Depends(Provider[Application.service])],
):
    ...
```

Для DependenciesContainer намеренно не фиксируется непроверенная магия **getattr**: точный клиентский пример — обязательный результат U4.

### Scope Boundaries

**В первом этапе:** спецификация, type-only объявления/заглушки, положительные и отрицательные typing fixtures, документация ошибок и runtime-сценариев. Заглушки не должны создавать впечатление работающего DI.

**Отложено в U9–U11:** исполнение графа, кэши, binding, inject/wire/unwire и проверки с реальным FastAPI.

**Отложено в U12:** исследование partial initialization и overrides с PEP 827. Это не обещание реализовать все возможности PEP.

**Вне текущего плана:** Resource, request scopes, async providers, Configuration, автоматическая регистрация, полная совместимость со всей библиотекой dependency-injector, плагины type checker для основной ветки. Поддержка async-функций с синхронными провайдерами не означает поддержку async providers.

## Planning Contract

### Key Technical Decisions

* KTD1. Использовать ParamSpec для связи конструктора Factory/Singleton с аргументами callable; generic instance **getitem** — кандидат для Provide\[...\] и Provider\[...\]. Доказать на выбранных checker в U2/U6, не выдавать сигнатуры за проверенные. Требования: R1–R4, R11–R12.
* KTD2. Разделить объявление узла, символическую ссылку, связанный провайдер и execution context. Кэш Singleton идентифицируется исходным узлом и контекстом; прокси не создаёт собственный singleton. Требования: R5–R8.
* KTD3. Для R7 базовый runtime должен отклонять наследование от конкретного контейнера. Для статической проверки в примерах применять явный @final на конкретных контейнерах: @final на базе запретил бы и первый уровень; автоматически вывести «final после одного уровня» стандартная типизация не обещает.
* KTD4. Dependency должен сохранять тип результата исходного провайдера без публичного Any. Предложенную форму Dependency\[P: Provider\] проверить отдельно: извлечение T из произвольного P не считать решённым. Для DependenciesContainer исследовать типизированный descriptor/projection; провал проверки не маскировать Any и не заменять API молча. Требования: R8–R9.
* KTD5. FactoryAggregate моделировать как callable с селектором отдельно от нульаргументного Provider\[T\]. Для первой версии — общий T, только полностью настроенные Factory, runtime-ошибка неизвестного ключа, без динамических типизированных атрибутов по именам ключей. Требование: R10.
* KTD6. Предлагаемый wiring-контракт: wire(modules=\[...\]) связывает функцию с контекстом экземпляра; unwire() снимает привязку. Повторная привязка к другому активному контексту должна явно отклоняться, а не незаметно переключать приложение. Эти детали фиксируются в U6, до runtime. Требования: R11–R13.
* KTD7. Базовые провайдеры синхронные; sync/async функции получают подходящий inject wrapper. Разрешение маркеров происходит при вызове, явные значения сохраняются. Для FastAPI в U7 исследовать путь marker → Depends → inject, inspection сигнатуры и фактическое кэширование. Не обещать request scope или соответствие use_cache кэшу провайдера до проверки. Требования: R11–R14.
* KTD8. Предлагаемый набор проверок: актуальная стабильная Python на старте U1, mypy и Pyright с закреплёнными версиями. Не обещать поддержку диапазона Python и всех checker до выполнения U1–U8. Публичные корректные примеры проходят без подавления ошибок. Требования: R4, R14–R16.

### High-Level Technical Design

Схемы задают связи и границы ответственности, а не структуру будущих классов.

**Структура графа.** Объявление контейнера содержит узлы; Ref и Dependency указывают на исходные узлы. Экземпляр контейнера владеет execution context. Связанный провайдер соединяет узел с этим контекстом, resolver обходит зависимости, Singleton использует кэш контекста.

**Жизненный цикл.** Объявление макета → создание пустого контекста → binding при доступе/вызове → разрешение достижимого подграфа → результат. wire добавляет привязку функций к контексту; unwire удаляет эту привязку. Освобождение ресурсов и пользовательский lifecycle за рамками базы.

**Поток wiring.** В обычной функции inject проверяет переданные аргументы, затем разрешает оставшиеся Provide-маркеры. В FastAPI Depends обрабатывает callable-маркер, после чего inject должен получить возможность разрешить ссылку. Последний путь пока является гипотезой и проверяется отдельно в U7/U11.

**Публичные роли.**

| Объект | При объявлении | При исполнении |
| -- | -- | -- |
| Factory / Singleton | Настроенный узел | Связанный нульаргументный callable → T |
| .ref | Статически T | Символическая ссылка, разрешаемая только DSL |
| Dependency | Прокси исходного узла | Делегирование в том же контексте |
| DependenciesContainer | Типизированная композиция | Доступ к связанным узлам; форма уточняется U4 |
| FactoryAggregate | Набор фабрик общего T | Callable выбора по ключу → T |
| Provide\[...\] | Default типа T | Маркер инъекции значения |
| Provider\[...\] | Callable-маркер | Передача через Depends для последующей инъекции |

**Решения при вызове.** Явный аргумент → оставить значение; маркер с доступной привязкой → разрешить; маркер без привязки → понятная ошибка до пользовательского тела. Неизвестный ключ aggregate и цикл графа → диагностическая ошибка с путём/ключом. Конкретные исключения и момент обнаружения фиксируются U3/U5/U6.

### Assumptions and technical gates

Рабочая папка планирования не содержит исходников проекта, поэтому пути ниже — предлагаемые, а не описание существующего репозитория. В U1 сначала сверить их с реальным checkout; не создавать второй пакет рядом с уже существующим.

Публичный модуль providers и wiring-экспорты уточняются U1. Object/Constant, auto-wiring configuration и методы introspection не добавляются автоматически.

Блокирующие проверки для заморозки API: типизация композиции (U4), тип aggregate.ref (U5), сохранение сигнатуры и маркеры (U6), совместимость Depends с выбранным маркером (U7). Они не мешают начать проектирование, но запрещают считать API готовым к runtime-реализации до закрытия gate.

## Implementation Units

Все пути относительны будущему корню репозитория. Задачи U1–U8 создают только API-артефакты и проверки типов. Runtime-сценарии в них пока являются спецификацией будущих тестов.

| Unit | Результат | Основные файлы | Depends on |
| -- | -- | -- | -- |
| U1 | Базовая матрица и структура API | pyproject.toml, docs/api/contract.md | — |
| U2 | Provider, Factory, Singleton, Ref | src/pyinject/providers.\*, tests/typing/providers/ | U1 |
| U3 | Декларативный контейнер | src/pyinject/containers.\*, tests/typing/containers/ | U2 |
| U4 | Dependency и DependenciesContainer | src/pyinject/providers.\*, tests/typing/composition/ | U3 |
| U5 | FactoryAggregate | src/pyinject/providers.\*, tests/typing/aggregate/ | U4 |
| U6 | Provide, Provider, inject, wire | src/pyinject/wiring.\*, tests/typing/wiring/ | U3 |
| U7 | Контракт стандартного FastAPI Depends | docs/api/fastapi.md, tests/typing/fastapi/ | U6 |
| U8 | Заморозка public API v0 | docs/api/, examples/, CI typing | U4, U5, U7 |
| U9 | Resolver и базовые providers | src/pyinject/, tests/unit/ | U8 |
| U10 | Runtime композиции и aggregate | src/pyinject/, tests/unit/ | U9 |
| U11 | Runtime wiring и FastAPI | src/pyinject/wiring.\*, tests/integration/ | U10 |
| U12 | Отдельный PEP 827 эксперимент | экспериментальная ветка, docs/experiments/ | U8 |

### U1. Зафиксировать поверхность API и матрицу проверки

**Requirements:** R1, R4, R14–R16; KTD8. **Depends on:** —.

Определить точные exports, минимальную поддерживаемую Python и версии checker. Выбрать единственный источник типов (.py с заглушками либо .pyi), установить строгие настройки и формат positive/negative typing fixtures. Не скрывать unsupported API за Any. Зафиксировать runtime-сценарии отдельно от исполняемых статических проверок.

**Acceptance / verification:** воспроизводимая команда для каждого checker; положительный контроль проходит, заведомая ошибка типов даёт ожидаемую диагностику. Для negative fixtures проверять код/место ошибки, а не только ненулевой exit code. Отдельный импортный smoke допускается, но не считается реализацией DI.

### U2. Спроектировать базовые providers и .ref

**Requirements:** R1–R4, R14; KTD1. **Depends on:** U1.

Описать Provider, Factory, Singleton, тип результата, descriptor .ref и границу class declaration / bound provider. Проверить ParamSpec на функциях и конструкторах классов. Составить таблицу поддерживаемых callable, включая решение по overload/generic callable.

**Scenarios:** Factory(Service, repo=repo.ref) принимается; неверный тип repo, неизвестный kwarg и пропущенный обязательный аргумент отклоняются; positional-only и keyword-only сохраняются; bound factory() имеет ожидаемый T и не принимает дополнительные bindings. Отдельно показать, что использование .ref вне DSL может пройти checker и не гарантирует корректное исполнение.

**Done:** type-only сигнатуры и fixtures проходят выбранную матрицу; documented limitation не маскируется cast в клиентском примере.

### U3. Спроектировать декларативный контейнер и контекст

**Requirements:** R5–R7; KTD2–KTD3. **Depends on:** U2.

Описать class-level blueprint, тип атрибута экземпляра, границы изменяемости графа и идентичность узла. Определить контракт прямого вызова провайдера на классе и диагностику циклов. Явно отделить runtime-запрет наследования от гарантий @final. Не переносить execution context в class attributes.

**Scenarios:** тип app.service() — Service; произвольные аргументы отклоняются; @final запрещает дальнейшее наследование статически. Будущие runtime-тесты: два прямых контейнера допустимы, наследник конкретного контейнера запрещён; constructors не вызываются при объявлении/Container(); Singleton одинаков внутри одного экземпляра и различен между двумя; Factory создаёт новые объекты; цикл даёт понятный путь.

**Done:** контракт и typing fixtures готовы; runtime-сценарии записаны, но ещё не реализованы.

### U4. Спроектировать типизированную композицию

**Requirements:** R8–R9; KTD2, KTD4. **Depends on:** U3.

Доказать обязательный пример Dependency(Infrastructure.repository) → repository.ref → Service. Сопоставить сохранение конкретного P и извлечение результата T; выбрать точную сигнатуру только после проверки. Для DependenciesContainer зафиксировать клиентский пример доступа к атрибутам без Any и динамического «всё разрешено».

**Scenarios:** .ref прокси имеет Repository; неизвестный атрибут группы и неверная зависимость обнаруживаются; несколько прокси одного исходного Singleton разделяют объект в одном контексте, два Application() изолированы. Нет скрытого Infrastructure() и обязательного constructor injection.

**Done:** оба механизма имеют public typing proof. Если желаемая форма невыразима, приложить минимальный контрпример и конкретные варианты изменения; U8 остаётся заблокированным до решения. Не удалять DependenciesContainer из базы молча.

### U5. Спроектировать FactoryAggregate

**Requirements:** R10; KTD5. **Depends on:** U4.

Зафиксировать декларацию именованных полностью настроенных Factory, общий T, callable-сигнатуру выбора и .ref как callable. Описать совместимость с wiring и передачу aggregate.ref в конструктор потребителя callable.

**Scenarios:** выбор двух реализаций даёт общий Service; несовместимый результат фабрики отклоняется; aggregate.ref подходит Callable выбора и не подходит параметру Service; неизвестный ключ обрабатывается runtime-ошибкой; нет аргументов для донастройки выбранной Factory. Контракт кэша не добавляет собственный Singleton и сохраняет общий контекст вложенных узлов.

**Done:** positive/negative fixtures и контракт ошибок готовы; ограничения ключей и дочерних providers явные.

### U6. Спроектировать маркеры и wiring обычных функций

**Requirements:** R11, R13–R14; KTD1, KTD6–KTD7. **Depends on:** U3.

Определить exports Provide, Provider, inject; доказать generic **getitem** на экземпляре и сохранение сигнатур декоратором. Зафиксировать wire/unwire, выбор контекста, конфликт повторного wiring и момент диагностики недостижимых ссылок.

**Scenarios:** вызов без default-инъецируемого аргумента допустим; явный корректный аргумент принимается, неверный отклоняется; обязательный бизнес-аргумент остаётся обязательным; return type и coroutine shape сохраняются. Будущие runtime-кейсы: отсутствие wiring даёт ошибку до тела только когда нужно разрешать маркер; полностью явные аргументы работают; wire/unwire повторяемы по документированному контракту; конфликт двух активных контейнеров не меняет привязку незаметно.

**Done:** типы маркеров и decorator proof, контракт wiring и ошибки записаны без реализации инъекции.

### U7. Спроектировать FastAPI-путь без клиентского адаптера

**Requirements:** R12–R14; KTD7. **Depends on:** U6.

Описать точный порядок router / inject и путь стандартного Depends(Provider\[...\]). Проверить по исходникам закреплённой версии FastAPI inspection callable-маркера и сигнатуры wrapper. Определить минимальный протокол маркера для будущей интеграции. Runtime smoke относится к U11; U7 не выдаёт статическую проверку за доказательство runtime.

**Scenarios:** параметр endpoint имеет Service и остаётся обязательным при прямом Python-вызове; return type Provider-маркера проверяется отдельно. Ошибочное соответствие Annotated типа и зависимости документируется как невыявляемое checker. Для будущих интеграционных тестов: sync/async endpoint, query schema без случайных args/kwargs, реальный объект вместо маркера в теле, explicit argument, Depends caching и use_cache=False без неподтверждённых обещаний request scope.

**Done:** последовательность интеграции обоснована анализом FastAPI, несовместимости оформлены как блокеры; runtime-проверки готовы для U11.

### U8. Заморозить public API v0

**Requirements:** R1–R16; KTD1–KTD8. **Depends on:** U4, U5, U7.

Собрать единую API-reference, таблицу exports, перечень исключений и примеры Infrastructure/Application, FactoryAggregate, обычной функции и FastAPI. Перенести статические проверки в CI. Сверить каждое требование с примером/fixture/будущим runtime-сценарием.

**Scenarios:** чистое окружение воспроизводит обе проверки; все positive fixtures проходят, все negative дают ожидаемые ошибки; ни один публичный пример не требует Any/cast/ignore. Неподдерживаемые формы и runtime-only гарантии обозначены.

**Done / API gate:** U1–U7 закрыты с доказательствами, нет нерешённых решений о форме API, complete API reference опубликована. Runtime ещё не считается работающим; переход к U9 разрешён только после gate.

### U9. Реализовать базовое исполнение графа

**Requirements:** R1–R7, R14; KTD2–KTD3. **Depends on:** U8. **Этап:** последующий runtime.

Реализовать согласованные узлы, binding, resolver, Ref, Factory, Singleton и enforcement контейнера. Не менять public signatures ради удобства. Перед реализацией выбрать и записать concurrency-контракт Singleton; FastAPI sync endpoints могут выполняться в разных потоках, поэтому нельзя молча считать все вызовы однопоточными.

**Tests:** ленивость, Factory freshness, Singleton identity/isolation, циклы и исключения constructor, восстановление после неудачного создания, прямой class-level вызов и запрещённое наследование; конкурентное первое создание в пределах выбранного контракта. Проверки типов остаются зелёными.

**Done:** unit-тесты проходят; публичные объявления заменены реализацией без изменения API.

### U10. Реализовать композицию и aggregate

**Requirements:** R8–R10; KTD2, KTD4–KTD5. **Depends on:** U9. **Этап:** последующий runtime.

Реализовать Dependency, DependenciesContainer и FactoryAggregate согласно замороженным сигнатурам; выполнять все исходные узлы в контексте root-контейнера.

**Tests:** два proxy одного Singleton возвращают один объект внутри Application; разные Application изолированы; group projection сохраняет контекст; вложенные Factory используют общую singleton-зависимость; неизвестный ключ и несовместимые объявления имеют согласованные ошибки; aggregate.ref действительно является связанным callable.

**Done:** composition/aggregate unit-тесты и typing suites проходят.

### U11. Реализовать wiring и подтвердить FastAPI

**Requirements:** R11–R14; KTD6–KTD7. **Depends on:** U10. **Этап:** последующий runtime.

Реализовать согласованные inject, wire/unwire и маркеры. Добавить проверки с реальным FastAPI без обязательного клиентского интеграционного слоя.

**Tests:** все сценарии U6/U7; sync/async handlers, explicit values, unwire, конфликт контекстов, сигнатура и OpenAPI без служебных параметров, ошибка до тела, правильная идентичность Singleton и свежесть Factory. Отдельно измерить фактическое число разрешений при повторном Depends и use_cache=False; закрепить наблюдаемую семантику тестом.

**Done:** HTTP-интеграционные и type-тесты проходят, ни один маркер не попадает в тело пользователя. При несовместимости механики с FastAPI не вводить setup(app) молча: вернуть конкретный конфликт на пересмотр API.

### U12. Исследовать PEP 827 в отдельной ветке

**Requirements:** R16; D2. **Depends on:** U8. **Этап:** эксперимент, не блокирует U9–U11.

Создать experiment/pep827 от зафиксированной базовой точки. Проверить статус PEP и доступность экспериментального checker, закрепить поддерживаемый commit/toolchain. Исследовать преобразование сигнатуры по переданным bindings, остаточные параметры, повторное связывание, overrides и готовность вложенных providers.

**Tests:** минимальные positive/negative примеры для каждой поддерживаемой операции; неверный binding, лишний kwarg, незаполненная нижележащая зависимость, совместимое/несовместимое переопределение. Неподдержанное отделить от поломки прототипа. Проверить отсутствие экспериментальных зависимостей в базовой ветке.

**Done:** отчёт о фактических возможностях и ограничениях плюс воспроизводимый typing-прототип; при отсутствии работоспособного toolchain допустим проверенный отчёт о блокере, но не заявление об успешной реализации.

## Verification Contract

**Сейчас:** результат — этот план и задачи; проверки реализации не запускались.

**API phase:** U1 фиксирует версии и точные команды. Положительные примеры проверяются mypy и Pyright; отрицательные — harness с ожидаемыми диагностическими кодами и местами. При противоречии checker сохраняется минимальный пример; простое подавление ошибки не закрывает задачу. Для .ref и Annotated отдельно документируются случаи, проходящие static check без runtime-гарантии.

**Runtime phase:** unit-тесты покрывают заявленные сценарии графа; integration-тесты выполняют реальные HTTP-запросы через FastAPI. Текущая типовая матрица обязательна после каждого runtime-этапа. Запуск широких дополнительных проверок нужен только при изменении поведения или обнаружении риска.

**PEP phase:** отдельные версии и команды, результаты не смешиваются с подтверждением базового API.

## Definition of Done

Планирование завершено, когда документ и задачи доступны в проекте Linear, у каждой задачи есть результат, критерии приёмки и зависимости, а предложения отделены от согласованных решений.

Первый этап разработки завершён только после U8: public API документирован, typing fixtures подтверждены, нет незакрытых блокеров композиции и wiring. Реализованный runtime появляется только после U9–U11. Эксперимент U12 имеет собственный критерий завершения и не является условием готовности базы. Заброшенные варианты сигнатур не остаются в public exports.

## Sources

* Решения пользователя в обсуждении Python DI framework — источник требований и ограничений.
* [Typing: ParamSpec и generics](<https://typing.python.org/en/latest/spec/generics.html>)
* [Typing: final](<https://typing.python.org/en/latest/spec/qualifiers.html>)
* [Python descriptors](<https://docs.python.org/3/howto/descriptor.html>)
* [dependency-injector: Factory](<https://python-dependency-injector.ets-labs.org/providers/factory.html>)
* [dependency-injector: Aggregate](<https://python-dependency-injector.ets-labs.org/providers/aggregate.html>)
* [dependency-injector: wiring](<https://python-dependency-injector.ets-labs.org/wiring.html>)
* [dependency-injector: FastAPI example](<https://python-dependency-injector.ets-labs.org/examples/fastapi.html>)
* [FastAPI Depends](<https://fastapi.tiangolo.com/reference/dependencies/>)
* [PEP 827](<https://peps.python.org/pep-0827/>)
* [Экспериментальная ветка mypy typemap](<https://github.com/msullivan/mypy/tree/typemap>)
