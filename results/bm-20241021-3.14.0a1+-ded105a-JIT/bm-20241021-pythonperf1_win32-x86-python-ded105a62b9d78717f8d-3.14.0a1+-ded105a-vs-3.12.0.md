# Results vs. 3.12.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                            |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 476 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 64.6 ms: 1.96x faster                                                           |
| float          | 76.7 ms                                                         | 46.6 ms: 1.65x faster                                                           |
| pidigits       | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.47x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| regex_dna      | 127 ms                                                          | 124 ms: 1.03x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 55.1 ms: 1.31x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 160 us: 1.31x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 42.1 ms: 1.26x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 246 us: 1.16x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.69 ms: 1.75x faster                                                           |
| django_template | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 16.6 us: 2.31x faster                                                           |
| nbody                      | 127 ms                                                          | 64.6 ms: 1.96x faster                                                           |
| scimark_sor                | 130 ms                                                          | 70.2 ms: 1.85x faster                                                           |
| logging_silent             | 101 ns                                                          | 55.6 ns: 1.82x faster                                                           |
| spectral_norm              | 104 ms                                                          | 57.8 ms: 1.80x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.69 ms: 1.75x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 40.0 ms: 1.66x faster                                                           |
| float                      | 76.7 ms                                                         | 46.6 ms: 1.65x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.9 ms: 1.61x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.48 ms: 1.55x faster                                                           |
| deepcopy                   | 360 us                                                          | 236 us: 1.53x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 61.8 ms: 1.51x faster                                                           |
| fannkuch                   | 354 ms                                                          | 237 ms: 1.49x faster                                                            |
| comprehensions             | 19.2 us                                                         | 13.0 us: 1.48x faster                                                           |
| scimark_fft                | 271 ms                                                          | 183 ms: 1.48x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.53 sec: 1.44x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.52 ms: 1.42x faster                                                           |
| go                         | 137 ms                                                          | 96.7 ms: 1.42x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 49.8 ms: 1.39x faster                                                           |
| pyflate                    | 424 ms                                                          | 312 ms: 1.36x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 222 ms: 1.34x faster                                                            |
| async_tree_io              | 693 ms                                                          | 524 ms: 1.32x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.44 us: 1.32x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 55.1 ms: 1.31x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 160 us: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 269 ms: 1.30x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.30x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.58 us: 1.29x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.32 ms: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.5 ms: 1.27x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 567 ms: 1.27x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 42.1 ms: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.23 us: 1.26x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 551 ms: 1.23x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 76.3 ms: 1.23x faster                                                           |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                            |
| pycparser                  | 978 ms                                                          | 809 ms: 1.21x faster                                                            |
| coroutines                 | 20.9 ms                                                         | 17.3 ms: 1.21x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.3 ms: 1.20x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 476 ms: 1.18x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 246 us: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.13x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                          |
| raytrace                   | 308 ms                                                          | 275 ms: 1.12x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 988 us: 1.12x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.89 ms: 1.08x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| 2to3                       | 280 ms                                                          | 264 ms: 1.06x faster                                                            |
| richards                   | 41.3 ms                                                         | 39.2 ms: 1.05x faster                                                           |
| sympy_str                  | 240 ms                                                          | 230 ms: 1.04x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 88.0 ms: 1.04x faster                                                           |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.03x faster                                                            |
| richards_super             | 46.5 ms                                                         | 45.3 ms: 1.03x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 17.3 ms: 1.01x faster                                                           |
| sympy_expand               | 398 ms                                                          | 399 ms: 1.00x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 101 ms: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                          | 204 ms: 1.02x slower                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 49.9 ms: 1.03x slower                                                           |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                            |
| docutils                   | 1.98 sec                                                        | 2.06 sec: 1.04x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 8.14 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.5 ms: 1.10x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.11x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.33 ms: 1.15x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| json                       | 4.15 ms                                                         | 5.02 ms: 1.21x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 94.1 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.82x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_parse, async_generators
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown