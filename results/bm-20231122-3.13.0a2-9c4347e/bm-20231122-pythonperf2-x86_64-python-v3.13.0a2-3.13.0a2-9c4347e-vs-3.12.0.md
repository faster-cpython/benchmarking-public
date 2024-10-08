# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x slower
- HPT reliability: 91.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.47 ms: 1.03x slower                                            |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 429 ms: 1.05x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 435 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 706 ms: 1.01x slower                                             |
| async_tree_io              | 1.04 sec                                                     | 1.07 sec: 1.03x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 556 ms: 1.03x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.03x slower                                           |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.9 ms: 1.05x faster                                            |
| float          | 76.6 ms                                                      | 80.9 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_effbot   | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                            |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle               | 10.5 us                                                      | 10.0 us: 1.05x faster                                            |
| pickle_pure_python   | 318 us                                                       | 308 us: 1.03x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 84.0 ms: 1.03x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.34 us: 1.02x faster                                            |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                            |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                            |
| xml_etree_iterparse  | 103 ms                                                       | 108 ms: 1.05x slower                                             |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 151 ms: 1.05x slower                                             |
| unpickle_pure_python | 210 us                                                       | 225 us: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (3): unpickle_list, tomli_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.3 ms: 1.31x slower                                            |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.8 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 16.6 us: 1.32x faster                                            |
| typing_runtime_protocols   | 152 us                                                       | 126 us: 1.21x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 71.7 ms: 1.12x faster                                            |
| raytrace                   | 298 ms                                                       | 271 ms: 1.10x faster                                             |
| generators                 | 37.4 ms                                                      | 34.2 ms: 1.09x faster                                            |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                             |
| async_generators           | 390 ms                                                       | 370 ms: 1.05x faster                                             |
| async_tree_none            | 452 ms                                                       | 429 ms: 1.05x faster                                             |
| pickle                     | 10.5 us                                                      | 10.0 us: 1.05x faster                                            |
| bench_mp_pool              | 4.76 ms                                                      | 4.54 ms: 1.05x faster                                            |
| nbody                      | 88.0 ms                                                      | 83.9 ms: 1.05x faster                                            |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                             |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                            |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                            |
| logging_format             | 7.48 us                                                      | 7.20 us: 1.04x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                            |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                            |
| pickle_pure_python         | 318 us                                                       | 308 us: 1.03x faster                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.27 us: 1.03x faster                                            |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                             |
| create_gc_cycles           | 1.59 ms                                                      | 1.55 ms: 1.03x faster                                            |
| xml_etree_generate         | 86.1 ms                                                      | 84.0 ms: 1.03x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                           |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| pickle_list                | 4.43 us                                                      | 4.34 us: 1.02x faster                                            |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                             |
| deepcopy                   | 368 us                                                       | 362 us: 1.02x faster                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.9 ms: 1.02x faster                                            |
| docutils                   | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                           |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                            |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                            |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                           |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                             |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                             |
| nqueens                    | 89.9 ms                                                      | 89.5 ms: 1.00x faster                                            |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                           |
| spectral_norm              | 91.6 ms                                                      | 92.3 ms: 1.01x slower                                            |
| sympy_expand               | 484 ms                                                       | 488 ms: 1.01x slower                                             |
| pathlib                    | 18.9 ms                                                      | 19.1 ms: 1.01x slower                                            |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| async_tree_none_tg         | 431 ms                                                       | 435 ms: 1.01x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 58.1 ms: 1.01x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 706 ms: 1.01x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| regex_effbot               | 3.57 ms                                                      | 3.63 ms: 1.02x slower                                            |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                            |
| django_template            | 38.2 ms                                                      | 38.8 ms: 1.02x slower                                            |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 37.6 us: 1.02x slower                                            |
| logging_silent             | 94.4 ns                                                      | 96.5 ns: 1.02x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                            |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| async_tree_io              | 1.04 sec                                                     | 1.07 sec: 1.03x slower                                           |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 556 ms: 1.03x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.03x slower                                           |
| chameleon                  | 7.23 ms                                                      | 7.47 ms: 1.03x slower                                            |
| aiohttp                    | 1.02 ms                                                      | 1.06 ms: 1.04x slower                                            |
| gunicorn                   | 1.00 ms                                                      | 1.05 ms: 1.05x slower                                            |
| xml_etree_iterparse        | 103 ms                                                       | 108 ms: 1.05x slower                                             |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 151 ms: 1.05x slower                                             |
| float                      | 76.6 ms                                                      | 80.9 ms: 1.06x slower                                            |
| pycparser                  | 1.23 sec                                                     | 1.31 sec: 1.06x slower                                           |
| hexiom                     | 5.96 ms                                                      | 6.35 ms: 1.07x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                            |
| fannkuch                   | 350 ms                                                       | 374 ms: 1.07x slower                                             |
| unpickle_pure_python       | 210 us                                                       | 225 us: 1.07x slower                                             |
| python_startup             | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.61 ms: 1.11x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 3.94 ms: 1.13x slower                                            |
| richards_super             | 51.3 ms                                                      | 58.3 ms: 1.13x slower                                            |
| richards                   | 45.7 ms                                                      | 52.1 ms: 1.14x slower                                            |
| go                         | 150 ms                                                       | 173 ms: 1.16x slower                                             |
| pyflate                    | 439 ms                                                       | 513 ms: 1.17x slower                                             |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                            |
| coverage                   | 66.7 ms                                                      | 79.1 ms: 1.19x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 11.3 ms: 1.31x slower                                            |
| scimark_sor                | 109 ms                                                       | 146 ms: 1.34x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, unpickle_list, scimark_sparse_mat_mult, async_tree_memoization, sqlglot_normalize, scimark_lu, pidigits, scimark_fft, bench_thread_pool, tomli_loads, pickle_dict, mako, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-pythonperf2-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 91.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.87x