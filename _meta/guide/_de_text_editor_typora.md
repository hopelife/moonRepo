[Typora Support](http://support.typora.io/)

# Quick Strart


## Markdown Reference

### Block Elements

#### Task List

```markdown
- [ ] a task list item
- [ ] list syntax required
- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed
```

- [ ] a task list item
- [ ] list syntax required
- [ ] normal **formatting**, @mentions, #1234 refs
- [ ] incomplete
- [x] completed

#### Math Blocks
You can render LaTeX mathematical expressions using **MathJax**.

Input $$, then press ‘Return’ key will trigger an input field which accept Tex/LaTex source. Following is an example:

$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$

In markdown source file, math block is LaTeX expression wrapped by ‘$$’ mark:

```latex
$$
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} 
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0 \\
\end{vmatrix}
$$
```

### Span Elements

#### Images

```markdown
![Alt text](/path/to/img.jpg)

![Alt text](/path/to/img.jpg "Optional title")
```

#### Emoji ``:happy:``
Input emoji with syntax :smile:.

User can trigger auto-complete suggestions for emoji by pressing ESC key, or trigger it automatically after enable it on preference panel. Also, input UTF8 emoji char directly from Edit -> Emoji & Symbols from menu bar is also supported.

#### Inline Math
To use this feature, first, please enable it in Preference Panel -> Markdown Tab. Then use ``$`` to wrap TeX command, for example: ``$\lim_{x \to \infty} \exp(-x) = 0$`` will be rendered as LaTeX command.

To trigger inline preview for inline math: input “$”, then press ESC key, then input TeX command, a preview tooltip will be visible like below:

![inline-math](./images/de_text_editor_typora/inline-math.gif)

#### Subscript
To use this feature, first, please enable it in Preference Panel -> Markdown Tab. Then use ~ to wrap subscript content, for example: H~2~O, X~long\ text~/

#### Superscript
To use this feature, first, please enable it in Preference Panel -> Markdown Tab. Then use ^ to wrap superscript content, for example: X^2^.

#### Highlight
To use this feature, first, please enable it in Preference Panel -> Markdown Tab. Then use == to wrap highlight content, for example: ==highlight==.

## Draw Diagrams With Markdown

[Draw Diagrams With Markdown](http://support.typora.io/Draw-Diagrams-With-Markdown/)

### Sequence

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bot thinks
Bob->Alice: I am good thanks!
```

### Flow chart

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

### Mermaid

#### Sequence

```mermaid
%% Example of sequence diagram
  sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
    Bob->>Alice: Not so good :(
    else is well
    Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
    Bob->>Alice: Thanks for asking
    end
```

#### Flowchart

```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

#### Gantt

```mermaid
%% Example with slection of syntaxes
        gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid

        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d

        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d

        section Documentation
        Describe gantt syntax               :active, a1, after des1, 3d
        Add gantt diagram to demo page      :after a1  , 20h
        Add another diagram to demo page    :doc1, after a1  , 48h

        section Last section
        Describe gantt syntax               :after doc1, 3d
        Add gantt diagram to demo page      : 20h
        Add another diagram to demo page    : 48h
```
