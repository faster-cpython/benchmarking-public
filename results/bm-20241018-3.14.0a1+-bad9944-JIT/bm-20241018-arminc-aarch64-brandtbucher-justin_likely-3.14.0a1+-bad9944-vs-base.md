# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.001x slower
- HPT reliability: 80.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.62 sec                                                                 | 3.58 sec: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (4): 2to3, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp      | 636 ms                                                                   | 621 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl  | 2.28 sec                                                                 | 2.26 sec: 1.01x faster                                                  |
| async_tree_none  | 461 ms                                                                   | 457 ms: 1.01x faster                                                    |
| async_tree_io_tg | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                  |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_generators, async_tree_cpu_io_mixed_tg, coroutines, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                                   | 115 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.90 ms                                                                  | 4.96 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 113 ms                                                                   | 112 ms: 1.01x faster                                                    |
| xml_etree_iterparse | 151 ms                                                                   | 150 ms: 1.01x faster                                                    |
| unpickle            | 18.9 us                                                                  | 19.6 us: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (11): pickle_pure_python, unpickle_pure_python, tomli_loads, pickle, xml_etree_process, unpickle_list, pickle_dict, json_loads, pickle_list, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.7 ms                                                                  | 14.5 ms: 1.01x faster                                                   |
| python_startup_no_site | 8.79 ms                                                                  | 8.73 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 82.2 ms                                                                  | 83.9 ms: 1.02x slower                                                   |
| mako           | 13.2 ms                                                                  | 13.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal             | 6.51 ms                                                                  | 6.24 ms: 1.04x faster                                                   |
| telco                    | 9.89 ms                                                                  | 9.64 ms: 1.03x faster                                                   |
| asyncio_tcp              | 636 ms                                                                   | 621 ms: 1.03x faster                                                    |
| scimark_monte_carlo      | 90.5 ms                                                                  | 88.7 ms: 1.02x faster                                                   |
| spectral_norm            | 156 ms                                                                   | 154 ms: 1.01x faster                                                    |
| xml_etree_generate       | 113 ms                                                                   | 112 ms: 1.01x faster                                                    |
| python_startup           | 14.7 ms                                                                  | 14.5 ms: 1.01x faster                                                   |
| docutils                 | 3.62 sec                                                                 | 3.58 sec: 1.01x faster                                                  |
| asyncio_tcp_ssl          | 2.28 sec                                                                 | 2.26 sec: 1.01x faster                                                  |
| xml_etree_iterparse      | 151 ms                                                                   | 150 ms: 1.01x faster                                                    |
| async_tree_none          | 461 ms                                                                   | 457 ms: 1.01x faster                                                    |
| scimark_lu               | 149 ms                                                                   | 148 ms: 1.01x faster                                                    |
| async_tree_io_tg         | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                  |
| python_startup_no_site   | 8.79 ms                                                                  | 8.73 ms: 1.01x faster                                                   |
| mdp                      | 3.49 sec                                                                 | 3.50 sec: 1.00x slower                                                  |
| sqlglot_parse            | 1.71 ms                                                                  | 1.71 ms: 1.00x slower                                                   |
| generators               | 58.8 ms                                                                  | 59.1 ms: 1.00x slower                                                   |
| bpe_tokeniser            | 5.92 sec                                                                 | 5.96 sec: 1.01x slower                                                  |
| pprint_safe_repr         | 1.22 sec                                                                 | 1.23 sec: 1.01x slower                                                  |
| nqueens                  | 123 ms                                                                   | 124 ms: 1.01x slower                                                    |
| meteor_contest           | 122 ms                                                                   | 124 ms: 1.01x slower                                                    |
| regex_effbot             | 4.90 ms                                                                  | 4.96 ms: 1.01x slower                                                   |
| nbody                    | 114 ms                                                                   | 115 ms: 1.01x slower                                                    |
| richards_super           | 71.2 ms                                                                  | 72.2 ms: 1.01x slower                                                   |
| pathlib                  | 21.5 ms                                                                  | 21.8 ms: 1.01x slower                                                   |
| hexiom                   | 10.2 ms                                                                  | 10.3 ms: 1.01x slower                                                   |
| typing_runtime_protocols | 214 us                                                                   | 219 us: 1.02x slower                                                    |
| richards                 | 63.4 ms                                                                  | 64.6 ms: 1.02x slower                                                   |
| genshi_xml               | 82.2 ms                                                                  | 83.9 ms: 1.02x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                   | 159 ms: 1.02x slower                                                    |
| sqlite_synth             | 3.89 us                                                                  | 4.00 us: 1.03x slower                                                   |
| mako                     | 13.2 ms                                                                  | 13.6 ms: 1.03x slower                                                   |
| pprint_pformat           | 2.53 sec                                                                 | 2.62 sec: 1.04x slower                                                  |
| unpickle                 | 18.9 us                                                                  | 19.6 us: 1.04x slower                                                   |
| Geometric mean           | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (64): bench_mp_pool, logging_simple, sympy_sum, sympy_integrate, async_tree_memoization, dulwich_log, logging_format, deepcopy_reduce, deltablue, coverage, async_tree_cpu_io_mixed, crypto_pyaes, scimark_sparse_mat_mult, scimark_fft, regex_v8, pickle_pure_python, unpickle_pure_python, html5lib, django_template, async_tree_memoization_tg, tomli_loads, pickle, xml_etree_process, async_tree_none_tg, unpickle_list, scimark_sor, fannkuch, logging_silent, async_generators, genshi_text, pylint, 2to3, sympy_expand, sympy_str, chaos, async_tree_cpu_io_mixed_tg, pickle_dict, comprehensions, pidigits, coroutines, json, json_loads, bench_thread_pool, asyncio_websockets, pycparser, float, raytrace, sphinx, regex_compile, sqlglot_optimize, deepcopy_memo, deepcopy, pyflate, tornado_http, thrift, unpack_sequence, pickle_list, regex_dna, xml_etree_parse, create_gc_cycles, go, json_dumps, sqlglot_transpile, async_tree_io

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 80.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x