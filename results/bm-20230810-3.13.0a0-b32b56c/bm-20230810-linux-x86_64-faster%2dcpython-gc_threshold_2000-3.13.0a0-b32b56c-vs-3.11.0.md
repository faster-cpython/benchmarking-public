
# Results vs. 3.11.0

- fork: faster-cpython
- ref: gc_threshold_2000
- machine: linux-x86_64
- commit hash: b32b56c
- commit date: 2023-08-10
- overall geometric mean: 1.06x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                       |
| tornado_http   | 96.3 ms                                                | 92.4 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| nbody          | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                        |
| float          | 77.2 ms                                                | 78.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.72 ms: 1.07x faster                                                        |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                         |
| regex_v8       | 22.0 ms                                                | 23.6 ms: 1.07x slower                                                        |
| regex_dna      | 204 ms                                                 | 220 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                                         |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 104 ms                                                 | 98.8 ms: 1.05x faster                                                        |
| tomli_loads          | 2.22 sec                                               | 2.12 sec: 1.05x faster                                                       |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                                        |
| pickle_pure_python   | 306 us                                                 | 299 us: 1.02x faster                                                         |
| unpickle_list        | 4.91 us                                                | 4.85 us: 1.01x faster                                                        |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                                        |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                        |
| xml_etree_process    | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| xml_etree_generate   | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                        |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                        |
| pickle_list          | 4.11 us                                                | 4.66 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 6.76 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 147 us: 3.30x faster                                                         |
| generators               | 73.5 ms                                                | 28.3 ms: 2.60x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 484 ms: 1.90x faster                                                         |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                                       |
| async_tree_io            | 1.30 sec                                               | 853 ms: 1.52x faster                                                         |
| async_tree_none          | 526 ms                                                 | 355 ms: 1.48x faster                                                         |
| async_tree_memoization   | 627 ms                                                 | 447 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 570 ms: 1.30x faster                                                         |
| json_dumps               | 12.6 ms                                                | 9.79 ms: 1.29x faster                                                        |
| mypy2                    | 420 ms                                                 | 337 ms: 1.25x faster                                                         |
| coverage                 | 100 ms                                                 | 85.3 ms: 1.17x faster                                                        |
| chaos                    | 69.2 ms                                                | 59.8 ms: 1.16x faster                                                        |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                        |
| sqlglot_parse            | 1.40 ms                                                | 1.26 ms: 1.11x faster                                                        |
| deltablue                | 3.67 ms                                                | 3.33 ms: 1.10x faster                                                        |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                                        |
| crypto_pyaes             | 74.7 ms                                                | 68.5 ms: 1.09x faster                                                        |
| raytrace                 | 297 ms                                                 | 273 ms: 1.09x faster                                                         |
| sqlglot_transpile        | 1.70 ms                                                | 1.57 ms: 1.08x faster                                                        |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                                         |
| regex_effbot             | 3.99 ms                                                | 3.72 ms: 1.07x faster                                                        |
| nqueens                  | 83.4 ms                                                | 78.5 ms: 1.06x faster                                                        |
| hexiom                   | 6.37 ms                                                | 6.00 ms: 1.06x faster                                                        |
| richards_super           | 56.8 ms                                                | 53.5 ms: 1.06x faster                                                        |
| gc_traversal             | 4.02 ms                                                | 3.80 ms: 1.06x faster                                                        |
| xml_etree_parse          | 158 ms                                                 | 150 ms: 1.06x faster                                                         |
| xml_etree_iterparse      | 104 ms                                                 | 98.8 ms: 1.05x faster                                                        |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                         |
| tomli_loads              | 2.22 sec                                               | 2.12 sec: 1.05x faster                                                       |
| tornado_http             | 96.3 ms                                                | 92.4 ms: 1.04x faster                                                        |
| nbody                    | 93.1 ms                                                | 89.8 ms: 1.04x faster                                                        |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                                        |
| sqlglot_normalize        | 108 ms                                                 | 104 ms: 1.03x faster                                                         |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                        |
| logging_format           | 6.68 us                                                | 6.53 us: 1.02x faster                                                        |
| docutils                 | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                       |
| pickle_pure_python       | 306 us                                                 | 299 us: 1.02x faster                                                         |
| regex_compile            | 138 ms                                                 | 135 ms: 1.02x faster                                                         |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                        |
| scimark_monte_carlo      | 68.1 ms                                                | 67.2 ms: 1.01x faster                                                        |
| unpickle_list            | 4.91 us                                                | 4.85 us: 1.01x faster                                                        |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                                         |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                                                       |
| sqlglot_optimize         | 53.1 ms                                                | 52.8 ms: 1.01x faster                                                        |
| float                    | 77.2 ms                                                | 78.3 ms: 1.01x slower                                                        |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                       |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                                        |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                                        |
| mdp                      | 2.62 sec                                               | 2.68 sec: 1.03x slower                                                       |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.03x slower                                                        |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.03x slower                                                         |
| deepcopy                 | 342 us                                                 | 352 us: 1.03x slower                                                         |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.63 ms: 1.03x slower                                                        |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                                        |
| mako                     | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                        |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                        |
| pprint_safe_repr         | 701 ms                                                 | 730 ms: 1.04x slower                                                         |
| richards                 | 45.7 ms                                                | 47.7 ms: 1.04x slower                                                        |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.04x slower                                                         |
| dulwich_log              | 63.7 ms                                                | 66.6 ms: 1.05x slower                                                        |
| logging_silent           | 101 ns                                                 | 106 ns: 1.05x slower                                                         |
| xml_etree_process        | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                        |
| pyflate                  | 418 ms                                                 | 445 ms: 1.06x slower                                                         |
| xml_etree_generate       | 76.2 ms                                                | 81.2 ms: 1.07x slower                                                        |
| regex_v8                 | 22.0 ms                                                | 23.6 ms: 1.07x slower                                                        |
| scimark_fft              | 328 ms                                                 | 353 ms: 1.07x slower                                                         |
| regex_dna                | 204 ms                                                 | 220 ms: 1.08x slower                                                         |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                                        |
| python_startup           | 8.52 ms                                                | 9.27 ms: 1.09x slower                                                        |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                        |
| sqlite_synth             | 2.52 us                                                | 2.78 us: 1.10x slower                                                        |
| unpack_sequence          | 43.1 ns                                                | 48.0 ns: 1.11x slower                                                        |
| python_startup_no_site   | 6.01 ms                                                | 6.76 ms: 1.13x slower                                                        |
| pickle_list              | 4.11 us                                                | 4.66 us: 1.13x slower                                                        |
| async_generators         | 368 ms                                                 | 441 ms: 1.20x slower                                                         |
| telco                    | 6.58 ms                                                | 7.93 ms: 1.20x slower                                                        |
| dask                     | 360 ms                                                 | 498 ms: 1.38x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (5): scimark_lu, bench_thread_pool, bench_mp_pool, go, fannkuch
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
