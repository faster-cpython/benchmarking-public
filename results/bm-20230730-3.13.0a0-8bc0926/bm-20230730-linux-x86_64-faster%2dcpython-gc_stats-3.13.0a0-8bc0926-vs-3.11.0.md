
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 8bc0926
- commit date: 2023-07-30
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                              |
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                |
| float          | 77.2 ms                                                | 79.2 ms: 1.03x slower                                               |
| nbody          | 93.1 ms                                                | 96.2 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                               |
| regex_compile  | 138 ms                                                 | 137 ms: 1.00x faster                                                |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                               |
| regex_dna      | 204 ms                                                 | 215 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.74 ms: 1.29x faster                                               |
| unpickle_pure_python | 228 us                                                 | 214 us: 1.07x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                |
| pickle_pure_python   | 306 us                                                 | 297 us: 1.03x faster                                                |
| json_loads           | 26.5 us                                                | 25.9 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                               |
| tomli_loads          | 2.22 sec                                               | 2.30 sec: 1.04x slower                                              |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                               |
| unpickle_list        | 4.91 us                                                | 5.16 us: 1.05x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 57.7 ms: 1.07x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 83.8 ms: 1.10x slower                                               |
| unpickle             | 13.7 us                                                | 15.1 us: 1.10x slower                                               |
| pickle_list          | 4.11 us                                                | 4.58 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.35 ms: 1.10x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.83 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                                |
| generators               | 73.5 ms                                                | 28.2 ms: 2.61x faster                                               |
| asyncio_tcp              | 922 ms                                                 | 489 ms: 1.88x faster                                                |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                              |
| json_dumps               | 12.6 ms                                                | 9.74 ms: 1.29x faster                                               |
| mypy2                    | 420 ms                                                 | 338 ms: 1.24x faster                                                |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.16x faster                                               |
| chaos                    | 69.2 ms                                                | 59.9 ms: 1.16x faster                                               |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                               |
| deltablue                | 3.67 ms                                                | 3.31 ms: 1.11x faster                                               |
| comprehensions           | 22.4 us                                                | 20.4 us: 1.10x faster                                               |
| async_tree_none          | 526 ms                                                 | 483 ms: 1.09x faster                                                |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                              |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.30 ms: 1.08x faster                                               |
| richards_super           | 56.8 ms                                                | 52.8 ms: 1.08x faster                                               |
| coverage                 | 100 ms                                                 | 93.2 ms: 1.07x faster                                               |
| async_tree_memoization   | 627 ms                                                 | 586 ms: 1.07x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 214 us: 1.07x faster                                                |
| crypto_pyaes             | 74.7 ms                                                | 70.1 ms: 1.06x faster                                               |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.05x faster                                               |
| hexiom                   | 6.37 ms                                                | 6.08 ms: 1.05x faster                                               |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                |
| pickle_pure_python       | 306 us                                                 | 297 us: 1.03x faster                                                |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                              |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                                |
| logging_format           | 6.68 us                                                | 6.54 us: 1.02x faster                                               |
| json_loads               | 26.5 us                                                | 25.9 us: 1.02x faster                                               |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| logging_simple           | 6.03 us                                                | 5.97 us: 1.01x faster                                               |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| tornado_http             | 96.3 ms                                                | 95.3 ms: 1.01x faster                                               |
| json                     | 4.94 ms                                                | 4.89 ms: 1.01x faster                                               |
| mdp                      | 2.62 sec                                               | 2.59 sec: 1.01x faster                                              |
| nqueens                  | 83.4 ms                                                | 82.8 ms: 1.01x faster                                               |
| scimark_monte_carlo      | 68.1 ms                                                | 67.6 ms: 1.01x faster                                               |
| regex_compile            | 138 ms                                                 | 137 ms: 1.00x faster                                                |
| bench_thread_pool        | 819 us                                                 | 817 us: 1.00x faster                                                |
| sqlglot_optimize         | 53.1 ms                                                | 53.3 ms: 1.00x slower                                               |
| create_gc_cycles         | 1.49 ms                                                | 1.49 ms: 1.00x slower                                               |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.01x slower                                               |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                              |
| richards                 | 45.7 ms                                                | 46.2 ms: 1.01x slower                                               |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                              |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                               |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                |
| fannkuch                 | 388 ms                                                 | 395 ms: 1.02x slower                                                |
| pprint_safe_repr         | 701 ms                                                 | 717 ms: 1.02x slower                                                |
| float                    | 77.2 ms                                                | 79.2 ms: 1.03x slower                                               |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                               |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                               |
| nbody                    | 93.1 ms                                                | 96.2 ms: 1.03x slower                                               |
| tomli_loads              | 2.22 sec                                               | 2.30 sec: 1.04x slower                                              |
| dulwich_log              | 63.7 ms                                                | 66.3 ms: 1.04x slower                                               |
| gc_traversal             | 4.02 ms                                                | 4.19 ms: 1.04x slower                                               |
| deepcopy                 | 342 us                                                 | 357 us: 1.04x slower                                                |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                               |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.70 ms: 1.05x slower                                               |
| logging_silent           | 101 ns                                                 | 106 ns: 1.05x slower                                                |
| unpickle_list            | 4.91 us                                                | 5.16 us: 1.05x slower                                               |
| regex_dna                | 204 ms                                                 | 215 ms: 1.05x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 45.7 ns: 1.06x slower                                               |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                                |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                |
| xml_etree_process        | 53.9 ms                                                | 57.7 ms: 1.07x slower                                               |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                               |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                               |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                               |
| python_startup           | 8.52 ms                                                | 9.35 ms: 1.10x slower                                               |
| xml_etree_generate       | 76.2 ms                                                | 83.8 ms: 1.10x slower                                               |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.10x slower                                               |
| pickle_list              | 4.11 us                                                | 4.58 us: 1.11x slower                                               |
| python_startup_no_site   | 6.01 ms                                                | 6.83 ms: 1.14x slower                                               |
| telco                    | 6.58 ms                                                | 7.79 ms: 1.18x slower                                               |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                                |
| dask                     | 360 ms                                                 | 520 ms: 1.45x slower                                                |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (4): meteor_contest, bench_mp_pool, scimark_lu, scimark_sor
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
