QPython 文档

    官网的导航出bug了 根本没法看 整理下方便查阅

    QPython接口文档文字版
        AndroidFacade
            Clipboard APIs
                setClipboard(text)
                getClipboard(text)
            Intent & startActivity APIs
                makeIntent(action, uri, type, extras, categories, packagename, classname, flags)
                getIntent()
                startActivityForResult(action, uri, type, extras, packagename, classname)
                startActivityForResultIntent(intent)
                startActivityIntent(intent, wait)
                startActivity(action, uri, type, extras, wait, packagename, classname)
            SendBroadcast APIs
                sendBroadcast(action, uri, type, extras, packagename, classname)
                sendBroadcastIntent(intent)
            Vibrate
                vibrate(intent)
            NetworkStatus
                getNetworkStatus()
            PackageVersion APIs
                requiredVersion(requiredVersion)
                getPackageVersionCode(packageName)
                getPackageVersion(packageName)
            System APIs
                getConstants(classname)
                environment()
                log(message)
            SendEmail
                sendEmail(to, subject, body, attachmentUri)
            Toast, getInput, getPassword, notify APIs
                makeToast(message)
                getInput(title, message)
                getPassword(title, message)
                notify(title, message, url)
        ApplicationManagerFacade
            Manager APIs
                getLaunchableApplications()
                launch(classname)
                getRunningPackages()
                forceStopPackage(packageName)
        CameraFacade
            cameraCapturePicture(targetPath)
            cameraInteractiveCapturePicture(targetPath)
        CommonIntentsFacade
            Barcode
                scanBarcode()
            View APIs
                pick(uri)
                view(uri, type, extras)
                viewMap(query)
                viewContacts()
                viewHtml(path)
                search(query)
        ContactsFacade
            pickContact()
            pickPhone()
            contactsGetAttributes()
            contactsGetIds()
            contactsGet(attributes)
            contactsGetById(id)
            contactsGetCount()
            queryContent(uri, attributes, selection, selectionArgs, order)
            queryAttributes(uri)
        EventFacade
            eventClearBuffer()
            eventRegisterForBroadcast(category, enqueue)
            eventUnregisterForBroadcast(category)
            eventGetBrodcastCategories()
            eventPoll(number_of_events)
            eventWaitFor(eventName, timeout)
            eventWait(timeout)
            eventPost(name, data, enqueue)
            rpcPostEvent(name, data)
            receiveEvent()
            waitForEvent(eventName, timeout)
            startEventDispatcher(port)
            stopEventDispatcher()
        LocationFacade
            Providers APIs
                locationProviders()
                locationProviderEnabled(provider)
            Location APIs
                startLocating(minDistance, minUpdateDistance)
                readLocation()
                stopLocating()
                getLastKnownLocation()
            GEO
                geocode(latitude, longitude, maxResults)
        PhoneFacade
            PhoneStat APIs
                startTrackingPhoneState()
                readPhoneState()
                stopTrackingPhoneState()
            Call & Dia APIs
                phoneCall(uri)
                phoneCallNumber(number)
                phoneDial(uri)
                phoneDialNumber(number)
            Get information APIs
                getCellLocation()
                getNetworkOperator()
                getNetworkOperatorName()
                getNetworkType()
                getPhoneType()
                getSimCountryIso()
                getSimOperator()
                getSimOperatorName()
                getSimSerialNumber()
                getSimState()
                getSubscriberId()
                getVoiceMailAlphaTag()
                getVoiceMailNumber()
                checkNetworkRoaming()
                getDeviceId()
                getDeviceSoftwareVersion()
                getLine1Number()
                getNeighboringCellInfo()
        MediaRecorderFacade
            Audio
                recorderStartMicrophone(targetPath)
            Video APIs
                recorderStartVideo(targetPath, duration, videoSize)
                recorderCaptureVideo(targetPath, duration, recordAudio)
                startInteractiveVideoRecording(path)
            Stop
                recorderStop()
        SensorManagerFacade
            Start & Stop
                startSensingTimed(sensorNumber, delayTime)
                startSensingThreshold(ensorNumber, threshold, axis)
                startSensing(sampleSize)
                stopSensing()
            Read data APIs
                readSensors()
                sensorsGetAccuracy()
                sensorsGetLight()
                sensorsReadAccelerometer()
                sensorsReadMagnetometer()
                sensorsReadOrientation()
        SettingsFacade
            Screen
                setScreenTimeout(value)
                getScreenTimeout()
            AirplanerMode
                checkAirplaneMode()
                toggleAirplaneMode(enabled)
            Ringer Silent Mode
                checkRingerSilentMode()
                toggleRingerSilentMode(enabled)
            Vibrate Mode
                toggleVibrateMode(enabled)
                getVibrateMode(ringer)
            Ringer & Media Volume
                getMaxRingerVolume()
                getRingerVolume()
                setRingerVolume(volume)
                getMaxMediaVolume()
                Returns the maximum media volume
                getMediaVolume()
                setMediaVolume(volume)
            Screen Brightness
                getScreenBrightness()
                setScreenBrightness(value)
                checkScreenOn()
        SmsFacade
            smsSend(destinationAddress, text)
            smsGetMessageCount(unreadOnly, folder)
            smsGetMessageIds(unreadOnly, folder)
            smsGetMessages(unreadOnly, folder, attributes)
            smsGetMessageById(id, attributes)
            smsGetAttributes()
            smsDeleteMessage(id)
            smsMarkMessageRead(ids, read)
        SpeechRecognitionFacade
            recognizeSpeech(prompt, language, languageModel)
        ToneGeneratorFacade
            generateDtmfTones(phoneNumber, toneDuration)
        WakeLockFacade
            wakeLockAcquireFull()
            wakeLockAcquirePartial()
            wakeLockAcquireBright()
            wakeLockAcquireDim()
            wakeLockRelease()
        WifiFacade
            wifiGetScanResults()
            wifiLockAcquireFull()
            wifiLockAcquireScanOnly()
            wifiLockRelease()
            wifiStartScan()
            checkWifiState()
            toggleWifiState(enabled)
            wifiDisconnect()
            wifiGetConnectionInfo()
            wifiReassociate()
            wifiReconnect()
        BatteryManagerFacade
            readBatteryData()
            batteryStartMonitoring()
            batteryStopMonitoring()
            batteryGetStatus()
            batteryGetHealth()
            batteryGetPlugType()
            batteryCheckPresent()
            batteryGetLevel()
            batteryGetVoltage()
            batteryGetTemperature()
            batteryGetTechnology()
        ActivityResultFacade
            setResultBoolean(resultCode, resultValue)
            setResultByte(resultCode, resultValue)
            setResultShort(resultCode, resultValue)
            setResultChar(resultCode, resultValue)
            setResultInteger(resultCode, resultValue)
            setResultLong(resultCode, resultValue)
            setResultFloat(resultCode, resultValue)
            setResultDouble(resultCode, resultValue)
            setResultString(resultCode, resultValue)
            setResultBooleanArray(resultCode, resultValue)
            setResultByteArray(resultCode, resultValue)
            setResultShortArray(resultCode, resultValue)
            setResultCharArray(resultCode, resultValue)
            setResultIntegerArray(resultCode, resultValue)
            setResultLongArray(resultCode, resultValue)
            setResultFloatArray(resultCode, resultValue)
            setResultDoubleArray(resultCode, resultValue)
            setResultStringArray(resultCode, resultValue)
            setResultSerializable(resultCode, resultValue)
        MediaPlayerFacade
            Control
                mediaPlay(url, tag, play)
                mediaPlayPause(tag)
                mediaPlayStart(tag)
                mediaPlayClose(tag)
                mediaIsPlaying(tag)
                mediaPlaySetLooping(enabled, tag)
                mediaPlaySeek(msec, tag)
            Get Information
                mediaPlayInfo(tag)
                mediaPlayList()
        PreferencesFacade
            prefGetValue(key, filename)
            prefPutValue(key, value, filename)
            prefGetAll(filename)
        QPyInterfaceFacade
            executeQPy(script)
        TextToSpeechFacade
            ttsSpeak(message)
            ttsIsSpeaking()
        EyesFreeFacade
            ttsSpeak(message)
        BluetoothFacade
            bluetoothActiveConnections()
            bluetoothWriteBinary(base64, connID)
            bluetoothReadBinary(bufferSize, connID)
            bluetoothConnect(uuid, address)
            bluetoothAccept(uuid, timeout)
            bluetoothMakeDiscoverable(duration)
            bluetoothWrite(ascii, connID)
            bluetoothReadReady(connID)
            bluetoothRead(bufferSize, connID)
            bluetoothReadLine(connID)
            bluetoothGetRemoteDeviceName(address)
            bluetoothGetLocalName()
            bluetoothSetLocalName(name)
            bluetoothGetScanMode()
            bluetoothGetConnectedDeviceName(connID)
            checkBluetoothState()
            toggleBluetoothState(enabled, prompt)
            bluetoothStop(connID)
            bluetoothGetLocalAddress()
            bluetoothDiscoveryStart()
            bluetoothDiscoveryCancel()
            bluetoothIsDiscovering()
        SignalStrengthFacade
            startTrackingSignalStrengths()
            readSignalStrengths()
            stopTrackingSignalStrengths()
        WebCamFacade
            webcamStart(resolutionLevel, jpegQuality, port)
            webcamAdjustQuality(resolutionLevel, jpegQuality)
            cameraStartPreview(resolutionLevel, jpegQuality, filepath)
            cameraStopPreview()
        UiFacade
            Dialog
                dialogCreateInput(title, message, defaultText, inputType)
                dialogCreatePassword(title, message)
                dialogGetInput(title, message, defaultText)
                dialogGetPassword(title, message)
                dialogCreateSeekBar(start, maximum, title)
                dialogCreateTimePicker(hour, minute, is24hour)
                dialogCreateDatePicker(year, month, day)
            NFC
                NFCBeamMessage(content, title, message)
                dialogCreateNFCBeamSlave(title, message)
            Progress
                dialogCreateSpinnerProgress(message, maximumProgress)
                dialogSetCurrentProgress(current)
                dialogSetMaxProgress(max)
                dialogCreateHorizontalProgress(title, message, maximumProgress)
            Alert
                dialogCreateAlert(title, message)
            Dialog Control
                dialogSetPositiveButtonText(text)
                dialogSetNegativeButtonText(text)
                dialogSetNeutralButtonText(text)
                dialogSetItems(items)
                dialogSetSingleChoiceItems(items, selected)
                dialogSetMultiChoiceItems(items, selected)
                addContextMenuItem(label, event, eventData)
                addOptionsMenuItem(label, event, eventData, iconName)
                dialogGetResponse()
                dialogGetSelectedItems()
                dialogDismiss()
                dialogShow()
            Layout
                fullShow(layout)
                fullDismiss()
                fullQuery()
                fullQueryDetail(id)
                fullSetProperty(id)
                fullSetList(id, list)
                fullKeyOverride(keycodes, enable)
            WebView
                webViewShow()
        USB Host Serial Facade
            Requirements
            Status
            Author
            APIs
                usbserialGetDeviceList()
                usbserialDisconnect(connID)
                usbserialActiveConnections()
                usbserialWriteBinary(base64, connID)
                usbserialReadBinary(bufferSize, connID)
                usbserialConnect(hash, options)
                usbserialHostEnable()
                usbserialWrite(String ascii, String connID)
                usbserialReadReady(connID)
                usbserialRead(connID, bufferSize)
                usbserialGetDeviceName(connID)

