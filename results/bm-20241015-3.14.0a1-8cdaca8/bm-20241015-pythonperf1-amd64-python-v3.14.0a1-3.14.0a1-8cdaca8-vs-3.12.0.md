# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: windows-amd64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.032x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                            |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                          |
| tornado_http   | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                       | 1.05x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 215 ms: 1.33x faster                                            |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                            |
| async_tree_io              | 731 ms                                                      | 574 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 407 ms: 1.23x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 645 ms: 1.20x faster                                            |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| float          | 56.8 ms                                                     | 55.6 ms: 1.02x faster                                           |
| nbody          | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| regex_compile  | 87.5 ms                                                     | 91.1 ms: 1.04x slower                                           |
| regex_v8       | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                           |
| xml_etree_parse      | 93.0 ms                                                     | 95.4 ms: 1.03x slower                                           |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                           |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                           |
| xml_etree_generate   | 55.8 ms                                                     | 59.3 ms: 1.06x slower                                           |
| pickle_list          | 2.83 us                                                     | 3.00 us: 1.06x slower                                           |
| unpickle             | 8.18 us                                                     | 9.00 us: 1.10x slower                                           |
| xml_etree_process    | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                           |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                            |
| json_loads           | 13.9 us                                                     | 15.5 us: 1.12x slower                                           |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.14x slower                                            |
| tomli_loads          | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                          |
| json_dumps           | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                           |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                           |
| python_startup         | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                           |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                           |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                           |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 266 ms: 1.38x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.53 sec: 1.37x faster                                          |
| async_tree_none_tg         | 285 ms                                                      | 215 ms: 1.33x faster                                            |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                            |
| async_tree_io              | 731 ms                                                      | 574 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 407 ms: 1.23x faster                                            |
| deepcopy                   | 238 us                                                      | 194 us: 1.23x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 281 ms: 1.21x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 645 ms: 1.20x faster                                            |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 20.4 us: 1.16x faster                                           |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                           |
| mako                       | 7.09 ms                                                     | 6.73 ms: 1.05x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                           |
| go                         | 91.6 ms                                                     | 88.5 ms: 1.03x faster                                           |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                            |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| float                      | 56.8 ms                                                     | 55.6 ms: 1.02x faster                                           |
| generators                 | 22.5 ms                                                     | 22.1 ms: 1.02x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 43.6 ms: 1.02x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 90.9 ms: 1.01x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                           |
| nqueens                    | 62.8 ms                                                     | 63.9 ms: 1.02x slower                                           |
| logging_format             | 6.72 us                                                     | 6.85 us: 1.02x slower                                           |
| logging_simple             | 6.28 us                                                     | 6.42 us: 1.02x slower                                           |
| xml_etree_parse            | 93.0 ms                                                     | 95.4 ms: 1.03x slower                                           |
| chaos                      | 43.3 ms                                                     | 44.6 ms: 1.03x slower                                           |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                           |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                            |
| meteor_contest             | 74.6 ms                                                     | 77.0 ms: 1.03x slower                                           |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                            |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                           |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                          |
| crypto_pyaes               | 48.5 ms                                                     | 50.3 ms: 1.04x slower                                           |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                            |
| logging_silent             | 60.5 ns                                                     | 62.9 ns: 1.04x slower                                           |
| regex_compile              | 87.5 ms                                                     | 91.1 ms: 1.04x slower                                           |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                           |
| tornado_http               | 89.5 ms                                                     | 93.8 ms: 1.05x slower                                           |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                           |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                            |
| xml_etree_generate         | 55.8 ms                                                     | 59.3 ms: 1.06x slower                                           |
| sqlglot_normalize          | 187 ms                                                      | 199 ms: 1.06x slower                                            |
| pickle_list                | 2.83 us                                                     | 3.00 us: 1.06x slower                                           |
| scimark_lu                 | 58.9 ms                                                     | 63.2 ms: 1.07x slower                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 37.2 ms: 1.08x slower                                           |
| pycparser                  | 699 ms                                                      | 756 ms: 1.08x slower                                            |
| spectral_norm              | 66.9 ms                                                     | 72.9 ms: 1.09x slower                                           |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                           |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                          |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                          |
| scimark_fft                | 184 ms                                                      | 202 ms: 1.09x slower                                            |
| unpickle                   | 8.18 us                                                     | 9.00 us: 1.10x slower                                           |
| pprint_safe_repr           | 513 ms                                                      | 565 ms: 1.10x slower                                            |
| sympy_expand               | 284 ms                                                      | 312 ms: 1.10x slower                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.2 ms: 1.10x slower                                           |
| nbody                      | 71.9 ms                                                     | 79.3 ms: 1.10x slower                                           |
| xml_etree_process          | 37.7 ms                                                     | 41.7 ms: 1.11x slower                                           |
| pyflate                    | 295 ms                                                      | 327 ms: 1.11x slower                                            |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                            |
| json_loads                 | 13.9 us                                                     | 15.5 us: 1.12x slower                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.12x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.3 ms: 1.12x slower                                           |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                           |
| richards                   | 28.4 ms                                                     | 32.3 ms: 1.14x slower                                           |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.14x slower                                            |
| unpack_sequence            | 37.5 ns                                                     | 42.7 ns: 1.14x slower                                           |
| sqlglot_parse              | 804 us                                                      | 921 us: 1.15x slower                                            |
| richards_super             | 32.1 ms                                                     | 36.8 ms: 1.15x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 16.5 ms: 1.16x slower                                           |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                            |
| tomli_loads                | 1.37 sec                                                    | 1.61 sec: 1.18x slower                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                            |
| scimark_sor                | 78.8 ms                                                     | 93.2 ms: 1.18x slower                                           |
| telco                      | 4.13 ms                                                     | 4.89 ms: 1.19x slower                                           |
| coverage                   | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                           |
| bench_mp_pool              | 69.2 ms                                                     | 84.0 ms: 1.21x slower                                           |
| json_dumps                 | 5.70 ms                                                     | 6.93 ms: 1.22x slower                                           |
| python_startup             | 19.5 ms                                                     | 24.6 ms: 1.26x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 1.97 ms: 1.29x slower                                           |
| asyncio_tcp                | 487 ms                                                      | 661 ms: 1.36x slower                                            |
| create_gc_cycles           | 752 us                                                      | 1.41 ms: 1.88x slower                                           |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                    |

Benchmark hidden because not significant (2): pickle, pathlib
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.032x slower
# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown