﻿init:
    $ semen = Character('Семён', color="#ff8f92", what_color="fdf4e3")
    $ host = Character('Ведущий', color="#8954b1", what_color="fdf4e3")
    $ secretary = DynamicCharacter('secretary_name', color="#ff7bff", what_color="fdf4e3")
    $ director = Character('Павел Андреевич', color="#2cdbf2", what_color="fdf4e3")
    $ artyom = Character('Артем', color="#ffc208", what_color="fdf4e3")
    $ fyodor = Character('Федор', color="#9ad35d", what_color="fdf4e3")
    $ denis = Character('Денис', color="#55a394", what_color="fdf4e3")

    $ semen_mind = Character('', what_color="#c8c8c8", what_italic=True)
    $ story = Character('')
    $ ambience = Character('', what_color="#646464", what_bold=True, what_italic=True)
    $ letter = Character('Письмо', what_italic=True, what_prefix="\"", what_suffix="\"")

    image host = "host.png"
    image secretary = "secretary.png"
    image director = "director.png"
    image artyom = "artyom.png"
    image fyodor = "fyodor.png"
    image denis = "denis.png"

    image bg place_competition = "placeCompetition.jpg"
    image bg flat = "flat.jpg"
    image bg street = "street.jpg"
    image bg building = "building.jpg"
    image bg director_office = "directorOffice.jpg"
    image bg office_work = "officeWork.jpg"
    image bg desk = "desk.jpg"
    image bg reception = "reception.jpg"
    image bg meeting_room = "meetingRoom.jpg"
    image bg corridor = "corridor.jpg"

    $ secretary_name = "Секретарша"



# Игра начинается здесь:
label start:

    $ relationship_secretary = 0
    $ relationship_director = 0
    $ relationship_artyom = 0
    $ relationship_fyodor = 0
    $ relationship_denis = 0

    scene bg place_competition
    show host
    host "Дамы и Господа, до окончания финального этапа конкурса «Виртуоз .NET» осталось 10 минут!"
    host "Напоминаю, что Победитель получает уникальную возможность стать работником самой крупной IT компании страны. Покажите всё, на что вы способны!"
    semen_mind "Чёрт, у меня нет никаких идей! Если я сейчас быстро что-нибудь не придумаю, то останусь без работы и через неделю уеду обратно в деревню, а 4 года моей учебы в университете можно считать выброшенными коту под хвост!"
    hide host

    scene black
    centered "Две недели спустя..."

    scene bg flat
    semen_mind "Комната убрана. Все вещи собраны. Документы получил, ключи сдал. Такси прибудет через..."
    ambience "<стук в дверь>"
    semen "Да-да, уже выхожу!"
    story "Скрежет бумаги о деревянный пол обратил на себя все мое внимание. Немедленно подойдя к двери, я подобрал с пола бумажный конверт."

    semen_mind "<Смешок> С каких пор в общежитии почту стали доставлять прямо в комнаты студентам? Подождите, с каких пор мне в принципе стала приходить почта?"
    story "Последний раз похожий конверт мне присылал военкомат на первом курсе. С тех пор подобных подарков я ни от кого не получал."
    story "В голову начали закрадываться невеселые мысли о моем ближайшем будущем. Любопытство и желание побыстрее избавиться от находки боролись друг с другом."
    story "Наконец, ловкими движениями пальцев конверт был растерзан, а на свет появился внушительных размеров лист бумаги от начала и до конца исписанный текстом."
    letter "Уважаемый Попов Семен Степанович! Поздравляем, вы стали победителем конкурса «Виртуоз .NET»!"
    letter "Просим вас в день получения письма прибыть в региональный офис компании для прохождения стажировки ... При себе иметь удостоверение личности ... Не забудьте надеть маску ..."
    story "Руки и ноги задрожали. Я похватал все вещи и выбежал из комнаты."

    scene bg street
    story "С баулами наперевес я мчался через весь город, не веря своему счастью. Полчаса назад я думал, что до конца своих дней буду вспахивать грядки и доить коров, теперь у меня появился настоящий шанс обрести счастливое будущее!"

    scene bg building
    story "Сказать честно, прибыв к зданию офиса, я немного успокоился."
    semen_mind "Чтобы главная IT компания страны оповещала своих работников через бумажные письма? Очень консервативно."
    story "К тому же, я был полностью уверен, что две недели назад полностью провалился, и не одна уважающая себя IT компания не предложит мне работу."
    story "Немного погодя, набравшись духа, я все-таки открыл входную дверь здания. В нос сразу же ударил едкий запас кофе и шоколада, ясно свидетельствующий, что люди здесь работают на износ."

