# Semantic Markup

You may have been using various tags to help you style your content. `<h1>` text is larger than `<p>` text, and `<strong>` makes something bold. While on its own this is usually fine, HTML was not designed to style content, but to "mark up" its distinct components *semantically*.

Semantic HTML means to identify your content by its meaning, rather than its presentation. `<h1>` indicates that something is the most important header on the page, and `<p>` means that something is a paragraph of text. It's easy to get in the habit of using the generic tags, `<div>` and `<span>`, to set any other kind of content, such as a footer, apart. HTML actually has a wealth of tags, such as `<footer>`, that are intended to help identify content.

You may be realizing at this point that within the HTML `<body>`, you could just use `<div>` and `<span>` (or almost any other tag) to markup an entire document, and just use CSS classes to distinguish between them. It's an unfortunately common practice. The advantages of writing semantically are:

* **Readability**. Semantically written documents are much easier for other developers to follow.
* **Accessibility**. Assistive devices, such as screen-readers for the visually impaired, rely on tags to help users navigate through content.
* **Consumability**. Tools like screen-scrapers and crawlers look for markup to separate content from structure.
* **SEO**. Search engines use semantic markup to map your site and identify content. Poor markup can result in down-ranking.
* **Separation of Concerns**.  HTML is primarily concerned with *content*, while CSS is primarily concerned with *presentation* (JavaScript is concerned with *behavior*). While it is possible to dictate appearance with HTML, manipulate content with CSS, and do just about anything with JavaScript, each of them specializes in one thing. By "separating concerns", you allow each technology to stick with what it's good at.

## Exercise: Semantic Scavenger Hunt

