# Results vs. 3.12.0

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: de9adc3
- commit date: 2025-02-06
- overall geometric mean: 1.043x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 340 ms: 1.59x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 658 ms: 1.58x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                                  |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                                   |
| nbody          | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                                  |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| regex_dna      | 239 ms                                                       | 231 ms: 1.03x faster                                                                   |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 98.7 ms: 1.04x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.04x faster                                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 83.9 ms: 1.03x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                                   |
| xml_etree_process    | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 329 us: 1.03x slower                                                                   |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.2 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                  |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 340 ms: 1.59x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 658 ms: 1.58x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 279 ms: 1.54x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 353 ms: 1.54x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 523 ms: 1.33x faster                                                                   |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                                  |
| deepcopy                   | 368 us                                                       | 288 us: 1.28x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.27x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 30.5 us: 1.21x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 15.8 ms: 1.20x faster                                                                  |
| go                         | 150 ms                                                       | 127 ms: 1.17x faster                                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                                   |
| spectral_norm              | 91.6 ms                                                      | 83.1 ms: 1.10x faster                                                                  |
| float                      | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.87 us: 1.09x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.20 us: 1.08x faster                                                                  |
| raytrace                   | 298 ms                                                       | 277 ms: 1.08x faster                                                                   |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                                   |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| crypto_pyaes               | 80.3 ms                                                      | 75.4 ms: 1.07x faster                                                                  |
| chaos                      | 64.0 ms                                                      | 60.0 ms: 1.07x faster                                                                  |
| django_template            | 38.2 ms                                                      | 35.9 ms: 1.06x faster                                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.8 ms: 1.06x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.4 ms: 1.06x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.1 ms: 1.05x faster                                                                  |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.05x faster                                                                 |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 98.7 ms: 1.04x faster                                                                  |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                                   |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.04x faster                                                                   |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 231 ms: 1.03x faster                                                                   |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                                   |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 83.9 ms: 1.03x faster                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.74 ms: 1.02x faster                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.35 ms: 1.02x faster                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                                 |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                                  |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                                   |
| sqlglot_normalize          | 116 ms                                                       | 116 ms: 1.01x slower                                                                   |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                                  |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                                   |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                                   |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                                 |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.02x slower                                                                  |
| richards                   | 45.7 ms                                                      | 47.0 ms: 1.03x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 96.9 ns: 1.03x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                                   |
| deltablue                  | 3.24 ms                                                      | 3.33 ms: 1.03x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 52.9 ms: 1.03x slower                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 60.2 ms: 1.03x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 90.8 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 329 us: 1.03x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                                  |
| async_generators           | 390 ms                                                       | 405 ms: 1.04x slower                                                                   |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                                  |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.05x slower                                                                   |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.49 ms: 1.07x slower                                                                  |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.76 ms: 1.13x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 77.5 ms: 1.16x slower                                                                  |
| telco                      | 6.96 ms                                                      | 8.11 ms: 1.17x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 16.2 ms: 1.39x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.76 ms: 1.73x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.38 ms: 1.83x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.64 sec: 343.28x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                           |

Benchmark hidden because not significant (5): asyncio_websockets, docutils, sqlglot_optimize, pyflate, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250206-3.14.0a4+-de9adc3/bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x