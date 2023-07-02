
# Results vs. 3.10.4

- fork: gvanrossum
- ref: tweak_uops
- machine: linux-x86_64
- commit hash: 5b85a49
- commit date: 2023-07-01
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                          |
| tornado_http   | 127 ms                                                 | 97.1 ms: 1.31x faster                                           |
| Geometric mean | (ref)                                                  | 1.24x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.8 ms: 1.48x faster                                           |
| float          | 111 ms                                                 | 82.6 ms: 1.34x faster                                           |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.24x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 141 ms: 1.26x faster                                            |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                           |
| regex_dna      | 222 ms                                                 | 217 ms: 1.02x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.85 ms: 1.19x slower                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.74 ms: 1.39x faster                                           |
| unpickle_pure_python | 300 us                                                 | 223 us: 1.35x faster                                            |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.26x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.52 sec: 1.16x faster                                          |
| json_loads           | 28.8 us                                                | 25.8 us: 1.12x faster                                           |
| xml_etree_generate   | 94.2 ms                                                | 85.5 ms: 1.10x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                            |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                            |
| pickle_list          | 4.56 us                                                | 4.59 us: 1.01x slower                                           |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                           |
| unpickle_list        | 4.82 us                                                | 5.06 us: 1.05x slower                                           |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                           |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                           |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.24 ms: 1.53x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 6.72 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-linux-x86_64-gvanrossum-tweak_uops-3.13.0a0-5b85a49 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.46x faster                                            |
| generators               | 76.8 ms                                                | 29.9 ms: 2.57x faster                                           |
| deltablue                | 7.42 ms                                                | 3.38 ms: 2.19x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                            |
| chaos                    | 106 ms                                                 | 60.9 ms: 1.75x faster                                           |
| logging_silent           | 175 ns                                                 | 103 ns: 1.69x faster                                            |
| raytrace                 | 464 ms                                                 | 274 ms: 1.69x faster                                            |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                          |
| richards_super           | 90.7 ms                                                | 54.3 ms: 1.67x faster                                           |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.63x faster                                            |
| go                       | 229 ms                                                 | 143 ms: 1.60x faster                                            |
| richards                 | 74.9 ms                                                | 48.4 ms: 1.55x faster                                           |
| python_startup           | 14.2 ms                                                | 9.24 ms: 1.53x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.36 ms: 1.51x faster                                           |
| pickle_pure_python       | 455 us                                                 | 305 us: 1.49x faster                                            |
| nbody                    | 142 ms                                                 | 95.8 ms: 1.48x faster                                           |
| async_tree_none          | 717 ms                                                 | 487 ms: 1.47x faster                                            |
| pyflate                  | 673 ms                                                 | 458 ms: 1.47x faster                                            |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.47x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 73.8 ms: 1.47x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.69 ms: 1.45x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.57 ms: 1.45x faster                                           |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                            |
| async_tree_memoization   | 854 ms                                                 | 596 ms: 1.43x faster                                            |
| coroutines               | 31.8 ms                                                | 22.4 ms: 1.42x faster                                           |
| json_dumps               | 13.5 ms                                                | 9.74 ms: 1.39x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 46.9 ns: 1.38x faster                                           |
| logging_format           | 8.91 us                                                | 6.54 us: 1.36x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 38.5 us: 1.36x faster                                           |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                           |
| logging_simple           | 8.07 us                                                | 5.99 us: 1.35x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 223 us: 1.35x faster                                            |
| spectral_norm            | 150 ms                                                 | 112 ms: 1.34x faster                                            |
| float                    | 111 ms                                                 | 82.6 ms: 1.34x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 726 ms: 1.32x faster                                            |
| tornado_http             | 127 ms                                                 | 97.1 ms: 1.31x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 726 ms: 1.31x faster                                            |
| comprehensions           | 26.8 us                                                | 21.1 us: 1.27x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.26x faster                                           |
| regex_compile            | 177 ms                                                 | 141 ms: 1.26x faster                                            |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.26x faster                                          |
| mypy2                    | 428 ms                                                 | 341 ms: 1.26x faster                                            |
| deepcopy                 | 442 us                                                 | 352 us: 1.25x faster                                            |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                            |
| nqueens                  | 100 ms                                                 | 83.0 ms: 1.20x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 54.9 ms: 1.19x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.25 us: 1.18x faster                                           |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                          |
| tomli_loads              | 2.92 sec                                               | 2.52 sec: 1.16x faster                                          |
| scimark_fft              | 424 ms                                                 | 370 ms: 1.15x faster                                            |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                           |
| bench_thread_pool        | 947 us                                                 | 835 us: 1.13x faster                                            |
| json_loads               | 28.8 us                                                | 25.8 us: 1.12x faster                                           |
| json                     | 5.42 ms                                                | 4.87 ms: 1.11x faster                                           |
| fannkuch                 | 486 ms                                                 | 437 ms: 1.11x faster                                            |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                           |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 85.5 ms: 1.10x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.11 ms: 1.07x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                            |
| pathlib                  | 20.0 ms                                                | 19.1 ms: 1.05x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                            |
| regex_dna                | 222 ms                                                 | 217 ms: 1.02x faster                                            |
| mdp                      | 2.82 sec                                               | 2.77 sec: 1.02x faster                                          |
| meteor_contest           | 115 ms                                                 | 113 ms: 1.02x faster                                            |
| pickle_list              | 4.56 us                                                | 4.59 us: 1.01x slower                                           |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                           |
| gc_traversal             | 3.84 ms                                                | 3.98 ms: 1.04x slower                                           |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                            |
| unpickle_list            | 4.82 us                                                | 5.06 us: 1.05x slower                                           |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                           |
| async_generators         | 425 ms                                                 | 466 ms: 1.10x slower                                            |
| telco                    | 6.54 ms                                                | 7.30 ms: 1.12x slower                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.72 ms: 1.15x slower                                           |
| pickle_dict              | 27.3 us                                                | 32.4 us: 1.19x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.85 ms: 1.19x slower                                           |
| dask                     | 423 ms                                                 | 527 ms: 1.25x slower                                            |
| coverage                 | 72.8 ms                                                | 92.2 ms: 1.27x slower                                           |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
