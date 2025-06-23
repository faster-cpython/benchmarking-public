# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| docutils       | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| html5lib       | 65.1 ms                                                               | 62.4 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                              |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 896 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                                              |
| nbody          | 105 ms                                                                | 125 ms: 1.19x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                             |
| regex_compile  | 137 ms                                                                | 120 ms: 1.15x faster                                                              |
| regex_dna      | 254 ms                                                                | 225 ms: 1.13x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 27.3 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| tomli_loads         | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                            |
| xml_etree_iterparse | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| xml_etree_process   | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                                             |
| json_loads          | 30.7 us                                                               | 32.3 us: 1.05x slower                                                             |
| pickle_pure_python  | 365 us                                                                | 392 us: 1.07x slower                                                              |
| json_dumps          | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                             |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                             |
| genshi_text     | 27.4 ms                                                               | 26.5 ms: 1.04x faster                                                             |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.63 sec: 2.09x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 467 ms: 1.66x faster                                                              |
| async_tree_none            | 624 ms                                                                | 389 ms: 1.60x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 464 ms: 1.60x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 896 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 908 ms: 1.55x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 374 ms: 1.54x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 656 ms: 1.39x faster                                                              |
| deepcopy                   | 446 us                                                                | 325 us: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 39.2 us: 1.26x faster                                                             |
| go                         | 157 ms                                                                | 126 ms: 1.25x faster                                                              |
| comprehensions             | 25.4 us                                                               | 20.4 us: 1.25x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.9 ms: 1.21x faster                                                             |
| dulwich_log                | 62.0 ms                                                               | 53.4 ms: 1.16x faster                                                             |
| regex_effbot               | 4.64 ms                                                               | 4.03 ms: 1.15x faster                                                             |
| regex_compile              | 137 ms                                                                | 120 ms: 1.15x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.59 us: 1.14x faster                                                             |
| regex_dna                  | 254 ms                                                                | 225 ms: 1.13x faster                                                              |
| pylint                     | 355 ms                                                                | 316 ms: 1.12x faster                                                              |
| pyflate                    | 559 ms                                                                | 513 ms: 1.09x faster                                                              |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                              |
| async_generators           | 491 ms                                                                | 452 ms: 1.09x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                              |
| float                      | 92.1 ms                                                               | 86.0 ms: 1.07x faster                                                             |
| tomli_loads                | 2.59 sec                                                              | 2.42 sec: 1.07x faster                                                            |
| sympy_sum                  | 154 ms                                                                | 145 ms: 1.07x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 142 ms: 1.06x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                             |
| spectral_norm              | 131 ms                                                                | 124 ms: 1.05x faster                                                              |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.05x faster                                                              |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                             |
| html5lib                   | 65.1 ms                                                               | 62.4 ms: 1.04x faster                                                             |
| django_template            | 40.7 ms                                                               | 39.1 ms: 1.04x faster                                                             |
| regex_v8                   | 28.3 ms                                                               | 27.3 ms: 1.04x faster                                                             |
| genshi_text                | 27.4 ms                                                               | 26.5 ms: 1.04x faster                                                             |
| sqlite_synth               | 3.77 us                                                               | 3.70 us: 1.02x faster                                                             |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                                              |
| docutils                   | 2.98 sec                                                              | 2.95 sec: 1.01x faster                                                            |
| logging_format             | 8.34 us                                                               | 8.29 us: 1.01x faster                                                             |
| xml_etree_process          | 79.0 ms                                                               | 79.4 ms: 1.01x slower                                                             |
| richards_super             | 58.5 ms                                                               | 59.0 ms: 1.01x slower                                                             |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                                              |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                                             |
| richards                   | 50.9 ms                                                               | 52.4 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                             |
| scimark_lu                 | 146 ms                                                                | 154 ms: 1.05x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.01 sec: 1.07x slower                                                            |
| fannkuch                   | 443 ms                                                                | 474 ms: 1.07x slower                                                              |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                              |
| pprint_safe_repr           | 916 ms                                                                | 988 ms: 1.08x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.40 ms: 1.10x slower                                                             |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.08 ms: 1.14x slower                                                             |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                              |
| nbody                      | 105 ms                                                                | 125 ms: 1.19x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.34x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.92 ms: 1.58x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.83 ms: 1.99x slower                                                             |
| logging_silent             | 127 ns                                                                | 614 ns: 4.84x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.04x faster                                                                      |

Benchmark hidden because not significant (16): crypto_pyaes, deltablue, chaos, meteor_contest, nqueens, pycparser, hexiom, asyncio_websockets, xml_etree_generate, genshi_xml, logging_simple, sympy_expand, scimark_fft, unpickle_pure_python, coroutines, thrift
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x