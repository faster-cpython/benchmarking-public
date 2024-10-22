# Results vs. 3.12.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.04x faster
- HPT reliability: 95.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                   |
| tornado_http   | 136 ms                                                                | 121 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                                    |
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.31x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 356 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| django_template | 40.7 ms                                                               | 42.9 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 400 ms: 1.44x faster                                                    |
| async_tree_none            | 624 ms                                                                | 438 ms: 1.42x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 549 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 533 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.08 sec: 1.31x faster                                                  |
| generators                 | 43.5 ms                                                               | 34.4 ms: 1.26x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 726 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.40 us: 1.21x faster                                                   |
| raytrace                   | 353 ms                                                                | 294 ms: 1.20x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                   |
| tornado_http               | 136 ms                                                                | 121 ms: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.77 ms: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.7 ms: 1.05x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.25 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.8 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 356 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                   |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.55 sec: 1.02x faster                                                  |
| async_generators           | 491 ms                                                                | 482 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.38 sec: 1.01x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.6 ms: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 61.8 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                  |
| float                      | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 127 ms: 1.01x slower                                                    |
| go                         | 157 ms                                                                | 159 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 576 ms: 1.02x slower                                                    |
| richards                   | 50.9 ms                                                               | 51.9 ms: 1.02x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 66.4 ms: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 957 us: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| logging_silent             | 127 ns                                                                | 130 ns: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 464 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 942 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.37 ms: 1.03x slower                                                   |
| scimark_sor                | 150 ms                                                                | 154 ms: 1.03x slower                                                    |
| pyflate                    | 559 ms                                                                | 577 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.81 ms: 1.05x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.9 ms: 1.05x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.92 ms: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.79 ms: 1.09x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.6 ms: 1.12x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.29 ms: 1.19x slower                                                   |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                            |

Benchmark hidden because not significant (9): sqlglot_parse, bench_mp_pool, nqueens, richards_super, regex_dna, hexiom, asyncio_websockets, meteor_contest, pylint
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: bpe_tokeniser

# HPT report

- Reliability score: 95.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x