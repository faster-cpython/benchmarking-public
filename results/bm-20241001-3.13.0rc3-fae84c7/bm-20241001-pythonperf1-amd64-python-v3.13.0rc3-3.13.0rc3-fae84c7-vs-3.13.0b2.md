# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc3
- machine: windows-amd64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 216 ms: 1.05x slower                                              |
| chameleon      | 4.80 ms                                                         | 4.89 ms: 1.02x slower                                             |
| docutils       | 1.63 sec                                                        | 1.56 sec: 1.04x faster                                            |
| html5lib       | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                             |
| tornado_http   | 81.8 ms                                                         | 92.2 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                           | 1.06x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 506 ms: 1.20x faster                                              |
| async_tree_io              | 588 ms                                                          | 516 ms: 1.14x faster                                              |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 374 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 370 ms: 1.03x faster                                              |
| async_tree_memoization_tg  | 258 ms                                                          | 286 ms: 1.11x slower                                              |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                      |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 50.3 ms: 1.01x slower                                             |
| nbody          | 67.6 ms                                                         | 71.0 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                           | 1.02x slower                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                             |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                              |
| regex_compile  | 78.0 ms                                                         | 83.8 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_iterparse  | 62.3 ms                                                         | 61.1 ms: 1.02x faster                                             |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                             |
| xml_etree_process    | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                             |
| unpickle             | 8.40 us                                                         | 8.49 us: 1.01x slower                                             |
| pickle               | 7.11 us                                                         | 7.21 us: 1.01x slower                                             |
| unpickle_list        | 2.62 us                                                         | 2.66 us: 1.02x slower                                             |
| tomli_loads          | 1.35 sec                                                        | 1.39 sec: 1.03x slower                                            |
| json_dumps           | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                             |
| pickle_dict          | 18.1 us                                                         | 18.8 us: 1.04x slower                                             |
| pickle_pure_python   | 175 us                                                          | 183 us: 1.05x slower                                              |
| unpickle_pure_python | 122 us                                                          | 130 us: 1.07x slower                                              |
| pickle_list          | 2.90 us                                                         | 3.11 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.10x slower                                             |
| python_startup         | 20.3 ms                                                         | 22.4 ms: 1.10x slower                                             |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                             |
| mako            | 6.36 ms                                                         | 6.68 ms: 1.05x slower                                             |
| genshi_text     | 14.4 ms                                                         | 15.5 ms: 1.08x slower                                             |
| genshi_xml      | 31.6 ms                                                         | 34.3 ms: 1.09x slower                                             |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 506 ms: 1.20x faster                                              |
| async_tree_io              | 588 ms                                                          | 516 ms: 1.14x faster                                              |
| create_gc_cycles           | 888 us                                                          | 807 us: 1.10x faster                                              |
| json                       | 3.19 ms                                                         | 2.99 ms: 1.07x faster                                             |
| docutils                   | 1.63 sec                                                        | 1.56 sec: 1.04x faster                                            |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 374 ms: 1.04x faster                                              |
| spectral_norm              | 63.7 ms                                                         | 61.5 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 370 ms: 1.03x faster                                              |
| async_generators           | 223 ms                                                          | 219 ms: 1.02x faster                                              |
| xml_etree_iterparse        | 62.3 ms                                                         | 61.1 ms: 1.02x faster                                             |
| logging_format             | 6.22 us                                                         | 6.11 us: 1.02x faster                                             |
| logging_simple             | 5.78 us                                                         | 5.70 us: 1.01x faster                                             |
| telco                      | 4.67 ms                                                         | 4.61 ms: 1.01x faster                                             |
| richards                   | 26.7 ms                                                         | 26.4 ms: 1.01x faster                                             |
| richards_super             | 30.2 ms                                                         | 29.8 ms: 1.01x faster                                             |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                             |
| json_loads                 | 14.2 us                                                         | 14.0 us: 1.01x faster                                             |
| gc_traversal               | 1.55 ms                                                         | 1.55 ms: 1.01x faster                                             |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                              |
| nqueens                    | 56.7 ms                                                         | 56.9 ms: 1.00x slower                                             |
| crypto_pyaes               | 45.5 ms                                                         | 45.7 ms: 1.01x slower                                             |
| xml_etree_process          | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                             |
| pyflate                    | 279 ms                                                          | 281 ms: 1.01x slower                                              |
| typing_runtime_protocols   | 101 us                                                          | 102 us: 1.01x slower                                              |
| unpickle                   | 8.40 us                                                         | 8.49 us: 1.01x slower                                             |
| scimark_lu                 | 56.6 ms                                                         | 57.2 ms: 1.01x slower                                             |
| deltablue                  | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                             |
| fannkuch                   | 243 ms                                                          | 246 ms: 1.01x slower                                              |
| sqlglot_normalize          | 173 ms                                                          | 175 ms: 1.01x slower                                              |
| deepcopy_reduce            | 1.99 us                                                         | 2.02 us: 1.01x slower                                             |
| float                      | 49.7 ms                                                         | 50.3 ms: 1.01x slower                                             |
| pickle                     | 7.11 us                                                         | 7.21 us: 1.01x slower                                             |
| unpickle_list              | 2.62 us                                                         | 2.66 us: 1.02x slower                                             |
| raytrace                   | 162 ms                                                          | 165 ms: 1.02x slower                                              |
| sympy_integrate            | 12.2 ms                                                         | 12.4 ms: 1.02x slower                                             |
| chameleon                  | 4.80 ms                                                         | 4.89 ms: 1.02x slower                                             |
| django_template            | 21.7 ms                                                         | 22.1 ms: 1.02x slower                                             |
| scimark_sor                | 75.3 ms                                                         | 76.9 ms: 1.02x slower                                             |
| bench_thread_pool          | 768 us                                                          | 786 us: 1.02x slower                                              |
| sqlglot_optimize           | 32.7 ms                                                         | 33.5 ms: 1.02x slower                                             |
| sqlglot_transpile          | 955 us                                                          | 980 us: 1.03x slower                                              |
| generators                 | 19.6 ms                                                         | 20.1 ms: 1.03x slower                                             |
| deepcopy                   | 220 us                                                          | 226 us: 1.03x slower                                              |
| tomli_loads                | 1.35 sec                                                        | 1.39 sec: 1.03x slower                                            |
| sympy_sum                  | 84.4 ms                                                         | 86.8 ms: 1.03x slower                                             |
| json_dumps                 | 5.61 ms                                                         | 5.78 ms: 1.03x slower                                             |
| chaos                      | 38.4 ms                                                         | 39.5 ms: 1.03x slower                                             |
| mypy2                      | 418 ms                                                          | 431 ms: 1.03x slower                                              |
| coroutines                 | 12.8 ms                                                         | 13.1 ms: 1.03x slower                                             |
| scimark_fft                | 171 ms                                                          | 176 ms: 1.03x slower                                              |
| deepcopy_memo              | 22.1 us                                                         | 22.8 us: 1.03x slower                                             |
| hexiom                     | 3.72 ms                                                         | 3.85 ms: 1.03x slower                                             |
| pickle_dict                | 18.1 us                                                         | 18.8 us: 1.04x slower                                             |
| pprint_safe_repr           | 474 ms                                                          | 492 ms: 1.04x slower                                              |
| mdp                        | 1.31 sec                                                        | 1.36 sec: 1.04x slower                                            |
| pprint_pformat             | 966 ms                                                          | 1.00 sec: 1.04x slower                                            |
| go                         | 82.1 ms                                                         | 85.4 ms: 1.04x slower                                             |
| pickle_pure_python         | 175 us                                                          | 183 us: 1.05x slower                                              |
| pathlib                    | 75.9 ms                                                         | 79.3 ms: 1.05x slower                                             |
| 2to3                       | 207 ms                                                          | 216 ms: 1.05x slower                                              |
| nbody                      | 67.6 ms                                                         | 71.0 ms: 1.05x slower                                             |
| mako                       | 6.36 ms                                                         | 6.68 ms: 1.05x slower                                             |
| scimark_monte_carlo        | 39.1 ms                                                         | 41.1 ms: 1.05x slower                                             |
| sympy_str                  | 159 ms                                                          | 167 ms: 1.05x slower                                              |
| sympy_expand               | 271 ms                                                          | 285 ms: 1.05x slower                                              |
| sqlglot_parse              | 748 us                                                          | 789 us: 1.05x slower                                              |
| meteor_contest             | 69.9 ms                                                         | 73.9 ms: 1.06x slower                                             |
| unpickle_pure_python       | 122 us                                                          | 130 us: 1.07x slower                                              |
| aiohttp                    | 889 us                                                          | 950 us: 1.07x slower                                              |
| pickle_list                | 2.90 us                                                         | 3.11 us: 1.07x slower                                             |
| bench_mp_pool              | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                             |
| thrift                     | 8.11 ms                                                         | 8.70 ms: 1.07x slower                                             |
| regex_compile              | 78.0 ms                                                         | 83.8 ms: 1.07x slower                                             |
| genshi_text                | 14.4 ms                                                         | 15.5 ms: 1.08x slower                                             |
| genshi_xml                 | 31.6 ms                                                         | 34.3 ms: 1.09x slower                                             |
| dulwich_log                | 38.0 ms                                                         | 41.4 ms: 1.09x slower                                             |
| coverage                   | 42.1 ms                                                         | 45.9 ms: 1.09x slower                                             |
| asyncio_tcp                | 471 ms                                                          | 517 ms: 1.10x slower                                              |
| python_startup_no_site     | 16.2 ms                                                         | 17.9 ms: 1.10x slower                                             |
| python_startup             | 20.3 ms                                                         | 22.4 ms: 1.10x slower                                             |
| async_tree_memoization_tg  | 258 ms                                                          | 286 ms: 1.11x slower                                              |
| tornado_http               | 81.8 ms                                                         | 92.2 ms: 1.13x slower                                             |
| html5lib                   | 35.0 ms                                                         | 40.2 ms: 1.15x slower                                             |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                      |

Benchmark hidden because not significant (15): asyncio_tcp_ssl, xml_etree_generate, scimark_sparse_mat_mult, xml_etree_parse, flaskblogging, pidigits, sqlite_synth, logging_silent, async_tree_none_tg, pycparser, comprehensions, async_tree_none, pylint, async_tree_memoization, regex_v8
Ignored benchmarks (1) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1-amd64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown