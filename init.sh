supervisord -c supervisord.ini
if [ $run_web == 1 ]; then
  echo "开启web服务"
  # 执行命令，开启web服务
  supervisorctl start web_api
fi

if [ $run_scheduler == 1 ]; then
  echo "开启任务调度"
    supervisorctl start scheduler
fi

if [ $run_flower == 1 ]; then
  echo "开启flower"
  # 以守护进程启动
  supervisorctl start celery_flower
fi

if [ $run_worker == 1 ]; then
  echo "开启celery worker"
  supervisorctl start celery_worker
fi

tail -f /dev/null
