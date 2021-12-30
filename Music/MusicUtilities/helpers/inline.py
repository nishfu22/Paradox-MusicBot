from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)
from Music import BOT_NAME
from Music.config import GROUP, CHANNEL

def play_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="Support​​", url=f"https://t.me/{GROUP}"),
            InlineKeyboardButton(text="Menu", callback_data=f"other {videoid}|{user_id}"),
        ],
        [      
               InlineKeyboardButton(text="Close", callback_data=f"close"),
        ],
    ]
    return buttons


def others_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumevc2"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausevc2"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipvc2"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopvc2"),
        ],
        [
            InlineKeyboardButton(text="➕ Add Your List​", callback_data=f'playlist {videoid}|{user_id}'),
            InlineKeyboardButton(text="➕ Add Group List​", callback_data=f'group_playlist {videoid}|{user_id}'),
        ],
        [
            InlineKeyboardButton(
                text="⬇️ Unduh Audio", callback_data=f"gets audio|{videoid}|{user_id}"
            ),
            InlineKeyboardButton(
                text="⬇️ Unduh Video", callback_data=f"gets video|{videoid}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="Tutup", callback_data=f"close2"),
        ],
    ]
    return buttons


play_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("▶️", callback_data="resumevc"),
            InlineKeyboardButton("⏸️", callback_data="pausevc"),
            InlineKeyboardButton("⏭️", callback_data="skipvc"),
            InlineKeyboardButton("⏹️", callback_data="stopvc"),
        ],
        [InlineKeyboardButton("Tutup", callback_data="close")],
    ]
)


def audio_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumevc2"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausevc2"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipvc2"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopvc2"),
        ],
        [InlineKeyboardButton(text="Tutup", callback_data="close2")],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1️⃣", callback_data=f"Music2 {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2️⃣", callback_data=f"Music2 {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3️⃣", callback_data=f"Music2 {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4️⃣", callback_data=f"Music2 {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5️⃣", callback_data=f"Music2 {ID5}|{duration5}|{user_id}"
            ),
        ],
        [InlineKeyboardButton(text="➡️", callback_data=f"popat 1|{query}|{user_id}")],
        [
            InlineKeyboardButton(
                text="Tutup", callback_data=f"ppcl2 smex|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6️⃣", callback_data=f"Music2 {ID6}|{duration6}|{user_id}"
            ),
            InlineKeyboardButton(
                text="7️⃣", callback_data=f"Music2 {ID7}|{duration7}|{user_id}"
            ),
            InlineKeyboardButton(
                text="8️⃣", callback_data=f"Music2 {ID8}|{duration8}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="9️⃣", callback_data=f"Music2 {ID9}|{duration9}|{user_id}"
            ),
            InlineKeyboardButton(
                text="🔟", callback_data=f"Music2 {ID10}|{duration10}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="⬅️", callback_data=f"popat 2|{query}|{user_id}"),
        ],
        [InlineKeyboardButton(text="Tutup", callback_data=f"ppcl2 smex|{user_id}")],
    ]
    return buttons


def personal_markup(link):
    buttons = [
        [InlineKeyboardButton(text="Tonton Di YouTube", url=f"{link}")],
        [InlineKeyboardButton(text="Tutup", callback_data=f"close2")],
    ]
    return buttons


start_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "📚 Daftar Perintah 📚", url="https://telegra.ph/ᴇʟグー-12-30"
            )
        ],
        [InlineKeyboardButton("Tutup", callback_data="close2")],
    ]
)

confirm_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Ya", callback_data="cbdel"),
            InlineKeyboardButton("Tidak", callback_data="close2"),
        ]
    ]
)

confirm_group_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Ya", callback_data="cbgroupdel"),
            InlineKeyboardButton("Tidak", callback_data="close2"),
        ]
    ]
)

close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Tutup", callback_data="close2")]]
)

play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "➕ User Playlist​", callback_data="P_list"
                    ),
                    InlineKeyboardButton(
                        "➕ Group Playlist​​", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Tutup​", callback_data="close2"
                    )
                ]
            ]
        )

def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"Groups", callback_data=f'play_playlist {user_id}|group'),
            ],
            [
                InlineKeyboardButton(text=f"{user_name[:8]}", callback_data=f'play_playlist {user_id}|personal'),
            ],
            [
                InlineKeyboardButton(text="Tutup​", callback_data="close2")              
            ],
        ]
    return buttons


def start_pannel():
    if not CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 Setting", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if not CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 Setting", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Support", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Channel", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Channel", url=f"https://t.me/{CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="✨ Support", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons


def private_panel():
    if not CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if not CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Support", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}*", buttons
    if CHANNEL and not GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Channel", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {BOT_NAME}**", buttons
    if CHANNEL and GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    "➕ Add Me To Your Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ Channel", url=f"https://t.me/{CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="✨ Support", url=f"https://t.me/{GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Audio Quality", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Audio Volume", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized User", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Close", callback_data="close"),
        ],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset Audio Volume 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Low Vol", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Medium Vol", callback_data="MV"),
        [
            InlineKeyboardButton(text="🔊 High Vol", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Amplified Vol", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Costume Volume 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Back", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 Costume Volume 🔼", callback_data="AV")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Authorized User List", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Back", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Back", callback_data="settingm")],
    ]
    return f"🔧  **{BOT_NAME} Settings**", buttons


stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot Stats", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot Stats", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot Stats", callback_data=f"bot_stats"
            ),            
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Storage Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Assistant Stats", callback_data=f"assis_stats"
            )
        ],
    ]
)


stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="System Stats", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="General Stats", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bot Stats", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="General Stats", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ɢᴇᴛᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