Spend the next 30 minutes finding examples of semantic tags being used "in the wild", aka on live websites. For each tag, use MDN to help you write a definition of the semantic use of the tag, then find a live example, record the url for the website where the tag is used and write a sentence about (Is the tag is being used appropriately? Why or why not? You don't need to find an example for every tag, just do as many as you can. We'll share examples of uses found after completing.

Here are the various semantic tags to define and look for on the internet:

### Structural

Use these tags to create the overall hierarchy of the content in your page:

* header
* nav
* main
* section
* article
* aside
* footer
* div

Lets look deeper into each of these:

#### Header
A `header` tag is most commonly found at the top of a page. It contains the logo or name of the site and often also includes the `nav` tag (though it does not need to). Furthermore, you can place `header` tags inside of other structural tags such as `article` or `section` tags. They will often have a heading tag (`h1 - h6`) to give a title/heading to the content it is the header of.

`header` tags can also be found inside of other tag elements. For example, if a specific section of your page has unique content that can be described with it's own title you may consider putting a `header` tag inside of a `section` tag. That `header` tag might optionally have an `h1-h6` tag as well to give some insight into the relative importance of that section.

#### Navigation

All links used for navigating around a site (internal links) should be contained inside of a `nav` tag. The `nav` tag often lives inside of a `header` tag (in a navbar at the top of the page). Depending on the layout and look you want your site to have it can also make sense to put the navigation links above or below the header. Alternatively, it may make sense to have a `nav` tag inside of an `aside` or even a `footer` tag depending on how you want to set up the user experience for your site.

#### Main

The `main` tag is intended to contain content that is not repeated elsewhwere in your site. This is where the bulk of your other HTML will live. There should only be one `main` tag per HTML document.

#### Section and Article

The distinction between `section` and `article` tags is an ongoing debate.

W3C defines an `article` tag as such:

>"The article element represents a complete, or self-contained, composition in a document, page, application, or site and that is, in principle, independently distributable or reusable, e.g. in syndication. This could be a forum post, a magazine or newspaper article, a blog entry, a user-submitted comment, an interactive widget or gadget, or any other independent
item of content.
 
>When article elements are nested, the inner article elements represent articles that are in principle related to the contents of the outer article. For instance, a blog entry on a site that accepts user-submitted comments could represent the comments as article elements nested within the article element for the blog entry."

They define a `section` tag this way: 

>"The section element represents a generic section of a document or application. A section, in this context, is a thematic grouping of content. Each section should be identified, typically by including a heading (h1-h6 element) as a child of the section element.
>
>Examples of sections would be chapters, the various tabbed pages in a tabbed dialog box, or the numbered sections of a thesis. A Web site's home page could be split into sections for an introduction, news items, and contact information."

Based on these definitions, a possible structure of a blog site could look like this:

```html

<div id="blog-articles-about-animals">
   
  <section>
    <h1>Articles about Turtles</h1>
    <article>
      <h2>Where Turtles Live</h2>
      <p>blah blah</p>
    </article>
    <article>
      <h2>What Turtles Eat</h2>
      <p>blah blah</p>
    </article>
  </section>
   
  <section>
    <h1>Articles about Chickens</h1>
    <article>
      <h2>History of Chickens in USA</h2>
      <p>blah blah</p>
    </article>
    <article>
      <h2>Chickens in the Wild</h2>
      <p>blah blah</p>
    </article>
  </section>
   
</div>
```

[This is a good article in Smashing Magazine](https://www.smashingmagazine.com/2013/01/the-importance-of-sections/#the-problem-with-div) that would likely agree with this usage. However, [this one](http://www.hongkiat.com/blog/html-5-semantics/) would argue that `section` tags should be nested inside of `article` tags.

Confused? Don't worry. As stated above there is an open debate about how to properly use these two tags. Reading those two above articles as well as doing a some more of your own research will allow you to make your own decisions on when and how to use these tags.

If you want a general rule you can ask yourself these questions: 

1. Would the content make sense all by itself in an RSS feed reader that is pulling content from your site? If so, use `article`
2. Is the content related to other content on the page? If so, use `section`
3. And if there isn't any semantic relationship with the containers, use `div`

Alternatively, check out [this](http://html5doctor.com/downloads/h5d-sectioning-flowchart.png) flowchart.

#### Aside

An `aside` tag is used as a container for content that is related to the main content of the page but not directly a part of it. A use case for an `aside` tag is often a sidebar navigation feature for your site. In this case the `aside` would be outside of your `main` tag and contain a `nav` tag (and possibly its own `header` and `footer` if appropriate). 

#### Footer

The `footer` usually contains information at the bottom of the content area and this information is related to the page content in some way. It usually displays the copyright or credit to the author, links to related documents, copyright/privacy/etc links for the entire site. Some sites also use footers to contain navigation links as well (those links of course also being inside of a `nav` tag).

#### Div

The `div` tag is the most generic element used for structuring a page. The `div` itself has nearly no real meaning in HTML5, but is simply a division, or a general container of the content. A `div` will be useful when creating separations in the content that can’t be used by the other structure tags.

A little bit of history for you: In HTML4 the structure tags of `header`, `nav`, `footer`, etc, didn’t exist. All you had were `div` tags that could be differentiated by classes and ids. 

### Text Markup

These tags are for marking up text content within a structural element:

* p
* h1-h6
* ul
* ol
* li
* blockquote
* em
* strong
* b
* i
* s
* mark
* hr
* wbr
* pre
* br
* cite
* code
* kybd
* samp
* var
* q
* data
* abbr
* small
* sub
* sup
* del
* ins
* time
* address
* details
* summary

Some of these tags are fairly self explanitory but for those tags that aren't **here is MDN's [HTML element reference page](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) for more about these tags' intended uses.**


#### Description Lists

Description lists are for key-value pairs of information, like glossaries.

```html
<dl>
    <dt>HTML</dt>
    <dd>Hypertext Markup Language</dd>
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
    <dt>JS</dt>
    <dd>JavaScript</dd>
</dl>
```

Note for memorization: `<dl>` means "description list", `<dt>` means "description term", and `<dd>` means "description definition".

**You Try**:

  - Create a description list
  - Create the terms rock, paper, scissors
  - Create the definitions for each term, an example would be "Rock beats scissors"

## Exercise: The Semantic News

Fork and clone the [semantic HTML](https://github.com/gSchool/semantic-html-exercise) repository. `index.html` is a news site that's been marked up with `<div>` and `<span>` tags. Using the list of tags above, update the code with semantic tags. When you're done, add/commit/push, and then submit a pull request.

> Fun fact: Facebook has implemented something called [Instant Articles](https://instantarticles.fb.com) to help news sources have their articles be more friendly with Facebook. Their docs stress the use of [semantic tags and specific formats](https://developers.facebook.com/docs/instant-articles).

## Exercise: Rectifying past wrongs

Go back to an exercise you completed last week without using semantic HTML (maybe something in the Intro to HTML LE). Change out the unsemantic markup with semantic tags. Share your solution with a classmate and ask for constructive criticism about the markup used.

## Resources

- https://developer.mozilla.org/en-US/docs/Web/HTML/Element
- http://html5doctor.com/element-index/

## Slides

[Slides](https://docs.google.com/presentation/d/1CPwESaDcaiN06Rgie4sctVpfQ-wPCOT2d5nV4kskrYs/edit#slide=id.g12bbca21b1_0_107)
