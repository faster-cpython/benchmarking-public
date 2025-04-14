# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: linux-aarch64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.003x faster
- HPT reliability: 71.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                             |

Benchmark hidden because not significant (5): 2to3, chameleon, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| async_generators | 500 ms                                                   | 464 ms: 1.08x faster                                     |
| Geometric mean   | (ref)                                                    | 1.01x faster                                             |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| nbody          | 118 ms                                                   | 112 ms: 1.06x faster                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.36 ms: 1.17x faster                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                             |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                     |
| xml_etree_parse     | 203 ms                                                   | 194 ms: 1.04x faster                                     |
| Geometric mean      | (ref)                                                    | 1.02x faster                                             |

Benchmark hidden because not significant (7): json_dumps, xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python, pickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 63.0 ms: 1.02x slower                                    |
| django_template | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                    |
| Geometric mean  | (ref)                                                    | 1.03x slower                                             |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-arminc-aarch64-python-v3.13.2-3.13.2-4f8bb39 |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------:|
| regex_effbot        | 5.10 ms                                                  | 4.36 ms: 1.17x faster                                    |
| async_generators    | 500 ms                                                   | 464 ms: 1.08x faster                                     |
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                     |
| nbody               | 118 ms                                                   | 112 ms: 1.06x faster                                     |
| xml_etree_parse     | 203 ms                                                   | 194 ms: 1.04x faster                                     |
| genshi_xml          | 61.6 ms                                                  | 63.0 ms: 1.02x slower                                    |
| docutils            | 2.96 sec                                                 | 3.04 sec: 1.03x slower                                   |
| richards_super      | 60.8 ms                                                  | 62.8 ms: 1.03x slower                                    |
| pyflate             | 582 ms                                                   | 604 ms: 1.04x slower                                     |
| django_template     | 39.4 ms                                                  | 41.5 ms: 1.05x slower                                    |
| create_gc_cycles    | 3.39 ms                                                  | 3.59 ms: 1.06x slower                                    |
| Geometric mean      | (ref)                                                    | 1.00x faster                                             |

Benchmark hidden because not significant (89): generators, tornado_http, json_dumps, bench_thread_pool, coverage, pathlib, sqlglot_transpile, xml_etree_generate, json, sympy_sum, regex_v8, json_loads, async_tree_none_tg, bench_mp_pool, scimark_lu, nqueens, chaos, k_core, sqlglot_optimize, async_tree_io_tg, xml_etree_process, sqlalchemy_imperative, gunicorn, chameleon, unpickle_pure_python, shortest_path, pycparser, sqlalchemy_declarative, subparsers, regex_compile, raytrace, async_tree_memoization_tg, async_tree_cpu_io_mixed, deepcopy_memo, mako, thrift, pickle_pure_python, scimark_fft, asyncio_websockets, fannkuch, connected_components, deltablue, python_startup, sphinx, coroutines, gc_traversal, sympy_str, bpe_tokeniser, 2to3, go, tomli_loads, deepcopy, logging_format, async_tree_io, html5lib, sympy_expand, scimark_sor, async_tree_none, many_optionals, python_startup_no_site, mdp, djangocms, scimark_sparse_mat_mult, sqlglot_parse, spectral_norm, pprint_pformat, pidigits, hexiom, richards, async_tree_memoization, pprint_safe_repr, float, async_tree_cpu_io_mixed_tg, sqlglot_normalize, comprehensions, regex_dna, sympy_integrate, meteor_contest, crypto_pyaes, sqlite_synth, deepcopy_reduce, gevent_hub, telco, logging_silent, genshi_text, pylint, typing_runtime_protocols, logging_simple, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 71.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x