label director_meeting:

    scene bg reception
    story "Девушка, стоящая за стойкой ресепшна, сразу обратила на меня внимание. Видимо, новые лица здесь не часто появляются. Чтобы сгладить неловкий момент, я поспешил начать разговор."
    semen "Доброе утро, мне сегодня пришло оповещение..."
    story "Речь оборвалась, краска залила лицо. Ситуация, произошедшая сегодня, была по-настоящему необычной, похожей на чью-нибудь глупую шутку, и это вдруг стало мне полностью очевидно."
    story "Я был готов выбежать из офиса и забыть об этом недоразумении. Вдруг в мой поток панических мыслей вмешался голос секретарши."

    show secretary
    secretary "Доброе утро, наконец-то вы явились! Вас со вчерашнего дня ждут!"
    semen "Извините, вы меня с кем-то перепутали."
    secretary "Семен Степанович, боюсь, что это полностью исключено. Вы точная копия мужчины, досье на которого мне прислали вчера утром. Я от всей души поздравляю вас с победой в конкурсе!"
    secretary "Уверенна, что наша компания оставит у вас только приятное впечатление! Не стойте же, пройдемте со мной в кабинет Директора."
    hide secretary

    scene bg corridor
    story "Она говорила еще что-то, но я уже был не в состоянии слушать. Мое сердце готово было выпрыгнуть из груди, давление в голове затрудняло мысли. Я молча плёлся вслед за девушкой."
    secretary "Вот, пожалуйста, вам в эту дверь."
    story "Девушка постучала в дверь, раздался писк и замок отварился. Улыбаясь, секретарша рукой указывала мне на вход. Я шагнул в неизвестность."

    scene bg director_office
    story "В кабинете сидел средних лет мужчина, крепкого телосложения, его выискивающий взгляд сразу прошелся по мне с ног до головы. Мне опять стало очень неловко. Хотя лицо человека, сидящего за столом, выражало только доброту и заботу."
    semen "Доброе утро, я сегодня получил письмо и поспешил явиться в офис. Спасибо вам большое за предоставленную возможность."

    show director
    director "Здравствуйте, присаживайтесь, не стойте. Чемоданы свои можете поставить у двери, шапку и курточку повесить на вешалку."
    story "После этих слов я понял, насколько невежественно, даже грубо, выглядел мой визит, хотя казалось, будто моего собеседника это нисколько не удивило. Разложив все свои вещи, я сел за стол."
    director "Задавайте свои вопросы, судя по вашему взгляду, у вас их достаточно."
    semen "На какую должность я стажируюсь? Что входит в мои обязанности? С кем мне предстоит работать?"
    story "- протараторил я со скоростью пулемета, едва выговаривая слова..."
    story "Лицо моего собеседника изменилось, приобретя деловитые и строгие черты."
    director "Давайте по порядку. Вы будете введены в уже организованную команду .NET разработчиков. Разделение по обязанностям отсутствует, мы практикуем SCRUM технологию организации рабочего процесса."
    director "Если вам удастся произвести хорошее впечатление на коллектив, то у нашего с вами сотрудничества будет будущее."
    semen "Получается, они нанимают меня на работу, а не вы?"
    director "Взаимодействие с коллективом - важная часть работы. Считайте, что ваш рабочий день в коллективе – одно больше собеседование, его кульминацией станет вечерняя общая встреча, где вся команда, включая вас, обсудит результаты рабочего дня."
    director "Если коллектив вас не примет – не расстраивайтесь, если вы докажите свою пользу компании, я постараюсь внедрить вас в работу другой команды."
    ambience "<мягкие звуки раздаются из стола>"
    director "У команды перерыв, самое время для вас познакомиться с коллегами. Прошу вас. Анастасия вас проводит до нужного кабинета."
    director "Ваши сумку и одежку я сохраню у себя в офисе до вечера, можете не беспокоится. В добрый путь! Желаю вам всего наилучшего."
    hide director
    $ secretary_name = "Анастасия"

