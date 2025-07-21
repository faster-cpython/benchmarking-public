# Results vs. 3.12.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-aarch64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.085x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 349 ms: 1.13x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.21 sec: 1.07x slower                                                  |
| html5lib       | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 826 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 441 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 842 ms: 1.68x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 632 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.57x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 94.2 ms: 1.02x slower                                                   |
| nbody          | 105 ms                                                                | 180 ms: 1.72x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.87 ms: 1.20x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 25.7 ms: 1.10x faster                                                   |
| regex_dna      | 254 ms                                                                | 236 ms: 1.08x faster                                                    |
| regex_compile  | 137 ms                                                                | 149 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 135 ms: 1.11x faster                                                    |
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.09x faster                                                    |
| pickle_dict          | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.66 us: 1.08x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.82 sec: 1.09x slower                                                  |
| unpickle             | 18.5 us                                                               | 20.1 us: 1.09x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.95 us: 1.13x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 296 us: 1.14x slower                                                    |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| json_loads           | 30.7 us                                                               | 37.0 us: 1.20x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 441 us: 1.21x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 15.0 ms: 1.23x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 140 ms: 1.25x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 102 ms: 1.30x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| python_startup         | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.59x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 74.6 ms: 1.23x slower                                                   |
| django_template | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 36.7 ms: 1.34x slower                                                   |
| mako            | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.36x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.93 sec: 1.77x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 826 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 441 ms: 1.68x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 842 ms: 1.68x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                                    |
| async_tree_none            | 624 ms                                                                | 392 ms: 1.59x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 367 ms: 1.57x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 2.84 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 632 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.87 ms: 1.20x faster                                                   |
| deepcopy                   | 446 us                                                                | 390 us: 1.14x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 135 ms: 1.11x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 25.7 ms: 1.10x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.44 us: 1.09x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.09x faster                                                    |
| regex_dna                  | 254 ms                                                                | 236 ms: 1.08x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.4 ms: 1.08x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 46.5 us: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                   |
| comprehensions             | 25.4 us                                                               | 24.4 us: 1.04x faster                                                   |
| go                         | 157 ms                                                                | 151 ms: 1.04x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 60.3 ms: 1.03x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| float                      | 92.1 ms                                                               | 94.2 ms: 1.02x slower                                                   |
| async_generators           | 491 ms                                                                | 506 ms: 1.03x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                   |
| pyflate                    | 559 ms                                                                | 588 ms: 1.05x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.15 us: 1.07x slower                                                   |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                    |
| pylint                     | 355 ms                                                                | 379 ms: 1.07x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                  |
| deepcopy_reduce            | 4.10 us                                                               | 4.40 us: 1.07x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.21 sec: 1.07x slower                                                  |
| pickle_list                | 5.25 us                                                               | 5.66 us: 1.08x slower                                                   |
| regex_compile              | 137 ms                                                                | 149 ms: 1.08x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.82 sec: 1.09x slower                                                  |
| unpickle                   | 18.5 us                                                               | 20.1 us: 1.09x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 31.6 ms: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 70.9 ms: 1.09x slower                                                   |
| logging_format             | 8.34 us                                                               | 9.10 us: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                    |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.42 sec: 1.11x slower                                                  |
| hexiom                     | 6.98 ms                                                               | 7.72 ms: 1.11x slower                                                   |
| raytrace                   | 353 ms                                                                | 393 ms: 1.11x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.63 ms: 1.12x slower                                                   |
| scimark_fft                | 418 ms                                                                | 470 ms: 1.12x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.95 us: 1.13x slower                                                   |
| 2to3                       | 308 ms                                                                | 349 ms: 1.13x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 296 us: 1.14x slower                                                    |
| json                       | 5.54 ms                                                               | 6.34 ms: 1.14x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.05 sec: 1.15x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.17 sec: 1.15x slower                                                  |
| chaos                      | 71.4 ms                                                               | 82.8 ms: 1.16x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.17x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.25 ms: 1.17x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 25.4 ms: 1.17x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 184 ms: 1.19x slower                                                    |
| json_loads                 | 30.7 us                                                               | 37.0 us: 1.20x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 441 us: 1.21x slower                                                    |
| sympy_str                  | 280 ms                                                                | 339 ms: 1.21x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.56 ms: 1.22x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 15.0 ms: 1.23x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 74.6 ms: 1.23x slower                                                   |
| meteor_contest             | 112 ms                                                                | 139 ms: 1.24x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 140 ms: 1.25x slower                                                    |
| django_template            | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 107 ms: 1.26x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 110 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 186 ms: 1.28x slower                                                    |
| thrift                     | 937 us                                                                | 1.20 ms: 1.28x slower                                                   |
| sympy_expand               | 454 ms                                                                | 584 ms: 1.29x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 102 ms: 1.30x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.7 ms: 1.34x slower                                                   |
| fannkuch                   | 443 ms                                                                | 598 ms: 1.35x slower                                                    |
| richards_super             | 58.5 ms                                                               | 79.8 ms: 1.37x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 247 us: 1.37x slower                                                    |
| richards                   | 50.9 ms                                                               | 70.8 ms: 1.39x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.82 ms: 1.39x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.0 ms: 1.43x slower                                                   |
| coverage                   | 87.3 ms                                                               | 144 ms: 1.65x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.3 ms: 1.65x slower                                                   |
| nbody                      | 105 ms                                                                | 180 ms: 1.72x slower                                                    |
| python_startup             | 11.4 ms                                                               | 20.0 ms: 1.76x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 66.4 ms: 9.42x slower                                                   |
| telco                      | 8.51 ms                                                               | 189 ms: 22.24x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                            |

Benchmark hidden because not significant (2): asyncio_tcp, pidigits
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-arminc-aarch64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.085x slower

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.34x