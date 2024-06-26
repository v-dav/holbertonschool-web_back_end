function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3',
      {
        phoneNumber: job.phoneNumber,
        message: job.message,
      })
      .save((err) => {
        if (err) {
          console.log(`Notification job ${newJob.id} failed: ${err}`);
        } else {
          console.log(`Notification job created: ${newJob.id}`);
        }
      });
    newJob.on('complete', () => console.log(`Notification job ${newJob.id} completed`));
    newJob.on('progress', (progress) => console.log(`Notification job ${newJob.id} ${progress}% complete`));
  }
}

module.exports = createPushNotificationsJobs;
