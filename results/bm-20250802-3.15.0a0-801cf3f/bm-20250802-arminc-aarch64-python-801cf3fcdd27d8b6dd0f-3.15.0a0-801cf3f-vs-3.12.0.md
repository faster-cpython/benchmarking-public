# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| html5lib       | 65.1 ms                                                               | 60.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 456 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 451 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 363 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 654 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.56x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.7 ms: 1.09x faster                                                   |
| pidigits       | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.86 ms: 1.20x faster                                                   |
| regex_dna      | 254 ms                                                                | 222 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 121 ms: 1.13x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| xml_etree_generate  | 112 ms                                                                | 110 ms: 1.02x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 6.47 us: 1.05x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.59 us: 1.07x slower                                                   |
| json_loads          | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 396 us: 1.09x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| pickle              | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, unpickle, unpickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.58 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 456 ms: 1.70x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 451 ms: 1.64x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 879 ms: 1.61x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 363 ms: 1.59x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 906 ms: 1.55x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 654 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 646 ms: 1.37x faster                                                    |
| deepcopy                   | 446 us                                                                | 329 us: 1.35x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 36.7 us: 1.35x faster                                                   |
| comprehensions             | 25.4 us                                                               | 19.9 us: 1.27x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.3 ms: 1.23x faster                                                   |
| go                         | 157 ms                                                                | 128 ms: 1.23x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.86 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.50 us: 1.17x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 53.9 ms: 1.15x faster                                                   |
| regex_dna                  | 254 ms                                                                | 222 ms: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                   |
| regex_compile              | 137 ms                                                                | 121 ms: 1.13x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.11x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.56 us: 1.10x faster                                                   |
| pylint                     | 355 ms                                                                | 321 ms: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.09x faster                                                    |
| float                      | 92.1 ms                                                               | 84.7 ms: 1.09x faster                                                   |
| pyflate                    | 559 ms                                                                | 515 ms: 1.09x faster                                                    |
| async_generators           | 491 ms                                                                | 453 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.1 ms: 1.08x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 60.8 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 531 ms: 1.07x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                   |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.82 sec: 1.03x faster                                                  |
| scimark_lu                 | 146 ms                                                                | 142 ms: 1.02x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                    |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 896 ms: 1.02x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.94 sec: 1.01x faster                                                  |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 29.5 ms: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 238 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.58 ms: 1.02x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 462 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 980 us: 1.05x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.47 us: 1.05x slower                                                   |
| json                       | 5.54 ms                                                               | 5.81 ms: 1.05x slower                                                   |
| richards                   | 50.9 ms                                                               | 53.5 ms: 1.05x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.59 us: 1.07x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 195 us: 1.08x slower                                                    |
| richards_super             | 58.5 ms                                                               | 63.2 ms: 1.08x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.05 ms: 1.14x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                   |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.88 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.74 ms: 1.95x slower                                                   |
| telco                      | 8.51 ms                                                               | 164 ms: 19.30x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.99 sec: 424.06x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (19): regex_v8, crypto_pyaes, chaos, sympy_str, meteor_contest, django_template, nqueens, pycparser, hexiom, xml_etree_process, asyncio_tcp_ssl, unpickle, genshi_text, genshi_xml, unpickle_pure_python, logging_silent, scimark_fft, pickle_dict, sympy_expand
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x