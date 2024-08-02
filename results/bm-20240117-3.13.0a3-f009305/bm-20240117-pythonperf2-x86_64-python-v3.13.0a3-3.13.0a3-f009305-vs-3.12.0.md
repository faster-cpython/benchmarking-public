# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.01x slower
- HPT reliability: 96.41%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 294 ms: 1.03x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.26 ms: 1.00x slower                                            |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none  | 452 ms                                                       | 435 ms: 1.04x faster                                             |
| async_tree_io_tg | 1.05 sec                                                     | 1.07 sec: 1.02x slower                                           |
| async_tree_io    | 1.04 sec                                                     | 1.08 sec: 1.03x slower                                           |
| Geometric mean   | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                            |
| pidigits       | 265 ms                                                       | 263 ms: 1.01x faster                                             |
| float          | 76.6 ms                                                      | 78.0 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                             |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                            |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                             |
| pickle               | 10.5 us                                                      | 10.4 us: 1.02x faster                                            |
| xml_etree_generate   | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                            |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                            |
| pickle_list          | 4.43 us                                                      | 4.49 us: 1.01x slower                                            |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.01x slower                                             |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.23 sec: 1.03x slower                                           |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                            |
| unpickle_list        | 4.66 us                                                      | 4.82 us: 1.03x slower                                            |
| xml_etree_iterparse  | 103 ms                                                       | 107 ms: 1.04x slower                                             |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.6 ms: 1.08x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.0 ms: 1.27x slower                                            |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                            |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 152 us                                                       | 113 us: 1.34x faster                                             |
| comprehensions           | 21.9 us                                                      | 16.5 us: 1.33x faster                                            |
| crypto_pyaes             | 80.3 ms                                                      | 71.4 ms: 1.12x faster                                            |
| raytrace                 | 298 ms                                                       | 265 ms: 1.12x faster                                             |
| generators               | 37.4 ms                                                      | 33.8 ms: 1.11x faster                                            |
| chaos                    | 64.0 ms                                                      | 59.9 ms: 1.07x faster                                            |
| async_generators         | 390 ms                                                       | 368 ms: 1.06x faster                                             |
| sympy_sum                | 162 ms                                                       | 154 ms: 1.05x faster                                             |
| bench_mp_pool            | 4.76 ms                                                      | 4.57 ms: 1.04x faster                                            |
| async_tree_none          | 452 ms                                                       | 435 ms: 1.04x faster                                             |
| pickle_pure_python       | 318 us                                                       | 307 us: 1.04x faster                                             |
| nbody                    | 88.0 ms                                                      | 85.3 ms: 1.03x faster                                            |
| tornado_http             | 121 ms                                                       | 118 ms: 1.03x faster                                             |
| sympy_str                | 302 ms                                                       | 294 ms: 1.03x faster                                             |
| coroutines               | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                            |
| deepcopy_reduce          | 3.37 us                                                      | 3.28 us: 1.03x faster                                            |
| mdp                      | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                           |
| sympy_integrate          | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                            |
| logging_format           | 7.48 us                                                      | 7.31 us: 1.02x faster                                            |
| regex_compile            | 144 ms                                                       | 141 ms: 1.02x faster                                             |
| asyncio_tcp              | 378 ms                                                       | 371 ms: 1.02x faster                                             |
| regex_effbot             | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                            |
| pickle                   | 10.5 us                                                      | 10.4 us: 1.02x faster                                            |
| scimark_monte_carlo      | 69.0 ms                                                      | 67.9 ms: 1.02x faster                                            |
| docutils                 | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| create_gc_cycles         | 1.59 ms                                                      | 1.57 ms: 1.01x faster                                            |
| asyncio_tcp_ssl          | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                           |
| scimark_lu               | 98.8 ms                                                      | 97.8 ms: 1.01x faster                                            |
| nqueens                  | 89.9 ms                                                      | 89.1 ms: 1.01x faster                                            |
| logging_simple           | 6.71 us                                                      | 6.66 us: 1.01x faster                                            |
| pidigits                 | 265 ms                                                       | 263 ms: 1.01x faster                                             |
| xml_etree_generate       | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                            |
| chameleon                | 7.23 ms                                                      | 7.26 ms: 1.00x slower                                            |
| django_template          | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                            |
| xml_etree_process        | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                            |
| sqlglot_transpile        | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                            |
| pprint_safe_repr         | 807 ms                                                       | 813 ms: 1.01x slower                                             |
| spectral_norm            | 91.6 ms                                                      | 92.3 ms: 1.01x slower                                            |
| deepcopy_memo            | 36.8 us                                                      | 37.1 us: 1.01x slower                                            |
| sqlglot_parse            | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| meteor_contest           | 128 ms                                                       | 130 ms: 1.01x slower                                             |
| pickle_list              | 4.43 us                                                      | 4.49 us: 1.01x slower                                            |
| unpickle_pure_python     | 210 us                                                       | 213 us: 1.01x slower                                             |
| async_tree_io_tg         | 1.05 sec                                                     | 1.07 sec: 1.02x slower                                           |
| logging_silent           | 94.4 ns                                                      | 96.0 ns: 1.02x slower                                            |
| float                    | 76.6 ms                                                      | 78.0 ms: 1.02x slower                                            |
| sympy_expand             | 484 ms                                                       | 494 ms: 1.02x slower                                             |
| asyncio_websockets       | 387 ms                                                       | 395 ms: 1.02x slower                                             |
| json_loads               | 24.4 us                                                      | 25.0 us: 1.02x slower                                            |
| sqlglot_optimize         | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                            |
| json                     | 5.12 ms                                                      | 5.27 ms: 1.03x slower                                            |
| 2to3                     | 285 ms                                                       | 294 ms: 1.03x slower                                             |
| mako                     | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                            |
| tomli_loads              | 2.16 sec                                                     | 2.23 sec: 1.03x slower                                           |
| json_dumps               | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                            |
| async_tree_io            | 1.04 sec                                                     | 1.08 sec: 1.03x slower                                           |
| unpickle_list            | 4.66 us                                                      | 4.82 us: 1.03x slower                                            |
| xml_etree_iterparse      | 103 ms                                                       | 107 ms: 1.04x slower                                             |
| unpickle                 | 14.8 us                                                      | 15.4 us: 1.04x slower                                            |
| xml_etree_parse          | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| dulwich_log              | 65.4 ms                                                      | 68.2 ms: 1.04x slower                                            |
| aiohttp                  | 1.02 ms                                                      | 1.06 ms: 1.04x slower                                            |
| gunicorn                 | 1.00 ms                                                      | 1.05 ms: 1.05x slower                                            |
| pycparser                | 1.23 sec                                                     | 1.32 sec: 1.07x slower                                           |
| python_startup           | 11.6 ms                                                      | 12.6 ms: 1.08x slower                                            |
| hexiom                   | 5.96 ms                                                      | 6.46 ms: 1.08x slower                                            |
| deltablue                | 3.24 ms                                                      | 3.54 ms: 1.09x slower                                            |
| regex_v8                 | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| fannkuch                 | 350 ms                                                       | 386 ms: 1.10x slower                                             |
| go                       | 150 ms                                                       | 166 ms: 1.11x slower                                             |
| gc_traversal             | 3.48 ms                                                      | 3.94 ms: 1.13x slower                                            |
| pyflate                  | 439 ms                                                       | 501 ms: 1.14x slower                                             |
| richards_super           | 51.3 ms                                                      | 59.4 ms: 1.16x slower                                            |
| richards                 | 45.7 ms                                                      | 53.7 ms: 1.17x slower                                            |
| telco                    | 6.96 ms                                                      | 8.23 ms: 1.18x slower                                            |
| coverage                 | 66.7 ms                                                      | 82.9 ms: 1.24x slower                                            |
| python_startup_no_site   | 8.64 ms                                                      | 11.0 ms: 1.27x slower                                            |
| scimark_sor              | 109 ms                                                       | 144 ms: 1.32x slower                                             |
| Geometric mean           | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (16): deepcopy, pickle_dict, regex_dna, async_tree_none_tg, sqlite_synth, pathlib, sqlglot_normalize, scimark_sparse_mat_mult, pprint_pformat, scimark_fft, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, bench_thread_pool, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.41% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.89x