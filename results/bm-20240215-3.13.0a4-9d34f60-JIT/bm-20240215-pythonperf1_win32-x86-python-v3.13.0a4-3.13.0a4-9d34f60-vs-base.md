# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                                                        | 256 ms: 1.11x slower                                                                                              |
| chameleon      | 5.61 ms                                                                                                       | 6.01 ms: 1.07x slower                                                                                             |
| docutils       | 1.71 sec                                                                                                      | 1.82 sec: 1.06x slower                                                                                            |
| tornado_http   | 93.5 ms                                                                                                       | 99.9 ms: 1.07x slower                                                                                             |
| Geometric mean | (ref)                                                                                                         | 1.08x slower                                                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 489 ms                                                                                                        | 503 ms: 1.03x slower                                                                                              |
| async_tree_cpu_io_mixed    | 496 ms                                                                                                        | 515 ms: 1.04x slower                                                                                              |
| async_tree_io              | 584 ms                                                                                                        | 624 ms: 1.07x slower                                                                                              |
| async_tree_io_tg           | 570 ms                                                                                                        | 612 ms: 1.07x slower                                                                                              |
| async_tree_memoization     | 299 ms                                                                                                        | 325 ms: 1.08x slower                                                                                              |
| async_tree_none            | 239 ms                                                                                                        | 260 ms: 1.09x slower                                                                                              |
| async_tree_none_tg         | 225 ms                                                                                                        | 246 ms: 1.10x slower                                                                                              |
| async_tree_memoization_tg  | 284 ms                                                                                                        | 313 ms: 1.10x slower                                                                                              |
| Geometric mean             | (ref)                                                                                                         | 1.07x slower                                                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| float          | 52.8 ms                                                                                                       | 53.9 ms: 1.02x slower                                                                                             |
| pidigits       | 197 ms                                                                                                        | 202 ms: 1.03x slower                                                                                              |
| nbody          | 76.8 ms                                                                                                       | 89.7 ms: 1.17x slower                                                                                             |
| Geometric mean | (ref)                                                                                                         | 1.07x slower                                                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 16.0 ms                                                                                                       | 16.2 ms: 1.01x slower                                                                                             |
| regex_effbot   | 1.89 ms                                                                                                       | 1.91 ms: 1.01x slower                                                                                             |
| regex_dna      | 116 ms                                                                                                        | 120 ms: 1.03x slower                                                                                              |
| regex_compile  | 93.4 ms                                                                                                       | 110 ms: 1.18x slower                                                                                              |
| Geometric mean | (ref)                                                                                                         | 1.06x slower                                                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 60.0 ms                                                                                                       | 60.2 ms: 1.00x slower                                                                                             |
| unpickle             | 10.0 us                                                                                                       | 10.1 us: 1.01x slower                                                                                             |
| tomli_loads          | 1.62 sec                                                                                                      | 1.65 sec: 1.02x slower                                                                                            |
| pickle               | 7.90 us                                                                                                       | 8.11 us: 1.03x slower                                                                                             |
| pickle_list          | 3.25 us                                                                                                       | 3.35 us: 1.03x slower                                                                                             |
| json_dumps           | 6.71 ms                                                                                                       | 6.95 ms: 1.04x slower                                                                                             |
| xml_etree_process    | 41.2 ms                                                                                                       | 42.8 ms: 1.04x slower                                                                                             |
| pickle_pure_python   | 210 us                                                                                                        | 223 us: 1.06x slower                                                                                              |
| unpickle_pure_python | 140 us                                                                                                        | 156 us: 1.11x slower                                                                                              |
| Geometric mean       | (ref)                                                                                                         | 1.02x slower                                                                                                      |

