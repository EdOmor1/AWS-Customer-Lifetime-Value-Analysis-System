import boto3

# Initialize Backup client
backup = boto3.client('backup', region_name='your_region')

def setup_backup():
    response = backup.create_backup_plan(
        BackupPlan={
            'BackupPlanName': 'MyBackupPlan',
            'Rules': [
                {
                    'RuleName': 'DailyBackup',
                    'TargetBackupVaultName': 'MyBackupVault',
                    'ScheduleExpression': 'cron(0 12 * * ? *)',
                    'StartWindowMinutes': 60,
                    'CompletionWindowMinutes': 180,
                    'Lifecycle': {
                        'DeleteAfterDays': 30
                    }
                }
            ]
        }
    )
    print("Backup plan created: ", response['BackupPlanId'])

if __name__ == "__main__":
    setup_backup()
