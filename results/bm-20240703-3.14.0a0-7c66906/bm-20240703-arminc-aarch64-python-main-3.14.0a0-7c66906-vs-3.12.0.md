# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.03x faster
- HPT reliability: 83.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 304 ms: 1.01x faster                                    |
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                  |
| html5lib       | 65.1 ms                                                               | 68.8 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                    |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.29x faster                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                    |
| float          | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                   |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.07x faster                                    |
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                   |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.02x faster                                    |
| unpickle_pure_python | 260 us                                                                | 254 us: 1.02x faster                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                  |
| pickle_pure_python   | 365 us                                                                | 361 us: 1.01x faster                                    |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                   |
| json_loads           | 30.7 us                                                               | 33.2 us: 1.08x slower                                   |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                   |
| python_startup         | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                   |
| Geometric mean         | (ref)                                                                 | 1.11x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                   |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                   |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                   |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 437 ms: 1.43x faster                                    |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                    |
| async_tree_memoization     | 777 ms                                                                | 556 ms: 1.40x faster                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 534 ms: 1.39x faster                                    |
| deepcopy                   | 446 us                                                                | 335 us: 1.33x faster                                    |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.09 sec: 1.29x faster                                  |
| deepcopy_memo              | 49.6 us                                                               | 39.1 us: 1.27x faster                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                    |
| comprehensions             | 25.4 us                                                               | 20.9 us: 1.22x faster                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.47 us: 1.18x faster                                   |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                    |
| generators                 | 43.5 ms                                                               | 38.0 ms: 1.15x faster                                   |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                   |
| logging_simple             | 7.63 us                                                               | 6.92 us: 1.10x faster                                   |
| logging_format             | 8.34 us                                                               | 7.61 us: 1.10x faster                                   |
| scimark_lu                 | 146 ms                                                                | 136 ms: 1.07x faster                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.07x faster                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.07x faster                                   |
| deltablue                  | 4.12 ms                                                               | 3.87 ms: 1.06x faster                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.7 ms: 1.06x faster                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                   |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                    |
| chaos                      | 71.4 ms                                                               | 68.0 ms: 1.05x faster                                   |
| dulwich_log                | 62.0 ms                                                               | 59.3 ms: 1.05x faster                                   |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                   |
| dask                       | 376 ms                                                                | 367 ms: 1.03x faster                                    |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                  |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                  |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.02x faster                                    |
| unpickle_pure_python       | 260 us                                                                | 254 us: 1.02x faster                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.8 ms: 1.01x faster                                   |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                  |
| sympy_integrate            | 21.6 ms                                                               | 21.3 ms: 1.01x faster                                   |
| 2to3                       | 308 ms                                                                | 304 ms: 1.01x faster                                    |
| pickle_pure_python         | 365 us                                                                | 361 us: 1.01x faster                                    |
| nqueens                    | 99.2 ms                                                               | 99.9 ms: 1.01x slower                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                    |
| thrift                     | 937 us                                                                | 943 us: 1.01x slower                                    |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                    |
| float                      | 92.1 ms                                                               | 92.9 ms: 1.01x slower                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                  |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.3 ms: 1.02x slower                                   |
| richards_super             | 58.5 ms                                                               | 59.6 ms: 1.02x slower                                   |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                   |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                    |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 63.0 ms: 1.03x slower                                   |
| sympy_expand               | 454 ms                                                                | 466 ms: 1.03x slower                                    |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                   |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                  |
| sqlglot_normalize          | 126 ms                                                                | 130 ms: 1.04x slower                                    |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                   |
| richards                   | 50.9 ms                                                               | 53.2 ms: 1.04x slower                                   |
| pyflate                    | 559 ms                                                                | 586 ms: 1.05x slower                                    |
| fannkuch                   | 443 ms                                                                | 466 ms: 1.05x slower                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                  |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.55 ms: 1.06x slower                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                   |
| html5lib                   | 65.1 ms                                                               | 68.8 ms: 1.06x slower                                   |
| pprint_safe_repr           | 916 ms                                                                | 970 ms: 1.06x slower                                    |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                   |
| scimark_fft                | 418 ms                                                                | 446 ms: 1.07x slower                                    |
| json_loads                 | 30.7 us                                                               | 33.2 us: 1.08x slower                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                    |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                   |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                    |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                    |
| gc_traversal               | 4.40 ms                                                               | 4.86 ms: 1.11x slower                                   |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                   |
| python_startup             | 11.4 ms                                                               | 13.2 ms: 1.16x slower                                   |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                   |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                            |

Benchmark hidden because not significant (9): pylint, tornado_http, async_generators, asyncio_tcp, asyncio_websockets, regex_dna, bench_mp_pool, genshi_xml, meteor_contest
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906.json: bpe_tokeniser

# HPT report

- Reliability score: 83.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x