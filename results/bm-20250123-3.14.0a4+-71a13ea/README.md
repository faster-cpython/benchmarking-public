# Results

- fork: mdboom/test_without_pgo_wor
- version: 3.14.0a4+
- config: 
- commit hash: [71a13ea](https://github.com/mdboom/cpython/commit/71a13ea)
- commit date: 2025-01-23T12:56:42-05:00
- commit merge base: [f18b2264929c56360c868d7ad77508035d751352](https://github.com/python/cpython/commit/f18b2264929c56360c868d7ad77508035d751352)
- ref: test_without_pgo_wor

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/12935151985)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea.json)

### vs. 3.10.4

- Geometric mean: 1.091x slower (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, flaskblogging, float, gc_traversal, generators, genshi_text, genshi_xml, go, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.10.4.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.081x slower (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 2to3, aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, chaos, comprehensions, coroutines, coverage, create_gc_cycles, crypto_pyaes, dask, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, go, hexiom, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, mypy2, nqueens, pathlib, pickle, pickle_dict, pickle_list, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, tomli_loads, tornado_http, typing_runtime_protocols, unpack_sequence, unpickle, unpickle_list, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.12.0.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.153x slower (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 2to3, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bench_mp_pool, bench_thread_pool, bpe_tokeniser, chameleon, chaos, comprehensions, connected_components, coroutines, coverage, create_gc_cycles, crypto_pyaes, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, djangocms, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, genshi_text, genshi_xml, gevent_hub, go, hexiom, html5lib, json, json_dumps, json_loads, k_core, logging_format, logging_silent, logging_simple, mako, many_optionals, mdp, meteor_contest, nqueens, pathlib, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, shortest_path, spectral_norm, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, subparsers, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, tornado_http, typing_runtime_protocols, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.13.0.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.058x slower (HPT: reliability of 84.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: 🔴 2to3, async_generators, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bench_mp_pool, bench_thread_pool, bpe_tokeniser, chaos, comprehensions, connected_components, coroutines, coverage, create_gc_cycles, crypto_pyaes, deepcopy, deepcopy_memo, deepcopy_reduce, deltablue, django_template, docutils, dulwich_log, fannkuch, float, gc_traversal, generators, genshi_text, genshi_xml, go, hexiom, html5lib, json, json_dumps, json_loads, k_core, logging_format, logging_silent, logging_simple, mako, many_optionals, mdp, meteor_contest, nqueens, pathlib, pickle_pure_python, pidigits, pprint_pformat, pprint_safe_repr, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, shortest_path, spectral_norm, sphinx, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sqlite_synth, subparsers, sympy_expand, sympy_integrate, sympy_str, sympy_sum, telco, thrift, tomli_loads, typing_runtime_protocols, unpickle_pure_python, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
- [📄table](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-base.md)
- [📈time plot](bm-20250123-pythonperf1-amd64-mdboom-test_without_pgo_wor-3.14.0a4%2B-71a13ea-vs-base.svg)

