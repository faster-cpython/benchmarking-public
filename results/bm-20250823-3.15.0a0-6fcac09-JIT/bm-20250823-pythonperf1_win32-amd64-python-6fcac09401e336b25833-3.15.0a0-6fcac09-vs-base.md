# Results vs. base

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.027x faster
- HPT reliability: 97.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                                                                                     | 214 ms: 1.01x faster                                                                                                           |
| docutils       | 1.59 sec                                                                                                                   | 1.61 sec: 1.01x slower                                                                                                         |
| html5lib       | 37.5 ms                                                                                                                    | 37.8 ms: 1.01x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.00x faster                                                                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp               | 379 ms                                                                                                                     | 368 ms: 1.03x faster                                                                                                           |
| async_tree_none           | 173 ms                                                                                                                     | 170 ms: 1.01x faster                                                                                                           |
| coroutines                | 14.0 ms                                                                                                                    | 14.0 ms: 1.00x faster                                                                                                          |
| async_tree_cpu_io_mixed   | 327 ms                                                                                                                     | 329 ms: 1.01x slower                                                                                                           |
| async_tree_memoization_tg | 205 ms                                                                                                                     | 208 ms: 1.02x slower                                                                                                           |
| async_generators          | 225 ms                                                                                                                     | 245 ms: 1.09x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.00x slower                                                                                                                   |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.0 ms                                                                                                                    | 53.0 ms: 1.21x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                                                                                    | 13.1 ms: 1.05x faster                                                                                                          |
| regex_dna      | 120 ms                                                                                                                     | 116 ms: 1.04x faster                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                                     | 104 us: 1.29x faster                                                                                                           |
| tomli_loads          | 1.39 sec                                                                                                                   | 1.09 sec: 1.27x faster                                                                                                         |
| xml_etree_generate   | 56.4 ms                                                                                                                    | 51.1 ms: 1.10x faster                                                                                                          |
| xml_etree_process    | 38.7 ms                                                                                                                    | 35.4 ms: 1.10x faster                                                                                                          |
| unpickle_list        | 2.83 us                                                                                                                    | 2.69 us: 1.05x faster                                                                                                          |
| pickle_pure_python   | 211 us                                                                                                                     | 201 us: 1.05x faster                                                                                                           |
| json_loads           | 14.3 us                                                                                                                    | 13.9 us: 1.03x faster                                                                                                          |
| pickle               | 7.87 us                                                                                                                    | 7.72 us: 1.02x faster                                                                                                          |
| xml_etree_iterparse  | 62.3 ms                                                                                                                    | 61.6 ms: 1.01x faster                                                                                                          |
| json_dumps           | 5.34 ms                                                                                                                    | 5.38 ms: 1.01x slower                                                                                                          |
| pickle_dict          | 19.2 us                                                                                                                    | 19.5 us: 1.01x slower                                                                                                          |
| pickle_list          | 3.28 us                                                                                                                    | 3.33 us: 1.02x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.3 ms                                                                                                                    | 18.9 ms: 1.02x faster                                                                                                          |
| Geometric mean         | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.56 ms                                                                                                                    | 5.20 ms: 1.26x faster                                                                                                          |
| genshi_xml     | 34.0 ms                                                                                                                    | 34.5 ms: 1.01x slower                                                                                                          |
| genshi_text    | 15.2 ms                                                                                                                    | 15.6 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python      | 134 us                                                                                                                     | 104 us: 1.29x faster                                                                                                           |
| tomli_loads               | 1.39 sec                                                                                                                   | 1.09 sec: 1.27x faster                                                                                                         |
| mako                      | 6.56 ms                                                                                                                    | 5.20 ms: 1.26x faster                                                                                                          |
| fannkuch                  | 260 ms                                                                                                                     | 212 ms: 1.22x faster                                                                                                           |
| nbody                     | 64.0 ms                                                                                                                    | 53.0 ms: 1.21x faster                                                                                                          |
| scimark_fft               | 180 ms                                                                                                                     | 149 ms: 1.21x faster                                                                                                           |
| bpe_tokeniser             | 2.94 sec                                                                                                                   | 2.53 sec: 1.16x faster                                                                                                         |
| pprint_pformat            | 981 ms                                                                                                                     | 851 ms: 1.15x faster                                                                                                           |
| pprint_safe_repr          | 478 ms                                                                                                                     | 417 ms: 1.14x faster                                                                                                           |
| scimark_sparse_mat_mult   | 2.51 ms                                                                                                                    | 2.27 ms: 1.11x faster                                                                                                          |
| xml_etree_generate        | 56.4 ms                                                                                                                    | 51.1 ms: 1.10x faster                                                                                                          |
| unpack_sequence           | 37.9 ns                                                                                                                    | 34.4 ns: 1.10x faster                                                                                                          |
| xml_etree_process         | 38.7 ms                                                                                                                    | 35.4 ms: 1.10x faster                                                                                                          |
| telco                     | 4.13 ms                                                                                                                    | 3.82 ms: 1.08x faster                                                                                                          |
| pyflate                   | 288 ms                                                                                                                     | 268 ms: 1.07x faster                                                                                                           |
| sqlglot_v2_parse          | 809 us                                                                                                                     | 763 us: 1.06x faster                                                                                                           |
| regex_v8                  | 13.8 ms                                                                                                                    | 13.1 ms: 1.05x faster                                                                                                          |
| comprehensions            | 10.8 us                                                                                                                    | 10.3 us: 1.05x faster                                                                                                          |
| unpickle_list             | 2.83 us                                                                                                                    | 2.69 us: 1.05x faster                                                                                                          |
| k_core                    | 1.66 sec                                                                                                                   | 1.58 sec: 1.05x faster                                                                                                         |
| crypto_pyaes              | 46.7 ms                                                                                                                    | 44.6 ms: 1.05x faster                                                                                                          |
| pickle_pure_python        | 211 us                                                                                                                     | 201 us: 1.05x faster                                                                                                           |
| connected_components      | 326 ms                                                                                                                     | 312 ms: 1.04x faster                                                                                                           |
| regex_dna                 | 120 ms                                                                                                                     | 116 ms: 1.04x faster                                                                                                           |
| sqlglot_v2_transpile      | 1.01 ms                                                                                                                    | 969 us: 1.04x faster                                                                                                           |
| shortest_path             | 357 ms                                                                                                                     | 345 ms: 1.04x faster                                                                                                           |
| pycparser                 | 701 ms                                                                                                                     | 678 ms: 1.03x faster                                                                                                           |
| subparsers                | 30.2 ms                                                                                                                    | 29.2 ms: 1.03x faster                                                                                                          |
| typing_runtime_protocols  | 104 us                                                                                                                     | 101 us: 1.03x faster                                                                                                           |
| asyncio_tcp               | 379 ms                                                                                                                     | 368 ms: 1.03x faster                                                                                                           |
| json_loads                | 14.3 us                                                                                                                    | 13.9 us: 1.03x faster                                                                                                          |
| spectral_norm             | 63.1 ms                                                                                                                    | 61.5 ms: 1.03x faster                                                                                                          |
| sqlite_synth              | 1.55 us                                                                                                                    | 1.52 us: 1.02x faster                                                                                                          |
| hexiom                    | 4.04 ms                                                                                                                    | 3.95 ms: 1.02x faster                                                                                                          |
| python_startup_no_site    | 19.3 ms                                                                                                                    | 18.9 ms: 1.02x faster                                                                                                          |
| pickle                    | 7.87 us                                                                                                                    | 7.72 us: 1.02x faster                                                                                                          |
| nqueens                   | 60.8 ms                                                                                                                    | 59.7 ms: 1.02x faster                                                                                                          |
| meteor_contest            | 71.5 ms                                                                                                                    | 70.4 ms: 1.02x faster                                                                                                          |
| async_tree_none           | 173 ms                                                                                                                     | 170 ms: 1.01x faster                                                                                                           |
| 2to3                      | 217 ms                                                                                                                     | 214 ms: 1.01x faster                                                                                                           |
| xml_etree_iterparse       | 62.3 ms                                                                                                                    | 61.6 ms: 1.01x faster                                                                                                          |
| raytrace                  | 174 ms                                                                                                                     | 172 ms: 1.01x faster                                                                                                           |
| mdp                       | 794 ms                                                                                                                     | 788 ms: 1.01x faster                                                                                                           |
| richards_super            | 30.3 ms                                                                                                                    | 30.1 ms: 1.01x faster                                                                                                          |
| coroutines                | 14.0 ms                                                                                                                    | 14.0 ms: 1.00x faster                                                                                                          |
| logging_silent            | 54.6 ns                                                                                                                    | 54.4 ns: 1.00x faster                                                                                                          |
| async_tree_cpu_io_mixed   | 327 ms                                                                                                                     | 329 ms: 1.01x slower                                                                                                           |
| json_dumps                | 5.34 ms                                                                                                                    | 5.38 ms: 1.01x slower                                                                                                          |
| docutils                  | 1.59 sec                                                                                                                   | 1.61 sec: 1.01x slower                                                                                                         |
| html5lib                  | 37.5 ms                                                                                                                    | 37.8 ms: 1.01x slower                                                                                                          |
| go                        | 76.1 ms                                                                                                                    | 76.8 ms: 1.01x slower                                                                                                          |
| scimark_sor               | 76.3 ms                                                                                                                    | 77.1 ms: 1.01x slower                                                                                                          |
| pickle_dict               | 19.2 us                                                                                                                    | 19.5 us: 1.01x slower                                                                                                          |
| sympy_str                 | 165 ms                                                                                                                     | 167 ms: 1.01x slower                                                                                                           |
| sqlglot_v2_normalize      | 69.4 ms                                                                                                                    | 70.4 ms: 1.01x slower                                                                                                          |
| logging_simple            | 5.97 us                                                                                                                    | 6.05 us: 1.01x slower                                                                                                          |
| genshi_xml                | 34.0 ms                                                                                                                    | 34.5 ms: 1.01x slower                                                                                                          |
| async_tree_memoization_tg | 205 ms                                                                                                                     | 208 ms: 1.02x slower                                                                                                           |
| pickle_list               | 3.28 us                                                                                                                    | 3.33 us: 1.02x slower                                                                                                          |
| generators                | 18.8 ms                                                                                                                    | 19.2 ms: 1.02x slower                                                                                                          |
| sqlglot_v2_optimize       | 33.6 ms                                                                                                                    | 34.4 ms: 1.02x slower                                                                                                          |
| genshi_text               | 15.2 ms                                                                                                                    | 15.6 ms: 1.02x slower                                                                                                          |
| coverage                  | 48.9 ms                                                                                                                    | 50.1 ms: 1.02x slower                                                                                                          |
| sympy_expand              | 281 ms                                                                                                                     | 288 ms: 1.02x slower                                                                                                           |
| deepcopy_memo             | 19.3 us                                                                                                                    | 19.8 us: 1.03x slower                                                                                                          |
| scimark_monte_carlo       | 39.0 ms                                                                                                                    | 40.3 ms: 1.03x slower                                                                                                          |
| gc_traversal              | 2.05 ms                                                                                                                    | 2.12 ms: 1.04x slower                                                                                                          |
| thrift                    | 488 us                                                                                                                     | 506 us: 1.04x slower                                                                                                           |
| chaos                     | 39.3 ms                                                                                                                    | 41.1 ms: 1.05x slower                                                                                                          |
| scimark_lu                | 56.4 ms                                                                                                                    | 59.7 ms: 1.06x slower                                                                                                          |
| async_generators          | 225 ms                                                                                                                     | 245 ms: 1.09x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

Benchmark hidden because not significant (31): django_template, async_tree_none_tg, pylint, async_tree_io_tg, regex_compile, asyncio_tcp_ssl, sphinx, json, deltablue, logging_format, bench_thread_pool, regex_effbot, sympy_integrate, xml_etree_parse, create_gc_cycles, bench_mp_pool, async_tree_memoization, async_tree_io, python_startup, sympy_sum, richards, float, deepcopy_reduce, async_tree_cpu_io_mixed_tg, deepcopy, dulwich_log, many_optionals, pathlib, unpickle, pidigits, asyncio_websockets

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 97.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown