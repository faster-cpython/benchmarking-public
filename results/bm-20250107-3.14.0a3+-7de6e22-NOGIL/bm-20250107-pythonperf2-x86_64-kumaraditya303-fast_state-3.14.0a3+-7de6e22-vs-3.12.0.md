# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.184x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 383 ms: 1.34x slower                                                       |
| docutils       | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                     |
| Geometric mean | (ref)                                                        | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 728 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 315 ms: 1.37x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 765 ms: 1.36x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 405 ms: 1.33x faster                                                       |
| async_tree_none            | 452 ms                                                       | 357 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 442 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 605 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 248 ms: 1.07x faster                                                       |
| float          | 76.6 ms                                                      | 104 ms: 1.36x slower                                                       |
| nbody          | 88.0 ms                                                      | 132 ms: 1.50x slower                                                       |
| Geometric mean | (ref)                                                        | 1.24x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.31 ms: 1.08x faster                                                      |
| regex_dna      | 239 ms                                                       | 251 ms: 1.05x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                      |
| regex_compile  | 144 ms                                                       | 172 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 91.3 ms: 1.13x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                       |
| json_loads           | 24.4 us                                                      | 28.1 us: 1.15x slower                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 100 ms: 1.16x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.62 sec: 1.22x slower                                                     |
| xml_etree_process    | 58.4 ms                                                      | 75.8 ms: 1.30x slower                                                      |
| json_dumps           | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                      |
| unpickle_pure_python | 210 us                                                       | 325 us: 1.55x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 514 us: 1.61x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.22x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                      |
| python_startup         | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.51x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 53.4 ms: 1.40x slower                                                      |
| mako            | 10.0 ms                                                      | 19.4 ms: 1.93x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.64x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 728 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 315 ms: 1.37x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 765 ms: 1.36x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 405 ms: 1.33x faster                                                       |
| async_tree_none            | 452 ms                                                       | 357 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 566 ms: 1.23x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 442 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 605 ms: 1.15x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 91.3 ms: 1.13x faster                                                      |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.31 ms: 1.08x faster                                                      |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 248 ms: 1.07x faster                                                       |
| deepcopy                   | 368 us                                                       | 348 us: 1.06x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.64 us: 1.05x faster                                                      |
| asyncio_websockets         | 387 ms                                                       | 379 ms: 1.02x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 23.3 ms: 1.02x slower                                                      |
| generators                 | 37.4 ms                                                      | 38.7 ms: 1.03x slower                                                      |
| regex_dna                  | 239 ms                                                       | 251 ms: 1.05x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 39.2 us: 1.07x slower                                                      |
| json                       | 5.12 ms                                                      | 5.59 ms: 1.09x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 3.81 ms: 1.10x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.15 sec: 1.10x slower                                                     |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                      |
| mdp                        | 2.57 sec                                                     | 2.88 sec: 1.12x slower                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.78 us: 1.12x slower                                                      |
| sympy_sum                  | 162 ms                                                       | 183 ms: 1.13x slower                                                       |
| scimark_fft                | 301 ms                                                       | 345 ms: 1.15x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 105 ms: 1.15x slower                                                       |
| json_loads                 | 24.4 us                                                      | 28.1 us: 1.15x slower                                                      |
| xml_etree_generate         | 86.1 ms                                                      | 100 ms: 1.16x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.45 sec: 1.18x slower                                                     |
| sympy_str                  | 302 ms                                                       | 359 ms: 1.19x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 28.5 ms: 1.19x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 78.3 ms: 1.20x slower                                                      |
| regex_compile              | 144 ms                                                       | 172 ms: 1.20x slower                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 22.7 ms: 1.21x slower                                                      |
| meteor_contest             | 128 ms                                                       | 156 ms: 1.22x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.62 sec: 1.22x slower                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 99.2 ms: 1.23x slower                                                      |
| sympy_expand               | 484 ms                                                       | 599 ms: 1.24x slower                                                       |
| comprehensions             | 21.9 us                                                      | 27.2 us: 1.24x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 113 ms: 1.26x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 145 ms: 1.26x slower                                                       |
| sqlalchemy_declarative     | 159 ms                                                       | 201 ms: 1.26x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 72.6 ms: 1.26x slower                                                      |
| logging_format             | 7.48 us                                                      | 9.59 us: 1.28x slower                                                      |
| pprint_safe_repr           | 807 ms                                                       | 1.04 sec: 1.29x slower                                                     |
| xml_etree_process          | 58.4 ms                                                      | 75.8 ms: 1.30x slower                                                      |
| logging_simple             | 6.71 us                                                      | 8.72 us: 1.30x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.17 sec: 1.31x slower                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.51 ms: 1.31x slower                                                      |
| async_generators           | 390 ms                                                       | 515 ms: 1.32x slower                                                       |
| 2to3                       | 285 ms                                                       | 383 ms: 1.34x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 133 ms: 1.35x slower                                                       |
| float                      | 76.6 ms                                                      | 104 ms: 1.36x slower                                                       |
| telco                      | 6.96 ms                                                      | 9.52 ms: 1.37x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 12.0 ms: 1.39x slower                                                      |
| django_template            | 38.2 ms                                                      | 53.4 ms: 1.40x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 14.4 ms: 1.41x slower                                                      |
| fannkuch                   | 350 ms                                                       | 516 ms: 1.47x slower                                                       |
| pyflate                    | 439 ms                                                       | 654 ms: 1.49x slower                                                       |
| nbody                      | 88.0 ms                                                      | 132 ms: 1.50x slower                                                       |
| chaos                      | 64.0 ms                                                      | 96.4 ms: 1.51x slower                                                      |
| richards_super             | 51.3 ms                                                      | 77.9 ms: 1.52x slower                                                      |
| typing_runtime_protocols   | 152 us                                                       | 231 us: 1.52x slower                                                       |
| richards                   | 45.7 ms                                                      | 70.0 ms: 1.53x slower                                                      |
| unpickle_pure_python       | 210 us                                                       | 325 us: 1.55x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 9.32 ms: 1.56x slower                                                      |
| mypy2                      | 830 ms                                                       | 1.31 sec: 1.57x slower                                                     |
| raytrace                   | 298 ms                                                       | 471 ms: 1.58x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 109 ms: 1.58x slower                                                       |
| coverage                   | 66.7 ms                                                      | 106 ms: 1.59x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 2.82 ms: 1.59x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 514 us: 1.61x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 1.55 ms: 1.63x slower                                                      |
| go                         | 150 ms                                                       | 245 ms: 1.64x slower                                                       |
| python_startup             | 11.6 ms                                                      | 19.1 ms: 1.64x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 2.35 ms: 1.71x slower                                                      |
| logging_silent             | 94.4 ns                                                      | 164 ns: 1.74x slower                                                       |
| scimark_sor                | 109 ms                                                       | 194 ms: 1.78x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                      |
| mako                       | 10.0 ms                                                      | 19.4 ms: 1.93x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 7.14 ms: 2.21x slower                                                      |
| bench_mp_pool              | 4.76 ms                                                      | 52.5 ms: 11.01x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.27x slower                                                               |
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.184x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.25x