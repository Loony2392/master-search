' VBScript for Windows File Operations
' This script provides reliable file opening on Windows without browser restrictions

' Function to open file in Explorer
Sub OpenFileInExplorer(filePath)
    Dim shell
    Set shell = CreateObject("WScript.Shell")
    
    ' Use Explorer /select to highlight the file
    Dim cmd
    cmd = "explorer.exe /select,""" & filePath & """"
    
    On Error Resume Next
    shell.Run cmd, 1, False
    On Error GoTo 0
    
    If Err.Number <> 0 Then
        MsgBox "Fehler beim Öffnen: " & Err.Description
    End If
End Sub

' Function to copy file
Sub CopyFile(sourcePath, destPath)
    Dim shell, fileSystem
    Set shell = CreateObject("WScript.Shell")
    Set fileSystem = CreateObject("Scripting.FileSystemObject")
    
    On Error Resume Next
    fileSystem.CopyFile sourcePath, destPath, True
    On Error GoTo 0
    
    If Err.Number <> 0 Then
        MsgBox "Fehler beim Kopieren: " & Err.Description
    Else
        MsgBox "Datei erfolgreich kopiert zu: " & destPath
    End If
End Sub

' Get command line arguments
If WScript.Arguments.Count >= 2 Then
    Dim action
    action = WScript.Arguments(0)
    
    If action = "open" Then
        OpenFileInExplorer WScript.Arguments(1)
    ElseIf action = "copy" Then
        If WScript.Arguments.Count >= 3 Then
            CopyFile WScript.Arguments(1), WScript.Arguments(2)
        End If
    End If
End If
