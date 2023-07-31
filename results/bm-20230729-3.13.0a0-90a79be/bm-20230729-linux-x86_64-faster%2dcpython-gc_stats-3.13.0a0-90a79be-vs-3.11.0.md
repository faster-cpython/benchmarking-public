
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 90a79be
- commit date: 2023-07-29
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.65 sec: 1.01x slower                                              |
| tornado_http   | 96.3 ms                                                | 95.6 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                               |
| float          | 77.2 ms                                                | 81.4 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                               |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.67 ms: 1.30x faster                                               |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                |
| pickle_pure_python   | 306 us                                                 | 295 us: 1.04x faster                                                |
| json_loads           | 26.5 us                                                | 26.1 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                               |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 58.0 ms: 1.08x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 84.1 ms: 1.10x slower                                               |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                               |
| pickle_list          | 4.11 us                                                | 4.71 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.39 ms: 1.10x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.87 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-90a79be |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.34x faster                                                |
| generators               | 73.5 ms                                                | 29.1 ms: 2.52x faster                                               |
| asyncio_tcp              | 922 ms                                                 | 478 ms: 1.93x faster                                                |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                              |
| json_dumps               | 12.6 ms                                                | 9.67 ms: 1.30x faster                                               |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                                |
| coroutines               | 25.5 ms                                                | 21.6 ms: 1.18x faster                                               |
| chaos                    | 69.2 ms                                                | 60.3 ms: 1.15x faster                                               |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                               |
| deltablue                | 3.67 ms                                                | 3.29 ms: 1.12x faster                                               |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                               |
| raytrace                 | 297 ms                                                 | 272 ms: 1.09x faster                                                |
| async_tree_none          | 526 ms                                                 | 483 ms: 1.09x faster                                                |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                              |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.08x faster                                               |
| richards_super           | 56.8 ms                                                | 52.7 ms: 1.08x faster                                               |
| coverage                 | 100 ms                                                 | 93.4 ms: 1.07x faster                                               |
| async_tree_memoization   | 627 ms                                                 | 587 ms: 1.07x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.07x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                               |
| crypto_pyaes             | 74.7 ms                                                | 71.0 ms: 1.05x faster                                               |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                |
| hexiom                   | 6.37 ms                                                | 6.09 ms: 1.05x faster                                               |
| nqueens                  | 83.4 ms                                                | 79.9 ms: 1.04x faster                                               |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                |
| pickle_pure_python       | 306 us                                                 | 295 us: 1.04x faster                                                |
| logging_format           | 6.68 us                                                | 6.45 us: 1.04x faster                                               |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 723 ms: 1.02x faster                                                |
| logging_simple           | 6.03 us                                                | 5.92 us: 1.02x faster                                               |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                                |
| json_loads               | 26.5 us                                                | 26.1 us: 1.02x faster                                               |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                |
| scimark_monte_carlo      | 68.1 ms                                                | 67.2 ms: 1.01x faster                                               |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| gc_traversal             | 4.02 ms                                                | 3.98 ms: 1.01x faster                                               |
| json                     | 4.94 ms                                                | 4.90 ms: 1.01x faster                                               |
| go                       | 140 ms                                                 | 139 ms: 1.01x faster                                                |
| tornado_http             | 96.3 ms                                                | 95.6 ms: 1.01x faster                                               |
| bench_thread_pool        | 819 us                                                 | 815 us: 1.00x faster                                                |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                               |
| docutils                 | 2.63 sec                                               | 2.65 sec: 1.01x slower                                              |
| nbody                    | 93.1 ms                                                | 94.2 ms: 1.01x slower                                               |
| richards                 | 45.7 ms                                                | 46.4 ms: 1.02x slower                                               |
| deepcopy_memo            | 37.0 us                                                | 37.7 us: 1.02x slower                                               |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                               |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                              |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                                |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                               |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                                |
| deepcopy                 | 342 us                                                 | 350 us: 1.02x slower                                                |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                                |
| pprint_safe_repr         | 701 ms                                                 | 722 ms: 1.03x slower                                                |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                               |
| fannkuch                 | 388 ms                                                 | 401 ms: 1.03x slower                                                |
| mdp                      | 2.62 sec                                               | 2.70 sec: 1.03x slower                                              |
| pickle                   | 10.1 us                                                | 10.4 us: 1.03x slower                                               |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                              |
| dulwich_log              | 63.7 ms                                                | 66.1 ms: 1.04x slower                                               |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                               |
| float                    | 77.2 ms                                                | 81.4 ms: 1.05x slower                                               |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.76 ms: 1.06x slower                                               |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                                |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                |
| deepcopy_reduce          | 2.94 us                                                | 3.14 us: 1.07x slower                                               |
| xml_etree_process        | 53.9 ms                                                | 58.0 ms: 1.08x slower                                               |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                               |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 47.3 ns: 1.10x slower                                               |
| python_startup           | 8.52 ms                                                | 9.39 ms: 1.10x slower                                               |
| xml_etree_generate       | 76.2 ms                                                | 84.1 ms: 1.10x slower                                               |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                               |
| python_startup_no_site   | 6.01 ms                                                | 6.87 ms: 1.14x slower                                               |
| pickle_list              | 4.11 us                                                | 4.71 us: 1.15x slower                                               |
| telco                    | 6.58 ms                                                | 7.88 ms: 1.20x slower                                               |
| async_generators         | 368 ms                                                 | 455 ms: 1.24x slower                                                |
| dask                     | 360 ms                                                 | 519 ms: 1.44x slower                                                |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (4): pycparser, sqlglot_optimize, bench_mp_pool, unpickle_list
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
