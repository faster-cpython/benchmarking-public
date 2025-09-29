# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.163x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.78 sec: 1.57x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.1 ms: 1.18x faster                                                            |
| sphinx         | 719 ms                                                          | 646 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 139 ms: 2.60x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 321 ms: 1.54x faster                                                             |
| async_tree_io              | 526 ms                                                          | 341 ms: 1.54x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 185 ms: 1.53x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 143 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| float          | 54.6 ms                                                         | 45.0 ms: 1.21x faster                                                            |
| nbody          | 80.0 ms                                                         | 76.9 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.0 ms: 1.29x faster                                                            |
| regex_compile  | 101 ms                                                          | 88.2 ms: 1.15x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| regex_dna      | 114 ms                                                          | 113 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.03 ms: 1.21x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 89.3 ms: 1.20x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 149 us: 1.08x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 59.1 ms: 1.06x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 223 us: 1.04x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 43.5 ms: 1.02x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.19 sec: 1.28x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 38.5 ms: 1.30x faster                                                            |
| django_template | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 18.9 ms: 1.14x faster                                                            |
| mako            | 7.09 ms                                                         | 9.65 ms: 1.36x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 550 us: 18.16x faster                                                            |
| coverage                   | 324 ms                                                          | 68.5 ms: 4.73x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.7 ms: 2.89x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 139 ms: 2.60x faster                                                             |
| deepcopy                   | 314 us                                                          | 184 us: 1.71x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 321 ms: 1.54x faster                                                             |
| async_tree_io              | 526 ms                                                          | 341 ms: 1.54x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 185 ms: 1.53x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.07 sec: 1.52x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 143 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.50x faster                                                             |
| pidigits                   | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.34 us: 1.46x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.78 ms: 1.46x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.01 us: 1.45x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.22 ms: 1.43x faster                                                            |
| json                       | 4.27 ms                                                         | 3.04 ms: 1.40x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.7 us: 1.36x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 38.5 ms: 1.30x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.0 ms: 1.29x faster                                                            |
| pycparser                  | 872 ms                                                          | 680 ms: 1.28x faster                                                             |
| logging_format             | 8.72 us                                                         | 7.08 us: 1.23x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 527 ms: 1.23x faster                                                             |
| sympy_expand               | 373 ms                                                          | 305 ms: 1.22x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.55 us: 1.22x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 74.5 ms: 1.22x faster                                                            |
| float                      | 54.6 ms                                                         | 45.0 ms: 1.21x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.03 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.3 ms: 1.20x faster                                                            |
| go                         | 109 ms                                                          | 90.7 ms: 1.20x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.1 ms: 1.18x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.3 ms: 1.18x faster                                                            |
| sympy_str                  | 212 ms                                                          | 180 ms: 1.18x faster                                                             |
| django_template            | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                            |
| 2to3                       | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| regex_compile              | 101 ms                                                          | 88.2 ms: 1.15x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 92.5 ms: 1.14x faster                                                            |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 18.9 ms: 1.14x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.13x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 123 us: 1.12x faster                                                             |
| sphinx                     | 719 ms                                                          | 646 ms: 1.11x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 13.5 ms: 1.11x faster                                                            |
| chaos                      | 50.2 ms                                                         | 45.5 ms: 1.10x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.4 us: 1.09x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 149 us: 1.08x faster                                                             |
| scimark_fft                | 205 ms                                                          | 191 ms: 1.07x faster                                                             |
| pyflate                    | 320 ms                                                          | 300 ms: 1.07x faster                                                             |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 59.1 ms: 1.06x faster                                                            |
| richards                   | 32.7 ms                                                         | 31.3 ms: 1.04x faster                                                            |
| nbody                      | 80.0 ms                                                         | 76.9 ms: 1.04x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 223 us: 1.04x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 69.7 ms: 1.03x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.03 ms: 1.03x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 43.5 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 56.3 ms: 1.01x faster                                                            |
| regex_dna                  | 114 ms                                                          | 113 ms: 1.00x faster                                                             |
| generators                 | 21.8 ms                                                         | 22.0 ms: 1.01x slower                                                            |
| raytrace                   | 201 ms                                                          | 203 ms: 1.01x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.49 ms: 1.01x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.0 ns: 1.01x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.37 ms: 1.01x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 48.6 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 306 ms: 1.02x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 63.2 ms: 1.05x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.00 ms: 1.06x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 83.4 ms: 1.12x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.51 sec: 1.14x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.19 sec: 1.28x slower                                                           |
| mako                       | 7.09 ms                                                         | 9.65 ms: 1.36x slower                                                            |
| many_optionals             | 436 us                                                          | 633 us: 1.45x slower                                                             |
| docutils                   | 1.78 sec                                                        | 2.78 sec: 1.57x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.43 sec: 1.57x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.60 sec: 1.89x slower                                                           |
| shortest_path              | 290 ms                                                          | 630 ms: 2.17x slower                                                             |
| connected_components       | 267 ms                                                          | 586 ms: 2.20x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 35.0 ms: 2.37x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                     |

Benchmark hidden because not significant (4): scimark_sor, spectral_norm, richards_super, xml_etree_generate
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.163x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown