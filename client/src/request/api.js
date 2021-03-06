import { get, post } from './http'

export const apiUserList = p => get('kctool/user', p);

export const apiGenUser = p => post('kctool/user/add', p);

export const apiDeposite = p =>post('/kctool/account/receipt', p);

export const apiIncomeCheckTotal =p => get('kctool/income/check_total',p);

export const apiIncomeCheckSubscribe=p => get('kctool/income/check_subscribe_income',p);

export const apiIncomeCheckTime=p => get('kctool/income/check_time_income',p);

export const apiIncomeCheckDemand=p => get('kctool/income/check_demand_income',p);

export const apiIncomeCheckBlack=p => get('kctool/income/check_blacklist_income',p);

export const apiIncomeCheckFake=p => get('kctool/income/check_fake_income',p);

export const apiIncomeCheckVote=p => get('kctool/income/check_vote_income',p);

export const apiIncomeCheckLiquidity=p => get('kctool/check/liquidity',p);

export const apiSoftIncomeCheck=p => get('kctool/soft/income/check',p);

export const apiSoftLowerCheck=p => get('kctool/soft/lower/check',p);

export const apiGoogleCode=p => get('kctool/google_code',p);

export const apiClearCurrencyCache=p => get('kctool/currency/clear',p);

export const apiClearPoolxCache=p => get('kctool/px-redis/clear',p);

export const apiShardingPoolTable=p => get('kctool/px_sharding_table',p);

export const apiShardingAccount=p => get('kctool/sharding-account',p);

export const apiGetNftTokens=p => get('/kctool/currency/nft/tokens',p)

export const apiNftReceipt=p => post('/kctool/account/nft-receipt',p)

export const apiTaskPause=p => get('/kctool/scheduler/pause',p)

export const apiTaskResume=p => get('/kctool/scheduler/resume',p)

export const apiGetTask=() => get('/kctool/scheduler/gettask')
