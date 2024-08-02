# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.9 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.36x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.4 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 173 ms: 1.26x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 397 us: 1.09x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.0 ms: 1.31x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 33.6 ms: 1.22x slower                                                   |
| django_template | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 80.1 ms: 1.32x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 403 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 443 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 569 ms: 1.36x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.10 sec: 1.28x faster                                                  |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 731 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 714 ms: 1.24x faster                                                    |
| deepcopy                   | 446 us                                                                | 375 us: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.1 ms: 1.11x faster                                                   |
| generators                 | 43.5 ms                                                               | 39.3 ms: 1.11x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.90 us: 1.06x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.28 us: 1.05x faster                                                   |
| float                      | 92.1 ms                                                               | 89.4 ms: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                  |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.8 ms: 1.03x slower                                                   |
| dask                       | 376 ms                                                                | 387 ms: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.5 ms: 1.03x slower                                                   |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                    |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.88 ms: 1.06x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                   |
| fannkuch                   | 443 ms                                                                | 472 ms: 1.06x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                  |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.58 ms: 1.08x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.99 ms: 1.09x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.4 us: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                    |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                   |
| richards                   | 50.9 ms                                                               | 55.6 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 623 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 461 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.9 ms: 1.10x slower                                                   |
| pyflate                    | 559 ms                                                                | 618 ms: 1.11x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.61 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                    |
| sympy_str                  | 280 ms                                                                | 316 ms: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.03 ms: 1.13x slower                                                   |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 70.1 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| pylint                     | 355 ms                                                                | 412 ms: 1.16x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 180 ms: 1.16x slower                                                    |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 25.3 ms: 1.17x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.15 ms: 1.17x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| scimark_sor                | 150 ms                                                                | 176 ms: 1.18x slower                                                    |
| sympy_expand               | 454 ms                                                                | 534 ms: 1.18x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 73.1 ms: 1.18x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 8.57 ms: 1.21x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.22x slower                                                   |
| chaos                      | 71.4 ms                                                               | 87.0 ms: 1.22x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 33.6 ms: 1.22x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.23x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                  |
| django_template            | 40.7 ms                                                               | 50.8 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                    |
| regex_compile              | 137 ms                                                                | 173 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.27x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 8.99 ms: 1.29x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.0 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 80.1 ms: 1.32x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (9): xml_etree_parse, deepcopy_reduce, xml_etree_iterparse, crypto_pyaes, xml_etree_generate, xml_etree_process, asyncio_websockets, bench_thread_pool, tornado_http
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.02x