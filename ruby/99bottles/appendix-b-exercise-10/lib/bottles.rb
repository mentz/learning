# frozen_string_literal: true

# Exercise finished at 26 minutes and 32 seconds.

class Bottles
  def song
    verses(99, 0)
  end

  def verses(bottles_start, bottles_end)
    bottles_start.downto(bottles_end).map do |bottles|
      verse(bottles)
    end.join("\n")
  end

  def verse(bottles)
    "#{statement(bottles)}\n#{action(bottles)}\n"
  end

  private

  def noun(bottles)
    bottles == 1 ? 'bottle' : 'bottles'
  end

  def statement(bottles)
    if bottles.zero?
      'No more bottles of beer on the wall, no more bottles of beer.'
    else
      "#{bottles} #{noun(bottles)} of beer on the wall, #{bottles} #{noun(bottles)} of beer."
    end
  end

  def action(bottles)
    if bottles.zero?
      'Go to the store and buy some more, 99 bottles of beer on the wall.'
    else
      "Take #{bottles == 1 ? 'it' : 'one'} down and pass it around, " \
      "#{bottles == 1 ? 'no more' : bottles - 1} #{noun(bottles - 1)} of beer on the wall."
    end
  end
end
