#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Category Definitions and Utilities
========================================
Centralized definitions for file categories and their supported file types.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

# Category definitions with emoji, description, and supported file types
CATEGORY_INFO = {
    'code': {
        'emoji': '💻',
        'label': 'Code',
        'description': 'Programming Languages & Scripts',
        'extensions': [
            # Python
            'py', 'pyc', 'pyo', 'pyd',
            # Java
            'java', 'class', 'jar',
            # JavaScript/TypeScript
            'js', 'jsx', 'mjs', 'cjs', 'ts', 'tsx',
            # C/C++
            'cpp', 'cc', 'cxx', 'c', 'h', 'hpp', 'hxx', 'hh',
            # C#
            'cs', 'csproj',
            # Swift
            'swift', 'swiftpm',
            # Go
            'go',
            # Rust
            'rs', 'rlib',
            # Ruby
            'rb', 'rbw', 'rake', 'gemspec',
            # PHP
            'php', 'php3', 'php4', 'php5', 'php7', 'php8', 'phtml',
            # Scala
            'scala', 'sc',
            # Kotlin
            'kt', 'kts',
            # Shell scripts
            'sh', 'bash', 'zsh', 'fish', 'ksh',
            # PowerShell
            'ps1', 'psm1', 'psd1',
            # Batch/Command
            'bat', 'cmd', 'com',
            # Perl
            'pl', 'pm',
            # Lua
            'lua',
            # R
            'r', 'rmd', 'rnotebook',
            # Julia
            'jl',
            # Dart
            'dart',
            # Elm
            'elm',
            # Clojure
            'clj', 'cljs', 'cljc', 'edn',
            # Elixir
            'ex', 'exs',
            # Erlang
            'erl', 'hrl',
            # Haskell
            'hs', 'lhs',
            # OCaml
            'ml', 'mli',
            # F#
            'fs', 'fsi', 'fsx',
            # Pascal
            'pas', 'pp',
            # Assembly
            'asm', 's',
            # Visual Basic
            'vb', 'vbs', 'vbproj',
            # Groovy/Gradle
            'groovy', 'gradle', 'maven', 'pom',
            # Build tools
            'makefile', 'make', 'ninja', 'cmake', 'sbt', 'cargo', 'cabal', 'stack',
        ]
    },
    
    'markup': {
        'emoji': '📝',
        'label': 'Markup',
        'description': 'Markup & Documentation Formats',
        'extensions': [
            'md', 'markdown', 'rst', 'rest', 'adoc', 'asciidoc',
            'textile', 'rdoc', 'org', 'wiki', 'mediawiki',
            'mdown', 'mkd', 'tex', 'latex',
        ]
    },
    
    'documents': {
        'emoji': '📄',
        'label': 'Documents',
        'description': 'Office & Publishing Documents',
        'extensions': [
            'pdf', 'doc', 'docx', 'docm', 'odt', 'ott',
            'rtf', 'pages', 'txt', 'text', 'wps', 'wpd',
        ]
    },
    
    'spreadsheets': {
        'emoji': '📊',
        'label': 'Spreadsheets',
        'description': 'Spreadsheet Files',
        'extensions': [
            'xls', 'xlsx', 'xlsm', 'xlt', 'ods', 'ots',
            'csv', 'tsv', 'dsv', 'numbers', 'gnumeric',
            'xlam', 'xltx', 'xltm',
        ]
    },
    
    'presentations': {
        'emoji': '🎬',
        'label': 'Presentations',
        'description': 'Presentation & Slide Files',
        'extensions': [
            'ppt', 'pptx', 'pptm', 'potx', 'odp', 'otp',
            'key', 'gslides', 'pps', 'ppsx',
        ]
    },
    
    'data': {
        'emoji': '💾',
        'label': 'Data',
        'description': 'Data Format Files',
        'extensions': [
            'json', 'jsonl', 'ndjson', 'xml', 'xsd', 'xsl', 'xslt',
            'yaml', 'yml', 'toml', 'protobuf', 'proto',
            'avro', 'msgpack', 'cbor', 'bson', 'ion', 'edn', 's_expr',
        ]
    },
    
    'databases': {
        'emoji': '🗄️',
        'label': 'Databases',
        'description': 'Database Files',
        'extensions': [
            'sql', 'sqlite', 'db', 'mdb', 'dbf', 'dbc',
            'accdb', 'laccdb', 'mysql', 'postgresql', 'mongo',
            'ibd', 'frm', 'myd',
        ]
    },
    
    'logs': {
        'emoji': '📝',
        'label': 'Logs',
        'description': 'Log & System Files',
        'extensions': [
            'log', 'logs', 'trace', 'debug', 'out', '1', '2', 'syslog',
        ]
    },
    
    'config': {
        'emoji': '⚙️',
        'label': 'Config',
        'description': 'Configuration Files',
        'extensions': [
            'conf', 'config', 'cfg', 'cnf', 'ini', 'inf',
            'env', 'envrc', 'properties', 'gradle', 'cmake',
            'dockerfile', 'docker-compose', 'compose',
            'kubernetes', 'k8s', 'terraform', 'tf', 'tfvars',
            'ansible', 'playbook', 'chef', 'recipe',
            'puppet', 'pp', 'saltstack', 'sls', 'nix',
            'vcxproj', 'csproj', 'fsproj', 'vbproj',
            'targets', 'props', 'vimrc', 'vim', 'emacs',
            'gitconfig', 'gitignore', 'gitattributes', 'editorconfig',
            'eslintrc', 'prettierrc', 'stylelintrc',
            'npmrc', 'yarnrc', 'bowerrc', 'htaccess',
            'nginx', 'apache', 'httpd',
            'bash_profile', 'bashrc', 'profile', 'zshrc', 'zsh_profile',
            'fishrc', 'screenrc', 'tmuxconf',
        ]
    },
    
    'web': {
        'emoji': '🌐',
        'label': 'Web',
        'description': 'Web Development Files',
        'extensions': [
            'html', 'htm', 'xhtml', 'css', 'scss', 'sass', 'less',
            'vue', 'svelte', 'astro', 'qvp',
            'jsx', 'tsx', 'pug', 'jade',
            'handlebars', 'hbs', 'ejs', 'erb', 'haml', 'slim', 'blade',
            'jinja', 'jinja2', 'liquid', 'mustache', 'twig',
            'freemarker', 'ftl', 'velocity', 'vm', 'js', 'ts',
        ]
    },
    
    'media': {
        'emoji': '🖼️',
        'label': 'Media',
        'description': 'Images, Audio & Video Files (100+ formats)',
        'extensions': [
            # Images
            'jpg', 'jpeg', 'jpe', 'png', 'apng', 'gif', 'gifv',
            'webp', 'svg', 'svgz', 'ico', 'cur', 'bmp', 'dib',
            'tiff', 'tif', 'psd', 'psb', 'xcf', 'ai', 'eps',
            'pdf', 'raw', 'cr2', 'crw', 'nef', 'raf', 'orf',
            'heic', 'heif',
            # Audio
            'mp3', 'wav', 'wma', 'flac', 'aac', 'm4a', 'm4b',
            'ogg', 'oga', 'opus', 'aiff', 'aif', 'ape', 'alac',
            'dsd', 'mid', 'midi',
            # Video
            'mp4', 'm4v', 'avi', 'divx', 'mkv', 'mka', 'mks',
            'mov', 'qt', 'flv', 'f4v', 'wmv', 'wm', 'webm',
            '3gp', '3gpp', '3g2', 'ts', 'm2ts', 'mts', 'mxf',
            'ogv', 'vob', 'f4p',
        ]
    },
    
    'archives': {
        'emoji': '📦',
        'label': 'Archives',
        'description': 'Archive & Compression Files',
        'extensions': [
            'zip', 'zipx', 'rar', '7z', 'tar', 'gz', 'gzip', 'tgz',
            'tar.gz', 'tarbz2', 'tar.bz2', 'tbz', 'tbz2',
            'bz2', 'bzip2', 'xz', 'z', 'lz', 'lzma',
            'zstd', 'zst', 'brotli', 'br', 'cab', 'msi',
            'iso', 'cue', 'dmg', 'pkg', 'udif',
            'deb', 'rpm', 'apk', 'appimage', 'asar',
            'whl', 'egg',
        ]
    },
    
    'fonts': {
        'emoji': '🔤',
        'label': 'Fonts',
        'description': 'Font Files',
        'extensions': [
            'ttf', 'otf', 'woff', 'woff2', 'eot', 'fon', 'fnt',
            'pfa', 'pfb', 'afm', 'ufm', 'ttc', 'dfont', 'suit',
        ]
    },
    
    'text': {
        'emoji': '📄',
        'label': 'Text Files',
        'description': 'Plain Text & Subtitle Files',
        'extensions': [
            'txt', 'text', 'log', 'asc', 'ascii', 'nfo', 'inf',
            'readme', 'license', 'license.txt', 'changelog', 'changes',
            'contributing', 'authors', 'contributors', 'todo', 'fixme',
            'notice', 'manifest', 'm3u', 'm3u8', 'pls',
            'sub', 'srt', 'ass', 'ssa', 'vtt',
        ]
    },
}


