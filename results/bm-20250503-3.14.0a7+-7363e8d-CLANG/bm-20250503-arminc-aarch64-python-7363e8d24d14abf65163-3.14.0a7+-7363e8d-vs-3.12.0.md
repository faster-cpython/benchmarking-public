# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: linux-aarch64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| html5lib       | 65.1 ms                                                               | 58.3 ms: 1.12x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 452 ms: 1.72x faster                                                     |
| async_tree_none            | 624 ms                                                                | 372 ms: 1.68x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 447 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 865 ms: 1.63x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 861 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 357 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.54x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.4 ms: 1.07x faster                                                    |
| nbody          | 105 ms                                                                | 128 ms: 1.23x slower                                                     |
| pidigits       | 233 ms                                                                | 292 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| unpickle_list       | 6.17 us                                                               | 5.71 us: 1.08x faster                                                    |
| unpickle            | 18.5 us                                                               | 17.1 us: 1.08x faster                                                    |
| xml_etree_generate  | 112 ms                                                                | 107 ms: 1.04x faster                                                     |
| xml_etree_process   | 79.0 ms                                                               | 76.5 ms: 1.03x faster                                                    |
| xml_etree_iterparse | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| pickle_pure_python  | 365 us                                                                | 371 us: 1.02x slower                                                     |
| pickle_list         | 5.25 us                                                               | 5.43 us: 1.04x slower                                                    |
| xml_etree_parse     | 195 ms                                                                | 203 ms: 1.04x slower                                                     |
| json_loads          | 30.7 us                                                               | 34.9 us: 1.14x slower                                                    |
| pickle              | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 25.8 ms: 1.06x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 58.3 ms: 1.04x faster                                                    |
| django_template | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.62 sec: 2.11x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 452 ms: 1.72x faster                                                     |
| async_tree_none            | 624 ms                                                                | 372 ms: 1.68x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 447 ms: 1.66x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 865 ms: 1.63x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 861 ms: 1.63x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 357 ms: 1.62x faster                                                     |
| deepcopy                   | 446 us                                                                | 312 us: 1.43x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.2 us: 1.41x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.6 us: 1.30x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.25 us: 1.26x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 723 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 706 ms: 1.25x faster                                                     |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 53.0 ms: 1.17x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.2 ms: 1.17x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.14x faster                                                    |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| pylint                     | 355 ms                                                                | 311 ms: 1.14x faster                                                     |
| async_generators           | 491 ms                                                                | 434 ms: 1.13x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 138 ms: 1.12x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 58.3 ms: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 19.7 ms: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.61 us: 1.10x faster                                                    |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.77 ms: 1.09x faster                                                    |
| logging_silent             | 127 ns                                                                | 116 ns: 1.09x faster                                                     |
| chaos                      | 71.4 ms                                                               | 65.5 ms: 1.09x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.71 us: 1.08x faster                                                    |
| unpickle                   | 18.5 us                                                               | 17.1 us: 1.08x faster                                                    |
| sympy_str                  | 280 ms                                                                | 260 ms: 1.08x faster                                                     |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                     |
| pyflate                    | 559 ms                                                                | 524 ms: 1.07x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.07x faster                                                     |
| float                      | 92.1 ms                                                               | 86.4 ms: 1.07x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 25.8 ms: 1.06x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.9 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.9 ms: 1.05x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.04x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 58.3 ms: 1.04x faster                                                    |
| django_template            | 40.7 ms                                                               | 39.4 ms: 1.03x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 76.5 ms: 1.03x faster                                                    |
| scimark_fft                | 418 ms                                                                | 406 ms: 1.03x faster                                                     |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 552 ms: 1.03x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 85.6 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 916 ms                                                                | 923 ms: 1.01x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 371 us: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.43 us: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.71 ms: 1.04x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 203 ms: 1.04x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.94 us: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.06x slower                                                     |
| json                       | 5.54 ms                                                               | 5.87 ms: 1.06x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.24 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.75 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 198 us: 1.10x slower                                                     |
| fannkuch                   | 443 ms                                                                | 496 ms: 1.12x slower                                                     |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.9 us: 1.14x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                    |
| nbody                      | 105 ms                                                                | 128 ms: 1.23x slower                                                     |
| pidigits                   | 233 ms                                                                | 292 ms: 1.26x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.42x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.76 ms: 1.54x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.96x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.64 sec: 373.78x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (14): scimark_lu, scimark_sor, unpickle_pure_python, richards, pickle_dict, regex_effbot, docutils, asyncio_tcp_ssl, hexiom, pprint_pformat, sympy_expand, bench_thread_pool, coroutines, nqueens
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-arminc-aarch64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.070x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x