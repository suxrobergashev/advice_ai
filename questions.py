import random
import statistics
from difflib import SequenceMatcher

Data = {
    "Sizga o'qish yoki sport bilan shug'ullanish ko'proq yoqadimi? Nega?": {
        "O'qish yoqadi, chunki bilim olishni yaxshi ko'raman.": "O'qishga ko'proq qiziqadigan",
        "O'qish menga ko'proq yoqadi, chunki yangi bilimlarni o'rganish va o'zimni rivojlantirishni yaxshi ko'raman": "O'qishga ko'proq qiziqadigan",
        "O'qish orqali o'zim uchun ko'proq imkoniyatlar yarataman va hayotda muvaffaqiyatga erishishni xohlayman.": "O'qishga ko'proq qiziqadigan",
        "Menga ilmiy tadqiqotlar va kitob o'qish yoqadi, chunki bu men uchun qiziqarli va ma'lumotli bo'ladi.": "O'qishga ko'proq qiziqadigan",

        "Sport bilan shug'ullanish yoqadi, chunki bu menga energiya beradi.": "Sportga ko'proq qiziqadigan",
        "Sport bilan shug'ullanish menga ko'proq yoqadi, chunki jismoniy faollikdan zavq olaman va energiya to'playman.": "Sportga ko'proq qiziqadigan",
        "Sport meni sog'lom va baquvvat qiladi, shuningdek, raqobatlashishni yaxshi ko'raman.": "Sportga ko'proq qiziqadigan",
        "Men jamoaviy sport turlarini yaxshi ko'raman, chunki bu do'stlar bilan birga ishlash va muvaffaqiyatga erishish imkonini beradi.": "Sportga ko'proq qiziqadigan",

        "Ikkalasini ham yaxshi ko'raman, chunki o'qish orqali bilim olish va sport bilan shug'ullanish orqali sog'lig'imni saqlash muhim deb hisoblayman.": "Sportga va O'qishga qiziqadigan",
        "O'qish va sportni teng ravishda qilishga harakat qilaman, chunki ikkalasi ham o'z rivojlanishim uchun kerak.": "Sportga va O'qishga qiziqadigan",
        "Bu savolga aniq javob berolmayman, chunki ikkisini ham o'zimga kerakli deb hisoblayman.": "Neytral va ehtiyotkor",
        "Vaziyatga qarab o'qish yoki sportga qiziqishim o'zgaradi.": "Neytral va ehtiyotkor",
    },
    "Biror yangi narsani sinab ko'rishga tayyormisiz yoki ehtiyotkormisiz ?": {
        "Tayyor, har doim yangi narsalarni sinab ko'rishga intilaman.": "Yangi narsalarni sinab ko'rishga tayyor",
        "Men doim yangi narsalarni sinab ko'rishga tayyorman, chunki o'zimni rivojlantirishni va yangi tajribalarni yaxshi ko'raman.": "Yangi narsalarni sinab ko'rishga tayyor",
        "Yangi imkoniyatlarni o'rganishni qiziqarli deb bilaman, bu menga ko'proq bilim va ko'nikmalar beradi.": "Yangi narsalarni sinab ko'rishga tayyor",
        "Har qanday yangi tajriba hayotimda yangi yo'llarni ochadi, shuning uchun o'zimni hech qachon cheklamayman.": "Yangi narsalarni sinab ko'rishga tayyor",

        "Yangi narsalarni sinashdan oldin u haqda yaxshilab o'ylab ko'raman, chunki xatolardan qo'rqaman yoki zarar ko'rishni istamayman.": "sinchkov va xavf-xatarlarni oldindan ko'ra oladigan",
        "Men har qanday yangi narsa bilan ehtiyot bo'laman, chunki qaysidir tajribalar o'z oqibatlarini oldindan aytish qiyin": "sinchkov va xavf-xatarlarni oldindan ko'ra oladigan",
        "O'zimni ishonchli his qilmaguncha, ehtiyotkor bo'laman va yangi narsalarni darhol sinab ko'rmayman.": "sinchkov va xavf-xatarlarni oldindan ko'ra oladigan",
        "Ehtiyotkor, avval o'rganib olishni afzal ko'raman.": "sinchkov va xavf-xatarlarni oldindan ko'ra oladigan",

        "Ba'zan yangi narsalarni sinab ko'raman, lekin har doim xavflar va imkoniyatlarni hisobga olaman.": "muvozanatni saqlay oladigan va har qanday vaziyatda oqilona harakat qiladigan",
        "Yangi narsalarni sinashga tayyorman, lekin ehtiyotkorlik bilan harakat qilaman, chunki har qanday yangilik foydali bo'lmasligi mumkin.": "muvozanatni saqlay oladigan va har qanday vaziyatda oqilona harakat qiladigan",
        "Sinashga tayyorman, lekin qachon ehtiyot bo'lish kerakligini bilaman": "muvozanatni saqlay oladigan va har qanday vaziyatda oqilona harakat qiladigan",
    },
    "Qiyin vaziyatlarda qanday harakat qilasiz? Sabrlimi yoki tez asabiylashasizmi?": {
        "Sabrliman, sabr-toqat bilan muammoni hal qilishga harakat qilaman.": "stressli holatlarda ham o'zini yo'qotmaydigan, tinch va sabrli",
        "Qiyin vaziyatlarda asabiylashmayman va tinchlanishga harakat qilaman. Sabrlilik bilan vaziyatni tahlil qilishga urinaman.": "stressli holatlarda ham o'zini yo'qotmaydigan, tinch va sabrli",
        "Qiyin sharoitda sabr qilishga ishonaman, chunki muammolar vaqt o'tishi bilan o'z-o'zidan hal bo'lishi mumkin.": "stressli holatlarda ham o'zini yo'qotmaydigan, tinch va sabrli",
        "Qiyin vaziyatlarda avvaliga tinchlanib, keyin nima qilish kerakligini o'ylayman.": "stressli holatlarda ham o'zini yo'qotmaydigan, tinch va sabrli",

        "Tez asabiylashaman, lekin keyin tinchlanishga harakat qilaman.": "stressli vaziyatlarda tezda asabiylashishga moyillik bor",
        "Tez asabiylashaman, chunki qiyin vaziyatlarda o'zimni nazorat qilish qiyin bo'ladi.": "stressli vaziyatlarda tezda asabiylashishga moyillik bor",
        "Qiyin vaziyatda ko'pincha stressga berilaman va bu meni tezda asabiylashtiradi.": "stressli vaziyatlarda tezda asabiylashishga moyillik bor",
        "Qiyin vaziyatlarda juda asabiy bo'laman, chunki hamma narsa nazoratimdan chiqib ketayotgandek tuyuladi.": "stressli vaziyatlarda tezda asabiylashishga moyillik bor",

        "Odatda sabr qilaman, lekin juda og'ir bo'lsa, asabiylashishim mumkin.": "qiyin vaziyatlarda muvozanatni saqlashga urinadigan",
        "Qiyin vaziyatlarda harakatlarim holatga bog'liq. Ba'zida sabr qilaman, ba'zida esa asabiylashib ketishim mumkin.": "qiyin vaziyatlarda muvozanatni saqlashga urinadigan",
        "Avvaliga sabr qilib harakat qilaman, lekin agar vaziyat juda yomonlashsa, asabiylashib qolishim mumkin.": "qiyin vaziyatlarda muvozanatni saqlashga urinadigan",

        "Har doim muammoni hal qilish uchun chuqur nafas olib, vaziyatni tahlil qilishga harakat qilaman.": "vaziyatni tahlil qilish orqali hissiyotlarini nazorat qilishga qodir",
        "Asabiylashmaslikka harakat qilaman va vaziyatni o'ylab, tinchlik bilan hal qilish yo'llarini izlayman.": "vaziyatni tahlil qilish orqali hissiyotlarini nazorat qilishga qodir",
        "Og'ir sharoitlarda salbiy his-tuyg'ularni nazorat qilishni o'rganishga harakat qilaman.": "vaziyatni tahlil qilish orqali hissiyotlarini nazorat qilishga qodir"

    },
    "Do'stlaringiz orasida siz ko'proq tinglaysizmi yoki yetakchilik qilasizmi ?": {
        "Ko'proq tinglaydigan, do'stlarimning fikrlarini eshitishni yaxshi ko'raman.": "g'amxo'r va boshqalarni tushunishga moyil",
        "Men ko'proq tinglashni afzal ko'raman, chunki do'stlarimning fikrlari va hissiyotlarini bilishni xohlayman.": "g'amxo'r va boshqalarni tushunishga moyil",
        "Odatda ko'proq tinglayman, do'stlarim o'z fikrlarini ifoda etishlari uchun ularga imkon beraman.": "g'amxo'r va boshqalarni tushunishga moyil",
        "Do'stlarimni diqqat bilan tinglayman, chunki har bir insonning gapirishga arziydigan narsa bor.": "g'amxo'r va boshqalarni tushunishga moyil",

        "Yetakchilik qiladigan, har doim fikrlarimni bildirishga harakat qilaman.": "tabiatan yetakchi va boshqalarga yo'l ko'rsatishni yaxshi ko'radigan",
        "Do'stlar orasida ko'proq yetakchilik qilaman, chunki ko'pchilik mas'uliyatni o'z zimmamga olishimni kutadi.": "tabiatan yetakchi va boshqalarga yo'l ko'rsatishni yaxshi ko'radigan",
        "Odatda men yetakchi rolni olaman, chunki ko'pincha qarorlarni tezroq va samaraliroq qabul qilishim mumkin.": "tabiatan yetakchi va boshqalarga yo'l ko'rsatishni yaxshi ko'radigan",
        "Do'stlarim orasida yetakchilik qilishni yaxshi ko'raman, chunki ularga yordam berish va yo'l ko'rsatishni xohlayman.": "tabiatan yetakchi va boshqalarga yo'l ko'rsatishni yaxshi ko'radigan",

        "Ba'zida tinglayman, ba'zida esa yetakchilik qilaman. Bu vaziyatga bog'liq.": "moslashuvchan va vaziyatga qarab o'z rolini o'zgartirishga qodir",
        "Do'stlarimni tinglashni yaxshi ko'raman, lekin kerak bo'lganda yetakchilik qilishdan ham cho'chimayman.": "moslashuvchan va vaziyatga qarab o'z rolini o'zgartirishga qodir",
        "Ko'pincha tinglashni afzal ko'raman, lekin do'stlarimning qaror qabul qilishlariga yordam berish uchun yetakchilik qilishim mumkin.": "moslashuvchan va vaziyatga qarab o'z rolini o'zgartirishga qodir",

        "O'zimni tinglovchi ham, yetakchi ham deb hisoblamayman, lekin doimo jamoaviy ishlashga harakat qilaman.": "jamoada hamma teng ishtirok etishini xohlaydigan",
        "Ba'zida yetakchi bo'laman, lekin ko'pincha boshqalar bilan birga qaror qabul qilishni afzal ko'raman.": "jamoada hamma teng ishtirok etishini xohlaydigan",
        "Har bir insonning fikrini tinglashni va hamkorlikda ishlashni yaxshi ko'raman.": "jamoada hamma teng ishtirok etishini xohlaydigan",
    },
    "Biror xatoni ko'rsangiz, buni aytasizmi yoki sukut saqlaysizmi?": {
        "Ayta bilaman, muammolarni hal qilishda ochiq bo'lish kerak deb o'ylayman.": "ochiq, halol va haqiqatparvar",
        "Nimadir noto'g'ri bo'lsa, albatta aytaman. To'g'ridan-to'g'ri gapirishni yaxshi ko'raman.": "ochiq, halol va haqiqatparvar",
        "Agar adolatsizlik yoki noto'g'ri narsa ko'rsam, bu haqda gapirish kerak deb o'ylayman.": "ochiq, halol va haqiqatparvar",
        "Haqiqatan ham, noto'g'ri narsalarni aytishga odatlanganman, chunki adolatli bo'lish muhim.": "ochiq, halol va haqiqatparvar",

        "Sukut saqlayman, ba'zida muammolarni hal qilishni afzal ko'raman.": "mojarolarni yoqtirmaydigan va o'z fikrini ochiq aytishdan tortinadigan",
        "Ko'p hollarda sukut saqlashni afzal ko'raman, chunki mojarolardan qochishga harakat qilaman.": "mojarolarni yoqtirmaydigan va o'z fikrini ochiq aytishdan tortinadigan",
        "Agar kimdir noto'g'ri ish qilsa, har doim aytmasligim mumkin, chunki buni o'zim uchun katta muammo deb bilmayman.": "mojarolarni yoqtirmaydigan va o'z fikrini ochiq aytishdan tortinadigan",
        "Noto'g'ri narsani sezsam ham, ko'pincha sukut saqlayman, chunki boshqalarning fikrini hurmat qilaman.": "mojarolarni yoqtirmaydigan va o'z fikrini ochiq aytishdan tortinadigan",

        "Ba'zi hollarda aytaman, ba'zi hollarda esa sukut saqlayman, vaziyatga bog'liq.": "Vaziyatga qarab harakat qiladigan",
        "Agar muammo jiddiy bo'lsa, aytaman, lekin kichik xatolar uchun boshqalarga imkon berishni afzal ko'raman.": "Vaziyatga qarab harakat qiladigan",
        "Agar noto'g'ri narsa meni bevosita ta'sir qilsa, aytaman, aks holda sukut saqlashim mumkin.": "Vaziyatga qarab harakat qiladigan",

        "Nimadir noto'g'ri bo'lsa, uni to'g'ri tarzda aytishga harakat qilaman, shunchaki tanqid qilmayman.": "Samarali muloqotni afzal ko'radigan",
        "Noto'g'ri narsalarni gapirishim mumkin, lekin odatda yechim topishga harakat qilaman.": "Samarali muloqotni afzal ko'radigan",
        "Agar narsa noto'g'ri bo'lsa, buni muloyimlik bilan aytaman, chunki mojarolarni avj oldirishni xohlamayman.": "Samarali muloqotni afzal ko'radigan"
    },
    "Bo'sh vaqtingiz bo'lganda, ko'proq nima bilan shug'ullanishni yoqtirasiz?": {
        "Sport bilan shug'ullanishni yoqtiraman, yugurish yoki sport zaliga boraman.": "faol hayot tarzini tanlagan",
        "Do'stlarim bilan ko'proq vaqt o'tkazishni yaxshi ko'raman, ular bilan birgalikda o'yinlar o'ynashni yoki sayr qilishni yoqtiraman.": "faol hayot tarzini tanlagan",
        "Tabiatda sayr qilishni yoki velosipedda yurishni yaxshi ko'raman.": "faol hayot tarzini tanlagan",

        "Kitob o'qishni yaxshi ko'raman, ayniqsa yangi bilimlarni olishdan zavq olaman.": "Tinch va ijodiy mashg'ulotlarni afzal ko'radigan",
        "Musiqa tinglash yoki chizishni yaxshi ko'raman.": "Tinch va ijodiy mashg'ulotlarni afzal ko'radigan",
        "Film tomosha qilish yoki seriallar ko'rishni yoqtiraman.": "Tinch va ijodiy mashg'ulotlarni afzal ko'radigan",

        "Texnologiya va kompyuter o'yinlariga ko'proq qiziqaman, bo'sh vaqtimda yangi o'yinlarni o'ynayman yoki dasturlashni o'rganaman.": "Texnologiya va bilim olishni yaxshi ko'radigan",
        "Internetda yangi narsalarni o'rganishni, videolar va hujjatli filmlarni ko'rishni yoqtiraman.": "Texnologiya va bilim olishni yaxshi ko'radigan",
        "Texnologiya yangiliklarini kuzataman yoki o'zimni qiziqtirgan loyihalar ustida ishlayman.": "Texnologiya va bilim olishni yaxshi ko'radigan",

        "Do'stlar bilan uchrashish va suhbatlashishni yaxshi ko'raman.": "Ijtimoiy va jamoaviy faoliyatni afzal ko'radigan",
        "Oila bilan vaqt o'tkazishni afzal ko'raman, ular bilan birga o'yinlar o'ynashni yoki sayrga chiqishni yoqtiraman.": "Ijtimoiy va jamoaviy faoliyatni afzal ko'radigan",
        "Jamoat ishlari yoki ko'ngillilik ishlarida qatnashishni yaxshi ko'raman.": "Ijtimoiy va jamoaviy faoliyatni afzal ko'radigan",

        "Shaxsiy rivojlanish va meditatsiya bilan shug'ullanaman.": "O'zingiz bilan shug'ullanishni yoqtiradigan",
        "O'zimni ko'proq o'ylab, kelajakdagi rejalarga tayyorlanishni yaxshi ko'raman.": "O'zingiz bilan shug'ullanishni yoqtiradigan",
        "O'zimni yaxshi his qilish uchun fitness bilan shug'ullanaman": "O'zingiz bilan shug'ullanishni yoqtiradigan"
    },
    "Ota-onangiz yoki yaqinlaringiz sizni qanday tariflashadi ?": {
        "Meni ishonchli va mas'uliyatli deb o'ylashadi, chunki men har doim va'dalarimni bajarishga harakat qilaman.": "Mas'uliyatli va ishonchli",
        "Ota-onam meni har doim o'z maqsadlariga erishadigan va tirishqoq inson deb bilishadi.": "Mas'uliyatli va ishonchli",
        "Yaqinlarim meni mas'uliyatli va ularga yordam berishga tayyor odam sifatida ko'rishadi.": "Mas'uliyatli va ishonchli",

        "Ota-onam meni mehribon va qo'llab-quvvatlovchi inson deb bilishadi, chunki men har doim ularga yordam berishga harakat qilaman.": "Mehribon va qo'llab-quvvatlovchi",
        "Yaqinlarim meni halol va ularni tinglaydigan inson sifatida ko'rishadi.": "Mehribon va qo'llab-quvvatlovchi",
        "Oila a'zolarim meni juda g'amxo'r va boshqalarga mehribonlik bilan munosabatda bo'lishimni yaxshi ko'rishadi.": "Mehribon va qo'llab-quvvatlovchi",

        "Ota-onam meni bilimli va o'qishga qiziqish bilan qaraydigan inson deb bilishadi.": "O'qimishli va tirishqoq",
        "Meni har doim tirishqoq deb hisoblashadi, chunki men doimo o'z ustimda ishlashga intilaman.": "O'qimishli va tirishqoq",
        "Yaqinlarim meni bilim va o'rganish uchun intilishim tufayli qadrlashadi.": "O'qimishli va tirishqoq",

        "Yaqinlarim meni ijodiy va o'ziga xos deb bilishadi, chunki men yangi g'oyalarni ishlab chiqishdan zavq olaman.": "Ijodiy va o'ziga xos fazilatlar bilan ajralib turadigan",
        "Ota-onam meni doim boshqalardan ajralib turadigan fazilatlarim tufayli yaxshi ko'rishadi.": "Ijodiy va o'ziga xos fazilatlar bilan ajralib turadigan",
        "Meni ijodiy fikrlashim va noyob yondashuvlarim uchun qadrlashadi.": "Ijodiy va o'ziga xos fazilatlar bilan ajralib turadigan",

        "Ota-onam meni jamoatchilikda faol va boshqalarga yordam berishga qiziqish bilan qaraydigan inson deb bilishadi.": "Jamoat va ijtimoiy faoliyatni yoqtiradigan",
        "Meni ko'ngillilik ishlariga qiziqishim va jamiyatda o'z hissamni qo'shishim tufayli hurmat qilishadi.": "Jamoat va ijtimoiy faoliyatni yoqtiradigan",
        "Yaqinlarim meni jamiyatga foyda keltiradigan ishlar qiladigan deb o'ylashadi.": "Jamoat va ijtimoiy faoliyatni yoqtiradigan"
    },
    "Muammolarnigizni o'zingiz hal qilishga urinasizmi yoki yordam so'rashni afzal ko'rasizmi?": {
        "Odatda muammolarni o'zim hal qilishga harakat qilaman, chunki bu men uchun tajriba va rivojlanish imkoniyatidir.": "Mustaqil va o'ziga ishongan",
        "Men avval muammoni o'zim hal qilishni afzal ko'raman, faqat qiyin bo'lsa yordam so'rayman.": "Mustaqil va o'ziga ishongan",
        "Har doim o'zimni sinab ko'rishga intilaman va faqat muammo katta bo'lsa, yordam so'rayman.": "Mustaqil va o'ziga ishongan",

        "Agar muammo juda qiyin bo'lsa, yordam so'rashdan uyalmayman, chunki bu yanada tezroq va samaraliroq yechim topish uchun muhim.": "Yordam so'rashga tayyor va hamkorlikni qadrlaydigan",
        "Yordam so'rashni o'rganish men uchun muhim, chunki boshqalarning tajribasi ko'p narsalarni hal qilishi mumkin.": "Yordam so'rashga tayyor va hamkorlikni qadrlaydigan",
        "Men hamkorlikni qadrlayman va boshqalarning fikrlarini o'rgangan holda muammolarni hal qilaman.": "Yordam so'rashga tayyor va hamkorlikni qadrlaydigan",

        "Avval muammoni o'zim hal qilishga harakat qilaman, lekin kerak bo'lsa yordam so'rashga ham tayyorman.": "vaziyatga qarab harakat qiladigan va moslashuvchan",
        "Agar vaqt yoki bilim yetarli bo'lmasa, yordam so'rashdan qo'rqmayman, chunki bu men uchun eng to'g'ri qaror bo'ladi.": "vaziyatga qarab harakat qiladigan va moslashuvchan",
        "Muammoning murakkabligiga qarab o'zim hal qilaman yoki yordam so'rayman.": "vaziyatga qarab harakat qiladigan va moslashuvchan",

        "Men odatda yordam so'rashni afzal ko'raman, chunki boshqalarning fikri muammolarni hal qilishda foydali bo'lishi mumkin.": "yordam so'rashga ko'proq moyilligi bor",
        "Yordam so'rash men uchun muhim, chunki bu menga tezroq va osonroq yechim topishga yordam beradi.": "yordam so'rashga ko'proq moyilligi bor",
        "Men ko'pincha yordam so'rayman, chunki bu ko'proq tajriba va bilim olishga imkon beradi.": "yordam so'rashga ko'proq moyilligi bor",
    },
    "Biror maqsad qo‘yganingizda, uni oxirigacha yetkazasizmi yoki yarim yo‘lda to‘xtaysizmi?": {
        "Men qo'ygan maqsadlarimga erishish uchun oxirigacha boraman, hatto qiyinchiliklar bilan yuzma-yuz kelsam ham.": "qat'iy va irodali",
        "Har doim maqsadimni oxirigacha yetkazishga harakat qilaman, chunki men o'zimga berilgan va'dalarni bajara olishimni istayman.": "qat'iy va irodali",
        "Maqsadlarimga qat'iylik bilan qarayman va ularni amalga oshirish uchun bor kuchimni sarflayman.": "qat'iy va irodali",

        "Ba'zan maqsadlarimga erishish yo'lida qiyinchiliklarga duch kelaman va o'zimni tahlil qilib, yana davom etishga harakat qilaman.": "o'z-o'zini baholash va muammolarni aniqlashdagi qobiliyati bor",
        "Agar maqsadga erishishda qiyinchilik bo'lsa, to'xtab, fikr yuritaman va keyin yana harakat qilaman.": "o'z-o'zini baholash va muammolarni aniqlashdagi qobiliyati bor",
        "Maqsadlarimni oxirigacha yetkazishga harakat qilaman, lekin ba'zida zarur bo'lsa, to'xtab o'ylab olaman.": "o'z-o'zini baholash va muammolarni aniqlashdagi qobiliyati bor",

        "Agar maqsadimga yetishish qiyin bo'lsa, men uni oxirigacha davom ettirishga harakat qilaman, lekin zarur bo'lsa, to'xtab fikr yuritaman.": "moslashuvchan va vaziyatga qarab harakat qiladigan",
        "Men maqsadlarni oxiriga yetkazishga intilaman, lekin muammolar bilan to'qnashganda zarur o'zgarishlar kiritishdan cho'chimayman.": "moslashuvchan va vaziyatga qarab harakat qiladigan",
        "Maqsadlarimga erishish uchun qat'iyat bilan harakat qilaman, lekin qiyinchiliklar paydo bo'lsa, qanday qilib davom etishni o'ylab ko'raman.": "moslashuvchan va vaziyatga qarab harakat qiladigan",

        "Agar maqsad qiyin bo'lsa, ba'zida to'xtashga qaror qilaman va yangi maqsadlar qo'yaman.": "muammolar paydo bo'lganda o'z maqsadlarini o'zgartirishga tayyor",
        "Men ba'zan maqsadimni davom ettirishni qiyin deb bilsam, shunchaki to'xtayman va boshqa narsalarga e'tibor beraman.": "muammolar paydo bo'lganda o'z maqsadlarini o'zgartirishga tayyor",
        "Agar maqsadga erishish juda qiyin bo'lsa, men ba'zida uni tark etishga qaror qilaman.": "muammolar paydo bo'lganda o'z maqsadlarini o'zgartirishga tayyor",
    },
    "Biror kishi bilan tortishganingizda, birinchi bo‘lib kechirim so‘raysizmi?": {
        "Men birinchi bo'lib kechirim so'rashga harakat qilaman, chunki munosabatlarni saqlash men uchun muhim.": "munosabatlarga bo'lgan yondashuvchanlik va kechirimli",
        "Agar tortishuvda o'z hissiyotlarimni boshqarishni bilsam, men kechirim so'rashga tayyorman.": "munosabatlarga bo'lgan yondashuvchanlik va kechirimli",
        "Men tortishuvdan so'ng, tezda kechirim so'rashni afzal ko'raman, chunki bu o'zaro tushunishni yaxshilaydi.": "munosabatlarga bo'lgan yondashuvchanlik va kechirimli",

        "Men avvalgi vaziyatni baholayman va kechirim so'rashim kerakmi yoki yo'qligini tushunishga harakat qilaman.": "o'z nuqtai nazarini aniqlashga harakat qiladigan",
        "Agar meni xato qilganimni his qilsam, kechirim so'rayman, lekin ba'zan o'z nuqtai nazarimni himoya qilaman.": "o'z nuqtai nazarini aniqlashga harakat qiladigan",
        "Meni shunchaki ayblagan kishi bo'lsa, kechirim so'rashda ehtiyot bo'lishni afzal ko'raman.": "o'z nuqtai nazarini aniqlashga harakat qiladigan",

        "Men birinchi bo'lib kechirim so'ramayman, chunki ba'zida kishi o'z xatolarini tan olishi kerak deb o'ylayman.": "mustaqil fikrlaydigan va o'z nuqtai nazarini himoya qiladigan",
        "Agar tortishuvda haqiqatan ham haqligimni his qilsam, kechirim so'rashni o'zimga xos deb bilmayman.": "mustaqil fikrlaydigan va o'z nuqtai nazarini himoya qiladigan",
        "Men ba'zida kechirim so'rashdan qochaman, chunki o'z pozitsiyamni saqlab qolishni afzal ko'raman.": "mustaqil fikrlaydigan va o'z nuqtai nazarini himoya qiladigan",

        "Men ba'zida kechirim so'rashni osonlashtira olmayman, lekin o'z xatolarimni tan olishga harakat qilaman.": "o'z his-tuyg'ularini boshqarishda muammolari bor",
        "Agar tortishuvda boshqalarning his-tuyg'ulari bo'yicha qaror qilish qiyin bo'lsa, kechirim so'rashim kerakligini tushunaman, lekin qiyinchiliklar bor.": "o'z his-tuyg'ularini boshqarishda muammolari bor",
        "Men konfiliktni hal qilishda qiyinchiliklarga duch kelaman va shuning uchun kechirim so'rashga qaror qilmaslikka harakat qilaman.": "o'z his-tuyg'ularini boshqarishda muammolari bor",
    },
    "Ko'pchilik bilan ishlashni yoqtirasizmi yoki yolg'iz ishlashni afzal ko'rasizmi?": {
        "Men jamoaviy ishni yoqtiraman, chunki birgalikda ishlash va fikr almashish orqali ko'proq ijodiy yechimlar topamiz.": "ijtimoiy ko'nikmalari va jamoaviy ishga bo'lgan qiziqishi bor",
        "Jamoada ishlash meni rag'batlantiradi, chunki do'stlarim va hamkasblarimdan o'rganish imkoniyatim bor.": "ijtimoiy ko'nikmalari va jamoaviy ishga bo'lgan qiziqishi bor",
        "Birgalikda ishlash jarayonida ko'plab fikrlarni olish va yangi g'oyalarni yaratish qiziqarli.": "ijtimoiy ko'nikmalari va jamoaviy ishga bo'lgan qiziqishi bor",

        "Men yolg'iz ishlashni afzal ko'raman, chunki shunda o'z fikrlarimni to'liq ifodalashim va diqqatni jamlashim osonroq.": "mustaqillik va o'z-o'zini boshqarish qobiliyati bor",
        "Yolg'iz ishlaganda, vaqtimni o'zim belgilash va qiyinchiliklarga muvofiq javob berish imkoniyatim bo'ladi.": "mustaqillik va o'z-o'zini boshqarish qobiliyati bor",
        "Men ko'proq mustaqil fikr yuritishni yoqtiraman, shuning uchun yolg'iz ishlash meni qulayroq his qiladi.": "mustaqillik va o'z-o'zini boshqarish qobiliyati bor",

        "Men ko'pchilik bilan ishlashni yoqtiraman, lekin ba'zi vaziyatlarda yolg'iz ishlashni ham afzal ko'raman.": "jamoaviy ish va individual ishning afzalliklarini uyg'unlashtirishga intiladigan",
        "Jamoada ishlashni qadrlarim, lekin ba'zida o'zimga to'liq diqqatni jamlashim kerak bo'lgan vazifalar bo'ladi.": "jamoaviy ish va individual ishning afzalliklarini uyg'unlashtirishga intiladigan",
        "Agar loyiha murakkab bo'lsa, yolg'iz ishlashni afzal ko'raman, lekin boshqalardan yordam olishni ham qadrlayman.": "jamoaviy ish va individual ishning afzalliklarini uyg'unlashtirishga intiladigan",

        "Men ko'pchilik bilan ishlashga harakat qilaman, lekin ba'zida jamoada o'z fikrimni ifodalashda qiyinchiliklarga duch kelaman.": "jamoaviy ishda o'zini noqulay his qiladigan",
        "Yolg'iz ishlashni afzal ko'raman, chunki jamoa muammolariga duch kelganimda, buni boshqarish qiyin bo'ladi.": "jamoaviy ishda o'zini noqulay his qiladigan",
        "Men jamoada ishlashda noqulay his qilaman, shuning uchun ko'proq yolg'iz ishlashni afzal ko'raman.": "jamoaviy ishda o'zini noqulay his qiladigan",
    },
    "Biror muammoga duch kelsangiz, darhol uni hal qilasizmi yoki biroz ortga surasizmi?": {
        "Men muammolarni darhol hal qilishni afzal ko'raman, chunki buni kechiktirish faqat vaziyatni og'irlashtiradi.": "muammolarni tezda hal qilishga intiladigan",
        "Agar muammo paydo bo'lsa, uni tezda hal qilishga harakat qilaman, chunki bu menga ichki tinchlik beradi.": "muammolarni tezda hal qilishga intiladigan",
        "Muammolarni hal qilishda kechikish men uchun noqulay, shuning uchun darhol harakat qilaman.": "muammolarni tezda hal qilishga intiladigan",

        "Men ba'zida muammoga darhol qarshi chiqmayman, avval uning oqibatlarini o'ylab ko'raman.": "sabr-toqatli va vaziyatni baholashda ehtiyotkor",
        "Agar muammo murakkab bo'lsa, uni hal qilishdan oldin bir oz kutib turishni afzal ko'raman.": "sabr-toqatli va vaziyatni baholashda ehtiyotkor",
        "Men har doim darhol hal qilmayman, chunki ba'zida tinchlanish va fikr yuritish kerak bo'ladi.": "sabr-toqatli va vaziyatni baholashda ehtiyotkor",

        "Men muammoni darhol hal qilishga harakat qilaman, lekin ba'zan bir oz kutib turish ham foydali.": "kerak bo'lsa sabr bilan yondashadigan",
        "Agar muammo oddiy bo'lsa, tezda harakat qilaman, lekin agar murakkab bo'lsa, sabr bilan fikr yuritishga intilaman.": "kerak bo'lsa sabr bilan yondashadigan",
        "Ba'zida darhol hal qilaman, lekin qo'shimcha ma'lumot yoki vaqt kerak bo'lsa, bir oz kutaman.": "kerak bo'lsa sabr bilan yondashadigan",

        "Men ko'pincha muammolarni hal qilishda qiyinchiliklarga duch kelaman va shuning uchun darhol harakat qilmayman.": "tezda harakat qilishdan qochadigan",
        "Agar muammo paydo bo'lsa, uni hal qilishda o'z ishonchimni yo'qotganim uchun bir oz kutishim kerak.": "tezda harakat qilishdan qochadigan",
        "Men muammolarni hal qilishda noqulay his qilaman, shuning uchun ko'pincha kechikib harakat qilaman.": "tezda harakat qilishdan qochadigan",
    },
    "Ijodiy ishlarga qiziqasizmi yoki ko'proq aniq fanlar bilan shug'ullanishni yoqtirasizmi?": {
        "Men ijodiy ishlarga qiziqaman, chunki yangi g'oyalarni yaratish va ifodalash menga juda yoqadi.": "yangi g'oyalar yaratishga va o'zini ifodalashga intiladigan",
        "Rasm chizish, musiqa yaratish yoki yozuv yozish kabi ijodiy faoliyatlar menga ilhom beradi.": "yangi g'oyalar yaratishga va o'zini ifodalashga intiladigan",
        "Ijodiy jarayonlar men uchun o'z fikrlarimni ochib berish va his-tuyg'ularimni ifodalash imkonini yaratadi.": "yangi g'oyalar yaratishga va o'zini ifodalashga intiladigan",

        "Men aniq fanlarga qiziqaman, chunki ular ilmiy asoslangan va mantiqiy yechimlar taqdim etadi.": "aniq fanlarga qiziqadigan va ilmiy asoslangan yondashuvga intiladigan",
        "Matematika, fizika yoki informatika kabi fanlarni o'rganish menga juda qiziq.": "aniq fanlarga qiziqadigan va ilmiy asoslangan yondashuvga intiladigan",
        "Aniq fanlar bilan shug'ullanish menga muammolarni mantiqiy tarzda hal qilishga yordam beradi.": "aniq fanlarga qiziqadigan va ilmiy asoslangan yondashuvga intiladigan",

        "Men ijodiy ishlarga ham, aniq fanlarga ham qiziqaman; har ikkisi meni ilhomlantiradi.": "ijodiy va ilmiy yondashuvlarni birlashtirish qobiliyati bor",
        "Ijodiy g'oyalarni aniq fanlarga qo'llashni yaxshi ko'raman; masalan, muhandislikda ijodiy yechimlar ishlab chiqish.": "ijodiy va ilmiy yondashuvlarni birlashtirish qobiliyati bor",
        "O'z ijodimni ilmiy asosda rivojlantirishni afzal ko'raman, shuning uchun har ikkisini uyg'unlashtiraman.": "ijodiy va ilmiy yondashuvlarni birlashtirish qobiliyati bor",

        "Men ijodiy ishlar bilan shug'ullanishda noqulay his qilaman, lekin aniq fanlar bilan ko'proq qulayman.": "ilhom olishda qiyinchiliklarga duch keladigan va shuning uchun aniq fanlarga e'tibor beradigan",
        "Ijodiy fikrlashda qiyinchiliklarga duch kelaman, shuning uchun aniq fanlarga ko'proq e'tibor beraman.": "ilhom olishda qiyinchiliklarga duch keladigan va shuning uchun aniq fanlarga e'tibor beradigan",
        "Meni ijodiy ishlar hayajonlantiradi, lekin ko'pincha ularda muvaffaqiyatga erishish qiyin.": "ilhom olishda qiyinchiliklarga duch keladigan va shuning uchun aniq fanlarga e'tibor beradigan",
    },
    "Qanday vaziyatlarda eng ko'p asabiylashasiz?": {
        "Agar ko'p ish bo'lsa va vaqtni yetkazmasam, juda asabiylashaman.": "stressli vaziyatlarda qiyinchiliklarga duch keladigan",
        "Meni keraksiz tanqidlar yoki bahslar asabiylashtiradi, chunki men o'z fikrlarimni himoya qilishga intilaman.": "stressli vaziyatlarda qiyinchiliklarga duch keladigan",
        "Ba'zan odamlar shunchaki eshitmasalar, bu meni asabiylashtiradi.": "stressli vaziyatlarda qiyinchiliklarga duch keladigan",

        "Murakkab muammolarni hal qilishda yoki ish yukim ko'payganda asabiylashaman.": "muammolarga tez reaksiyaga ega",
        "Agar rejalashtirilgan narsalar bajarilmasa, bu meni asabiylashtiradi.": "muammolarga tez reaksiyaga ega",
        "Vaziyatlar nazoratdan chiqsa, juda asabiylashaman.": "muammolarga tez reaksiyaga ega",

        "Agar menda qiziqishim yo'q bo'lsa, menga majburan biror narsa qilishga majbur bo'lishim asabiylashtiradi.": "e'tiborni qiziqarli va muhim narsalarga qaratadigan",
        "Meni e'tiborsizlik yoki kutilmagan vaziyatlar asabiylashtiradi.": "e'tiborni qiziqarli va muhim narsalarga qaratadigan",
        "Odamlar o'zlari uchun muhim bo'lmagan narsalarga e'tibor bermaganda, men asabiylashaman.": "e'tiborni qiziqarli va muhim narsalarga qaratadigan",

        "Men ko'pincha sabr qilaman, lekin ba'zan kutilmagan vaziyatlar meni asabiylashtiradi.": "sabr-toqatli va stressni boshqarish qobiliyati bor",
        "O'z hissiyotlarimni boshqarishga harakat qilaman, lekin stressli vaziyatlar doimiy ravishda qiyinchilik tug'diradi.": "sabr-toqatli va stressni boshqarish qobiliyati bor",
        "Agar muammolar bir-biriga to'g'ri kelib qolsa, sabr-toqatim tugaydi va asabiylashaman.": "sabr-toqatli va stressni boshqarish qobiliyati bor",
    },
    "Hozirgi davrda qanday ko'nikmalar eng zarur deb o'ylaysiz?": {
        "Dasturlash va kod yozish ko'nikmalari bugungi kunda juda zarur, chunki har bir soha raqamlashtirilmoqda.": "texnologiyalarga qiziqadigan va zamonaviy ish bozoriga e'tibor beradigan",
        "Sun'iy intellekt va ma'lumotlar tahlili ko'nikmalarini o'rganish zarur deb hisoblayman.": "texnologiyalarga qiziqadigan va zamonaviy ish bozoriga e'tibor beradigan",
        "IT va texnologiyalar sohasidagi ko'nikmalar har qanday kasbda qo'llanilishi mumkin.": "texnologiyalarga qiziqadigan va zamonaviy ish bozoriga e'tibor beradigan",

        "Muloqot va jamoa bilan ishlash ko'nikmalari har doim zarur, chunki insonlar o'rtasidagi aloqalar muhim.": "soft-skills'ga va shaxsiy rivojlanishga e'tibor beradigan",
        "Qaror qabul qilish va muammolarni hal qilish ko'nikmalari zarur, chunki ish jarayonida turli vaziyatlar yuzaga keladi.": "soft-skills'ga va shaxsiy rivojlanishga e'tibor beradigan",
        "Emotsional intellekt va vaqtni boshqarish ko'nikmalari ham juda muhimdir.": "soft-skills'ga va shaxsiy rivojlanishga e'tibor beradigan",

        "Yangi til o'rganish va kommunikativ ko'nikmalarni rivojlantirish zarur deb o'ylayman.": "o'zini rivojlantiradigan va yangi imkoniyatlarni qidiradigan",
        "Kreativlik va innovatsion fikrlash ko'nikmalarini o'rganish muhim, chunki bu yangiliklarni keltiradi.": "o'zini rivojlantiradigan va yangi imkoniyatlarni qidiradigan",
        "O'z-o'zini rivojlantirish va shaxsiy brendni yaratish ko'nikmalarini ham afzal ko'raman.": "o'zini rivojlantiradigan va yangi imkoniyatlarni qidiradigan",

        "Men har qanday vaziyatda o'z ko'nikmalarimni o'zgartirishga tayyorman, chunki dunyo tez o'zgaradi.": "qiyinchiliklarga qarshi kurashish istagi bor",
        "Zamonaviy ko'nikmalarni o'rganish juda qiyin, lekin o'zgarishga tayyorman.": "qiyinchiliklarga qarshi kurashish istagi bor",
        "Muammolarga moslashish va ularni hal qilish ko'nikmalari meni har qanday holatda yordam beradi.": "qiyinchiliklarga qarshi kurashish istagi bor",
    },
    "Biror kishi sizni noto'g'ri tushunsa, qanday javob qaytarasiz?": {
        "Men avvalo, odam bilan ochiq muloqot qilishga harakat qilaman va u bilan fikrlarimni tushuntirishga urinamanu.": "murosali va sabrli muloqot qiladigan",
        "Agar u noto'g'ri tushungan bo'lsa, tushuntirishga harakat qilaman va o'z nuqtai nazarimni ochiq-oydin ifoda etaman.": "murosali va sabrli muloqot qiladigan",
        "Ularni tushunishga harakat qilaman va agar kerak bo'lsa, savol berib, aniqlik kiritishga intilaman.": "murosali va sabrli muloqot qiladigan",

        "Agar men noto'g'ri tushunsam, bu haqda qattiq gaplashaman va o'z fikrimni himoya qilaman.": "o'z fikrlarini himoya qilishni istaydigan",
        "Men to'g'ridan-to'g'ri ularni to'g'ri tushuntiraman va o'z nuqtai nazarimni ko'rsataman.": "o'z fikrlarini himoya qilishni istaydigan",
        "Agar bu muammo bo'lsa, buni ochiqchasiga aytaman va tuzatishga harakat qilaman.": "o'z fikrlarini himoya qilishni istaydigan",

        "Ba'zan o'zimni noto'g'ri tushunganidan xafa bo'lib qolaman, lekin so'rab, o'z fikrimni tushuntiraman.": "o'ziga nisbatan tanqidiy munosabatda bo'ladigan va o'z xatolarini tan oladigan",
        "Bunday vaziyatda juda xafa bo'lmayman, lekin tushuntirishga harakat qilaman.": "o'ziga nisbatan tanqidiy munosabatda bo'ladigan va o'z xatolarini tan oladigan",
        "Ba'zida muammo menda ekanligini tushunib, uzr so'rayman va vaziyatni tuzatishga harakat qilaman.": "o'ziga nisbatan tanqidiy munosabatda bo'ladigan va o'z xatolarini tan oladigan",

        "Ba'zida noto'g'ri tushunilganimda buni sezmasam ham, odam bilan ochiq gaplashish yaxshi bo'ladi.": "noaniq vaziyatlarda ochiq muloqot qilishga intiladigan",
        "Agar muammo bo'lsa, o'zaro kelishib olishimiz mumkin, lekin noto'g'ri tushunilgan vaziyatni hal qilish muhim.": "noaniq vaziyatlarda ochiq muloqot qilishga intiladigan",
        "Menga kerak bo'lganda, ularga o'z fikrlarimni aytish va vaziyatni hal qilishda yordam berish juda muhim.": "noaniq vaziyatlarda ochiq muloqot qilishga intiladigan",

    },
    "Kichik g'alabalarinvgizni qanday nishonlaysiz?": {
        "Men kichik g'alabalarimni nishonlash uchun do'stlarim bilan vaqt o'tkazaman yoki shunchaki o'zimni yaxshi his qilish uchun biror narsa qilaman.": "muvaffaqiyatlarni qadrlaydigan",
        "Har safar biror maqsadga erishsam, o'zimga kichik sovg'a beraman yoki sevimli ovqatimni tayyorlayman.": "muvaffaqiyatlarni qadrlaydigan",
        "Muvaffaqiyatlarimni bayram qilishni yaxshi ko'raman, shuning uchun kichik g'alabalarda ham o'zimga vaqt ajrataman.": "muvaffaqiyatlarni qadrlaydigan",

        "Men g'alabalarimni har doim qiyin ishlardan keyin oddiy bir narsa bilan nishonlayman, masalan, sevimli filmimni tomosha qilish.": "muvaffaqiyatlarni oddiy usullarda nishonlaydigan",
        "Kichik g'alabalardan keyin do'stlarim bilan kafeda o'tirish yoki birgalikda sayr qilish yaxshi.": "muvaffaqiyatlarni oddiy usullarda nishonlaydigan",
        "G'alaba qozonishda juda ochiq emasman, lekin o'zim uchun bu qanchalik muhimligini tushunaman.": "muvaffaqiyatlarni oddiy usullarda nishonlaydigan",

        "Men har doim katta muvaffaqiyatlarga e'tibor beraman, kichik g'alabalar esa ko'pincha o'tirib ketadi.": "kichik g'alabalarga ahamiyat bermaydigan",
        "Kichik g'alabalarni nishonlashni o'ylamayman, lekin ulardan ham foydalanishga harakat qilaman.": "kichik g'alabalarga ahamiyat bermaydigan",
        "Ba'zida muvaffaqiyatlarimni unutaman va keyinchalik o'ylab ko'rganimda ular haqida fikr yuritaman.": "kichik g'alabalarga ahamiyat bermaydigan",

        "Kichik g'alabalarimni boshqa muhim voqealar bilan bog'layman va ularni do'stlarim bilan bayram qilaman.": "hayotidagi kichik g'alabalarni yodda saqlaydigan",
        "Ba'zida muvaffaqiyatlarimni bahramand qilaman, ularni xotira sifatida saqlayman.": "hayotidagi kichik g'alabalarni yodda saqlaydigan",
        "G'alabalarimni nishonlash uchun o'z qiziqishlarimga vaqt ajrataman.": "hayotidagi kichik g'alabalarni yodda saqlaydigan",
    },
    "O'z-o'zingizni rivojlantirish uchun nimalarga e'tibor berasiz?": {
        "Men har doim yangi kitoblar o'qishga harakat qilaman va turli mavzularni o'rganaman.": "bilim olishga va o'z-o'zini rivojlantirishga qiziqishi bor",
        "Online kurslar va seminarlarni qatnashish orqali bilimlarimni kengaytirishga intilaman.": "bilim olishga va o'z-o'zini rivojlantirishga qiziqishi bor",
        "Yangi narsalarni o'rganishga va o'zimni doimiy ravishda yangilab turishga tayyorman.": "bilim olishga va o'z-o'zini rivojlantirishga qiziqishi bor",

        "O'z ko'nikmalarimni amaliy tajriba orqali rivojlantirishni afzal ko'raman.": "amaliy tajribaga e'tibor beradigan va o'z ko'nikmalarini rivojlantirishga harakat qiladigan",
        "Yangi loyihalarda qatnashib, o'z tajribamni oshiraman.": "amaliy tajribaga e'tibor beradigan va o'z ko'nikmalarini rivojlantirishga harakat qiladigan",
        "Ba'zan yangi narsalarni o'rganishda nazariy bilimlar kamlik qiladi, shuning uchun amaliyotga e'tibor beraman.": "amaliy tajribaga e'tibor beradigan va o'z ko'nikmalarini rivojlantirishga harakat qiladigan",

        "Meditatsiya qilish va o'z hissiyotlarimni tushunishga harakat qilaman.": "o'z hissiyotlari va fikrlari bilan ishlashga tayyor",
        "O'z ustimda ishlash va zaif tomonlarimni aniqlashda davom etaman.": "o'z hissiyotlari va fikrlari bilan ishlashga tayyor",
        "O'z-o'zini baholash va o'zgarishlarga tayyor turishga e'tibor beraman.": "o'z hissiyotlari va fikrlari bilan ishlashga tayyor",

        "Maqsadlarimni belgilab, ularga erishish uchun reja tuzaman.": "o'z hayotini maqsadli yo'nalishda rivojlantirishga tayyor",
        "Maqsadlarimga erishish jarayonida o'z o'zgarishlarimni nazorat qilishga harakat qilaman.": "o'z hayotini maqsadli yo'nalishda rivojlantirishga tayyor",
        "Har bir muvaffaqiyatimni rejalashtirish va baholashda davom etaman.": "o'z hayotini maqsadli yo'nalishda rivojlantirishga tayyor",

    },
    "Yangi do'stlar orttirishga qanday qaraysiz?": {
        "Yangi do'stlar orttirishni yaxshi ko'raman, har bir yangi tanishuv menga yangi fikrlar va tajribalar olib keladi.": "yangi tajribalar va fikrlar olishni qadrlaydigan",
        "Men odamlar bilan tanishishni va yangi munosabatlarni o'rnatishni afzal ko'raman.": "yangi tajribalar va fikrlar olishni qadrlaydigan",
        "Do'stlarimni kengaytirish orqali ko'proq qiziqarli odamlar bilan muloqot qilaman.": "yangi tajribalar va fikrlar olishni qadrlaydigan",

        "Yangi do'stlar orttirishga tayyorman, lekin kimlar bilan do'stlashishimni ehtiyotkorlik bilan tanlayman.": "yangi tanishuvlarga ehtiyotkorlik bilan yondashadigan",
        "Odamlar bilan tanishish jarayonida ularni yaxshilab tushunishga harakat qilaman.": "yangi tanishuvlarga ehtiyotkorlik bilan yondashadigan",
        "Ba'zida yangi do'stlar orttirishga ehtiyotkorlik bilan yondashaman, chunki har doim yaxshi natijalar bermaydi.": "yangi tanishuvlarga ehtiyotkorlik bilan yondashadigan",

        "Yangi do'stlar orttirish menga qiyin bo'ladi, lekin harakat qilaman.": "jtimoiy munosabatlarni o'rnatishda qiyinchiliklarga duch keladigan",
        "Odatda, men tanishish jarayonida asabiylashaman, lekin bu ustida ishlayapman.": "jtimoiy munosabatlarni o'rnatishda qiyinchiliklarga duch keladigan",
        "Ba'zida yangi odamlar bilan muloqot qilishni qiyin deb his qilaman, lekin yaxshi do'stlar orttirish uchun harakat qilaman.": "jtimoiy munosabatlarni o'rnatishda qiyinchiliklarga duch keladigan",

        "Men do'stlar orttirishga ko'p e'tibor bermayman, lekin mavjud do'stlarim bilan aloqani saqlashni afzal ko'raman.": "yangi do'stlar orttirishga ko'p ahamiyat bermaydigan",
        "Yangi do'stlar orttirish mening ustuvorligim emas, lekin ba'zan yangi odamlar bilan tanishishni yoqtiraman.": "yangi do'stlar orttirishga ko'p ahamiyat bermaydigan",
        "Agar yangi do'stlar paydo bo'lsa, qabul qilaman, lekin bu haqda ko'p o'ylamayman.": "yangi do'stlar orttirishga ko'p ahamiyat bermaydigan",
    },
    "Texnologiyalar hayotingizni qanday o'zgartirdi?": {
        "Texnologiyalar hayotimni ancha qulaylashtirdi; masalan, internet orqali ma'lumot topish juda oson.": "texnologiyalarning ijobiy ta'sirini qadrlaydigan",
        "Mobil telefonlar va ilovalar yordamida do'stlarim bilan bog'lanish vaqti-vaqti bilan muloqot qilishni osonlashtirdi.": "texnologiyalarning ijobiy ta'sirini qadrlaydigan",
        "Online ta'lim platformalari orqali yangi bilimlar olish imkoniyatim bor.": "texnologiyalarning ijobiy ta'sirini qadrlaydigan",

        "Ba'zida texnologiyalar hayotimni murakkablashtirishi mumkin; masalan, ma'lumot ko'p, lekin to'g'ri tanlash qiyin.": "texnologiyalarning ayrim salbiy ta'sirlarini haqida o'ylaydigan",
        "Ko'p vaqtimni telefon yoki kompyuterda o'tkazaman, bu esa muloqot qilishni kamaytiradi.": "texnologiyalarning ayrim salbiy ta'sirlarini haqida o'ylaydigan",
        "Texnologiyalar ko'pincha muammolarni hal qilishni osonlashtirishi o'rniga, yangi muammolar keltirishi mumkin.": "texnologiyalarning ayrim salbiy ta'sirlarini haqida o'ylaydigan",

        "Texnologiyalar doimiy o'zgarib turadi, shuning uchun ularni o'rganishga harakat qilaman.": "o'z bilimlarini yangilashga tayyor",
        "Yangi texnologiyalarni o'zlashtirishga harakat qilaman, lekin ba'zida qiyinchiliklar bor.": "o'z bilimlarini yangilashga tayyor",
        "Texnologiyalar bilan bog'liq bo'lgan yangiliklarni kuzatishga harakat qilaman.": "o'z bilimlarini yangilashga tayyor",

        "Texnologiyalar orqali yangi odamlar bilan tanishish imkoniyatim bor.": "ijtimoiy aloqalarni rivojlantirishda texnologiyalarni qadrlaydigan",
        "Ijtimoiy tarmoqlar yordamida do'stlarim bilan aloqani saqlayman, lekin ba'zida bu asl muloqotni kamaytiradi.": "ijtimoiy aloqalarni rivojlantirishda texnologiyalarni qadrlaydigan",
        "Texnologiyalar muloqot usullarini o'zgartiradi va odamlar o'rtasida masofani kamaytiradi.": "ijtimoiy aloqalarni rivojlantirishda texnologiyalarni qadrlaydigan",
    },
    "Biror vaqt o'z yo'lingizni tanlashga qiynalganmisiz?": {
        "Ha, o'z yo'limni tanlashda qiyinchiliklar yuzaga keldi; qaysi kasbni tanlashni bilmay qoldim.": "hayotida muhim qarorlar qabul qilishda qiyinaladigan",
        "O'qishga kirishda yoki yangi yo'nalishni tanlashda juda o'ylab qoldim.": "hayotida muhim qarorlar qabul qilishda qiyinaladigan",
        "Ba'zida qaysi yo'nalish menga ko'proq mos kelishini bilmayman.": "hayotida muhim qarorlar qabul qilishda qiyinaladigan",

        "O'z yo'limni tanlashda qiyinchiliklar bo'ldi, lekin vaqt o'tishi bilan o'z qiziqishlarimni aniqladim.": "qiyinchiliklarga qarshi kurashishda sabrli va qaror qabul qilishda qobiliyatli",
        "O'zimni qiziqtirgan narsalarni izlab, o'z yo'limni topishga harakat qildim.": "qiyinchiliklarga qarshi kurashishda sabrli va qaror qabul qilishda qobiliyatli",
        "O'zimga to'g'ri keladigan yo'lni tanlashda yordam beradigan insonlar bilan maslahatlashdim.": "qiyinchiliklarga qarshi kurashishda sabrli va qaror qabul qilishda qobiliyatli",

        "Men doimo o'z yo'limni aniqlashga harakat qilaman; har qanday qiyinchiliklarni yengishga tayyorman.": "o'z maqsadlariga erishish uchun, rejalashtirishga e'tibor beradigan",
        "O'z qiziqishlarim va maqsadlarimni o'rganib, kerakli yo'lni tanlayman.": "o'z maqsadlariga erishish uchun, rejalashtirishga e'tibor beradigan",
        "O'z yo'limni tanlashda ko'p vaqtim yo'q, lekin yaxshi reja tuzishga harakat qilaman.": "o'z maqsadlariga erishish uchun, rejalashtirishga e'tibor beradigan",

        "Men boshqalarning yo'lidan yurishni afzal ko'raman, chunki ular menga yordam berishi mumkin.": "o'z yo'lini tanlashda boshqalar fikrlariga tayanadigan",
        "Ba'zida boshqalar qanday yo'l tutayotganini kuzataman va ularni o'rganaman.": "o'z yo'lini tanlashda boshqalar fikrlariga tayanadigan",
        "O'zimning yo'limni topish o'rniga, do'stlarim va oila fikrlarini qabul qilaman.": "o'z yo'lini tanlashda boshqalar fikrlariga tayanadigan",
    },
    "Jamoaviy ishda qanday rolda bo‘lishni xohlaysiz?": {
        "Men jamoada lider bo'lishni yaxshi ko'raman; bu menga maqsadlarni belgilash va jamoani boshqarish imkonini beradi.": "jamoa uchun mas'uliyat olishga tayyor",
        "Lider sifatida boshqalar bilan birga ishlashni, ularni rag'batlantirishni va qo'llab-quvvatlashni afzal ko'raman.": "jamoa uchun mas'uliyat olishga tayyor",
        "Jamoa maqsadlariga erishishda yordam berish uchun rahbarlik qilish menga yoqadi.": "jamoa uchun mas'uliyat olishga tayyor",

        "Men jamoaviy ishda hamkorlik qilishni yaxshi ko'raman; bu menga boshqa fikrlarni eshitish imkonini beradi.": "hamkorlik va jamoaviy fikrlashni qadrlaydigan",
        "Meni qiziqtiradigan narsa bu boshqalar bilan birga fikr almashish va muammolarni birgalikda hal qilish.": "hamkorlik va jamoaviy fikrlashni qadrlaydigan",
        "Boshqalarning fikrlarini tinglash va birga ishlash menga yoqadi.": "hamkorlik va jamoaviy fikrlashni qadrlaydigan",

        "Men jamoada qo'llab-quvvatlovchi rolni afzal ko'raman; boshqalarga yordam berish va ularni rag'batlantirish menga yoqadi.": "jamoada tinchlik va ko'maklashishni qadrlaydigan",
        "Jamoada muammolarni hal qilishda yoki ehtiyojga muvofiq yordam berish menga yoqadi.": "jamoada tinchlik va ko'maklashishni qadrlaydigan",
        "Men ko'proq boshqalarning muvaffaqiyati uchun yordam berishga tayyorman.": "jamoada tinchlik va ko'maklashishni qadrlaydigan",

        "Men jamoada tahlilchi sifatida ishlashni yaxshi ko'raman; muammolarni hal qilish va strategiya ishlab chiqish menga yoqadi.": "jamoa ishini yanada samarali qilishga tayyor",
        "O'z fikrlarimni kiritib, jamoani yangi yo'nalishlarga olib borishni xohlayman.": "jamoa ishini yanada samarali qilishga tayyor",
        "Men tahlil qilish va qaror qabul qilishda yordam berishdan zavq olaman.": "jamoa ishini yanada samarali qilishga tayyor",
    },
    "Biror loyihani boshlashdan avval uni puxta rejalashtirasizmi?": {
        "Ha, har bir loyihani boshlashdan oldin puxta rejalashtirishni afzal ko'raman; bu menga muammolarni oldini olish imkonini beradi.": "har bir loyihani muvaffaqiyatli amalga oshirish uchun tayyorlanadigan",
        "Men reja tuzmasdan loyihaga kirishmayman, har bir qadamni belgilab olish muhim deb hisoblayman.": "har bir loyihani muvaffaqiyatli amalga oshirish uchun tayyorlanadigan",
        "Yaxshi reja yaratish, loyiha muvaffaqiyatiga ta'sir ko'rsatadi, shuning uchun har doim rejalashtiraman.": "har bir loyihani muvaffaqiyatli amalga oshirish uchun tayyorlanadigan",

        "Ba'zida puxta rejalashtirishni afzal ko'raman, lekin ba'zan shoshilinch loyihalar uchun tezda ishga kirishishga to'g'ri keladi.": "qisman rejalashtirishga e'tibor beradigan va muayyan vaziyatlarda shoshilinch harakat qiladigan",
        "Rejalashtirish muhim, lekin ba'zan qiziqish va motivatsiyani oshirish uchun tezda harakat qilishni afzal ko'raman.": "qisman rejalashtirishga e'tibor beradigan va muayyan vaziyatlarda shoshilinch harakat qiladigan",
        "Yaqin maqsadlarni belgilashim mumkin, lekin har doim rejalashtirishga e'tibor bermayman.": "qisman rejalashtirishga e'tibor beradigan va muayyan vaziyatlarda shoshilinch harakat qiladigan",

        "Men ko'proq spontan ishlarni afzal ko'raman; rejalashtirish menga noqulaylik tug'diradi.": "tezda ishga kirishishni ma'qul ko'radigan",
        "Lochiyalarni boshlashdan oldin puxta rejalashtirish o'rniga, ishga kirishishni afzal ko'raman.": "tezda ishga kirishishni ma'qul ko'radigan",
        "Ba'zan loyihalar qizig'i bilan boshlanadi va rejalashtirish juda ko'p vaqt talab qiladi.": "tezda ishga kirishishni ma'qul ko'radigan",

        "Men loyihalarni boshlashdan oldin jamoa bilan birga rejalashtirishni afzal ko'raman; bu yanada samarali reja yaratishga yordam beradi.": "jamoaviy yondashuvni afzal ko'radigan",
        "Jamoa fikrlarini tinglab, rejalashtirish jarayonini olib borishga harakat qilaman.": "jamoaviy yondashuvni afzal ko'radigan",
        "Yakuniy reja ko'pchilik bilan muhokama qilinishi, loyihaning muvaffaqiyatli bo'lishiga yordam beradi.": "jamoaviy yondashuvni afzal ko'radigan",
    },
    "Xato qilganingizda o‘zingizni qanday his qilasiz?": {
        "Xato qilsam, o'zimni avvaliga noqulay his qilaman, lekin bu xatoni o'rganish imkoniyati deb bilaman.": "xatolarni o'rganish va rivojlanish imkoniyati sifatida qabul qiladigan",
        "Har qanday xato — tajriba. Xatodan saboq olib, uni takrorlamaslikka harakat qilaman.": "xatolarni o'rganish va rivojlanish imkoniyati sifatida qabul qiladigan",
        "Xato qilganimda o'zimni biroz hafsalasi pir bo'lgan his qilaman, lekin bu kelajakda yaxshiroq bo'lish uchun motivatsiya beradi.": "xatolarni o'rganish va rivojlanish imkoniyati sifatida qabul qiladigan",

        "Xato qilganimda o'zimni juda yomon his qilaman va bu meni ko'p o'ylantiradi.": "xatolardan keyin o'zini yomon his qiladigan",
        "O'zimni xato qilganim uchun aybdor his qilaman va ko'pincha bu o'z ishonchimga ta'sir qiladi.": "xatolardan keyin o'zini yomon his qiladigan",
        "Ba'zida xato qilsam, o'zimni qiynalgan his qilaman va bu ko'pincha kayfiyatimga ta'sir qiladi.": "xatolardan keyin o'zini yomon his qiladigan",

        "Xato qilganimda, ko'p o'ylamaslikka harakat qilaman va darhol davom etaman.": "xatolarga ko'p ahamiyat bermaydigan va tezda unutadigan",
        "Xatolar ustida uzoq to'xtalmayman, chunki ular o'tib ketadi va men yangi vazifaga o'taman.": "xatolarga ko'p ahamiyat bermaydigan va tezda unutadigan",
        "Xato qilish — tabiiy, shuning uchun tezda oldinga qarayman.": "xatolarga ko'p ahamiyat bermaydigan va tezda unutadigan",

        "Xato qilganimda, bu haqda o'ylab, boshqalar bilan maslahatlashaman.": "xatolarni boshqalar bilan muhokama qiladigan",
        "Xatoni tan olib, jamoa bilan uni qanday tuzatishni o'rganishga harakat qilaman.": "xatolarni boshqalar bilan muhokama qiladigan",
        "Xato qilganimda, do'stlarim yoki hamkasblarim bilan gaplashib, ular nima qilish kerakligini maslahat berishadi.": "xatolarni boshqalar bilan muhokama qiladigan"
    },
    "O‘z vaqtingizdan to‘g‘ri foydalanasizmi?": {
        "Ha, o'z vaqtimni yaxshi rejalashtiraman. Har kuni oldindan rejalar tuzaman va ularni bajarishga harakat qilaman.": "vaqtni samarali boshqaradigan va maqsadlariga erishish uchun intizomli bo'la oladigan",
        "Vaqtni boshqarishda juda intizomli bo'lishga harakat qilaman, ish va dam olish uchun muvozanatni topganman.": "vaqtni samarali boshqaradigan va maqsadlariga erishish uchun intizomli bo'la oladigan",
        "Rejalar tuzib ishlash menga katta yordam beradi. Vaqtimni yaxshiroq boshqarishni o'rgandim, chunki bu hayotimni osonlashtiradi.": "vaqtni samarali boshqaradigan va maqsadlariga erishish uchun intizomli bo'la oladigan",

        "Ba'zan vaqtni boshqarish qiyin bo'lib qoladi, ayniqsa, ko'p ishlar yig'ilib qolganda.": "vaqtni boshqarishda hali tajribasi kamroq",
        "Vaqtimni to'g'ri taqsimlashni hali o'rganayotgan bo'lsam-da, ba'zida ortga qolib ketaman.": "vaqtni boshqarishda hali tajribasi kamroq",
        "Rejalar tuzishga harakat qilaman, lekin hammasi doim reja bo'yicha ketmaydi.": "vaqtni boshqarishda hali tajribasi kamroq",

        "Vaqtni boshqarishga unchalik e'tibor bermayman, chunki ko'proq spontan qarorlar qabul qilishni yaxshi ko'raman.": "ko'proq erkin, rejasiz hayot tarzini yoqtiradigan",
        "Har kuni rejalashtirish o'rniga, vaziyatga qarab harakat qilaman. Bu menga ko'proq mos keladi.": "ko'proq erkin, rejasiz hayot tarzini yoqtiradigan",
        "Juda rejalashtirilgan hayot menga zerikarli tuyuladi, shuning uchun vaqtimni rejasiz o'tkazishni yaxshi ko'raman.": "ko'proq erkin, rejasiz hayot tarzini yoqtiradigan",

        "Vaqtni boshqarishga ko'p o'ylamayman, chunki buni tabiiy ravishda qabul qilaman.": "rejalarga ko'p bog'lanmasdan ishlashga moyil",
        "Ishlarimni o'z vaqtida bajarishga harakat qilaman, lekin uni qat'iy rejalashtirmayman.": "rejalarga ko'p bog'lanmasdan ishlashga moyil",
        "Vaqtimni yaxshi rejalashtirishga harakat qilaman, lekin har doim ham bunga e'tibor qaratavermayman.": "rejalarga ko'p bog'lanmasdan ishlashga moyil",
    },
    "Ko'pchilikning fikriga qo'shilmasangiz, qanday yo'l tutasiz?": {
        "Agar kelishmasam, o'z fikrimni aniq bayon qilaman va uni himoya qilaman. Har kimning o'z fikri bo'lishi kerak, shuning uchun o'z nuqtai nazarimni ochiq aytaman.": "o'z nuqtai nazariga ishonchli va uni himoya qilishda qat'iyatli",
        "Agar haqiqat deb hisoblasam, ko'pchilikka qarshi turishga tayyorman. O'z pozitsiyamni tushuntirishga harakat qilaman.": "o'z nuqtai nazariga ishonchli va uni himoya qilishda qat'iyatli",
        "Kelishmovchilik bo'lsa ham, o'z fikrimni o'zgartirmayman, lekin buni xushmuomalalik bilan ifoda etaman.": "o'z nuqtai nazariga ishonchli va uni himoya qilishda qat'iyatli",

        "Agar kelishmasam, fikrimni hurmat bilan aytaman, lekin hech kimni xafa qilmaslikka harakat qilaman.": "ziddiyatlarni yumshatishga intiladigan",
        "Kelishmovchiliklarni mojaroga aylantirmaslikka harakat qilaman, balki boshqalarning fikrini tushunishga harakat qilaman.": "ziddiyatlarni yumshatishga intiladigan",
        "Ko'pchilik bilan kelishmovchilikda, murosa qilish yo'lini topishga harakat qilaman.": "ziddiyatlarni yumshatishga intiladigan",

        "Agar kelishmasam ham, ko'pchilikning fikrini qabul qilaman. Ba'zan ko'pchilik bilan kelishuv muhimroq bo'ladi.": "iddiyatlardan qochishga va tinchlikni saqlashga harakat qiladigan",
        "Kelishmasam ham, ko'pincha mojarodan qochish uchun sukut saqlayman.": "iddiyatlardan qochishga va tinchlikni saqlashga harakat qiladigan",
        "Ko'pchilik bilan kelishmaslikka harakat qilmayman, chunki bu vaziyatni yanada murakkablashtirishi mumkin.": "iddiyatlardan qochishga va tinchlikni saqlashga harakat qiladigan",

        "Agar kelishmasam, o'z fikrimni bildirishdan oldin boshqalarning nuqtai nazarini tushunishga harakat qilaman.": "o'z qarashlarini qayta ko'rib chiqish va o'rganishga moyil",
        "Men doim haq bo'lishim shart emas, shuning uchun ko'pchilikning fikriga quloq solib, o'zimni qayta ko'rib chiqaman.": "o'z qarashlarini qayta ko'rib chiqish va o'rganishga moyil",
        "Ba'zan boshqalarning fikri mening qarashlarimdan ko'ra ko'proq ma'no kasb etadi, shuning uchun ularga ochiq bo'laman.": "o'z qarashlarini qayta ko'rib chiqish va o'rganishga moyil",
    },
    "Yangi maqsad qo'yishda nimani birinchi o'ringa qo'yasiz?": {
        "Birinchi o'rinda maqsadni aniq belgilayman va unga qanday erishishimni rejalashtiraman.": "tashkilotchilik va aniqlikka katta ahamiyat beradigan",
        "Maqsadni aniq va o'lchovli qilib belgilayman, shunda uni kuzatish oson bo'ladi.": "tashkilotchilik va aniqlikka katta ahamiyat beradigan",
        "Har bir bosqichni rejalashtirish va ularga muddatlar belgilash muhim.": "tashkilotchilik va aniqlikka katta ahamiyat beradigan",

        "Maqsad qo'yishda, u meni ilhomlantirishi va motivatsiya berishi kerak. Qiziqarli bo'lishi muhim.": "motivatsiya va ilhomni muhim biladigan",
        "Birinchi o'rinda maqsadning men uchun qanchalik ahamiyatli ekanini o'ylayman.": "motivatsiya va ilhomni muhim biladigan",
        "Maqsad meni oldinga yetaklaydi va menga ruhiy kuch beradi.": "motivatsiya va ilhomni muhim biladigan",

        "Maqsadning hayotimga qanday foyda keltirishini o'ylab ko'raman.": "maqsadlarning foydasi va real hayotga qanday ta'sir qilishi haqida o'ylaydigan",
        "Maqsad menga yoki boshqalarga qanday yordam berishini ko'rib chiqaman.": "maqsadlarning foydasi va real hayotga qanday ta'sir qilishi haqida o'ylaydigan",
        "Qanchalik amaliy va erishish mumkin ekanligini birinchi o'rinda hisoblayman.": "maqsadlarning foydasi va real hayotga qanday ta'sir qilishi haqida o'ylaydigan",

        "Maqsadga erishish uchun qanday resurslar kerak bo'lishini baholayman.": "resurslar va imkoniyatlarni tahlil qilishga e'tibor beradigan",
        "Resurslarim va imkoniyatlarimni hisobga olib, realistik maqsad qo'yaman.": "resurslar va imkoniyatlarni tahlil qilishga e'tibor beradigan",
        "Birinchi navbatda mavjud resurslarni to'g'ri baholashga harakat qilaman.": "resurslar va imkoniyatlarni tahlil qilishga e'tibor beradigan",

        "Maqsad mening umumiy hayotiy rejalarimga mos keladimi, shuni ko'rib chiqaman.": "maqsadni katta rejalar bilan uyg'unlashtirishga e'tibor beradigan",
        "Birinchi o'rinda, qaysi maqsad eng muhimligini aniqlayman va unga ko'proq vaqt ajrataman.": "maqsadni katta rejalar bilan uyg'unlashtirishga e'tibor beradigan",
        "Maqsad mening uzoq muddatli maqsadlarimga mos keladimi, shuni hisobga olaman.": "maqsadni katta rejalar bilan uyg'unlashtirishga e'tibor beradigan",
    },
    "O'zingni yangi sohada sinab ko'rishga qiziqasizmi?": {
        "Ha, men yangi sohalarni o'rganishni yaxshi ko'raman, chunki bu meni rivojlantiradi.": "yangilikka och va o'zini turli sohalarda sinab ko'rishga tayyor",
        "Har doim yangi narsalarni sinab ko'rishga tayyorman, bu menga qiziq va zavqli bo'lib tuyuladi.": "yangilikka och va o'zini turli sohalarda sinab ko'rishga tayyor",
        "Yangi sohalar – bu yangi imkoniyatlar. Men yangi narsalarni o'rganishni yaxshi ko'raman.": "yangilikka och va o'zini turli sohalarda sinab ko'rishga tayyor",

        "Agar yangi soha menga qiziq bo'lsa, albatta, sinab ko'rishim mumkin.": "yangi tajribalarni tanlashda ehtiyotkor",
        "Foydali bo'lsa, yangi narsalarni sinab ko'rishga qarshiligim yo'q.": "yangi tajribalarni tanlashda ehtiyotkor",
        "Menga ma'lum bir sohalar qiziq, lekin boshqa yo'nalishlarga ehtiyotkorona yondashaman.": "yangi tajribalarni tanlashda ehtiyotkor",

        "Men odatda o'zim bilgan sohalarda ishlashni afzal ko'raman.": "risklarni minimallashtirishni afzal ko'radigan",
        "Yangi narsalar meni ko'pincha xavotirga soladi, shuning uchun o'ylab ish qilaman.": "risklarni minimallashtirishni afzal ko'radigan",
        "Yangi sohalarga kirishdan oldin, u haqda yetarli bilim va tajribaga ega bo'lishni xohlayman.": "risklarni minimallashtirishni afzal ko'radigan",

        "Yo'q, men odatda o'z yo'limni tanlab olganman va unga sodiq qolaman.": "yangi tajribalar va sohalarga qiziqishi past",
        "Menga yangi narsalar qiziq emas, ko'proq o'zim bilgan yo'nalishda davom etishni xohlayman.": "yangi tajribalar va sohalarga qiziqishi past",
        "Yangi sohalar meni qiziqtirmaydi, men o'zimga tanish narsalar bilan shug'ullanishni afzal ko'raman.": "yangi tajribalar va sohalarga qiziqishi past",
    },
    "Qaysi mavzuda ko'p bilimga ega bo'lishni istaysiz?": {
        "Men texnologiyalar va dasturlashda ko'proq bilim olishni istayman.": "aniq bir sohada bilim olishga e'tiborini qaratadigan",
        "Menga tibbiyot sohasi qiziq, shuning uchun bu borada chuqur bilim olishni xohlayman.": "aniq bir sohada bilim olishga e'tiborini qaratadigan",
        "Men tarixni yaxshi ko'raman va unda ko'proq bilimga ega bo'lishni xohlayman.": "aniq bir sohada bilim olishga e'tiborini qaratadigan",

        "Men umumiy bilimlarni oshirishni xohlayman, ayniqsa psixologiya va odamlar bilan ishlash borasida.": "o'zini turli yo'nalishlarda rivojlantirishni xohlaydigan",
        "Hayotiy ko'nikmalar va moliyaviy savodxonlik haqida ko'proq bilishni istayman.": "o'zini turli yo'nalishlarda rivojlantirishni xohlaydigan",
        "Men turli madaniyatlar va tillarni o'rganishga qiziqaman.": "o'zini turli yo'nalishlarda rivojlantirishni xohlaydigan",

        "Men san'at va ijodiy yo'nalishlarda bilim olishni istayman.": "san'at va ijodiy ishlarga moyil",
        "Musiqa yoki adabiyot haqida ko'proq bilishni xohlayman, chunki bu menga ilhom beradi.": "san'at va ijodiy ishlarga moyil",
        "Kinomatografiya va filmlar yaratish texnikasi haqida chuqurroq bilim olishni istayman.": "san'at va ijodiy ishlarga moyil",

        "Men sun'iy intellekt va texnologik yangiliklar haqida ko'proq bilishni xohlayman.": "zamonaviy texnologiyalar haqida bilim olishga intiladigan",
        "Menga ilm-fan, kosmos va fizikaga oid bilimlar qiziq.": "zamonaviy texnologiyalar haqida bilim olishga intiladigan",
        "Men texnologiyalarni rivojlantirish va startaplar haqida ko'proq o'rganishni istayman.": "zamonaviy texnologiyalar haqida bilim olishga intiladigan"
    },
}

