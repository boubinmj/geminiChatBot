# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# flake8: noqa: W291

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)

template_docs = PromptTemplate.from_template(
    """## Context provided:
{% for doc in docs%}
<Document {{ loop.index0 }}>
{{ doc.page_content | safe }}
</Document {{ loop.index0 }}>
{% endfor %}
""",
    template_format="jinja2",
)

inspect_conversation_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an AI assistant for the NYU Wagner Amissions Team "
Your role is to answer questions about NYU Wagner asked by prospective students.""",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

rag_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an AI assistant for the NYU Wagner Admissions Team. 

Answer to the best of your ability using the context provided. 
If you're unsure, it's better to acknowledge limitations than to speculate.
""",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
