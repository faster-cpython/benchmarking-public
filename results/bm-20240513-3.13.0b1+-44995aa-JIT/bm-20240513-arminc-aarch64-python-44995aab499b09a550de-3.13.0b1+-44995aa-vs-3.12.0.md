# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 362 ms: 1.17x slower                                                     |
| chameleon      | 8.81 ms                                                               | 9.14 ms: 1.04x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                   |
| html5lib       | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                    |
| tornado_http   | 136 ms                                                                | 141 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 496 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 614 ms: 1.21x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 654 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 806 ms: 1.13x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 817 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                    |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                     |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 248 ms: 1.03x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                    |
| regex_compile  | 137 ms                                                                | 167 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| pickle_list          | 5.25 us                                                               | 5.20 us: 1.01x faster                                                    |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.05x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 118 ms: 1.05x slower                                                     |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.06x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 393 us: 1.08x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.65 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 49.5 ms: 1.22x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.9 ms: 1.24x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 496 ms: 1.26x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 474 ms: 1.22x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 614 ms: 1.21x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 654 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 806 ms: 1.13x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.12x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 817 ms: 1.08x faster                                                     |
| raytrace                   | 353 ms                                                                | 327 ms: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.4 ms: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.33 us: 1.04x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.05 us: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.03x faster                                                     |
| float                      | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.20 us: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                     |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.6 ms: 1.02x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.48 sec: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.65 sec: 1.02x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.6 ms: 1.03x slower                                                    |
| tornado_http               | 136 ms                                                                | 141 ms: 1.04x slower                                                     |
| chameleon                  | 8.81 ms                                                               | 9.14 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 972 us: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                                    |
| async_generators           | 491 ms                                                                | 514 ms: 1.05x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 118 ms: 1.05x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                    |
| dask                       | 376 ms                                                                | 397 ms: 1.05x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 119 ms: 1.06x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.06x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.65 us: 1.08x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.2 ms: 1.08x slower                                                    |
| fannkuch                   | 443 ms                                                                | 479 ms: 1.08x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                   |
| mypy2                      | 873 ms                                                                | 946 ms: 1.08x slower                                                     |
| richards                   | 50.9 ms                                                               | 55.2 ms: 1.08x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 458 ms: 1.10x slower                                                     |
| pyflate                    | 559 ms                                                                | 613 ms: 1.10x slower                                                     |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 624 ms: 1.10x slower                                                     |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 68.7 ms: 1.11x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.03 ms: 1.11x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.87 ms: 1.12x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.63 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.97 ms: 1.12x slower                                                    |
| deepcopy                   | 446 us                                                                | 502 us: 1.13x slower                                                     |
| go                         | 157 ms                                                                | 178 ms: 1.13x slower                                                     |
| coverage                   | 87.3 ms                                                               | 99.1 ms: 1.13x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.66 us: 1.14x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                     |
| gunicorn                   | 1.14 ms                                                               | 1.31 ms: 1.16x slower                                                    |
| aiohttp                    | 1.16 ms                                                               | 1.34 ms: 1.16x slower                                                    |
| sympy_str                  | 280 ms                                                                | 324 ms: 1.16x slower                                                     |
| pylint                     | 355 ms                                                                | 411 ms: 1.16x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 146 ms: 1.16x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 71.3 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                     |
| 2to3                       | 308 ms                                                                | 362 ms: 1.17x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 182 ms: 1.18x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.18x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.55 sec: 1.19x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 26.0 ms: 1.20x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.30 ms: 1.21x slower                                                    |
| sympy_expand               | 454 ms                                                                | 548 ms: 1.21x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                   |
| django_template            | 40.7 ms                                                               | 49.5 ms: 1.22x slower                                                    |
| regex_compile              | 137 ms                                                                | 167 ms: 1.22x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 33.9 ms: 1.24x slower                                                    |
| chaos                      | 71.4 ms                                                               | 89.2 ms: 1.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.27x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.45 ms: 1.28x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.97 ms: 1.29x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 82.0 ms: 1.35x slower                                                    |
| telco                      | 8.51 ms                                                               | 167 ms: 19.61x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.10x slower                                                             |

Benchmark hidden because not significant (5): coroutines, crypto_pyaes, deepcopy_memo, xml_etree_iterparse, mako
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x