# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: windows-amd64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.07x faster
- HPT reliability: 98.01%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 233 ms: 1.07x slower                                                             |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                           |
| tornado_http   | 89.5 ms                                                     | 85.2 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                             |
| async_tree_io_tg           | 771 ms                                                      | 517 ms: 1.49x faster                                                             |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                             |
| async_tree_io              | 731 ms                                                      | 523 ms: 1.40x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 249 ms: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                             |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.0 ms: 1.36x faster                                                            |
| float          | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                            |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                             |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                            |
| regex_compile  | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                            |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 178 us: 1.10x faster                                                             |
| xml_etree_generate   | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.2 ms: 1.08x faster                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                            |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                                             |
| xml_etree_parse      | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                            |
| json_dumps           | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                            |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.07x slower                                                            |
| python_startup         | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                            |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.54x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 241 ms: 1.52x faster                                                             |
| async_tree_io_tg           | 771 ms                                                      | 517 ms: 1.49x faster                                                             |
| spectral_norm              | 66.9 ms                                                     | 45.1 ms: 1.48x faster                                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.48x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 16.1 us: 1.47x faster                                                            |
| async_tree_none            | 291 ms                                                      | 206 ms: 1.42x faster                                                             |
| async_tree_io              | 731 ms                                                      | 523 ms: 1.40x faster                                                             |
| mako                       | 7.09 ms                                                     | 5.10 ms: 1.39x faster                                                            |
| async_tree_memoization     | 339 ms                                                      | 249 ms: 1.36x faster                                                             |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                            |
| nbody                      | 71.9 ms                                                     | 53.0 ms: 1.36x faster                                                            |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                             |
| float                      | 56.8 ms                                                     | 44.5 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                             |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                             |
| crypto_pyaes               | 48.5 ms                                                     | 39.7 ms: 1.22x faster                                                            |
| pyflate                    | 295 ms                                                      | 250 ms: 1.18x faster                                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.19 ms: 1.17x faster                                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.5 ms: 1.17x faster                                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                            |
| fannkuch                   | 247 ms                                                      | 219 ms: 1.13x faster                                                             |
| logging_simple             | 6.28 us                                                     | 5.64 us: 1.11x faster                                                            |
| logging_format             | 6.72 us                                                     | 6.09 us: 1.10x faster                                                            |
| pickle_pure_python         | 195 us                                                      | 178 us: 1.10x faster                                                             |
| chaos                      | 43.3 ms                                                     | 39.4 ms: 1.10x faster                                                            |
| logging_silent             | 60.5 ns                                                     | 55.5 ns: 1.09x faster                                                            |
| xml_etree_generate         | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.2 ms: 1.08x faster                                                            |
| tomli_loads                | 1.37 sec                                                    | 1.26 sec: 1.08x faster                                                           |
| pathlib                    | 80.5 ms                                                     | 75.1 ms: 1.07x faster                                                            |
| bench_thread_pool          | 857 us                                                      | 801 us: 1.07x faster                                                             |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                             |
| pprint_safe_repr           | 513 ms                                                      | 483 ms: 1.06x faster                                                             |
| pprint_pformat             | 1.05 sec                                                    | 989 ms: 1.06x faster                                                             |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                             |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                            |
| tornado_http               | 89.5 ms                                                     | 85.2 ms: 1.05x faster                                                            |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                            |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                     | 71.7 ms: 1.04x faster                                                            |
| asyncio_tcp                | 487 ms                                                      | 469 ms: 1.04x faster                                                             |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                                             |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                            |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                            |
| xml_etree_parse            | 93.0 ms                                                     | 91.1 ms: 1.02x faster                                                            |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                             |
| sqlglot_parse              | 804 us                                                      | 815 us: 1.01x slower                                                             |
| go                         | 91.6 ms                                                     | 92.8 ms: 1.01x slower                                                            |
| generators                 | 22.5 ms                                                     | 22.9 ms: 1.02x slower                                                            |
| regex_compile              | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                            |
| json_dumps                 | 5.70 ms                                                     | 5.80 ms: 1.02x slower                                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                            |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                            |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                            |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                            |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                             |
| sympy_sum                  | 91.5 ms                                                     | 94.2 ms: 1.03x slower                                                            |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                             |
| richards_super             | 32.1 ms                                                     | 33.2 ms: 1.03x slower                                                            |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 36.1 ms: 1.05x slower                                                            |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                           |
| pycparser                  | 699 ms                                                      | 740 ms: 1.06x slower                                                             |
| async_generators           | 239 ms                                                      | 255 ms: 1.06x slower                                                             |
| 2to3                       | 218 ms                                                      | 233 ms: 1.07x slower                                                             |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                           |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.07x slower                                                            |
| scimark_sor                | 78.8 ms                                                     | 85.0 ms: 1.08x slower                                                            |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                            |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                            |
| telco                      | 4.13 ms                                                     | 4.50 ms: 1.09x slower                                                            |
| python_startup             | 19.5 ms                                                     | 21.3 ms: 1.09x slower                                                            |
| sympy_expand               | 284 ms                                                      | 313 ms: 1.10x slower                                                             |
| hexiom                     | 4.10 ms                                                     | 4.59 ms: 1.12x slower                                                            |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                            |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                            |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.18x slower                                                             |
| scimark_lu                 | 58.9 ms                                                     | 70.3 ms: 1.19x slower                                                            |
| create_gc_cycles           | 752 us                                                      | 899 us: 1.20x slower                                                             |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-pythonperf1-amd64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.01% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown