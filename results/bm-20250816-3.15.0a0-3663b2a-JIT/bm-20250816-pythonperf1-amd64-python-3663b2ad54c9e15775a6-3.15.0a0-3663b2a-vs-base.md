# Results vs. base

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.026x faster
- HPT reliability: 86.53%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                                                                               | 217 ms: 1.01x slower                                                                                                     |
| docutils       | 1.60 sec                                                                                                             | 1.62 sec: 1.01x slower                                                                                                   |
| html5lib       | 37.6 ms                                                                                                              | 38.4 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io             | 388 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| async_tree_memoization_tg | 207 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| asyncio_websockets        | 157 ms                                                                                                               | 163 ms: 1.04x slower                                                                                                     |
| async_generators          | 227 ms                                                                                                               | 245 ms: 1.08x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.25 sec                                                                                                             | 1.39 sec: 1.12x slower                                                                                                   |
| asyncio_tcp               | 380 ms                                                                                                               | 497 ms: 1.31x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.6 ms                                                                                                              | 57.5 ms: 1.11x faster                                                                                                    |
| pidigits       | 145 ms                                                                                                               | 143 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                                                               | 118 ms: 1.06x faster                                                                                                     |
| regex_v8       | 13.9 ms                                                                                                              | 13.7 ms: 1.02x faster                                                                                                    |
| regex_compile  | 78.8 ms                                                                                                              | 78.0 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.58 ms                                                                                                              | 1.60 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 132 us                                                                                                               | 104 us: 1.27x faster                                                                                                     |
| tomli_loads          | 1.38 sec                                                                                                             | 1.12 sec: 1.24x faster                                                                                                   |
| xml_etree_generate   | 56.3 ms                                                                                                              | 50.0 ms: 1.13x faster                                                                                                    |
| xml_etree_process    | 39.2 ms                                                                                                              | 35.3 ms: 1.11x faster                                                                                                    |
| pickle               | 8.25 us                                                                                                              | 7.60 us: 1.09x faster                                                                                                    |
| pickle_pure_python   | 212 us                                                                                                               | 200 us: 1.06x faster                                                                                                     |
| pickle_list          | 3.38 us                                                                                                              | 3.23 us: 1.05x faster                                                                                                    |
| xml_etree_iterparse  | 63.5 ms                                                                                                              | 61.8 ms: 1.03x faster                                                                                                    |
| pickle_dict          | 19.7 us                                                                                                              | 19.2 us: 1.03x faster                                                                                                    |
| unpickle_list        | 2.82 us                                                                                                              | 2.76 us: 1.02x faster                                                                                                    |
| xml_etree_parse      | 87.0 ms                                                                                                              | 85.3 ms: 1.02x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (3): json_loads, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.64 ms                                                                                                              | 5.28 ms: 1.26x faster                                                                                                    |
| genshi_text    | 15.3 ms                                                                                                              | 15.5 ms: 1.01x slower                                                                                                    |
| genshi_xml     | 33.4 ms                                                                                                              | 34.6 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json | results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python      | 132 us                                                                                                               | 104 us: 1.27x faster                                                                                                     |
| mako                      | 6.64 ms                                                                                                              | 5.28 ms: 1.26x faster                                                                                                    |
| fannkuch                  | 263 ms                                                                                                               | 211 ms: 1.25x faster                                                                                                     |
| unpack_sequence           | 40.5 ns                                                                                                              | 32.7 ns: 1.24x faster                                                                                                    |
| tomli_loads               | 1.38 sec                                                                                                             | 1.12 sec: 1.24x faster                                                                                                   |
| scimark_fft               | 177 ms                                                                                                               | 149 ms: 1.19x faster                                                                                                     |
| bpe_tokeniser             | 2.93 sec                                                                                                             | 2.54 sec: 1.15x faster                                                                                                   |
| scimark_sparse_mat_mult   | 2.53 ms                                                                                                              | 2.24 ms: 1.13x faster                                                                                                    |
| xml_etree_generate        | 56.3 ms                                                                                                              | 50.0 ms: 1.13x faster                                                                                                    |
| pprint_pformat            | 994 ms                                                                                                               | 884 ms: 1.12x faster                                                                                                     |
| pprint_safe_repr          | 489 ms                                                                                                               | 435 ms: 1.12x faster                                                                                                     |
| xml_etree_process         | 39.2 ms                                                                                                              | 35.3 ms: 1.11x faster                                                                                                    |
| telco                     | 4.38 ms                                                                                                              | 3.96 ms: 1.11x faster                                                                                                    |
| nbody                     | 63.6 ms                                                                                                              | 57.5 ms: 1.11x faster                                                                                                    |
| pyflate                   | 293 ms                                                                                                               | 265 ms: 1.10x faster                                                                                                     |
| pickle                    | 8.25 us                                                                                                              | 7.60 us: 1.09x faster                                                                                                    |
| crypto_pyaes              | 47.7 ms                                                                                                              | 44.9 ms: 1.06x faster                                                                                                    |
| pickle_pure_python        | 212 us                                                                                                               | 200 us: 1.06x faster                                                                                                     |
| regex_dna                 | 124 ms                                                                                                               | 118 ms: 1.06x faster                                                                                                     |
| sqlglot_v2_parse          | 810 us                                                                                                               | 766 us: 1.06x faster                                                                                                     |
| coverage                  | 51.0 ms                                                                                                              | 48.4 ms: 1.05x faster                                                                                                    |
| pickle_list               | 3.38 us                                                                                                              | 3.23 us: 1.05x faster                                                                                                    |
| k_core                    | 1.67 sec                                                                                                             | 1.60 sec: 1.05x faster                                                                                                   |
| pycparser                 | 723 ms                                                                                                               | 691 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_transpile      | 1.01 ms                                                                                                              | 967 us: 1.04x faster                                                                                                     |
| deepcopy_memo             | 18.7 us                                                                                                              | 18.0 us: 1.04x faster                                                                                                    |
| connected_components      | 326 ms                                                                                                               | 313 ms: 1.04x faster                                                                                                     |
| comprehensions            | 10.9 us                                                                                                              | 10.5 us: 1.03x faster                                                                                                    |
| typing_runtime_protocols  | 106 us                                                                                                               | 103 us: 1.03x faster                                                                                                     |
| xml_etree_iterparse       | 63.5 ms                                                                                                              | 61.8 ms: 1.03x faster                                                                                                    |
| pickle_dict               | 19.7 us                                                                                                              | 19.2 us: 1.03x faster                                                                                                    |
| meteor_contest            | 70.8 ms                                                                                                              | 69.1 ms: 1.02x faster                                                                                                    |
| spectral_norm             | 64.5 ms                                                                                                              | 63.1 ms: 1.02x faster                                                                                                    |
| unpickle_list             | 2.82 us                                                                                                              | 2.76 us: 1.02x faster                                                                                                    |
| xml_etree_parse           | 87.0 ms                                                                                                              | 85.3 ms: 1.02x faster                                                                                                    |
| sqlite_synth              | 1.55 us                                                                                                              | 1.52 us: 1.02x faster                                                                                                    |
| json                      | 2.95 ms                                                                                                              | 2.90 ms: 1.02x faster                                                                                                    |
| shortest_path             | 355 ms                                                                                                               | 349 ms: 1.02x faster                                                                                                     |
| async_tree_io             | 388 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| regex_v8                  | 13.9 ms                                                                                                              | 13.7 ms: 1.02x faster                                                                                                    |
| pidigits                  | 145 ms                                                                                                               | 143 ms: 1.01x faster                                                                                                     |
| regex_compile             | 78.8 ms                                                                                                              | 78.0 ms: 1.01x faster                                                                                                    |
| deepcopy                  | 170 us                                                                                                               | 169 us: 1.01x faster                                                                                                     |
| deepcopy_reduce           | 1.83 us                                                                                                              | 1.82 us: 1.01x faster                                                                                                    |
| chaos                     | 39.5 ms                                                                                                              | 39.7 ms: 1.00x slower                                                                                                    |
| 2to3                      | 215 ms                                                                                                               | 217 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_optimize       | 33.8 ms                                                                                                              | 34.1 ms: 1.01x slower                                                                                                    |
| logging_format            | 6.37 us                                                                                                              | 6.45 us: 1.01x slower                                                                                                    |
| genshi_text               | 15.3 ms                                                                                                              | 15.5 ms: 1.01x slower                                                                                                    |
| regex_effbot              | 1.58 ms                                                                                                              | 1.60 ms: 1.01x slower                                                                                                    |
| docutils                  | 1.60 sec                                                                                                             | 1.62 sec: 1.01x slower                                                                                                   |
| many_optionals            | 551 us                                                                                                               | 559 us: 1.02x slower                                                                                                     |
| async_tree_memoization_tg | 207 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| sympy_expand              | 283 ms                                                                                                               | 288 ms: 1.02x slower                                                                                                     |
| mdp                       | 794 ms                                                                                                               | 809 ms: 1.02x slower                                                                                                     |
| go                        | 75.3 ms                                                                                                              | 76.7 ms: 1.02x slower                                                                                                    |
| scimark_monte_carlo       | 39.5 ms                                                                                                              | 40.3 ms: 1.02x slower                                                                                                    |
| html5lib                  | 37.6 ms                                                                                                              | 38.4 ms: 1.02x slower                                                                                                    |
| sympy_integrate           | 12.2 ms                                                                                                              | 12.4 ms: 1.02x slower                                                                                                    |
| sympy_str                 | 166 ms                                                                                                               | 170 ms: 1.02x slower                                                                                                     |
| generators                | 18.9 ms                                                                                                              | 19.4 ms: 1.02x slower                                                                                                    |
| raytrace                  | 174 ms                                                                                                               | 179 ms: 1.03x slower                                                                                                     |
| deltablue                 | 2.18 ms                                                                                                              | 2.25 ms: 1.03x slower                                                                                                    |
| scimark_sor               | 77.0 ms                                                                                                              | 79.6 ms: 1.03x slower                                                                                                    |
| scimark_lu                | 55.8 ms                                                                                                              | 57.7 ms: 1.03x slower                                                                                                    |
| logging_simple            | 5.93 us                                                                                                              | 6.15 us: 1.04x slower                                                                                                    |
| genshi_xml                | 33.4 ms                                                                                                              | 34.6 ms: 1.04x slower                                                                                                    |
| asyncio_websockets        | 157 ms                                                                                                               | 163 ms: 1.04x slower                                                                                                     |
| async_generators          | 227 ms                                                                                                               | 245 ms: 1.08x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.25 sec                                                                                                             | 1.39 sec: 1.12x slower                                                                                                   |
| asyncio_tcp               | 380 ms                                                                                                               | 497 ms: 1.31x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (31): float, django_template, python_startup_no_site, json_loads, thrift, bench_thread_pool, python_startup, sqlglot_v2_normalize, nqueens, sympy_sum, async_tree_memoization, logging_silent, json_dumps, async_tree_cpu_io_mixed_tg, dulwich_log, async_tree_io_tg, hexiom, pylint, sphinx, coroutines, bench_mp_pool, richards_super, async_tree_none_tg, richards, unpickle, create_gc_cycles, async_tree_none, async_tree_cpu_io_mixed, subparsers, gc_traversal, pathlib

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 86.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown