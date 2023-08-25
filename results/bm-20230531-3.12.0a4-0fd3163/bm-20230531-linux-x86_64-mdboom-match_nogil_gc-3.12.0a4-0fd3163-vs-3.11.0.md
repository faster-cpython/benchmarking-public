
# Results vs. 3.11.0

- fork: mdboom
- ref: match_nogil_gc
- machine: linux-x86_64
- commit hash: 0fd3163
- commit date: 2023-05-31
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                            |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                           |
| docutils       | 2.63 sec                                               | 2.15 sec: 1.22x faster                                          |
| html5lib       | 64.5 ms                                                | 57.8 ms: 1.12x faster                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 77.2 ms                                                | 60.7 ms: 1.27x faster                                           |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                            |
| nbody          | 93.1 ms                                                | 92.3 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.16x faster                                           |
| regex_compile  | 138 ms                                                 | 131 ms: 1.05x faster                                            |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.55 ms: 1.32x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 122 ms: 1.30x faster                                            |
| xml_etree_iterparse  | 104 ms                                                 | 80.9 ms: 1.28x faster                                           |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                            |
| tomli_loads          | 2.22 sec                                               | 1.98 sec: 1.12x faster                                          |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                           |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                            |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                           |
| xml_etree_process    | 53.9 ms                                                | 51.6 ms: 1.04x faster                                           |
| xml_etree_generate   | 76.2 ms                                                | 73.4 ms: 1.04x faster                                           |
| pickle_list          | 4.11 us                                                | 4.05 us: 1.02x faster                                           |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                           |
| unpickle_list        | 4.91 us                                                | 4.95 us: 1.01x slower                                           |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                           |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.24 ms: 1.04x faster                                           |
| python_startup_no_site | 6.01 ms                                                | 5.93 ms: 1.01x faster                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 45.9 ms: 1.13x faster                                           |
| genshi_text     | 21.6 ms                                                | 20.2 ms: 1.07x faster                                           |
| mako            | 10.1 ms                                                | 9.69 ms: 1.04x faster                                           |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230531-linux-x86_64-mdboom-match_nogil_gc-3.12.0a4-0fd3163 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io            | 1.30 sec                                               | 534 ms: 2.43x faster                                            |
| async_tree_none          | 526 ms                                                 | 260 ms: 2.02x faster                                            |
| async_tree_memoization   | 627 ms                                                 | 315 ms: 1.99x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                          |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 469 ms: 1.58x faster                                            |
| mypy2                    | 420 ms                                                 | 309 ms: 1.36x faster                                            |
| json_dumps               | 12.6 ms                                                | 9.55 ms: 1.32x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 122 ms: 1.30x faster                                            |
| xml_etree_iterparse      | 104 ms                                                 | 80.9 ms: 1.28x faster                                           |
| float                    | 77.2 ms                                                | 60.7 ms: 1.27x faster                                           |
| docutils                 | 2.63 sec                                               | 2.15 sec: 1.22x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.38 ms: 1.19x faster                                           |
| deltablue                | 3.67 ms                                                | 3.11 ms: 1.18x faster                                           |
| regex_effbot             | 3.99 ms                                                | 3.46 ms: 1.16x faster                                           |
| unpickle_pure_python     | 228 us                                                 | 198 us: 1.15x faster                                            |
| dask                     | 360 ms                                                 | 317 ms: 1.13x faster                                            |
| logging_silent           | 101 ns                                                 | 89.6 ns: 1.13x faster                                           |
| genshi_xml               | 51.8 ms                                                | 45.9 ms: 1.13x faster                                           |
| tomli_loads              | 2.22 sec                                               | 1.98 sec: 1.12x faster                                          |
| pycparser                | 1.18 sec                                               | 1.06 sec: 1.12x faster                                          |
| json_loads               | 26.5 us                                                | 23.7 us: 1.12x faster                                           |
| html5lib                 | 64.5 ms                                                | 57.8 ms: 1.12x faster                                           |
| scimark_sor              | 118 ms                                                 | 106 ms: 1.11x faster                                            |
| deepcopy_memo            | 37.0 us                                                | 33.8 us: 1.09x faster                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.12 ms: 1.09x faster                                           |
| async_generators         | 368 ms                                                 | 338 ms: 1.09x faster                                            |
| pickle_pure_python       | 306 us                                                 | 282 us: 1.08x faster                                            |
| json                     | 4.94 ms                                                | 4.59 ms: 1.08x faster                                           |
| richards                 | 45.7 ms                                                | 42.5 ms: 1.08x faster                                           |
| nqueens                  | 83.4 ms                                                | 77.6 ms: 1.07x faster                                           |
| richards_super           | 56.8 ms                                                | 52.9 ms: 1.07x faster                                           |
| genshi_text              | 21.6 ms                                                | 20.2 ms: 1.07x faster                                           |
| scimark_fft              | 328 ms                                                 | 309 ms: 1.06x faster                                            |
| 2to3                     | 259 ms                                                 | 245 ms: 1.06x faster                                            |
| spectral_norm            | 100 ms                                                 | 94.7 ms: 1.06x faster                                           |
| mdp                      | 2.62 sec                                               | 2.48 sec: 1.06x faster                                          |
| fannkuch                 | 388 ms                                                 | 368 ms: 1.05x faster                                            |
| hexiom                   | 6.37 ms                                                | 6.06 ms: 1.05x faster                                           |
| regex_compile            | 138 ms                                                 | 131 ms: 1.05x faster                                            |
| typing_runtime_protocols | 486 us                                                 | 463 us: 1.05x faster                                            |
| unpickle                 | 13.7 us                                                | 13.0 us: 1.05x faster                                           |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                            |
| sympy_expand             | 475 ms                                                 | 455 ms: 1.04x faster                                            |
| scimark_monte_carlo      | 68.1 ms                                                | 65.2 ms: 1.04x faster                                           |
| pprint_pformat           | 1.46 sec                                               | 1.39 sec: 1.04x faster                                          |
| xml_etree_process        | 53.9 ms                                                | 51.6 ms: 1.04x faster                                           |
| scimark_lu               | 110 ms                                                 | 105 ms: 1.04x faster                                            |
| mako                     | 10.1 ms                                                | 9.69 ms: 1.04x faster                                           |
| logging_simple           | 6.03 us                                                | 5.80 us: 1.04x faster                                           |
| xml_etree_generate       | 76.2 ms                                                | 73.4 ms: 1.04x faster                                           |
| sympy_integrate          | 21.0 ms                                                | 20.2 ms: 1.04x faster                                           |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                           |
| pyflate                  | 418 ms                                                 | 403 ms: 1.04x faster                                            |
| pprint_safe_repr         | 701 ms                                                 | 676 ms: 1.04x faster                                            |
| raytrace                 | 297 ms                                                 | 286 ms: 1.04x faster                                            |
| python_startup           | 8.52 ms                                                | 8.24 ms: 1.04x faster                                           |
| bench_thread_pool        | 819 us                                                 | 792 us: 1.03x faster                                            |
| sympy_str                | 290 ms                                                 | 281 ms: 1.03x faster                                            |
| deepcopy                 | 342 us                                                 | 332 us: 1.03x faster                                            |
| sqlglot_optimize         | 53.1 ms                                                | 51.6 ms: 1.03x faster                                           |
| sympy_sum                | 167 ms                                                 | 163 ms: 1.02x faster                                            |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                           |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                            |
| create_gc_cycles         | 1.49 ms                                                | 1.46 ms: 1.02x faster                                           |
| chameleon                | 6.47 ms                                                | 6.37 ms: 1.02x faster                                           |
| sqlglot_parse            | 1.40 ms                                                | 1.38 ms: 1.02x faster                                           |
| pickle_list              | 4.11 us                                                | 4.05 us: 1.02x faster                                           |
| python_startup_no_site   | 6.01 ms                                                | 5.93 ms: 1.01x faster                                           |
| crypto_pyaes             | 74.7 ms                                                | 73.7 ms: 1.01x faster                                           |
| telco                    | 6.58 ms                                                | 6.52 ms: 1.01x faster                                           |
| nbody                    | 93.1 ms                                                | 92.3 ms: 1.01x faster                                           |
| coverage                 | 100 ms                                                 | 99.2 ms: 1.01x faster                                           |
| chaos                    | 69.2 ms                                                | 68.8 ms: 1.01x faster                                           |
| pickle_dict              | 31.1 us                                                | 31.2 us: 1.00x slower                                           |
| unpickle_list            | 4.91 us                                                | 4.95 us: 1.01x slower                                           |
| django_template          | 32.6 ms                                                | 32.9 ms: 1.01x slower                                           |
| pickle                   | 10.1 us                                                | 10.2 us: 1.01x slower                                           |
| deepcopy_reduce          | 2.94 us                                                | 2.97 us: 1.01x slower                                           |
| unpack_sequence          | 43.1 ns                                                | 43.6 ns: 1.01x slower                                           |
| thrift                   | 756 us                                                 | 772 us: 1.02x slower                                            |
| coroutines               | 25.5 ms                                                | 26.1 ms: 1.02x slower                                           |
| meteor_contest           | 107 ms                                                 | 109 ms: 1.02x slower                                            |
| regex_dna                | 204 ms                                                 | 210 ms: 1.03x slower                                            |
| sqlite_synth             | 2.52 us                                                | 2.67 us: 1.06x slower                                           |
| comprehensions           | 22.4 us                                                | 23.9 us: 1.07x slower                                           |
| generators               | 73.5 ms                                                | 79.1 ms: 1.08x slower                                           |
| Geometric mean           | (ref)                                                  | 1.10x faster                                                    |

Benchmark hidden because not significant (6): pathlib, dulwich_log, bench_mp_pool, sqlglot_normalize, regex_v8, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
