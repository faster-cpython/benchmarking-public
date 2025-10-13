# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: windows-amd64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| sphinx         | 719 ms                                                          | 626 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.22x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 171 ms: 1.43x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 387 ms: 1.28x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 239 ms: 1.13x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 55.9 ms: 1.43x faster                                                            |
| pidigits       | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 43.8 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 77.7 ms: 1.30x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.09 sec: 1.58x faster                                                           |
| json_loads           | 21.6 us                                                         | 13.9 us: 1.55x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.53x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.42 ms: 1.35x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 49.0 ms: 1.25x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.3 ms: 1.24x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 202 us: 1.14x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.1 ms: 1.13x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.9 ms: 1.36x faster                                                            |
| mako            | 7.09 ms                                                         | 5.27 ms: 1.35x faster                                                            |
| django_template | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.34x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 511 us: 19.52x faster                                                            |
| coverage                   | 324 ms                                                          | 49.4 ms: 6.55x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.2 ms: 2.84x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 163 ms: 2.22x faster                                                             |
| mdp                        | 1.62 sec                                                        | 786 ms: 2.07x faster                                                             |
| deepcopy                   | 314 us                                                          | 159 us: 1.98x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 13.8 us: 1.84x faster                                                            |
| telco                      | 6.96 ms                                                         | 3.86 ms: 1.80x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.75 us: 1.66x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 43.6 ms: 1.59x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.09 sec: 1.58x faster                                                           |
| json_loads                 | 21.6 us                                                         | 13.9 us: 1.55x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 857 ms: 1.55x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.53x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 426 ms: 1.52x faster                                                             |
| scimark_fft                | 205 ms                                                          | 136 ms: 1.50x faster                                                             |
| json                       | 4.27 ms                                                         | 2.92 ms: 1.46x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 331 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 171 ms: 1.43x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                            |
| nbody                      | 80.0 ms                                                         | 55.9 ms: 1.43x faster                                                            |
| fannkuch                   | 299 ms                                                          | 211 ms: 1.42x faster                                                             |
| go                         | 109 ms                                                          | 76.9 ms: 1.41x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.82 us: 1.37x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 333 ms: 1.37x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.37 us: 1.37x faster                                                            |
| pidigits                   | 201 ms                                                          | 147 ms: 1.37x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.9 ms: 1.36x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.56 sec: 1.35x faster                                                           |
| json_dumps                 | 7.30 ms                                                         | 5.42 ms: 1.35x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.27 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 103 us: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| regex_compile              | 101 ms                                                          | 77.7 ms: 1.30x faster                                                            |
| sympy_expand               | 373 ms                                                          | 288 ms: 1.30x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 44.1 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.20 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| pycparser                  | 872 ms                                                          | 682 ms: 1.28x faster                                                             |
| sympy_str                  | 212 ms                                                          | 166 ms: 1.28x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.53 us: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 387 ms: 1.28x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.3 ms: 1.27x faster                                                            |
| pyflate                    | 320 ms                                                          | 252 ms: 1.27x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 38.9 ms: 1.25x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 49.0 ms: 1.25x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 84.3 ms: 1.25x faster                                                            |
| float                      | 54.6 ms                                                         | 43.8 ms: 1.25x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.3 ms: 1.24x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.6 ms: 1.24x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 829 us: 1.21x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.20x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.3 ms: 1.20x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 60.3 ms: 1.20x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.7 ms: 1.19x faster                                                            |
| pylint                     | 227 ms                                                          | 193 ms: 1.17x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.17x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| raytrace                   | 201 ms                                                          | 174 ms: 1.15x faster                                                             |
| 2to3                       | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| sphinx                     | 719 ms                                                          | 626 ms: 1.15x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 202 us: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 239 ms: 1.13x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.1 ms: 1.13x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.1 ns: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| scimark_sor                | 85.9 ms                                                         | 79.1 ms: 1.09x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.11 ms: 1.08x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.21 ms: 1.06x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.1 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.3 ms: 1.03x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 88.8 ms: 1.02x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.55 sec: 1.13x slower                                                           |
| connected_components       | 267 ms                                                          | 316 ms: 1.18x slower                                                             |
| shortest_path              | 290 ms                                                          | 347 ms: 1.20x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                            |
| many_optionals             | 436 us                                                          | 571 us: 1.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.8 ms: 2.09x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (2): regex_dna, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf1_win32-amd64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown