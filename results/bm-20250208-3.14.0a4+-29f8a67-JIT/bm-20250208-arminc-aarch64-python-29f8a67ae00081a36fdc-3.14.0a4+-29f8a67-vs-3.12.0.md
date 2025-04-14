# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.002x slower
- HPT reliability: 73.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 318 ms: 1.03x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.27 sec: 1.10x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 496 ms: 1.49x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 958 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 955 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 397 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.1 ms: 1.09x faster                                                    |
| pidigits       | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| nbody          | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 183 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                   |
| unpickle_list        | 6.17 us                                                               | 6.39 us: 1.04x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 273 us: 1.05x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 41.0 us: 1.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 415 us: 1.14x slower                                                     |
| json_loads           | 30.7 us                                                               | 35.8 us: 1.17x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.16 us: 1.17x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| pickle               | 13.4 us                                                               | 16.3 us: 1.21x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.00 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                    |
| mako           | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| genshi_xml     | 60.6 ms                                                               | 65.1 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 496 ms: 1.49x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 958 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 955 ms: 1.47x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 397 ms: 1.45x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 683 ms: 1.29x faster                                                     |
| deepcopy                   | 446 us                                                                | 353 us: 1.26x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 40.1 us: 1.24x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.1 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.56 us: 1.15x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.10x faster                                                     |
| float                      | 92.1 ms                                                               | 84.1 ms: 1.09x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.6 ms: 1.09x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 183 ms: 1.07x faster                                                     |
| pylint                     | 355 ms                                                                | 333 ms: 1.07x faster                                                     |
| raytrace                   | 353 ms                                                                | 335 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.05x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.93 us: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.32 us: 1.04x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.52 sec: 1.03x faster                                                   |
| sympy_str                  | 280 ms                                                                | 288 ms: 1.03x slower                                                     |
| 2to3                       | 308 ms                                                                | 318 ms: 1.03x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.39 us: 1.04x slower                                                    |
| scimark_sor                | 150 ms                                                                | 155 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.90 ms: 1.04x slower                                                    |
| pidigits                   | 233 ms                                                                | 242 ms: 1.04x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.55 sec: 1.04x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                    |
| logging_silent             | 127 ns                                                                | 133 ns: 1.05x slower                                                     |
| pyflate                    | 559 ms                                                                | 587 ms: 1.05x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 273 us: 1.05x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.99 us: 1.06x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.55 ms: 1.06x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 133 ms: 1.06x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.39 ms: 1.06x slower                                                    |
| go                         | 157 ms                                                                | 167 ms: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 65.1 ms: 1.07x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 66.0 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.00 ms: 1.08x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.27 sec: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.79 ms: 1.10x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 41.0 us: 1.10x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 95.2 ms: 1.10x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 68.4 ms: 1.10x slower                                                    |
| sympy_expand               | 454 ms                                                                | 503 ms: 1.11x slower                                                     |
| coverage                   | 87.3 ms                                                               | 98.1 ms: 1.12x slower                                                    |
| json                       | 5.54 ms                                                               | 6.22 ms: 1.12x slower                                                    |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.1 ms: 1.13x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 415 us: 1.14x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                   |
| json_loads                 | 30.7 us                                                               | 35.8 us: 1.17x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.16 us: 1.17x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 215 us: 1.19x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| pickle                     | 13.4 us                                                               | 16.3 us: 1.21x slower                                                    |
| fannkuch                   | 443 ms                                                                | 543 ms: 1.22x slower                                                     |
| nbody                      | 105 ms                                                                | 129 ms: 1.24x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.10 ms: 1.30x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.31 sec: 1.43x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.70 sec: 1.43x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.75 ms: 1.54x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.54 ms: 1.84x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.46 sec: 348.69x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                             |

Benchmark hidden because not significant (24): regex_compile, comprehensions, xml_etree_iterparse, sqlalchemy_declarative, html5lib, regex_dna, django_template, async_generators, unpickle, xml_etree_generate, chaos, scimark_monte_carlo, asyncio_tcp, scimark_fft, coroutines, xml_etree_process, asyncio_websockets, sympy_sum, sqlalchemy_imperative, thrift, deltablue, sympy_integrate, richards_super, richards
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 73.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x