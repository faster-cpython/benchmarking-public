# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.341x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 509 ms: 1.65x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| html5lib       | 65.1 ms                                                               | 119 ms: 1.83x slower                                                    |
| tornado_http   | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.56x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 692 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 730 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.33 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 865 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 895 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 568 ms: 1.01x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 204 ms: 2.21x slower                                                    |
| nbody          | 105 ms                                                                | 279 ms: 2.67x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.81x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.44 ms: 1.05x faster                                                   |
| regex_dna      | 254 ms                                                                | 257 ms: 1.01x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 33.2 ms: 1.17x slower                                                   |
| regex_compile  | 137 ms                                                                | 244 ms: 1.78x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| pickle               | 13.4 us                                                               | 13.3 us: 1.01x faster                                                   |
| pickle_list          | 5.25 us                                                               | 5.30 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 39.2 us: 1.05x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.10 us: 1.15x slower                                                   |
| unpickle             | 18.5 us                                                               | 21.4 us: 1.16x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.3 us: 1.22x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 157 ms: 1.40x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.12 sec: 1.59x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 130 ms: 1.64x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 522 us: 2.01x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 751 us: 2.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.9 ms: 1.43x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.0 ms: 1.59x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.50x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 100 ms: 1.65x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 50.4 ms: 1.84x slower                                                   |
| django_template | 40.7 ms                                                               | 80.7 ms: 1.98x slower                                                   |
| mako            | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.91x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.47 ms: 1.27x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.62 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 692 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 730 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.33 sec: 1.05x faster                                                  |
| regex_effbot               | 4.64 ms                                                               | 4.44 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 865 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 895 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 568 ms: 1.01x faster                                                    |
| pickle                     | 13.4 us                                                               | 13.3 us: 1.01x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                  |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.30 us: 1.01x slower                                                   |
| regex_dna                  | 254 ms                                                                | 257 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.94 us: 1.05x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 39.2 us: 1.05x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.4 ms: 1.07x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.47 sec: 1.13x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 7.10 us: 1.15x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 653 ms: 1.15x slower                                                    |
| unpickle                   | 18.5 us                                                               | 21.4 us: 1.16x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 33.2 ms: 1.17x slower                                                   |
| deepcopy                   | 446 us                                                                | 528 us: 1.19x slower                                                    |
| json                       | 5.54 ms                                                               | 6.65 ms: 1.20x slower                                                   |
| json_loads                 | 30.7 us                                                               | 37.3 us: 1.22x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.26 sec: 1.25x slower                                                  |
| docutils                   | 2.98 sec                                                              | 3.93 sec: 1.32x slower                                                  |
| generators                 | 43.5 ms                                                               | 57.3 ms: 1.32x slower                                                   |
| scimark_fft                | 418 ms                                                                | 560 ms: 1.34x slower                                                    |
| async_generators           | 491 ms                                                                | 658 ms: 1.34x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 67.1 us: 1.35x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 39.2 ms: 1.35x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 5.71 us: 1.39x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 157 ms: 1.40x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.70 ms: 1.40x slower                                                   |
| pylint                     | 355 ms                                                                | 498 ms: 1.41x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.4 ms: 1.42x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.9 ms: 1.43x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.4 ms: 1.46x slower                                                   |
| coverage                   | 87.3 ms                                                               | 129 ms: 1.48x slower                                                    |
| meteor_contest             | 112 ms                                                                | 167 ms: 1.49x slower                                                    |
| tornado_http               | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 149 ms: 1.50x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.98 ms: 1.51x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 96.8 ms: 1.56x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 137 ms: 1.58x slower                                                    |
| comprehensions             | 25.4 us                                                               | 40.3 us: 1.59x slower                                                   |
| python_startup             | 11.4 ms                                                               | 18.0 ms: 1.59x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.12 sec: 1.59x slower                                                  |
| pycparser                  | 1.26 sec                                                              | 2.01 sec: 1.60x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 34.8 ms: 1.61x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 130 ms: 1.64x slower                                                    |
| 2to3                       | 308 ms                                                                | 509 ms: 1.65x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 100 ms: 1.65x slower                                                    |
| fannkuch                   | 443 ms                                                                | 743 ms: 1.67x slower                                                    |
| spectral_norm              | 131 ms                                                                | 220 ms: 1.69x slower                                                    |
| thrift                     | 937 us                                                                | 1.62 ms: 1.73x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 218 ms: 1.73x slower                                                    |
| regex_compile              | 137 ms                                                                | 244 ms: 1.78x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 322 us: 1.78x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.00 sec: 1.79x slower                                                  |
| logging_format             | 8.34 us                                                               | 15.0 us: 1.79x slower                                                   |
| sympy_str                  | 280 ms                                                                | 503 ms: 1.80x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 3.40 sec: 1.81x slower                                                  |
| logging_simple             | 7.63 us                                                               | 13.8 us: 1.81x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.66 sec: 1.81x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 111 ms: 1.81x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 119 ms: 1.83x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 50.4 ms: 1.84x slower                                                   |
| django_template            | 40.7 ms                                                               | 80.7 ms: 1.98x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 309 ms: 2.00x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 522 us: 2.01x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 173 ms: 2.03x slower                                                    |
| sympy_expand               | 454 ms                                                                | 926 ms: 2.04x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 751 us: 2.06x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.3 ms: 2.19x slower                                                   |
| chaos                      | 71.4 ms                                                               | 157 ms: 2.20x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.4 ms: 2.20x slower                                                   |
| float                      | 92.1 ms                                                               | 204 ms: 2.21x slower                                                    |
| logging_silent             | 127 ns                                                                | 281 ns: 2.21x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 326 ms: 2.24x slower                                                    |
| scimark_sor                | 150 ms                                                                | 336 ms: 2.25x slower                                                    |
| raytrace                   | 353 ms                                                                | 803 ms: 2.27x slower                                                    |
| richards_super             | 58.5 ms                                                               | 136 ms: 2.32x slower                                                    |
| richards                   | 50.9 ms                                                               | 118 ms: 2.32x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.26 ms: 2.33x slower                                                   |
| go                         | 157 ms                                                                | 387 ms: 2.46x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.68 ms: 2.51x slower                                                   |
| nbody                      | 105 ms                                                                | 279 ms: 2.67x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.4 ms: 3.02x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 40.1 ms: 5.69x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.51x slower                                                            |

Benchmark hidden because not significant (1): async_tree_none
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.341x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.34x

# Memory
- memory change: 1.07x