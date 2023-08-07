
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.75 sec: 1.15x faster                                        |
| tornado_http   | 127 ms                                                 | 97.3 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 102 ms: 1.39x faster                                          |
| float          | 111 ms                                                 | 84.4 ms: 1.31x faster                                         |
| pidigits       | 190 ms                                                 | 200 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 150 ms: 1.18x faster                                          |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                         |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.39 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.89 ms: 1.37x faster                                         |
| unpickle_pure_python | 300 us                                                 | 222 us: 1.36x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                         |
| json_loads           | 28.8 us                                                | 25.4 us: 1.14x faster                                         |
| tomli_loads          | 2.92 sec                                               | 2.58 sec: 1.13x faster                                        |
| xml_etree_generate   | 94.2 ms                                                | 86.1 ms: 1.09x faster                                         |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                          |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                         |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                         |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                         |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                         |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.39 ms: 1.51x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                         |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.1 ms: 1.22x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 152 us: 3.35x faster                                          |
| generators               | 76.8 ms                                                | 29.1 ms: 2.63x faster                                         |
| deltablue                | 7.42 ms                                                | 3.42 ms: 2.17x faster                                         |
| asyncio_tcp              | 925 ms                                                 | 490 ms: 1.89x faster                                          |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                        |
| raytrace                 | 464 ms                                                 | 280 ms: 1.66x faster                                          |
| richards_super           | 90.7 ms                                                | 55.9 ms: 1.62x faster                                         |
| chaos                    | 106 ms                                                 | 65.5 ms: 1.62x faster                                         |
| crypto_pyaes             | 118 ms                                                 | 73.8 ms: 1.61x faster                                         |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.58x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 68.9 ms: 1.57x faster                                         |
| go                       | 229 ms                                                 | 147 ms: 1.56x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                         |
| richards                 | 74.9 ms                                                | 48.7 ms: 1.54x faster                                         |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                          |
| python_startup           | 14.2 ms                                                | 9.39 ms: 1.51x faster                                         |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                         |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                        |
| async_tree_none          | 717 ms                                                 | 493 ms: 1.45x faster                                          |
| async_tree_memoization   | 854 ms                                                 | 594 ms: 1.44x faster                                          |
| coroutines               | 31.8 ms                                                | 22.4 ms: 1.42x faster                                         |
| nbody                    | 142 ms                                                 | 102 ms: 1.39x faster                                          |
| pyflate                  | 673 ms                                                 | 485 ms: 1.39x faster                                          |
| scimark_lu               | 163 ms                                                 | 118 ms: 1.39x faster                                          |
| spectral_norm            | 150 ms                                                 | 109 ms: 1.38x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.89 ms: 1.37x faster                                         |
| logging_format           | 8.91 us                                                | 6.56 us: 1.36x faster                                         |
| unpickle_pure_python     | 300 us                                                 | 222 us: 1.36x faster                                          |
| logging_simple           | 8.07 us                                                | 6.01 us: 1.34x faster                                         |
| tornado_http             | 127 ms                                                 | 97.3 ms: 1.31x faster                                         |
| float                    | 111 ms                                                 | 84.4 ms: 1.31x faster                                         |
| pprint_pformat           | 1.99 sec                                               | 1.52 sec: 1.31x faster                                        |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 732 ms: 1.30x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 49.8 ns: 1.30x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 741 ms: 1.29x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 59.0 ms: 1.27x faster                                         |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                        |
| hexiom                   | 9.53 ms                                                | 7.61 ms: 1.25x faster                                         |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 41.9 us: 1.25x faster                                         |
| mypy2                    | 428 ms                                                 | 350 ms: 1.22x faster                                          |
| mako                     | 14.8 ms                                                | 12.1 ms: 1.22x faster                                         |
| deepcopy                 | 442 us                                                 | 362 us: 1.22x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 54.6 ms: 1.20x faster                                         |
| deepcopy_reduce          | 3.82 us                                                | 3.20 us: 1.19x faster                                         |
| regex_compile            | 177 ms                                                 | 150 ms: 1.18x faster                                          |
| docutils                 | 3.17 sec                                               | 2.75 sec: 1.15x faster                                        |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                         |
| json_loads               | 28.8 us                                                | 25.4 us: 1.14x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.58 sec: 1.13x faster                                        |
| dulwich_log              | 75.9 ms                                                | 67.2 ms: 1.13x faster                                         |
| json                     | 5.42 ms                                                | 4.86 ms: 1.12x faster                                         |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                         |
| regex_dna                | 222 ms                                                 | 200 ms: 1.11x faster                                          |
| scimark_fft              | 424 ms                                                 | 385 ms: 1.10x faster                                          |
| bench_thread_pool        | 947 us                                                 | 864 us: 1.10x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 86.1 ms: 1.09x faster                                         |
| comprehensions           | 26.8 us                                                | 25.0 us: 1.07x faster                                         |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                          |
| pathlib                  | 20.0 ms                                                | 19.1 ms: 1.05x faster                                         |
| sqlite_synth             | 2.93 us                                                | 2.80 us: 1.05x faster                                         |
| fannkuch                 | 486 ms                                                 | 468 ms: 1.04x faster                                          |
| nqueens                  | 100 ms                                                 | 98.9 ms: 1.01x faster                                         |
| mdp                      | 2.82 sec                                               | 2.83 sec: 1.00x slower                                        |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                         |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                         |
| gc_traversal             | 3.84 ms                                                | 3.99 ms: 1.04x slower                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.70 ms: 1.05x slower                                         |
| regex_effbot             | 3.23 ms                                                | 3.39 ms: 1.05x slower                                         |
| pidigits                 | 190 ms                                                 | 200 ms: 1.06x slower                                          |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                         |
| async_generators         | 425 ms                                                 | 466 ms: 1.10x slower                                          |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                         |
| python_startup_no_site   | 5.82 ms                                                | 6.88 ms: 1.18x slower                                         |
| telco                    | 6.54 ms                                                | 8.05 ms: 1.23x slower                                         |
| dask                     | 423 ms                                                 | 532 ms: 1.26x slower                                          |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                         |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                  |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, meteor_contest
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
