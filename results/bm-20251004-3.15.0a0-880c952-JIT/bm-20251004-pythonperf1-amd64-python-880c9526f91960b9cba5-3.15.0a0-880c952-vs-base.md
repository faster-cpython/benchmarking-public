# Results vs. base

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.017x faster
- HPT reliability: 81.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.58 sec                                                                                                             | 1.65 sec: 1.04x slower                                                                                                   |
| html5lib       | 37.0 ms                                                                                                              | 39.0 ms: 1.05x slower                                                                                                    |
| sphinx         | 620 ms                                                                                                               | 637 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 165 ms                                                                                                               | 167 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 333 ms                                                                                                               | 337 ms: 1.01x slower                                                                                                     |
| async_tree_memoization_tg  | 207 ms                                                                                                               | 211 ms: 1.02x slower                                                                                                     |
| async_tree_none            | 170 ms                                                                                                               | 174 ms: 1.02x slower                                                                                                     |
| async_tree_cpu_io_mixed    | 324 ms                                                                                                               | 336 ms: 1.03x slower                                                                                                     |
| asyncio_websockets         | 158 ms                                                                                                               | 165 ms: 1.05x slower                                                                                                     |
| coroutines                 | 13.9 ms                                                                                                              | 14.6 ms: 1.05x slower                                                                                                    |
| async_generators           | 228 ms                                                                                                               | 246 ms: 1.08x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.25 sec                                                                                                             | 1.44 sec: 1.15x slower                                                                                                   |
| asyncio_tcp                | 384 ms                                                                                                               | 492 ms: 1.28x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.05x slower                                                                                                             |

Benchmark hidden because not significant (3): async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.4 ms                                                                                                              | 54.9 ms: 1.17x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.6 ms                                                                                                              | 14.2 ms: 1.03x faster                                                                                                    |
| regex_compile  | 78.8 ms                                                                                                              | 78.0 ms: 1.01x faster                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 121 ms: 1.01x slower                                                                                                     |
| regex_effbot   | 1.48 ms                                                                                                              | 1.54 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                                                                               | 107 us: 1.25x faster                                                                                                     |
| tomli_loads          | 1.36 sec                                                                                                             | 1.11 sec: 1.23x faster                                                                                                   |
| xml_etree_generate   | 55.5 ms                                                                                                              | 49.9 ms: 1.11x faster                                                                                                    |
| xml_etree_process    | 38.6 ms                                                                                                              | 35.6 ms: 1.08x faster                                                                                                    |
| pickle_pure_python   | 206 us                                                                                                               | 200 us: 1.03x faster                                                                                                     |
| json_loads           | 14.2 us                                                                                                              | 14.1 us: 1.01x faster                                                                                                    |
| json_dumps           | 5.42 ms                                                                                                              | 5.47 ms: 1.01x slower                                                                                                    |
| unpickle             | 8.77 us                                                                                                              | 8.89 us: 1.01x slower                                                                                                    |
| xml_etree_parse      | 87.9 ms                                                                                                              | 90.5 ms: 1.03x slower                                                                                                    |
| xml_etree_iterparse  | 61.9 ms                                                                                                              | 63.9 ms: 1.03x slower                                                                                                    |
| pickle_dict          | 19.2 us                                                                                                              | 20.5 us: 1.07x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (3): unpickle_list, pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.0 ms                                                                                                              | 19.5 ms: 1.03x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.60 ms                                                                                                              | 5.43 ms: 1.22x faster                                                                                                    |
| genshi_text    | 15.1 ms                                                                                                              | 15.6 ms: 1.03x slower                                                                                                    |
| genshi_xml     | 33.9 ms                                                                                                              | 35.2 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json | results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 133 us                                                                                                               | 107 us: 1.25x faster                                                                                                     |
| fannkuch                   | 264 ms                                                                                                               | 213 ms: 1.24x faster                                                                                                     |
| tomli_loads                | 1.36 sec                                                                                                             | 1.11 sec: 1.23x faster                                                                                                   |
| scimark_fft                | 168 ms                                                                                                               | 137 ms: 1.22x faster                                                                                                     |
| mako                       | 6.60 ms                                                                                                              | 5.43 ms: 1.22x faster                                                                                                    |
| pprint_pformat             | 1.00 sec                                                                                                             | 839 ms: 1.19x faster                                                                                                     |
| pprint_safe_repr           | 491 ms                                                                                                               | 412 ms: 1.19x faster                                                                                                     |
| nbody                      | 64.4 ms                                                                                                              | 54.9 ms: 1.17x faster                                                                                                    |
| bpe_tokeniser              | 2.96 sec                                                                                                             | 2.53 sec: 1.17x faster                                                                                                   |
| pyflate                    | 280 ms                                                                                                               | 250 ms: 1.12x faster                                                                                                     |
| xml_etree_generate         | 55.5 ms                                                                                                              | 49.9 ms: 1.11x faster                                                                                                    |
| xml_etree_process          | 38.6 ms                                                                                                              | 35.6 ms: 1.08x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.39 ms                                                                                                              | 2.24 ms: 1.07x faster                                                                                                    |
| sqlglot_v2_parse           | 817 us                                                                                                               | 768 us: 1.06x faster                                                                                                     |
| crypto_pyaes               | 47.4 ms                                                                                                              | 45.0 ms: 1.05x faster                                                                                                    |
| gc_traversal               | 2.21 ms                                                                                                              | 2.12 ms: 1.04x faster                                                                                                    |
| unpack_sequence            | 36.8 ns                                                                                                              | 35.4 ns: 1.04x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                              | 973 us: 1.04x faster                                                                                                     |
| k_core                     | 1.68 sec                                                                                                             | 1.62 sec: 1.03x faster                                                                                                   |
| regex_v8                   | 14.6 ms                                                                                                              | 14.2 ms: 1.03x faster                                                                                                    |
| pickle_pure_python         | 206 us                                                                                                               | 200 us: 1.03x faster                                                                                                     |
| chaos                      | 40.9 ms                                                                                                              | 39.7 ms: 1.03x faster                                                                                                    |
| nqueens                    | 61.8 ms                                                                                                              | 60.0 ms: 1.03x faster                                                                                                    |
| logging_simple             | 6.02 us                                                                                                              | 5.85 us: 1.03x faster                                                                                                    |
| meteor_contest             | 74.0 ms                                                                                                              | 71.9 ms: 1.03x faster                                                                                                    |
| spectral_norm              | 65.9 ms                                                                                                              | 64.0 ms: 1.03x faster                                                                                                    |
| deepcopy_reduce            | 1.81 us                                                                                                              | 1.76 us: 1.03x faster                                                                                                    |
| raytrace                   | 180 ms                                                                                                               | 176 ms: 1.03x faster                                                                                                     |
| telco                      | 4.14 ms                                                                                                              | 4.04 ms: 1.02x faster                                                                                                    |
| scimark_sor                | 77.2 ms                                                                                                              | 76.1 ms: 1.02x faster                                                                                                    |
| json_loads                 | 14.2 us                                                                                                              | 14.1 us: 1.01x faster                                                                                                    |
| connected_components       | 327 ms                                                                                                               | 323 ms: 1.01x faster                                                                                                     |
| logging_format             | 6.44 us                                                                                                              | 6.37 us: 1.01x faster                                                                                                    |
| regex_compile              | 78.8 ms                                                                                                              | 78.0 ms: 1.01x faster                                                                                                    |
| sqlite_synth               | 1.56 us                                                                                                              | 1.54 us: 1.01x faster                                                                                                    |
| scimark_monte_carlo        | 39.5 ms                                                                                                              | 39.4 ms: 1.00x faster                                                                                                    |
| comprehensions             | 10.7 us                                                                                                              | 10.8 us: 1.01x slower                                                                                                    |
| json_dumps                 | 5.42 ms                                                                                                              | 5.47 ms: 1.01x slower                                                                                                    |
| richards                   | 26.8 ms                                                                                                              | 27.1 ms: 1.01x slower                                                                                                    |
| typing_runtime_protocols   | 102 us                                                                                                               | 103 us: 1.01x slower                                                                                                     |
| regex_dna                  | 119 ms                                                                                                               | 121 ms: 1.01x slower                                                                                                     |
| coverage                   | 50.6 ms                                                                                                              | 51.2 ms: 1.01x slower                                                                                                    |
| many_optionals             | 563 us                                                                                                               | 570 us: 1.01x slower                                                                                                     |
| json                       | 2.90 ms                                                                                                              | 2.93 ms: 1.01x slower                                                                                                    |
| async_tree_none_tg         | 165 ms                                                                                                               | 167 ms: 1.01x slower                                                                                                     |
| shortest_path              | 353 ms                                                                                                               | 357 ms: 1.01x slower                                                                                                     |
| unpickle                   | 8.77 us                                                                                                              | 8.89 us: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 333 ms                                                                                                               | 337 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 1.27 ms                                                                                                              | 1.29 ms: 1.02x slower                                                                                                    |
| async_tree_memoization_tg  | 207 ms                                                                                                               | 211 ms: 1.02x slower                                                                                                     |
| sympy_str                  | 166 ms                                                                                                               | 169 ms: 1.02x slower                                                                                                     |
| async_tree_none            | 170 ms                                                                                                               | 174 ms: 1.02x slower                                                                                                     |
| sqlglot_v2_normalize       | 69.5 ms                                                                                                              | 71.0 ms: 1.02x slower                                                                                                    |
| bench_mp_pool              | 88.1 ms                                                                                                              | 90.1 ms: 1.02x slower                                                                                                    |
| sympy_sum                  | 85.0 ms                                                                                                              | 87.0 ms: 1.02x slower                                                                                                    |
| generators                 | 19.1 ms                                                                                                              | 19.6 ms: 1.03x slower                                                                                                    |
| sphinx                     | 620 ms                                                                                                               | 637 ms: 1.03x slower                                                                                                     |
| python_startup_no_site     | 19.0 ms                                                                                                              | 19.5 ms: 1.03x slower                                                                                                    |
| pycparser                  | 696 ms                                                                                                               | 716 ms: 1.03x slower                                                                                                     |
| sqlglot_v2_optimize        | 33.7 ms                                                                                                              | 34.7 ms: 1.03x slower                                                                                                    |
| hexiom                     | 4.02 ms                                                                                                              | 4.14 ms: 1.03x slower                                                                                                    |
| xml_etree_parse            | 87.9 ms                                                                                                              | 90.5 ms: 1.03x slower                                                                                                    |
| thrift                     | 498 us                                                                                                               | 514 us: 1.03x slower                                                                                                     |
| sympy_expand               | 283 ms                                                                                                               | 291 ms: 1.03x slower                                                                                                     |
| mdp                        | 786 ms                                                                                                               | 811 ms: 1.03x slower                                                                                                     |
| xml_etree_iterparse        | 61.9 ms                                                                                                              | 63.9 ms: 1.03x slower                                                                                                    |
| dulwich_log                | 38.8 ms                                                                                                              | 40.1 ms: 1.03x slower                                                                                                    |
| genshi_text                | 15.1 ms                                                                                                              | 15.6 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 324 ms                                                                                                               | 336 ms: 1.03x slower                                                                                                     |
| deltablue                  | 2.18 ms                                                                                                              | 2.26 ms: 1.04x slower                                                                                                    |
| genshi_xml                 | 33.9 ms                                                                                                              | 35.2 ms: 1.04x slower                                                                                                    |
| regex_effbot               | 1.48 ms                                                                                                              | 1.54 ms: 1.04x slower                                                                                                    |
| sympy_integrate            | 12.1 ms                                                                                                              | 12.6 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.58 sec                                                                                                             | 1.65 sec: 1.04x slower                                                                                                   |
| scimark_lu                 | 56.0 ms                                                                                                              | 58.3 ms: 1.04x slower                                                                                                    |
| pylint                     | 190 ms                                                                                                               | 198 ms: 1.04x slower                                                                                                     |
| asyncio_websockets         | 158 ms                                                                                                               | 165 ms: 1.05x slower                                                                                                     |
| coroutines                 | 13.9 ms                                                                                                              | 14.6 ms: 1.05x slower                                                                                                    |
| html5lib                   | 37.0 ms                                                                                                              | 39.0 ms: 1.05x slower                                                                                                    |
| pickle_dict                | 19.2 us                                                                                                              | 20.5 us: 1.07x slower                                                                                                    |
| async_generators           | 228 ms                                                                                                               | 246 ms: 1.08x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.25 sec                                                                                                             | 1.44 sec: 1.15x slower                                                                                                   |
| asyncio_tcp                | 384 ms                                                                                                               | 492 ms: 1.28x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (19): async_tree_io, pathlib, deepcopy_memo, richards_super, django_template, float, async_tree_io_tg, logging_silent, unpickle_list, pidigits, go, deepcopy, pickle, pickle_list, 2to3, python_startup, async_tree_memoization, subparsers, bench_thread_pool

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 81.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown