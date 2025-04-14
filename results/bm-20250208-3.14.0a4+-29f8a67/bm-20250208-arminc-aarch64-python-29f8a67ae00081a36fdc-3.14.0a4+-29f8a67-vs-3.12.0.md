# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.040x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| html5lib       | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 503 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 926 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 928 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 493 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 392 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 691 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 680 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.5 ms: 1.06x faster                                                    |
| pidigits       | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| nbody          | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.14 ms: 1.12x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.09x faster                                                     |
| regex_dna      | 254 ms                                                                | 260 ms: 1.02x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 185 ms: 1.05x faster                                                     |
| tomli_loads         | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                   |
| pickle_dict         | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| unpickle_list       | 6.17 us                                                               | 6.44 us: 1.04x slower                                                    |
| xml_etree_process   | 79.0 ms                                                               | 82.5 ms: 1.04x slower                                                    |
| xml_etree_iterparse | 150 ms                                                                | 159 ms: 1.06x slower                                                     |
| pickle_pure_python  | 365 us                                                                | 390 us: 1.07x slower                                                     |
| pickle_list         | 5.25 us                                                               | 5.90 us: 1.12x slower                                                    |
| json_loads          | 30.7 us                                                               | 35.3 us: 1.15x slower                                                    |
| pickle              | 13.4 us                                                               | 16.4 us: 1.22x slower                                                    |
| json_dumps          | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (3): unpickle, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 403 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 503 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 926 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 928 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 493 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 392 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 691 ms: 1.32x faster                                                     |
| deepcopy                   | 446 us                                                                | 339 us: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 680 ms: 1.30x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.6 us: 1.22x faster                                                    |
| comprehensions             | 25.4 us                                                               | 21.5 us: 1.18x faster                                                    |
| generators                 | 43.5 ms                                                               | 36.8 ms: 1.18x faster                                                    |
| pylint                     | 355 ms                                                                | 304 ms: 1.17x faster                                                     |
| go                         | 157 ms                                                                | 140 ms: 1.12x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.14 ms: 1.12x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.72 us: 1.10x faster                                                    |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.10x faster                                                     |
| raytrace                   | 353 ms                                                                | 323 ms: 1.09x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.4 ms: 1.08x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.08x faster                                                     |
| async_generators           | 491 ms                                                                | 454 ms: 1.08x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.08x faster                                                     |
| sympy_str                  | 280 ms                                                                | 261 ms: 1.07x faster                                                     |
| float                      | 92.1 ms                                                               | 86.5 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.29 us: 1.05x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.9 ms: 1.04x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 62.9 ms: 1.03x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 548 ms: 1.03x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.53 sec: 1.03x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                   |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| regex_dna                  | 254 ms                                                                | 260 ms: 1.02x slower                                                     |
| scimark_fft                | 418 ms                                                                | 434 ms: 1.04x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 38.8 us: 1.04x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 953 ms: 1.04x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.44 us: 1.04x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 82.5 ms: 1.04x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.97 sec: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                   |
| pidigits                   | 233 ms                                                                | 244 ms: 1.05x slower                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 159 ms: 1.06x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.46 ms: 1.07x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 390 us: 1.07x slower                                                     |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.08x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.12 us: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 486 ms: 1.10x slower                                                     |
| json                       | 5.54 ms                                                               | 6.14 ms: 1.11x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.46 ms: 1.11x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.90 us: 1.12x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.3 ms: 1.14x slower                                                    |
| nbody                      | 105 ms                                                                | 120 ms: 1.15x slower                                                     |
| json_loads                 | 30.7 us                                                               | 35.3 us: 1.15x slower                                                    |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.4 us: 1.22x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 15.0 ms: 1.22x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.01 ms: 1.59x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.59 ms: 1.87x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.97 sec: 845.78x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (29): sqlglot_parse, django_template, logging_format, unpickle, scimark_lu, chaos, pyflate, sqlglot_optimize, sqlglot_transpile, 2to3, sympy_integrate, genshi_text, crypto_pyaes, coroutines, bench_thread_pool, xml_etree_generate, nqueens, asyncio_websockets, scimark_monte_carlo, pycparser, sympy_expand, unpickle_pure_python, scimark_sparse_mat_mult, richards_super, richards, sqlglot_normalize, scimark_sor, thrift, genshi_xml
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x