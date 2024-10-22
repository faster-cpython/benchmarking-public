# Results vs. 3.12.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 58.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                                |
| tornado_http   | 121 ms                                                       | 117 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 775 ms: 1.36x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 542 ms: 1.29x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 817 ms: 1.27x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                                 |
| float          | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                                 |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                                  |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                                  |
| regex_v8       | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 85.4 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.02x slower                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                                 |
| json_loads           | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.45 sec: 1.13x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                                 |
| django_template | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 775 ms: 1.36x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 335 ms: 1.35x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 405 ms: 1.34x faster                                                                  |
| generators                 | 37.4 ms                                                      | 29.0 ms: 1.29x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 542 ms: 1.29x faster                                                                  |
| deepcopy                   | 368 us                                                       | 289 us: 1.28x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 817 ms: 1.27x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.4 us: 1.26x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 30.7 us: 1.20x faster                                                                 |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                                 |
| crypto_pyaes               | 80.3 ms                                                      | 71.3 ms: 1.13x faster                                                                 |
| logging_format             | 7.48 us                                                      | 6.86 us: 1.09x faster                                                                 |
| bench_thread_pool          | 950 us                                                       | 874 us: 1.09x faster                                                                  |
| raytrace                   | 298 ms                                                       | 275 ms: 1.08x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                                 |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                                 |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 4.57 ms: 1.04x faster                                                                 |
| tornado_http               | 121 ms                                                       | 117 ms: 1.03x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                                 |
| nqueens                    | 89.9 ms                                                      | 87.2 ms: 1.03x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                                  |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                                  |
| dask                       | 392 ms                                                       | 384 ms: 1.02x faster                                                                  |
| chaos                      | 64.0 ms                                                      | 62.9 ms: 1.02x faster                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                                |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.01x faster                                                                  |
| scimark_fft                | 301 ms                                                       | 297 ms: 1.01x faster                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.15 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.3 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 97.9 ms: 1.01x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 85.4 ms: 1.01x faster                                                                 |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 818 ms: 1.01x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 66.2 ms: 1.01x slower                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.02x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                                |
| sqlglot_optimize           | 57.5 ms                                                      | 58.6 ms: 1.02x slower                                                                 |
| xml_etree_process          | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 24.9 us: 1.02x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                                  |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                                |
| spectral_norm              | 91.6 ms                                                      | 95.2 ms: 1.04x slower                                                                 |
| logging_silent             | 94.4 ns                                                      | 98.1 ns: 1.04x slower                                                                 |
| sympy_expand               | 484 ms                                                       | 503 ms: 1.04x slower                                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 9.06 ms: 1.05x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                                 |
| float                      | 76.6 ms                                                      | 80.6 ms: 1.05x slower                                                                 |
| django_template            | 38.2 ms                                                      | 40.2 ms: 1.05x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.43 ms: 1.06x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.43 ms: 1.06x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.34 ms: 1.06x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 373 ms: 1.07x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 25.5 ms: 1.08x slower                                                                 |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                                  |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                                  |
| pyflate                    | 439 ms                                                       | 485 ms: 1.11x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.89 ms: 1.13x slower                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.45 sec: 1.13x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                                  |
| richards                   | 45.7 ms                                                      | 52.1 ms: 1.14x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 59.5 ms: 1.16x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 84.2 ms: 1.26x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (3): sqlglot_transpile, pickle_pure_python, xml_etree_parse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf2-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 58.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x