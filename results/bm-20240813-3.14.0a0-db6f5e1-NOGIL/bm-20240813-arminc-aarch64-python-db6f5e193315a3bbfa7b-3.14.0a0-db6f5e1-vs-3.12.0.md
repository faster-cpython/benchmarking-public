# Results vs. 3.12.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-aarch64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 517 ms: 1.68x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.11 sec: 1.38x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.87x slower                                                    |
| tornado_http   | 136 ms                                                                | 208 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 746 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_none            | 624 ms                                                                | 608 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 565 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 872 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 212 ms: 2.30x slower                                                    |
| nbody          | 105 ms                                                                | 286 ms: 2.73x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.85x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| regex_dna      | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| regex_compile  | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.9 us: 1.27x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 162 ms: 1.44x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.8 ms: 1.46x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.23 sec: 1.63x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 132 ms: 1.68x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 543 us: 2.09x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 782 us: 2.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.48x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.52x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 106 ms: 1.74x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 53.6 ms: 1.95x slower                                                   |
| django_template | 40.7 ms                                                               | 84.2 ms: 2.07x slower                                                   |
| mako            | 12.9 ms                                                               | 29.0 ms: 2.25x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.99x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.48 ms: 1.26x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.61 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 746 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                    |
| async_tree_none            | 624 ms                                                                | 608 ms: 1.03x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 565 ms: 1.02x faster                                                    |
| regex_dna                  | 254 ms                                                                | 249 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 872 ms: 1.01x faster                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.13 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.9 ms: 1.10x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.59 sec: 1.18x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 684 ms: 1.21x slower                                                    |
| deepcopy                   | 446 us                                                                | 563 us: 1.26x slower                                                    |
| json                       | 5.54 ms                                                               | 7.00 ms: 1.26x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.9 us: 1.27x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.36 sec: 1.28x slower                                                  |
| generators                 | 43.5 ms                                                               | 57.1 ms: 1.31x slower                                                   |
| async_generators           | 491 ms                                                                | 673 ms: 1.37x slower                                                    |
| docutils                   | 2.98 sec                                                              | 4.11 sec: 1.38x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 40.0 ms: 1.38x slower                                                   |
| scimark_fft                | 418 ms                                                                | 580 ms: 1.39x slower                                                    |
| pylint                     | 355 ms                                                                | 510 ms: 1.44x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.95 ms: 1.44x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 162 ms: 1.44x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.1 ms: 1.45x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.8 ms: 1.46x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 72.2 us: 1.46x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.08 us: 1.48x slower                                                   |
| meteor_contest             | 112 ms                                                                | 169 ms: 1.51x slower                                                    |
| telco                      | 8.51 ms                                                               | 12.9 ms: 1.52x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 152 ms: 1.53x slower                                                    |
| tornado_http               | 136 ms                                                                | 208 ms: 1.53x slower                                                    |
| coverage                   | 87.3 ms                                                               | 136 ms: 1.56x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 137 ms: 1.59x slower                                                    |
| python_startup             | 11.4 ms                                                               | 18.1 ms: 1.59x slower                                                   |
| comprehensions             | 25.4 us                                                               | 40.8 us: 1.61x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 35.0 ms: 1.62x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.05 sec: 1.63x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 2.13 ms: 1.63x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.23 sec: 1.63x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 132 ms: 1.68x slower                                                    |
| 2to3                       | 308 ms                                                                | 517 ms: 1.68x slower                                                    |
| fannkuch                   | 443 ms                                                                | 751 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 106 ms: 1.74x slower                                                    |
| spectral_norm              | 131 ms                                                                | 233 ms: 1.78x slower                                                    |
| thrift                     | 937 us                                                                | 1.69 ms: 1.80x slower                                                   |
| pyflate                    | 559 ms                                                                | 1.02 sec: 1.82x slower                                                  |
| sympy_str                  | 280 ms                                                                | 521 ms: 1.86x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 235 ms: 1.87x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.87x slower                                                    |
| regex_compile              | 137 ms                                                                | 258 ms: 1.88x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 343 us: 1.90x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 117 ms: 1.91x slower                                                    |
| logging_format             | 8.34 us                                                               | 16.1 us: 1.93x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.66 sec: 1.94x slower                                                  |
| logging_simple             | 7.63 us                                                               | 14.8 us: 1.94x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.78 sec: 1.94x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 53.6 ms: 1.95x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 317 ms: 2.05x slower                                                    |
| django_template            | 40.7 ms                                                               | 84.2 ms: 2.07x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 177 ms: 2.08x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 543 us: 2.09x slower                                                    |
| sympy_expand               | 454 ms                                                                | 964 ms: 2.13x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 782 us: 2.14x slower                                                    |
| chaos                      | 71.4 ms                                                               | 159 ms: 2.22x slower                                                    |
| mako                       | 12.9 ms                                                               | 29.0 ms: 2.25x slower                                                   |
| logging_silent             | 127 ns                                                                | 286 ns: 2.26x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.8 ms: 2.26x slower                                                   |
| scimark_sor                | 150 ms                                                                | 339 ms: 2.27x slower                                                    |
| float                      | 92.1 ms                                                               | 212 ms: 2.30x slower                                                    |
| raytrace                   | 353 ms                                                                | 816 ms: 2.31x slower                                                    |
| richards                   | 50.9 ms                                                               | 118 ms: 2.32x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.27 ms: 2.34x slower                                                   |
| richards_super             | 58.5 ms                                                               | 139 ms: 2.38x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 347 ms: 2.39x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.71 ms: 2.53x slower                                                   |
| nbody                      | 105 ms                                                                | 286 ms: 2.73x slower                                                    |
| go                         | 157 ms                                                                | 445 ms: 2.83x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.7 ms: 3.08x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.56x slower                                                            |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240813-3.14.0a0-db6f5e1-NOGIL/bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.08x