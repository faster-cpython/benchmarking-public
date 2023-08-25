
# Results vs. 3.11.0

- fork: mdboom
- ref: nogil_d595911
- machine: linux-x86_64
- commit hash: d595911
- commit date: 2023-04-27
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 287 ms: 1.11x slower                                           |
| chameleon      | 6.47 ms                                                | 7.73 ms: 1.19x slower                                          |
| html5lib       | 64.5 ms                                                | 68.3 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.12x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 77.2 ms                                                | 67.0 ms: 1.15x faster                                          |
| pidigits       | 198 ms                                                 | 187 ms: 1.06x faster                                           |
| nbody          | 93.1 ms                                                | 103 ms: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                          |
| regex_dna      | 204 ms                                                 | 219 ms: 1.07x slower                                           |
| regex_compile  | 138 ms                                                 | 151 ms: 1.10x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.5 ms: 1.20x faster                                          |
| xml_etree_parse      | 158 ms                                                 | 133 ms: 1.19x faster                                           |
| pickle_dict          | 31.1 us                                                | 29.9 us: 1.04x faster                                          |
| pickle               | 10.1 us                                                | 9.82 us: 1.03x faster                                          |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                           |
| unpickle_pure_python | 228 us                                                 | 237 us: 1.04x slower                                           |
| json_loads           | 26.5 us                                                | 28.1 us: 1.06x slower                                          |
| tomli_loads          | 2.22 sec                                               | 2.39 sec: 1.08x slower                                         |
| pickle_list          | 4.11 us                                                | 4.47 us: 1.09x slower                                          |
| unpickle_list        | 4.91 us                                                | 5.35 us: 1.09x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                          |
| unpickle             | 13.7 us                                                | 15.3 us: 1.12x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 60.5 ms: 1.12x slower                                          |
| xml_etree_iterparse  | 104 ms                                                 | 121 ms: 1.16x slower                                           |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.70 ms: 1.11x slower                                          |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 21.6 ms                                                | 24.3 ms: 1.13x slower                                          |
| mako           | 10.1 ms                                                | 13.6 ms: 1.35x slower                                          |
| Geometric mean | (ref)                                                  | 1.15x slower                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io            | 1.30 sec                                               | 580 ms: 2.23x faster                                           |
| async_tree_none          | 526 ms                                                 | 289 ms: 1.82x faster                                           |
| async_tree_memoization   | 627 ms                                                 | 362 ms: 1.73x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 535 ms: 1.72x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.85 sec: 1.69x faster                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 514 ms: 1.44x faster                                           |
| gc_traversal             | 4.02 ms                                                | 3.11 ms: 1.29x faster                                          |
| json_dumps               | 12.6 ms                                                | 10.5 ms: 1.20x faster                                          |
| xml_etree_parse          | 158 ms                                                 | 133 ms: 1.19x faster                                           |
| float                    | 77.2 ms                                                | 67.0 ms: 1.15x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.52 ms: 1.14x faster                                          |
| pidigits                 | 198 ms                                                 | 187 ms: 1.06x faster                                           |
| pickle_dict              | 31.1 us                                                | 29.9 us: 1.04x faster                                          |
| pycparser                | 1.18 sec                                               | 1.14 sec: 1.03x faster                                         |
| pickle                   | 10.1 us                                                | 9.82 us: 1.03x faster                                          |
| coroutines               | 25.5 ms                                                | 25.1 ms: 1.02x faster                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                          |
| json                     | 4.94 ms                                                | 5.05 ms: 1.02x slower                                          |
| pickle_pure_python       | 306 us                                                 | 315 us: 1.03x slower                                           |
| telco                    | 6.58 ms                                                | 6.81 ms: 1.03x slower                                          |
| nqueens                  | 83.4 ms                                                | 86.4 ms: 1.04x slower                                          |
| unpickle_pure_python     | 228 us                                                 | 237 us: 1.04x slower                                           |
| sqlglot_optimize         | 53.1 ms                                                | 55.4 ms: 1.04x slower                                          |
| go                       | 140 ms                                                 | 147 ms: 1.05x slower                                           |
| sqlglot_normalize        | 108 ms                                                 | 114 ms: 1.05x slower                                           |
| html5lib                 | 64.5 ms                                                | 68.3 ms: 1.06x slower                                          |
| richards_super           | 56.8 ms                                                | 60.2 ms: 1.06x slower                                          |
| json_loads               | 26.5 us                                                | 28.1 us: 1.06x slower                                          |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.06x slower                                           |
| generators               | 73.5 ms                                                | 78.3 ms: 1.07x slower                                          |
| richards                 | 45.7 ms                                                | 48.8 ms: 1.07x slower                                          |
| pathlib                  | 18.2 ms                                                | 19.5 ms: 1.07x slower                                          |
| regex_dna                | 204 ms                                                 | 219 ms: 1.07x slower                                           |
| hexiom                   | 6.37 ms                                                | 6.85 ms: 1.07x slower                                          |
| logging_silent           | 101 ns                                                 | 109 ns: 1.08x slower                                           |
| tomli_loads              | 2.22 sec                                               | 2.39 sec: 1.08x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 40.1 us: 1.08x slower                                          |
| sympy_integrate          | 21.0 ms                                                | 22.8 ms: 1.08x slower                                          |
| pickle_list              | 4.11 us                                                | 4.47 us: 1.09x slower                                          |
| unpickle_list            | 4.91 us                                                | 5.35 us: 1.09x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.91 ms: 1.09x slower                                          |
| deepcopy                 | 342 us                                                 | 373 us: 1.09x slower                                           |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                          |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| regex_compile            | 138 ms                                                 | 151 ms: 1.10x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 81.9 ms: 1.10x slower                                          |
| pprint_pformat           | 1.46 sec                                               | 1.60 sec: 1.10x slower                                         |
| typing_runtime_protocols | 486 us                                                 | 535 us: 1.10x slower                                           |
| pprint_safe_repr         | 701 ms                                                 | 772 ms: 1.10x slower                                           |
| chaos                    | 69.2 ms                                                | 76.6 ms: 1.11x slower                                          |
| 2to3                     | 259 ms                                                 | 287 ms: 1.11x slower                                           |
| nbody                    | 93.1 ms                                                | 103 ms: 1.11x slower                                           |
| python_startup_no_site   | 6.01 ms                                                | 6.70 ms: 1.11x slower                                          |
| fannkuch                 | 388 ms                                                 | 433 ms: 1.12x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 76.1 ms: 1.12x slower                                          |
| unpickle                 | 13.7 us                                                | 15.3 us: 1.12x slower                                          |
| sympy_expand             | 475 ms                                                 | 533 ms: 1.12x slower                                           |
| spectral_norm            | 100 ms                                                 | 112 ms: 1.12x slower                                           |
| xml_etree_process        | 53.9 ms                                                | 60.5 ms: 1.12x slower                                          |
| mdp                      | 2.62 sec                                               | 2.94 sec: 1.12x slower                                         |
| genshi_text              | 21.6 ms                                                | 24.3 ms: 1.13x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.32 us: 1.13x slower                                          |
| sympy_str                | 290 ms                                                 | 329 ms: 1.13x slower                                           |
| pyflate                  | 418 ms                                                 | 475 ms: 1.14x slower                                           |
| scimark_lu               | 110 ms                                                 | 125 ms: 1.14x slower                                           |
| scimark_fft              | 328 ms                                                 | 374 ms: 1.14x slower                                           |
| logging_simple           | 6.03 us                                                | 6.89 us: 1.14x slower                                          |
| sympy_sum                | 167 ms                                                 | 192 ms: 1.15x slower                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.97 ms: 1.15x slower                                          |
| logging_format           | 6.68 us                                                | 7.75 us: 1.16x slower                                          |
| xml_etree_iterparse      | 104 ms                                                 | 121 ms: 1.16x slower                                           |
| raytrace                 | 297 ms                                                 | 346 ms: 1.17x slower                                           |
| meteor_contest           | 107 ms                                                 | 126 ms: 1.18x slower                                           |
| chameleon                | 6.47 ms                                                | 7.73 ms: 1.19x slower                                          |
| comprehensions           | 22.4 us                                                | 26.8 us: 1.19x slower                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.67 ms: 1.19x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 51.8 ns: 1.20x slower                                          |
| sqlite_synth             | 2.52 us                                                | 3.33 us: 1.32x slower                                          |
| mako                     | 10.1 ms                                                | 13.6 ms: 1.35x slower                                          |
| bench_thread_pool        | 819 us                                                 | 1.64 ms: 2.01x slower                                          |
| Geometric mean           | (ref)                                                  | 1.03x slower                                                   |

Benchmark hidden because not significant (6): deltablue, regex_v8, async_generators, bench_mp_pool, genshi_xml, mypy2
Ignored benchmarks (14) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, coverage, dask, django_template, djangocms, docutils, dulwich_log, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift, tornado_http


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x
