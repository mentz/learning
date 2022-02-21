require 'rails_helper'

RSpec.describe ImageService do
  let(:user) { User.create!(email: 'abc@dev.com', password: '123123') }
  let(:image_params) do
    {
      title: 'Kitana',
      file: nil,
      user_id: user.id
    }
  end

  describe '.create' do
    subject { ImageService.create(image_params) }
    
    let(:dbl_image) { double('Image', save: false) }

    context 'when image is saved with success' do
      it 'increments db count by one' do
        expect { subject }.to change(Image, :count).by(1)
      end

      it 'calls ImageProcessWorker' do
        expect(ImageProcessWorker).to receive(:perform_async)

        subject
      end
    end

    context 'when image failed to save' do
      before { allow(Image).to receive(:new).and_return(dbl_image) }

      it 'returns false' do
        expect(subject).to eq(false)
      end

      it 'does not call ImageProcessWorker' do
        expect(ImageProcessWorker).not_to receive(:perform_async)

        subject
      end
    end
  end

  describe '.update' do
    subject { ImageService.update(image_params.merge(id: image.id)) }

    let!(:image) { Image.create!(image_params) }

    context 'when image is updated with success' do
      it 'does not increment db count by one' do
        expect { subject }.to change(Image, :count).by(0)
      end

      it 'calls ImageProcessWorker' do
        expect(ImageProcessWorker).to receive(:perform_async)

        subject
      end
    end

    context 'when image failed to save' do
      before { allow(Image).to receive(:update).and_return(false) }

      it 'returns false' do
        expect(subject).to eq(false)
      end

      it 'does not call ImageProcessWorker' do
        expect(ImageProcessWorker).not_to receive(:perform_async)

        subject
      end
    end
  end
end