AndroidFacade
Clipboard APIs
setClipboard(text)

    Put text in the clipboard

    Parameters: text (str) – text

getClipboard(text)

    Read text from the clipboard

    Return: The text in the clipboard

from androidhelper import Android
droid = Android()
#setClipboard
droid.setClipboard("Hello World")
#getClipboard
clipboard = droid.getClipboard().result
Intent & startActivity APIs
makeIntent(action, uri, type, extras, categories, packagename, classname, flags)

    Starts an activity and returns the result

    Parameters:
    action (str) – action
    uri(Optional) (str) – uri
    type(Optional) (str) – MIME type/subtype of the URI
    extras(Optional) (object) – a Map of extras to add to the Intent
    categories(Optional) (list) – a List of categories to add to the Intent
    packagename(Optional) (str) – name of package. If used, requires classname to be useful
    classname(Optional) (str) – name of class. If used, requires packagename to be useful
    flags(Optional) (int) – Intent flags

    Return:
    An object representing an Intent

getIntent()

    Returns the intent that launched the script

startActivityForResult(action, uri, type, extras, packagename, classname)

    Starts an activity and returns the result

    Parameters:
    action (str) – action
    uri(Optional) (str) – uri
    type(Optional) (str) – MIME type/subtype of the URI
    extras(Optional) (object) – a Map of extras to add to the Intent
    packagename(Optional) (str) – name of package. If used, requires classname to be useful
    classname(Optional) (str) – name of class. If used, requires packagename to be useful

    Return:
    A Map representation of the result Intent

