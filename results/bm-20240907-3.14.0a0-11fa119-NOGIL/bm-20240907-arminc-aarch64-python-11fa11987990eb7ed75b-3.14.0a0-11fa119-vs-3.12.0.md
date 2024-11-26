# Results vs. 3.12.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.358x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 518 ms: 1.68x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.10 sec: 1.37x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| tornado_http   | 136 ms                                                                | 207 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 699 ms: 1.06x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 572 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 207 ms: 2.25x slower                                                    |
| nbody          | 105 ms                                                                | 281 ms: 2.68x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.83x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                   |
| regex_dna      | 254 ms                                                                | 261 ms: 1.03x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.17x slower                                                   |
| regex_compile  | 137 ms                                                                | 259 ms: 1.89x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| pickle               | 13.4 us                                                               | 13.3 us: 1.01x faster                                                   |
| pickle_dict          | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 157 ms: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.99 us: 1.13x slower                                                   |
| unpickle             | 18.5 us                                                               | 21.7 us: 1.18x slower                                                   |
| json_loads           | 30.7 us                                                               | 39.3 us: 1.28x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.9 ms: 1.46x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.19 sec: 1.61x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 130 ms: 1.65x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 542 us: 2.09x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 777 us: 2.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.31x slower                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.2 ms: 1.60x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.53x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 53.3 ms: 1.94x slower                                                   |
| django_template | 40.7 ms                                                               | 83.4 ms: 2.05x slower                                                   |
| mako            | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.98x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.45 ms: 1.27x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.62 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 699 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 739 ms: 1.05x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 871 ms: 1.01x faster                                                    |
| pickle                     | 13.4 us                                                               | 13.3 us: 1.01x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 572 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.20 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| regex_dna                  | 254 ms                                                                | 261 ms: 1.03x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 157 ms: 1.04x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.8 ms: 1.09x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.17 us: 1.11x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.99 us: 1.13x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.17x slower                                                   |
| unpickle                   | 18.5 us                                                               | 21.7 us: 1.18x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.62 sec: 1.20x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 683 ms: 1.21x slower                                                    |
| mdp                        | 3.41 sec                                                              | 4.32 sec: 1.27x slower                                                  |
| json                       | 5.54 ms                                                               | 7.03 ms: 1.27x slower                                                   |
| deepcopy                   | 446 us                                                                | 571 us: 1.28x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.3 us: 1.28x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.7 ms: 1.33x slower                                                   |
| async_generators           | 491 ms                                                                | 653 ms: 1.33x slower                                                    |
| scimark_fft                | 418 ms                                                                | 573 ms: 1.37x slower                                                    |
| docutils                   | 2.98 sec                                                              | 4.10 sec: 1.37x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 40.9 ms: 1.41x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.82 ms: 1.42x slower                                                   |
| pylint                     | 355 ms                                                                | 511 ms: 1.44x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 72.1 us: 1.45x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.46x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.9 ms: 1.46x slower                                                   |
| meteor_contest             | 112 ms                                                                | 167 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 6.14 us: 1.50x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.8 ms: 1.50x slower                                                   |
| tornado_http               | 136 ms                                                                | 207 ms: 1.53x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 152 ms: 1.54x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 96.1 ms: 1.55x slower                                                   |
| coverage                   | 87.3 ms                                                               | 136 ms: 1.55x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 137 ms: 1.58x slower                                                    |
| python_startup             | 11.4 ms                                                               | 18.2 ms: 1.60x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 34.7 ms: 1.60x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.02 sec: 1.61x slower                                                  |
| comprehensions             | 25.4 us                                                               | 40.9 us: 1.61x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.19 sec: 1.61x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 2.13 ms: 1.63x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 130 ms: 1.65x slower                                                    |
| fannkuch                   | 443 ms                                                                | 738 ms: 1.67x slower                                                    |
| 2to3                       | 308 ms                                                                | 518 ms: 1.68x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| spectral_norm              | 131 ms                                                                | 226 ms: 1.73x slower                                                    |
| thrift                     | 937 us                                                                | 1.69 ms: 1.80x slower                                                   |
| pyflate                    | 559 ms                                                                | 1.02 sec: 1.83x slower                                                  |
| sympy_str                  | 280 ms                                                                | 514 ms: 1.84x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 336 us: 1.86x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 237 ms: 1.88x slower                                                    |
| regex_compile              | 137 ms                                                                | 259 ms: 1.89x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.9 us: 1.91x slower                                                   |
| logging_simple             | 7.63 us                                                               | 14.6 us: 1.91x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.76 sec: 1.92x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.64 sec: 1.93x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 119 ms: 1.93x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 53.3 ms: 1.94x slower                                                   |
| django_template            | 40.7 ms                                                               | 83.4 ms: 2.05x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 318 ms: 2.06x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 176 ms: 2.07x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 542 us: 2.09x slower                                                    |
| sympy_expand               | 454 ms                                                                | 961 ms: 2.12x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 777 us: 2.13x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| chaos                      | 71.4 ms                                                               | 160 ms: 2.24x slower                                                    |
| logging_silent             | 127 ns                                                                | 284 ns: 2.24x slower                                                    |
| float                      | 92.1 ms                                                               | 207 ms: 2.25x slower                                                    |
| scimark_sor                | 150 ms                                                                | 341 ms: 2.28x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.9 ms: 2.28x slower                                                   |
| richards                   | 50.9 ms                                                               | 117 ms: 2.29x slower                                                    |
| raytrace                   | 353 ms                                                                | 815 ms: 2.31x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 350 ms: 2.41x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.45 ms: 2.44x slower                                                   |
| richards_super             | 58.5 ms                                                               | 143 ms: 2.44x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.67 ms: 2.51x slower                                                   |
| go                         | 157 ms                                                                | 404 ms: 2.57x slower                                                    |
| nbody                      | 105 ms                                                                | 281 ms: 2.68x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.7 ms: 3.09x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.52x slower                                                            |

Benchmark hidden because not significant (4): async_tree_io, async_tree_cpu_io_mixed, async_tree_none, pickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.358x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.08x