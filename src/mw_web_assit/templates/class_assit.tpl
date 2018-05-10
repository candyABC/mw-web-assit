{% for object in objects %}
export class {{ object.name|capitalize }}Assit{
    constructor (){
        {% for prop in object.props %}
        this.{{ prop.name }}={{ prop.default }}
        {% endfor %}
      }
    static rules(){
        return {
        {% for prop in object.props %}
        {{ prop.name }}:[
            {required: true,{% if prop.ruleType %}type:'{{ prop.ruleType}}',{% endif %} message: '{{ prop.description }}', trigger: 'blur'},
            {required: true,{% if prop.ruleType %}type:'{{ prop.ruleType}}',{% endif %} message: '{{ prop.description }}', trigger: 'change'}]
        {% endfor %}
      }
    }
}
{% endfor %}
