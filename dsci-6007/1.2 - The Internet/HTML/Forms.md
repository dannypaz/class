# HTML Forms

## Objectives

* Explain what a web form is.
* Explain what control tags are.
* Build a web form with various controls tags.
* Verify user data with the built-in HTML5 form validation.
* Verify user data with JavaScript-based form validation.

## What's a web form?

If you've ever given your credit card information to a website, performed a search on Google, or logged into Facebook then you've used a web form. **Web forms** (or just forms) are the main way of getting information from your user into your application. Sometimes this information never leaves the browser and sometimes it's sent to a web server.

At it's core, Google's search page is a simple web form with one input and two buttons.

![](http://i.imgur.com/hcP92bJ.png)

With a little code, we can easily recreate their form.

```html
<form>
	<input type="text">

	<div>
		<button>Google Search</button>
		<button>I'm Feeling Lucky</button>
	</div>
</form>
```

Like all forms, this one contains a few control tags.

## What's a control tag?

The following HTML tags are **control tags**—tags that build elements which a user can control to give information.

- `<input>`
- `<select>`
- `<textarea>`
- `<button>`

Before the rise of JavaScript, control tags were always nested within a `<form>` tag. That's because control tags have a predefined behavior when nested inside of a `<form>` tag. Nowadays, the `<form>` element isn't needed anymore. Fortunately for you, we'll be teaching you both techniques.

## The `<input>` tag

There are [many ways](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) the `<input>` control tag can be used. But the most common (and default) way is as a single-line text field.

```html
<input type="text">
```

Remember when we talked about semantic HTML? We also have semantic `<input>` types that help describe the nature of the input. Aside from `type="text"`, there's also the following textual controls.

```html
<input type="email">
<input type="search">
<input type="password">
<input type="tel">
<input type="url">
```

These control types provides some basic input validation, data formatting, and/or special keyboard types on mobile.

Additionally, there are the following non-textual controls.

```html
<input type="color">
<input type="date">
<input type="file">
<input type="number">
<input type="range">
```

### Radios and Checkboxes

The `<input>` control also has a `radio` and `checkbox` type for displaying both radio buttons and checkboxes respectively. Both of these types allow the user to select options from a set of choices. The key difference is that radio buttons only allow one choice.

```html
<input type="radio" name="rappers" value="Biggie"> Biggie
<input type="radio" name="rappers" value="Dre"> Dre
<input type="radio" name="rappers" value="Snoop" checked> Snoop
```

As you can see, each radio button must belong to a **group** which is defined by setting the `name` attribute to the same value. This forces one radio button to be selected per group.

On the other hand, checkboxes use `type="checkbox"` and its `name` must be different per `<input>` control.

```html
<input type="checkbox" name="rapper1" value="Ice Cube"> Ice Cube
<input type="checkbox" name="rapper2" value="Kanye" checked> Kanye
<input type="checkbox" name="rapper3" value="Eminem"> Eminem
```

### Hidden fields

Hidden fields are as described -- hidden. There is no visual for the user to see. These have been quite useful in passing data in through the form that the user does not need to enter specifically (e.g. An item ID).

```html
<input type="hidden" name="secret" value="Tupac is alive">
```

## The `<label>` tag

Each control tag will usually have some sort of caption that instructs the user on what type of input to give. For example, next to a text box with a caption "Name", you are then expected to type your name in. We use the `<label>` element to specify the text that describes the expected input. For example:

```html
<label>
	Album
  <input type="text" name="album">
</label>
```

You can also connect a `<label>` tag to an `<input>` tag with the `for` and `id` attributes respectively.

```html
<label for="album">Album</label>
<input id="album" type="text" name="album">
```

## The `<select>` tag

You can create select boxes that allow the user to choose from a set of options. You have the ability to allow users to select multiple options by using the `multiple` attribute.

```html
<!-- The second option will be initially selected. -->
<select name="vh1_show">
  <option value="basketball_wives_la">Basketball Wives LA</option>
  <option value="get_rich_or_die_tryin" selected>Get Rich or Die Tryin'</option>
  <option value="black_ink_crew">Black Ink Crew</option>
</select>
```

Multiple choice select boxes.

```html
<!-- The second and third option will be initially selected. -->
<select name="vh1_show" multiple>
  <option value="the_jame_foxx_show">The Jamie Foxx Show</option>
  <option value="fresh_prince_of_bel_air" selected>Fresh Prince of Bel-Air</option>
  <option value="love_and_hip_hop_atlanta">Love and Hip Hop Atlanta</option>
</select>
```

## Buttons

We've seen plenty of buttons before, but let's dig a little bit deeper.

```html
<button name="button">Belly</button>
```

Buttons contain a `type` attribute with three options.

* `button` (default)
* `submit` (default when in a form)
* `reset`

```html
<button type="button">This an anonymous button</button>
<button type="submit">This a submit button</button>
<button type="reset">This a reset button</button>
```

## Assignment

There are more challenges in [this repository](https://github.com/gSchool/html-forms) where you can experiment with the basic control tags. Knowing what types of inputs are available is essential to designing a form that is simple and easy to use. When you encounter a new type ask yourself "what would I use this for?"

## Common Attributes

With control tags, there are a variety of attributes available. Many attributes vary by tag and some are nonstandard but highly recommended. Take a look at [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) and let's discuss.

- autocapitalize
- autocomplete
- autofocus
- checked
- disabled
- maxlength
- minlength
- multiple
- name
- placeholder
- pattern
- required
- readonly
- size
- spellcheck
- tabindex
- value

## HTML and JS Form Validation

### Why?

As a web developer, you will spend an obscene amount of time working on HTML forms. Form validation is a large part of what is project-specific, and it is dependent on what's called "business logic". Because it varies from project to project, what gets validated and how, according to what needs, is something that's always being tweaked, prodded and updated. 9 times out of 10 when you collect information from a user, it's going to be from a form, and you want the user to have a nice experience.

We're also validating our form input because our programs can't work without proper inputs. Writing simple programs up until this point means only one person has been using your program: you. In the future, this won't be the case- sometimes forms are confusing if you don't know how they work in advance. Your users will often make mistakes, and will often need to be corrected in an expedient way that encourages the user to continue interacting with the form.

So what do we do to ensure we get good input for our programs?

## Form Validation

### HTML5 Validation

First, we need to make it easy for humans with good intentions to use our interface. We can use a number of HTML5 capabilities to do this, such as tabindex, input types, and patterns.

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

### What will HTML5 do?

When an element is invalid, two things occur:

* The element will now match a special CSS pseudo-class called :invalid. This allows you to stylize your invalid elements. Similarly, valid elements match the :valid pseudo-class.
* The browser will try to block the user from submitting the form.

## JS Validation

Now that we've done some validation with HTML5, it's time to use JS to finish up the job.

### Accessing values

There are a number of validation libraries that we can use, that will allow us to validate our forms using code someone else has written. Rather than doing that, however, we need to understand how these libraries go about doing what they do, which we'll do by doing some implementation.

First, let's look at how to go about getting the values of the form:

**Get the value of an `input` element**

Given: `<input type="phone" name="phone" id="phone">`

```javascript
var phoneValue = document.getElementById("phone").value;
```

Using either of these techniques, we can access the current value of any `input` element. This also works for `textarea` elements as well.

Take a look at the code below for how to access other kinds of form input through the DOM.

```javascript
var form = document.querySelector('#some-form');
var input = document.querySelector('#some-input');

document.forms;           // Get all forms on a page
form.elements;            // Get all form elements
input.type.toLowerCase(); // Get input type (radio, checkbox, text, etc.)
input.value;              // Get input value
input.name;               // Get input name
input.checked;            // Get the checked status of a checkbox or radio button
input.disabled;           // Get input disabled status
```

[source: gomakestuff](http://gomakethings.com/ditching-jquery/#working-with-forms)

[(why we're using .checked)](https://jsperf.com/prop-vs-ischecked/5)

![](https://students-gschool-production.s3.amazonaws.com/uploads/asset/file/410/propvschecked.png)


### When to access values

Now that we know how to access values, we need to know when to access them. If we were to use the above code when the page loads, we would only see blank or placeholder values. Why? Because we need to wait to check these until the user tries to submit the form, or until the user is done filling out the field.

**submit event**  

In order to check the form when the user hits the "I'm finished filling out this form button", we need to listen for the "submit" action on the form. *Remember, we need to select the form, not the submit button.* This is for when you want to validate the entire form at once.

```javascript
var myForm = document.getElementById('myForm');
myForm.addEventListener('submit', function () {
	// do entire form validation here
});
```

**blur event**  

If we want to check a field as soon as a user is done typing, we can listen to the "blur" event. The blur event fires as soon as a field loses focus.

```javascript
var myForm = document.getElementById('myForm');
myForm.addEventListener('blur', function () {
	// do single input validation here
});
```

#### What do I do if there's an error?

A typical pattern is to display either next to the incorrectly filled out element, or at the top of the form, a new DOM element that lists the error in question. Try to be descriptive, tell the user what they did wrong- did they miss filling out the field, or did they just forget to put dashes in their phone number?

When you bind an event handler to something that has a _default action_, the handler will fire and then the default action will happen. A default action is something like a form's submission to the location that's in the action property, or the navigation that happens when you click a link. In order to render errors, you have to stop the default action. One way is to use `event.preventDefault();`, but simply calling `return false` from within a jQuery event handler will stop the default event from occuring.


```javascript
var myForm = document.getElementById('myForm');
myForm.addEventListener('submit', function() {
  if (some_error_condition) {
    var errDiv = document.createElement('div');
    errDiv.className = 'error';
    errDiv.textContent = 'Please fix your phone number';
    myForm.appendChild(errDiv);
    return false; 			// This tells the submission not to happen
  }
});
```

## Displaying Validation with Materialize

The [dialogs](http://materializecss.com/dialogs.html) documentation page offers many helpful tools to help you properly display validation errors.

## Questions

* Why do we need to do form validation inside an event listener?
* What is a better experience for the user- using the `required` attribute, or using JS to ensure all required fields are checked?
* Why might browser validation not be enough?
* What would happen if someone used console Javascript to submit their form, bypassing your validation?

## Styling Forms with CSS Frameworks

- [Bootstrap Forms](http://getbootstrap.com/css/#forms)
- [Materialize Forms](http://materializecss.com/forms.html)

## Additional Resources on Forms

- https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/My_first_HTML_form
- https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input
- http://diveintohtml5.info/forms.html
- http://www.wufoo.com/html5/
- http://morgancarter.com.au/design-solutions/which-input-when

## Slides

* [Slides](https://docs.google.com/presentation/d/1BeonEGxHl0uQUWQJc_1XJFKS794T4zZnJAIUUoUBy4M/edit#slide=id.p)
