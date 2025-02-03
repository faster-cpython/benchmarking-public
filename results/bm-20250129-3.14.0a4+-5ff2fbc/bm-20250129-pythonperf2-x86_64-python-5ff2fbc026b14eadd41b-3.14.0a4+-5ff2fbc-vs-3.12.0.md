# Results vs. 3.12.0

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.04 ms: 1.18x faster                                                        |
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.6 ms: 1.05x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 83.5 ms: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 209 us: 1.00x faster                                                         |
| pickle_pure_python   | 318 us                                                       | 323 us: 1.01x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.9 us: 1.10x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                        |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 649 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 337 ms: 1.60x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 349 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 511 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| deepcopy                   | 368 us                                                       | 278 us: 1.33x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.8 us: 1.30x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                        |
| go                         | 150 ms                                                       | 123 ms: 1.21x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.21x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.04 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                         |
| float                      | 76.6 ms                                                      | 69.1 ms: 1.11x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.75 us: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.7 ms: 1.11x faster                                                        |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 83.4 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.8 ms: 1.10x faster                                                        |
| chaos                      | 64.0 ms                                                      | 58.5 ms: 1.09x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.17 us: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                        |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.6 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.7 ms: 1.05x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.71 ms: 1.04x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.5 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 785 ms: 1.03x faster                                                         |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                         |
| pyflate                    | 439 ms                                                       | 430 ms: 1.02x faster                                                         |
| nbody                      | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 56.6 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                         |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.8 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| richards                   | 45.7 ms                                                      | 45.3 ms: 1.01x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                       |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                         |
| unpickle_pure_python       | 210 us                                                       | 209 us: 1.00x faster                                                         |
| sympy_expand               | 484 ms                                                       | 487 ms: 1.01x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.25 ms: 1.01x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 323 us: 1.01x slower                                                         |
| fannkuch                   | 350 ms                                                       | 355 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.06 ms: 1.02x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 410 ms: 1.05x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                        |
| json                       | 5.12 ms                                                      | 5.56 ms: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.9 ms: 1.10x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.9 us: 1.10x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.66 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.11x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.93 ms: 1.14x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.3 ms: 1.19x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.68 ms: 1.68x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.10 ms: 1.75x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.29 sec: 271.52x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, richards_super, asyncio_websockets, dulwich_log, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-5ff2fbc/bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x