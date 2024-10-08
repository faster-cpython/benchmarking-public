# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 210 ms: 1.02x slower                                            |
| chameleon      | 4.80 ms                                                         | 4.91 ms: 1.02x slower                                           |
| docutils       | 1.63 sec                                                        | 1.53 sec: 1.06x faster                                          |
| html5lib       | 35.0 ms                                                         | 35.9 ms: 1.03x slower                                           |
| tornado_http   | 81.8 ms                                                         | 85.5 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 389 ms                                                          | 448 ms: 1.15x slower                                            |
| async_tree_none            | 218 ms                                                          | 263 ms: 1.21x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 465 ms: 1.22x slower                                            |
| async_tree_io              | 588 ms                                                          | 724 ms: 1.23x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 750 ms: 1.24x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 270 ms: 1.34x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| Geometric mean             | (ref)                                                           | 1.25x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| float          | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                           |
| nbody          | 67.6 ms                                                         | 74.1 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 13.7 us: 1.04x faster                                           |
| json_dumps           | 5.61 ms                                                         | 5.54 ms: 1.01x faster                                           |
| pickle_dict          | 18.1 us                                                         | 18.2 us: 1.00x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 53.6 ms: 1.01x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                           |
| pickle_pure_python   | 175 us                                                          | 179 us: 1.02x slower                                            |
| xml_etree_parse      | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                           |
| pickle               | 7.11 us                                                         | 7.31 us: 1.03x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.39 sec: 1.03x slower                                          |
| unpickle_list        | 2.62 us                                                         | 2.73 us: 1.04x slower                                           |
| unpickle_pure_python | 122 us                                                          | 128 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (3): pickle_list, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                           |
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.4 ms: 1.01x faster                                           |
| mako            | 6.36 ms                                                         | 6.57 ms: 1.03x slower                                           |
| genshi_text     | 14.4 ms                                                         | 16.1 ms: 1.12x slower                                           |
| genshi_xml      | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                           |
| Geometric mean  | (ref)                                                           | 1.07x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols   | 101 us                                                          | 70.5 us: 1.43x faster                                           |
| create_gc_cycles           | 888 us                                                          | 732 us: 1.21x faster                                            |
| json                       | 3.19 ms                                                         | 2.88 ms: 1.11x faster                                           |
| pycparser                  | 754 ms                                                          | 701 ms: 1.07x faster                                            |
| crypto_pyaes               | 45.5 ms                                                         | 42.8 ms: 1.06x faster                                           |
| docutils                   | 1.63 sec                                                        | 1.53 sec: 1.06x faster                                          |
| json_loads                 | 14.2 us                                                         | 13.7 us: 1.04x faster                                           |
| deepcopy_reduce            | 1.99 us                                                         | 1.93 us: 1.04x faster                                           |
| spectral_norm              | 63.7 ms                                                         | 61.6 ms: 1.03x faster                                           |
| scimark_lu                 | 56.6 ms                                                         | 54.9 ms: 1.03x faster                                           |
| gc_traversal               | 1.55 ms                                                         | 1.52 ms: 1.03x faster                                           |
| mypy2                      | 418 ms                                                          | 409 ms: 1.02x faster                                            |
| sympy_sum                  | 84.4 ms                                                         | 82.6 ms: 1.02x faster                                           |
| sqlite_synth               | 1.60 us                                                         | 1.57 us: 1.02x faster                                           |
| sympy_str                  | 159 ms                                                          | 156 ms: 1.02x faster                                            |
| pidigits                   | 150 ms                                                          | 148 ms: 1.02x faster                                            |
| django_template            | 21.7 ms                                                         | 21.4 ms: 1.01x faster                                           |
| json_dumps                 | 5.61 ms                                                         | 5.54 ms: 1.01x faster                                           |
| comprehensions             | 10.4 us                                                         | 10.3 us: 1.01x faster                                           |
| python_startup             | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                           |
| sympy_expand               | 271 ms                                                          | 268 ms: 1.01x faster                                            |
| raytrace                   | 162 ms                                                          | 161 ms: 1.01x faster                                            |
| pickle_dict                | 18.1 us                                                         | 18.2 us: 1.00x slower                                           |
| fannkuch                   | 243 ms                                                          | 245 ms: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.52 ms: 1.01x slower                                           |
| aiohttp                    | 889 us                                                          | 896 us: 1.01x slower                                            |
| sqlglot_optimize           | 32.7 ms                                                         | 33.0 ms: 1.01x slower                                           |
| xml_etree_generate         | 53.2 ms                                                         | 53.6 ms: 1.01x slower                                           |
| sqlglot_normalize          | 173 ms                                                          | 175 ms: 1.01x slower                                            |
| deepcopy                   | 220 us                                                          | 223 us: 1.01x slower                                            |
| sqlglot_parse              | 748 us                                                          | 761 us: 1.02x slower                                            |
| async_generators           | 223 ms                                                          | 227 ms: 1.02x slower                                            |
| 2to3                       | 207 ms                                                          | 210 ms: 1.02x slower                                            |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                            |
| coroutines                 | 12.8 ms                                                         | 13.0 ms: 1.02x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                           |
| pickle_pure_python         | 175 us                                                          | 179 us: 1.02x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 39.9 ms: 1.02x slower                                           |
| richards_super             | 30.2 ms                                                         | 30.8 ms: 1.02x slower                                           |
| logging_silent             | 52.9 ns                                                         | 54.1 ns: 1.02x slower                                           |
| telco                      | 4.67 ms                                                         | 4.77 ms: 1.02x slower                                           |
| xml_etree_parse            | 90.9 ms                                                         | 93.0 ms: 1.02x slower                                           |
| chameleon                  | 4.80 ms                                                         | 4.91 ms: 1.02x slower                                           |
| hexiom                     | 3.72 ms                                                         | 3.82 ms: 1.02x slower                                           |
| richards                   | 26.7 ms                                                         | 27.4 ms: 1.02x slower                                           |
| thrift                     | 8.11 ms                                                         | 8.32 ms: 1.03x slower                                           |
| html5lib                   | 35.0 ms                                                         | 35.9 ms: 1.03x slower                                           |
| pickle                     | 7.11 us                                                         | 7.31 us: 1.03x slower                                           |
| sqlglot_transpile          | 955 us                                                          | 981 us: 1.03x slower                                            |
| bench_mp_pool              | 64.8 ms                                                         | 66.6 ms: 1.03x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 71.9 ms: 1.03x slower                                           |
| chaos                      | 38.4 ms                                                         | 39.5 ms: 1.03x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.39 sec: 1.03x slower                                          |
| mako                       | 6.36 ms                                                         | 6.57 ms: 1.03x slower                                           |
| pyflate                    | 279 ms                                                          | 288 ms: 1.03x slower                                            |
| scimark_sor                | 75.3 ms                                                         | 78.0 ms: 1.03x slower                                           |
| go                         | 82.1 ms                                                         | 84.9 ms: 1.04x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 491 ms: 1.04x slower                                            |
| logging_format             | 6.22 us                                                         | 6.47 us: 1.04x slower                                           |
| pprint_pformat             | 966 ms                                                          | 1.00 sec: 1.04x slower                                          |
| unpickle_list              | 2.62 us                                                         | 2.73 us: 1.04x slower                                           |
| scimark_fft                | 171 ms                                                          | 178 ms: 1.04x slower                                            |
| logging_simple             | 5.78 us                                                         | 6.04 us: 1.04x slower                                           |
| tornado_http               | 81.8 ms                                                         | 85.5 ms: 1.05x slower                                           |
| pathlib                    | 75.9 ms                                                         | 79.3 ms: 1.05x slower                                           |
| nqueens                    | 56.7 ms                                                         | 59.3 ms: 1.05x slower                                           |
| deltablue                  | 1.88 ms                                                         | 1.97 ms: 1.05x slower                                           |
| unpickle_pure_python       | 122 us                                                          | 128 us: 1.05x slower                                            |
| coverage                   | 42.1 ms                                                         | 44.3 ms: 1.05x slower                                           |
| float                      | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                           |
| mdp                        | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                          |
| dulwich_log                | 38.0 ms                                                         | 41.1 ms: 1.08x slower                                           |
| bench_thread_pool          | 768 us                                                          | 839 us: 1.09x slower                                            |
| nbody                      | 67.6 ms                                                         | 74.1 ms: 1.10x slower                                           |
| python_startup_no_site     | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                           |
| genshi_text                | 14.4 ms                                                         | 16.1 ms: 1.12x slower                                           |
| generators                 | 19.6 ms                                                         | 22.1 ms: 1.13x slower                                           |
| genshi_xml                 | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                           |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 448 ms: 1.15x slower                                            |
| async_tree_none            | 218 ms                                                          | 263 ms: 1.21x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 465 ms: 1.22x slower                                            |
| async_tree_io              | 588 ms                                                          | 724 ms: 1.23x slower                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.83 sec: 1.24x slower                                          |
| async_tree_io_tg           | 605 ms                                                          | 750 ms: 1.24x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 341 ms: 1.29x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 270 ms: 1.34x slower                                            |
| async_tree_memoization_tg  | 258 ms                                                          | 349 ms: 1.35x slower                                            |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (11): regex_v8, asyncio_tcp, pickle_list, regex_compile, xml_etree_process, flaskblogging, regex_effbot, sympy_integrate, unpickle, pylint, deepcopy_memo

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown