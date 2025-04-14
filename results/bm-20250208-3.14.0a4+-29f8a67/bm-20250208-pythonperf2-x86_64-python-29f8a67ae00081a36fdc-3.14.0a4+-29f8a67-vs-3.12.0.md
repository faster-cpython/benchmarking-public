# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.048x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 643 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.0 ms: 1.11x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 93.7 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.2 ms: 1.08x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 4.89 us: 1.05x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 35.7 us: 1.10x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.39 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 643 ms: 1.62x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.55x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 509 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 519 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 31.0 us: 1.19x faster                                                        |
| go                         | 150 ms                                                       | 127 ms: 1.17x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.09 ms: 1.16x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.4 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.94 us: 1.15x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.5 ms: 1.12x faster                                                        |
| float                      | 76.6 ms                                                      | 69.0 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                         |
| logging_format             | 7.48 us                                                      | 6.77 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 84.1 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.2 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                         |
| django_template            | 38.2 ms                                                      | 35.6 ms: 1.07x faster                                                        |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.06x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| unpack_sequence            | 53.2 ns                                                      | 50.4 ns: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.04x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 781 ms: 1.03x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| pyflate                    | 439 ms                                                       | 426 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.35 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                         |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.01x faster                                                         |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                         |
| richards_super             | 51.3 ms                                                      | 51.6 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 59.1 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.06 ms: 1.02x slower                                                        |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 97.8 ns: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 367 ms: 1.05x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.89 us: 1.05x slower                                                        |
| async_generators           | 390 ms                                                       | 410 ms: 1.05x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                        |
| nbody                      | 88.0 ms                                                      | 93.7 ms: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.47 ms: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 35.7 us: 1.10x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.67 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                         |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.89 ms: 1.13x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.3 us: 1.17x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.5 ms: 1.19x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.39 us: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.85 ms: 1.79x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.37 ms: 1.83x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 889 ms: 186.62x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (9): unpickle, bench_thread_pool, sqlglot_optimize, docutils, asyncio_tcp_ssl, richards, asyncio_websockets, scimark_fft, pycparser
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x