Professions = [
    'Dasturchilik kasbi',
    'Pedagogik mutahassislik kasbi',
    'Oshpaslik kasbi',
    'Shifokorlik kasbi',
    'Arxitektorlik kasbi'
]

questions_list = list(Data.keys())


def get_character(data):
    character_ = 'Sizning xarakteringiz: '
    for d in data:
        character_ += f"{Data.get(questions_list[d.get('pk') - 1]).get(d.get('answer'))}, "
    character_ += ' insonsiz.'
    character_ += f"\nSizga {random.choice(Professions)} to'g'ri keladi."

    return character_


def find_best_match(user_answer: str, def_answer_list: list[str]):
    user_answer_to_words = user_answer.split()
    res_average = {}
    for def_answer_item in def_answer_list:
        res_average[def_answer_item] = statistics.mean(list(map(
            lambda answer_item: SequenceMatcher(None, def_answer_item.lower(), answer_item.lower()).ratio(),
            user_answer_to_words
        )))

    return max(res_average, key=res_average.get)


def get_user_character_and_profession(data):
    """
    res = [
        {
            'pk': 1,
            'answer': "Sport yoqadi"
        },
    ]
    :param data:
    :return:
    """
    result_list = [
        {'pk': dat.get('pk'),
         'answer': find_best_match(dat.get('answer'), list(Data.get(questions_list[dat.get('pk') - 1]).keys()))} for dat
        in
        data
    ]
    character = get_character(result_list)
    return character
