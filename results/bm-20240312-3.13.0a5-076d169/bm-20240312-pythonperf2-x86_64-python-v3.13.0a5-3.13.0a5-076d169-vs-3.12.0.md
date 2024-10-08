# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.01x slower
- HPT reliability: 98.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.28 ms: 1.01x slower                                            |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none           | 452 ms                                                       | 433 ms: 1.04x faster                                             |
| async_tree_none_tg        | 431 ms                                                       | 434 ms: 1.01x slower                                             |
| async_tree_memoization_tg | 540 ms                                                       | 546 ms: 1.01x slower                                             |
| async_tree_io_tg          | 1.05 sec                                                     | 1.07 sec: 1.02x slower                                           |
| async_tree_io             | 1.04 sec                                                     | 1.07 sec: 1.03x slower                                           |
| Geometric mean            | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| float          | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                            |
| nbody          | 88.0 ms                                                      | 91.5 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                             |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.0 us: 1.05x faster                                            |
| pickle_pure_python   | 318 us                                                       | 305 us: 1.04x faster                                             |
| pickle               | 10.5 us                                                      | 10.2 us: 1.04x faster                                            |
| unpickle_list        | 4.66 us                                                      | 4.56 us: 1.02x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                             |
| json_dumps           | 10.2 ms                                                      | 10.3 ms: 1.01x slower                                            |
| xml_etree_generate   | 86.1 ms                                                      | 87.7 ms: 1.02x slower                                            |
| pickle_list          | 4.43 us                                                      | 4.51 us: 1.02x slower                                            |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                             |
| xml_etree_process    | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                            |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                           |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.1 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                            |
| mako            | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions            | 21.9 us                                                      | 16.7 us: 1.32x faster                                            |
| typing_runtime_protocols  | 152 us                                                       | 116 us: 1.31x faster                                             |
| raytrace                  | 298 ms                                                       | 253 ms: 1.18x faster                                             |
| generators                | 37.4 ms                                                      | 33.1 ms: 1.13x faster                                            |
| crypto_pyaes              | 80.3 ms                                                      | 72.5 ms: 1.11x faster                                            |
| async_generators          | 390 ms                                                       | 366 ms: 1.07x faster                                             |
| sympy_sum                 | 162 ms                                                       | 152 ms: 1.06x faster                                             |
| bench_mp_pool             | 4.76 ms                                                      | 4.49 ms: 1.06x faster                                            |
| logging_format            | 7.48 us                                                      | 7.11 us: 1.05x faster                                            |
| pickle_dict               | 32.5 us                                                      | 31.0 us: 1.05x faster                                            |
| chaos                     | 64.0 ms                                                      | 61.1 ms: 1.05x faster                                            |
| scimark_lu                | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                            |
| async_tree_none           | 452 ms                                                       | 433 ms: 1.04x faster                                             |
| pickle_pure_python        | 318 us                                                       | 305 us: 1.04x faster                                             |
| logging_simple            | 6.71 us                                                      | 6.44 us: 1.04x faster                                            |
| pickle                    | 10.5 us                                                      | 10.2 us: 1.04x faster                                            |
| coroutines                | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                            |
| sympy_str                 | 302 ms                                                       | 293 ms: 1.03x faster                                             |
| sqlite_synth              | 2.77 us                                                      | 2.69 us: 1.03x faster                                            |
| mdp                       | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                           |
| sympy_integrate           | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                            |
| deepcopy_reduce           | 3.37 us                                                      | 3.29 us: 1.02x faster                                            |
| unpickle_list             | 4.66 us                                                      | 4.56 us: 1.02x faster                                            |
| docutils                  | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| pprint_pformat            | 1.65 sec                                                     | 1.63 sec: 1.01x faster                                           |
| nqueens                   | 89.9 ms                                                      | 88.7 ms: 1.01x faster                                            |
| pidigits                  | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| django_template           | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                            |
| regex_compile             | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| pprint_safe_repr          | 807 ms                                                       | 800 ms: 1.01x faster                                             |
| asyncio_websockets        | 387 ms                                                       | 384 ms: 1.01x faster                                             |
| regex_dna                 | 239 ms                                                       | 237 ms: 1.01x faster                                             |
| asyncio_tcp_ssl           | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| meteor_contest            | 128 ms                                                       | 129 ms: 1.01x slower                                             |
| deepcopy_memo             | 36.8 us                                                      | 37.0 us: 1.01x slower                                            |
| xml_etree_parse           | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| chameleon                 | 7.23 ms                                                      | 7.28 ms: 1.01x slower                                            |
| sqlglot_normalize         | 116 ms                                                       | 117 ms: 1.01x slower                                             |
| async_tree_none_tg        | 431 ms                                                       | 434 ms: 1.01x slower                                             |
| unpickle_pure_python      | 210 us                                                       | 211 us: 1.01x slower                                             |
| spectral_norm             | 91.6 ms                                                      | 92.4 ms: 1.01x slower                                            |
| sqlglot_parse             | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| logging_silent            | 94.4 ns                                                      | 95.3 ns: 1.01x slower                                            |
| json_dumps                | 10.2 ms                                                      | 10.3 ms: 1.01x slower                                            |
| async_tree_memoization_tg | 540 ms                                                       | 546 ms: 1.01x slower                                             |
| tornado_http              | 121 ms                                                       | 123 ms: 1.01x slower                                             |
| sqlglot_transpile         | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| deepcopy                  | 368 us                                                       | 373 us: 1.01x slower                                             |
| dask                      | 392 ms                                                       | 397 ms: 1.01x slower                                             |
| mako                      | 10.0 ms                                                      | 10.1 ms: 1.01x slower                                            |
| xml_etree_generate        | 86.1 ms                                                      | 87.7 ms: 1.02x slower                                            |
| pickle_list               | 4.43 us                                                      | 4.51 us: 1.02x slower                                            |
| scimark_fft               | 301 ms                                                       | 307 ms: 1.02x slower                                             |
| gc_traversal              | 3.48 ms                                                      | 3.55 ms: 1.02x slower                                            |
| async_tree_io_tg          | 1.05 sec                                                     | 1.07 sec: 1.02x slower                                           |
| xml_etree_iterparse       | 103 ms                                                       | 105 ms: 1.02x slower                                             |
| scimark_monte_carlo       | 69.0 ms                                                      | 70.6 ms: 1.02x slower                                            |
| 2to3                      | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| float                     | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                            |
| sqlglot_optimize          | 57.5 ms                                                      | 59.1 ms: 1.03x slower                                            |
| async_tree_io             | 1.04 sec                                                     | 1.07 sec: 1.03x slower                                           |
| xml_etree_process         | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                            |
| unpickle                  | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| bench_thread_pool         | 950 us                                                       | 979 us: 1.03x slower                                             |
| gunicorn                  | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                            |
| nbody                     | 88.0 ms                                                      | 91.5 ms: 1.04x slower                                            |
| sympy_expand              | 484 ms                                                       | 504 ms: 1.04x slower                                             |
| json                      | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                            |
| dulwich_log               | 65.4 ms                                                      | 68.8 ms: 1.05x slower                                            |
| tomli_loads               | 2.16 sec                                                     | 2.29 sec: 1.06x slower                                           |
| hexiom                    | 5.96 ms                                                      | 6.32 ms: 1.06x slower                                            |
| pycparser                 | 1.23 sec                                                     | 1.31 sec: 1.06x slower                                           |
| aiohttp                   | 1.02 ms                                                      | 1.09 ms: 1.07x slower                                            |
| python_startup            | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                            |
| regex_v8                  | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| deltablue                 | 3.24 ms                                                      | 3.56 ms: 1.10x slower                                            |
| go                        | 150 ms                                                       | 167 ms: 1.11x slower                                             |
| richards_super            | 51.3 ms                                                      | 57.5 ms: 1.12x slower                                            |
| richards                  | 45.7 ms                                                      | 51.2 ms: 1.12x slower                                            |
| fannkuch                  | 350 ms                                                       | 406 ms: 1.16x slower                                             |
| pyflate                   | 439 ms                                                       | 509 ms: 1.16x slower                                             |
| telco                     | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                            |
| coverage                  | 66.7 ms                                                      | 78.5 ms: 1.18x slower                                            |
| python_startup_no_site    | 8.64 ms                                                      | 11.1 ms: 1.28x slower                                            |
| scimark_sor               | 109 ms                                                       | 143 ms: 1.31x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (10): asyncio_tcp, pathlib, async_tree_memoization, scimark_sparse_mat_mult, regex_effbot, async_tree_cpu_io_mixed, json_loads, async_tree_cpu_io_mixed_tg, create_gc_cycles, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.89x