# Results vs. base

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.035x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                                                             | 1.60 sec: 1.01x faster                                                                                                   |
| html5lib       | 37.5 ms                                                                                                              | 36.7 ms: 1.02x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 176 ms                                                                                                               | 168 ms: 1.04x faster                                                                                                     |
| asyncio_websockets         | 166 ms                                                                                                               | 162 ms: 1.03x faster                                                                                                     |
| async_tree_io              | 390 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 336 ms                                                                                                               | 332 ms: 1.01x faster                                                                                                     |
| async_tree_io_tg           | 382 ms                                                                                                               | 378 ms: 1.01x faster                                                                                                     |
| coroutines                 | 14.4 ms                                                                                                              | 14.6 ms: 1.01x slower                                                                                                    |
| async_generators           | 234 ms                                                                                                               | 251 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                                                              | 55.5 ms: 1.18x faster                                                                                                    |
| float          | 42.5 ms                                                                                                              | 43.7 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 121 ms                                                                                                               | 118 ms: 1.03x faster                                                                                                     |
| regex_compile  | 77.3 ms                                                                                                              | 76.8 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.53 ms                                                                                                              | 1.56 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                               | 105 us: 1.28x faster                                                                                                     |
| tomli_loads          | 1.34 sec                                                                                                             | 1.08 sec: 1.24x faster                                                                                                   |
| xml_etree_generate   | 55.1 ms                                                                                                              | 50.2 ms: 1.10x faster                                                                                                    |
| xml_etree_process    | 38.1 ms                                                                                                              | 35.8 ms: 1.07x faster                                                                                                    |
| pickle_pure_python   | 209 us                                                                                                               | 198 us: 1.06x faster                                                                                                     |
| pickle               | 7.80 us                                                                                                              | 7.44 us: 1.05x faster                                                                                                    |
| json_loads           | 14.3 us                                                                                                              | 13.8 us: 1.04x faster                                                                                                    |
| pickle_list          | 3.27 us                                                                                                              | 3.16 us: 1.03x faster                                                                                                    |
| unpickle_list        | 2.78 us                                                                                                              | 2.69 us: 1.03x faster                                                                                                    |
| pickle_dict          | 19.4 us                                                                                                              | 19.0 us: 1.02x faster                                                                                                    |
| xml_etree_parse      | 86.3 ms                                                                                                              | 84.7 ms: 1.02x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.67 ms                                                                                                              | 5.25 ms: 1.27x faster                                                                                                    |
| django_template | 25.2 ms                                                                                                              | 24.0 ms: 1.05x faster                                                                                                    |
| genshi_xml      | 34.4 ms                                                                                                              | 34.0 ms: 1.01x faster                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | results/bm-20250913-3.15.0a0-7168e98/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json | results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 134 us                                                                                                               | 105 us: 1.28x faster                                                                                                     |
| mako                       | 6.67 ms                                                                                                              | 5.25 ms: 1.27x faster                                                                                                    |
| tomli_loads                | 1.34 sec                                                                                                             | 1.08 sec: 1.24x faster                                                                                                   |
| fannkuch                   | 261 ms                                                                                                               | 212 ms: 1.23x faster                                                                                                     |
| scimark_fft                | 180 ms                                                                                                               | 147 ms: 1.22x faster                                                                                                     |
| richards                   | 26.8 ms                                                                                                              | 22.3 ms: 1.20x faster                                                                                                    |
| bpe_tokeniser              | 2.96 sec                                                                                                             | 2.50 sec: 1.18x faster                                                                                                   |
| nbody                      | 65.5 ms                                                                                                              | 55.5 ms: 1.18x faster                                                                                                    |
| richards_super             | 30.5 ms                                                                                                              | 26.5 ms: 1.15x faster                                                                                                    |
| pprint_safe_repr           | 480 ms                                                                                                               | 422 ms: 1.14x faster                                                                                                     |
| pprint_pformat             | 975 ms                                                                                                               | 867 ms: 1.12x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.51 ms                                                                                                              | 2.23 ms: 1.12x faster                                                                                                    |
| pyflate                    | 282 ms                                                                                                               | 252 ms: 1.12x faster                                                                                                     |
| xml_etree_generate         | 55.1 ms                                                                                                              | 50.2 ms: 1.10x faster                                                                                                    |
| telco                      | 4.14 ms                                                                                                              | 3.80 ms: 1.09x faster                                                                                                    |
| sqlglot_v2_parse           | 820 us                                                                                                               | 769 us: 1.07x faster                                                                                                     |
| xml_etree_process          | 38.1 ms                                                                                                              | 35.8 ms: 1.07x faster                                                                                                    |
| scimark_monte_carlo        | 40.5 ms                                                                                                              | 38.1 ms: 1.06x faster                                                                                                    |
| k_core                     | 1.67 sec                                                                                                             | 1.58 sec: 1.06x faster                                                                                                   |
| pickle_pure_python         | 209 us                                                                                                               | 198 us: 1.06x faster                                                                                                     |
| crypto_pyaes               | 47.1 ms                                                                                                              | 44.7 ms: 1.05x faster                                                                                                    |
| pickle                     | 7.80 us                                                                                                              | 7.44 us: 1.05x faster                                                                                                    |
| django_template            | 25.2 ms                                                                                                              | 24.0 ms: 1.05x faster                                                                                                    |
| nqueens                    | 61.5 ms                                                                                                              | 58.8 ms: 1.05x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                              | 969 us: 1.04x faster                                                                                                     |
| async_tree_none            | 176 ms                                                                                                               | 168 ms: 1.04x faster                                                                                                     |
| comprehensions             | 10.9 us                                                                                                              | 10.5 us: 1.04x faster                                                                                                    |
| gc_traversal               | 2.13 ms                                                                                                              | 2.06 ms: 1.04x faster                                                                                                    |
| logging_silent             | 55.2 ns                                                                                                              | 53.2 ns: 1.04x faster                                                                                                    |
| json_loads                 | 14.3 us                                                                                                              | 13.8 us: 1.04x faster                                                                                                    |
| pickle_list                | 3.27 us                                                                                                              | 3.16 us: 1.03x faster                                                                                                    |
| unpickle_list              | 2.78 us                                                                                                              | 2.69 us: 1.03x faster                                                                                                    |
| connected_components       | 327 ms                                                                                                               | 318 ms: 1.03x faster                                                                                                     |
| pycparser                  | 705 ms                                                                                                               | 685 ms: 1.03x faster                                                                                                     |
| scimark_lu                 | 58.3 ms                                                                                                              | 56.8 ms: 1.03x faster                                                                                                    |
| regex_dna                  | 121 ms                                                                                                               | 118 ms: 1.03x faster                                                                                                     |
| asyncio_websockets         | 166 ms                                                                                                               | 162 ms: 1.03x faster                                                                                                     |
| sympy_sum                  | 87.5 ms                                                                                                              | 85.4 ms: 1.03x faster                                                                                                    |
| sqlite_synth               | 1.55 us                                                                                                              | 1.51 us: 1.03x faster                                                                                                    |
| shortest_path              | 357 ms                                                                                                               | 349 ms: 1.02x faster                                                                                                     |
| html5lib                   | 37.5 ms                                                                                                              | 36.7 ms: 1.02x faster                                                                                                    |
| deltablue                  | 2.20 ms                                                                                                              | 2.15 ms: 1.02x faster                                                                                                    |
| spectral_norm              | 62.5 ms                                                                                                              | 61.2 ms: 1.02x faster                                                                                                    |
| json                       | 2.89 ms                                                                                                              | 2.83 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 390 ms                                                                                                               | 382 ms: 1.02x faster                                                                                                     |
| pickle_dict                | 19.4 us                                                                                                              | 19.0 us: 1.02x faster                                                                                                    |
| xml_etree_parse            | 86.3 ms                                                                                                              | 84.7 ms: 1.02x faster                                                                                                    |
| meteor_contest             | 72.6 ms                                                                                                              | 71.4 ms: 1.02x faster                                                                                                    |
| go                         | 75.5 ms                                                                                                              | 74.3 ms: 1.02x faster                                                                                                    |
| raytrace                   | 177 ms                                                                                                               | 174 ms: 1.02x faster                                                                                                     |
| docutils                   | 1.63 sec                                                                                                             | 1.60 sec: 1.01x faster                                                                                                   |
| async_tree_cpu_io_mixed_tg | 336 ms                                                                                                               | 332 ms: 1.01x faster                                                                                                     |
| async_tree_io_tg           | 382 ms                                                                                                               | 378 ms: 1.01x faster                                                                                                     |
| mdp                        | 800 ms                                                                                                               | 791 ms: 1.01x faster                                                                                                     |
| genshi_xml                 | 34.4 ms                                                                                                              | 34.0 ms: 1.01x faster                                                                                                    |
| typing_runtime_protocols   | 101 us                                                                                                               | 100 us: 1.01x faster                                                                                                     |
| regex_compile              | 77.3 ms                                                                                                              | 76.8 ms: 1.01x faster                                                                                                    |
| hexiom                     | 4.04 ms                                                                                                              | 4.02 ms: 1.00x faster                                                                                                    |
| sympy_str                  | 165 ms                                                                                                               | 166 ms: 1.01x slower                                                                                                     |
| create_gc_cycles           | 1.24 ms                                                                                                              | 1.25 ms: 1.01x slower                                                                                                    |
| coroutines                 | 14.4 ms                                                                                                              | 14.6 ms: 1.01x slower                                                                                                    |
| sympy_integrate            | 12.3 ms                                                                                                              | 12.4 ms: 1.01x slower                                                                                                    |
| sqlglot_v2_optimize        | 33.5 ms                                                                                                              | 34.0 ms: 1.02x slower                                                                                                    |
| thrift                     | 502 us                                                                                                               | 510 us: 1.02x slower                                                                                                     |
| regex_effbot               | 1.53 ms                                                                                                              | 1.56 ms: 1.02x slower                                                                                                    |
| generators                 | 18.9 ms                                                                                                              | 19.2 ms: 1.02x slower                                                                                                    |
| deepcopy_memo              | 16.6 us                                                                                                              | 16.9 us: 1.02x slower                                                                                                    |
| many_optionals             | 551 us                                                                                                               | 563 us: 1.02x slower                                                                                                     |
| float                      | 42.5 ms                                                                                                              | 43.7 ms: 1.03x slower                                                                                                    |
| bench_thread_pool          | 836 us                                                                                                               | 860 us: 1.03x slower                                                                                                     |
| sympy_expand               | 284 ms                                                                                                               | 292 ms: 1.03x slower                                                                                                     |
| async_generators           | 234 ms                                                                                                               | 251 ms: 1.07x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (30): deepcopy, unpickle, logging_format, chaos, sqlglot_v2_normalize, sphinx, deepcopy_reduce, 2to3, pidigits, asyncio_tcp_ssl, subparsers, unpack_sequence, scimark_sor, logging_simple, async_tree_none_tg, genshi_text, xml_etree_iterparse, async_tree_cpu_io_mixed, bench_mp_pool, pathlib, python_startup_no_site, async_tree_memoization, asyncio_tcp, python_startup, dulwich_log, async_tree_memoization_tg, coverage, json_dumps, pylint, regex_v8

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown