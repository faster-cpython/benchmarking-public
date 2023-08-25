
# Results vs. 3.10.4

- fork: mdboom
- ref: bolt_experiment
- machine: linux-x86_64
- commit hash: b488f91
- commit date: 2023-05-05
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 270 ms: 1.24x faster                                              |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                            |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                              |
| Geometric mean | (ref)                                                  | 1.22x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.7 ms: 1.61x faster                                             |
| float          | 111 ms                                                 | 81.6 ms: 1.35x faster                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                             |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.81 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 323 us: 1.41x faster                                              |
| unpickle_pure_python | 300 us                                                 | 220 us: 1.37x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.92 ms: 1.36x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 59.7 ms: 1.25x faster                                             |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 85.3 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                              |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                             |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                             |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                             |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                             |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                      |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.14 ms: 1.55x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.7 ms: 2.50x faster                                             |
| deltablue               | 7.42 ms                                                | 3.56 ms: 2.08x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 510 ms: 1.81x faster                                              |
| logging_silent          | 175 ns                                                 | 104 ns: 1.68x faster                                              |
| richards                | 74.9 ms                                                | 44.6 ms: 1.68x faster                                             |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                              |
| nbody                   | 142 ms                                                 | 87.7 ms: 1.61x faster                                             |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.58x faster                                              |
| python_startup          | 14.2 ms                                                | 9.14 ms: 1.55x faster                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.53x faster                                             |
| chaos                   | 106 ms                                                 | 69.8 ms: 1.52x faster                                             |
| pyflate                 | 673 ms                                                 | 447 ms: 1.51x faster                                              |
| raytrace                | 464 ms                                                 | 310 ms: 1.50x faster                                              |
| hexiom                  | 9.53 ms                                                | 6.41 ms: 1.49x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 80.4 ms: 1.47x faster                                             |
| scimark_monte_carlo     | 108 ms                                                 | 73.6 ms: 1.47x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                             |
| async_tree_none         | 717 ms                                                 | 500 ms: 1.43x faster                                              |
| coroutines              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                             |
| async_tree_io           | 1.77 sec                                               | 1.24 sec: 1.43x faster                                            |
| pickle_pure_python      | 455 us                                                 | 323 us: 1.41x faster                                              |
| scimark_lu              | 163 ms                                                 | 116 ms: 1.40x faster                                              |
| unpack_sequence         | 64.7 ns                                                | 46.6 ns: 1.39x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 617 ms: 1.39x faster                                              |
| unpickle_pure_python    | 300 us                                                 | 220 us: 1.37x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 38.3 us: 1.37x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.92 ms: 1.36x faster                                             |
| spectral_norm           | 150 ms                                                 | 111 ms: 1.36x faster                                              |
| float                   | 111 ms                                                 | 81.6 ms: 1.35x faster                                             |
| mako                    | 14.8 ms                                                | 10.9 ms: 1.35x faster                                             |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 723 ms: 1.32x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.53 sec: 1.30x faster                                            |
| fannkuch                | 486 ms                                                 | 375 ms: 1.29x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 750 ms: 1.27x faster                                              |
| xml_etree_process       | 74.9 ms                                                | 59.7 ms: 1.25x faster                                             |
| logging_format          | 8.91 us                                                | 7.12 us: 1.25x faster                                             |
| tornado_http            | 127 ms                                                 | 102 ms: 1.25x faster                                              |
| logging_simple          | 8.07 us                                                | 6.47 us: 1.25x faster                                             |
| 2to3                    | 336 ms                                                 | 270 ms: 1.24x faster                                              |
| nqueens                 | 100 ms                                                 | 82.1 ms: 1.22x faster                                             |
| deepcopy                | 442 us                                                 | 363 us: 1.22x faster                                              |
| mypy2                   | 428 ms                                                 | 353 ms: 1.21x faster                                              |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.19 us: 1.20x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 113 ms: 1.19x faster                                              |
| scimark_fft             | 424 ms                                                 | 355 ms: 1.19x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 55.6 ms: 1.17x faster                                             |
| docutils                | 3.17 sec                                               | 2.73 sec: 1.16x faster                                            |
| comprehensions          | 26.8 us                                                | 23.3 us: 1.15x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.80 ms: 1.14x faster                                             |
| bench_thread_pool       | 947 us                                                 | 837 us: 1.13x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                             |
| json_loads              | 28.8 us                                                | 25.7 us: 1.12x faster                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.12x faster                                              |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                             |
| xml_etree_generate      | 94.2 ms                                                | 85.3 ms: 1.10x faster                                             |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.3 ms: 1.10x faster                                             |
| json                    | 5.42 ms                                                | 4.94 ms: 1.10x faster                                             |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                              |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                            |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.8 ms: 1.07x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.79 us: 1.05x faster                                             |
| gc_traversal            | 3.84 ms                                                | 3.68 ms: 1.04x faster                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                              |
| unpickle_list           | 4.82 us                                                | 4.88 us: 1.01x slower                                             |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                             |
| telco                   | 6.54 ms                                                | 6.82 ms: 1.04x slower                                             |
| unpickle                | 14.1 us                                                | 15.0 us: 1.06x slower                                             |
| async_generators        | 425 ms                                                 | 459 ms: 1.08x slower                                              |
| python_startup_no_site  | 5.82 ms                                                | 6.67 ms: 1.15x slower                                             |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.81 ms: 1.18x slower                                             |
| dask                    | 423 ms                                                 | 542 ms: 1.28x slower                                              |
| coverage                | 72.8 ms                                                | 103 ms: 1.42x slower                                              |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