startActivityForResultIntent(intent)

    Starts an activity and returns the result

    Parameters: intent (Intent) – Intent in the format as returned from makeIntent

    Return: A Map representation of the result Intent

startActivityIntent(intent, wait)

    Starts an activity

    Parameters:
    intent (Intent) – Intent in the format as returned from makeIntent
    wait(Optional) (bool) – block until the user exits the started activity

startActivity(action, uri, type, extras, wait, packagename, classname)

    Starts an activity

    Parameters:
    action (str) – action
    uri(Optional) (str) – uri
    type(Optional) (str) – MIME type/subtype of the URI
    extras(Optional) (object) – a Map of extras to add to the Intent
    wait(Optional) (bool) – block until the user exits the started activity
    packagename(Optional) (str) – name of package. If used, requires classname to be useful
    classname(Optional) (str) – name of class. If used, requires packagename to be useful

SendBroadcast APIs
sendBroadcast(action, uri, type, extras, packagename, classname)

    Send a broadcast

    Parameters:
    action (str) – action
    uri(Optional) (str) – uri
    type(Optional) (str) – MIME type/subtype of the URI
    extras(Optional) (object) – a Map of extras to add to the Intent
    packagename(Optional) (str) – name of package. If used, requires classname to be useful
    classname(Optional) (str) – name of class. If used, requires packagename to be useful

sendBroadcastIntent(intent)

    Send a broadcast

    Parameters: intent (Intent) – Intent in the format as returned from makeIntent

Vibrate
vibrate(intent)

    Vibrates the phone or a specified duration in milliseconds

    Parameters: duration (int) – duration in milliseconds

NetworkStatus
getNetworkStatus()

    Returns the status of network connection

PackageVersion APIs
requiredVersion(requiredVersion)

    Checks if version of QPython SL4A is greater than or equal to the specified version

    Parameters: requiredVersion (int) – requiredVersion

    Return: true or false

getPackageVersionCode(packageName)

    Returns package version code

    Parameters: packageName (str) – packageName

    Return: Package version code

getPackageVersion(packageName)

    Returns package version name

    Parameters: packageName (str) – packageName

    Return: Package version name

System APIs
getConstants(classname)

    Get list of constants (static final fields) for a class

    Parameters: classname (str) – classname

    Return: list

environment()

    A map of various useful environment details

    Return: environment map object includes id, display, offset, TZ, SDK, download, appcache, availblocks, blocksize, blockcount, sdcard

log(message)

Writes message to logcat

    Parameters: message (str) – message

SendEmail
sendEmail(to, subject, body, attachmentUri)

    Launches an activity that sends an e-mail message to a given recipient

    Parameters:
    to (str) – A comma separated list of recipients
    subject (str) – subject
    body (str) – mail body
    attachmentUri(Optional) (str) – message

Toast, getInput, getPassword, notify APIs
makeToast(message)

    Displays a short-duration Toast notification

    Parameters: message (str) – message

getInput(title, message)

    Queries the user for a text input

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box

getPassword(title, message)

    Queries the user for a password

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box

notify(title, message, url)

    Displays a notification that will be canceled when the user clicks on it

    Parameters:
    title (str) – title
    message (str) – message
    url(optional) (str) – url
    ::

