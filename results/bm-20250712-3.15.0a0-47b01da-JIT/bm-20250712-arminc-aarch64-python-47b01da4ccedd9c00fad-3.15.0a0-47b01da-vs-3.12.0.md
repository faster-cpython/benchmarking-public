# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.010x faster
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 313 ms: 1.02x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                  |
| html5lib       | 65.1 ms                                                               | 64.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 491 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 480 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 920 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 676 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| nbody          | 105 ms                                                                | 129 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                   |
| regex_dna      | 254 ms                                                                | 222 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.30 sec: 1.13x faster                                                  |
| xml_etree_parse     | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 106 ms: 1.05x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| xml_etree_process   | 79.0 ms                                                               | 76.0 ms: 1.04x faster                                                   |
| unpickle_list       | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| pickle_list         | 5.25 us                                                               | 5.60 us: 1.07x slower                                                   |
| json_loads          | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 406 us: 1.11x slower                                                    |
| pickle              | 13.4 us                                                               | 15.9 us: 1.19x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 491 ms: 1.58x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 480 ms: 1.54x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 920 ms: 1.53x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 386 ms: 1.49x faster                                                    |
| deepcopy                   | 446 us                                                                | 324 us: 1.38x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 676 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 665 ms: 1.33x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 39.0 us: 1.27x faster                                                   |
| generators                 | 43.5 ms                                                               | 35.5 ms: 1.22x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                   |
| comprehensions             | 25.4 us                                                               | 21.7 us: 1.17x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 53.4 ms: 1.16x faster                                                   |
| regex_dna                  | 254 ms                                                                | 222 ms: 1.14x faster                                                    |
| richards                   | 50.9 ms                                                               | 44.8 ms: 1.14x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.61 us: 1.14x faster                                                   |
| richards_super             | 58.5 ms                                                               | 51.7 ms: 1.13x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.30 sec: 1.13x faster                                                  |
| float                      | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                                   |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                    |
| pylint                     | 355 ms                                                                | 323 ms: 1.10x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.03 us: 1.09x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.72 us: 1.08x faster                                                   |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 106 ms: 1.05x faster                                                    |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.0 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.05x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.5 ms: 1.05x faster                                                   |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.96 ms: 1.04x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 76.0 ms: 1.04x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.66 us: 1.03x faster                                                   |
| async_generators           | 491 ms                                                                | 479 ms: 1.02x faster                                                    |
| scimark_fft                | 418 ms                                                                | 410 ms: 1.02x faster                                                    |
| pyflate                    | 559 ms                                                                | 550 ms: 1.02x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 64.0 ms: 1.02x faster                                                   |
| go                         | 157 ms                                                                | 155 ms: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 29.3 ms: 1.01x slower                                                   |
| 2to3                       | 308 ms                                                                | 313 ms: 1.02x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.02x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| thrift                     | 937 us                                                                | 958 us: 1.02x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.5 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 63.6 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.05x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.14 sec: 1.05x slower                                                  |
| pickle_list                | 5.25 us                                                               | 5.60 us: 1.07x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.48 ms: 1.07x slower                                                   |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| sympy_expand               | 454 ms                                                                | 495 ms: 1.09x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 406 us: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.00 ms: 1.13x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 213 us: 1.18x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.19x slower                                                   |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                    |
| nbody                      | 105 ms                                                                | 129 ms: 1.24x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.35 sec: 1.25x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                                  |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.77 ms: 1.97x slower                                                   |
| telco                      | 8.51 ms                                                               | 165 ms: 19.41x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 1.25 sec: 176.80x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                            |

Benchmark hidden because not significant (12): chaos, scimark_monte_carlo, sympy_integrate, unpickle_pure_python, django_template, sympy_sum, sympy_str, asyncio_tcp, mako, unpickle, genshi_text, pickle_dict
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x