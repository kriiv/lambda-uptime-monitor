The goal here is to create the simplest uptime monitor possible.
We check an HTTP endpoint for a 200 status code. If not 200 status, we return a Slack webhook alert.
Lambda is triggered on schedule via Cloudwatch.
