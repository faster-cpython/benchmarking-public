# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.041x slower
- HPT reliability: 98.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.30 sec: 1.10x slower                                                   |
| html5lib       | 65.1 ms                                                               | 75.6 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 944 ms: 1.49x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                     |
| async_tree_none            | 624 ms                                                                | 425 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 965 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 514 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 688 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.41x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 241 ms: 1.03x slower                                                     |
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.18 ms: 1.11x faster                                                    |
| regex_compile  | 137 ms                                                                | 146 ms: 1.06x slower                                                     |
| regex_dna      | 254 ms                                                                | 272 ms: 1.07x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.79 us: 1.10x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 41.2 us: 1.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 406 us: 1.11x slower                                                     |
| json_loads           | 30.7 us                                                               | 35.6 us: 1.16x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.17 us: 1.17x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                                    |
| pickle               | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| django_template | 40.7 ms                                                               | 48.3 ms: 1.19x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 85.8 ms: 1.42x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 944 ms: 1.49x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 528 ms: 1.47x faster                                                     |
| async_tree_none            | 624 ms                                                                | 425 ms: 1.47x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 965 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 514 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 404 ms: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 688 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 722 ms: 1.26x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 43.1 us: 1.15x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.18 ms: 1.11x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.2 ms: 1.11x faster                                                    |
| deepcopy                   | 446 us                                                                | 409 us: 1.09x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 181 ms: 1.08x faster                                                     |
| pylint                     | 355 ms                                                                | 337 ms: 1.05x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.56 sec: 1.01x faster                                                   |
| pidigits                   | 233 ms                                                                | 241 ms: 1.03x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.55 sec: 1.04x slower                                                   |
| 2to3                       | 308 ms                                                                | 321 ms: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 162 ms: 1.05x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 89.6 ms: 1.05x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 598 ms: 1.06x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.98 us: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.06x slower                                                     |
| spectral_norm              | 131 ms                                                                | 138 ms: 1.06x slower                                                     |
| logging_simple             | 7.63 us                                                               | 8.08 us: 1.06x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                                     |
| logging_format             | 8.34 us                                                               | 8.83 us: 1.06x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.31 sec: 1.06x slower                                                   |
| regex_compile              | 137 ms                                                                | 146 ms: 1.06x slower                                                     |
| richards_super             | 58.5 ms                                                               | 62.1 ms: 1.06x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.1 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 13.8 ms: 1.07x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.39 us: 1.07x slower                                                    |
| regex_dna                  | 254 ms                                                                | 272 ms: 1.07x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.96 ms: 1.07x slower                                                    |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| pyflate                    | 559 ms                                                                | 605 ms: 1.08x slower                                                     |
| sympy_str                  | 280 ms                                                                | 303 ms: 1.08x slower                                                     |
| go                         | 157 ms                                                                | 170 ms: 1.08x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.51 ms: 1.09x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 159 ms: 1.10x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.79 us: 1.10x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 41.2 us: 1.10x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.30 sec: 1.10x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.62 ms: 1.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 406 us: 1.11x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.6 ms: 1.11x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 140 ms: 1.11x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.93 ms: 1.12x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 70.0 ms: 1.13x slower                                                    |
| meteor_contest             | 112 ms                                                                | 126 ms: 1.13x slower                                                     |
| json                       | 5.54 ms                                                               | 6.28 ms: 1.13x slower                                                    |
| fannkuch                   | 443 ms                                                                | 508 ms: 1.15x slower                                                     |
| sympy_expand               | 454 ms                                                                | 521 ms: 1.15x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 70.6 ms: 1.15x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.7 ms: 1.15x slower                                                    |
| json_loads                 | 30.7 us                                                               | 35.6 us: 1.16x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 75.6 ms: 1.16x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.16x slower                                                     |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                     |
| logging_silent             | 127 ns                                                                | 149 ns: 1.17x slower                                                     |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.17 us: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.4 ms: 1.18x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.9 us: 1.18x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.18x slower                                                    |
| django_template            | 40.7 ms                                                               | 48.3 ms: 1.19x slower                                                    |
| chaos                      | 71.4 ms                                                               | 86.7 ms: 1.21x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.54 sec: 1.23x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 227 us: 1.26x slower                                                     |
| generators                 | 43.5 ms                                                               | 55.5 ms: 1.27x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 134 ms: 1.35x slower                                                     |
| genshi_xml                 | 60.6 ms                                                               | 85.8 ms: 1.42x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.30 sec: 1.42x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.69 sec: 1.43x slower                                                   |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.46x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.87 ms: 1.56x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.56 sec: 221.36x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (12): float, xml_etree_iterparse, unpickle, comprehensions, xml_etree_generate, async_generators, xml_etree_process, scimark_fft, asyncio_websockets, coroutines, raytrace, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 98.75% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x