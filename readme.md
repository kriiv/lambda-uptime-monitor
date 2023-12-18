The goal here is to create the simplest uptime monitor possible.

We check an HTTP endpoint for a 200 status code. If not 200 status, we return a Slack webhook alert.

Lambda is triggered on schedule via Cloudwatch.

Repo is completely packaged, ready to zip and push to Lambda.

Slack webhook URl set in env variables. `SLACK_WEBHOOK_URL`
