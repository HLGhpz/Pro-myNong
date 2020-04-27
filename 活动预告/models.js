const mongoose = require('mongoose')

const mongodbUrl = 'mongodb://localhost:27017/active-database'

mongoose.connect(mongodbUrl, {
  useCreateIndex: true,
  useNewUrlParser: true
})

const activeSchema = new mongoose.Schema({
	title: {
    type: String,
    unique: true
	},
	date: {
		type: Date
	}
});

const active = mongoose.model('active', activeSchema);

module.exports = {active}