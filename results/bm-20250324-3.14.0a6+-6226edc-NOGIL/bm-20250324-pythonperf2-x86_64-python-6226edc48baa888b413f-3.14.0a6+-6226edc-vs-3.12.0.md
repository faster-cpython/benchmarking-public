# Results vs. 3.12.0

- fork: python
- ref: 6226edc48baa888b413f
- machine: linux-x86_64
- commit hash: 6226edc
- commit date: 2025-03-24
- overall geometric mean: 1.052x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 326 ms: 1.14x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 549 ms: 1.92x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 579 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 243 ms: 1.77x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 307 ms: 1.76x faster                                                         |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 337 ms: 1.61x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 474 ms: 1.47x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 510 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.66x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 249 ms: 1.07x faster                                                         |
| float          | 76.6 ms                                                      | 77.0 ms: 1.00x slower                                                        |
| nbody          | 88.0 ms                                                      | 133 ms: 1.52x slower                                                         |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                        |
| regex_compile  | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.7 ms: 1.15x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 97.5 ms: 1.13x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 367 us: 1.15x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 244 us: 1.17x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                        |
| json_loads           | 24.4 us                                                      | 29.2 us: 1.20x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                        |
| python_startup         | 11.6 ms                                                      | 19.4 ms: 1.67x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 45.7 ms: 1.20x slower                                                        |
| mako            | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 549 ms: 1.92x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 579 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 243 ms: 1.77x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 307 ms: 1.76x faster                                                         |
| gc_traversal               | 3.48 ms                                                      | 2.10 ms: 1.65x faster                                                        |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.63x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 337 ms: 1.61x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 474 ms: 1.47x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 510 ms: 1.37x faster                                                         |
| generators                 | 37.4 ms                                                      | 30.6 ms: 1.22x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 89.7 ms: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.12 ms: 1.14x faster                                                        |
| deepcopy                   | 368 us                                                       | 333 us: 1.11x faster                                                         |
| comprehensions             | 21.9 us                                                      | 20.2 us: 1.08x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.5 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.60 us: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 249 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| asyncio_websockets         | 387 ms                                                       | 375 ms: 1.03x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 36.2 us: 1.02x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                        |
| float                      | 76.6 ms                                                      | 77.0 ms: 1.00x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.02x slower                                                       |
| go                         | 150 ms                                                       | 153 ms: 1.02x slower                                                         |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.51 us: 1.04x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 97.3 ms: 1.06x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| sympy_sum                  | 162 ms                                                       | 175 ms: 1.08x slower                                                         |
| logging_format             | 7.48 us                                                      | 8.07 us: 1.08x slower                                                        |
| logging_simple             | 6.71 us                                                      | 7.24 us: 1.08x slower                                                        |
| chaos                      | 64.0 ms                                                      | 69.2 ms: 1.08x slower                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 173 ms: 1.08x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.80 sec: 1.09x slower                                                       |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                         |
| raytrace                   | 298 ms                                                       | 328 ms: 1.10x slower                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 20.7 ms: 1.10x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| json                       | 5.12 ms                                                      | 5.66 ms: 1.11x slower                                                        |
| sympy_str                  | 302 ms                                                       | 334 ms: 1.11x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                                        |
| regex_compile              | 144 ms                                                       | 161 ms: 1.12x slower                                                         |
| pprint_safe_repr           | 807 ms                                                       | 904 ms: 1.12x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.86 sec: 1.13x slower                                                       |
| pyflate                    | 439 ms                                                       | 495 ms: 1.13x slower                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 97.5 ms: 1.13x slower                                                        |
| 2to3                       | 285 ms                                                       | 326 ms: 1.14x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 91.9 ms: 1.14x slower                                                        |
| scimark_fft                | 301 ms                                                       | 347 ms: 1.15x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 367 us: 1.15x slower                                                         |
| sympy_expand               | 484 ms                                                       | 564 ms: 1.17x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 244 us: 1.17x slower                                                         |
| django_template            | 38.2 ms                                                      | 45.7 ms: 1.20x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                        |
| json_loads                 | 24.4 us                                                      | 29.2 us: 1.20x slower                                                        |
| meteor_contest             | 128 ms                                                       | 154 ms: 1.20x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.22x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.44 ms: 1.25x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 4.05 ms: 1.25x slower                                                        |
| richards                   | 45.7 ms                                                      | 57.3 ms: 1.25x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 124 ms: 1.25x slower                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 86.7 ms: 1.26x slower                                                        |
| async_generators           | 390 ms                                                       | 495 ms: 1.27x slower                                                         |
| richards_super             | 51.3 ms                                                      | 66.8 ms: 1.30x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.3 ms: 1.30x slower                                                        |
| fannkuch                   | 350 ms                                                       | 473 ms: 1.35x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.73 ms: 1.36x slower                                                        |
| telco                      | 6.96 ms                                                      | 9.51 ms: 1.37x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 214 us: 1.41x slower                                                         |
| nbody                      | 88.0 ms                                                      | 133 ms: 1.52x slower                                                         |
| bench_thread_pool          | 950 us                                                       | 1.44 ms: 1.52x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 13.8 ms: 1.60x slower                                                        |
| python_startup             | 11.6 ms                                                      | 19.4 ms: 1.67x slower                                                        |
| mako                       | 10.0 ms                                                      | 17.7 ms: 1.77x slower                                                        |
| coverage                   | 66.7 ms                                                      | 121 ms: 1.81x slower                                                         |
| bench_mp_pool              | 4.76 ms                                                      | 50.4 ms: 10.58x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.09x slower                                                                 |
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250324-3.14.0a6+-6226edc-NOGIL/bm-20250324-pythonperf2-x86_64-python-6226edc48baa888b413f-3.14.0a6+-6226edc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.28x