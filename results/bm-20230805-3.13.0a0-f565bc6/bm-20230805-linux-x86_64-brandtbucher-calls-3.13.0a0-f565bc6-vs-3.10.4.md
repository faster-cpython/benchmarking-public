
# Results vs. 3.10.4

- fork: brandtbucher
- ref: calls
- machine: linux-x86_64
- commit hash: f565bc6
- commit date: 2023-08-05
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                       |
| tornado_http   | 127 ms                                                 | 95.9 ms: 1.33x faster                                        |
| Geometric mean | (ref)                                                  | 1.26x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.2 ms: 1.61x faster                                        |
| float          | 111 ms                                                 | 79.6 ms: 1.39x faster                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                         |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                        |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                         |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                         |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                         |
| json_dumps           | 13.5 ms                                                | 9.92 ms: 1.36x faster                                        |
| xml_etree_process    | 74.9 ms                                                | 57.1 ms: 1.31x faster                                        |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.26x faster                                       |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                        |
| xml_etree_generate   | 94.2 ms                                                | 83.5 ms: 1.13x faster                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                         |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                        |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                        |
| pickle_list          | 4.56 us                                                | 4.72 us: 1.03x slower                                        |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                        |
| pickle_dict          | 27.3 us                                                | 33.4 us: 1.23x slower                                        |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.37 ms: 1.51x faster                                        |
| python_startup_no_site | 5.82 ms                                                | 6.85 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-calls-3.13.0a0-f565bc6 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.57x faster                                         |
| generators               | 76.8 ms                                                | 30.2 ms: 2.54x faster                                        |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                        |
| asyncio_tcp              | 925 ms                                                 | 487 ms: 1.90x faster                                         |
| chaos                    | 106 ms                                                 | 60.0 ms: 1.77x faster                                        |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                         |
| raytrace                 | 464 ms                                                 | 272 ms: 1.71x faster                                         |
| crypto_pyaes             | 118 ms                                                 | 69.9 ms: 1.69x faster                                        |
| richards_super           | 90.7 ms                                                | 53.6 ms: 1.69x faster                                        |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                       |
| go                       | 229 ms                                                 | 140 ms: 1.63x faster                                         |
| unpack_sequence          | 64.7 ns                                                | 40.0 ns: 1.62x faster                                        |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                         |
| nbody                    | 142 ms                                                 | 88.2 ms: 1.61x faster                                        |
| richards                 | 74.9 ms                                                | 47.0 ms: 1.59x faster                                        |
| scimark_monte_carlo      | 108 ms                                                 | 68.0 ms: 1.59x faster                                        |
| hexiom                   | 9.53 ms                                                | 6.04 ms: 1.58x faster                                        |
| sqlglot_parse            | 2.06 ms                                                | 1.31 ms: 1.57x faster                                        |
| pyflate                  | 673 ms                                                 | 441 ms: 1.53x faster                                         |
| python_startup           | 14.2 ms                                                | 9.37 ms: 1.51x faster                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.63 ms: 1.51x faster                                        |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.50x faster                                       |
| async_tree_none          | 717 ms                                                 | 479 ms: 1.50x faster                                         |
| pickle_pure_python       | 455 us                                                 | 305 us: 1.49x faster                                         |
| coroutines               | 31.8 ms                                                | 21.7 ms: 1.46x faster                                        |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.45x faster                                         |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.45x faster                                         |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                         |
| float                    | 111 ms                                                 | 79.6 ms: 1.39x faster                                        |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                         |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                        |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.38x faster                                        |
| json_dumps               | 13.5 ms                                                | 9.92 ms: 1.36x faster                                        |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                       |
| comprehensions           | 26.8 us                                                | 20.1 us: 1.33x faster                                        |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                         |
| tornado_http             | 127 ms                                                 | 95.9 ms: 1.33x faster                                        |
| logging_simple           | 8.07 us                                                | 6.10 us: 1.32x faster                                        |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 721 ms: 1.32x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 57.1 ms: 1.31x faster                                        |
| logging_format           | 8.91 us                                                | 6.79 us: 1.31x faster                                        |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                         |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                         |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                       |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                         |
| nqueens                  | 100 ms                                                 | 78.8 ms: 1.27x faster                                        |
| deepcopy                 | 442 us                                                 | 350 us: 1.26x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.26x faster                                       |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                        |
| fannkuch                 | 486 ms                                                 | 396 ms: 1.23x faster                                         |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                        |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                       |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                         |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.74 ms: 1.15x faster                                        |
| dulwich_log              | 75.9 ms                                                | 66.1 ms: 1.15x faster                                        |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                        |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                        |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                        |
| xml_etree_generate       | 94.2 ms                                                | 83.5 ms: 1.13x faster                                        |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                        |
| mdp                      | 2.82 sec                                               | 2.52 sec: 1.12x faster                                       |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                         |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.08x faster                                         |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                         |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                        |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                        |
| regex_dna                | 222 ms                                                 | 212 ms: 1.05x faster                                         |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                         |
| gc_traversal             | 3.84 ms                                                | 3.84 ms: 1.00x faster                                        |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                        |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                        |
| pickle_list              | 4.56 us                                                | 4.72 us: 1.03x slower                                        |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                        |
| async_generators         | 425 ms                                                 | 452 ms: 1.06x slower                                         |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                        |
| python_startup_no_site   | 5.82 ms                                                | 6.85 ms: 1.18x slower                                        |
| telco                    | 6.54 ms                                                | 7.82 ms: 1.20x slower                                        |
| pickle_dict              | 27.3 us                                                | 33.4 us: 1.23x slower                                        |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                         |
| coverage                 | 72.8 ms                                                | 93.9 ms: 1.29x slower                                        |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
