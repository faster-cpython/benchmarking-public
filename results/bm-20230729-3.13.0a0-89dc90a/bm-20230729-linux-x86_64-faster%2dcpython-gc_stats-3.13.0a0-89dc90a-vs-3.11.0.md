
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 89dc90a
- commit date: 2023-07-29
- overall geometric mean: 1.04x faster
- HPT reliability: 76.10%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                              |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 92.3 ms: 1.01x faster                                               |
| pidigits       | 198 ms                                                 | 201 ms: 1.01x slower                                                |
| float          | 77.2 ms                                                | 80.7 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                               |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                                |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                               |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.76 ms: 1.29x faster                                               |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                |
| pickle_pure_python   | 306 us                                                 | 296 us: 1.03x faster                                                |
| json_loads           | 26.5 us                                                | 26.0 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                               |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                               |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                               |
| tomli_loads          | 2.22 sec                                               | 2.33 sec: 1.05x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 57.8 ms: 1.07x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 83.9 ms: 1.10x slower                                               |
| pickle_list          | 4.11 us                                                | 4.59 us: 1.12x slower                                               |
| unpickle             | 13.7 us                                                | 15.4 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.36 ms: 1.10x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.84 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.31x faster                                                |
| generators               | 73.5 ms                                                | 27.9 ms: 2.63x faster                                               |
| asyncio_tcp              | 922 ms                                                 | 476 ms: 1.94x faster                                                |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                              |
| json_dumps               | 12.6 ms                                                | 9.76 ms: 1.29x faster                                               |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                                |
| coroutines               | 25.5 ms                                                | 21.9 ms: 1.16x faster                                               |
| chaos                    | 69.2 ms                                                | 59.5 ms: 1.16x faster                                               |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                               |
| deltablue                | 3.67 ms                                                | 3.31 ms: 1.11x faster                                               |
| comprehensions           | 22.4 us                                                | 20.3 us: 1.11x faster                                               |
| async_tree_io            | 1.30 sec                                               | 1.18 sec: 1.10x faster                                              |
| async_tree_none          | 526 ms                                                 | 483 ms: 1.09x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                               |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 582 ms: 1.08x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                |
| richards_super           | 56.8 ms                                                | 53.1 ms: 1.07x faster                                               |
| sqlglot_transpile        | 1.70 ms                                                | 1.61 ms: 1.06x faster                                               |
| coverage                 | 100 ms                                                 | 94.6 ms: 1.06x faster                                               |
| crypto_pyaes             | 74.7 ms                                                | 70.7 ms: 1.06x faster                                               |
| hexiom                   | 6.37 ms                                                | 6.09 ms: 1.05x faster                                               |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                |
| pickle_pure_python       | 306 us                                                 | 296 us: 1.03x faster                                                |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 720 ms: 1.03x faster                                                |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                              |
| sqlglot_normalize        | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| logging_format           | 6.68 us                                                | 6.54 us: 1.02x faster                                               |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                                |
| nqueens                  | 83.4 ms                                                | 81.9 ms: 1.02x faster                                               |
| json_loads               | 26.5 us                                                | 26.0 us: 1.02x faster                                               |
| scimark_lu               | 110 ms                                                 | 108 ms: 1.01x faster                                                |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.01x faster                                              |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                                |
| tornado_http             | 96.3 ms                                                | 95.2 ms: 1.01x faster                                               |
| logging_simple           | 6.03 us                                                | 5.97 us: 1.01x faster                                               |
| nbody                    | 93.1 ms                                                | 92.3 ms: 1.01x faster                                               |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| bench_thread_pool        | 819 us                                                 | 815 us: 1.01x faster                                                |
| sqlglot_optimize         | 53.1 ms                                                | 52.9 ms: 1.00x faster                                               |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.01x slower                                               |
| gc_traversal             | 4.02 ms                                                | 4.06 ms: 1.01x slower                                               |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                              |
| unpickle_list            | 4.91 us                                                | 4.97 us: 1.01x slower                                               |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                                |
| pidigits                 | 198 ms                                                 | 201 ms: 1.01x slower                                                |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                              |
| richards                 | 45.7 ms                                                | 46.4 ms: 1.02x slower                                               |
| fannkuch                 | 388 ms                                                 | 394 ms: 1.02x slower                                                |
| deepcopy_memo            | 37.0 us                                                | 37.9 us: 1.02x slower                                               |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.03x slower                                               |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                               |
| pprint_safe_repr         | 701 ms                                                 | 721 ms: 1.03x slower                                                |
| dulwich_log              | 63.7 ms                                                | 65.8 ms: 1.03x slower                                               |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                                |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                               |
| float                    | 77.2 ms                                                | 80.7 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.70 ms: 1.04x slower                                               |
| tomli_loads              | 2.22 sec                                               | 2.33 sec: 1.05x slower                                              |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                                |
| pyflate                  | 418 ms                                                 | 446 ms: 1.07x slower                                                |
| scimark_fft              | 328 ms                                                 | 352 ms: 1.07x slower                                                |
| xml_etree_process        | 53.9 ms                                                | 57.8 ms: 1.07x slower                                               |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                               |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.08x slower                                               |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.09x slower                                               |
| python_startup           | 8.52 ms                                                | 9.36 ms: 1.10x slower                                               |
| xml_etree_generate       | 76.2 ms                                                | 83.9 ms: 1.10x slower                                               |
| pickle_list              | 4.11 us                                                | 4.59 us: 1.12x slower                                               |
| unpickle                 | 13.7 us                                                | 15.4 us: 1.12x slower                                               |
| python_startup_no_site   | 6.01 ms                                                | 6.84 ms: 1.14x slower                                               |
| telco                    | 6.58 ms                                                | 7.79 ms: 1.18x slower                                               |
| unpack_sequence          | 43.1 ns                                                | 51.1 ns: 1.19x slower                                               |
| async_generators         | 368 ms                                                 | 451 ms: 1.22x slower                                                |
| dask                     | 360 ms                                                 | 517 ms: 1.44x slower                                                |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (5): scimark_monte_carlo, create_gc_cycles, bench_mp_pool, json, scimark_sor
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 76.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
