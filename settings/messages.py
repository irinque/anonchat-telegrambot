from config import BOT_NAME, RULES

message_ban = "*🤡 Администратор выдал вам бан!*\nНа вас поступила жалоба(ы), и на основе вердикта администратора доступ к боту *прекращен*."
message_registration = "*🚀 Сначала зарегистрируйтесь!*\nДля этого прожмите /start и подтвердите ознакомление с *правилами пользования!*"
message_error = "*❌ Ничего не выйдет!*\nВы не состоите в чате, а также не находитесь в очереди."
message_ticket = "*N%s*\n*📝 Пришла жалоба:*\n- Ответчик: %s\n- Причина: %s\n- Сообщения ответчика: %s"

message_start_exists = "*👀 Рад вашему возвращению!*\nНе переживайте, я внес вас в базу еще в первую встречу, вам доступен весь функционал!"
message_start_firstvisit = "*👋 Привет, я %s*!\nИспользуя чат со мной, вы можете поговорить со случайным пользователем абсолютно анонимно!\n\nУ меня предусмотрены *правила*, нарушение которых приведет к *блокировке*. Чтобы *продолжить работу* со мной - необходимо подтвердить *ознакомление с правилами использования*.\n\n[Правила использования бота %s](%s)" % (BOT_NAME, BOT_NAME, RULES)

message_menu_success = "*📡 Выдал вам меню управления ботом!*\n*🔎 Поиск* - Поиск собеседника.\n*⛔ Стоп* - Завершение разговора/Выход из поиска.\n*👀 Профиль* - Ваш профиль и статистика."

message_search_queue = "*⌛ Вы первый в очереди!*\nНичего страшного, как только кто-то начнет поиск - я вас соединю. *Нужно немного подождать!*"
message_search_queue_duplicated = "*⛔ Вы уже в очереди!*\nПонимаю, что вам нетерпится пообщаться, но я уже *подбираю* вам собеседника!"
message_search_session_started = "*🔔 Подключили вас к собеседнику!*\nВсе что вы напишите в чат боту - ваш собеседник увидит."
message_search_session_duplicated = "*⛔ Вы уже в чате с собеседником!*\nСначала завершите разговор с этим собеседником, чтобы искать нового!"
message_search_session_complaint = "*🤠 Спасибо за содействие!*\nВаша жалоба отправлена, она будет рассмотрена нашим администратором в ближайшее время."

message_stop_session_ended = "*🔕 Отключил вас от собеседника!*\nТеперь ваши сообщения видны только боту."
message_stop_session_ended_byinterlocutor = "*🔕 Собеседник отключился!*\nТеперь ваши сообщения видны только боту."
message_stop_queue_removed = "*🚧 Убрал вас из очереди*\nЖду вас снова!"

message_profile_normal = "*📊 Данные Профиля:*\n- *ID:* %s\n- *Общался раз:* %s\n- *Регистрация:* %s\n- *Статус:* Пользователь"
message_profile_banned = "*📊 Данные Профиля:*\n- *ID:* %s\n- *Общался раз:* %s\n- *Регистрация:* %s\n- *Статус:* Забанен"
message_profile_admin = "*📊 Данные Профиля:*\n- *ID:* %s\n- *Общался раз:* %s\n- *Регистрация:* %s\n- *Статус:* Администратор\n- *Забанил:* %s"

message_rules_accept = "*✅ Доступ выдан!*\nВы подтвердили ознакомление с правилами, теперь вы *можете пользоваться* всеми функциями бота."