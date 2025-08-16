from lxml import etree
import sys

danger = {
  'android.permission.READ_SMS',
  'android.permission.RECEIVE_SMS',
  'android.permission.CALL_PHONE',
  'android.permission.RECORD_AUDIO',
  'android.permission.READ_CONTACTS',
  'android.permission.WRITE_SETTINGS',
  'android.permission.SYSTEM_ALERT_WINDOW'
}

tree = etree.parse(sys.argv[1])
perms = tree.xpath('//uses-permission/@android:name', namespaces={'android':'http://schemas.android.com/apk/res/android'})

findings = [p for p in perms if p in danger]
print('Dangerous permissions found:' if findings else 'No dangerous permissions detected.')
for p in findings: print('-', p)