label coworkers_meeting:
    scene bg corridor
    story "У двери меня ждала уже знакомая мне секретарша. Как только я покинул пределы кабинета, дверь сразу бесшумно притворилась. Замок, закрываясь, издал едва уловимый щелчок."
    story "Моя проводница устремилась в даль коридора, я поспешил вслед за ней."

    menu:
        "Познакомится с Анастасией поближе":
            show secretary
            semen "Похоже, во всей суете мы с вами не успели познакомиться. Я до сих пор не знаю, как к вам обращаться."
            secretary "Ах, конечно! Вас визит был столь ожидаем, что я совсем забыла о правилах этикета. Меня зовут Анастасия, можете называть меня просто Настя, и давайте перейдем на \"ты\" все-таки мы с вами почти одного возраста."
            semen "Хорошо! Как приятно в такой напряженной обстановке встретить столь милого человека..."
            secretary "Развел Павел Андреевич не показался тебе милым?"
            semen "Боюсь, что мужчины не употребляют такое слово по отношению друг к другу."
            semen "Отвращения он точно не вызывает, но что-то в его доброте настораживает. К тому же, всё это короткое собеседование показалось мне очень странным."
            secretary "Павел Андреевич очень занятой человек. Его отношения к делу является ключевым фактором того, что наша компания считается флагманом IT индустрии. Он очень проницателен."
            secretary "То, что мы идем знакомить тебя с коллективом - очень хороший знак. Тебе повезло!"
            hide secretary
            $ relationship_secretary += 1
        "Молча идти в кабинет команды":
            pass

    story "За тот час, что я здесь провел, запах кофе уже перестал ощущаться. Но, когда мы подошли к назначенной двери, едкий запах кофеина буквально пронзил мой мозг. В глазах на несколько секунд помутнело."
    story "Анастасия явно заметила это и на лице её появилась едва заметная улыбка."
    story "Ритуал открытия двери повторился. Секретарша осталась в коридоре, а я вновь шагнул в неизвестность."

    scene bg office_work
    story "В кабинете явно шла активная трудовая деятельность, но как только я появился, все сразу притихли. Вновь меня осмотрели с ног до головы."
    story "По своему виду я явно не походил на кого-нибудь куратора или инвестора, поэтому обеспокоенные взгляды программистов быстро сменились на вопросительные и недоумевающие. Я поспешил представиться."
    semen "Доброе утро, меня зовут Семён, меня присоединили к вашей команде."
    story "Я остановился и стал ждать ответной реакции."
    story "Первым голос подал молодой парнишка. Он подошел ко мне, поспешил пожать руку и представиться."

    show artyom
    artyom "Привет, здесь можно отбросить формальности. Мы здесь одна семья. Меня зовут Артем."
    show fyodor at right
    show denis at left
    artyom "Человек справа от тебя - Федор, слева - Денис."
    artyom "Не стесняйся, чувствуй себя как дома!"
    story "Слова Артема подняли мне настроение. Я решил осмотреть представленных мне коллег."
    story "По их взглядам было видно, что они вовсе не разделяют оптимизма своего товарища. Денис явно потерял ко мне всякий интерес и вернулся к работе, Фёдор властно продолжал осматривать меня."
    hide artyom
    hide fyodor
    hide denis

    show fyodor
    fyodor "Тебя прислали нам на выручку? Отлично, у нас как раз есть для тебя задача."
    story "Голос Федора был тверд и явно командовал мной. Он смотрел на меня как хищник на добычу. Из всех встретившихся мне сегодня людей, он более остальных походил на руководителя."
    story "Я хотел было ответить, но Артем меня опередил."
    hide fyodor
    show fyodor at left
    show artyom at right
    story "Федор, погоди, давай сперва узнаем у нашего нового товарища какими языками .NET он владеет."

    menu:
        "Ответить нахально":
            semen "Я полный бездарь. 4 года учебы в университете списывал зачади. Знаю, что у вас здесь вся работа построена похожим образом, так что не потеряюсь!"
            story "Лицо Артема выразило недоумение. Фёдор буквально закипел от того, что кто-то в моем положении позволил себе подобную выходку."
            fyodor "Выметайся вон отсюда! Сейчас же!"
            hide fyodor
            hide artyom
            if relationship_secretary == 1:
                jump ending_2
            else:
                jump ending_1
        "Скромно, но полно рассказать о своих навыках":
            $ relationship_artyom += 1
            $ relationship_fyodor += 1
            semen "Владею уровнем Мидл по Python, С# и C++. Готов совершенствоваться."
            story "Артем посмотрел на меня с одобрением, Федору тоже явно понравилось, то что он услышал, правда он усиленно старался это не показывать."
            fyodor "«Синьоры» и «Мидлы» нас мало интересуют. При выполнении задачи станет понятно, что ты умеешь на самом деле. Садись за стол."
        "Явно преувеличивать свои заслуги":
            $ relationship_artyom += 1
            $ relationship_fyodor -= 1
            semen "Решу любой вопрос за пару мгновений. Python, C#, C++ - мне всё по плечу. В университете я был лучший на потоке. В школе сдал ЕГЭ на 300 баллов. Можете не переживать."
            story "Артема явно развеселил мой ответ, и он одобрительно хлопнул меня по плечу. На лице Федор было явное недовольство от моего бахвальства."
            Fyodor "Надеюсь, что работу ты делаешь так же хорошо, как языком метёшь. Садись за стол, перерыв скоро закончится."
    hide fyodor
    hide artyom

    scene bg desk
    story "Оказавшись за столом, я обратил внимание на Дениса, который до сих пор не проявлял никакой активности по отношению ко мне."

    menu:
        "Приступить к работе":
            pass
        "Попытаться разговорить Дениса":
            show denis
            story "Немного поразмыслив, как привлечь внимание человека за соседним столом, я решил просто обратиться к нему по имени."
            semen "Денис, ты еще не проронил не слова. Могу я тебя отвлечь от работы на некоторое время?"
            story "Денис нехотя отвел взгляд от монитора и уставился на меня как истукан."
            story "В таком положении мне было крайне сложно построить диалог. Денис явно не из тех, кто любит разговоры ни о чем."

            menu:
                "Попытаться элегантно завершить разговор":
                    semen "Не мог бы ты одолжить зарядник? Я свой дома оставил."
                    story "Денис неторопливо открыл выдвижной шкафчик своего стола и достал оттуда стандартное зарядное устройство. Через мгновение оно уже лежало передо мной."
                    story "Чтобы поддержать легенду, я полез в карман штанов, чтобы достать телефон, но по иронии судьбы его там не оказалось."
                    story "Я хотел было извиниться, но мой собеседник уже во всю набирал текст на клавиатуре, не обращая на меня никакого внимания."
                "Начать расспрашивать Дениса о всякой всячине":
                    $ relationship_denis -= 1
                    semen "Эй! Не будь таким нудным. Расскажи лучше, чем вы тут занимаетесь. Какие планы строите, какие реализуете?"
                    story "Денис поморщился от моей фразы. Немного погодя, он с определенным усилием начал выдавливать из себя слова. Было видно, что общение с новыми людьми ему явно не приносит удовольствия."
                    denis "Фёдор сейчас введет тебя в курс дела. Все разговоры о том, что не касается напрямую нашей настоящей задачи, обсудим потом."
            hide denis

label work:
    return

label ending_1:
    scene black
    story "День, о котором я так долго мечтал, закончился, похоронив мое будущее IT специалиста. Анастасия проводила меня до выхода и попрощалась со мной навсегда."
    story "Уже через несколько дней я вернулся к родителям в деревню. Силовые упражнения на воздухе укрепили мой дух и здоровье. К тому же, у меня появилось достаточно времени, чтобы переосмыслить свои жизненные цели."
    story "Мы с отцом долго вынашивали идею и спустя несколько лет открыли продуктовый магазин. Бизнес потихоньку растет, доходы тоже."
    story "Те полдня стажировки дали мне ясно понять, что нет смысла тратить свою жизнь на дело,которое не приносит тебе никакого удовольствия."
    return

label ending_2:
    scene black
    story "День, о котором я так долго мечтал, закончился, похоронив мое будущее IT специалиста. Анастасия проводила меня до выхода и оставила мне свой номер телефона."
    story "Уже через несколько дней я вернулся к родителям в деревню. Силовые упражнения на воздухе укрепили мой дух и здоровье. К тому же у меня появилось достаточно времени, чтобы переосмыслить свои жизненные цели."
    story "Мы с отцом долго вынашивали идею и спустя несколько лет открыли продуктовый магазин. Я продолжил общаться с Анастасией. Она сделала хорошую карьеру в компании пройдя путь от секретарши до директора."
    story "С её поддержкой за весьма скромную плату я внедрил в наш семейный бизнес инновационные технологии, которые увеличивали нашу прибыль в геометрической прогрессии. Один магазин разросся до сети. Сейчас в наших планах выйти на международный рынок."
    story "Те полдня стажировки дали мне ясно понять, что нет смысла тратить свою жизнь на дело, которое не приносит тебе никакого удовольствия."
    return
