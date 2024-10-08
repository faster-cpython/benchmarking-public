# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: linux-aarch64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.01x faster
- HPT reliability: 89.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 8.86 ms: 1.01x slower                                        |
| docutils       | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 624 ms                                                                | 573 ms: 1.09x faster                                         |
| async_tree_memoization  | 777 ms                                                                | 737 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed | 912 ms                                                                | 893 ms: 1.02x faster                                         |
| async_tree_io_tg        | 1.40 sec                                                              | 1.43 sec: 1.02x slower                                       |
| async_tree_io           | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                       |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                 |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 103 ms: 1.01x faster                                         |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| float          | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                        |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 349 us: 1.05x faster                                         |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.02x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| pickle               | 13.4 us                                                               | 13.3 us: 1.01x faster                                        |
| unpickle_list        | 6.17 us                                                               | 6.25 us: 1.01x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| json_dumps           | 12.3 ms                                                               | 12.8 ms: 1.04x slower                                        |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.05x slower                                        |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                        |
| xml_etree_generate   | 112 ms                                                                | 118 ms: 1.05x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                               | 12.2 ms: 1.07x slower                                        |
| python_startup_no_site | 8.37 ms                                                               | 10.5 ms: 1.25x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 181 us                                                                | 133 us: 1.35x faster                                         |
| comprehensions           | 25.4 us                                                               | 19.9 us: 1.28x faster                                        |
| generators               | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                        |
| raytrace                 | 353 ms                                                                | 296 ms: 1.19x faster                                         |
| sympy_sum                | 154 ms                                                                | 140 ms: 1.11x faster                                         |
| crypto_pyaes             | 86.6 ms                                                               | 79.2 ms: 1.09x faster                                        |
| regex_compile            | 137 ms                                                                | 126 ms: 1.09x faster                                         |
| async_tree_none          | 624 ms                                                                | 573 ms: 1.09x faster                                         |
| sympy_str                | 280 ms                                                                | 260 ms: 1.07x faster                                         |
| logging_format           | 8.34 us                                                               | 7.83 us: 1.07x faster                                        |
| sqlglot_parse            | 1.46 ms                                                               | 1.37 ms: 1.07x faster                                        |
| logging_simple           | 7.63 us                                                               | 7.18 us: 1.06x faster                                        |
| scimark_lu               | 146 ms                                                                | 137 ms: 1.06x faster                                         |
| pylint                   | 355 ms                                                                | 335 ms: 1.06x faster                                         |
| sympy_integrate          | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                        |
| chaos                    | 71.4 ms                                                               | 67.6 ms: 1.06x faster                                        |
| async_tree_memoization   | 777 ms                                                                | 737 ms: 1.05x faster                                         |
| pickle_pure_python       | 365 us                                                                | 349 us: 1.05x faster                                         |
| sqlglot_transpile        | 1.83 ms                                                               | 1.75 ms: 1.04x faster                                        |
| dulwich_log              | 62.0 ms                                                               | 59.7 ms: 1.04x faster                                        |
| deepcopy_reduce          | 4.10 us                                                               | 3.95 us: 1.04x faster                                        |
| scimark_monte_carlo      | 85.1 ms                                                               | 82.1 ms: 1.04x faster                                        |
| deepcopy                 | 446 us                                                                | 431 us: 1.03x faster                                         |
| nqueens                  | 99.2 ms                                                               | 96.0 ms: 1.03x faster                                        |
| deltablue                | 4.12 ms                                                               | 4.00 ms: 1.03x faster                                        |
| deepcopy_memo            | 49.6 us                                                               | 48.2 us: 1.03x faster                                        |
| mdp                      | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                       |
| docutils                 | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                       |
| async_tree_cpu_io_mixed  | 912 ms                                                                | 893 ms: 1.02x faster                                         |
| bench_thread_pool        | 1.31 ms                                                               | 1.29 ms: 1.02x faster                                        |
| pathlib                  | 24.5 ms                                                               | 24.2 ms: 1.02x faster                                        |
| unpickle_pure_python     | 260 us                                                                | 256 us: 1.02x faster                                         |
| pprint_safe_repr         | 916 ms                                                                | 903 ms: 1.01x faster                                         |
| pprint_pformat           | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                       |
| xml_etree_iterparse      | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| nbody                    | 105 ms                                                                | 103 ms: 1.01x faster                                         |
| pickle                   | 13.4 us                                                               | 13.3 us: 1.01x faster                                        |
| hexiom                   | 6.98 ms                                                               | 6.92 ms: 1.01x faster                                        |
| thrift                   | 937 us                                                                | 929 us: 1.01x faster                                         |
| async_generators         | 491 ms                                                                | 487 ms: 1.01x faster                                         |
| coroutines               | 29.0 ms                                                               | 28.8 ms: 1.01x faster                                        |
| chameleon                | 8.81 ms                                                               | 8.86 ms: 1.01x slower                                        |
| pidigits                 | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| richards_super           | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                        |
| asyncio_websockets       | 658 ms                                                                | 664 ms: 1.01x slower                                         |
| float                    | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                        |
| genshi_text              | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                        |
| gc_traversal             | 4.40 ms                                                               | 4.45 ms: 1.01x slower                                        |
| unpickle_list            | 6.17 us                                                               | 6.25 us: 1.01x slower                                        |
| aiohttp                  | 1.16 ms                                                               | 1.18 ms: 1.01x slower                                        |
| async_tree_io_tg         | 1.40 sec                                                              | 1.43 sec: 1.02x slower                                       |
| async_tree_io            | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                       |
| richards                 | 50.9 ms                                                               | 51.8 ms: 1.02x slower                                        |
| asyncio_tcp_ssl          | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                       |
| dask                     | 376 ms                                                                | 383 ms: 1.02x slower                                         |
| pycparser                | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                       |
| xml_etree_process        | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                        |
| go                       | 157 ms                                                                | 161 ms: 1.03x slower                                         |
| logging_silent           | 127 ns                                                                | 130 ns: 1.03x slower                                         |
| sqlite_synth             | 3.77 us                                                               | 3.88 us: 1.03x slower                                        |
| json                     | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                        |
| fannkuch                 | 443 ms                                                                | 459 ms: 1.03x slower                                         |
| spectral_norm            | 131 ms                                                                | 135 ms: 1.04x slower                                         |
| create_gc_cycles         | 1.92 ms                                                               | 1.99 ms: 1.04x slower                                        |
| json_dumps               | 12.3 ms                                                               | 12.8 ms: 1.04x slower                                        |
| unpickle                 | 18.5 us                                                               | 19.3 us: 1.05x slower                                        |
| json_loads               | 30.7 us                                                               | 32.2 us: 1.05x slower                                        |
| scimark_sparse_mat_mult  | 6.19 ms                                                               | 6.51 ms: 1.05x slower                                        |
| xml_etree_generate       | 112 ms                                                                | 118 ms: 1.05x slower                                         |
| scimark_fft              | 418 ms                                                                | 441 ms: 1.05x slower                                         |
| pyflate                  | 559 ms                                                                | 591 ms: 1.06x slower                                         |
| regex_effbot             | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                        |
| regex_v8                 | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                        |
| python_startup           | 11.4 ms                                                               | 12.2 ms: 1.07x slower                                        |
| gunicorn                 | 1.14 ms                                                               | 1.23 ms: 1.09x slower                                        |
| scimark_sor              | 150 ms                                                                | 165 ms: 1.10x slower                                         |
| coverage                 | 87.3 ms                                                               | 102 ms: 1.16x slower                                         |
| telco                    | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                        |
| python_startup_no_site   | 8.37 ms                                                               | 10.5 ms: 1.25x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (21): xml_etree_parse, regex_dna, async_tree_memoization_tg, asyncio_tcp, sympy_expand, bench_mp_pool, 2to3, django_template, sqlglot_optimize, genshi_xml, sqlglot_normalize, tomli_loads, async_tree_none_tg, mako, pickle_list, tornado_http, async_tree_cpu_io_mixed_tg, pickle_dict, html5lib, meteor_contest, mypy2
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json: flaskblogging

# HPT report

- Reliability score: 89.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.89x