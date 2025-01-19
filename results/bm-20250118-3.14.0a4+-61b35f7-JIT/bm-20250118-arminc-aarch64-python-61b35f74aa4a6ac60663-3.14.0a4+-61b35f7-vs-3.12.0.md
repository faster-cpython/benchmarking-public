# Results vs. 3.12.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.037x slower
- HPT reliability: 98.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 329 ms: 1.07x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                   |
| html5lib       | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 921 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 519 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 681 ms: 1.30x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.5 ms: 1.04x faster                                                    |
| pidigits       | 233 ms                                                                | 245 ms: 1.05x slower                                                     |
| nbody          | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 144 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 264 us: 1.02x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 39.4 us: 1.06x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.66 us: 1.08x slower                                                    |
| json_loads           | 30.7 us                                                               | 33.6 us: 1.09x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 405 us: 1.11x slower                                                     |
| pickle_list          | 5.25 us                                                               | 6.08 us: 1.16x slower                                                    |
| pickle               | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 15.8 ms: 1.29x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| django_template | 40.7 ms                                                               | 48.8 ms: 1.20x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.7 ms: 1.23x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 87.0 ms: 1.44x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 915 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 921 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 519 ms: 1.50x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 389 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 701 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 681 ms: 1.30x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 43.2 us: 1.15x faster                                                    |
| deepcopy                   | 446 us                                                                | 411 us: 1.08x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 22.7 ms: 1.08x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| float                      | 92.1 ms                                                               | 88.5 ms: 1.04x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 153 ms: 1.03x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.8 us: 1.02x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| unpickle_pure_python       | 260 us                                                                | 264 us: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 674 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.5 ms: 1.03x slower                                                    |
| spectral_norm              | 131 ms                                                                | 135 ms: 1.03x slower                                                     |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 594 ms: 1.05x slower                                                     |
| regex_compile              | 137 ms                                                                | 144 ms: 1.05x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 162 ms: 1.05x slower                                                     |
| thrift                     | 937 us                                                                | 985 us: 1.05x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.59 sec: 1.05x slower                                                   |
| pidigits                   | 233 ms                                                                | 245 ms: 1.05x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.4 us: 1.06x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.38 ms: 1.06x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.33 sec: 1.06x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 23.0 ms: 1.07x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.02 us: 1.07x slower                                                    |
| logging_format             | 8.34 us                                                               | 8.91 us: 1.07x slower                                                    |
| 2to3                       | 308 ms                                                                | 329 ms: 1.07x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                                    |
| logging_simple             | 7.63 us                                                               | 8.19 us: 1.07x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.96 ms: 1.07x slower                                                    |
| sympy_str                  | 280 ms                                                                | 301 ms: 1.08x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.68 ms: 1.08x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.66 us: 1.08x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 94.0 ms: 1.09x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.24 sec: 1.09x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                    |
| richards_super             | 58.5 ms                                                               | 63.8 ms: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.1 ms: 1.09x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.6 us: 1.09x slower                                                    |
| richards                   | 50.9 ms                                                               | 56.3 ms: 1.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.63 ms: 1.11x slower                                                    |
| json                       | 5.54 ms                                                               | 6.17 ms: 1.11x slower                                                    |
| pyflate                    | 559 ms                                                                | 624 ms: 1.12x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                     |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 70.2 ms: 1.14x slower                                                    |
| chaos                      | 71.4 ms                                                               | 82.3 ms: 1.15x slower                                                    |
| pickle_list                | 5.25 us                                                               | 6.08 us: 1.16x slower                                                    |
| sympy_expand               | 454 ms                                                                | 526 ms: 1.16x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 32.9 ms: 1.16x slower                                                    |
| fannkuch                   | 443 ms                                                                | 515 ms: 1.16x slower                                                     |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.8 us: 1.18x slower                                                    |
| logging_silent             | 127 ns                                                                | 150 ns: 1.18x slower                                                     |
| nbody                      | 105 ms                                                                | 124 ms: 1.19x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 73.7 ms: 1.19x slower                                                    |
| go                         | 157 ms                                                                | 188 ms: 1.19x slower                                                     |
| django_template            | 40.7 ms                                                               | 48.8 ms: 1.20x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.54 sec: 1.22x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 222 us: 1.23x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 33.7 ms: 1.23x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 126 ms: 1.27x slower                                                     |
| generators                 | 43.5 ms                                                               | 55.5 ms: 1.28x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 15.8 ms: 1.29x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.71 ms: 1.39x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.29 sec: 1.41x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.65 sec: 1.41x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 87.0 ms: 1.44x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 7.00 ms: 1.59x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 2.21 sec: 313.52x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (12): xml_etree_iterparse, raytrace, pylint, coroutines, unpickle, regex_dna, xml_etree_generate, async_generators, sqlalchemy_imperative, scimark_fft, xml_etree_process, deepcopy_reduce
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.037x slower

# HPT report

- Reliability score: 98.81% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x