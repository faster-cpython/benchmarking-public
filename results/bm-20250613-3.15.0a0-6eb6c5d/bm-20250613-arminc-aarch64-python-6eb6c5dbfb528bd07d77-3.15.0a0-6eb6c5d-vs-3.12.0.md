# Results vs. 3.12.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-aarch64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.027x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| docutils       | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                  |
| html5lib       | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 913 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                   |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                                   |
| regex_dna      | 254 ms                                                                | 221 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| tomli_loads         | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| pickle_pure_python  | 365 us                                                                | 384 us: 1.05x slower                                                    |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                   |
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                   |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.65 sec: 2.07x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 463 ms: 1.60x faster                                                    |
| async_tree_none            | 624 ms                                                                | 396 ms: 1.57x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 898 ms: 1.57x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 913 ms: 1.54x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 379 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 657 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                    |
| deepcopy                   | 446 us                                                                | 328 us: 1.36x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                   |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                                   |
| go                         | 157 ms                                                                | 127 ms: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.6 ms: 1.22x faster                                                   |
| dulwich_log                | 62.0 ms                                                               | 51.5 ms: 1.20x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 3.88 ms: 1.20x faster                                                   |
| regex_dna                  | 254 ms                                                                | 221 ms: 1.15x faster                                                    |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.61 us: 1.14x faster                                                   |
| regex_compile              | 137 ms                                                                | 122 ms: 1.12x faster                                                    |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| async_generators           | 491 ms                                                                | 453 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.07x faster                                                   |
| html5lib                   | 65.1 ms                                                               | 61.0 ms: 1.07x faster                                                   |
| pyflate                    | 559 ms                                                                | 527 ms: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.44 sec: 1.06x faster                                                  |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                    |
| sympy_str                  | 280 ms                                                                | 265 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.0 ms: 1.05x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 26.3 ms: 1.04x faster                                                   |
| regex_v8                   | 28.3 ms                                                               | 27.4 ms: 1.04x faster                                                   |
| 2to3                       | 308 ms                                                                | 298 ms: 1.03x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 89.8 ms: 1.03x faster                                                   |
| docutils                   | 2.98 sec                                                              | 2.92 sec: 1.02x faster                                                  |
| meteor_contest             | 112 ms                                                                | 110 ms: 1.02x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                  |
| logging_format             | 8.34 us                                                               | 8.25 us: 1.01x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.56 us: 1.01x faster                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.81 us: 1.01x slower                                                   |
| richards                   | 50.9 ms                                                               | 52.3 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                   |
| json                       | 5.54 ms                                                               | 5.73 ms: 1.04x slower                                                   |
| sympy_expand               | 454 ms                                                                | 471 ms: 1.04x slower                                                    |
| scimark_fft                | 418 ms                                                                | 439 ms: 1.05x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 153 ms: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 191 us: 1.06x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.02 sec: 1.07x slower                                                  |
| fannkuch                   | 443 ms                                                                | 476 ms: 1.07x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 989 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                   |
| telco                      | 8.51 ms                                                               | 9.48 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.01 ms: 1.13x slower                                                   |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.1 ms: 1.33x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 6.84 ms: 1.56x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.88 ms: 2.02x slower                                                   |
| logging_silent             | 127 ns                                                                | 615 ns: 4.85x slower                                                    |
| coverage                   | 87.3 ms                                                               | 566 ms: 6.48x slower                                                    |
| thrift                     | 937 us                                                                | 193 ms: 206.48x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (15): scimark_sor, crypto_pyaes, chaos, spectral_norm, deltablue, xml_etree_generate, hexiom, richards_super, xml_etree_process, genshi_xml, nqueens, unpickle_pure_python, asyncio_websockets, pidigits, coroutines
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.10x