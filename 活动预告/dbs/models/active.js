const mongoose = require('mongoose')

// mongoose.connect(mongodbUrl, {
//   useCreateIndex: true,
//   useNewUrlParser: true
// })

let activeSchema = new mongoose.Schema({
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