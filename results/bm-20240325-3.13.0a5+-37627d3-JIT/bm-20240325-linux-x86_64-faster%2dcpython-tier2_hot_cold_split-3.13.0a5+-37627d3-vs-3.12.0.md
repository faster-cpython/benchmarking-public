# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 37627d3
- commit date: 2024-03-25
- overall geometric mean: 1.02x faster
- HPT reliability: 83.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                             |
| chameleon      | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                            |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                           |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 929 ms: 1.27x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 354 ms: 1.27x faster                                                             |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 924 ms: 1.25x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 462 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 611 ms: 1.19x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                            |
| nbody          | 97.0 ms                                                | 91.1 ms: 1.06x faster                                                            |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                            |
| regex_compile  | 148 ms                                                 | 146 ms: 1.02x faster                                                             |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                           |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                             |
| unpickle_list        | 5.29 us                                                | 5.08 us: 1.04x faster                                                            |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.8 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                             |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                            |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                            |
| unpickle_pure_python | 230 us                                                 | 240 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.0 ms: 1.15x slower                                                            |
| python_startup_no_site | 6.94 ms                                                | 9.44 ms: 1.36x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                            |
| django_template | 34.6 ms                                                | 36.2 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.41x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 929 ms: 1.27x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 354 ms: 1.27x faster                                                             |
| async_tree_none            | 472 ms                                                 | 375 ms: 1.26x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 924 ms: 1.25x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 462 ms: 1.25x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                                             |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.20x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 611 ms: 1.19x faster                                                             |
| scimark_fft                | 382 ms                                                 | 339 ms: 1.13x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 74.1 ms: 1.10x faster                                                            |
| logging_format             | 7.23 us                                                | 6.55 us: 1.10x faster                                                            |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                            |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.90 us: 1.09x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.69 ms: 1.08x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.46 ms: 1.07x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 70.0 ms: 1.07x faster                                                            |
| raytrace                   | 312 ms                                                 | 292 ms: 1.07x faster                                                             |
| fannkuch                   | 417 ms                                                 | 391 ms: 1.07x faster                                                             |
| nbody                      | 97.0 ms                                                | 91.1 ms: 1.06x faster                                                            |
| chaos                      | 67.0 ms                                                | 63.1 ms: 1.06x faster                                                            |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                                            |
| logging_silent             | 104 ns                                                 | 99.3 ns: 1.05x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.18 us: 1.05x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                             |
| unpickle_list              | 5.29 us                                                | 5.08 us: 1.04x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 39.3 us: 1.04x faster                                                            |
| chameleon                  | 7.41 ms                                                | 7.14 ms: 1.04x faster                                                            |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 754 ms: 1.03x faster                                                             |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                            |
| deepcopy                   | 371 us                                                 | 363 us: 1.02x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                            |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                                            |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 60.4 ms: 1.02x faster                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                            |
| regex_compile              | 148 ms                                                 | 146 ms: 1.02x faster                                                             |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 87.8 ms: 1.02x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                            |
| pathlib                    | 19.3 ms                                                | 19.1 ms: 1.01x faster                                                            |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                                             |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.47 ms: 1.00x faster                                                            |
| pyflate                    | 482 ms                                                 | 481 ms: 1.00x faster                                                             |
| gc_traversal               | 3.79 ms                                                | 3.82 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.13 us: 1.01x slower                                                            |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                            |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                             |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                            |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                             |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                            |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                             |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                            |
| sympy_integrate            | 21.4 ms                                                | 21.8 ms: 1.02x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 859 us: 1.02x slower                                                             |
| sympy_expand               | 478 ms                                                 | 491 ms: 1.03x slower                                                             |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                             |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                                             |
| dulwich_log                | 68.5 ms                                                | 70.9 ms: 1.03x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                           |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                           |
| unpickle_pure_python       | 230 us                                                 | 240 us: 1.04x slower                                                             |
| asyncio_tcp                | 491 ms                                                 | 511 ms: 1.04x slower                                                             |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.04x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                            |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.06x slower                                                             |
| gunicorn                   | 1.24 ms                                                | 1.31 ms: 1.06x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 58.1 ms: 1.06x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.80 sec: 1.06x slower                                                           |
| aiohttp                    | 1.15 ms                                                | 1.22 ms: 1.06x slower                                                            |
| nqueens                    | 83.3 ms                                                | 90.8 ms: 1.09x slower                                                            |
| go                         | 139 ms                                                 | 155 ms: 1.11x slower                                                             |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                             |
| hexiom                     | 6.41 ms                                                | 7.22 ms: 1.13x slower                                                            |
| python_startup             | 9.55 ms                                                | 11.0 ms: 1.15x slower                                                            |
| telco                      | 7.10 ms                                                | 8.51 ms: 1.20x slower                                                            |
| coverage                   | 72.7 ms                                                | 96.7 ms: 1.33x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 9.44 ms: 1.36x slower                                                            |
| unpack_sequence            | 54.0 ns                                                | 92.1 ns: 1.71x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (6): mypy2, richards, pycparser, bench_mp_pool, json_loads, xml_etree_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240325-3.13.0a5+-37627d3-JIT/bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 83.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.04x