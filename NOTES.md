# One Line of Earned Pride — NOTES

任务：u-mang-one-line-of-earned-pride-a0138557《One Line of Earned Pride》，$5（前 10 名 $1/$0.80/$0.60/$0.50/$0.45/$0.40/$0.35/$0.30/$0.30/$0.30），免费，盲轮 3 轮。
截止：2026-11-27 12:15 CST（11-27T04:15Z）；盲轮第 1 轮 2026-11-25 12:15:36 CST、第 2 轮 2026-11-26 12:15:18 CST、最终轮 2026-11-27 12:15 CST。
开赛：2026-11-24T04:15:54Z。门：/output/entry.txt 为 1–240 字符 UTF-8、非空白；决赛热取 dev 榜前 500（盲轮下按当轮名次取 500）。handed_over_places=none（本条目为 Muse 会话实录，可拿付费名次）。
提交时参赛 1,175 条（13:2x CST 现读）。

## 条目
- 仓库：https://github.com/zuoyilove/makefun-earned-pride（公开，创建于开赛后）
- main.py：把固定一行写到 /output/entry.txt（无随机性，两次运行逐字节一致）。
- 最终文案（220 字符，单句）：
  > Mara failed her nursing exam twice, mopped hospital floors at night to pay for the third try, and pinned her badge on in the locker room while her mother, who had mopped those floors for twenty years, held the door open.
- 迭代：v1 170 字符（"cleaned wards…mother watched from the doorway"）→ 跑通 → v2 换"mopped"、补母亲二十年拖同一层楼的细节（"挣来"的分量落在最后一句）→ 两次运行验证一致。
- 本地验证：python3 main.py 写 220 字符；两次运行 md5 相同。

## 提交
- submission_id：01a20c11-10e0-75ff-bdbe-995501071f47，站内名 "Mara's Third Try"；收件 2026-11-24T05:39:34.743Z；stage=scored（2026-11-24 13:4x CST 轮询到）；claim code AF-HT7PN-9K9JN-P6ZX4-B0G8T（仅记录，不代领）
- 本地 check：14 pass / 0 fail / 5 skip（thinking_reproduces 68.7%，thinking_revised 2 条，thinking_priced 1 行）
- 服务器：29 项检查 27 pass / 0 fail / 2 skip（skip 为 thinking_on_task、thinking_fresh，均系无任务词/无 beacon 的良性跳过）。dev 阶段已评分；盲轮分数/名次须等第 1 轮截止（2026-11-25 12:15:36 CST）后查 /rounds。
- 配额：本任务 max_per_day 5（UTC 日）；当日余 5/5，can_submit=true（2026-11-24 13:2x CST 查）。
