# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-x86
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.025x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 268 ms: 1.07x slower                                                           |
| docutils       | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                         |
| sphinx         | 719 ms                                                          | 758 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 201 ms: 1.81x faster                                                           |
| async_tree_none            | 245 ms                                                          | 202 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 234 ms: 1.21x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 247 ms: 1.20x faster                                                           |
| async_tree_io              | 526 ms                                                          | 447 ms: 1.18x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 189 ms: 1.14x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 445 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 450 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                          |
| async_generators           | 270 ms                                                          | 299 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 53.8 ms: 1.01x faster                                                          |
| pidigits       | 201 ms                                                          | 205 ms: 1.02x slower                                                           |
| nbody          | 80.0 ms                                                         | 93.6 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                          |
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                          |
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                           |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                         |
| json_loads           | 21.6 us                                                         | 22.0 us: 1.02x slower                                                          |
| xml_etree_parse      | 107 ms                                                          | 114 ms: 1.06x slower                                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                          |
| unpickle_pure_python | 160 us                                                          | 176 us: 1.10x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| xml_etree_process    | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.43 ms: 1.16x slower                                                          |
| pickle_pure_python   | 231 us                                                          | 272 us: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.3 ms: 1.03x slower                                                          |
| python_startup_no_site | 19.7 ms                                                         | 22.2 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 53.7 ms: 1.07x slower                                                          |
| genshi_text     | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                          |
| django_template | 29.8 ms                                                         | 33.9 ms: 1.14x slower                                                          |
| mako            | 7.09 ms                                                         | 8.14 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 750 us: 13.31x faster                                                          |
| coverage                   | 324 ms                                                          | 58.8 ms: 5.51x faster                                                          |
| pathlib                    | 82.9 ms                                                         | 37.6 ms: 2.21x faster                                                          |
| asyncio_websockets         | 363 ms                                                          | 201 ms: 1.81x faster                                                           |
| mdp                        | 1.62 sec                                                        | 1.02 sec: 1.59x faster                                                         |
| deepcopy                   | 314 us                                                          | 243 us: 1.29x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 20.6 us: 1.24x faster                                                          |
| async_tree_none            | 245 ms                                                          | 202 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 234 ms: 1.21x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 247 ms: 1.20x faster                                                           |
| async_tree_io              | 526 ms                                                          | 447 ms: 1.18x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 14.6 ms: 1.15x faster                                                          |
| async_tree_none_tg         | 214 ms                                                          | 189 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.60 us: 1.12x faster                                                          |
| async_tree_io_tg           | 494 ms                                                          | 445 ms: 1.11x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 450 ms: 1.08x faster                                                           |
| go                         | 109 ms                                                          | 103 ms: 1.06x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.70 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 441 ms: 1.03x faster                                                           |
| float                      | 54.6 ms                                                         | 53.8 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 648 ms                                                          | 650 ms: 1.00x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.33 sec: 1.00x slower                                                         |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.74 sec: 1.02x slower                                                         |
| json_loads                 | 21.6 us                                                         | 22.0 us: 1.02x slower                                                          |
| sqlite_synth               | 1.95 us                                                         | 2.00 us: 1.02x slower                                                          |
| sympy_str                  | 212 ms                                                          | 217 ms: 1.02x slower                                                           |
| pidigits                   | 201 ms                                                          | 205 ms: 1.02x slower                                                           |
| regex_compile              | 101 ms                                                          | 103 ms: 1.02x slower                                                           |
| sympy_expand               | 373 ms                                                          | 384 ms: 1.03x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 109 ms: 1.03x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.3 ms: 1.03x slower                                                          |
| shortest_path              | 290 ms                                                          | 300 ms: 1.04x slower                                                           |
| pycparser                  | 872 ms                                                          | 906 ms: 1.04x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                         |
| sphinx                     | 719 ms                                                          | 758 ms: 1.05x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 51.4 ms: 1.05x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.45 sec: 1.06x slower                                                         |
| json                       | 4.27 ms                                                         | 4.51 ms: 1.06x slower                                                          |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 114 ms: 1.06x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.68 sec: 1.06x slower                                                         |
| genshi_xml                 | 50.1 ms                                                         | 53.7 ms: 1.07x slower                                                          |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                          |
| 2to3                       | 250 ms                                                          | 268 ms: 1.07x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 80.1 ms: 1.07x slower                                                          |
| create_gc_cycles           | 1.06 ms                                                         | 1.14 ms: 1.08x slower                                                          |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.6 ms: 1.08x slower                                                          |
| pyflate                    | 320 ms                                                          | 347 ms: 1.08x slower                                                           |
| chaos                      | 50.2 ms                                                         | 54.6 ms: 1.09x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 1.91 ms: 1.09x slower                                                          |
| deltablue                  | 2.33 ms                                                         | 2.55 ms: 1.09x slower                                                          |
| genshi_text                | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                          |
| fannkuch                   | 299 ms                                                          | 327 ms: 1.10x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 176 us: 1.10x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 62.7 ms: 1.10x slower                                                          |
| scimark_sor                | 85.9 ms                                                         | 94.7 ms: 1.10x slower                                                          |
| async_generators           | 270 ms                                                          | 299 ms: 1.11x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 68.3 ms: 1.11x slower                                                          |
| richards                   | 32.7 ms                                                         | 36.4 ms: 1.11x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 77.4 ms: 1.12x slower                                                          |
| typing_runtime_protocols   | 138 us                                                          | 154 us: 1.12x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.76 us: 1.12x slower                                                          |
| python_startup_no_site     | 19.7 ms                                                         | 22.2 ms: 1.13x slower                                                          |
| logging_simple             | 7.99 us                                                         | 9.03 us: 1.13x slower                                                          |
| xml_etree_process          | 44.2 ms                                                         | 50.0 ms: 1.13x slower                                                          |
| hexiom                     | 4.44 ms                                                         | 5.04 ms: 1.14x slower                                                          |
| richards_super             | 36.7 ms                                                         | 41.7 ms: 1.14x slower                                                          |
| django_template            | 29.8 ms                                                         | 33.9 ms: 1.14x slower                                                          |
| scimark_fft                | 205 ms                                                          | 234 ms: 1.14x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.14 ms: 1.15x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 104 ms: 1.15x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.43 ms: 1.16x slower                                                          |
| nqueens                    | 72.1 ms                                                         | 83.8 ms: 1.16x slower                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.31 ms: 1.17x slower                                                          |
| nbody                      | 80.0 ms                                                         | 93.6 ms: 1.17x slower                                                          |
| pickle_pure_python         | 231 us                                                          | 272 us: 1.18x slower                                                           |
| comprehensions             | 12.5 us                                                         | 14.8 us: 1.18x slower                                                          |
| scimark_lu                 | 60.2 ms                                                         | 72.1 ms: 1.20x slower                                                          |
| generators                 | 21.8 ms                                                         | 26.5 ms: 1.22x slower                                                          |
| raytrace                   | 201 ms                                                          | 246 ms: 1.22x slower                                                           |
| many_optionals             | 436 us                                                          | 560 us: 1.28x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.33 ms: 1.32x slower                                                          |
| subparsers                 | 14.8 ms                                                         | 23.3 ms: 1.58x slower                                                          |
| logging_silent             | 60.3 ns                                                         | 345 ns: 5.72x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (4): html5lib, pylint, sympy_integrate, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1_win32-x86-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown