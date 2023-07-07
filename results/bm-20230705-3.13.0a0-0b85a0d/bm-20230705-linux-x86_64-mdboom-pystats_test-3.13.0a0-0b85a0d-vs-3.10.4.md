
# Results vs. 3.10.4

- fork: mdboom
- ref: pystats_test
- machine: linux-x86_64
- commit hash: 0b85a0d
- commit date: 2023-07-05
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                        |
| tornado_http   | 127 ms                                                 | 96.7 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                  | 1.25x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.9 ms: 1.58x faster                                         |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                         |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                          |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                         |
| regex_dna      | 222 ms                                                 | 208 ms: 1.06x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 307 us: 1.49x faster                                          |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 58.3 ms: 1.28x faster                                         |
| tomli_loads          | 2.92 sec                                               | 2.34 sec: 1.25x faster                                        |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                          |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                         |
| unpickle             | 14.1 us                                                | 14.8 us: 1.04x slower                                         |
| pickle               | 10.3 us                                                | 10.8 us: 1.04x slower                                         |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                         |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.19 ms: 1.54x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                         |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230705-linux-x86_64-mdboom-pystats_test-3.13.0a0-0b85a0d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                          |
| generators               | 76.8 ms                                                | 29.1 ms: 2.64x faster                                         |
| deltablue                | 7.42 ms                                                | 3.27 ms: 2.27x faster                                         |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                          |
| chaos                    | 106 ms                                                 | 59.6 ms: 1.78x faster                                         |
| raytrace                 | 464 ms                                                 | 269 ms: 1.73x faster                                          |
| richards_super           | 90.7 ms                                                | 53.3 ms: 1.70x faster                                         |
| logging_silent           | 175 ns                                                 | 103 ns: 1.69x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                        |
| go                       | 229 ms                                                 | 138 ms: 1.67x faster                                          |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                          |
| richards                 | 74.9 ms                                                | 46.6 ms: 1.61x faster                                         |
| nbody                    | 142 ms                                                 | 89.9 ms: 1.58x faster                                         |
| hexiom                   | 9.53 ms                                                | 6.12 ms: 1.56x faster                                         |
| python_startup           | 14.2 ms                                                | 9.19 ms: 1.54x faster                                         |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                         |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 78.6 ms: 1.51x faster                                         |
| async_tree_none          | 717 ms                                                 | 482 ms: 1.49x faster                                          |
| pickle_pure_python       | 455 us                                                 | 307 us: 1.49x faster                                          |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                         |
| scimark_monte_carlo      | 108 ms                                                 | 73.5 ms: 1.47x faster                                         |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                          |
| async_tree_memoization   | 854 ms                                                 | 589 ms: 1.45x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 45.3 ns: 1.43x faster                                         |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                          |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                         |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                         |
| float                    | 111 ms                                                 | 79.7 ms: 1.39x faster                                         |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                         |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                         |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                         |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                        |
| logging_simple           | 8.07 us                                                | 5.96 us: 1.35x faster                                         |
| spectral_norm            | 150 ms                                                 | 112 ms: 1.34x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                          |
| tornado_http             | 127 ms                                                 | 96.7 ms: 1.32x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 724 ms: 1.31x faster                                          |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                         |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                        |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 58.3 ms: 1.28x faster                                         |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                          |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                          |
| deepcopy                 | 442 us                                                 | 350 us: 1.26x faster                                          |
| nqueens                  | 100 ms                                                 | 79.8 ms: 1.25x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.34 sec: 1.25x faster                                        |
| sqlglot_optimize         | 65.3 ms                                                | 53.2 ms: 1.23x faster                                         |
| fannkuch                 | 486 ms                                                 | 399 ms: 1.22x faster                                          |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.63 ms: 1.18x faster                                         |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                          |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                          |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                         |
| regex_v8                 | 25.0 ms                                                | 22.2 ms: 1.13x faster                                         |
| mdp                      | 2.82 sec                                               | 2.51 sec: 1.12x faster                                        |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                         |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                         |
| json                     | 5.42 ms                                                | 4.88 ms: 1.11x faster                                         |
| xml_etree_generate       | 94.2 ms                                                | 84.9 ms: 1.11x faster                                         |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.11x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                          |
| regex_dna                | 222 ms                                                 | 208 ms: 1.06x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.06x faster                                         |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.05x faster                                         |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                         |
| unpickle_list            | 4.82 us                                                | 4.93 us: 1.02x slower                                         |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                          |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.04x slower                                         |
| pickle                   | 10.3 us                                                | 10.8 us: 1.04x slower                                         |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                         |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.44 ms: 1.07x slower                                         |
| telco                    | 6.54 ms                                                | 7.22 ms: 1.10x slower                                         |
| pickle_dict              | 27.3 us                                                | 31.0 us: 1.14x slower                                         |
| python_startup_no_site   | 5.82 ms                                                | 6.68 ms: 1.15x slower                                         |
| dask                     | 423 ms                                                 | 524 ms: 1.24x slower                                          |
| coverage                 | 72.8 ms                                                | 91.8 ms: 1.26x slower                                         |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                  |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
