import re
from datetime import datetime
from typing import List, Tuple, Dict

from docutils import nodes
from docutils.nodes import Element, TextElement
from docutils.parsers.rst import Directive
from sphinx.addnodes import pending_xref
from sphinx.application import Sphinx
from sphinx.directives import Node
from sphinx.domains import Domain
from sphinx.roles import XRefRole
from sphinx.util.nodes import set_source_info
from sphinx.writers.html5 import HTML5Translator
from sphinx.writers.texinfo import TexinfoTranslator
from sphinx.writers.text import TextTranslator


class PostNode(nodes.General, nodes.Element):
    name = "PostNode"


def visit_post_node_html(translator: HTML5Translator, node: PostNode):
    translator.visit_section(node)


def depart_post_node_html(translator: HTML5Translator, node: PostNode):
    translator.depart_section(node)


def visit_post_node_texinfo(translator: TexinfoTranslator, node: PostNode):
    translator.visit_section(node)


def depart_post_node_texinfo(translator: TexinfoTranslator, node: PostNode):
    translator.depart_section(node)


def visit_post_node_text(translator: TextTranslator, node: PostNode):
    translator.visit_section(node)


def depart_post_node_text(translator: TextTranslator, node: PostNode):
    translator.depart_section(node)


def _fetch_date_from_file(node):
    date_patten = re.compile(r"(\d{4}-\d{2}-\d{2})")
    dates = date_patten.findall(node.source)
    date_str = dates[0] if dates else None
    date = datetime.strptime(date_str, "%Y-%m-%d")
    node["publish_date"] = date
    return date


class PostDirective(Directive):
    has_content = True

    def run(self) -> list[Node]:
        node = PostNode()
        node.document = self.state.document
        set_source_info(self, node)
        date = _fetch_date_from_file(node)
        node.append(
            nodes.line(text=f"Published on: {date.strftime('%d %B %Y')}"),
        )
        node.append(
            nodes.transition()
        )
        return [node]


class AllPostsNode(TextElement):
    pass


class Posts(Domain):
    name = "posts"
    label = "List of all the posts"

    roles = {
        'reref': XRefRole()
    }

    directives = {
        'all': AllPostsNode,
    }

    initial_data = {
        'objects': [],
        'obj2ingredient': {},
    }

    def merge_domaindata(self, docnames: List[str], otherdata: Dict) -> None:
        print(f"---------------------------> Merging domain data")
        pass

    def resolve_any_xref(self, env: "BuildEnvironment", fromdocname: str, builder: "Builder", target: str,
                         node: pending_xref, contnode: Element) -> List[Tuple[str, Element]]:
        print(f"---------------------------> Resolving XRef")
        pass


def setup(app: Sphinx):
    app.add_node(
        PostNode,
        html=(visit_post_node_html, depart_post_node_html),
        latex=(visit_post_node_texinfo, depart_post_node_texinfo),
        text=(visit_post_node_text, depart_post_node_text),
    )
    app.add_domain(Posts)
    app.add_directive("post", PostDirective)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
