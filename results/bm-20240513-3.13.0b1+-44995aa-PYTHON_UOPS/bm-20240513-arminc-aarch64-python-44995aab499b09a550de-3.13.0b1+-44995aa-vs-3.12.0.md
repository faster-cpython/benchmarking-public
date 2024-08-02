# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                                     |
| chameleon      | 8.81 ms                                                               | 10.3 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                   |
| html5lib       | 65.1 ms                                                               | 75.0 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 486 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 625 ms: 1.19x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 673 ms: 1.15x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 813 ms: 1.12x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 820 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                     |
| float          | 92.1 ms                                                               | 116 ms: 1.26x slower                                                     |
| nbody          | 105 ms                                                                | 150 ms: 1.44x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                    |
| regex_compile  | 137 ms                                                                | 173 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 161 ms: 1.07x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.73 us: 1.09x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 89.8 ms: 1.14x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 128 ms: 1.14x slower                                                     |
| tomli_loads          | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 470 us: 1.29x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 367 us: 1.41x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.51 ms: 1.02x slower                                                    |
| python_startup         | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 51.0 ms: 1.26x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 77.7 ms: 1.28x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 37.0 ms: 1.35x slower                                                    |
| mako            | 12.9 ms                                                               | 17.5 ms: 1.36x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.31x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 507 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 486 ms: 1.19x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 625 ms: 1.19x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 673 ms: 1.15x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 813 ms: 1.12x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| generators                 | 43.5 ms                                                               | 39.5 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 820 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.9 ms: 1.03x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.49 us: 1.02x faster                                                    |
| raytrace                   | 353 ms                                                                | 348 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.00x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.51 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                     |
| dask                       | 376 ms                                                                | 385 ms: 1.02x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 581 ms: 1.03x slower                                                     |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 986 us: 1.05x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.61 sec: 1.06x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.7 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.88 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 161 ms: 1.07x slower                                                     |
| async_generators           | 491 ms                                                                | 524 ms: 1.07x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 66.4 ms: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.06 us: 1.08x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.73 us: 1.09x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.2 ms: 1.10x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.77 ms: 1.10x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.38 sec: 1.10x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                    |
| pylint                     | 355 ms                                                                | 393 ms: 1.11x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 173 ms: 1.12x slower                                                     |
| aiohttp                    | 1.16 ms                                                               | 1.31 ms: 1.13x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 89.8 ms: 1.14x slower                                                    |
| sympy_str                  | 280 ms                                                                | 320 ms: 1.14x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 128 ms: 1.14x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 75.0 ms: 1.15x slower                                                    |
| sympy_expand               | 454 ms                                                                | 525 ms: 1.16x slower                                                     |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                                     |
| chameleon                  | 8.81 ms                                                               | 10.3 ms: 1.17x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.33 ms: 1.17x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.83 us: 1.18x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 73.7 ms: 1.20x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 152 ms: 1.21x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.32 ms: 1.21x slower                                                    |
| meteor_contest             | 112 ms                                                                | 136 ms: 1.21x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 106 ms: 1.22x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 26.4 ms: 1.22x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.80 ms: 1.23x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.25 ms: 1.23x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.39 ms: 1.25x slower                                                    |
| deepcopy                   | 446 us                                                                | 558 us: 1.25x slower                                                     |
| chaos                      | 71.4 ms                                                               | 89.5 ms: 1.25x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.25 sec: 1.25x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.0 ms: 1.26x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 227 us: 1.26x slower                                                     |
| comprehensions             | 25.4 us                                                               | 32.0 us: 1.26x slower                                                    |
| float                      | 92.1 ms                                                               | 116 ms: 1.26x slower                                                     |
| regex_compile              | 137 ms                                                                | 173 ms: 1.26x slower                                                     |
| go                         | 157 ms                                                                | 201 ms: 1.28x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 77.7 ms: 1.28x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 470 us: 1.29x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 5.32 ms: 1.29x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.45 sec: 1.30x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                                   |
| richards_super             | 58.5 ms                                                               | 76.9 ms: 1.31x slower                                                    |
| scimark_fft                | 418 ms                                                                | 561 ms: 1.34x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 37.0 ms: 1.35x slower                                                    |
| fannkuch                   | 443 ms                                                                | 599 ms: 1.35x slower                                                     |
| scimark_sor                | 150 ms                                                                | 202 ms: 1.35x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.35x slower                                                     |
| mako                       | 12.9 ms                                                               | 17.5 ms: 1.36x slower                                                    |
| pyflate                    | 559 ms                                                                | 759 ms: 1.36x slower                                                     |
| richards                   | 50.9 ms                                                               | 69.6 ms: 1.37x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.47 ms: 1.37x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 119 ms: 1.40x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 367 us: 1.41x slower                                                     |
| nbody                      | 105 ms                                                                | 150 ms: 1.44x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 213 ms: 1.46x slower                                                     |
| spectral_norm              | 131 ms                                                                | 194 ms: 1.48x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 75.9 us: 1.53x slower                                                    |
| logging_silent             | 127 ns                                                                | 199 ns: 1.57x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 11.4 ms: 1.64x slower                                                    |
| telco                      | 8.51 ms                                                               | 165 ms: 19.43x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.18x slower                                                             |

Benchmark hidden because not significant (7): xml_etree_parse, logging_format, mypy2, tornado_http, pickle_list, regex_dna, pickle_dict
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.93x