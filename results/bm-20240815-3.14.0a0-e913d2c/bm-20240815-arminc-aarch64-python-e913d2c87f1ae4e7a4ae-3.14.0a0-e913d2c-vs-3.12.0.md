# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-aarch64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.03x faster
- HPT reliability: 95.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.6 ms: 1.04x slower                                                   |
| tornado_http   | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                    |
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 547 ms: 1.42x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 531 ms: 1.39x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 699 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 92.5 ms: 1.00x slower                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 357 us: 1.02x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| json_loads           | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                   |
| django_template | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 398 ms: 1.45x faster                                                    |
| async_tree_none            | 624 ms                                                                | 433 ms: 1.44x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 547 ms: 1.42x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 531 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 332 us: 1.34x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.09 sec: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 699 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.26x faster                                                  |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 729 ms: 1.25x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.42 us: 1.20x faster                                                   |
| raytrace                   | 353 ms                                                                | 298 ms: 1.18x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.59 us: 1.10x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.98 us: 1.09x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.79 ms: 1.09x faster                                                   |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 127 ms: 1.07x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.24 ms: 1.06x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.4 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.0 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.9 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.31 sec: 1.03x faster                                                  |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 357 us: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 302 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                  |
| float                      | 92.1 ms                                                               | 92.5 ms: 1.00x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 27.8 ms: 1.01x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.07 ms: 1.01x slower                                                   |
| pyflate                    | 559 ms                                                                | 566 ms: 1.01x slower                                                    |
| sympy_expand               | 454 ms                                                                | 461 ms: 1.02x slower                                                    |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 934 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.93 sec: 1.02x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 581 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.37 ms: 1.03x slower                                                   |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 42.0 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| richards_super             | 58.5 ms                                                               | 60.6 ms: 1.04x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 67.6 ms: 1.04x slower                                                   |
| thrift                     | 937 us                                                                | 975 us: 1.04x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.11 sec: 1.04x slower                                                  |
| fannkuch                   | 443 ms                                                                | 463 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.4 ms: 1.05x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.5 us: 1.06x slower                                                   |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                    |
| scimark_fft                | 418 ms                                                                | 445 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 201 us: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.4 ms: 1.12x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.05 ms: 1.15x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.88 ms: 1.16x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.30 ms: 1.20x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (11): async_generators, xml_etree_generate, bench_mp_pool, nqueens, genshi_xml, asyncio_websockets, sqlglot_optimize, meteor_contest, pylint, xml_etree_process, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: bpe_tokeniser

# HPT report

- Reliability score: 95.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x