"""
2.预规划，预言，交互显示
3.广域搜索机 ，广域搜索机要不要过去，到目标上方
4.同时发现多个目标


    """
i = 0
uav = [ 
    '无人机 : ',
                    '', 
                    '', 
]
gcs = [ 
    '地面站 : ',
                    '', 
                    '向集群请求规划方案，画出路线预演', 
]
jq  = [ 
    ' 集群  : ',
                    '', 
                    '根据地面站选择区域，回馈分配结果', 
]

msglist = [
    uav,
    gcs,
    jq,
]