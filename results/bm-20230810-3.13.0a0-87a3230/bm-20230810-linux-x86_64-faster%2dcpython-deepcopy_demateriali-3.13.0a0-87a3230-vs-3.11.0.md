
# Results vs. 3.11.0

- fork: faster-cpython
- ref: deepcopy_demateriali
- machine: linux-x86_64
- commit hash: 87a3230
- commit date: 2023-08-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tornado_http   | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                            |
| nbody          | 93.1 ms                                                | 90.5 ms: 1.03x faster                                                           |
| float          | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                           |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                            |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                           |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.88 ms: 1.27x faster                                                           |
| unpickle_pure_python | 228 us                                                 | 213 us: 1.07x faster                                                            |
| tomli_loads          | 2.22 sec                                               | 2.08 sec: 1.07x faster                                                          |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                            |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                           |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                            |
| pickle_dict          | 31.1 us                                                | 32.0 us: 1.03x slower                                                           |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                                           |
| xml_etree_process    | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                           |
| pickle               | 10.1 us                                                | 10.6 us: 1.06x slower                                                           |
| xml_etree_generate   | 76.2 ms                                                | 82.4 ms: 1.08x slower                                                           |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                                           |
| pickle_list          | 4.11 us                                                | 4.60 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.39 ms: 1.10x slower                                                           |
| python_startup_no_site | 6.01 ms                                                | 6.88 ms: 1.14x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-deepcopy_demateriali-3.13.0a0-87a3230 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.34x faster                                                            |
| generators               | 73.5 ms                                                | 28.7 ms: 2.56x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 483 ms: 1.91x faster                                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                          |
| json_dumps               | 12.6 ms                                                | 9.88 ms: 1.27x faster                                                           |
| async_tree_none          | 526 ms                                                 | 435 ms: 1.21x faster                                                            |
| coverage                 | 100 ms                                                 | 84.7 ms: 1.18x faster                                                           |
| coroutines               | 25.5 ms                                                | 21.8 ms: 1.17x faster                                                           |
| chaos                    | 69.2 ms                                                | 59.5 ms: 1.16x faster                                                           |
| deltablue                | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                           |
| regex_effbot             | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                           |
| async_tree_memoization   | 627 ms                                                 | 562 ms: 1.12x faster                                                            |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.09x faster                                                           |
| raytrace                 | 297 ms                                                 | 274 ms: 1.08x faster                                                            |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                                           |
| unpickle_pure_python     | 228 us                                                 | 213 us: 1.07x faster                                                            |
| crypto_pyaes             | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                           |
| tomli_loads              | 2.22 sec                                               | 2.08 sec: 1.07x faster                                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 697 ms: 1.06x faster                                                            |
| hexiom                   | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                           |
| richards_super           | 56.8 ms                                                | 53.7 ms: 1.06x faster                                                           |
| nqueens                  | 83.4 ms                                                | 79.2 ms: 1.05x faster                                                           |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                            |
| logging_format           | 6.68 us                                                | 6.41 us: 1.04x faster                                                           |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                            |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.04x faster                                                            |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                          |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                           |
| gc_traversal             | 4.02 ms                                                | 3.90 ms: 1.03x faster                                                           |
| nbody                    | 93.1 ms                                                | 90.5 ms: 1.03x faster                                                           |
| logging_simple           | 6.03 us                                                | 5.88 us: 1.03x faster                                                           |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                                            |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.02x faster                                                            |
| tornado_http             | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                           |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                           |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 67.5 ms: 1.01x faster                                                           |
| logging_silent           | 101 ns                                                 | 100 ns: 1.01x faster                                                            |
| go                       | 140 ms                                                 | 140 ms: 1.00x slower                                                            |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                           |
| fannkuch                 | 388 ms                                                 | 392 ms: 1.01x slower                                                            |
| regex_dna                | 204 ms                                                 | 207 ms: 1.01x slower                                                            |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                                           |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                          |
| pickle_dict              | 31.1 us                                                | 32.0 us: 1.03x slower                                                           |
| mdp                      | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                          |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                                            |
| dulwich_log              | 63.7 ms                                                | 65.7 ms: 1.03x slower                                                           |
| deepcopy                 | 342 us                                                 | 354 us: 1.03x slower                                                            |
| pprint_safe_repr         | 701 ms                                                 | 726 ms: 1.04x slower                                                            |
| float                    | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                           |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                                            |
| unpack_sequence          | 43.1 ns                                                | 44.9 ns: 1.04x slower                                                           |
| unpickle_list            | 4.91 us                                                | 5.12 us: 1.04x slower                                                           |
| richards                 | 45.7 ms                                                | 47.8 ms: 1.05x slower                                                           |
| xml_etree_process        | 53.9 ms                                                | 56.7 ms: 1.05x slower                                                           |
| pickle                   | 10.1 us                                                | 10.6 us: 1.06x slower                                                           |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                            |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                           |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                            |
| xml_etree_generate       | 76.2 ms                                                | 82.4 ms: 1.08x slower                                                           |
| pyflate                  | 418 ms                                                 | 452 ms: 1.08x slower                                                            |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.08x slower                                                           |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.91 ms: 1.09x slower                                                           |
| python_startup           | 8.52 ms                                                | 9.39 ms: 1.10x slower                                                           |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                                           |
| pickle_list              | 4.11 us                                                | 4.60 us: 1.12x slower                                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.88 ms: 1.14x slower                                                           |
| telco                    | 6.58 ms                                                | 7.80 ms: 1.18x slower                                                           |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                                            |
| dask                     | 360 ms                                                 | 518 ms: 1.44x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (7): meteor_contest, json, docutils, bench_thread_pool, deepcopy_memo, bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
