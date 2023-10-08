import {defineUserConfig} from "@vuepress/cli"
import {defaultTheme} from '@vuepress/theme-default'
import * as fs from 'fs';

function get_md_files_names_in_path(path: string) {
    const files = fs.readdirSync(path);
    let file_paths = files.filter((file: string) => file.endsWith('.md'));
    // Filter index.md
    file_paths = file_paths.filter((file: string) => file !== 'index.md');
    return file_paths;
}

export default defineUserConfig({
    repo: 'EvoEvolver/EvoNote',
    docsDir: 'docs',
    head: [['link', { rel: 'icon', href: '/image/favicon.ico' }]],
    // @ts-ignore
    theme: defaultTheme({
        navbar: [
            {
                text: 'Home',
                link: '/',
            }
        ],
        sidebar: {
            "/": [{
                text: 'EvoNote Docs',
                children: [
                    {
                        text: 'Home',
                        link: '/',
                    },
                    {
                      text: 'Writings',
                        link: '/writings',
                    },
                    {
                        text: 'Development',
                        link: '/development',
                    },
                    {
                        text: 'Project tree',
                        link: 'https://evonote.org/html/project_tree.html',
                    }
                ],
            }],
            "/writings": [
                {
                text: 'Writings',
                    link: '/writings',
                children: get_md_files_names_in_path('writings').map((file: string) => {
                    return {
                        text: file.replace('.md', ''),
                        link: `/writings/${file}`,
                    }
                }),
            }]
        },
        sidebarDepth: 2,
    })
})