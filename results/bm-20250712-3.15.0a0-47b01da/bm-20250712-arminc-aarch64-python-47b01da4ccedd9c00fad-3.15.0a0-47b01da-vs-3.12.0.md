# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 374 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 872 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                   |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.85 ms: 1.20x faster                                                   |
| regex_dna      | 254 ms                                                                | 221 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| xml_etree_generate  | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| unpickle_list       | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| json_loads          | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| pickle_pure_python  | 365 us                                                                | 393 us: 1.08x slower                                                    |
| pickle_list         | 5.25 us                                                               | 5.86 us: 1.12x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                   |
| pickle              | 13.4 us                                                               | 15.5 us: 1.16x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, unpickle_pure_python, unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                                   |
| mako           | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                  |
| async_tree_none            | 624 ms                                                                | 374 ms: 1.67x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 473 ms: 1.64x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 872 ms: 1.62x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                    |
| deepcopy                   | 446 us                                                                | 321 us: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 659 ms: 1.38x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.2 us: 1.33x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.0 us: 1.27x faster                                                   |
| go                         | 157 ms                                                                | 127 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.4 ms: 1.23x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.85 ms: 1.20x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 52.8 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.55 us: 1.15x faster                                                   |
| regex_dna                  | 254 ms                                                                | 221 ms: 1.15x faster                                                    |
| regex_compile              | 137 ms                                                                | 122 ms: 1.13x faster                                                    |
| pylint                     | 355 ms                                                                | 319 ms: 1.11x faster                                                    |
| spectral_norm              | 131 ms                                                                | 118 ms: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.65 us: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| float                      | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.12 us: 1.07x faster                                                   |
| pyflate                    | 559 ms                                                                | 522 ms: 1.07x faster                                                    |
| chaos                      | 71.4 ms                                                               | 66.7 ms: 1.07x faster                                                   |
| async_generators           | 491 ms                                                                | 460 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.5 ms: 1.06x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                  |
| asyncio_tcp                | 566 ms                                                                | 543 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                                | 108 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.82 sec: 1.04x faster                                                  |
| pprint_safe_repr           | 916 ms                                                                | 884 ms: 1.04x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 4.00 ms: 1.03x faster                                                   |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                    |
| hexiom                     | 6.98 ms                                                               | 6.79 ms: 1.03x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                  |
| genshi_xml                 | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                  |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 146 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.80 us: 1.01x slower                                                   |
| thrift                     | 937 us                                                                | 946 us: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 673 ms: 1.02x slower                                                    |
| richards                   | 50.9 ms                                                               | 52.2 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.59 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.74 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.5 ms: 1.05x slower                                                   |
| fannkuch                   | 443 ms                                                                | 467 ms: 1.05x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.55 us: 1.06x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.8 us: 1.07x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 393 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.90 ms: 1.11x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.86 us: 1.12x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.5 us: 1.16x slower                                                   |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                    |
| coverage                   | 87.3 ms                                                               | 105 ms: 1.20x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.17 ms: 1.63x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 4.13 ms: 2.15x slower                                                   |
| telco                      | 8.51 ms                                                               | 166 ms: 19.51x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 2.81 sec: 398.00x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (17): pathlib, scimark_sor, crypto_pyaes, sympy_str, nqueens, genshi_text, xml_etree_process, pycparser, unpickle_pure_python, regex_v8, unpickle, sympy_expand, logging_silent, scimark_fft, coroutines, django_template, pickle_dict
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x