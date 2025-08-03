# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.019x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                   |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 127 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.79 ms: 1.22x faster                                                   |
| regex_dna      | 254 ms                                                                | 218 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.0 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 77.3 ms: 1.02x faster                                                   |
| unpickle             | 18.5 us                                                               | 18.3 us: 1.01x faster                                                   |
| unpickle_list        | 6.17 us                                                               | 6.48 us: 1.05x slower                                                   |
| pickle_list          | 5.25 us                                                               | 5.68 us: 1.08x slower                                                   |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 399 us: 1.09x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pickle               | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                   |
| genshi_xml     | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 391 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 385 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 331 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.1 us: 1.34x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 662 ms: 1.34x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.79 ms: 1.22x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.3 ms: 1.20x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.9 ms: 1.17x faster                                                   |
| regex_dna                  | 254 ms                                                                | 218 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                   |
| richards_super             | 58.5 ms                                                               | 50.8 ms: 1.15x faster                                                   |
| richards                   | 50.9 ms                                                               | 44.4 ms: 1.15x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| comprehensions             | 25.4 us                                                               | 22.6 us: 1.12x faster                                                   |
| spectral_norm              | 131 ms                                                                | 117 ms: 1.12x faster                                                    |
| float                      | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.56 us: 1.10x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| regex_compile              | 137 ms                                                                | 126 ms: 1.09x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.0 ms: 1.09x faster                                                   |
| pylint                     | 355 ms                                                                | 328 ms: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.7 ms: 1.05x faster                                                   |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                    |
| pyflate                    | 559 ms                                                                | 533 ms: 1.05x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 543 ms: 1.04x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.8 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 145 ms: 1.04x faster                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.64 us: 1.04x faster                                                   |
| scimark_fft                | 418 ms                                                                | 405 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| sympy_str                  | 280 ms                                                                | 272 ms: 1.03x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.8 ms: 1.02x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 77.3 ms: 1.02x faster                                                   |
| unpickle                   | 18.5 us                                                               | 18.3 us: 1.01x faster                                                   |
| 2to3                       | 308 ms                                                                | 310 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 29.5 ms: 1.02x slower                                                   |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 102 ms: 1.03x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.0 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.62 ms: 1.03x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.13 sec: 1.05x slower                                                  |
| unpickle_list              | 6.17 us                                                               | 6.48 us: 1.05x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 64.1 ms: 1.06x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                                  |
| sympy_expand               | 454 ms                                                                | 487 ms: 1.07x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.68 us: 1.08x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.09x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.58 ms: 1.09x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.94 ms: 1.12x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.3 us: 1.14x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                    |
| nbody                      | 105 ms                                                                | 127 ms: 1.21x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.15 sec: 1.25x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.00 ms: 1.59x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.79 ms: 1.98x slower                                                   |
| telco                      | 8.51 ms                                                               | 167 ms: 19.64x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 3.60 sec: 510.90x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (11): chaos, go, async_generators, html5lib, django_template, thrift, mako, meteor_contest, pickle_dict, scimark_lu, logging_silent
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x