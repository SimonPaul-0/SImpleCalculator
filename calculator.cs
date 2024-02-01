using System;
using System.Text.RegularExpressions;

class Calculator
{
    static double Calculate(string expression)
    {
        try
        {
            // Validate expression
            if (!Regex.IsMatch(expression, @"^[0-9+\-*/%() ]+$"))
            {
                throw new ArgumentException("Invalid characters in the expression.");
            }

            // Resolve parentheses first
            while (expression.Contains('('))
            {
                Match match = Regex.Match(expression, @"\([^()]+\)");
                if (match.Success)
                {
                    string sub = match.Value.Substring(1, match.Value.Length - 2);
                    double subResult = Calculate(sub);
                    expression = expression.Replace(match.Value, subResult.ToString());
                }
            }

            // Perform calculation
            double result = Convert.ToDouble(new System.Data.DataTable().Compute(expression, ""));
            return result;
        }
        catch (DivideByZeroException)
        {
            return double.NaN; // NaN indicates division by zero
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
            return double.NaN;
        }
    }

    static void Main()
    {
        while (true)
        {
            Console.Write("Enter a mathematical expression: ");
            string expr = Console.ReadLine();

            double res = Calculate(expr);
            if (double.IsNaN(res))
            {
                Console.WriteLine("Error: Division by zero or invalid expression.");
            }
            else
            {
                Console.WriteLine($"Result of the expression: {res}");
            }

            Console.Write("Want to see an intermediate result? (Y/N): ");
            string interChoice = Console.ReadLine().ToUpper();
            if (interChoice == "Y")
            {
                Console.Write("Enter an intermediate expression: ");
                string interExpr = Console.ReadLine();
                double interRes = Calculate(interExpr);
                Console.WriteLine($"Intermediate result: {interRes}");
            }

            Console.Write("Perform another calculation? (Y/N): ");
            string choice = Console.ReadLine().ToUpper();
            if (choice != "Y")
            {
                break;
            }
        }
    }
}
