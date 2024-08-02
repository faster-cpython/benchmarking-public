# Results vs. 3.12.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: linux-aarch64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 372 ms: 1.21x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                   |
| tornado_http   | 136 ms                                                                | 140 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 440 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 756 ms: 1.21x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 260 ms: 1.02x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 187 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.01x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 401 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.91 ms: 1.06x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 73.3 ms: 1.21x slower                                                   |
| django_template | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 440 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 39.0 us: 1.27x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.12 sec: 1.25x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 712 ms: 1.24x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 756 ms: 1.21x faster                                                    |
| deepcopy                   | 446 us                                                                | 388 us: 1.15x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                                   |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.3 us: 1.05x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.2 ms: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.16 us: 1.02x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.47 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                    |
| float                      | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                  |
| regex_dna                  | 254 ms                                                                | 260 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                   |
| async_generators           | 491 ms                                                                | 504 ms: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.6 ms: 1.03x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                  |
| tornado_http               | 136 ms                                                                | 140 ms: 1.04x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.25 us: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.1 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 974 us: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                  |
| richards_super             | 58.5 ms                                                               | 62.0 ms: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.7 us: 1.06x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.91 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                    |
| dask                       | 376 ms                                                                | 401 ms: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.95 ms: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 597 ms: 1.07x slower                                                    |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.42 ms: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| meteor_contest             | 112 ms                                                                | 121 ms: 1.08x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.4 ms: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.1 ms: 1.09x slower                                                   |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 401 us: 1.10x slower                                                    |
| fannkuch                   | 443 ms                                                                | 488 ms: 1.10x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 624 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 145 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.8 ms: 1.12x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.66 ms: 1.14x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.01 ms: 1.14x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 2.11 ms: 1.15x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| go                         | 157 ms                                                                | 183 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.17x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.28 ms: 1.17x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 148 ms: 1.18x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 72.8 ms: 1.19x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 32.9 ms: 1.20x slower                                                   |
| 2to3                       | 308 ms                                                                | 372 ms: 1.21x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 73.3 ms: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                   |
| chaos                      | 71.4 ms                                                               | 87.2 ms: 1.22x slower                                                   |
| pylint                     | 355 ms                                                                | 438 ms: 1.23x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 180 ms: 1.24x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.34 sec: 1.24x slower                                                  |
| sympy_str                  | 280 ms                                                                | 348 ms: 1.25x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                  |
| django_template            | 40.7 ms                                                               | 51.4 ms: 1.26x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 27.7 ms: 1.28x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 200 ms: 1.30x slower                                                    |
| sympy_expand               | 454 ms                                                                | 593 ms: 1.31x slower                                                    |
| generators                 | 43.5 ms                                                               | 57.3 ms: 1.32x slower                                                   |
| regex_compile              | 137 ms                                                                | 187 ms: 1.36x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.75 ms: 1.40x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (2): bench_thread_pool, mako
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-arminc-aarch64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x