def get_category_extensions_formatted(category_key: str) -> str:
    """Get formatted list of extensions for a category"""
    if category_key not in CATEGORY_INFO:
        return ""
    
    info = CATEGORY_INFO[category_key]
    extensions = info['extensions']
    
    # Format as comma-separated list with line breaks every 5 items
    formatted_list = []
    for i, ext in enumerate(extensions, 1):
        formatted_list.append(f".{ext}")
        if i % 8 == 0:
            formatted_list.append("\n")
    
    return ", ".join(formatted_list)


def get_category_tooltip(category_key: str) -> str:
    """Get tooltip text for a category"""
    if category_key not in CATEGORY_INFO:
        return ""
    
    info = CATEGORY_INFO[category_key]
    ext_count = len(info['extensions'])
    
    # Create comprehensive tooltip
    tooltip = f"{info['emoji']} {info['label']}\n"
    tooltip += f"{info['description']}\n"
    tooltip += f"\n{ext_count} file types supported:\n"
    tooltip += get_category_extensions_formatted(category_key)
    
    return tooltip


def get_all_extensions_for_category(category_key: str) -> set:
    """Get all extensions for a category as a set"""
    if category_key not in CATEGORY_INFO:
        return set()
    
    return set(CATEGORY_INFO[category_key]['extensions'])
