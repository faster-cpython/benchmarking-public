# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.056x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 330 ms: 1.16x slower                                                               |
| docutils       | 2.87 sec                                                     | 3.24 sec: 1.13x slower                                                             |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 328 ms: 1.31x faster                                                               |
| async_tree_none            | 452 ms                                                       | 345 ms: 1.31x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 424 ms: 1.28x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.24x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 861 ms: 1.21x faster                                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 588 ms: 1.18x faster                                                               |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                               |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                              |
| float          | 76.6 ms                                                      | 81.1 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                              |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                               |
| regex_dna      | 239 ms                                                       | 257 ms: 1.08x slower                                                               |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                              |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                               |
| json_loads           | 24.4 us                                                      | 24.5 us: 1.00x slower                                                              |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                             |
| xml_etree_process    | 58.4 ms                                                      | 61.3 ms: 1.05x slower                                                              |
| unpickle_pure_python | 210 us                                                       | 228 us: 1.09x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 351 us: 1.10x slower                                                               |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                              |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                              |
| django_template | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.08x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 379 ms: 1.42x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 328 ms: 1.31x faster                                                               |
| async_tree_none            | 452 ms                                                       | 345 ms: 1.31x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 424 ms: 1.28x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.24x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 861 ms: 1.21x faster                                                               |
| async_tree_io_tg           | 1.05 sec                                                     | 878 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 588 ms: 1.18x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                              |
| deepcopy                   | 368 us                                                       | 325 us: 1.14x faster                                                               |
| deepcopy_memo              | 36.8 us                                                      | 33.8 us: 1.09x faster                                                              |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.17 us: 1.06x faster                                                              |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                               |
| crypto_pyaes               | 80.3 ms                                                      | 78.1 ms: 1.03x faster                                                              |
| logging_format             | 7.48 us                                                      | 7.31 us: 1.02x faster                                                              |
| comprehensions             | 21.9 us                                                      | 21.7 us: 1.01x faster                                                              |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                               |
| json_loads                 | 24.4 us                                                      | 24.5 us: 1.00x slower                                                              |
| logging_simple             | 6.71 us                                                      | 6.78 us: 1.01x slower                                                              |
| mako                       | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                              |
| json                       | 5.12 ms                                                      | 5.21 ms: 1.02x slower                                                              |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                               |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                              |
| scimark_lu                 | 98.8 ms                                                      | 102 ms: 1.03x slower                                                               |
| mdp                        | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.22 sec: 1.03x slower                                                             |
| dulwich_log                | 65.4 ms                                                      | 67.6 ms: 1.03x slower                                                              |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                              |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                              |
| pprint_safe_repr           | 807 ms                                                       | 837 ms: 1.04x slower                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.73 sec: 1.04x slower                                                             |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.05x slower                                                             |
| xml_etree_process          | 58.4 ms                                                      | 61.3 ms: 1.05x slower                                                              |
| bench_thread_pool          | 950 us                                                       | 998 us: 1.05x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                              |
| meteor_contest             | 128 ms                                                       | 135 ms: 1.06x slower                                                               |
| float                      | 76.6 ms                                                      | 81.1 ms: 1.06x slower                                                              |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                               |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                               |
| sqlalchemy_declarative     | 159 ms                                                       | 170 ms: 1.07x slower                                                               |
| raytrace                   | 298 ms                                                       | 318 ms: 1.07x slower                                                               |
| scimark_monte_carlo        | 69.0 ms                                                      | 73.8 ms: 1.07x slower                                                              |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.08x slower                                                               |
| regex_dna                  | 239 ms                                                       | 257 ms: 1.08x slower                                                               |
| scimark_fft                | 301 ms                                                       | 326 ms: 1.08x slower                                                               |
| unpickle_pure_python       | 210 us                                                       | 228 us: 1.09x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 3.55 ms: 1.10x slower                                                              |
| spectral_norm              | 91.6 ms                                                      | 101 ms: 1.10x slower                                                               |
| sympy_str                  | 302 ms                                                       | 332 ms: 1.10x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 351 us: 1.10x slower                                                               |
| go                         | 150 ms                                                       | 165 ms: 1.10x slower                                                               |
| chaos                      | 64.0 ms                                                      | 70.9 ms: 1.11x slower                                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.53 ms: 1.11x slower                                                              |
| richards                   | 45.7 ms                                                      | 50.8 ms: 1.11x slower                                                              |
| sympy_sum                  | 162 ms                                                       | 181 ms: 1.12x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                              |
| docutils                   | 2.87 sec                                                     | 3.24 sec: 1.13x slower                                                             |
| sympy_expand               | 484 ms                                                       | 548 ms: 1.13x slower                                                               |
| telco                      | 6.96 ms                                                      | 7.89 ms: 1.13x slower                                                              |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                              |
| richards_super             | 51.3 ms                                                      | 58.6 ms: 1.14x slower                                                              |
| sqlglot_transpile          | 1.78 ms                                                      | 2.03 ms: 1.14x slower                                                              |
| fannkuch                   | 350 ms                                                       | 403 ms: 1.15x slower                                                               |
| django_template            | 38.2 ms                                                      | 44.0 ms: 1.15x slower                                                              |
| 2to3                       | 285 ms                                                       | 330 ms: 1.16x slower                                                               |
| generators                 | 37.4 ms                                                      | 43.4 ms: 1.16x slower                                                              |
| pyflate                    | 439 ms                                                       | 511 ms: 1.17x slower                                                               |
| sympy_integrate            | 23.9 ms                                                      | 28.1 ms: 1.17x slower                                                              |
| coverage                   | 66.7 ms                                                      | 78.8 ms: 1.18x slower                                                              |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.00 ms: 1.19x slower                                                              |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.22x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                               |
| async_generators           | 390 ms                                                       | 479 ms: 1.23x slower                                                               |
| sqlglot_normalize          | 116 ms                                                       | 144 ms: 1.25x slower                                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 74.3 ms: 1.29x slower                                                              |
| hexiom                     | 5.96 ms                                                      | 7.96 ms: 1.34x slower                                                              |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                              |
| gc_traversal               | 3.48 ms                                                      | 6.29 ms: 1.81x slower                                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                              |
| bench_mp_pool              | 4.76 ms                                                      | 1.37 sec: 288.27x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.13x slower                                                                       |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_generate, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x