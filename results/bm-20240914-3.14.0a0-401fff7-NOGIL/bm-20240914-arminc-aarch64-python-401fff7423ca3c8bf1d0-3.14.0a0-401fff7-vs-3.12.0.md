# Results vs. 3.12.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.49x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 509 ms: 1.65x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.97 sec: 1.33x slower                                                  |
| html5lib       | 65.1 ms                                                               | 118 ms: 1.82x slower                                                    |
| tornado_http   | 136 ms                                                                | 203 ms: 1.50x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.57x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 723 ms: 1.07x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 692 ms: 1.07x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                  |
| async_tree_none            | 624 ms                                                                | 600 ms: 1.04x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 562 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 866 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 901 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 205 ms: 2.22x slower                                                    |
| nbody          | 105 ms                                                                | 281 ms: 2.69x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.82x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.47 ms: 1.04x faster                                                   |
| regex_dna      | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                                   |
| regex_compile  | 137 ms                                                                | 246 ms: 1.79x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.06x faster                                                    |
| pickle               | 13.4 us                                                               | 13.2 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 153 ms: 1.02x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.35 us: 1.02x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 39.0 us: 1.04x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.98 us: 1.13x slower                                                   |
| unpickle             | 18.5 us                                                               | 21.5 us: 1.16x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.1 us: 1.24x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 155 ms: 1.38x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 125 ms: 1.58x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 4.12 sec: 1.59x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 525 us: 2.02x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 749 us: 2.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.28x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.51x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 100 ms: 1.65x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 51.0 ms: 1.86x slower                                                   |
| django_template | 40.7 ms                                                               | 79.2 ms: 1.95x slower                                                   |
| mako            | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.91x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.46 ms: 1.27x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.60 ms: 1.20x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 723 ms: 1.07x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 692 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.34 sec: 1.05x faster                                                  |
| async_tree_none            | 624 ms                                                                | 600 ms: 1.04x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.47 ms: 1.04x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 562 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 866 ms: 1.02x faster                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.94 ms: 1.02x faster                                                   |
| pickle                     | 13.4 us                                                               | 13.2 us: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 901 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 153 ms: 1.02x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.35 us: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 39.0 us: 1.04x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.1 ms: 1.06x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.01 us: 1.06x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.98 us: 1.13x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 32.2 ms: 1.14x slower                                                   |
| unpickle                   | 18.5 us                                                               | 21.5 us: 1.16x slower                                                   |
| deepcopy                   | 446 us                                                                | 530 us: 1.19x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.61 sec: 1.19x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 677 ms: 1.20x slower                                                    |
| json                       | 5.54 ms                                                               | 6.75 ms: 1.22x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.1 us: 1.24x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.29 sec: 1.26x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.97 sec: 1.33x slower                                                  |
| async_generators           | 491 ms                                                                | 656 ms: 1.34x slower                                                    |
| generators                 | 43.5 ms                                                               | 58.3 ms: 1.34x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 39.2 ms: 1.35x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 67.7 us: 1.36x slower                                                   |
| scimark_fft                | 418 ms                                                                | 579 ms: 1.38x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 155 ms: 1.38x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 5.71 us: 1.39x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.64 ms: 1.39x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| pylint                     | 355 ms                                                                | 506 ms: 1.43x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.7 ms: 1.49x slower                                                   |
| coverage                   | 87.3 ms                                                               | 130 ms: 1.49x slower                                                    |
| meteor_contest             | 112 ms                                                                | 167 ms: 1.49x slower                                                    |
| tornado_http               | 136 ms                                                                | 203 ms: 1.50x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 149 ms: 1.50x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 95.1 ms: 1.53x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 2.02 ms: 1.54x slower                                                   |
| comprehensions             | 25.4 us                                                               | 40.1 us: 1.58x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 125 ms: 1.58x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 137 ms: 1.58x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.99 sec: 1.59x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 34.4 ms: 1.59x slower                                                   |
| python_startup             | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.12 sec: 1.59x slower                                                  |
| 2to3                       | 308 ms                                                                | 509 ms: 1.65x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 100 ms: 1.65x slower                                                    |
| fannkuch                   | 443 ms                                                                | 741 ms: 1.67x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 219 ms: 1.74x slower                                                    |
| thrift                     | 937 us                                                                | 1.63 ms: 1.74x slower                                                   |
| spectral_norm              | 131 ms                                                                | 231 ms: 1.77x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 109 ms: 1.78x slower                                                    |
| regex_compile              | 137 ms                                                                | 246 ms: 1.79x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.00 sec: 1.79x slower                                                  |
| typing_runtime_protocols   | 181 us                                                                | 324 us: 1.80x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.65 sec: 1.80x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.40 sec: 1.81x slower                                                  |
| sympy_str                  | 280 ms                                                                | 507 ms: 1.81x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 118 ms: 1.82x slower                                                    |
| logging_simple             | 7.63 us                                                               | 14.1 us: 1.85x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 51.0 ms: 1.86x slower                                                   |
| logging_format             | 8.34 us                                                               | 15.5 us: 1.86x slower                                                   |
| django_template            | 40.7 ms                                                               | 79.2 ms: 1.95x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 172 ms: 2.02x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 525 us: 2.02x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 317 ms: 2.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 749 us: 2.05x slower                                                    |
| sympy_expand               | 454 ms                                                                | 936 ms: 2.06x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.3 ms: 2.19x slower                                                   |
| mako                       | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| float                      | 92.1 ms                                                               | 205 ms: 2.22x slower                                                    |
| chaos                      | 71.4 ms                                                               | 160 ms: 2.24x slower                                                    |
| logging_silent             | 127 ns                                                                | 285 ns: 2.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 329 ms: 2.26x slower                                                    |
| scimark_sor                | 150 ms                                                                | 341 ms: 2.28x slower                                                    |
| raytrace                   | 353 ms                                                                | 813 ms: 2.30x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.22 ms: 2.31x slower                                                   |
| richards                   | 50.9 ms                                                               | 119 ms: 2.33x slower                                                    |
| richards_super             | 58.5 ms                                                               | 140 ms: 2.40x slower                                                    |
| go                         | 157 ms                                                                | 382 ms: 2.43x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.71 ms: 2.53x slower                                                   |
| nbody                      | 105 ms                                                                | 281 ms: 2.69x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.5 ms: 3.03x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.49x slower                                                            |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.07x