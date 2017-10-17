# HTML5 Form Validation

### Entry Ticket
In order to start this Learning Experience, you need to be able to:

* Write HTML Forms
	* Use `input` tags
	* Specify a `type` on an input tag
	* Use a submit button and a `form` tag to submit your values to another page

### Objectives
Bt the end of this Learning Experience you should be able to:

* Use HTML5 input types as a first-line validation technique
* Use other HTML5 techniques to validate input

### Why?

As a web developer, you will spend just an obscene amount of time working on HTML forms. Form validation is a large part of what is project-specific, and dependent on what's called "business logic". Because it varies from project to project, what gets validated and how, according to what needs, is something that's always being tweaked, prodded and updated. 9 times out of 10 when you collect information from a user, it's going to be from a form, and you want the user to have a nice experience.

We're also validating our form input because our programs can't work without proper inputs. Writing simple programs up until this point means only one person has been using your program: you. In the future, this won't be the case- sometimes forms are confusing if you don't know how they work in advance. Your users will often make mistakes, and will often need to be corrected in an expedient way that encourages the user to continue interacting with the form.

So what do we do to ensure we get good input for our programs?

## Form Validation

### HTML5 Validation

First, we need to make it easy for humans with good intentions to use our interface. We can use a number of HTML5 capabilities to do this, such as tabindex, input types, and patterns.

*(Required)* [Read this article about HTML5 Forms](http://diveintohtml5.info/forms.html), focus specifically on input types and [validation](http://diveintohtml5.info/forms.html#validation).

After that, given the form below, change it to use HTML5 form validation techniques.
Make sure:

 * Email fields are type="email"
 * numerical fields are type="number", one that makes sense
 * Required fields have the `required` attribute (with no ="true"- check the documentation)
 * Set the `tabindex` property on each form element

```html
<form>
	<label>Name (required)</label>
	<input type="text" name="name">
	<label>Email (required)</label>
	<input type="text" name="email">
	<label>Age (required, must be older than 13)</label>
	<input type="text" name="age">

	<label>Number of siblings</label>
	<input type="text" name="siblings">

	<label>Number of rooms in your house</label>
	<input type="text" name="rooms">

	<label>Blog url</label>
	<input type="text" name="blog">

	<label>Twitter Username</label>
	<input type="text" name="twitter">
	<input type="submit">
</form>

```

***Bonus*** If you know regex, use the `pattern` property to ensure users include an @ sign in front of their twitter username.

### Validating with JavaScript

Not every form can be checked with a simple "type" field. Also, [not every browser](http://caniuse.com/#search=type%3D) can use every type. So, we need to do some validation using jQuery.

For more information on how to do that, see this article:

[Form Validation With JavaScript](https://github.com/gschool/browser-dom-curriculum/Form Validation.md)
