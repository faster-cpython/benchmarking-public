# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 59.5 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 376 ms: 1.66x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 458 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 366 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.52x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                    |
| nbody          | 105 ms                                                                | 119 ms: 1.13x slower                                                     |
| pidigits       | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.21 ms: 1.10x faster                                                    |
| regex_dna      | 254 ms                                                                | 233 ms: 1.09x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.59 sec                                                              | 2.37 sec: 1.09x faster                                                   |
| unpickle_list      | 6.17 us                                                               | 5.68 us: 1.09x faster                                                    |
| xml_etree_generate | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| unpickle           | 18.5 us                                                               | 17.2 us: 1.07x faster                                                    |
| xml_etree_process  | 79.0 ms                                                               | 74.1 ms: 1.07x faster                                                    |
| pickle_list        | 5.25 us                                                               | 5.60 us: 1.07x slower                                                    |
| xml_etree_parse    | 195 ms                                                                | 209 ms: 1.07x slower                                                     |
| pickle_pure_python | 365 us                                                                | 392 us: 1.07x slower                                                     |
| json_loads         | 30.7 us                                                               | 33.1 us: 1.08x slower                                                    |
| pickle             | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (3): pickle_dict, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 25.9 ms: 1.06x faster                                                    |
| django_template | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                    |
| genshi_xml      | 60.6 ms                                                               | 58.1 ms: 1.04x faster                                                    |
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 466 ms: 1.67x faster                                                     |
| async_tree_none            | 624 ms                                                                | 376 ms: 1.66x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 458 ms: 1.62x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 876 ms: 1.61x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 889 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 366 ms: 1.58x faster                                                     |
| deepcopy                   | 446 us                                                                | 312 us: 1.43x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.6 us: 1.39x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 725 ms: 1.26x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 709 ms: 1.25x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 50.7 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.36 us: 1.22x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.1 ms: 1.21x faster                                                    |
| async_generators           | 491 ms                                                                | 416 ms: 1.18x faster                                                     |
| pylint                     | 355 ms                                                                | 303 ms: 1.17x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 136 ms: 1.15x faster                                                     |
| spectral_norm              | 131 ms                                                                | 114 ms: 1.15x faster                                                     |
| raytrace                   | 353 ms                                                                | 311 ms: 1.13x faster                                                     |
| regex_compile              | 137 ms                                                                | 123 ms: 1.11x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 143 ms: 1.10x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.21 ms: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 141 ms: 1.09x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 59.5 ms: 1.09x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.37 sec: 1.09x faster                                                   |
| regex_dna                  | 254 ms                                                                | 233 ms: 1.09x faster                                                     |
| logging_simple             | 7.63 us                                                               | 7.00 us: 1.09x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 78.0 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.67 us: 1.09x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.68 us: 1.09x faster                                                    |
| sympy_str                  | 280 ms                                                                | 257 ms: 1.09x faster                                                     |
| xml_etree_generate         | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| scimark_fft                | 418 ms                                                                | 388 ms: 1.08x faster                                                     |
| float                      | 92.1 ms                                                               | 85.3 ms: 1.08x faster                                                    |
| chaos                      | 71.4 ms                                                               | 66.2 ms: 1.08x faster                                                    |
| unpickle                   | 18.5 us                                                               | 17.2 us: 1.07x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 74.1 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                    |
| 2to3                       | 308 ms                                                                | 291 ms: 1.06x faster                                                     |
| pyflate                    | 559 ms                                                                | 528 ms: 1.06x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.22 sec: 1.06x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 25.9 ms: 1.06x faster                                                    |
| logging_silent             | 127 ns                                                                | 121 ns: 1.05x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.8 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 143 ms: 1.04x faster                                                     |
| richards_super             | 58.5 ms                                                               | 56.1 ms: 1.04x faster                                                    |
| genshi_xml                 | 60.6 ms                                                               | 58.1 ms: 1.04x faster                                                    |
| docutils                   | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| pprint_safe_repr           | 916 ms                                                                | 910 ms: 1.01x faster                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.83 us: 1.02x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.20 ms: 1.03x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.1 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| json                       | 5.54 ms                                                               | 5.78 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 191 us: 1.06x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.60 us: 1.07x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| coverage                   | 87.3 ms                                                               | 93.3 ms: 1.07x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 209 ms: 1.07x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 392 us: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.22 ms: 1.08x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                     |
| nbody                      | 105 ms                                                                | 119 ms: 1.13x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                    |
| pidigits                   | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.52 ms: 1.48x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.37 sec: 336.08x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (16): sympy_integrate, sqlalchemy_imperative, asyncio_tcp, pickle_dict, pycparser, pprint_pformat, richards, bench_thread_pool, unpickle_pure_python, sympy_expand, xml_etree_iterparse, scimark_sparse_mat_mult, coroutines, nqueens, asyncio_websockets, thrift
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x