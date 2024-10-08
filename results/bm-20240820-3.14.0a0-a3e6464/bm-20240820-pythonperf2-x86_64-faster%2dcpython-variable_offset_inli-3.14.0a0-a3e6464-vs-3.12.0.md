# Results vs. 3.12.0

- fork: faster-cpython
- ref: variable_offset_inli
- machine: linux-x86_64
- commit hash: a3e6464
- commit date: 2024-08-20
- overall geometric mean: 1.02x faster
- HPT reliability: 76.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 288 ms: 1.01x slower                                                                  |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                                |
| tornado_http   | 121 ms                                                       | 118 ms: 1.02x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.37x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 787 ms: 1.34x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 552 ms: 1.26x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                                  |
| float          | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                                 |
| regex_dna      | 239 ms                                                       | 255 ms: 1.07x slower                                                                  |
| regex_v8       | 23.6 ms                                                      | 27.6 ms: 1.17x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                                 |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.24 sec: 1.04x slower                                                                |
| unpickle_pure_python | 210 us                                                       | 218 us: 1.04x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                                 |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 311 ms: 1.39x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 393 ms: 1.37x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 399 ms: 1.36x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 787 ms: 1.34x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 806 ms: 1.29x faster                                                                  |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 552 ms: 1.26x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.2 us: 1.26x faster                                                                 |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 573 ms: 1.21x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                                 |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                                 |
| bench_thread_pool          | 950 us                                                       | 854 us: 1.11x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.6 ms: 1.09x faster                                                                 |
| logging_format             | 7.48 us                                                      | 6.95 us: 1.08x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                                  |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                                                 |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                                |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                                  |
| raytrace                   | 298 ms                                                       | 291 ms: 1.03x faster                                                                  |
| tornado_http               | 121 ms                                                       | 118 ms: 1.02x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 84.3 ms: 1.02x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                                 |
| regex_effbot               | 3.57 ms                                                      | 3.52 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.2 ms: 1.01x faster                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                  |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 353 ms: 1.01x slower                                                                  |
| 2to3                       | 285 ms                                                       | 288 ms: 1.01x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 58.4 ms: 1.02x slower                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.28 ms: 1.02x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                                                 |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.03x slower                                                                |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 834 ms: 1.03x slower                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.24 sec: 1.04x slower                                                                |
| float                      | 76.6 ms                                                      | 79.7 ms: 1.04x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                                 |
| unpickle_pure_python       | 210 us                                                       | 218 us: 1.04x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                                 |
| spectral_norm              | 91.6 ms                                                      | 96.1 ms: 1.05x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.07 ms: 1.05x slower                                                                 |
| hexiom                     | 5.96 ms                                                      | 6.34 ms: 1.06x slower                                                                 |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                                                  |
| regex_dna                  | 239 ms                                                       | 255 ms: 1.07x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.46 ms: 1.07x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 103 ns: 1.09x slower                                                                  |
| richards                   | 45.7 ms                                                      | 50.1 ms: 1.09x slower                                                                 |
| richards_super             | 51.3 ms                                                      | 56.5 ms: 1.10x slower                                                                 |
| pyflate                    | 439 ms                                                       | 487 ms: 1.11x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 173 us: 1.14x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.95 ms: 1.14x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                                 |
| regex_v8                   | 23.6 ms                                                      | 27.6 ms: 1.17x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 78.4 ms: 1.18x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.05 ms: 1.29x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 4.58 ms: 1.32x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (9): bench_mp_pool, pycparser, chaos, nbody, xml_etree_parse, xml_etree_process, xml_etree_iterparse, pickle_pure_python, scimark_fft
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240820-3.14.0a0-a3e6464/bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 76.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x