import androidhelper
droid = androidhelper.Android()
droid.notify(‘Hello’,’QPython’,’http://qpython.org’)
# you could set the 3rd parameter None also
ApplicationManagerFacade
Manager APIs
getLaunchableApplications()

    Returns a list of all launchable application class names

    Return: map object

launch(classname)

    Start activity with the given class name

    Parameters: classname (str) – classname

getRunningPackages()

    Returns a list of packages running activities or services

    Return: List of packages running activities

forceStopPackage(packageName)

    Force stops a package

    Parameters: packageName (str) – packageName

CameraFacade
cameraCapturePicture(targetPath)

    Take a picture and save it to the specified path

    Return: A map of Booleans autoFocus and takePicture where True indicates success

cameraInteractiveCapturePicture(targetPath)

    Starts the image capture application to take a picture and saves it to the specified path

CommonIntentsFacade
Barcode
scanBarcode()

    Starts the barcode scanner

    Return: A Map representation of the result Intent

View APIs
pick(uri)

    Display content to be picked by URI (e.g. contacts)

    Return: A map of result values

view(uri, type, extras)

    Start activity with view action by URI (i.e. browser, contacts, etc.)

viewMap(query)

    Opens a map search for query (e.g. pizza, 123 My Street)

viewContacts()

    Opens the list of contacts

viewHtml(path)

    Opens the browser to display a local HTML file

search(query)

    Starts a search for the given query

ContactsFacade
pickContact()

    Displays a list of contacts to pick from

    Return: A map of result values

pickPhone()

    Displays a list of phone numbers to pick from

    Return: The selected phone number

contactsGetAttributes()

    Returns a List of all possible attributes for contacts

    Return: a List of contacts as Maps

contactsGetIds()

    Returns a List of all contact IDs

contactsGet(attributes)

    Returns a List of all contacts

contactsGetById(id)

    Returns contacts by ID

contactsGetCount()

    Returns the number of contacts

queryContent(uri, attributes, selection, selectionArgs, order)

    Content Resolver Query

    Return: result of query as Maps

queryAttributes(uri)

    Content Resolver Query Attributes

    Return: a list of available columns for a given content uri

EventFacade
eventClearBuffer()

    Clears all events from the event buffer

eventRegisterForBroadcast(category, enqueue)

    Registers a listener for a new broadcast signal

eventUnregisterForBroadcast(category)

    Stop listening for a broadcast signal

eventGetBrodcastCategories()

    Lists all the broadcast signals we are listening for

eventPoll(number_of_events)

    Returns and removes the oldest n events (i.e. location or sensor update, etc.) from the event buffer

    Return: A List of Maps of event properties

eventWaitFor(eventName, timeout)

    Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer

    Return: Map of event properties

eventWait(timeout)

    Blocks until an event occurs. The returned event is removed from the buffer

    Return: Map of event properties

eventPost(name, data, enqueue)

    Post an event to the event queue

rpcPostEvent(name, data)

    Post an event to the event queue

receiveEvent()

    Returns and removes the oldest event (i.e. location or sensor update, etc.) from the event buffer

    Return: Map of event properties

waitForEvent(eventName, timeout)

    Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer

    Return: Map of event properties

startEventDispatcher(port)

    Opens up a socket where you can read for events posted

stopEventDispatcher()

    Stops the event server, you can’t read in the port anymore

LocationFacade
Providers APIs
locationProviders()

    Returns availables providers on the phone

locationProviderEnabled(provider)

    Ask if provider is enabled

Location APIs
startLocating(minDistance, minUpdateDistance)

    Starts collecting location data

readLocation()

    Returns the current location as indicated by all available providers

    Return: A map of location information by provider

stopLocating()

    Stops collecting location data

getLastKnownLocation()

    Returns the last known location of the device

    Return: A map of location information by provider

Droid = androidhelper.Android()
location = Droid.getLastKnownLocation().result
location = location.get('network', location.get('gps'))
GEO
geocode(latitude, longitude, maxResults)

    Returns a list of addresses for the given latitude and longitude

    Return: A list of addresses

PhoneFacade
PhoneStat APIs
startTrackingPhoneState()

    Starts tracking phone state

readPhoneState()

    Returns the current phone state and incoming number

    Return: A Map of “state” and “incomingNumber”

stopTrackingPhoneState()

    Stops tracking phone state

Call & Dia APIs
phoneCall(uri)

    Calls a contact/phone number by URI

phoneCallNumber(number)

    Calls a phone number

phoneDial(uri)

    Dials a contact/phone number by URI

phoneDialNumber(number)

    Dials a phone number

Get information APIs
getCellLocation()

    Returns the current cell location

getNetworkOperator()

    Returns the numeric name (MCC+MNC) of current registered operator

getNetworkOperatorName()

    Returns the alphabetic name of current registered operator

getNetworkType()

    Returns a the radio technology (network type) currently in use on the device

getPhoneType()

    Returns the device phone type

getSimCountryIso()

    Returns the ISO country code equivalent for the SIM provider’s country code

getSimOperator()

    Returns the MCC+MNC (mobile country code + mobile network code) of the provider of the SIM. 5 or 6 decimal digits

getSimOperatorName()

    Returns the Service Provider Name (SPN)

getSimSerialNumber()

    Returns the serial number of the SIM, if applicable. Return null if it is unavailable

getSimState()

    Returns the state of the device SIM card

getSubscriberId()

    Returns the unique subscriber ID, for example, the IMSI for a GSM phone. Return null if it is unavailable

getVoiceMailAlphaTag()

    Retrieves the alphabetic identifier associated with the voice mail number

getVoiceMailNumber()

    Returns the voice mail number. Return null if it is unavailable

checkNetworkRoaming()

    Returns true if the device is considered roaming on the current network, for GSM purposes

getDeviceId()

    Returns the unique device ID, for example, the IMEI for GSM and the MEID for CDMA phones. Return null if device ID is not available

getDeviceSoftwareVersion()

    Returns the software version number for the device, for example, the IMEI/SV for GSM phones. Return null if the software version is not available

getLine1Number()

    Returns the phone number string for line 1, for example, the MSISDN for a GSM phone. Return null if it is unavailable

getNeighboringCellInfo()

    Returns the neighboring cell information of the device

MediaRecorderFacade
Audio
recorderStartMicrophone(targetPath)

    Records audio from the microphone and saves it to the given location

Video APIs
recorderStartVideo(targetPath, duration, videoSize)

    Records video from the camera and saves it to the given location. Duration specifies the maximum duration of the recording session. If duration is 0 this method will return and the recording will only be stopped when recorderStop is called or when a scripts exits. Otherwise it will block for the time period equal to the duration argument. videoSize: 0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480.

recorderCaptureVideo(targetPath, duration, recordAudio)

    Records video (and optionally audio) from the camera and saves it to the given location. Duration specifies the maximum duration of the recording session. If duration is not provided this method will return immediately and the recording will only be stopped when recorderStop is called or when a scripts exits. Otherwise it will block for the time period equal to the duration argument.

startInteractiveVideoRecording(path)

    Starts the video capture application to record a video and saves it to the specified path

Stop
recorderStop()

    Stops a previously started recording

SensorManagerFacade
Start & Stop
startSensingTimed(sensorNumber, delayTime)

    Starts recording sensor data to be available for polling

startSensingThreshold(ensorNumber, threshold, axis)

    Records to the Event Queue sensor data exceeding a chosen threshold

startSensing(sampleSize)

    Starts recording sensor data to be available for polling

stopSensing()

    Stops collecting sensor data

Read data APIs
readSensors()

    Returns the most recently recorded sensor data

sensorsGetAccuracy()

    Returns the most recently received accuracy value

sensorsGetLight()

    Returns the most recently received light value

sensorsReadAccelerometer()

    Returns the most recently received accelerometer values

    Return: a List of Floats [(acceleration on the) X axis, Y axis, Z axis]

sensorsReadMagnetometer()

    Returns the most recently received magnetic field values

    Return: a List of Floats [(magnetic field value for) X axis, Y axis, Z axis]

sensorsReadOrientation()

    Returns the most recently received orientation values

    Return: a List of Doubles [azimuth, pitch, roll]

Droid = androidhelper.Android()
Droid.startSensingTimed(1, 250)
sensor = Droid.sensorsReadOrientation().result
Droid.stopSensing()
SettingsFacade
Screen
setScreenTimeout(value)

    Sets the screen timeout to this number of seconds

    Return: The original screen timeout

getScreenTimeout()

    Gets the screen timeout

    Return: the current screen timeout in seconds

AirplanerMode
checkAirplaneMode()

    Checks the airplane mode setting

    Return: True if airplane mode is enabled

toggleAirplaneMode(enabled)

    Toggles airplane mode on and off

    Return: True if airplane mode is enabled

Ringer Silent Mode
checkRingerSilentMode()

    Checks the ringer silent mode setting

    Return: True if ringer silent mode is enabled

toggleRingerSilentMode(enabled)

    Toggles ringer silent mode on and off

    Return: True if ringer silent mode is enabled

Vibrate Mode
toggleVibrateMode(enabled)

    Toggles vibrate mode on and off. If ringer=true then set Ringer setting, else set Notification setting

    Return: True if vibrate mode is enabled

getVibrateMode(ringer)

    Checks Vibration setting. If ringer=true then query Ringer setting, else query Notification setting

    Return: True if vibrate mode is enabled

Ringer & Media Volume
getMaxRingerVolume()

    Returns the maximum ringer volume

getRingerVolume()

    Returns the current ringer volume

setRingerVolume(volume)

    Sets the ringer volume

getMaxMediaVolume()
Returns the maximum media volume
getMediaVolume()

    Returns the current media volume

setMediaVolume(volume)

    Sets the media volume

Screen Brightness
getScreenBrightness()

    Returns the screen backlight brightness

    Return: the current screen brightness between 0 and 255

setScreenBrightness(value)

    Sets the the screen backlight brightness

    Return: the original screen brightness

checkScreenOn()

    Checks if the screen is on or off (requires API level 7)

    Return: True if the screen is currently on

SmsFacade
smsSend(destinationAddress, text)

    Sends an SMS

    Parameters:
    destinationAddress (str) – typically a phone number
    text (str) –

smsGetMessageCount(unreadOnly, folder)

    Returns the number of messages

    Parameters:
    unreadOnly (bool) – typically a phone number
    folder(optional) (str) – default “inbox”

smsGetMessageIds(unreadOnly, folder)

    Returns a List of all message IDs

    Parameters:
    unreadOnly (bool) – typically a phone number
    folder(optional) (str) – default “inbox”

smsGetMessages(unreadOnly, folder, attributes)

    Returns a List of all messages

    Parameters:
    unreadOnly (bool) – typically a phone number
    folder (str) – default “inbox”
    attributes(optional) (list) – attributes

    Return:
    a List of messages as Maps

smsGetMessageById(id, attributes)

Returns message attributes

    Parameters:
    id (int) – message ID
    attributes(optional) (list) – attributes

    Return:
    a List of messages as Maps

smsGetAttributes()

    Returns a List of all possible message attributes

smsDeleteMessage(id)

    Deletes a message

    Parameters: id (int) – message ID

    Return: True if the message was deleted

smsMarkMessageRead(ids, read)

    Marks messages as read

    Parameters:
    ids (list) – List of message IDs to mark as read
    read (bool) – true or false

    Return:
    number of messages marked read

SpeechRecognitionFacade
recognizeSpeech(prompt, language, languageModel)

    Recognizes user’s speech and returns the most likely result

    Parameters:
    prompt(optional) (str) – text prompt to show to the user when asking them to speak
    language(optional) (str) – language override to inform the recognizer that it should expect speech in a language different than the one set in the java.util.Locale.getDefault()
    languageModel(optional) (str) – informs the recognizer which speech model to prefer (see android.speech.RecognizeIntent)

    Return:
    An empty string in case the speech cannot be recongnized

ToneGeneratorFacade
generateDtmfTones(phoneNumber, toneDuration)

    Generate DTMF tones for the given phone number

    Parameters:
    phoneNumber (str) – phone number
    toneDuration(optional) (int) – default 100, duration of each tone in milliseconds

WakeLockFacade
wakeLockAcquireFull()

    Acquires a full wake lock (CPU on, screen bright, keyboard bright)

wakeLockAcquirePartial()

    Acquires a partial wake lock (CPU on)

wakeLockAcquireBright()

    Acquires a bright wake lock (CPU on, screen bright)

wakeLockAcquireDim()

    Acquires a dim wake lock (CPU on, screen dim)

wakeLockRelease()

    Releases the wake lock

WifiFacade
wifiGetScanResults()

    Returns the list of access points found during the most recent Wifi scan

wifiLockAcquireFull()

    Acquires a full Wifi lock

wifiLockAcquireScanOnly()

    Acquires a scan only Wifi lock

wifiLockRelease()

    Releases a previously acquired Wifi lock

wifiStartScan()

    Starts a scan for Wifi access points

    Return: True if the scan was initiated successfully

checkWifiState()

    Checks Wifi state

    Return: True if Wifi is enabled

toggleWifiState(enabled)

    Toggle Wifi on and off

    Parameters: enabled(optional) (bool) – enabled

    Return: True if Wifi is enabled

wifiDisconnect()

    Disconnects from the currently active access point

    Return: True if the operation succeeded

wifiGetConnectionInfo()

    Returns information about the currently active access point

wifiReassociate()

    Returns information about the currently active access point

    Return: True if the operation succeeded

wifiReconnect()

    Reconnects to the currently active access point

    Return: True if the operation succeeded

BatteryManagerFacade
readBatteryData()

    Returns the most recently recorded battery data

batteryStartMonitoring()

    Starts tracking battery state

batteryStopMonitoring()

    Stops tracking battery state

batteryGetStatus()

    Returns the most recently received battery status data: 1 - unknown; 2 - charging; 3 - discharging; 4 - not charging; 5 - full

batteryGetHealth()

    Returns the most recently received battery health data: 1 - unknown; 2 - good; 3 - overheat; 4 - dead; 5 - over voltage; 6 - unspecified failure

batteryGetPlugType()

    Returns the most recently received plug type data: -1 - unknown 0 - unplugged 1 - power source is an AC charger 2 - power source is a USB port

batteryCheckPresent()

    Returns the most recently received battery presence data

batteryGetLevel()

    Returns the most recently received battery level (percentage)

batteryGetVoltage()

    Returns the most recently received battery voltage

batteryGetTemperature()

    Returns the most recently received battery temperature

batteryGetTechnology()

    Returns the most recently received battery technology data

ActivityResultFacade
setResultBoolean(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultByte(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultShort(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultChar(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultInteger(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultLong(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultFloat(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultDouble(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultString(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultBooleanArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultByteArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultShortArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultCharArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultIntegerArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultLongArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultFloatArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultDoubleArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultStringArray(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

setResultSerializable(resultCode, resultValue)

    Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value

    Parameters:
    resultCode (int) –
    resultValue (byte) –

MediaPlayerFacade
Control
mediaPlay(url, tag, play)

    Open a media file

    Parameters:
    url (str) – url of media resource
    tag(optional) (str) – string identifying resource (default=default)
    play(optional) (bool) – start playing immediately

    Return:
    true if play successful

mediaPlayPause(tag)

    pause playing media file

    Parameters: tag (str) – string identifying resource (default=default)

    Return: true if successful

mediaPlayStart(tag)

    start playing media file

    Parameters: tag (str) – string identifying resource (default=default)

    Return: true if successful

mediaPlayClose(tag)

    Close media file

    Parameters: tag (str) – string identifying resource (default=default)

    Return: true if successful

mediaIsPlaying(tag)

    Checks if media file is playing

    Parameters: tag (str) – string identifying resource (default=default)

    Return: true if successful

mediaPlaySetLooping(enabled, tag)

    Set Looping

    Parameters:
    enabled (bool) – default true
    tag (str) – string identifying resource (default=default)

    Return:
    True if successful

mediaPlaySeek(msec, tag)

    Seek To Position

    Parameters:
    msec (int) – default true
    tag (str) – string identifying resource (default=default)

    Return:
    New Position (in ms)

Get Information
mediaPlayInfo(tag)

    Information on current media

    Parameters: tag (str) – string identifying resource (default=default)

    Return: Media Information

mediaPlayList()

    Lists currently loaded media

    Return: List of Media Tags

PreferencesFacade
prefGetValue(key, filename)

    Read a value from shared preferences

    Parameters:
    key (str) – key
    filename(optional) (str) – Desired preferences file. If not defined, uses the default Shared Preferences.

prefPutValue(key, value, filename)

    Write a value to shared preferences

    Parameters:
    key (str) – key
    value (str) – value
    filename(optional) (str) – Desired preferences file. If not defined, uses the default Shared Preferences.

prefGetAll(filename)

    Get list of Shared Preference Values

    Parameters: filename(optional) (str) – Desired preferences file. If not defined, uses the default Shared Preferences.

QPyInterfaceFacade
executeQPy(script)

    Execute a qpython script by absolute path

    Parameters: script (str) – The absolute path of the qpython script

    Return: bool

TextToSpeechFacade
ttsSpeak(message)

    Speaks the provided message via TTS

    Parameters: message (str) – message

ttsIsSpeaking()

    Returns True if speech is currently in progress

EyesFreeFacade
ttsSpeak(message)

Speaks the provided message via TTS

    Parameters: message (str) – message

BluetoothFacade
bluetoothActiveConnections()

    Returns active Bluetooth connections

bluetoothWriteBinary(base64, connID)

    Send bytes over the currently open Bluetooth connection

    Parameters:
    base64 (str) – A base64 encoded String of the bytes to be sent
    connID(optional) (str) – Connection id

bluetoothReadBinary(bufferSize, connID)

    Read up to bufferSize bytes and return a chunked, base64 encoded string

    Parameters:
    bufferSize (int) – default 4096
    connID(optional) (str) – Connection id

bluetoothConnect(uuid, address)

    Connect to a device over Bluetooth. Blocks until the connection is established or fails

    Parameters:
    uuid (str) – The UUID passed here must match the UUID used by the server device
    address(optional) (str) – The user will be presented with a list of discovered devices to choose from if an address is not provided

    Return:
    True if the connection was established successfully

bluetoothAccept(uuid, timeout)

    Listens for and accepts a Bluetooth connection. Blocks until the connection is established or fails

    Parameters:
    uuid (str) – The UUID passed here must match the UUID used by the server device
    timeout (int) – How long to wait for a new connection, 0 is wait for ever (default=0)

bluetoothMakeDiscoverable(duration)

    Requests that the device be discoverable for Bluetooth connections

    Parameters: duration (int) – period of time, in seconds, during which the device should be discoverable (default=300)

bluetoothWrite(ascii, connID)

    Sends ASCII characters over the currently open Bluetooth connection

    Parameters:
    ascii (str) – text
    connID (str) – Connection id

bluetoothReadReady(connID)

    Sends ASCII characters over the currently open Bluetooth connection

    Parameters:
    ascii (str) – text
    connID (str) – Connection id

bluetoothRead(bufferSize, connID)

    Read up to bufferSize ASCII characters

    Parameters:
    bufferSize (int) – default=4096
    connID(optional) (str) – Connection id

bluetoothReadLine(connID)

    Read the next line

    Parameters: connID(optional) (str) – Connection id

bluetoothGetRemoteDeviceName(address)

    Queries a remote device for it’s name or null if it can’t be resolved

    Parameters: address (str) – Bluetooth Address For Target Device

bluetoothGetLocalName()

    Gets the Bluetooth Visible device name

bluetoothSetLocalName(name)

    Sets the Bluetooth Visible device name, returns True on success

    Parameters: name (str) – New local name

bluetoothGetScanMode()

    Gets the scan mode for the local dongle. Return values: -1 when Bluetooth is disabled. 0 if non discoverable and non connectable. 1 connectable non discoverable. 3 connectable and discoverable.

bluetoothGetConnectedDeviceName(connID)

    Returns the name of the connected device

    Parameters: connID (str) – Connection id

checkBluetoothState()

    Checks Bluetooth state

    Return: True if Bluetooth is enabled

toggleBluetoothState(enabled, prompt)

    Toggle Bluetooth on and off

    Parameters:
    enabled (bool) –
    prompt (str) – Prompt the user to confirm changing the Bluetooth state, default=true

    Return:
    True if Bluetooth is enabled

bluetoothStop(connID)

    Stops Bluetooth connection

    Parameters: connID (str) – Connection id

bluetoothGetLocalAddress()

    Returns the hardware address of the local Bluetooth adapter

bluetoothDiscoveryStart()

    Start the remote device discovery process

    Return: true on success, false on error

bluetoothDiscoveryCancel()

    Cancel the current device discovery process

    Return: true on success, false on error

bluetoothIsDiscovering()

    Return true if the local Bluetooth adapter is currently in the device discovery process

SignalStrengthFacade
startTrackingSignalStrengths()

    Starts tracking signal strengths

readSignalStrengths()

    Returns the current signal strengths

    Return: A map of gsm_signal_strength

stopTrackingSignalStrengths()

    Stops tracking signal strength

WebCamFacade
webcamStart(resolutionLevel, jpegQuality, port)

    Starts an MJPEG stream and returns a Tuple of address and port for the stream

    Parameters:
    resolutionLevel (int) – increasing this number provides higher resolution (default=0)
    jpegQuality (int) – a number from 0-10 (default=20)
    port (int) – If port is specified, the webcam service will bind to port, otherwise it will pick any available port (default=0)

webcamAdjustQuality(resolutionLevel, jpegQuality)

    Adjusts the quality of the webcam stream while it is running

    Parameters:
    resolutionLevel (int) – increasing this number provides higher resolution (default=0)
    jpegQuality (int) – a number from 0-10 (default=20)

cameraStartPreview(resolutionLevel, jpegQuality, filepath)

    Start Preview Mode. Throws ‘preview’ events

    Parameters:
    resolutionLevel (int) – increasing this number provides higher resolution (default=0)
    jpegQuality (int) – a number from 0-10 (default=20)
    filepath (str) – Path to store jpeg files

    Return:
    True if successful

cameraStopPreview()

    Stop the preview mode

UiFacade
Dialog
dialogCreateInput(title, message, defaultText, inputType)

    Create a text input dialog

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box
    defaultText(optional) (str) – text to insert into the input box
    inputType(optional) (str) – type of input data, ie number or text

dialogCreatePassword(title, message)

    Create a password input dialog

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box

dialogGetInput(title, message, defaultText)

    Create a password input dialog

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box
    defaultText(optional) (str) – text to insert into the input box

dialogGetPassword(title, message)

    Queries the user for a password

    Parameters:
    title (str) – title of the password box
    message (str) – message to display above the input box

dialogCreateSeekBar(start, maximum, title)

    Create seek bar dialog

    Parameters:
    start (int) – default=50
    maximum (int) – default=100
    title (int) – title

dialogCreateTimePicker(hour, minute, is24hour)

    Create time picker dialog

    Parameters:
    hour (int) – default=0
    miute (int) – default=0
    is24hour (bool) – default=false

dialogCreateDatePicker(year, month, day)

    Create date picker dialog

    Parameters:
    year (int) – default=1970
    month (int) – default=1
    day (int) – default=1

NFC

Data structs QPython NFC json result

{
"role": <role>, # could be self/master/slave
"stat": <stat>, # could be ok / fail / cancl
"message": <message get>
}
APIs

dialogCreateNFCBeamMaster(title, message, inputType)

    Create a dialog where you could create a qpython beam master

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box
    inputType(optional) (str) – type of input data, ie number or text

NFCBeamMessage(content, title, message)

    Create a dialog where you could create a qpython beam master

    Parameters:
    content (str) – message you want to sent
    title (str) – title of the input box
    message (str) – message to display above the input box
    inputType(optional) (str) – type of input data, ie number or text

dialogCreateNFCBeamSlave(title, message)

    Create a qpython beam slave

    Parameters:
    title (str) – title of the input box
    message (str) – message to display above the input box

Progress
dialogCreateSpinnerProgress(message, maximumProgress)

    Create a spinner progress dialog

    Parameters:
    message(optional) (str) – message
    maximunProgress(optional) (int) – dfault=100

dialogSetCurrentProgress(current)

    Set progress dialog current value

    Parameters: current (int) – current

dialogSetMaxProgress(max)

    Set progress dialog maximum value

    Parameters: max (int) – max

dialogCreateHorizontalProgress(title, message, maximumProgress)

    Create a horizontal progress dialog

    Parameters:
    title(optional) (str) – title
    message(optional) (str) – message
    maximunProgress(optional) (int) – dfault=100

Alert
dialogCreateAlert(title, message)

    Create alert dialog

    Parameters:
    title(optional) (str) – title
    message(optional) (str) – message
    maximunProgress(optional) (int) – dfault=100

Dialog Control
dialogSetPositiveButtonText(text)

    Set alert dialog positive button text

    Parameters: text (str) – text

dialogSetNegativeButtonText(text)

    Set alert dialog negative button text

    Parameters: text (str) – text

dialogSetNeutralButtonText(text)

    Set alert dialog button text

    Parameters: text (str) – text

dialogSetItems(items)

    Set alert dialog list items

    Parameters: items (list) – items

dialogSetSingleChoiceItems(items, selected)

    Set alert dialog list items

    Parameters:
    items (list) – items
    selected (int) – selected item index (default=0)

dialogSetMultiChoiceItems(items, selected)

    Set dialog multiple choice items and selection

    Parameters:
    items (list) – items
    selected (int) – selected item index (default=0)

addContextMenuItem(label, event, eventData)

    Adds a new item to context menu

    Parameters:
    label (str) – label for this menu item
    event (str) – event that will be generated on menu item click
    eventData (object) – event object

addOptionsMenuItem(label, event, eventData, iconName)

Adds a new item to context menu

    Parameters:
    label (str) – label for this menu item
    event (str) – event that will be generated on menu item click
    eventData (object) – event object
    iconName (str) – Android system menu icon, see http://developer.android.com/reference/android/R.drawable.html

dialogGetResponse()

    Returns dialog response

dialogGetSelectedItems()

    This method provides list of items user selected

dialogDismiss()

    Dismiss dialog

dialogShow()

    Show dialog

Layout
fullShow(layout)

    Show Full Screen

    Parameters: layout (string) – String containing View layout

fullDismiss()

    Dismiss Full Screen

fullQuery()

    Get Fullscreen Properties

fullQueryDetail(id)

    Get fullscreen properties for a specific widget

    Parameters: id (str) – id of layout widget

fullSetProperty(id)

    Set fullscreen widget property

    Parameters:
    id (str) – id of layout widget
    property (str) – name of property to set
    value (str) – value to set property to

fullSetList(id, list)

    Attach a list to a fullscreen widget

    Parameters:
    id (str) – id of layout widget
    list (list) – List to set

fullKeyOverride(keycodes, enable)

    Override default key actions

    Parameters:
    keycodes (str) – id of layout widget
    enable (bool) – List to set (default=true)

WebView
webViewShow()

    Display a WebView with the given URL

    Parameters:
    url (str) – url
    wait(optional) (bool) – block until the user exits the WebView

USB Host Serial Facade

QPython 1.3.1+ and QPython3 1.0.3+ contains this feature

SL4A Facade for USB Serial devices by Android USB Host API.

It control the USB-Serial like devices from Andoroid which has USB Host Controller .

The sample demonstration is also available at youtube video
Requirements

Android device which has USB Host controller (and enabled in that firmware).

Android 4.0 (API14) or later.

USB Serial devices (see Status).

USB Serial devices were not handled by Android kernel.

    I heard some android phone handle USB Serial devices > make /dev/ttyUSB0 in kernel level. > In this case, Android does not be able to handle the device > from OS level.

please check Android Applications be able to grab the target USB Devices, such as USB Device Info.
Status

probably work with USB CDC, like FTDI, Arduino or else.

2012/09/10: work with 78K0F0730 device (new RL78) with Tragi BIOS board.

M78K0F0730

2012/09/24: work with some pl2303 devcies.
Author

This facade developped by Kuri65536 you can see the commit log in it.
APIs
usbserialGetDeviceList()

    Returns USB devices reported by USB Host API.

    Return: Returns “Map of id and string information Map<String, String>

usbserialDisconnect(connID)

    Disconnect all USB-device

    Parameters: connID (str) – connection ID

usbserialActiveConnections()

    Returns active USB-device connections.

    Return: Returns “Active USB-device connections by Map UUID vs device-name.”

usbserialWriteBinary(base64, connID)

    Send bytes over the currently open USB Serial connection.

    Parameters:
    base64 (str) –
    connId (str) –

usbserialReadBinary(bufferSize, connID)

    Read up to bufferSize bytes and return a chunked, base64 encoded string

    Parameters:
    bufferSize (int) –
    connId (str) –

usbserialConnect(hash, options)

    Connect to a device with USB-Host. request the connection and exit

    Parameters:
    hash (str) –
    options (str) –

    Return:
    Returns messages the request status

usbserialHostEnable()

    Requests that the host be enable for USB Serial connections.

    Return: True if the USB Device is accesible

usbserialWrite(String ascii, String connID)

    Sends ASCII characters over the currently open USB Serial connection

    Parameters:
    ascii (str) –
    connID (str) –

usbserialReadReady(connID)

        Parameters: connID (str) –

    Return: True if the next read is guaranteed not to block

usbserialRead(connID, bufferSize)

    Read up to bufferSize ASCII characters.

    Parameters:
    connID (str) –
    bufferSize (int) –

usbserialGetDeviceName(connID)

    Queries a remote device for it’s name or null if it can’t be resolved

    Parameters: connID (str) –

