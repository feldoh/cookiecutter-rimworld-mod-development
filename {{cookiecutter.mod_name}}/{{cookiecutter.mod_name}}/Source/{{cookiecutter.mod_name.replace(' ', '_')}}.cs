using System.Reflection;
using System.Linq;
using Verse;
using RimWorld;
using UnityEngine;
{%if(cookiecutter.harmony != 'n')%}using HarmonyLib;
{%endif%}
namespace {{cookiecutter.mod_name.replace(' ', '_')}}
{
{%if(cookiecutter.settings != 'n')%}	public static Settings settings;
{%endif%}	public class Mod : Verse.Mod
	{
		public Mod(ModContentPack content) : base(content)
		{
{%if(cookiecutter.helloWorld != 'n')%}			Log.Message("Hello world from {{cookiecutter.mod_name}}");

{% endif %}{%if(cookiecutter.settings != 'n')%}			// initialize settings
			settings = GetSettings<Settings>();

{%endif%}{%if(cookiecutter.harmony != 'n')%}#if DEBUG
			Harmony.DEBUG = true;
#endif

			Harmony harmony = new Harmony("{{cookiecutter.author}}.rimworld.{{cookiecutter.mod_name.replace(' ', '_')}}.main");	
			harmony.PatchAll();
{%endif%}		}
{%if(cookiecutter.settings != 'n')%}
		public override void DoSettingsWindowContents(Rect inRect)
		{
			base.DoSettingsWindowContents(inRect);
			settings.DoWindowContents(inRect);
		}

		public override string SettingsCategory()
		{
			return "{{cookiecutter.mod_name}}";
		}
{% endif %}	}
}