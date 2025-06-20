# Results vs. 3.12.0

- fork: python
- ref: 7cc89496922b7edb033e
- machine: linux-aarch64
- commit hash: 7cc8949
- commit date: 2025-06-19
- overall geometric mean: 1.065x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| html5lib       | 65.1 ms                                                               | 62.8 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 894 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 654 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.1 ms: 1.07x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 120 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.85 ms: 1.21x faster                                                   |
| regex_dna      | 254 ms                                                                | 219 ms: 1.16x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 394 us: 1.08x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                   |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.69 sec: 2.02x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 463 ms: 1.68x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 460 ms: 1.61x faster                                                    |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 894 ms: 1.58x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 375 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 654 ms: 1.39x faster                                                    |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 38.2 us: 1.30x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.24x faster                                                   |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.85 ms: 1.21x faster                                                   |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                                   |
| regex_dna                  | 254 ms                                                                | 219 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.58 us: 1.14x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 54.2 ms: 1.14x faster                                                   |
| pylint                     | 355 ms                                                                | 317 ms: 1.12x faster                                                    |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                   |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.09x faster                                                    |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                    |
| pyflate                    | 559 ms                                                                | 522 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.1 ms: 1.07x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.06x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 26.9 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.9 ms: 1.05x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 83.5 ms: 1.04x faster                                                   |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.8 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 297 ms: 1.04x faster                                                    |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.04x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                   |
| meteor_contest             | 112 ms                                                                | 109 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                  |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| logging_simple             | 7.63 us                                                               | 7.56 us: 1.01x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| thrift                     | 937 us                                                                | 943 us: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.60 ms: 1.03x slower                                                   |
| sympy_expand               | 454 ms                                                                | 467 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.07x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 155 ms: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                   |
| fannkuch                   | 443 ms                                                                | 480 ms: 1.08x slower                                                    |
| richards                   | 50.9 ms                                                               | 55.6 ms: 1.09x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.01 sec: 1.10x slower                                                  |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.08 sec: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.85 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.44 ms: 1.11x slower                                                   |
| nbody                      | 105 ms                                                                | 120 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.97 ms: 1.59x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.96x slower                                                   |
| logging_silent             | 127 ns                                                                | 627 ns: 4.94x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (10): chaos, django_template, nqueens, sympy_sum, logging_format, scimark_fft, hexiom, genshi_xml, coroutines, unpickle_pure_python
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250619-3.15.0a0-7cc8949/bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x