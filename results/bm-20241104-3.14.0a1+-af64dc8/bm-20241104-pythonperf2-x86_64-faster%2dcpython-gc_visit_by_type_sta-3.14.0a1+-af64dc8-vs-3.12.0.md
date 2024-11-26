# Results vs. 3.12.0

- fork: faster-cpython
- ref: gc_visit_by_type_sta
- machine: linux-x86_64
- commit hash: af64dc8
- commit date: 2024-11-04
- overall geometric mean: 1.015x faster
- HPT reliability: 97.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                                   |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 330 ms: 1.37x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 835 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.25x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 868 ms: 1.21x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                                   |
| nbody          | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                                  |
| float          | 76.6 ms                                                      | 82.3 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                   |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                                  |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                                   |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                                   |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.47 sec: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                                  |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 374 ms: 1.45x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 330 ms: 1.37x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 407 ms: 1.34x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 323 ms: 1.33x faster                                                                   |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                                  |
| async_tree_io              | 1.04 sec                                                     | 835 ms: 1.25x faster                                                                   |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 560 ms: 1.25x faster                                                                   |
| generators                 | 37.4 ms                                                      | 30.2 ms: 1.24x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 868 ms: 1.21x faster                                                                   |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.19x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.96 us: 1.14x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                                   |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.10x faster                                                                  |
| go                         | 150 ms                                                       | 137 ms: 1.09x faster                                                                   |
| bench_thread_pool          | 950 us                                                       | 879 us: 1.08x faster                                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 74.5 ms: 1.08x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                                   |
| logging_format             | 7.48 us                                                      | 7.00 us: 1.07x faster                                                                  |
| async_generators           | 390 ms                                                       | 369 ms: 1.06x faster                                                                   |
| chaos                      | 64.0 ms                                                      | 60.7 ms: 1.05x faster                                                                  |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                                   |
| raytrace                   | 298 ms                                                       | 285 ms: 1.05x faster                                                                   |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                   |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.49 us: 1.03x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 95.6 ms: 1.03x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.8 ms: 1.03x faster                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                                   |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.02x faster                                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.3 ms: 1.02x faster                                                                  |
| asyncio_websockets         | 387 ms                                                       | 380 ms: 1.02x faster                                                                   |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                                   |
| xml_etree_generate         | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                                  |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.75 us: 1.01x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                                  |
| fannkuch                   | 350 ms                                                       | 352 ms: 1.01x slower                                                                   |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                                   |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                                 |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                                   |
| nbody                      | 88.0 ms                                                      | 89.7 ms: 1.02x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 67.1 ms: 1.03x slower                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 498 ms: 1.03x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 6.15 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                                   |
| spectral_norm              | 91.6 ms                                                      | 96.0 ms: 1.05x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.45 ms: 1.06x slower                                                                  |
| pyflate                    | 439 ms                                                       | 466 ms: 1.06x slower                                                                   |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                                   |
| deltablue                  | 3.24 ms                                                      | 3.45 ms: 1.06x slower                                                                  |
| django_template            | 38.2 ms                                                      | 40.7 ms: 1.07x slower                                                                  |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                  |
| richards                   | 45.7 ms                                                      | 49.0 ms: 1.07x slower                                                                  |
| float                      | 76.6 ms                                                      | 82.3 ms: 1.07x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 55.3 ms: 1.08x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.73 ms: 1.11x slower                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.47 sec: 1.15x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                                   |
| coverage                   | 66.7 ms                                                      | 78.2 ms: 1.17x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 15.8 ms: 1.36x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 5.78 ms: 1.66x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 3.05 ms: 1.92x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 2.11 sec: 443.26x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                           |

Benchmark hidden because not significant (5): scimark_fft, xml_etree_iterparse, json, json_loads, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241104-3.14.0a1+-af64dc8/bm-20241104-pythonperf2-x86_64-faster%2dcpython-gc_visit_by_type_sta-3.14.0a1+-af64dc8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 97.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x