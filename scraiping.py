from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd

base_url = 'https://careerconnection.jp/review/rating/Rating/?pageNo={}'

d_list = []

for enu, i in enumerate(range(1080, 1160)):
    print('='*30, enu, '='*30)
    url = base_url.format(i)
    r = requests.get(url)
    sleep(4)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, 'lxml')

    company_pages = soup.select('h2')
    for j in company_pages:
        company_url = j.select_one('a').get('href')
        r_page = requests.get(company_url)
        r_page.raise_for_status()
        sleep(3)
        r_soup = BeautifulSoup(r_page.content, 'lxml')

        name_xx = r_soup.select_one('.pc-report-header__company')
        name = name_xx.text if name_xx else None

        dtxdd_all_all = r_soup.select_one('.pc-company-summary')
        dtxdd_all = dtxdd_all_all.select('dt, dd')
        p_list = []
        for p in dtxdd_all:
            pp = p.text
            p_list.append(pp)
        if '英名' in p_list:
            number1 = p_list.index('英名')
            name_english = p_list[number1 + 1]
        else:
            name_english = None
        if '企業HP' in p_list:
            number2 = p_list.index('企業HP')
            hp = p_list[number2 + 1]
        else:
            hp = None
        if '住所' in p_list:
            number3 = p_list.index('住所')
            address = p_list[number3 + 1]
        else:
            address = None
        if '業界' in p_list:
            number4 = p_list.index('業界')
            industry = p_list[number4 + 1]
        else:
            industry = None
        if '代表者' in p_list:
            number5 = p_list.index('代表者')
            president = p_list[number5 + 1]
        else:
            president = None
        if '設立年月' in p_list:
            number6 = p_list.index('設立年月')
            establish_day = p_list[number6 + 1]
        else:
            establish_day = None
        if '上場区分' in p_list:
            number7 = p_list.index('上場区分')
            listing = p_list[number7 + 1]
        else:
            listing = None
        
        reputation_xx = r_soup.select_one('.pc-report-header-review-aggregate__rating-average')
        reputation = reputation_xx.text if reputation_xx else None
        income_xx = r_soup.select_one('.value-main')
        income = income_xx.text if income_xx else None
        overtime_xx = r_soup.select_one('.overview-area__time-list1')
        overtime = overtime_xx.text if overtime_xx else None
        holiday_work_xx = r_soup.select_one('.overview-area__time-list2')
        holiday_work = holiday_work_xx.text if holiday_work_xx else None
        leave_xx = r_soup.select_one('.overview-area__time-list3')
        leave = leave_xx.text if leave_xx else None

        white_black_url_xx = r_soup.select_one('.pc-report-header-nav > li:nth-of-type(6) > a')
        if white_black_url_xx:
            white_black_url = white_black_url_xx.get('href')
            wb_page = requests.get(white_black_url)
            sleep(3)
            wb_page.raise_for_status()
            wb_soup = BeautifulSoup(wb_page.content, 'lxml')
            aaa = wb_soup.find(text="労働時間の満足度").parent.parent
            work_xx = aaa.select_one('.pc-rating__average')
            work = work_xx.text if work_xx else None
            aaa = wb_soup.find(text="仕事のやりがい").parent.parent
            rewarding_xx = aaa.select_one('.pc-rating__average')
            rewarding = rewarding_xx.text if rewarding_xx else None
            aaa = wb_soup.find(text="ストレス度の低さ").parent.parent
            stress_xx = aaa.select_one('.pc-rating__average')
            stress = stress_xx.text if stress_xx else None
            aaa = wb_soup.find(text="休日数の満足度").parent.parent
            holiday_xx = aaa.select_one('.pc-rating__average')
            holiday = holiday_xx.text if holiday_xx else None
            aaa = wb_soup.find(text="給与の満足度").parent.parent
            salary_xx = aaa.select_one('.pc-rating__average')
            salary = salary_xx.text if salary_xx else None
            aaa = wb_soup.find(text="ホワイト度").parent.parent
            white_xx = aaa.select_one('.pc-rating__average')
            white = white_xx.text if white_xx else None
        else:
            work = None
            rewarding = None
            stress = None
            holiday = None
            salary = None
            white = None

        kuchi_url_xx = r_soup.select_one('.pc-report-header-nav > li:nth-of-type(7) > a')
        
        if kuchi_url_xx:
            kuchi_url = kuchi_url_xx.get('href')
            kuchi_page = requests.get(kuchi_url)
            sleep(1)
            kuchi_page.raise_for_status()
            kuchi_soup = BeautifulSoup(kuchi_page.content, 'lxml')
            sougou_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)').text
            sougou_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(1) > td:nth-of-type(3)').text
            sougou_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(1) > td:nth-of-type(4)').text
            yarigai_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)').text
            yarigai_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)').text
            yarigai_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(2) > td:nth-of-type(4)').text
            kyuyo_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(3) > td:nth-of-type(2)').text
            kyuyo_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(3) > td:nth-of-type(3)').text
            kyuyo_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(3) > td:nth-of-type(4)').text
            nensyuu_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)').text
            nensyuu_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(4) > td:nth-of-type(3)').text
            nensyuu_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(4) > td:nth-of-type(4)').text
            roudoujikan_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)').text
            roudoujikan_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(5) > td:nth-of-type(3)').text
            roudoujikan_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(5) > td:nth-of-type(4)').text
            yukyu_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)').text
            yukyu_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(6) > td:nth-of-type(3)').text
            yukyu_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(6) > td:nth-of-type(4)').text
            zanngyou_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)').text
            zanngyou_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(7) > td:nth-of-type(3)').text
            zanngyou_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(7) > td:nth-of-type(4)').text
            kyujitu_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)').text
            kyujitu_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(8) > td:nth-of-type(3)').text
            kyujitu_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(8) > td:nth-of-type(4)').text
            syukkin_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)').text
            syukkin_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(9) > td:nth-of-type(3)').text
            syukkin_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(9) > td:nth-of-type(4)').text
            howaito_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(10) > td:nth-of-type(2)').text
            howaito_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(10) > td:nth-of-type(3)').text
            howaito_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(10) > td:nth-of-type(4)').text
            storesu_ow = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)').text
            storesu_te = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(11) > td:nth-of-type(3)').text
            storesu_el = kuchi_soup.select_one('.compare-evaluation-area__table > tbody > tr:nth-of-type(11) > td:nth-of-type(4)').text
        else:
            sougou_ow = sougou_te = sougou_el = yarigai_ow = yarigai_te = yarigai_el = kyuyo_ow = kyuyo_te = kyuyo_el = nensyuu_ow = nensyuu_te = nensyuu_el = roudoujikan_ow = roudoujikan_te = roudoujikan_el = yukyu_ow = yukyu_te = yukyu_el = zanngyou_ow = zanngyou_te = zanngyou_el = kyujitu_ow = kyujitu_te = kyujitu_el = syukkin_ow = syukkin_te = syukkin_el = howaito_ow = howaito_te = howaito_el = storesu_ow = storesu_te = storesu_el = '-'

        d_list.append({
            '企業名': name,
            '英名': name_english,
            '企業HP': hp,
            '住所': address,
            '業界': industry,
            '代表者': president,
            '設立年月': establish_day,
            '上場区分': listing,
            '総合評価': reputation,
            '平均収入': income,
            '月の残業時間': overtime,
            '月の休日出勤': holiday_work,
            '有休消化率': leave,
            '労働時間の満足度': work,
            '仕事のやりがい': rewarding,
            'ストレス度の低さ': stress,
            '休日数の満足度': holiday,
            '給与の満足度': salary,
            'ホワイト度': white,
            '総合評価OP':sougou_ow,
            '仕事のやりがいOP':yarigai_ow,
            '給与の満足度OP':kyuyo_ow,
            '平均年収OP':nensyuu_ow,
            '労働時間の満足度OP':roudoujikan_ow,
            '有給休暇消化率OP':yukyu_ow,
            '平均残業時間OP':zanngyou_ow,
            '休日数の満足度OP':kyujitu_ow,
            '平均休日の出勤数OP':syukkin_ow,
            'ホワイト度OP':howaito_ow,
            'ストレス度の低さOP':storesu_ow,
            '総合評価転職':sougou_te,
            '仕事のやりがい転職':yarigai_te,
            '給与の満足度転職':kyuyo_te,
            '平均年収転職':nensyuu_te,
            '労働時間の満足度転職':roudoujikan_te,
            '有給休暇消化率転職':yukyu_te,
            '平均残業時間転職':zanngyou_te,
            '休日数の満足度転職':kyujitu_te,
            '平均休日の出勤数転職':syukkin_te,
            'ホワイト度転職':howaito_te,
            'ストレス度の低さ転職':storesu_te,
            '総合評価EL':sougou_el,
            '仕事のやりがいEL':yarigai_el,
            '給与の満足度EL':kyuyo_el,
            '平均年収EL':nensyuu_el,
            '労働時間の満足度EL':roudoujikan_el,
            '有給休暇消化率EL':yukyu_el,
            '平均残業時間EL':zanngyou_el,
            '休日数の満足度EL':kyujitu_el,
            '平均休日の出勤数EL':syukkin_el,
            'ホワイト度EL':howaito_el,
            'ストレス度の低さEL':storesu_el,
        })
        print(d_list[-1])

df = pd.DataFrame(d_list)
df.to_excel('company_list1099-1150.xlsx', index=None, encoding='utf-8-sig')



