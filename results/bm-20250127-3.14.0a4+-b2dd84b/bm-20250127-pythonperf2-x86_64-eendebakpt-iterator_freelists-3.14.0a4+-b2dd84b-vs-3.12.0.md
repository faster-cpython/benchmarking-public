# Results vs. 3.12.0

- fork: eendebakpt
- ref: iterator_freelists
- machine: linux-x86_64
- commit hash: b2dd84b
- commit date: 2025-01-27
- overall geometric mean: 1.058x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                           |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 640 ms: 1.63x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                           |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.58x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 346 ms: 1.57x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.55x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.35x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.54x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.2 ms: 1.11x faster                                                          |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                           |
| nbody          | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                          |
| regex_compile  | 144 ms                                                       | 134 ms: 1.08x faster                                                           |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                           |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.1 ms: 1.07x faster                                                          |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 82.7 ms: 1.04x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                           |
| pickle_pure_python   | 318 us                                                       | 324 us: 1.02x slower                                                           |
| json_loads           | 24.4 us                                                      | 26.0 us: 1.07x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                          |
| python_startup         | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                          |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 646 ms: 1.63x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 640 ms: 1.63x faster                                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                           |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.58x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 346 ms: 1.57x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.55x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.35x faster                                                           |
| deepcopy                   | 368 us                                                       | 278 us: 1.32x faster                                                           |
| generators                 | 37.4 ms                                                      | 28.3 ms: 1.32x faster                                                          |
| comprehensions             | 21.9 us                                                      | 16.7 us: 1.31x faster                                                          |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                          |
| go                         | 150 ms                                                       | 122 ms: 1.23x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                          |
| logging_format             | 7.48 us                                                      | 6.66 us: 1.12x faster                                                          |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                           |
| logging_simple             | 6.71 us                                                      | 6.06 us: 1.11x faster                                                          |
| float                      | 76.6 ms                                                      | 69.2 ms: 1.11x faster                                                          |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.10x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 73.3 ms: 1.10x faster                                                          |
| spectral_norm              | 91.6 ms                                                      | 83.6 ms: 1.10x faster                                                          |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                          |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                           |
| regex_compile              | 144 ms                                                       | 134 ms: 1.08x faster                                                           |
| raytrace                   | 298 ms                                                       | 277 ms: 1.08x faster                                                           |
| chaos                      | 64.0 ms                                                      | 59.5 ms: 1.07x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 96.1 ms: 1.07x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.5 ms: 1.07x faster                                                          |
| sympy_str                  | 302 ms                                                       | 285 ms: 1.06x faster                                                           |
| mdp                        | 2.57 sec                                                     | 2.42 sec: 1.06x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 93.2 ms: 1.06x faster                                                          |
| tomli_loads                | 2.16 sec                                                     | 2.05 sec: 1.05x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 770 ms: 1.05x faster                                                           |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                          |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.05x faster                                                          |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.1 ms: 1.04x faster                                                          |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.70 ms: 1.04x faster                                                          |
| bench_thread_pool          | 950 us                                                       | 911 us: 1.04x faster                                                           |
| xml_etree_generate         | 86.1 ms                                                      | 82.7 ms: 1.04x faster                                                          |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 55.7 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 116 ms                                                       | 113 ms: 1.03x faster                                                           |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                           |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                           |
| pyflate                    | 439 ms                                                       | 432 ms: 1.01x faster                                                           |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                           |
| nbody                      | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                          |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                           |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.01x faster                                                         |
| deltablue                  | 3.24 ms                                                      | 3.25 ms: 1.00x slower                                                          |
| richards_super             | 51.3 ms                                                      | 51.7 ms: 1.01x slower                                                          |
| dulwich_log                | 65.4 ms                                                      | 66.0 ms: 1.01x slower                                                          |
| richards                   | 45.7 ms                                                      | 46.2 ms: 1.01x slower                                                          |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 324 us: 1.02x slower                                                           |
| nqueens                    | 89.9 ms                                                      | 91.4 ms: 1.02x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 6.07 ms: 1.02x slower                                                          |
| scimark_fft                | 301 ms                                                       | 309 ms: 1.03x slower                                                           |
| logging_silent             | 94.4 ns                                                      | 97.1 ns: 1.03x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 8.93 ms: 1.03x slower                                                          |
| scimark_sor                | 109 ms                                                       | 114 ms: 1.05x slower                                                           |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                           |
| async_generators           | 390 ms                                                       | 410 ms: 1.05x slower                                                           |
| json                       | 5.12 ms                                                      | 5.41 ms: 1.06x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                          |
| json_loads                 | 24.4 us                                                      | 26.0 us: 1.07x slower                                                          |
| typing_runtime_protocols   | 152 us                                                       | 164 us: 1.08x slower                                                           |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.69 ms: 1.12x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.12x slower                                                          |
| telco                      | 6.96 ms                                                      | 7.97 ms: 1.14x slower                                                          |
| coverage                   | 66.7 ms                                                      | 81.3 ms: 1.22x slower                                                          |
| python_startup             | 11.6 ms                                                      | 15.9 ms: 1.37x slower                                                          |
| create_gc_cycles           | 1.59 ms                                                      | 2.72 ms: 1.71x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                          |
| bench_mp_pool              | 4.76 ms                                                      | 1.16 sec: 243.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): pycparser, sympy_expand, xml_etree_process
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250127-3.14.0a4+-b2dd84b/bm-20250127-pythonperf2-x86_64-eendebakpt-iterator_freelists-3.14.0a4+-b2dd84b.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x