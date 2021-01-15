# encoding=utf-8
# @Author : wangjie
# @Time : 2021/1/11 下午4:21

'''定时任务配置'''

from exts import scheduler
from kctool import check_lower_soft, check_soft_income, check_total_pol_income, check_subscribe_income, \
    check_time_income, check_demand_income, check_black_income, check_fake_income, check_vote_income, check_liquidity,\
    TimeUitl
from kctool.commonMethods.dingtalk_util import SendMessage


class SchedulerConfig():
    JOBS = [
        {
            'id': '1',
            'name': 'soft_income_check',
            'func': 'scheduler:soft_check_income',
            'args': None,
            'trigger': 'cron',  # cron表示定时任务
            'hour': 18,
            'minute': 0,
            'second':0
        },
        {
            'id': '2',
            'name': 'staking_income_check',
            'func': 'scheduler:staking_check_income',
            'args': None,
            'trigger': 'cron',  # cron表示定时任务
            'hour': 18,
            'minute': 0,
            'second': 0
        }

    ]


def if_success(result):
    return ' <font color=#008000 >通过</font>' if result == "success" else '<font color=#FF0000 >错误</font>'


def soft_check_income():
    with scheduler.app.app_context():
        msg = '#### Soft Staking收益检查{} \n'.format(TimeUitl().day_gen(-1))
        msg = msg + '- 检查最小持仓收益:' + if_success(check_lower_soft()['result'])+'\n'
        msg = msg + '- 检查持仓收益:' + if_success(check_soft_income()['result'])+'\n'
        sendMessage = SendMessage()
        sendMessage.send_action_card(title="持仓收益检查", text=msg, actionURL="http://10.2.1.32:8080/soft_income_check")

def staking_check_income():
    with scheduler.app.app_context():
        msg = '#### Staking收益检查{} \n'.format(TimeUitl().day_gen(-1))
        msg = msg + '- POL总收益数量检查:' + if_success(check_total_pol_income()['result'])+'\n'
        msg = msg + '- 定期产品申购期收益检查:' + if_success(check_subscribe_income()['result'])+'\n'
        msg = msg + '- 定期产品质押期间收益检查:' + if_success(check_time_income()['result'])+'\n'
        msg = msg + '- 活期产品收益检查:' + if_success(check_demand_income()['result'])+'\n'
        msg = msg + '- 本币收益黑名单收益检查:' + if_success(check_black_income()['result'])+'\n'
        msg = msg + '- Fake锁仓收益检查:' + if_success(check_fake_income()['result'])+'\n'
        msg = msg + '- 投票治理收益检查:' + if_success(check_vote_income()['result'])+'\n'
        msg = msg + '- 赎回期系数检查:' + if_success(check_liquidity()['result'])+'\n'
        sendMessage = SendMessage()
        sendMessage.send_action_card(title="锁仓收益检查", text=msg)
