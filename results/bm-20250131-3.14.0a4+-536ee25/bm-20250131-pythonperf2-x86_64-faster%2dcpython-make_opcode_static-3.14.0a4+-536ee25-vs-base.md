# Results vs. base

- fork: faster-cpython
- ref: make_opcode_static
- machine: linux-x86_64
- commit hash: 536ee25
- commit date: 2025-01-31
- overall geometric mean: 1.001x slower
- HPT reliability: 86.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 2.85 sec                                                                     | 2.84 sec: 1.01x faster                                                               |
| html5lib       | 66.3 ms                                                                      | 65.7 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 279 ms                                                                       | 276 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 389 ms                                                                       | 384 ms: 1.01x faster                                                                 |
| async_tree_memoization_tg  | 338 ms                                                                       | 335 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 507 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed    | 517 ms                                                                       | 520 ms: 1.01x slower                                                                 |
| async_tree_memoization     | 349 ms                                                                       | 351 ms: 1.01x slower                                                                 |
| async_generators           | 404 ms                                                                       | 411 ms: 1.02x slower                                                                 |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                         |

Benchmark hidden because not significant (4): coroutines, async_tree_io, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                                       | 254 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                      | 25.2 ms: 1.03x faster                                                                |
| regex_dna      | 238 ms                                                                       | 230 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.20 ms                                                                      | 3.13 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                                        | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|---------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle_pure_python  | 327 us                                                                       | 322 us: 1.02x faster                                                                 |
| xml_etree_iterparse | 97.2 ms                                                                      | 96.3 ms: 1.01x faster                                                                |
| xml_etree_parse     | 136 ms                                                                       | 138 ms: 1.02x slower                                                                 |
| xml_etree_generate  | 82.9 ms                                                                      | 84.7 ms: 1.02x slower                                                                |
| tomli_loads         | 1.99 sec                                                                     | 2.04 sec: 1.03x slower                                                               |
| xml_etree_process   | 57.9 ms                                                                      | 59.8 ms: 1.03x slower                                                                |
| Geometric mean      | (ref)                                                                        | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                                |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|-----------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 53.0 ms                                                                      | 51.8 ms: 1.02x faster                                                                |
| django_template | 34.9 ms                                                                      | 35.1 ms: 1.01x slower                                                                |
| mako            | 10.7 ms                                                                      | 10.9 ms: 1.01x slower                                                                |
| genshi_text     | 22.6 ms                                                                      | 23.0 ms: 1.02x slower                                                                |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:----------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| spectral_norm              | 84.5 ms                                                                      | 81.3 ms: 1.04x faster                                                                |
| regex_v8                   | 26.0 ms                                                                      | 25.2 ms: 1.03x faster                                                                |
| regex_dna                  | 238 ms                                                                       | 230 ms: 1.03x faster                                                                 |
| gc_traversal               | 6.55 ms                                                                      | 6.35 ms: 1.03x faster                                                                |
| pprint_pformat             | 1.60 sec                                                                     | 1.56 sec: 1.03x faster                                                               |
| generators                 | 29.0 ms                                                                      | 28.2 ms: 1.03x faster                                                                |
| pprint_safe_repr           | 783 ms                                                                       | 762 ms: 1.03x faster                                                                 |
| raytrace                   | 271 ms                                                                       | 264 ms: 1.03x faster                                                                 |
| genshi_xml                 | 53.0 ms                                                                      | 51.8 ms: 1.02x faster                                                                |
| regex_effbot               | 3.20 ms                                                                      | 3.13 ms: 1.02x faster                                                                |
| create_gc_cycles           | 2.82 ms                                                                      | 2.76 ms: 1.02x faster                                                                |
| deepcopy                   | 281 us                                                                       | 277 us: 1.02x faster                                                                 |
| json                       | 5.53 ms                                                                      | 5.45 ms: 1.02x faster                                                                |
| pickle_pure_python         | 327 us                                                                       | 322 us: 1.02x faster                                                                 |
| crypto_pyaes               | 73.6 ms                                                                      | 72.7 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 279 ms                                                                       | 276 ms: 1.01x faster                                                                 |
| typing_runtime_protocols   | 167 us                                                                       | 165 us: 1.01x faster                                                                 |
| deepcopy_reduce            | 2.90 us                                                                      | 2.86 us: 1.01x faster                                                                |
| asyncio_websockets         | 389 ms                                                                       | 384 ms: 1.01x faster                                                                 |
| fannkuch                   | 365 ms                                                                       | 362 ms: 1.01x faster                                                                 |
| xml_etree_iterparse        | 97.2 ms                                                                      | 96.3 ms: 1.01x faster                                                                |
| async_tree_memoization_tg  | 338 ms                                                                       | 335 ms: 1.01x faster                                                                 |
| bpe_tokeniser              | 4.55 sec                                                                     | 4.51 sec: 1.01x faster                                                               |
| html5lib                   | 66.3 ms                                                                      | 65.7 ms: 1.01x faster                                                                |
| deltablue                  | 3.27 ms                                                                      | 3.24 ms: 1.01x faster                                                                |
| deepcopy_memo              | 29.7 us                                                                      | 29.4 us: 1.01x faster                                                                |
| thrift                     | 860 us                                                                       | 853 us: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 510 ms                                                                       | 507 ms: 1.01x faster                                                                 |
| docutils                   | 2.85 sec                                                                     | 2.84 sec: 1.01x faster                                                               |
| sqlalchemy_imperative      | 17.7 ms                                                                      | 17.6 ms: 1.01x faster                                                                |
| logging_silent             | 96.8 ns                                                                      | 96.4 ns: 1.00x faster                                                                |
| pidigits                   | 254 ms                                                                       | 254 ms: 1.00x faster                                                                 |
| python_startup             | 16.0 ms                                                                      | 16.1 ms: 1.00x slower                                                                |
| shortest_path              | 442 ms                                                                       | 442 ms: 1.00x slower                                                                 |
| scimark_sparse_mat_mult    | 4.65 ms                                                                      | 4.67 ms: 1.00x slower                                                                |
| sqlalchemy_declarative     | 141 ms                                                                       | 141 ms: 1.00x slower                                                                 |
| async_tree_cpu_io_mixed    | 517 ms                                                                       | 520 ms: 1.01x slower                                                                 |
| many_optionals             | 1000 us                                                                      | 1.01 ms: 1.01x slower                                                                |
| meteor_contest             | 124 ms                                                                       | 124 ms: 1.01x slower                                                                 |
| async_tree_memoization     | 349 ms                                                                       | 351 ms: 1.01x slower                                                                 |
| comprehensions             | 16.6 us                                                                      | 16.7 us: 1.01x slower                                                                |
| go                         | 124 ms                                                                       | 124 ms: 1.01x slower                                                                 |
| sympy_integrate            | 22.8 ms                                                                      | 23.0 ms: 1.01x slower                                                                |
| scimark_lu                 | 94.6 ms                                                                      | 95.3 ms: 1.01x slower                                                                |
| django_template            | 34.9 ms                                                                      | 35.1 ms: 1.01x slower                                                                |
| mdp                        | 2.44 sec                                                                     | 2.46 sec: 1.01x slower                                                               |
| dulwich_log                | 66.3 ms                                                                      | 66.9 ms: 1.01x slower                                                                |
| sympy_sum                  | 149 ms                                                                       | 151 ms: 1.01x slower                                                                 |
| nqueens                    | 85.7 ms                                                                      | 86.6 ms: 1.01x slower                                                                |
| sqlglot_optimize           | 56.2 ms                                                                      | 56.8 ms: 1.01x slower                                                                |
| chaos                      | 59.0 ms                                                                      | 59.8 ms: 1.01x slower                                                                |
| richards                   | 45.5 ms                                                                      | 46.1 ms: 1.01x slower                                                                |
| mako                       | 10.7 ms                                                                      | 10.9 ms: 1.01x slower                                                                |
| xml_etree_parse            | 136 ms                                                                       | 138 ms: 1.02x slower                                                                 |
| pathlib                    | 15.6 ms                                                                      | 15.9 ms: 1.02x slower                                                                |
| sqlglot_normalize          | 113 ms                                                                       | 115 ms: 1.02x slower                                                                 |
| richards_super             | 51.5 ms                                                                      | 52.4 ms: 1.02x slower                                                                |
| async_generators           | 404 ms                                                                       | 411 ms: 1.02x slower                                                                 |
| genshi_text                | 22.6 ms                                                                      | 23.0 ms: 1.02x slower                                                                |
| xml_etree_generate         | 82.9 ms                                                                      | 84.7 ms: 1.02x slower                                                                |
| scimark_fft                | 302 ms                                                                       | 309 ms: 1.02x slower                                                                 |
| bench_thread_pool          | 907 us                                                                       | 928 us: 1.02x slower                                                                 |
| coverage                   | 76.7 ms                                                                      | 78.6 ms: 1.03x slower                                                                |
| telco                      | 7.86 ms                                                                      | 8.07 ms: 1.03x slower                                                                |
| tomli_loads                | 1.99 sec                                                                     | 2.04 sec: 1.03x slower                                                               |
| pyflate                    | 429 ms                                                                       | 442 ms: 1.03x slower                                                                 |
| xml_etree_process          | 57.9 ms                                                                      | 59.8 ms: 1.03x slower                                                                |
| scimark_monte_carlo        | 62.0 ms                                                                      | 64.5 ms: 1.04x slower                                                                |
| scimark_sor                | 108 ms                                                                       | 113 ms: 1.05x slower                                                                 |
| Geometric mean             | (ref)                                                                        | 1.00x slower                                                                         |

Benchmark hidden because not significant (27): sphinx, float, logging_format, logging_simple, coroutines, sympy_expand, k_core, connected_components, regex_compile, python_startup_no_site, pylint, subparsers, unpickle_pure_python, json_loads, async_tree_io, pycparser, 2to3, hexiom, sympy_str, sqlglot_transpile, sqlglot_parse, sqlite_synth, async_tree_io_tg, async_tree_none, json_dumps, nbody, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 86.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x