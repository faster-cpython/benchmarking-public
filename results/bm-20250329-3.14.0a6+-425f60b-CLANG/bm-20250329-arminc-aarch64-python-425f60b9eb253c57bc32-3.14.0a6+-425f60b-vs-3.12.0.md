# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 292 ms: 1.05x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| html5lib       | 65.1 ms                                                               | 59.7 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 453 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 898 ms: 1.56x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 83.2 ms: 1.11x faster                                                    |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| pidigits       | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| regex_dna      | 254 ms                                                                | 243 ms: 1.05x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle             | 18.5 us                                                               | 16.9 us: 1.09x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.39 sec: 1.09x faster                                                   |
| unpickle_list        | 6.17 us                                                               | 5.71 us: 1.08x faster                                                    |
| xml_etree_process    | 79.0 ms                                                               | 74.2 ms: 1.06x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 107 ms: 1.05x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.02x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 202 ms: 1.04x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 381 us: 1.04x slower                                                     |
| pickle_list          | 5.25 us                                                               | 5.60 us: 1.07x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.3 us: 1.08x slower                                                    |
| pickle               | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.9 ms: 1.04x faster                                                    |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.59 sec: 2.14x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_none            | 624 ms                                                                | 382 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 453 ms: 1.63x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 870 ms: 1.62x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 364 ms: 1.58x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 898 ms: 1.56x faster                                                     |
| deepcopy                   | 446 us                                                                | 309 us: 1.44x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 36.2 us: 1.37x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.0 us: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 721 ms: 1.27x faster                                                     |
| generators                 | 43.5 ms                                                               | 34.7 ms: 1.25x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 49.7 ms: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.40 us: 1.21x faster                                                    |
| async_generators           | 491 ms                                                                | 414 ms: 1.19x faster                                                     |
| pylint                     | 355 ms                                                                | 303 ms: 1.17x faster                                                     |
| spectral_norm              | 131 ms                                                                | 112 ms: 1.17x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 136 ms: 1.16x faster                                                     |
| raytrace                   | 353 ms                                                                | 306 ms: 1.15x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.17 ms: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 76.5 ms: 1.11x faster                                                    |
| float                      | 92.1 ms                                                               | 83.2 ms: 1.11x faster                                                    |
| logging_silent             | 127 ns                                                                | 115 ns: 1.11x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.55 us: 1.11x faster                                                    |
| scimark_fft                | 418 ms                                                                | 382 ms: 1.09x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                     |
| unpickle                   | 18.5 us                                                               | 16.9 us: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 59.7 ms: 1.09x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.39 sec: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 134 ms: 1.09x faster                                                     |
| chaos                      | 71.4 ms                                                               | 65.8 ms: 1.09x faster                                                    |
| scimark_sor                | 150 ms                                                                | 138 ms: 1.08x faster                                                     |
| unpickle_list              | 6.17 us                                                               | 5.71 us: 1.08x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.81 ms: 1.08x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                     |
| pyflate                    | 559 ms                                                                | 521 ms: 1.07x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.2 ms: 1.07x faster                                                    |
| richards_super             | 58.5 ms                                                               | 54.9 ms: 1.07x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 74.2 ms: 1.06x faster                                                    |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                     |
| 2to3                       | 308 ms                                                                | 292 ms: 1.05x faster                                                     |
| richards                   | 50.9 ms                                                               | 48.3 ms: 1.05x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 107 ms: 1.05x faster                                                     |
| regex_dna                  | 254 ms                                                                | 243 ms: 1.05x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.9 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.02 ms: 1.03x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 552 ms: 1.03x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.93 sec: 1.02x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 256 us: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.15 sec: 1.01x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.90 sec: 1.01x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 934 ms: 1.02x slower                                                     |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.85 us: 1.02x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 202 ms: 1.04x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 381 us: 1.04x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 189 us: 1.05x slower                                                     |
| json                       | 5.54 ms                                                               | 5.88 ms: 1.06x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.05 ms: 1.06x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.60 us: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                     |
| json_loads                 | 30.7 us                                                               | 33.3 us: 1.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 95.6 ms: 1.10x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 496 ms: 1.12x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.14x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.2 ms: 1.43x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.69 ms: 1.52x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.80 ms: 1.98x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.90 sec: 411.06x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (11): genshi_text, sqlalchemy_imperative, genshi_xml, coroutines, pickle_dict, pycparser, bench_thread_pool, crypto_pyaes, sympy_expand, nqueens, hexiom
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x