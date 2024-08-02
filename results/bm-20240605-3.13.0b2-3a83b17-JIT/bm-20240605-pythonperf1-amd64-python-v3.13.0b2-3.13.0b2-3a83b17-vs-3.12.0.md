# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: windows-amd64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.05x faster
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                            |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                          |
| tornado_http   | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.02x slower                                                    |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 215 ms: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                            |
| async_tree_none            | 291 ms                                                      | 227 ms: 1.28x faster                                            |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 624 ms: 1.24x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                            |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                           |
| float          | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                           |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                       | 1.21x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                           |
| regex_compile  | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 175 us: 1.11x faster                                            |
| tomli_loads          | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                          |
| xml_etree_generate   | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.2 ms: 1.07x faster                                           |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                           |
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                           |
| pickle               | 7.43 us                                                     | 7.27 us: 1.02x faster                                           |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                            |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                           |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                           |
| unpickle             | 8.18 us                                                     | 8.73 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                    |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                           |
| python_startup         | 19.5 ms                                                     | 22.7 ms: 1.17x slower                                           |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                           |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                           |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 45.3 ms: 1.48x faster                                           |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                          |
| mako                       | 7.09 ms                                                     | 5.13 ms: 1.38x faster                                           |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                           |
| nbody                      | 71.9 ms                                                     | 53.1 ms: 1.35x faster                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 215 ms: 1.33x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                            |
| async_tree_none            | 291 ms                                                      | 227 ms: 1.28x faster                                            |
| float                      | 56.8 ms                                                     | 44.3 ms: 1.28x faster                                           |
| async_tree_io              | 731 ms                                                      | 579 ms: 1.26x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 624 ms: 1.24x faster                                            |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                            |
| crypto_pyaes               | 48.5 ms                                                     | 41.5 ms: 1.17x faster                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.19 ms: 1.17x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.7 ms: 1.16x faster                                           |
| fannkuch                   | 247 ms                                                      | 215 ms: 1.15x faster                                            |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                            |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                           |
| pickle_pure_python         | 195 us                                                      | 175 us: 1.11x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 461 ms: 1.11x faster                                            |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                           |
| pprint_pformat             | 1.05 sec                                                    | 946 ms: 1.11x faster                                            |
| tomli_loads                | 1.37 sec                                                    | 1.24 sec: 1.11x faster                                          |
| dulwich_log                | 44.3 ms                                                     | 40.2 ms: 1.10x faster                                           |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                            |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                           |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                            |
| xml_etree_generate         | 55.8 ms                                                     | 51.4 ms: 1.09x faster                                           |
| bench_thread_pool          | 857 us                                                      | 793 us: 1.08x faster                                            |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.2 ms: 1.07x faster                                           |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                           |
| logging_simple             | 6.28 us                                                     | 5.91 us: 1.06x faster                                           |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                           |
| pathlib                    | 80.5 ms                                                     | 76.3 ms: 1.05x faster                                           |
| logging_format             | 6.72 us                                                     | 6.42 us: 1.05x faster                                           |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.04x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.69 us: 1.04x faster                                           |
| tornado_http               | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                           |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                           |
| nqueens                    | 62.8 ms                                                     | 61.4 ms: 1.02x faster                                           |
| pickle                     | 7.43 us                                                     | 7.27 us: 1.02x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.02x faster                                            |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                            |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                           |
| deepcopy                   | 238 us                                                      | 241 us: 1.01x slower                                            |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                           |
| regex_compile              | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                           |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                           |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                           |
| go                         | 91.6 ms                                                     | 93.8 ms: 1.02x slower                                           |
| sympy_sum                  | 91.5 ms                                                     | 93.9 ms: 1.03x slower                                           |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                            |
| bench_mp_pool              | 69.2 ms                                                     | 72.0 ms: 1.04x slower                                           |
| richards                   | 28.4 ms                                                     | 29.7 ms: 1.05x slower                                           |
| richards_super             | 32.1 ms                                                     | 33.5 ms: 1.05x slower                                           |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                            |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                            |
| scimark_sor                | 78.8 ms                                                     | 83.5 ms: 1.06x slower                                           |
| pycparser                  | 699 ms                                                      | 741 ms: 1.06x slower                                            |
| unpickle                   | 8.18 us                                                     | 8.73 us: 1.07x slower                                           |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                           |
| aiohttp                    | 884 us                                                      | 954 us: 1.08x slower                                            |
| telco                      | 4.13 ms                                                     | 4.46 ms: 1.08x slower                                           |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                           |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                           |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                          |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                           |
| coverage                   | 40.8 ms                                                     | 45.5 ms: 1.11x slower                                           |
| sympy_expand               | 284 ms                                                      | 317 ms: 1.12x slower                                            |
| python_startup_no_site     | 16.2 ms                                                     | 18.6 ms: 1.15x slower                                           |
| hexiom                     | 4.10 ms                                                     | 4.72 ms: 1.15x slower                                           |
| python_startup             | 19.5 ms                                                     | 22.7 ms: 1.17x slower                                           |
| scimark_lu                 | 58.9 ms                                                     | 69.4 ms: 1.18x slower                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                            |
| create_gc_cycles           | 752 us                                                      | 912 us: 1.21x slower                                            |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (7): mypy2, asyncio_tcp, sqlglot_parse, json_dumps, chameleon, pickle_list, regex_v8
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.06% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown