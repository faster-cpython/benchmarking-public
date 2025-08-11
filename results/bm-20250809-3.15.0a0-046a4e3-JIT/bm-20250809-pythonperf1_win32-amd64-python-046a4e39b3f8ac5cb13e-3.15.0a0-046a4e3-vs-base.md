# Results vs. base

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.028x faster
- HPT reliability: 92.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                                                                     | 224 ms: 1.02x slower                                                                                                           |
| docutils       | 1.59 sec                                                                                                                   | 1.66 sec: 1.04x slower                                                                                                         |
| html5lib       | 37.6 ms                                                                                                                    | 38.6 ms: 1.02x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 390 ms                                                                                                                     | 385 ms: 1.01x faster                                                                                                           |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                                                                     | 340 ms: 1.01x slower                                                                                                           |
| asyncio_websockets         | 157 ms                                                                                                                     | 160 ms: 1.02x slower                                                                                                           |
| asyncio_tcp_ssl            | 1.40 sec                                                                                                                   | 1.44 sec: 1.03x slower                                                                                                         |
| async_generators           | 224 ms                                                                                                                     | 251 ms: 1.12x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, coroutines, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.8 ms                                                                                                                    | 54.9 ms: 1.20x faster                                                                                                          |
| float          | 44.0 ms                                                                                                                    | 43.3 ms: 1.02x faster                                                                                                          |
| pidigits       | 145 ms                                                                                                                     | 146 ms: 1.00x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 81.3 ms                                                                                                                    | 78.9 ms: 1.03x faster                                                                                                          |
| regex_effbot   | 1.48 ms                                                                                                                    | 1.55 ms: 1.04x slower                                                                                                          |
| regex_v8       | 13.3 ms                                                                                                                    | 14.0 ms: 1.05x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.44 sec                                                                                                                   | 1.10 sec: 1.30x faster                                                                                                         |
| unpickle_pure_python | 135 us                                                                                                                     | 105 us: 1.28x faster                                                                                                           |
| xml_etree_generate   | 57.9 ms                                                                                                                    | 51.2 ms: 1.13x faster                                                                                                          |
| xml_etree_process    | 40.2 ms                                                                                                                    | 35.7 ms: 1.13x faster                                                                                                          |
| pickle               | 8.05 us                                                                                                                    | 7.67 us: 1.05x faster                                                                                                          |
| pickle_pure_python   | 214 us                                                                                                                     | 204 us: 1.05x faster                                                                                                           |
| pickle_list          | 3.46 us                                                                                                                    | 3.36 us: 1.03x faster                                                                                                          |
| unpickle_list        | 2.85 us                                                                                                                    | 2.77 us: 1.03x faster                                                                                                          |
| pickle_dict          | 19.8 us                                                                                                                    | 19.4 us: 1.02x faster                                                                                                          |
| xml_etree_iterparse  | 64.4 ms                                                                                                                    | 63.2 ms: 1.02x faster                                                                                                          |
| xml_etree_parse      | 88.9 ms                                                                                                                    | 88.0 ms: 1.01x faster                                                                                                          |
| json_loads           | 14.1 us                                                                                                                    | 14.3 us: 1.02x slower                                                                                                          |
| json_dumps           | 5.36 ms                                                                                                                    | 5.45 ms: 1.02x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.66 ms                                                                                                                    | 5.28 ms: 1.26x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json | results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                | 1.44 sec                                                                                                                   | 1.10 sec: 1.30x faster                                                                                                         |
| unpickle_pure_python       | 135 us                                                                                                                     | 105 us: 1.28x faster                                                                                                           |
| fannkuch                   | 262 ms                                                                                                                     | 206 ms: 1.28x faster                                                                                                           |
| mako                       | 6.66 ms                                                                                                                    | 5.28 ms: 1.26x faster                                                                                                          |
| scimark_fft                | 187 ms                                                                                                                     | 148 ms: 1.26x faster                                                                                                           |
| nbody                      | 65.8 ms                                                                                                                    | 54.9 ms: 1.20x faster                                                                                                          |
| scimark_sparse_mat_mult    | 2.69 ms                                                                                                                    | 2.25 ms: 1.20x faster                                                                                                          |
| bpe_tokeniser              | 2.93 sec                                                                                                                   | 2.55 sec: 1.15x faster                                                                                                         |
| xml_etree_generate         | 57.9 ms                                                                                                                    | 51.2 ms: 1.13x faster                                                                                                          |
| pprint_pformat             | 1.02 sec                                                                                                                   | 907 ms: 1.13x faster                                                                                                           |
| xml_etree_process          | 40.2 ms                                                                                                                    | 35.7 ms: 1.13x faster                                                                                                          |
| pprint_safe_repr           | 497 ms                                                                                                                     | 442 ms: 1.13x faster                                                                                                           |
| telco                      | 4.72 ms                                                                                                                    | 4.24 ms: 1.11x faster                                                                                                          |
| pyflate                    | 293 ms                                                                                                                     | 265 ms: 1.11x faster                                                                                                           |
| sqlglot_v2_parse           | 836 us                                                                                                                     | 771 us: 1.08x faster                                                                                                           |
| unpack_sequence            | 35.8 ns                                                                                                                    | 33.2 ns: 1.08x faster                                                                                                          |
| shortest_path              | 379 ms                                                                                                                     | 355 ms: 1.07x faster                                                                                                           |
| sqlglot_v2_transpile       | 1.04 ms                                                                                                                    | 978 us: 1.06x faster                                                                                                           |
| scimark_monte_carlo        | 42.4 ms                                                                                                                    | 40.0 ms: 1.06x faster                                                                                                          |
| k_core                     | 1.70 sec                                                                                                                   | 1.62 sec: 1.05x faster                                                                                                         |
| pickle                     | 8.05 us                                                                                                                    | 7.67 us: 1.05x faster                                                                                                          |
| pickle_pure_python         | 214 us                                                                                                                     | 204 us: 1.05x faster                                                                                                           |
| sqlite_synth               | 1.61 us                                                                                                                    | 1.55 us: 1.04x faster                                                                                                          |
| scimark_sor                | 78.9 ms                                                                                                                    | 75.8 ms: 1.04x faster                                                                                                          |
| comprehensions             | 11.0 us                                                                                                                    | 10.5 us: 1.04x faster                                                                                                          |
| raytrace                   | 184 ms                                                                                                                     | 178 ms: 1.03x faster                                                                                                           |
| richards_super             | 31.1 ms                                                                                                                    | 30.2 ms: 1.03x faster                                                                                                          |
| pickle_list                | 3.46 us                                                                                                                    | 3.36 us: 1.03x faster                                                                                                          |
| regex_compile              | 81.3 ms                                                                                                                    | 78.9 ms: 1.03x faster                                                                                                          |
| nqueens                    | 63.1 ms                                                                                                                    | 61.3 ms: 1.03x faster                                                                                                          |
| richards                   | 27.2 ms                                                                                                                    | 26.4 ms: 1.03x faster                                                                                                          |
| thrift                     | 502 us                                                                                                                     | 489 us: 1.03x faster                                                                                                           |
| unpickle_list              | 2.85 us                                                                                                                    | 2.77 us: 1.03x faster                                                                                                          |
| pickle_dict                | 19.8 us                                                                                                                    | 19.4 us: 1.02x faster                                                                                                          |
| xml_etree_iterparse        | 64.4 ms                                                                                                                    | 63.2 ms: 1.02x faster                                                                                                          |
| pycparser                  | 702 ms                                                                                                                     | 690 ms: 1.02x faster                                                                                                           |
| connected_components       | 329 ms                                                                                                                     | 323 ms: 1.02x faster                                                                                                           |
| float                      | 44.0 ms                                                                                                                    | 43.3 ms: 1.02x faster                                                                                                          |
| go                         | 76.7 ms                                                                                                                    | 75.6 ms: 1.02x faster                                                                                                          |
| async_tree_io_tg           | 390 ms                                                                                                                     | 385 ms: 1.01x faster                                                                                                           |
| xml_etree_parse            | 88.9 ms                                                                                                                    | 88.0 ms: 1.01x faster                                                                                                          |
| crypto_pyaes               | 46.9 ms                                                                                                                    | 46.4 ms: 1.01x faster                                                                                                          |
| scimark_lu                 | 59.3 ms                                                                                                                    | 59.0 ms: 1.01x faster                                                                                                          |
| pidigits                   | 145 ms                                                                                                                     | 146 ms: 1.00x slower                                                                                                           |
| deepcopy_memo              | 18.2 us                                                                                                                    | 18.3 us: 1.01x slower                                                                                                          |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                                                                     | 340 ms: 1.01x slower                                                                                                           |
| chaos                      | 40.6 ms                                                                                                                    | 41.0 ms: 1.01x slower                                                                                                          |
| create_gc_cycles           | 1.31 ms                                                                                                                    | 1.32 ms: 1.01x slower                                                                                                          |
| typing_runtime_protocols   | 104 us                                                                                                                     | 105 us: 1.01x slower                                                                                                           |
| sympy_expand               | 287 ms                                                                                                                     | 290 ms: 1.01x slower                                                                                                           |
| json_loads                 | 14.1 us                                                                                                                    | 14.3 us: 1.02x slower                                                                                                          |
| mdp                        | 794 ms                                                                                                                     | 807 ms: 1.02x slower                                                                                                           |
| json_dumps                 | 5.36 ms                                                                                                                    | 5.45 ms: 1.02x slower                                                                                                          |
| subparsers                 | 29.3 ms                                                                                                                    | 29.8 ms: 1.02x slower                                                                                                          |
| bench_mp_pool              | 94.5 ms                                                                                                                    | 96.2 ms: 1.02x slower                                                                                                          |
| deepcopy_reduce            | 1.80 us                                                                                                                    | 1.84 us: 1.02x slower                                                                                                          |
| 2to3                       | 219 ms                                                                                                                     | 224 ms: 1.02x slower                                                                                                           |
| deltablue                  | 2.21 ms                                                                                                                    | 2.26 ms: 1.02x slower                                                                                                          |
| asyncio_websockets         | 157 ms                                                                                                                     | 160 ms: 1.02x slower                                                                                                           |
| spectral_norm              | 63.9 ms                                                                                                                    | 65.5 ms: 1.02x slower                                                                                                          |
| html5lib                   | 37.6 ms                                                                                                                    | 38.6 ms: 1.02x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.40 sec                                                                                                                   | 1.44 sec: 1.03x slower                                                                                                         |
| generators                 | 19.1 ms                                                                                                                    | 19.7 ms: 1.03x slower                                                                                                          |
| coverage                   | 49.6 ms                                                                                                                    | 51.1 ms: 1.03x slower                                                                                                          |
| gc_traversal               | 2.15 ms                                                                                                                    | 2.21 ms: 1.03x slower                                                                                                          |
| deepcopy                   | 168 us                                                                                                                     | 174 us: 1.04x slower                                                                                                           |
| dulwich_log                | 39.4 ms                                                                                                                    | 40.9 ms: 1.04x slower                                                                                                          |
| json                       | 2.97 ms                                                                                                                    | 3.10 ms: 1.04x slower                                                                                                          |
| docutils                   | 1.59 sec                                                                                                                   | 1.66 sec: 1.04x slower                                                                                                         |
| regex_effbot               | 1.48 ms                                                                                                                    | 1.55 ms: 1.04x slower                                                                                                          |
| many_optionals             | 546 us                                                                                                                     | 570 us: 1.04x slower                                                                                                           |
| regex_v8                   | 13.3 ms                                                                                                                    | 14.0 ms: 1.05x slower                                                                                                          |
| logging_silent             | 58.0 ns                                                                                                                    | 61.9 ns: 1.07x slower                                                                                                          |
| async_generators           | 224 ms                                                                                                                     | 251 ms: 1.12x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (28): async_tree_none, genshi_text, genshi_xml, async_tree_none_tg, sympy_str, sqlglot_v2_normalize, django_template, python_startup, sympy_sum, meteor_contest, coroutines, hexiom, sqlglot_v2_optimize, logging_format, sphinx, logging_simple, async_tree_memoization, sympy_integrate, async_tree_memoization_tg, async_tree_cpu_io_mixed, regex_dna, python_startup_no_site, unpickle, async_tree_io, pathlib, pylint, asyncio_tcp, bench_thread_pool

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 92.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown