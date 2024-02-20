import Post from "../../components/Post.astro";
import {  } from 'astro';

export interface ResponseData {
    projects: any,
}

export async function get({ params }: any) {
    let projects = await glob("./*.md");
    let content = {"projects":[]}
    for (const project of projects) {
        content["projects"].push(project.rawContent())
    }
    return {
        body: JSON.stringify(content)
    }
} 