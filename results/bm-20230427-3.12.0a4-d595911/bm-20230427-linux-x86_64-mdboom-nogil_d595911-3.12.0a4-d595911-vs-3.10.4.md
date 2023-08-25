
# Results vs. 3.10.4

- fork: mdboom
- ref: nogil_d595911
- machine: linux-x86_64
- commit hash: d595911
- commit date: 2023-04-27
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 287 ms: 1.17x faster                                           |
| chameleon      | 9.06 ms                                                | 7.73 ms: 1.17x faster                                          |
| html5lib       | 85.9 ms                                                | 68.3 ms: 1.26x faster                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 111 ms                                                 | 67.0 ms: 1.65x faster                                          |
| nbody          | 142 ms                                                 | 103 ms: 1.37x faster                                           |
| pidigits       | 190 ms                                                 | 187 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.32x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 151 ms: 1.17x faster                                           |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                          |
| regex_dna      | 222 ms                                                 | 219 ms: 1.01x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.45x faster                                           |
| json_dumps           | 13.5 ms                                                | 10.5 ms: 1.29x faster                                          |
| unpickle_pure_python | 300 us                                                 | 237 us: 1.27x faster                                           |
| xml_etree_process    | 74.9 ms                                                | 60.5 ms: 1.24x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 133 ms: 1.22x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.39 sec: 1.22x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                          |
| pickle               | 10.3 us                                                | 9.82 us: 1.05x faster                                          |
| json_loads           | 28.8 us                                                | 28.1 us: 1.03x faster                                          |
| pickle_list          | 4.56 us                                                | 4.47 us: 1.02x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 121 ms: 1.08x slower                                           |
| unpickle             | 14.1 us                                                | 15.3 us: 1.08x slower                                          |
| pickle_dict          | 27.3 us                                                | 29.9 us: 1.10x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.35 us: 1.11x slower                                          |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.70 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text    | 30.3 ms                                                | 24.3 ms: 1.25x faster                                          |
| genshi_xml     | 63.3 ms                                                | 51.9 ms: 1.22x faster                                          |
| mako           | 14.8 ms                                                | 13.6 ms: 1.09x faster                                          |
| Geometric mean | (ref)                                                  | 1.18x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230427-linux-x86_64-mdboom-nogil_d595911-3.12.0a4-d595911 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 580 ms: 3.06x faster                                           |
| async_tree_none          | 717 ms                                                 | 289 ms: 2.48x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 362 ms: 2.36x faster                                           |
| deltablue                | 7.42 ms                                                | 3.67 ms: 2.02x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 514 ms: 1.85x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 535 ms: 1.73x faster                                           |
| float                    | 111 ms                                                 | 67.0 ms: 1.65x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.85 sec: 1.62x faster                                         |
| logging_silent           | 175 ns                                                 | 109 ns: 1.61x faster                                           |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.57x faster                                           |
| go                       | 229 ms                                                 | 147 ms: 1.56x faster                                           |
| richards                 | 74.9 ms                                                | 48.8 ms: 1.54x faster                                          |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| richards_super           | 90.7 ms                                                | 60.2 ms: 1.51x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 81.9 ms: 1.45x faster                                          |
| pickle_pure_python       | 455 us                                                 | 315 us: 1.45x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 76.1 ms: 1.42x faster                                          |
| pyflate                  | 673 ms                                                 | 475 ms: 1.42x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.85 ms: 1.39x faster                                          |
| chaos                    | 106 ms                                                 | 76.6 ms: 1.39x faster                                          |
| nbody                    | 142 ms                                                 | 103 ms: 1.37x faster                                           |
| raytrace                 | 464 ms                                                 | 346 ms: 1.34x faster                                           |
| spectral_norm            | 150 ms                                                 | 112 ms: 1.34x faster                                           |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.31x faster                                         |
| scimark_lu               | 163 ms                                                 | 125 ms: 1.31x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 40.1 us: 1.31x faster                                          |
| json_dumps               | 13.5 ms                                                | 10.5 ms: 1.29x faster                                          |
| coroutines               | 31.8 ms                                                | 25.1 ms: 1.27x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 237 us: 1.27x faster                                           |
| html5lib                 | 85.9 ms                                                | 68.3 ms: 1.26x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 51.8 ns: 1.25x faster                                          |
| genshi_text              | 30.3 ms                                                | 24.3 ms: 1.25x faster                                          |
| sqlglot_transpile        | 2.45 ms                                                | 1.97 ms: 1.24x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.60 sec: 1.24x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 60.5 ms: 1.24x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 772 ms: 1.24x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.11 ms: 1.24x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.67 ms: 1.23x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 133 ms: 1.22x faster                                           |
| tomli_loads              | 2.92 sec                                               | 2.39 sec: 1.22x faster                                         |
| genshi_xml               | 63.3 ms                                                | 51.9 ms: 1.22x faster                                          |
| sqlglot_normalize        | 135 ms                                                 | 114 ms: 1.19x faster                                           |
| deepcopy                 | 442 us                                                 | 373 us: 1.18x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 55.4 ms: 1.18x faster                                          |
| 2to3                     | 336 ms                                                 | 287 ms: 1.17x faster                                           |
| chameleon                | 9.06 ms                                                | 7.73 ms: 1.17x faster                                          |
| logging_simple           | 8.07 us                                                | 6.89 us: 1.17x faster                                          |
| regex_compile            | 177 ms                                                 | 151 ms: 1.17x faster                                           |
| nqueens                  | 100 ms                                                 | 86.4 ms: 1.16x faster                                          |
| async_generators         | 425 ms                                                 | 369 ms: 1.15x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.32 us: 1.15x faster                                          |
| logging_format           | 8.91 us                                                | 7.75 us: 1.15x faster                                          |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                          |
| scimark_fft              | 424 ms                                                 | 374 ms: 1.13x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                          |
| fannkuch                 | 486 ms                                                 | 433 ms: 1.12x faster                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.91 ms: 1.11x faster                                          |
| mako                     | 14.8 ms                                                | 13.6 ms: 1.09x faster                                          |
| json                     | 5.42 ms                                                | 5.05 ms: 1.07x faster                                          |
| sympy_integrate          | 24.3 ms                                                | 22.8 ms: 1.07x faster                                          |
| pickle                   | 10.3 us                                                | 9.82 us: 1.05x faster                                          |
| json_loads               | 28.8 us                                                | 28.1 us: 1.03x faster                                          |
| pathlib                  | 20.0 ms                                                | 19.5 ms: 1.02x faster                                          |
| sympy_expand             | 545 ms                                                 | 533 ms: 1.02x faster                                           |
| pickle_list              | 4.56 us                                                | 4.47 us: 1.02x faster                                          |
| pidigits                 | 190 ms                                                 | 187 ms: 1.02x faster                                           |
| regex_dna                | 222 ms                                                 | 219 ms: 1.01x faster                                           |
| generators               | 76.8 ms                                                | 78.3 ms: 1.02x slower                                          |
| sympy_sum                | 185 ms                                                 | 192 ms: 1.04x slower                                           |
| mypy2                    | 428 ms                                                 | 445 ms: 1.04x slower                                           |
| telco                    | 6.54 ms                                                | 6.81 ms: 1.04x slower                                          |
| mdp                      | 2.82 sec                                               | 2.94 sec: 1.04x slower                                         |
| typing_runtime_protocols | 510 us                                                 | 535 us: 1.05x slower                                           |
| xml_etree_iterparse      | 111 ms                                                 | 121 ms: 1.08x slower                                           |
| unpickle                 | 14.1 us                                                | 15.3 us: 1.08x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.52 ms: 1.09x slower                                          |
| pickle_dict              | 27.3 us                                                | 29.9 us: 1.10x slower                                          |
| meteor_contest           | 115 ms                                                 | 126 ms: 1.10x slower                                           |
| unpickle_list            | 4.82 us                                                | 5.35 us: 1.11x slower                                          |
| sqlite_synth             | 2.93 us                                                | 3.33 us: 1.13x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.70 ms: 1.15x slower                                          |
| bench_thread_pool        | 947 us                                                 | 1.64 ms: 1.73x slower                                          |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                   |

Benchmark hidden because not significant (3): comprehensions, sympy_str, bench_mp_pool
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, coverage, dask, django_template, djangocms, docutils, dulwich_log, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift, tornado_http


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
