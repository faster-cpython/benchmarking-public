# Results vs. 3.12.0

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: linux-aarch64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.028x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                  |
| html5lib       | 65.1 ms                                                               | 61.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 381 ms: 1.63x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 81.3 ms: 1.13x faster                                                   |
| pidigits       | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 127 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.78 ms: 1.23x faster                                                   |
| regex_dna      | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 121 ms: 1.14x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 76.7 ms: 1.03x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| pickle_pure_python  | 365 us                                                                | 390 us: 1.07x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 62.1 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                  |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.63x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 481 ms: 1.62x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 880 ms: 1.60x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 471 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 900 ms: 1.56x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 382 ms: 1.51x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 35.9 us: 1.38x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 660 ms: 1.38x faster                                                    |
| deepcopy                   | 446 us                                                                | 330 us: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 654 ms: 1.35x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.78 ms: 1.23x faster                                                   |
| richards                   | 50.9 ms                                                               | 43.0 ms: 1.18x faster                                                   |
| richards_super             | 58.5 ms                                                               | 49.5 ms: 1.18x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.5 ms: 1.18x faster                                                   |
| generators                 | 43.5 ms                                                               | 36.9 ms: 1.18x faster                                                   |
| logging_simple             | 7.63 us                                                               | 6.65 us: 1.15x faster                                                   |
| comprehensions             | 25.4 us                                                               | 22.2 us: 1.14x faster                                                   |
| regex_dna                  | 254 ms                                                                | 223 ms: 1.14x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.34 us: 1.14x faster                                                   |
| spectral_norm              | 131 ms                                                                | 115 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 121 ms: 1.14x faster                                                    |
| float                      | 92.1 ms                                                               | 81.3 ms: 1.13x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.63 us: 1.13x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.31 sec: 1.12x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.11x faster                                                   |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.80 ms: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 61.1 ms: 1.06x faster                                                   |
| go                         | 157 ms                                                                | 150 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                   |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.05x faster                                                    |
| pyflate                    | 559 ms                                                                | 535 ms: 1.05x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.9 ms: 1.04x faster                                                   |
| chaos                      | 71.4 ms                                                               | 68.8 ms: 1.04x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.03x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 76.7 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                    |
| scimark_fft                | 418 ms                                                                | 409 ms: 1.02x faster                                                    |
| async_generators           | 491 ms                                                                | 481 ms: 1.02x faster                                                    |
| meteor_contest             | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 667 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.03 sec: 1.02x slower                                                  |
| genshi_xml                 | 60.6 ms                                                               | 62.1 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                   |
| pidigits                   | 233 ms                                                                | 239 ms: 1.03x slower                                                    |
| fannkuch                   | 443 ms                                                                | 457 ms: 1.03x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.21 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.82 ms: 1.05x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 390 us: 1.07x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.9 us: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.35 sec: 1.07x slower                                                  |
| sympy_expand               | 454 ms                                                                | 487 ms: 1.07x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 31.5 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.10 ms: 1.15x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                  |
| nbody                      | 105 ms                                                                | 127 ms: 1.22x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.81 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.81 ms: 1.98x slower                                                   |
| telco                      | 8.51 ms                                                               | 163 ms: 19.10x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (14): sympy_sum, unpickle_pure_python, sympy_integrate, genshi_text, json_dumps, django_template, mako, sympy_str, sqlite_synth, 2to3, logging_silent, nqueens, thrift, crypto_pyaes
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.12x