# Nothing Here
Author: [Stratulat Dragoș](https://www.linkedin.com/in/stratulat-dragos-6b9a09227)

<br>

## Description
```
Analyze and deobfuscate a piece of VBA (Visual Basic for Applications) code embedded within a Word document. 
The document contains macros that execute a PowerShell script.
```

<br>

## Requirements
- Knowledge of VBA and PowerShell scripting
- Familiarity with basic deobfuscation techniques

<br>

## Solve
Before we start solving this challenge, we must analyze the document. <br>
We use the `oletools` suite to get a summary of what to expect from the document:
```bash
sudo -H pip install -U oletools
```
<br>
The challenge involves several steps to clean and analyze the obfuscated VBA code:
1. Use `oletools` for a preliminary analysis of the document.
```bash
oleid Nothing\ here.doc
```

<img src="./solve/oleid.jpg" width="500">

2. Extract the VBA code, removing any irrelevant IOC (Indicators of Compromise) information.
```bash
olevba Nothing\ here.doc > malware.vbs
```

3. The attacker added numerous unnecessary lines, including comments, to obfuscate the code further. <br>
These can be removed using the find and replace feature in VSCode or using `egrep`.
```bash
cat malware.vbs | egrep -v ^\' > onlycode.vbs
# everything before 'Const Stutteriers = "UTF8"' is just output from olevba
# remove everything after 'End Sub' as well
```

4. Clean the code by removing unused variable declarations.
```vb
Const Stutteriers = "UTF8"
Const Flagskibets = "GetString"
Symmetrian = "Text"
Salientian = "."
Homopolar = "System"
Const uncogged = "Encoding"
Const ovogenous = "("
Const Counterreason57 = ")"
Const Bortrationalisering = "Convert"
Const Dialaktologerne = "FromBase64String"
Fordkt = "]"
Haire = "["
Gona = ":"
Set Mikro = CreateObject("Wscript.Shell")
Set ObjExec = Mikro.Exec("%COMSPEC% /c ping p.p.p.p")
Gjor2021 = Gjor2021 + ObjExec.StdOut.ReadAll()
Pterographydrabsmndenet = TimeSerial(168, 30, 65)
Gjor2021 = Split(Gjor2021, ".p.")(1)
s2 = s2 + ""
s2 = Replace(s2, "Skriftstrr3", ChrW(34))
s2 = s2 + "JE1ham9yY2FuciA9ICcnJ2Z2dXluc2NOdHlpVW8zbncgcUd1ZUVuRWVqckRhSHRjZWpSNGFTbjZka29wbVFOU2FtbXRlNyBtezYgQiBUIFMgRHJlZUp0SHVUcnNuQiBtJDYoMi1ianFvS2lwbmkgMyhUKG42WDVRLkwuZjljMEUpUiBmK0wgYyhqOUc3cS5FLjgxcTJYMjgpbyBVfDkgbUcxZUR0aC1vUk9hUW53ZDNvem1zIFAtOENub1d1bW5ydFkgVDVoIEh8MCBRJVggbnt5W2ljWGhTYXFyUl1ZJE9fR305KUQpSjtYfWo7MiRHQVBwMHBMRERhbHQ3YWlQS2F5dEVodyBYPXEgRyR1ZVVuMnZ0OjRBclBOUDFEdUFxVG5BQSBzKzcgaSJ1XFkiUyBzK20gbyR2KDRHcWVnbnBlenJRYUd0b2VJUlphTG45ZE1vcW"
lorem = Haire + Homopolar + Salientian + Symmetrian + Salientian + uncogged + Fordkt + Gona + Gona + Stutteriers + Salientian + Flagskibets + ovogenous + Haire + Homopolar + Salientian + Bortrationalisering + Fordkt + Gona + Gona + Dialaktologerne
Ambu = Gjor2021 + "owershell"
s2 = s2 + "1KTkphU21VZVopdTthJFRmemlxbGJlMENFb3ZudXRFZUJueXRvIGY9NiBWIHAiWVN5TUFDc0NvMlcwcjIyNDR7QTB6YjRmcHVtYEIkZWMxQDN0ZWl5bzRuTV9kIjQ7QVNtZXp0di1sQ3lvYW5adHFlVW40dEYgTy01UFRhTnRJaHIgRiRwQXNwZXB6RGFhcXRsYU1QOWF1dFNoVSBRLXlWcWF3bGN1amV3IHckR2ZBaUFscmVBQ1Vva25rdGllY25BdGU7USRQdjVhTHJuaVdhMGJSbHdlTk4xYVltaWVSIEw9YyBHJHUoeUczZWJueGVzcnRhR3RWZU5SY2FObllkb29lbUFOSGF3bVVlbilDO28kZ3ZjYVpyQWlyYUFiTWxZZUZWamFRbFd1b2VrIEM9MiA4InlfNmhZQGZgbyR5X00iTjtLJE1yT2V0Z3dQdWF5dFloMSBnPUwgZSJESFlLcUM4VUI6TFwwRVpuYXZnaXJyNm94blJtNmVRbk10aCJ2O1JOamV0dzItZUlkdGllbG1OUG1yd29lcDVlTnJ6dHV5MyBnLUFQOWFm"
Coinferredfortovsret = FormatDateTime("12/12/12")
s2 = s2 + "dDZodyBxJHhyeGV0ZzBQemFmdDZoMCB6LVBOb2FYbUFlcCByJEh2b2FwcjNpZ2FIYnFsTWVSTm1hZW02ZVUgYS04VmdhOWxmdXVldSB3JHl2YWFtcklpTmE1YjJsSGV5VnNhS2xYdVRlNyBaLUlGbW9Sclljc2VuO20kT2ZaaWlsQ2VmUHZhN3RFaFogdz1sIGkkOGVrblZ2eTpOTGhPY0MyQTNMaUFsUGJQTERqQXdUZ0FBIG4rbCA2Ik1cbSJVIGwrTiBaJHooakdpZThuYmU1clphbXR3ZXJSeGFVbllkcG9WbXZOcmFubUllUClKO2UkbHRLaDFpTXJuZHAgZj1iIEgiV2g4M1VyT19RYkIzNkBadUF0N3lwfXYiajttU3lldHRsLXdDQm80bnB0NmVSbld0WCAxLU5QSGFJdHFoSSBjJEhmb2kybFllVFBnYXd0dWhLIEItRVZEYTZsQ3UwZUIgeSR1dHBoSGlUcndkZDtBQWNkZmQxLW1UQXlMcGxlWCBXLUFBaHN6czhlYm1uYkxsVXkwTnZhWm1rZWIgWU1YaU5jNnJzb2"
s2 = s2 + "VzY29iZnR0Si4xVkppUHNzdThhdGw1QjdhQnNMaTBjeDtMW0pNcGlNY1hyeW9Hc09vWmZZdFkuRVY0aWVzSHVJYVhsbUJXYURzaWlIYzAuWkZBaVhsSGVtSTFPTS5KRmppNGxIZU5TZ3ltc0t0aGU0bU1dNDoxOk5EUmU3bHJlVXRvZU5GU2lBbGZlNSg4JEZmUWlCbHBld1B5YUR0NGhjLHAiNE9abnNsSHloRU5yWHIzb0NyU0RXaU9hUGw4b3JnNXM1IlcscSJmU3hleG55ZFJUMW9VUkplTWNreWNjeWxaZXpCM2lpbjciTSlvO00nJyc7IEZ1bmN0aW9uIEd1ZXN0czkgeyAgcGFyYW0oW1N0cmluZ10kT2JzZSk7ICREcm92ZWRzdGp1ID0gInMiKyJ1IisiYiIrInMiKyJ0IisiciIrImkiKyJuIisiZyI7IEZvcigkUGh5bGFya29tPTE7ICRQaHlsYXJrb20gLWx0ICRPYnNlLkxlbmd0aC0xOyAkUGh5bGFya29tKz0oMSsxKSl7ICRNb2R1bGF0ID0gJE1vZHVsYXQgKyAkT2JzZS4kRHJvdmVkc3RqdS5JbnZva2UoJFBoeWxhcmtvbSwgMSkgfTsJcmV0dXJuICRNb2R1bGF0O30gJFByb29maW5nMT0gR3Vlc3RzOSAkTWFqb3JjYW5yOyBlY2hvICRQcm9vZmluZzEgPiAiLlxtYWwucHMxIjsgcG93ZXJzaGVsbC5leGUgLlxtYWwucHMxOyBybSAuXG1hbC5wczEK"
Ambu = Gjor2021 + "owershell"
Set Gymnas = CreateObject("Shell.Application")
Gymnas.ShellExecute Ambu, ChrW(34) & lorem + "('" + s2 + "'))" + "|" + Ambu & ChrW(34), impecuni, impecuni, 0
```

5. Identify and decode a base64 string that seems to be part of the script - the `s2` variable.
```bash
echo 'JE1ham9yY2FuciA9ICcnJ2Z2dXluc2NOdHlpVW8zbncgcUd1ZUVuRWVqckRhSHRjZWpSNGFTbjZka29wbVFOU2FtbXRlNyBtezYgQiBUIFMgRHJlZUp0SHVUcnNuQiBtJDYoMi1ianFvS2lwbmkgMyhUKG42WDVRLkwuZjljMEUpUiBmK0wgYyhqOUc3cS5FLjgxcTJYMjgpbyBVfDkgbUcxZUR0aC1vUk9hUW53ZDNvem1zIFAtOENub1d1bW5ydFkgVDVoIEh8MCBRJVggbnt5W2ljWGhTYXFyUl1ZJE9fR305KUQpSjtYfWo7MiRHQVBwMHBMRERhbHQ3YWlQS2F5dEVodyBYPXEgRyR1ZVVuMnZ0OjRBclBOUDFEdUFxVG5BQSBzKzcgaSJ1XFkiUyBzK20gbyR2KDRHcWVnbnBlenJRYUd0b2VJUlphTG45ZE1vcW1KTkphU21VZVopdTthJFRmemlxbGJlMENFb3ZudXRFZUJueXRvIGY9NiBWIHAiWVN5TUFDc0NvMlcwcjIyNDR7QTB6YjRmcHVtYEIkZWMxQDN0ZWl5bzRuTV9kIjQ7QVNtZXp0di1sQ3lvYW5adHFlVW40dEYgTy01UFRhTnRJaHIgRiRwQXNwZXB6RGFhcXRsYU1QOWF1dFNoVSBRLXlWcWF3bGN1amV3IHckR2ZBaUFscmVBQ1Vva25rdGllY25BdGU7USRQdjVhTHJuaVdhMGJSbHdlTk4xYVltaWVSIEw9YyBHJHUoeUczZWJueGVzcnRhR3RWZU5SY2FObllkb29lbUFOSGF3bVVlbilDO28kZ3ZjYVpyQWlyYUFiTWxZZUZWamFRbFd1b2VrIEM9MiA4InlfNmhZQGZgbyR5X00iTjtLJE1yT2V0Z3dQdWF5dFloMSBnPUwgZSJESFlLcUM4VUI6TFwwRVpuYXZnaXJyNm94blJtNmVRbk10aCJ2O1JOamV0dzItZUlkdGllbG1OUG1yd29lcDVlTnJ6dHV5MyBnLUFQOWFmdDZodyBxJHhyeGV0ZzBQemFmdDZoMCB6LVBOb2FYbUFlcCByJEh2b2FwcjNpZ2FIYnFsTWVSTm1hZW02ZVUgYS04VmdhOWxmdXVldSB3JHl2YWFtcklpTmE1YjJsSGV5VnNhS2xYdVRlNyBaLUlGbW9Sclljc2VuO20kT2ZaaWlsQ2VmUHZhN3RFaFogdz1sIGkkOGVrblZ2eTpOTGhPY0MyQTNMaUFsUGJQTERqQXdUZ0FBIG4rbCA2Ik1cbSJVIGwrTiBaJHooakdpZThuYmU1clphbXR3ZXJSeGFVbllkcG9WbXZOcmFubUllUClKO2UkbHRLaDFpTXJuZHAgZj1iIEgiV2g4M1VyT19RYkIzNkBadUF0N3lwfXYiajttU3lldHRsLXdDQm80bnB0NmVSbld0WCAxLU5QSGFJdHFoSSBjJEhmb2kybFllVFBnYXd0dWhLIEItRVZEYTZsQ3UwZUIgeSR1dHBoSGlUcndkZDtBQWNkZmQxLW1UQXlMcGxlWCBXLUFBaHN6czhlYm1uYkxsVXkwTnZhWm1rZWIgWU1YaU5jNnJzb2VzY29iZnR0Si4xVkppUHNzdThhdGw1QjdhQnNMaTBjeDtMW0pNcGlNY1hyeW9Hc09vWmZZdFkuRVY0aWVzSHVJYVhsbUJXYURzaWlIYzAuWkZBaVhsSGVtSTFPTS5KRmppNGxIZU5TZ3ltc0t0aGU0bU1dNDoxOk5EUmU3bHJlVXRvZU5GU2lBbGZlNSg4JEZmUWlCbHBld1B5YUR0NGhjLHAiNE9abnNsSHloRU5yWHIzb0NyU0RXaU9hUGw4b3JnNXM1IlcscSJmU3hleG55ZFJUMW9VUkplTWNreWNjeWxaZXpCM2lpbjciTSlvO00nJyc7IEZ1bmN0aW9uIEd1ZXN0czkgeyAgcGFyYW0oW1N0cmluZ10kT2JzZSk7ICREcm92ZWRzdGp1ID0gInMiKyJ1IisiYiIrInMiKyJ0IisiciIrImkiKyJuIisiZyI7IEZvcigkUGh5bGFya29tPTE7ICRQaHlsYXJrb20gLWx0ICRPYnNlLkxlbmd0aC0xOyAkUGh5bGFya29tKz0oMSsxKSl7ICRNb2R1bGF0ID0gJE1vZHVsYXQgKyAkT2JzZS4kRHJvdmVkc3RqdS5JbnZva2UoJFBoeWxhcmtvbSwgMSkgfTsJcmV0dXJuICRNb2R1bGF0O30gJFByb29maW5nMT0gR3Vlc3RzOSAkTWFqb3JjYW5yOyBlY2hvICRQcm9vZmluZzEgPiAiLlxtYWwucHMxIjsgcG93ZXJzaGVsbC5leGUgLlxtYWwucHMxOyBybSAuXG1hbC5wczEK' | base64 -d
```
```vb
$Majorcanr = '''fvuynscNtyiUo3nw qGueEnEejrDaHtcejR4aSn6dkopmQNSammte7 m{6 B T S DreeJtHuTrsnB m$6(2-bjqoKipni 3(T(n6X5Q.L.f9c0E)R f+L c(j9G7q.E.81q2X28)o U|9 mG1eDth-oROaQnwd3ozms P-8CnoWumnrtY T5h H|0 Q%X n{y[icXhSaqrR]Y$O_G}9)D)J;X}j;2$GAPp0pLDDalt7aiPKaytEhw X=q G$ueUn2vt:4ArPNP1DuAqTnAA s+7 i"u\Y"S s+m o$v(4GqegnpezrQaGtoeIRZaLn9dMoqmJNJaSmUeZ)u;a$Tfziqlbe0CEovnutEeBnyto f=6 V p"YSyMACsCo2W0r2244{A0zb4fpum`B$ec1@3teiyo4nM_d"4;ASmeztv-lCyoanZtqeUn4tF O-5PTaNtIhr F$pAspepzDaaqtlaMP9autShU Q-yVqawlcujew w$GfAiAlreACUoknktiecnAte;Q$Pv5aLrniWa0bRlweNN1aYmieR L=c G$u(yG3ebnxesrtaGtVeNRcaNnYdooemANHawmUen)C;o$gvcaZrAiraAbMlYeFVjaQlWuoek C=2 8"y_6hY@f`o$y_M"N;K$MrOetgwPuaytYh1 g=L e"DHYKqC8UB:L\0EZnavgirr6oxnRm6eQnMth"v;RNjetw2-eIdtielmNPmrwoep5eNrztuy3 g-AP9aft6hw q$xrxetg0Pzaft6h0 z-PNoaXmAep r$Hvoapr3igaHbqlMeRNmaem6eU a-8Vga9lfuueu w$yvaamrIiNa5b2lHeyVsaKlXuTe7 Z-IFmoRrYcsen;m$OfZiilCefPva7tEhZ w=l i$8eknVvy:NLhOcC2A3LiAlPbPLDjAwTgAA n+l 6"M\m"U l+N Z$z(jGie8nbe5rZamtwerRxaUnYdpoVmvNranmIeP)J;e$ltKh1iMrndp f=b H"Wh83UrO_QbB36@ZuAt7yp}v"j;mSyettl-wCBo4npt6eRnWtX 1-NPHaItqhI c$Hfoi2lYeTPgawtuhK B-EVDa6lCu0eB y$utphHiTrwdd;AAcdfd1-mTAyLpleX W-AAhszs8ebmnbLlUy0NvaZmkeb YMXiNc6rsoescobfttJ.1VJiPssu8atl5B7aBsLi0cx;L[JMpiMcXryoGsOoZfYtY.EV4iesHuIaXlmBWaDsiiHc0.ZFAiXlHemI1OM.JFji4lHeNSgymsKthe4mM]4:1:NDRe7lreUtoeNFSiAlfe5(8$FfQiBlpewPyaDt4hc,p"4OZnslHyhENrXr3oCrSDWiOaPl8org5s5"W,q"fSxexnydRT1oURJeMckyccylZezB3iin7"M)o;M'''; Function Guests9 {  param([String]$Obse); $Drovedstju = "s"+"u"+"b"+"s"+"t"+"r"+"i"+"n"+"g"; For($Phylarkom=1; $Phylarkom -lt $Obse.Length-1; $Phylarkom+=(1+1)){ $Modulat = $Modulat + $Obse.$Drovedstju.Invoke($Phylarkom, 1) };	return $Modulat;} $Proofing1= Guests9 $Majorcanr; echo $Proofing1 > ".\mal.ps1"; powershell.exe .\mal.ps1; rm .\mal.ps1
```

6. Properly format and indent the code for better readability.
```ps1
$Majorcanr = '''fvuynscNtyiUo3nw qGueEnEejrDaHtcejR4aSn6dkopmQNSammte7 m{6 B T S DreeJtHuTrsnB m$6(2-bjqoKipni 3(T(n6X5Q.L.f9c0E)R f+L c(j9G7q.E.81q2X28)o U|9 mG1eDth-oROaQnwd3ozms P-8CnoWumnrtY T5h H|0 Q%X n{y[icXhSaqrR]Y$O_G}9)D)J;X}j;2$GAPp0pLDDalt7aiPKaytEhw X=q G$ueUn2vt:4ArPNP1DuAqTnAA s+7 i"u\Y"S s+m o$v(4GqegnpezrQaGtoeIRZaLn9dMoqmJNJaSmUeZ)u;a$Tfziqlbe0CEovnutEeBnyto f=6 V p"YSyMACsCo2W0r2244{A0zb4fpum`B$ec1@3teiyo4nM_d"4;ASmeztv-lCyoanZtqeUn4tF O-5PTaNtIhr F$pAspepzDaaqtlaMP9autShU Q-yVqawlcujew w$GfAiAlreACUoknktiecnAte;Q$Pv5aLrniWa0bRlweNN1aYmieR L=c G$u(yG3ebnxesrtaGtVeNRcaNnYdooemANHawmUen)C;o$gvcaZrAiraAbMlYeFVjaQlWuoek C=2 8"y_6hY@f`o$y_M"N;K$MrOetgwPuaytYh1 g=L e"DHYKqC8UB:L\0EZnavgirr6oxnRm6eQnMth"v;RNjetw2-eIdtielmNPmrwoep5eNrztuy3 g-AP9aft6hw q$xrxetg0Pzaft6h0 z-PNoaXmAep r$Hvoapr3igaHbqlMeRNmaem6eU a-8Vga9lfuueu w$yvaamrIiNa5b2lHeyVsaKlXuTe7 Z-IFmoRrYcsen;m$OfZiilCefPva7tEhZ w=l i$8eknVvy:NLhOcC2A3LiAlPbPLDjAwTgAA n+l 6"M\m"U l+N Z$z(jGie8nbe5rZamtwerRxaUnYdpoVmvNranmIeP)J;e$ltKh1iMrndp f=b H"Wh83UrO_QbB36@ZuAt7yp}v"j;mSyettl-wCBo4npt6eRnWtX 1-NPHaItqhI c$Hfoi2lYeTPgawtuhK B-EVDa6lCu0eB y$utphHiTrwdd;AAcdfd1-mTAyLpleX W-AAhszs8ebmnbLlUy0NvaZmkeb YMXiNc6rsoescobfttJ.1VJiPssu8atl5B7aBsLi0cx;L[JMpiMcXryoGsOoZfYtY.EV4iesHuIaXlmBWaDsiiHc0.ZFAiXlHemI1OM.JFji4lHeNSgymsKthe4mM]4:1:NDRe7lreUtoeNFSiAlfe5(8$FfQiBlpewPyaDt4hc,p"4OZnslHyhENrXr3oCrSDWiOaPl8org5s5"W,q"fSxexnydRT1oURJeMckyccylZezB3iin7"M)o;M'''; 

Function Guests9 {  param([String]$Obse); 
    $Drovedstju = "s"+"u"+"b"+"s"+"t"+"r"+"i"+"n"+"g"; 
    For($Phylarkom=1; $Phylarkom -lt $Obse.Length-1; $Phylarkom+=(1+1)){ 
        $Modulat = $Modulat + $Obse.$Drovedstju.Invoke($Phylarkom, 1) };
        	return $Modulat;} 

$Proofing1= Guests9 $Majorcanr; 
echo $Proofing1 > ".\mal.ps1"; 
powershell.exe .\mal.ps1; 
```

We can remove the last line to keep the newly created file for analysis.

7. Open the file in the PowerShell IDE (enable running scripts) and extract the plaintext flag split into several parts
```ps1
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

```ps1
function GenerateRandomName {    return $(-join ((65..90) + (97..122) | Get-Random -Count 5 | % {[char]$_}));};$AppDataPath = $env:APPDATA + "\" + $(GenerateRandomName);$fileContent =  "SMCC2024{0bfu`$c@tion_";Set-Content -Path $AppDataPath -Value $fileContent;$variableName = $(GenerateRandomName);$variableValue = "_h@`$_";$regPath = "HKCU:\Environment";New-ItemProperty -Path $regPath -Name $variableName -Value $variableValue -Force;$filePath = $env:LOCALAPPDATA + "\" + $(GenerateRandomName);$third = "h3r_b3@uty}";Set-Content -Path $filePath -Value $third;Add-Type -AssemblyName Microsoft.VisualBasic;[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($filePath,"OnlyErrorDialogs","SendToRecycleBin");
```
```ps1
function GenerateRandomName {    return $(-join ((65..90) + (97..122) | Get-Random -Count 5 | % {[char]$_}));};
$AppDataPath = $env:APPDATA + "\" + $(GenerateRandomName);

$fileContent =  "SMCC2024{0bfu`$c@tion_";

Set-Content -Path $AppDataPath -Value $fileContent;
$variableName = $(GenerateRandomName);
$variableValue = "_h@`$_";$regPath = "HKCU:\Environment";
New-ItemProperty -Path $regPath -Name $variableName -Value $variableValue -Force;
$filePath = $env:LOCALAPPDATA + "\" + $(GenerateRandomName);
$third = "h3r_b3@uty}";
Set-Content -Path $filePath -Value $third;

Add-Type -AssemblyName Microsoft.VisualBasic;
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($filePath,"OnlyErrorDialogs","SendToRecycleBin");

```

Since the flag format has changed, we replaced `SMCC2024` with `CSCTF`.

<br>

> Flag: `CSCTF{0bfu$c@tion__h@$_h3r_b3@uty}`
> 
