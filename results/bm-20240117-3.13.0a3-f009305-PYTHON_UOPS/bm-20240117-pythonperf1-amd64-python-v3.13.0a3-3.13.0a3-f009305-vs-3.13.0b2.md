# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 217 ms: 1.05x slower                                            |
| chameleon      | 4.80 ms                                                         | 5.10 ms: 1.06x slower                                           |
| docutils       | 1.63 sec                                                        | 1.59 sec: 1.02x faster                                          |
| tornado_http   | 81.8 ms                                                         | 88.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 450 ms: 1.16x slower                                            |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 469 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 722 ms: 1.23x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 748 ms: 1.24x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 275 ms: 1.36x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 354 ms: 1.37x slower                                            |
| Geometric mean             | (ref)                                                           | 1.26x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| float          | 49.7 ms                                                         | 55.5 ms: 1.12x slower                                           |
| nbody          | 67.6 ms                                                         | 79.2 ms: 1.17x slower                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                           |
| regex_dna      | 119 ms                                                          | 122 ms: 1.02x slower                                            |
| regex_compile  | 78.0 ms                                                         | 84.2 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.6 us: 1.05x faster                                           |
| unpickle             | 8.40 us                                                         | 8.21 us: 1.02x faster                                           |
| xml_etree_process    | 36.4 ms                                                         | 37.3 ms: 1.02x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                          |
| xml_etree_parse      | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                           |
| pickle_pure_python   | 175 us                                                          | 182 us: 1.04x slower                                            |
| pickle_dict          | 18.1 us                                                         | 18.8 us: 1.04x slower                                           |
| pickle               | 7.11 us                                                         | 7.37 us: 1.04x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 55.2 ms: 1.04x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.73 us: 1.04x slower                                           |
| pickle_list          | 2.90 us                                                         | 3.08 us: 1.06x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.5 ms: 1.08x slower                                           |
| unpickle_pure_python | 122 us                                                          | 137 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                           |
| python_startup_no_site | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 6.36 ms                                                         | 7.29 ms: 1.15x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 74.9 us: 1.35x faster                                           |
| create_gc_cycles           | 888 us                                                          | 738 us: 1.20x faster                                            |
| pycparser                  | 754 ms                                                          | 675 ms: 1.12x faster                                            |
| json_loads                 | 14.2 us                                                         | 13.6 us: 1.05x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.49 ms: 1.04x faster                                           |
| unpickle                   | 8.40 us                                                         | 8.21 us: 1.02x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.59 sec: 1.02x faster                                          |
| sqlite_synth               | 1.60 us                                                         | 1.57 us: 1.02x faster                                           |
| pidigits                   | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| scimark_lu                 | 56.6 ms                                                         | 56.9 ms: 1.01x slower                                           |
| richards_super             | 30.2 ms                                                         | 30.5 ms: 1.01x slower                                           |
| regex_effbot               | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                           |
| richards                   | 26.7 ms                                                         | 27.0 ms: 1.01x slower                                           |
| deepcopy_reduce            | 1.99 us                                                         | 2.02 us: 1.01x slower                                           |
| coroutines                 | 12.8 ms                                                         | 12.9 ms: 1.01x slower                                           |
| mypy2                      | 418 ms                                                          | 424 ms: 1.01x slower                                            |
| async_generators           | 223 ms                                                          | 227 ms: 1.02x slower                                            |
| python_startup             | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                           |
| regex_dna                  | 119 ms                                                          | 122 ms: 1.02x slower                                            |
| xml_etree_process          | 36.4 ms                                                         | 37.3 ms: 1.02x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.38 sec: 1.03x slower                                          |
| sympy_sum                  | 84.4 ms                                                         | 86.6 ms: 1.03x slower                                           |
| pathlib                    | 75.9 ms                                                         | 78.3 ms: 1.03x slower                                           |
| sympy_expand               | 271 ms                                                          | 279 ms: 1.03x slower                                            |
| xml_etree_parse            | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                           |
| bench_mp_pool              | 64.8 ms                                                         | 67.1 ms: 1.04x slower                                           |
| pickle_pure_python         | 175 us                                                          | 182 us: 1.04x slower                                            |
| pickle_dict                | 18.1 us                                                         | 18.8 us: 1.04x slower                                           |
| pickle                     | 7.11 us                                                         | 7.37 us: 1.04x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 55.2 ms: 1.04x slower                                           |
| sqlglot_parse              | 748 us                                                          | 778 us: 1.04x slower                                            |
| unpickle_list              | 2.62 us                                                         | 2.73 us: 1.04x slower                                           |
| sqlglot_normalize          | 173 ms                                                          | 180 ms: 1.04x slower                                            |
| sympy_str                  | 159 ms                                                          | 166 ms: 1.04x slower                                            |
| logging_silent             | 52.9 ns                                                         | 55.3 ns: 1.04x slower                                           |
| sqlglot_transpile          | 955 us                                                          | 1000 us: 1.05x slower                                           |
| deepcopy                   | 220 us                                                          | 230 us: 1.05x slower                                            |
| crypto_pyaes               | 45.5 ms                                                         | 47.7 ms: 1.05x slower                                           |
| 2to3                       | 207 ms                                                          | 217 ms: 1.05x slower                                            |
| generators                 | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                           |
| sqlglot_optimize           | 32.7 ms                                                         | 34.6 ms: 1.06x slower                                           |
| pickle_list                | 2.90 us                                                         | 3.08 us: 1.06x slower                                           |
| scimark_sor                | 75.3 ms                                                         | 79.9 ms: 1.06x slower                                           |
| chameleon                  | 4.80 ms                                                         | 5.10 ms: 1.06x slower                                           |
| sympy_integrate            | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                           |
| raytrace                   | 162 ms                                                          | 174 ms: 1.07x slower                                            |
| deepcopy_memo              | 22.1 us                                                         | 23.7 us: 1.07x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.23 us: 1.08x slower                                           |
| logging_format             | 6.22 us                                                         | 6.70 us: 1.08x slower                                           |
| tornado_http               | 81.8 ms                                                         | 88.2 ms: 1.08x slower                                           |
| regex_compile              | 78.0 ms                                                         | 84.2 ms: 1.08x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 67.5 ms: 1.08x slower                                           |
| fannkuch                   | 243 ms                                                          | 264 ms: 1.09x slower                                            |
| meteor_contest             | 69.9 ms                                                         | 76.2 ms: 1.09x slower                                           |
| coverage                   | 42.1 ms                                                         | 46.0 ms: 1.09x slower                                           |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.62 sec: 1.09x slower                                          |
| json                       | 3.19 ms                                                         | 3.52 ms: 1.11x slower                                           |
| go                         | 82.1 ms                                                         | 90.8 ms: 1.11x slower                                           |
| nqueens                    | 56.7 ms                                                         | 63.0 ms: 1.11x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 528 ms: 1.11x slower                                            |
| float                      | 49.7 ms                                                         | 55.5 ms: 1.12x slower                                           |
| dulwich_log                | 38.0 ms                                                         | 42.6 ms: 1.12x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                          |
| unpickle_pure_python       | 122 us                                                          | 137 us: 1.12x slower                                            |
| bench_thread_pool          | 768 us                                                          | 867 us: 1.13x slower                                            |
| pprint_pformat             | 966 ms                                                          | 1.09 sec: 1.13x slower                                          |
| python_startup_no_site     | 16.2 ms                                                         | 18.5 ms: 1.14x slower                                           |
| mako                       | 6.36 ms                                                         | 7.29 ms: 1.15x slower                                           |
| chaos                      | 38.4 ms                                                         | 44.0 ms: 1.15x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 450 ms: 1.16x slower                                            |
| pyflate                    | 279 ms                                                          | 323 ms: 1.16x slower                                            |
| nbody                      | 67.6 ms                                                         | 79.2 ms: 1.17x slower                                           |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.95 ms: 1.18x slower                                           |
| scimark_fft                | 171 ms                                                          | 203 ms: 1.19x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 47.5 ms: 1.21x slower                                           |
| async_tree_none            | 218 ms                                                          | 266 ms: 1.22x slower                                            |
| comprehensions             | 10.4 us                                                         | 12.7 us: 1.22x slower                                           |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 469 ms: 1.23x slower                                            |
| async_tree_io              | 588 ms                                                          | 722 ms: 1.23x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 748 ms: 1.24x slower                                            |
| spectral_norm              | 63.7 ms                                                         | 79.9 ms: 1.25x slower                                           |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| hexiom                     | 3.72 ms                                                         | 4.82 ms: 1.30x slower                                           |
| async_tree_none_tg         | 202 ms                                                          | 275 ms: 1.36x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 354 ms: 1.37x slower                                            |
| deltablue                  | 1.88 ms                                                         | 2.60 ms: 1.38x slower                                           |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                    |

Benchmark hidden because not significant (4): regex_v8, asyncio_tcp, json_dumps, telco
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown