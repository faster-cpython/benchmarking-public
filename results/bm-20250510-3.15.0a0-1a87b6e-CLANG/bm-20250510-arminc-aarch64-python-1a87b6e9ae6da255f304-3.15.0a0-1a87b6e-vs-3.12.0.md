# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.028x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| docutils       | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| html5lib       | 65.1 ms                                                               | 60.2 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 449 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 863 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 360 ms: 1.60x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 711 ms: 1.24x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| pidigits       | 233 ms                                                                | 292 ms: 1.25x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 120 ms: 1.15x faster                                                    |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 18.5 us                                                               | 17.0 us: 1.08x faster                                                   |
| tomli_loads         | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| unpickle_list       | 6.17 us                                                               | 5.79 us: 1.06x faster                                                   |
| xml_etree_process   | 79.0 ms                                                               | 76.1 ms: 1.04x faster                                                   |
| xml_etree_iterparse | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| xml_etree_parse     | 195 ms                                                                | 205 ms: 1.05x slower                                                    |
| pickle_pure_python  | 365 us                                                                | 385 us: 1.05x slower                                                    |
| pickle_list         | 5.25 us                                                               | 5.55 us: 1.06x slower                                                   |
| json_loads          | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| pickle              | 13.4 us                                                               | 15.1 us: 1.13x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 14.8 ms: 1.20x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (3): pickle_dict, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                   |
| genshi_text     | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                   |
| mako            | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.66 sec: 2.06x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 449 ms: 1.65x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 863 ms: 1.63x faster                                                    |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 360 ms: 1.60x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 894 ms: 1.57x faster                                                    |
| deepcopy                   | 446 us                                                                | 318 us: 1.40x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 35.7 us: 1.39x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 711 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 3.36 us: 1.22x faster                                                   |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 53.2 ms: 1.17x faster                                                   |
| regex_compile              | 137 ms                                                                | 120 ms: 1.15x faster                                                    |
| async_generators           | 491 ms                                                                | 432 ms: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.13x faster                                                   |
| pylint                     | 355 ms                                                                | 315 ms: 1.13x faster                                                    |
| raytrace                   | 353 ms                                                                | 320 ms: 1.10x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.76 ms: 1.10x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 19.9 ms: 1.08x faster                                                   |
| unpickle                   | 18.5 us                                                               | 17.0 us: 1.08x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 60.2 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.7 ms: 1.08x faster                                                   |
| sympy_sum                  | 154 ms                                                                | 143 ms: 1.08x faster                                                    |
| spectral_norm              | 131 ms                                                                | 121 ms: 1.08x faster                                                    |
| pyflate                    | 559 ms                                                                | 523 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.07x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.43 sec: 1.07x faster                                                  |
| unpickle_list              | 6.17 us                                                               | 5.79 us: 1.06x faster                                                   |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.05x faster                                                    |
| richards_super             | 58.5 ms                                                               | 55.6 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                   |
| richards                   | 50.9 ms                                                               | 49.0 ms: 1.04x faster                                                   |
| xml_etree_process          | 79.0 ms                                                               | 76.1 ms: 1.04x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.10 us: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 84.2 ms: 1.03x faster                                                   |
| scimark_fft                | 418 ms                                                                | 407 ms: 1.03x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                   |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.47 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.8 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.02 sec: 1.01x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 205 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.05x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.55 us: 1.06x slower                                                   |
| json                       | 5.54 ms                                                               | 5.88 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.77 ms: 1.09x slower                                                   |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                   |
| fannkuch                   | 443 ms                                                                | 487 ms: 1.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.36 ms: 1.10x slower                                                   |
| json_loads                 | 30.7 us                                                               | 34.2 us: 1.11x slower                                                   |
| pickle                     | 13.4 us                                                               | 15.1 us: 1.13x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.20x slower                                                   |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                    |
| pidigits                   | 233 ms                                                                | 292 ms: 1.25x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.73 ms: 1.53x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.85 ms: 2.01x slower                                                   |
| logging_silent             | 127 ns                                                                | 631 ns: 4.98x slower                                                    |
| coverage                   | 87.3 ms                                                               | 534 ms: 6.12x slower                                                    |
| thrift                     | 937 us                                                                | 192 ms: 204.47x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 3.51 sec: 496.88x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (14): chaos, pickle_dict, xml_etree_generate, unpickle_pure_python, asyncio_tcp, pycparser, pprint_pformat, regex_effbot, genshi_xml, pprint_safe_repr, sympy_expand, bench_thread_pool, hexiom, sqlite_synth
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.12x