Benchmark hidden because not significant (5): unpickle_list, xml_etree_iterparse, xml_etree_parse, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 22.0 ms                                                                                                       | 22.5 ms: 1.02x slower                                                                                             |
| python_startup_no_site | 19.7 ms                                                                                                       | 20.3 ms: 1.03x slower                                                                                             |
| Geometric mean         | (ref)                                                                                                         | 1.03x slower                                                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| mako      | 6.76 ms                                                                                                       | 7.43 ms: 1.10x slower                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:|
| pathlib                    | 88.6 ms                                                                                                       | 84.3 ms: 1.05x faster                                                                                             |
| create_gc_cycles           | 662 us                                                                                                        | 646 us: 1.03x faster                                                                                              |
| xml_etree_generate         | 60.0 ms                                                                                                       | 60.2 ms: 1.00x slower                                                                                             |
| regex_v8                   | 16.0 ms                                                                                                       | 16.2 ms: 1.01x slower                                                                                             |
| coverage                   | 460 ms                                                                                                        | 464 ms: 1.01x slower                                                                                              |
| unpickle                   | 10.0 us                                                                                                       | 10.1 us: 1.01x slower                                                                                             |
| regex_effbot               | 1.89 ms                                                                                                       | 1.91 ms: 1.01x slower                                                                                             |
| bench_mp_pool              | 70.4 ms                                                                                                       | 71.5 ms: 1.02x slower                                                                                             |
| gc_traversal               | 1.39 ms                                                                                                       | 1.42 ms: 1.02x slower                                                                                             |
| tomli_loads                | 1.62 sec                                                                                                      | 1.65 sec: 1.02x slower                                                                                            |
| float                      | 52.8 ms                                                                                                       | 53.9 ms: 1.02x slower                                                                                             |
| python_startup             | 22.0 ms                                                                                                       | 22.5 ms: 1.02x slower                                                                                             |
| pidigits                   | 197 ms                                                                                                        | 202 ms: 1.03x slower                                                                                              |
| json                       | 4.16 ms                                                                                                       | 4.27 ms: 1.03x slower                                                                                             |
| pickle                     | 7.90 us                                                                                                       | 8.11 us: 1.03x slower                                                                                             |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                                                        | 503 ms: 1.03x slower                                                                                              |
| python_startup_no_site     | 19.7 ms                                                                                                       | 20.3 ms: 1.03x slower                                                                                             |
| pickle_list                | 3.25 us                                                                                                       | 3.35 us: 1.03x slower                                                                                             |
| regex_dna                  | 116 ms                                                                                                        | 120 ms: 1.03x slower                                                                                              |
| json_dumps                 | 6.71 ms                                                                                                       | 6.95 ms: 1.04x slower                                                                                             |
| async_tree_cpu_io_mixed    | 496 ms                                                                                                        | 515 ms: 1.04x slower                                                                                              |
| bench_thread_pool          | 984 us                                                                                                        | 1.02 ms: 1.04x slower                                                                                             |
| xml_etree_process          | 41.2 ms                                                                                                       | 42.8 ms: 1.04x slower                                                                                             |
| coroutines                 | 14.1 ms                                                                                                       | 14.9 ms: 1.06x slower                                                                                             |
| docutils                   | 1.71 sec                                                                                                      | 1.82 sec: 1.06x slower                                                                                            |
| pickle_pure_python         | 210 us                                                                                                        | 223 us: 1.06x slower                                                                                              |
| async_tree_io              | 584 ms                                                                                                        | 624 ms: 1.07x slower                                                                                              |
| tornado_http               | 93.5 ms                                                                                                       | 99.9 ms: 1.07x slower                                                                                             |
| chameleon                  | 5.61 ms                                                                                                       | 6.01 ms: 1.07x slower                                                                                             |
| async_tree_io_tg           | 570 ms                                                                                                        | 612 ms: 1.07x slower                                                                                              |
| deepcopy_reduce            | 2.32 us                                                                                                       | 2.51 us: 1.08x slower                                                                                             |
| generators                 | 22.7 ms                                                                                                       | 24.6 ms: 1.08x slower                                                                                             |
| scimark_sparse_mat_mult    | 2.88 ms                                                                                                       | 3.12 ms: 1.08x slower                                                                                             |
| meteor_contest             | 77.4 ms                                                                                                       | 83.8 ms: 1.08x slower                                                                                             |
| richards_super             | 33.7 ms                                                                                                       | 36.5 ms: 1.08x slower                                                                                             |
| async_tree_memoization     | 299 ms                                                                                                        | 325 ms: 1.08x slower                                                                                              |
| async_tree_none            | 239 ms                                                                                                        | 260 ms: 1.09x slower                                                                                              |
| deepcopy                   | 261 us                                                                                                        | 285 us: 1.09x slower                                                                                              |
| async_tree_none_tg         | 225 ms                                                                                                        | 246 ms: 1.10x slower                                                                                              |
| sqlglot_transpile          | 1.10 ms                                                                                                       | 1.21 ms: 1.10x slower                                                                                             |
| mako                       | 6.76 ms                                                                                                       | 7.43 ms: 1.10x slower                                                                                             |
| async_tree_memoization_tg  | 284 ms                                                                                                        | 313 ms: 1.10x slower                                                                                              |
| logging_format             | 8.10 us                                                                                                       | 8.97 us: 1.11x slower                                                                                             |
| sqlglot_parse              | 868 us                                                                                                        | 961 us: 1.11x slower                                                                                              |
| scimark_sor                | 80.9 ms                                                                                                       | 89.6 ms: 1.11x slower                                                                                             |
| sympy_sum                  | 99.4 ms                                                                                                       | 110 ms: 1.11x slower                                                                                              |
| unpickle_pure_python       | 140 us                                                                                                        | 156 us: 1.11x slower                                                                                              |
| scimark_lu                 | 59.0 ms                                                                                                       | 65.6 ms: 1.11x slower                                                                                             |
| sqlglot_normalize          | 201 ms                                                                                                        | 224 ms: 1.11x slower                                                                                              |
| 2to3                       | 230 ms                                                                                                        | 256 ms: 1.11x slower                                                                                              |
| sympy_expand               | 341 ms                                                                                                        | 379 ms: 1.11x slower                                                                                              |
| logging_simple             | 7.46 us                                                                                                       | 8.35 us: 1.12x slower                                                                                             |
| spectral_norm              | 65.4 ms                                                                                                       | 73.2 ms: 1.12x slower                                                                                             |
| typing_runtime_protocols   | 87.8 us                                                                                                       | 98.7 us: 1.12x slower                                                                                             |
| sympy_str                  | 194 ms                                                                                                        | 218 ms: 1.13x slower                                                                                              |
| sqlglot_optimize           | 38.6 ms                                                                                                       | 43.7 ms: 1.13x slower                                                                                             |
| richards                   | 28.4 ms                                                                                                       | 32.2 ms: 1.13x slower                                                                                             |
| pycparser                  | 784 ms                                                                                                        | 891 ms: 1.14x slower                                                                                              |
| telco                      | 5.76 ms                                                                                                       | 6.55 ms: 1.14x slower                                                                                             |
| sympy_integrate            | 14.0 ms                                                                                                       | 16.0 ms: 1.14x slower                                                                                             |
| async_generators           | 262 ms                                                                                                        | 300 ms: 1.14x slower                                                                                              |
| deepcopy_memo              | 22.0 us                                                                                                       | 25.3 us: 1.15x slower                                                                                             |
| crypto_pyaes               | 52.6 ms                                                                                                       | 61.0 ms: 1.16x slower                                                                                             |
| nbody                      | 76.8 ms                                                                                                       | 89.7 ms: 1.17x slower                                                                                             |
| mdp                        | 1.57 sec                                                                                                      | 1.85 sec: 1.17x slower                                                                                            |
| logging_silent             | 56.9 ns                                                                                                       | 67.1 ns: 1.18x slower                                                                                             |
| regex_compile              | 93.4 ms                                                                                                       | 110 ms: 1.18x slower                                                                                              |
| fannkuch                   | 271 ms                                                                                                        | 322 ms: 1.19x slower                                                                                              |
| deltablue                  | 2.17 ms                                                                                                       | 2.58 ms: 1.19x slower                                                                                             |
| scimark_fft                | 198 ms                                                                                                        | 239 ms: 1.20x slower                                                                                              |
| pyflate                    | 307 ms                                                                                                        | 370 ms: 1.20x slower                                                                                              |
| comprehensions             | 11.5 us                                                                                                       | 14.1 us: 1.23x slower                                                                                             |
| pprint_safe_repr           | 568 ms                                                                                                        | 713 ms: 1.26x slower                                                                                              |
| raytrace                   | 191 ms                                                                                                        | 240 ms: 1.26x slower                                                                                              |
| pprint_pformat             | 1.16 sec                                                                                                      | 1.47 sec: 1.27x slower                                                                                            |
| go                         | 95.1 ms                                                                                                       | 123 ms: 1.29x slower                                                                                              |
| chaos                      | 46.3 ms                                                                                                       | 61.0 ms: 1.32x slower                                                                                             |
| nqueens                    | 66.9 ms                                                                                                       | 88.7 ms: 1.33x slower                                                                                             |
| hexiom                     | 4.20 ms                                                                                                       | 6.61 ms: 1.57x slower                                                                                             |
| scimark_monte_carlo        | 44.9 ms                                                                                                       | 71.6 ms: 1.60x slower                                                                                             |
| Geometric mean             | (ref)                                                                                                         | 1.10x slower                                                                                                      |

Benchmark hidden because not significant (8): unpickle_list, xml_etree_iterparse, xml_etree_parse, asyncio_tcp_ssl, sqlite_synth, pickle_dict, json_loads, asyncio_tcp
Ignored benchmarks (7) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown