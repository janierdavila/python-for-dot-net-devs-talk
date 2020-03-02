//functions
int[] numbers = new[] { 1, 2, 3, 4, 5, 6 };

foreach (var n in numbers)
{
	Console.Write(n + ",");
}

//yield use
void Main()
{
	var nums = FilterNumbers(n=> n % 2 == 0);
	foreach (var n in nums)
	{
		Console.WriteLine(n);
	}
}

IEnumerable<int> FilterNumbers(Predicate<int> predicate)
{
	for (int i = 0; i < 100; i++)
	{
		if(predicate(i))
			yield return i;
	}
}

#lambda
Func<int, int, int> add = (int a, int b) => a + b;

var c = add(5, 6);
Console.Write(c);

# Custom Attributes
void Main()
{	
	var attrs = Attribute.GetCustomAttributes(typeof(SampleClass));
	var author = (Author)attrs[0];
	Console.Write(author.version);
}

[AttributeUsage(AttributeTargets.Class |
				AttributeTargets.Struct)]
public class Author : System.Attribute
{
	private string name;
	public double version;

	public Author(string name)
	{
		this.name = name;
		version = 1.0;
	}
}

[Author("Janier", version = 1.1)]
class SampleClass
{ 
}