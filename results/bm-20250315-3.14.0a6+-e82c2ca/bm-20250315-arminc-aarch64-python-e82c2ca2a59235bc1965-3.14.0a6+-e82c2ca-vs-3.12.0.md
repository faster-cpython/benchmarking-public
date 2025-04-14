# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.045x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 296 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                     |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 911 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.7 ms: 1.05x faster                                                    |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 128 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                    |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 243 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| unpickle             | 18.5 us                                                               | 17.6 us: 1.05x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                   |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 269 us: 1.03x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.39 us: 1.04x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.55 us: 1.06x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 388 us: 1.06x slower                                                     |
| json_loads           | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                    |
| pickle               | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                    |
| django_template | 40.7 ms                                                               | 40.5 ms: 1.00x faster                                                    |
| mako            | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 477 ms: 1.63x faster                                                     |
| async_tree_none            | 624 ms                                                                | 388 ms: 1.61x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 885 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.58x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 371 ms: 1.55x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 911 ms: 1.54x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 663 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 650 ms: 1.36x faster                                                     |
| deepcopy                   | 446 us                                                                | 333 us: 1.34x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.9 us: 1.31x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 51.4 ms: 1.21x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 3.89 ms: 1.19x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.5 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                    |
| pylint                     | 355 ms                                                                | 312 ms: 1.14x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.0 ms: 1.12x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.95 us: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.60 us: 1.10x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 178 ms: 1.10x faster                                                     |
| raytrace                   | 353 ms                                                                | 322 ms: 1.10x faster                                                     |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| async_generators           | 491 ms                                                                | 451 ms: 1.09x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.6 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 141 ms: 1.07x faster                                                     |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                     |
| float                      | 92.1 ms                                                               | 87.7 ms: 1.05x faster                                                    |
| unpickle                   | 18.5 us                                                               | 17.6 us: 1.05x faster                                                    |
| regex_dna                  | 254 ms                                                                | 243 ms: 1.04x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.95 ms: 1.04x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 543 ms: 1.04x faster                                                     |
| 2to3                       | 308 ms                                                                | 296 ms: 1.04x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.50 sec: 1.04x faster                                                   |
| genshi_text                | 27.4 ms                                                               | 26.7 ms: 1.03x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                                   |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                    |
| django_template            | 40.7 ms                                                               | 40.5 ms: 1.00x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| richards_super             | 58.5 ms                                                               | 58.9 ms: 1.01x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.82 us: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 949 us: 1.01x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                                    |
| pyflate                    | 559 ms                                                                | 569 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 150 ms: 1.03x slower                                                     |
| scimark_fft                | 418 ms                                                                | 430 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 269 us: 1.03x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.39 us: 1.04x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 948 ms: 1.04x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| sympy_expand               | 454 ms                                                                | 472 ms: 1.04x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.2 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.54 ms: 1.06x slower                                                    |
| json                       | 5.54 ms                                                               | 5.85 ms: 1.06x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.55 us: 1.06x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 105 ms: 1.06x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 388 us: 1.06x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.52 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 199 us: 1.10x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.3 ms: 1.11x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.0 us: 1.11x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.49 ms: 1.11x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.7 ms: 1.12x slower                                                    |
| fannkuch                   | 443 ms                                                                | 502 ms: 1.13x slower                                                     |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.7 us: 1.17x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.21x slower                                                    |
| nbody                      | 105 ms                                                                | 128 ms: 1.22x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.41x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.64 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.54 ms: 1.85x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.92 sec: 413.67x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (15): html5lib, sympy_str, scimark_monte_carlo, asyncio_tcp_ssl, chaos, docutils, crypto_pyaes, scimark_sor, genshi_xml, pycparser, asyncio_websockets, coroutines, xml_etree_generate, regex_v8, meteor_contest
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x