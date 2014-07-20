import sublime, sublime_plugin

class ChangeLayout(sublime_plugin.TextCommand):
	engToRus = {
		'q' : 'й' ,
		'w' : 'ц' ,
		'e' : 'у' ,
		'r' : 'к' ,
		't' : 'е' ,
		'y' : 'н' ,
		'u' : 'г' ,
		'i' : 'ш' ,
		'o' : 'щ' ,
		'p' : 'з' ,
		'[' : 'х' ,
		']' : 'ъ' ,
		'a' : 'ф' ,
		's' : 'ы' ,
		'd' : 'в' ,
		'f' : 'а' ,
		'g' : 'п' ,
		'h' : 'р' ,
		'j' : 'о' ,
		'k' : 'л' ,
		'l' : 'д' ,
		';' : 'ж' ,
		'\'' : 'э' ,
		'z' : 'я' ,
		'x' : 'ч' ,
		'c' : 'с' ,
		'v' : 'м' ,
		'b' : 'и' ,
		'n' : 'т' ,
		'm' : 'ь' ,
		',' : 'б' ,
		'.' : 'ю' ,
		'`' : 'ё' ,
		'Q' : 'Й' ,
		'W' : 'Ц' ,
		'E' : 'У' ,
		'R' : 'К' ,
		'T' : 'Е' ,
		'Y' : 'Н' ,
		'U' : 'Г' ,
		'I' : 'Ш' ,
		'O' : 'Щ' ,
		'P' : 'З' ,
		'{' : 'Х' ,
		'}' : 'Ъ' ,
		'A' : 'Ф' ,
		'S' : 'Ы' ,
		'D' : 'В' ,
		'F' : 'А' ,
		'G' : 'П' ,
		'H' : 'Р' ,
		'J' : 'О' ,
		'K' : 'Л' ,
		'L' : 'Д' ,
		':' : 'Ж' ,
		'"' : 'Э' ,
		'Z' : 'Я' ,
		'X' : 'Ч' ,
		'C' : 'С' ,
		'V' : 'М' ,
		'B' : 'И' ,
		'N' : 'Т' ,
		'M' : 'Ь' ,
		'<' : 'Б' ,
		'>' : 'Ю' ,
		'~' : 'Ё' ,
		}

	rusToEng = {
		'й' : 'q' ,
		'ц' : 'w' ,
		'у' : 'e' ,
		'к' : 'r' ,
		'е' : 't' ,
		'н' : 'y' ,
		'г' : 'u' ,
		'ш' : 'i' ,
		'щ' : 'o' ,
		'з' : 'p' ,
		'х' : '[' ,
		'ъ' : ']' ,
		'ф' : 'a' ,
		'ы' : 's' ,
		'в' : 'd' ,
		'а' : 'f' ,
		'п' : 'g' ,
		'р' : 'h' ,
		'о' : 'j' ,
		'л' : 'k' ,
		'д' : 'l' ,
		'ж' : ';' ,
		'э' : '\'' ,
		'я' : 'z' ,
		'ч' : 'x' ,
		'с' : 'c' ,
		'м' : 'v' ,
		'и' : 'b' ,
		'т' : 'n' ,
		'ь' : 'm' ,
		'б' : ',' ,
		'ю' : '.' ,
		'ё' : '`' ,
		'Й' : 'Q' ,
		'Ц' : 'W' ,
		'У' : 'E' ,
		'К' : 'R' ,
		'Е' : 'T' ,
		'Н' : 'Y' ,
		'Г' : 'U' ,
		'Ш' : 'I' ,
		'Щ' : 'O' ,
		'З' : 'P' ,
		'Х' : '{' ,
		'Ъ' : '}' ,
		'Ф' : 'A' ,
		'Ы' : 'S' ,
		'В' : 'D' ,
		'А' : 'F' ,
		'П' : 'G' ,
		'Р' : 'H' ,
		'О' : 'J' ,
		'Л' : 'K' ,
		'Д' : 'L' ,
		'Ж' : ':' ,
		'Э' : '"' ,
		'Я' : 'Z' ,
		'Ч' : 'X' ,
		'С' : 'C' ,
		'М' : 'V' ,
		'И' : 'B' ,
		'Т' : 'N' ,
		'Ь' : 'M' ,
		'Б' : '<' ,
		'Ю' : '>' ,
		'Ё' : '~' ,
	}

	def convertToRussian(self, text):
		result = list( text )
		for i, _c in enumerate( result ) :
			if (_c in self.engToRus) :
				result[i] = self.engToRus[_c]
		return ''.join( result )

	def convertToEnglish(self, text):
		result = list( text )
		for i, _c in enumerate( result ) :
			if (_c in self.rusToEng) :
				result[i] = self.rusToEng[_c]
		return ''.join( result )

	def isRussian(self, text):
		for _c in text:
			if _c in self.rusToEng:
				return True
		return False

	def run(self, edit):
		view = self.view

		selection = view.sel()
		for _s in selection :
			text = view.substr( _s )
			if len( text ):
				if ( self.isRussian( text ) ):
					converted = self.convertToEnglish( text )
				else :
					converted = self.convertToRussian( text )
				view.replace( edit, _s, converted )