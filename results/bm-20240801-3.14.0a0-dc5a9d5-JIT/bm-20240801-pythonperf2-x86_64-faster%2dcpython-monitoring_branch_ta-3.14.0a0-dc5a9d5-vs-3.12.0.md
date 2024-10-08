# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: linux-x86_64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.02x faster
- HPT reliability: 66.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 306 ms: 1.07x slower                                                                  |
| docutils       | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                                |
| tornado_http   | 121 ms                                                       | 119 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 762 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 788 ms: 1.32x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 538 ms: 1.30x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.06x faster                                                                  |
| float          | 76.6 ms                                                      | 76.1 ms: 1.01x faster                                                                 |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                                 |
| regex_dna      | 239 ms                                                       | 235 ms: 1.01x faster                                                                  |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 97.7 ms: 1.05x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                                |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                                 |
| pickle_pure_python   | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                                  |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.05 ms: 1.11x faster                                                                 |
| django_template | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 302 ms: 1.43x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 762 ms: 1.38x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 788 ms: 1.32x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 538 ms: 1.30x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 578 ms: 1.20x faster                                                                  |
| deepcopy                   | 368 us                                                       | 306 us: 1.20x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 18.4 us: 1.19x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 70.5 ms: 1.14x faster                                                                 |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                                 |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                                 |
| mako                       | 10.0 ms                                                      | 9.05 ms: 1.11x faster                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.85 ms: 1.09x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                                 |
| logging_format             | 7.48 us                                                      | 6.88 us: 1.09x faster                                                                 |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                                 |
| scimark_fft                | 301 ms                                                       | 284 ms: 1.06x faster                                                                  |
| pidigits                   | 265 ms                                                       | 251 ms: 1.06x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 97.7 ms: 1.05x faster                                                                 |
| async_generators           | 390 ms                                                       | 372 ms: 1.05x faster                                                                  |
| bench_thread_pool          | 950 us                                                       | 905 us: 1.05x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                                 |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.01x faster                                                                  |
| tornado_http               | 121 ms                                                       | 119 ms: 1.01x faster                                                                  |
| generators                 | 37.4 ms                                                      | 36.9 ms: 1.01x faster                                                                 |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                                                 |
| fannkuch                   | 350 ms                                                       | 345 ms: 1.01x faster                                                                  |
| richards                   | 45.7 ms                                                      | 45.2 ms: 1.01x faster                                                                 |
| float                      | 76.6 ms                                                      | 76.1 ms: 1.01x faster                                                                 |
| pickle_pure_python         | 318 us                                                       | 317 us: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                                  |
| pyflate                    | 439 ms                                                       | 442 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                                  |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                                |
| pprint_safe_repr           | 807 ms                                                       | 819 ms: 1.01x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 52.8 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| sympy_str                  | 302 ms                                                       | 312 ms: 1.03x slower                                                                  |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                                |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.04x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                 |
| chaos                      | 64.0 ms                                                      | 66.5 ms: 1.04x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.86 ms: 1.05x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                                 |
| 2to3                       | 285 ms                                                       | 306 ms: 1.07x slower                                                                  |
| django_template            | 38.2 ms                                                      | 41.2 ms: 1.08x slower                                                                 |
| docutils                   | 2.87 sec                                                     | 3.12 sec: 1.09x slower                                                                |
| sympy_integrate            | 23.9 ms                                                      | 26.0 ms: 1.09x slower                                                                 |
| sqlglot_optimize           | 57.5 ms                                                      | 62.6 ms: 1.09x slower                                                                 |
| nqueens                    | 89.9 ms                                                      | 98.2 ms: 1.09x slower                                                                 |
| sympy_expand               | 484 ms                                                       | 531 ms: 1.10x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                                  |
| go                         | 150 ms                                                       | 165 ms: 1.10x slower                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 110 ms: 1.11x slower                                                                  |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.11x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.60 ms: 1.11x slower                                                                 |
| telco                      | 6.96 ms                                                      | 7.82 ms: 1.12x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.74 ms: 1.13x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 127 ms: 1.16x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 79.5 ms: 1.19x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 1.92 ms: 1.21x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (5): asyncio_tcp, raytrace, dask, asyncio_tcp_ssl, bench_mp_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-pythonperf2-x86_64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 66.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x