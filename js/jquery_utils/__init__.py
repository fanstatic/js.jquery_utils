from fanstatic import Library, Resource
from js.jquery import jquery

library = Library('jquery_utils', 'resources')

# Define the resources in the library like this.
# For options and examples, see the fanstatic documentation.
# resource1 = Resource(library, 'style.css')

css = Resource(library, 'jquery.utils.css')
jqueryutils = Resource(library, 'jquery.utils.js', depends=[css, jquery],
                                minified='jquery.utils.min.js')

ddbelatedpng = Resource(library, 'jquery.ddbelated.js',
                        depends=[jquery],
                        minified='jquery.ddbelated.min.js')
