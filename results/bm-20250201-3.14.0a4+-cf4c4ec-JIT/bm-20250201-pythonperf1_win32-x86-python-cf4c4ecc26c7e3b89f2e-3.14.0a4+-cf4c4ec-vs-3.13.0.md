# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-x86
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.067x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 272 ms: 1.09x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.96 sec: 1.10x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.6 ms: 1.02x slower                                                           |
| sphinx         | 719 ms                                                          | 798 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 477 ms: 1.10x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 260 ms: 1.09x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 474 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 207 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 493 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 470 ms: 1.03x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 53.2 ms: 1.03x faster                                                           |
| pidigits       | 201 ms                                                          | 202 ms: 1.00x slower                                                            |
| nbody          | 80.0 ms                                                         | 110 ms: 1.37x slower                                                            |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| regex_dna      | 114 ms                                                          | 125 ms: 1.10x slower                                                            |
| regex_compile  | 101 ms                                                          | 119 ms: 1.18x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| json_loads           | 21.6 us                                                         | 22.7 us: 1.05x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.86 sec: 1.09x slower                                                          |
| xml_etree_generate   | 61.4 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 54.6 ms: 1.24x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 301 us: 1.30x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.76 ms: 1.34x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 216 us: 1.35x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.8 ms: 1.02x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.1 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.64 ms: 1.08x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 56.8 ms: 1.13x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 26.3 ms: 1.22x slower                                                           |
| django_template | 29.8 ms                                                         | 38.1 ms: 1.28x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 806 us: 12.38x faster                                                           |
| coverage                   | 324 ms                                                          | 52.8 ms: 6.13x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 110 ms: 1.97x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 66.8 ms: 1.24x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| async_tree_io              | 526 ms                                                          | 477 ms: 1.10x faster                                                            |
| deepcopy                   | 314 us                                                          | 287 us: 1.09x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 260 ms: 1.09x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 474 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 235 ms: 1.04x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 207 ms: 1.04x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.90 us: 1.03x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 353 ms: 1.03x faster                                                            |
| float                      | 54.6 ms                                                         | 53.2 ms: 1.03x faster                                                           |
| pidigits                   | 201 ms                                                          | 202 ms: 1.00x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| python_startup             | 28.3 ms                                                         | 28.8 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 493 ms: 1.02x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 48.6 ms: 1.02x slower                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 3.00 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 470 ms: 1.03x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 72.0 ms: 1.04x slower                                                           |
| pylint                     | 227 ms                                                          | 236 ms: 1.04x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 94.9 ms: 1.05x slower                                                           |
| json_loads                 | 21.6 us                                                         | 22.7 us: 1.05x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.45 sec: 1.05x slower                                                          |
| coroutines                 | 16.2 ms                                                         | 17.2 ms: 1.06x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.85 ms: 1.06x slower                                                           |
| json                       | 4.27 ms                                                         | 4.57 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.08 ms: 1.07x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.64 ms: 1.08x slower                                                           |
| 2to3                       | 250 ms                                                          | 272 ms: 1.09x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.86 sec: 1.09x slower                                                          |
| dulwich_log                | 48.8 ms                                                         | 53.1 ms: 1.09x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.51 us: 1.09x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.73 us: 1.09x slower                                                           |
| regex_dna                  | 114 ms                                                          | 125 ms: 1.10x slower                                                            |
| sympy_expand               | 373 ms                                                          | 411 ms: 1.10x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.96 sec: 1.10x slower                                                          |
| pycparser                  | 872 ms                                                          | 962 ms: 1.10x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 117 ms: 1.10x slower                                                            |
| sphinx                     | 719 ms                                                          | 798 ms: 1.11x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.16 ms: 1.11x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.87 sec: 1.12x slower                                                          |
| sympy_str                  | 212 ms                                                          | 238 ms: 1.13x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 22.1 ms: 1.13x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 56.8 ms: 1.13x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.91 ms: 1.14x slower                                                           |
| connected_components       | 267 ms                                                          | 303 ms: 1.14x slower                                                            |
| shortest_path              | 290 ms                                                          | 336 ms: 1.16x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.54 sec: 1.16x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 752 ms: 1.16x slower                                                            |
| go                         | 109 ms                                                          | 127 ms: 1.17x slower                                                            |
| regex_compile              | 101 ms                                                          | 119 ms: 1.18x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 17.8 ms: 1.19x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.47 ms: 1.19x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.93 sec: 1.19x slower                                                          |
| scimark_fft                | 205 ms                                                          | 244 ms: 1.19x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 103 ms: 1.20x slower                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.20 ms: 1.20x slower                                                           |
| pyflate                    | 320 ms                                                          | 383 ms: 1.20x slower                                                            |
| async_generators           | 270 ms                                                          | 326 ms: 1.21x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 166 us: 1.21x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 74.3 ms: 1.21x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 73.3 ms: 1.22x slower                                                           |
| fannkuch                   | 299 ms                                                          | 364 ms: 1.22x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 26.3 ms: 1.22x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 54.6 ms: 1.24x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 92.6 ms: 1.24x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 51.9 ms: 1.25x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 71.7 ms: 1.26x slower                                                           |
| django_template            | 29.8 ms                                                         | 38.1 ms: 1.28x slower                                                           |
| richards_super             | 36.7 ms                                                         | 47.2 ms: 1.29x slower                                                           |
| richards                   | 32.7 ms                                                         | 42.3 ms: 1.29x slower                                                           |
| many_optionals             | 436 us                                                          | 566 us: 1.30x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 301 us: 1.30x slower                                                            |
| chaos                      | 50.2 ms                                                         | 66.7 ms: 1.33x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.11 ms: 1.33x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.76 ms: 1.34x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 64.3 ms: 1.35x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 216 us: 1.35x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 81.6 ns: 1.35x slower                                                           |
| nbody                      | 80.0 ms                                                         | 110 ms: 1.37x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 102 ms: 1.42x slower                                                            |
| comprehensions             | 12.5 us                                                         | 18.6 us: 1.49x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 22.3 ms: 1.51x slower                                                           |
| raytrace                   | 201 ms                                                          | 318 ms: 1.58x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.37 ms: 1.66x slower                                                           |
| generators                 | 21.8 ms                                                         | 37.5 ms: 1.72x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, create_gc_cycles, deepcopy_memo
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-pythonperf1_win32-x86-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown