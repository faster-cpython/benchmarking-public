# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.047x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                              |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 648 ms: 1.62x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.62x faster                                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                              |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.57x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 515 ms: 1.35x faster                                                              |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.3 ms: 1.11x faster                                                             |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                              |
| nbody          | 88.0 ms                                                      | 89.3 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                             |
| regex_compile  | 144 ms                                                       | 136 ms: 1.06x faster                                                              |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                              |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.4 ms: 1.07x faster                                                             |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                            |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                              |
| xml_etree_generate   | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                             |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                              |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                             |
| pickle_pure_python   | 318 us                                                       | 326 us: 1.02x slower                                                              |
| json_loads           | 24.4 us                                                      | 26.8 us: 1.10x slower                                                             |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                             |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                             |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                             |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 648 ms: 1.62x faster                                                              |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.62x faster                                                              |
| async_tree_memoization_tg  | 540 ms                                                       | 334 ms: 1.62x faster                                                              |
| async_tree_none            | 452 ms                                                       | 287 ms: 1.57x faster                                                              |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                              |
| async_tree_none_tg         | 431 ms                                                       | 277 ms: 1.55x faster                                                              |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                              |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 515 ms: 1.35x faster                                                              |
| generators                 | 37.4 ms                                                      | 28.3 ms: 1.32x faster                                                             |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                              |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                             |
| deepcopy_memo              | 36.8 us                                                      | 30.7 us: 1.20x faster                                                             |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                             |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                             |
| regex_effbot               | 3.57 ms                                                      | 3.14 ms: 1.14x faster                                                             |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                              |
| float                      | 76.6 ms                                                      | 69.3 ms: 1.11x faster                                                             |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                             |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                              |
| spectral_norm              | 91.6 ms                                                      | 83.6 ms: 1.10x faster                                                             |
| logging_simple             | 6.71 us                                                      | 6.17 us: 1.09x faster                                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.5 ms: 1.09x faster                                                             |
| logging_format             | 7.48 us                                                      | 6.89 us: 1.09x faster                                                             |
| crypto_pyaes               | 80.3 ms                                                      | 74.4 ms: 1.08x faster                                                             |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 96.4 ms: 1.07x faster                                                             |
| chaos                      | 64.0 ms                                                      | 60.5 ms: 1.06x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                             |
| regex_compile              | 144 ms                                                       | 136 ms: 1.06x faster                                                              |
| django_template            | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                              |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                              |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.72 ms: 1.04x faster                                                             |
| scimark_lu                 | 98.8 ms                                                      | 95.9 ms: 1.03x faster                                                             |
| bench_thread_pool          | 950 us                                                       | 923 us: 1.03x faster                                                              |
| xml_etree_generate         | 86.1 ms                                                      | 83.8 ms: 1.03x faster                                                             |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                            |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                            |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                              |
| nqueens                    | 89.9 ms                                                      | 88.7 ms: 1.01x faster                                                             |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                              |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                              |
| pprint_safe_repr           | 807 ms                                                       | 799 ms: 1.01x faster                                                              |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                              |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                              |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.01x slower                                                            |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                              |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                              |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                             |
| nbody                      | 88.0 ms                                                      | 89.3 ms: 1.02x slower                                                             |
| dulwich_log                | 65.4 ms                                                      | 66.4 ms: 1.02x slower                                                             |
| hexiom                     | 5.96 ms                                                      | 6.06 ms: 1.02x slower                                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 58.5 ms: 1.02x slower                                                             |
| deltablue                  | 3.24 ms                                                      | 3.30 ms: 1.02x slower                                                             |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                                              |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                             |
| logging_silent             | 94.4 ns                                                      | 96.6 ns: 1.02x slower                                                             |
| pickle_pure_python         | 318 us                                                       | 326 us: 1.02x slower                                                              |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                             |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                              |
| async_generators           | 390 ms                                                       | 418 ms: 1.07x slower                                                              |
| json                       | 5.12 ms                                                      | 5.53 ms: 1.08x slower                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.55 ms: 1.08x slower                                                             |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                             |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                             |
| json_loads                 | 24.4 us                                                      | 26.8 us: 1.10x slower                                                             |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                              |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                             |
| telco                      | 6.96 ms                                                      | 7.96 ms: 1.14x slower                                                             |
| coverage                   | 66.7 ms                                                      | 76.6 ms: 1.15x slower                                                             |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                             |
| create_gc_cycles           | 1.59 ms                                                      | 2.81 ms: 1.77x slower                                                             |
| gc_traversal               | 3.48 ms                                                      | 6.59 ms: 1.89x slower                                                             |
| bench_mp_pool              | 4.76 ms                                                      | 1.27 sec: 266.99x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): richards_super, richards, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-620dde2/bm-20250129-pythonperf2-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x