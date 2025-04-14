# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.008x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.78 sec                                                        | 1.83 sec: 1.03x slower                                                          |
| html5lib       | 47.5 ms                                                         | 46.5 ms: 1.02x faster                                                           |
| sphinx         | 719 ms                                                          | 737 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 461 ms: 1.14x faster                                                            |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 250 ms: 1.13x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 264 ms: 1.12x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 451 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 461 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 435 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 369 ms: 1.02x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| async_generators           | 270 ms                                                          | 302 ms: 1.12x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 201 ms: 1.00x slower                                                            |
| float          | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                           |
| nbody          | 80.0 ms                                                         | 89.4 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                            |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.69 sec: 1.01x faster                                                          |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.02x slower                                                            |
| json_loads           | 21.6 us                                                         | 22.4 us: 1.03x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.9 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 68.0 ms: 1.11x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 179 us: 1.12x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 49.6 ms: 1.12x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 274 us: 1.18x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.08 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.8 ms: 1.05x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 47.2 ms: 1.06x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 21.8 ms: 1.01x slower                                                           |
| mako            | 7.09 ms                                                         | 7.88 ms: 1.11x slower                                                           |
| django_template | 29.8 ms                                                         | 33.7 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 749 us: 13.33x faster                                                           |
| coverage                   | 324 ms                                                          | 52.5 ms: 6.17x faster                                                           |
| deepcopy                   | 314 us                                                          | 243 us: 1.29x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.8 us: 1.17x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.55 us: 1.14x faster                                                           |
| async_tree_io              | 526 ms                                                          | 461 ms: 1.14x faster                                                            |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 250 ms: 1.13x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 264 ms: 1.12x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 451 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 461 ms: 1.07x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.7 ms: 1.07x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 47.2 ms: 1.06x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.8 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 435 ms: 1.05x faster                                                            |
| go                         | 109 ms                                                          | 105 ms: 1.04x faster                                                            |
| pylint                     | 227 ms                                                          | 220 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.37 sec: 1.03x faster                                                          |
| html5lib                   | 47.5 ms                                                         | 46.5 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.69 sec: 1.01x faster                                                          |
| create_gc_cycles           | 1.06 ms                                                         | 1.05 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 641 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                          | 201 ms: 1.00x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.34 sec: 1.01x slower                                                          |
| genshi_text                | 21.5 ms                                                         | 21.8 ms: 1.01x slower                                                           |
| asyncio_websockets         | 363 ms                                                          | 369 ms: 1.02x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.02x slower                                                            |
| logging_format             | 8.72 us                                                         | 8.87 us: 1.02x slower                                                           |
| shortest_path              | 290 ms                                                          | 295 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                            |
| sympy_expand               | 373 ms                                                          | 381 ms: 1.02x slower                                                            |
| sympy_str                  | 212 ms                                                          | 216 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 108 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 306 ms: 1.02x slower                                                            |
| sphinx                     | 719 ms                                                          | 737 ms: 1.03x slower                                                            |
| pathlib                    | 82.9 ms                                                         | 85.1 ms: 1.03x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 93.0 ms: 1.03x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.15 ms: 1.03x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.83 sec: 1.03x slower                                                          |
| sqlglot_normalize          | 216 ms                                                          | 224 ms: 1.03x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.25 us: 1.03x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.03x slower                                                           |
| json_loads                 | 21.6 us                                                         | 22.4 us: 1.03x slower                                                           |
| float                      | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                           |
| regex_compile              | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 43.1 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 143 us: 1.04x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 72.5 ms: 1.05x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 59.5 ms: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.97 ms: 1.05x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 51.1 ms: 1.05x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| sympy_integrate            | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.9 ms: 1.07x slower                                                           |
| json                       | 4.27 ms                                                         | 4.58 ms: 1.07x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 80.1 ms: 1.07x slower                                                           |
| pyflate                    | 320 ms                                                          | 344 ms: 1.07x slower                                                            |
| chaos                      | 50.2 ms                                                         | 54.2 ms: 1.08x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.6 us: 1.09x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.34 ms: 1.09x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.10 ms: 1.10x slower                                                           |
| scimark_fft                | 205 ms                                                          | 226 ms: 1.11x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 68.0 ms: 1.11x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.88 ms: 1.11x slower                                                           |
| nbody                      | 80.0 ms                                                         | 89.4 ms: 1.12x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 179 us: 1.12x slower                                                            |
| async_generators           | 270 ms                                                          | 302 ms: 1.12x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 49.6 ms: 1.12x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 81.3 ms: 1.13x slower                                                           |
| django_template            | 29.8 ms                                                         | 33.7 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 71.2 ms: 1.18x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 274 us: 1.18x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 56.8 ms: 1.19x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.31 ms: 1.20x slower                                                           |
| many_optionals             | 436 us                                                          | 523 us: 1.20x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 105 ms: 1.22x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.84 ms: 1.22x slower                                                           |
| richards_super             | 36.7 ms                                                         | 44.9 ms: 1.22x slower                                                           |
| richards                   | 32.7 ms                                                         | 40.1 ms: 1.23x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.08 ms: 1.24x slower                                                           |
| generators                 | 21.8 ms                                                         | 27.1 ms: 1.24x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 78.7 ns: 1.30x slower                                                           |
| raytrace                   | 201 ms                                                          | 267 ms: 1.32x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 20.8 ms: 1.41x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): k_core, connected_components, pycparser, 2to3, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.74% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown