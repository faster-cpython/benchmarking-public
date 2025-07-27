# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.087x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 354 ms: 1.15x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.4 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 824 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 445 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 863 ms: 1.63x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 366 ms: 1.58x faster                                                    |
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.56x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 93.8 ms: 1.02x slower                                                   |
| nbody          | 105 ms                                                                | 182 ms: 1.74x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.76 ms: 1.23x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 26.2 ms: 1.08x faster                                                   |
| regex_dna      | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| regex_compile  | 137 ms                                                                | 149 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 133 ms: 1.13x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.07x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.9 us: 1.04x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.60 us: 1.07x slower                                                   |
| unpickle             | 18.5 us                                                               | 20.2 us: 1.10x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.89 sec: 1.11x slower                                                  |
| pickle               | 13.4 us                                                               | 15.0 us: 1.12x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.96 us: 1.13x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 301 us: 1.16x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.6 us: 1.23x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 452 us: 1.24x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 139 ms: 1.24x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 100 ms: 1.27x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.2 ms: 1.45x slower                                                   |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 51.3 ms: 1.26x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.7 ms: 1.30x slower                                                   |
| mako            | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.36x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.93 sec: 1.76x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 824 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 445 ms: 1.66x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 863 ms: 1.63x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 366 ms: 1.58x faster                                                    |
| async_tree_none            | 624 ms                                                                | 397 ms: 1.57x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.92 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 633 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 674 ms: 1.35x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.76 ms: 1.23x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 133 ms: 1.13x faster                                                    |
| deepcopy                   | 446 us                                                                | 395 us: 1.13x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.44 us: 1.10x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 26.2 ms: 1.08x faster                                                   |
| generators                 | 43.5 ms                                                               | 40.3 ms: 1.08x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 46.1 us: 1.08x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.07x faster                                                    |
| regex_dna                  | 254 ms                                                                | 240 ms: 1.06x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.5 ms: 1.05x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 59.3 ms: 1.05x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.02x slower                                                    |
| float                      | 92.1 ms                                                               | 93.8 ms: 1.02x slower                                                   |
| async_generators           | 491 ms                                                                | 500 ms: 1.02x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.27 us: 1.04x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 38.9 us: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 588 ms: 1.05x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.03 us: 1.05x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                  |
| pickle_list                | 5.25 us                                                               | 5.60 us: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 70.4 ms: 1.08x slower                                                   |
| regex_compile              | 137 ms                                                                | 149 ms: 1.08x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 31.4 ms: 1.08x slower                                                   |
| pylint                     | 355 ms                                                                | 385 ms: 1.08x slower                                                    |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.09x slower                                                    |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.09x slower                                                    |
| logging_format             | 8.34 us                                                               | 9.09 us: 1.09x slower                                                   |
| unpickle                   | 18.5 us                                                               | 20.2 us: 1.10x slower                                                   |
| logging_silent             | 127 ns                                                                | 140 ns: 1.11x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.89 sec: 1.11x slower                                                  |
| raytrace                   | 353 ms                                                                | 394 ms: 1.12x slower                                                    |
| scimark_fft                | 418 ms                                                                | 467 ms: 1.12x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.81 ms: 1.12x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.45 sec: 1.12x slower                                                  |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.96 us: 1.13x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.04 sec: 1.14x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.14 sec: 1.14x slower                                                  |
| chaos                      | 71.4 ms                                                               | 81.9 ms: 1.15x slower                                                   |
| json                       | 5.54 ms                                                               | 6.36 ms: 1.15x slower                                                   |
| 2to3                       | 308 ms                                                                | 354 ms: 1.15x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.74 ms: 1.15x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 301 us: 1.16x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.28 ms: 1.19x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 186 ms: 1.21x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 26.1 ms: 1.21x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 103 ms: 1.22x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 121 ms: 1.22x slower                                                    |
| meteor_contest             | 112 ms                                                                | 136 ms: 1.22x slower                                                    |
| json_loads                 | 30.7 us                                                               | 37.6 us: 1.23x slower                                                   |
| sympy_str                  | 280 ms                                                                | 345 ms: 1.23x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 452 us: 1.24x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 107 ms: 1.24x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 139 ms: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.71 ms: 1.25x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 75.7 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.3 ms: 1.26x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 100 ms: 1.27x slower                                                    |
| thrift                     | 937 us                                                                | 1.20 ms: 1.29x slower                                                   |
| sympy_expand               | 454 ms                                                                | 589 ms: 1.30x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 35.7 ms: 1.30x slower                                                   |
| fannkuch                   | 443 ms                                                                | 596 ms: 1.34x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 244 us: 1.35x slower                                                    |
| richards                   | 50.9 ms                                                               | 70.8 ms: 1.39x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.83 ms: 1.40x slower                                                   |
| richards_super             | 58.5 ms                                                               | 82.2 ms: 1.41x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.2 ms: 1.45x slower                                                   |
| coverage                   | 87.3 ms                                                               | 143 ms: 1.63x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| nbody                      | 105 ms                                                                | 182 ms: 1.74x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 64.7 ms: 9.17x slower                                                   |
| telco                      | 8.51 ms                                                               | 189 ms: 22.16x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (4): comprehensions, go, pidigits, asyncio_tcp
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.087x slower

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.33x