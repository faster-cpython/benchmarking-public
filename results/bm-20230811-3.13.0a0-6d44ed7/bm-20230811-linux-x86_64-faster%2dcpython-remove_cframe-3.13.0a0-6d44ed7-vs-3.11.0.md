
# Results vs. 3.11.0

- fork: faster-cpython
- ref: remove_cframe
- machine: linux-x86_64
- commit hash: 6d44ed7
- commit date: 2023-08-11
- overall geometric mean: 1.04x faster
- HPT reliability: 85.67%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                    |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                     |
| float          | 77.2 ms                                                | 79.6 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.79 ms: 1.05x faster                                                    |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                     |
| regex_v8       | 22.0 ms                                                | 23.1 ms: 1.05x slower                                                    |
| regex_dna      | 204 ms                                                 | 215 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                     |
| tomli_loads          | 2.22 sec                                               | 2.12 sec: 1.05x faster                                                   |
| json_loads           | 26.5 us                                                | 25.3 us: 1.05x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                                    |
| unpickle             | 13.7 us                                                | 14.0 us: 1.02x slower                                                    |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 57.6 ms: 1.07x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 83.0 ms: 1.09x slower                                                    |
| pickle_list          | 4.11 us                                                | 4.60 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230811-linux-x86_64-faster%2dcpython-remove_cframe-3.13.0a0-6d44ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                                     |
| generators               | 73.5 ms                                                | 28.9 ms: 2.54x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                     |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                   |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                    |
| async_tree_none          | 526 ms                                                 | 436 ms: 1.21x faster                                                     |
| coverage                 | 100 ms                                                 | 84.9 ms: 1.18x faster                                                    |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                    |
| chaos                    | 69.2 ms                                                | 60.5 ms: 1.14x faster                                                    |
| async_tree_memoization   | 627 ms                                                 | 561 ms: 1.12x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.30 ms: 1.11x faster                                                    |
| sqlglot_parse            | 1.40 ms                                                | 1.26 ms: 1.11x faster                                                    |
| crypto_pyaes             | 74.7 ms                                                | 67.7 ms: 1.10x faster                                                    |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                   |
| raytrace                 | 297 ms                                                 | 271 ms: 1.09x faster                                                     |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                                    |
| sqlglot_transpile        | 1.70 ms                                                | 1.58 ms: 1.08x faster                                                    |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.07x faster                                                     |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 696 ms: 1.06x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.04 ms: 1.05x faster                                                    |
| regex_effbot             | 3.99 ms                                                | 3.79 ms: 1.05x faster                                                    |
| tomli_loads              | 2.22 sec                                               | 2.12 sec: 1.05x faster                                                   |
| json_loads               | 26.5 us                                                | 25.3 us: 1.05x faster                                                    |
| richards_super           | 56.8 ms                                                | 54.3 ms: 1.05x faster                                                    |
| logging_format           | 6.68 us                                                | 6.42 us: 1.04x faster                                                    |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                     |
| nbody                    | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                    |
| unpack_sequence          | 43.1 ns                                                | 41.8 ns: 1.03x faster                                                    |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| json                     | 4.94 ms                                                | 4.82 ms: 1.03x faster                                                    |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                   |
| mdp                      | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 66.5 ms: 1.02x faster                                                    |
| nqueens                  | 83.4 ms                                                | 81.6 ms: 1.02x faster                                                    |
| logging_simple           | 6.03 us                                                | 5.91 us: 1.02x faster                                                    |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                                     |
| xml_etree_iterparse      | 104 ms                                                 | 102 ms: 1.02x faster                                                     |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                     |
| tornado_http             | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                    |
| fannkuch                 | 388 ms                                                 | 384 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 53.1 ms                                                | 52.6 ms: 1.01x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                    |
| bench_thread_pool        | 819 us                                                 | 815 us: 1.00x faster                                                     |
| deepcopy_memo            | 37.0 us                                                | 37.1 us: 1.00x slower                                                    |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.00x slower                                                    |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                   |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                     |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                                    |
| pprint_safe_repr         | 701 ms                                                 | 714 ms: 1.02x slower                                                     |
| unpickle                 | 13.7 us                                                | 14.0 us: 1.02x slower                                                    |
| deepcopy                 | 342 us                                                 | 351 us: 1.03x slower                                                     |
| float                    | 77.2 ms                                                | 79.6 ms: 1.03x slower                                                    |
| dulwich_log              | 63.7 ms                                                | 65.9 ms: 1.03x slower                                                    |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                                     |
| gc_traversal             | 4.02 ms                                                | 4.18 ms: 1.04x slower                                                    |
| scimark_lu               | 110 ms                                                 | 114 ms: 1.04x slower                                                     |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                                     |
| regex_v8                 | 22.0 ms                                                | 23.1 ms: 1.05x slower                                                    |
| richards                 | 45.7 ms                                                | 48.0 ms: 1.05x slower                                                    |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                     |
| regex_dna                | 204 ms                                                 | 215 ms: 1.06x slower                                                     |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                    |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                    |
| xml_etree_process        | 53.9 ms                                                | 57.6 ms: 1.07x slower                                                    |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                                     |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                     |
| deepcopy_reduce          | 2.94 us                                                | 3.17 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.88 ms: 1.09x slower                                                    |
| xml_etree_generate       | 76.2 ms                                                | 83.0 ms: 1.09x slower                                                    |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                                    |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                                    |
| pickle_list              | 4.11 us                                                | 4.60 us: 1.12x slower                                                    |
| python_startup_no_site   | 6.01 ms                                                | 6.82 ms: 1.14x slower                                                    |
| telco                    | 6.58 ms                                                | 7.94 ms: 1.21x slower                                                    |
| async_generators         | 368 ms                                                 | 457 ms: 1.24x slower                                                     |
| dask                     | 360 ms                                                 | 516 ms: 1.44x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (6): meteor_contest, bench_mp_pool, docutils, unpickle_list, go, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 85.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
