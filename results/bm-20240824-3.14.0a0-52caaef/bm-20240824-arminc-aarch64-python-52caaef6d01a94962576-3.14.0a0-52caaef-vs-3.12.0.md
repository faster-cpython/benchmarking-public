# Results vs. 3.12.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.03x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.8 ms: 1.04x slower                                                   |
| tornado_http   | 136 ms                                                                | 125 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                   |
| nbody          | 105 ms                                                                | 108 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| regex_dna      | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 356 us: 1.03x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 78.3 ms: 1.01x faster                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.8 ms: 1.01x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 27.5 ms: 1.00x slower                                                   |
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| django_template | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 423 ms: 1.48x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 557 ms: 1.40x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 419 ms: 1.38x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.34x faster                                                    |
| deepcopy                   | 446 us                                                                | 336 us: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.0 us: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.25x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.0 ms: 1.24x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.24x faster                                                  |
| comprehensions             | 25.4 us                                                               | 20.7 us: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 732 ms: 1.21x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.17 sec: 1.20x faster                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                   |
| raytrace                   | 353 ms                                                                | 303 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                   |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.61 us: 1.10x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 125 ms: 1.08x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.71 ms: 1.07x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.23 ms: 1.06x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.89 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 82.1 ms: 1.06x faster                                                   |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.6 ms: 1.05x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.5 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                                   |
| pickle_pure_python         | 365 us                                                                | 356 us: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                   |
| thrift                     | 937 us                                                                | 921 us: 1.02x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 59.8 ms: 1.01x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.37 sec: 1.01x faster                                                  |
| async_generators           | 491 ms                                                                | 485 ms: 1.01x faster                                                    |
| float                      | 92.1 ms                                                               | 91.2 ms: 1.01x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 98.3 ms: 1.01x faster                                                   |
| pyflate                    | 559 ms                                                                | 554 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.87 sec: 1.01x faster                                                  |
| regex_dna                  | 254 ms                                                                | 252 ms: 1.01x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 78.3 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 909 ms: 1.01x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 27.5 ms: 1.00x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                  |
| richards_super             | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                                   |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| sqlglot_optimize           | 61.3 ms                                                               | 62.2 ms: 1.01x slower                                                   |
| json                       | 5.54 ms                                                               | 5.66 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                   |
| fannkuch                   | 443 ms                                                                | 458 ms: 1.03x slower                                                    |
| nbody                      | 105 ms                                                                | 108 ms: 1.03x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.03x slower                                                  |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.0 ms: 1.04x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 67.8 ms: 1.04x slower                                                   |
| django_template            | 40.7 ms                                                               | 42.4 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.49 ms: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.88 ms: 1.05x slower                                                   |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| scimark_fft                | 418 ms                                                                | 443 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 192 us: 1.06x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| spectral_norm              | 131 ms                                                                | 140 ms: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.07x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 4.91 ms: 1.12x slower                                                   |
| coverage                   | 87.3 ms                                                               | 98.4 ms: 1.13x slower                                                   |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.77 ms: 1.15x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.31 ms: 1.20x slower                                                   |
| go                         | 157 ms                                                                | 193 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (10): bench_mp_pool, meteor_contest, asyncio_tcp, asyncio_websockets, xml_etree_iterparse, xml_etree_generate, hexiom, pidigits, pylint, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-52caaef/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: bpe_tokeniser

# HPT report

- Reliability score: 99.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x