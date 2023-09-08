

import plotly.graph_objects as go
import numpy as np

from evonote.gui.utlis import hypenate_texts
from evonote.model.llm import get_embeddings, flatten_nested_list

# see https://plotly.com/python/heatmaps/

def draw_heatmap(z, hovertext):

    fig = go.Figure(data=go.Heatmap(
        z=z,
        hovertext=hovertext,
        hovertemplate="<b>%{hovertext}</b><extra></extra>",
        )
    )

    fig.show()

def prepare_similarity_grid(src_lists, weight_list, query, content_list, width=5):
    query_embeddings = np.array(get_embeddings(query))
    query_embeddings = (query_embeddings.T * np.array(weight_list)).T
    flattened_src_lists, index_start = flatten_nested_list(src_lists)
    src_embeddings = np.array(get_embeddings(flattened_src_lists))
    # make inner product
    src_similarities = np.matmul(query_embeddings, src_embeddings.T).T

    matched_query_list = []
    src_list_for_display = []
    matched_query_score_list = []

    # iterate over lines
    for i, index in enumerate(index_start):
        similarity_for_note = src_similarities[index:index+min(len(src_lists[i]), width)]
        matched_query = []
        matched_query_score = []
        for j, similarity in enumerate(similarity_for_note):
            matched_query_index = np.argmax(similarity)
            matched_query.append(query[matched_query_index])
            matched_query_score.append(similarity[matched_query_index])
        # sort by score
        rank = np.argsort(matched_query_score)[::-1]
        matched_query = np.array(matched_query)[rank]
        matched_query_score = np.array(matched_query_score)[rank]
        if len(src_lists[i]) < width:
            src_list_for_display.append(src_lists[i] + [""] * (width - len(src_lists[i])))
            matched_query = np.concatenate([matched_query, [""] * (width - len(src_lists[i]))])
            matched_query_score = np.concatenate([matched_query_score, [None] * (width - len(src_lists[i]))])
        else:
            src_list_for_display.append(src_lists[i][:width])

        matched_query_list.append(list(matched_query))
        matched_query_score_list.append(list(matched_query_score))

    max_score = -1
    min_score = 1
    # normalize score to 0~1
    for i in range(len(matched_query_score_list)):
        for j in range(len(matched_query_score_list[i])):
            if matched_query_score_list[i][j] is not None:
                max_score = max(max_score, matched_query_score_list[i][j])
                min_score = min(min_score, matched_query_score_list[i][j])

    display_texts = []
    for i in range(len(matched_query_list)):
        display_text_for_note = []
        for j in range(len(matched_query_list[i])):
            if matched_query_list[i][j] == "":
                display_text_for_note.append("")
            else:
                score = matched_query_score_list[i][j]
                new_score = (score - min_score) / (max_score - min_score)
                text = "content: " + hypenate_texts(content_list[i], line_width=100) + "<br>"
                text += "src: " + src_list_for_display[i][j] + "<br>"
                # round score to 3 decimal places
                text += "query: " + matched_query_list[i][j] + "<br>" + "score: " + str(round(new_score, 3))
                display_text_for_note.append(text)
                if score is not None:
                    matched_query_score_list[i][j] = new_score
        display_texts.append(display_text_for_note)

    display_texts = display_texts[::-1]
    matched_query_score_list = matched_query_score_list[::-1]



    return display_texts, matched_query_score_list

def draw_similarity_gui(src_lists, weight_list, query, content_list, width=5):
    matched_query_list, matched_query_score_list = prepare_similarity_grid(src_lists, weight_list, query, content_list, width)
    draw_heatmap(matched_query_score_list, matched_query_list)

if __name__ == "__main__":
    content = ["note1", "note2", "note3"]
    src_lists = [["apple", "beer", "computer", "computer","computer" ,"computer"],
                 ["banana", "speakers"],
                 ["red", "watermelon", "microphone"]]
    query = ["apple", "guitar"]
    matched_query_list, matched_query_score_list = prepare_similarity_grid(src_lists, [0.5, 0.5], query, content)
    draw_heatmap(matched_query_score_list, matched_query_list)