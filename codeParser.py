from pycparser import c_parser , c_ast , parse_file
import re
text = r"""
    typedef int Node, Hash;
    // this is a comment
    void HashPrint(Hash* hash, void (*PrintFunc)(char*, char*))
    {
        unsigned int i;

        if (hash == NULL || hash->heads == NULL)
            return;

        for (i = 0; i < hash->table_size; ++i)
        {
            Node* temp = hash->heads[i];

            while (temp != NULL)
            {
                PrintFunc(temp->entry->key, temp->entry->value);
                temp = temp->next;
            }
        }
    }
"""

def extract_comments(code):
    # This regex captures single-line and multi-line comments
    comments = re.findall(r'(/\*.*?\*/|//.*?$)', code, re.DOTALL | re.MULTILINE)
    return comments

def parse_with_comments(code):
    comments = extract_comments(code)
    code_without_comments = re.sub(r'(/\*.*?\*/|//.*?$)', '', code, flags=re.DOTALL | re.MULTILINE)
    
    parser = c_parser.CParser()
    ast = parser.parse(code_without_comments)
    
    # You can then attempt to map `comments` back to relevant parts of `ast`
    return ast, comments



ast,comments = parse_with_comments(text)
ast.show()
print(comments)