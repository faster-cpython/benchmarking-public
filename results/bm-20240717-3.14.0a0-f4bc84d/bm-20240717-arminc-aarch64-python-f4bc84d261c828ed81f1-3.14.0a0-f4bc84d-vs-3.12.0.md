# Results vs. 3.12.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-aarch64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.03x faster
- HPT reliability: 89.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.06 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 68.0 ms: 1.05x slower                                                   |
| tornado_http   | 136 ms                                                                | 130 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 81.4 ms: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 62.3 ms: 1.03x slower                                                   |
| django_template | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                   |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 439 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 407 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 551 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 39.3 us: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 718 ms: 1.23x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                   |
| raytrace                   | 353 ms                                                                | 300 ms: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.87 us: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.28 us: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| tornado_http               | 136 ms                                                                | 130 ms: 1.04x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                   |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.5 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 82.5 ms: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.03x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float                      | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                   |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 579 ms: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 939 ms: 1.03x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.06 sec: 1.03x slower                                                  |
| go                         | 157 ms                                                                | 161 ms: 1.03x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 62.3 ms: 1.03x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 81.4 ms: 1.03x slower                                                   |
| richards_super             | 58.5 ms                                                               | 60.3 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 130 ms: 1.03x slower                                                    |
| thrift                     | 937 us                                                                | 970 us: 1.04x slower                                                    |
| pyflate                    | 559 ms                                                                | 580 ms: 1.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 68.0 ms: 1.05x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.8 ms: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 470 ms: 1.06x slower                                                    |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.90 ms: 1.06x slower                                                   |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.67 ms: 1.08x slower                                                   |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                   |
| coverage                   | 87.3 ms                                                               | 99.2 ms: 1.14x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.07 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (6): pylint, meteor_contest, nqueens, coroutines, asyncio_websockets, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: bpe_tokeniser

# HPT report

- Reliability score: 89.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x