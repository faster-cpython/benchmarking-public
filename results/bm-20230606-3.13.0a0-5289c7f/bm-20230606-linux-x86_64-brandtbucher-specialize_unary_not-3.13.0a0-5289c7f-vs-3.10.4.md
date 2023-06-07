
# Results vs. 3.10.4

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 5289c7f
- commit date: 2023-06-06
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.75 sec: 1.15x faster                                                      |
| tornado_http   | 127 ms                                                 | 103 ms: 1.23x faster                                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.2 ms: 1.54x faster                                                       |
| float          | 111 ms                                                 | 83.0 ms: 1.33x faster                                                       |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.22x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                       |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 320 us: 1.42x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.96 ms: 1.36x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 224 us: 1.34x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.26 sec: 1.29x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                       |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 85.3 ms: 1.10x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.45 us: 1.02x faster                                                       |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                       |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.36 ms: 1.51x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.81 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-5289c7f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                                        |
| generators               | 76.8 ms                                                | 30.1 ms: 2.55x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.61 ms: 2.05x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                                        |
| richards_super           | 90.7 ms                                                | 51.2 ms: 1.77x faster                                                       |
| logging_silent           | 175 ns                                                 | 104 ns: 1.68x faster                                                        |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                      |
| richards                 | 74.9 ms                                                | 45.3 ms: 1.65x faster                                                       |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                                        |
| chaos                    | 106 ms                                                 | 66.1 ms: 1.61x faster                                                       |
| nbody                    | 142 ms                                                 | 92.2 ms: 1.54x faster                                                       |
| raytrace                 | 464 ms                                                 | 305 ms: 1.52x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.36 ms: 1.51x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.36 ms: 1.50x faster                                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.38 ms: 1.49x faster                                                       |
| crypto_pyaes             | 118 ms                                                 | 79.4 ms: 1.49x faster                                                       |
| pyflate                  | 673 ms                                                 | 463 ms: 1.45x faster                                                        |
| scimark_monte_carlo      | 108 ms                                                 | 74.9 ms: 1.45x faster                                                       |
| sqlglot_transpile        | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                       |
| async_tree_none          | 717 ms                                                 | 501 ms: 1.43x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.24 sec: 1.43x faster                                                      |
| pickle_pure_python       | 455 us                                                 | 320 us: 1.42x faster                                                        |
| scimark_lu               | 163 ms                                                 | 115 ms: 1.42x faster                                                        |
| scimark_sor              | 197 ms                                                 | 139 ms: 1.41x faster                                                        |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 609 ms: 1.40x faster                                                        |
| coroutines               | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                       |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |
| deepcopy_memo            | 52.3 us                                                | 38.4 us: 1.36x faster                                                       |
| json_dumps               | 13.5 ms                                                | 9.96 ms: 1.36x faster                                                       |
| unpickle_pure_python     | 300 us                                                 | 224 us: 1.34x faster                                                        |
| float                    | 111 ms                                                 | 83.0 ms: 1.33x faster                                                       |
| tomli_loads              | 2.92 sec                                               | 2.26 sec: 1.29x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.55 sec: 1.28x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 744 ms: 1.28x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 762 ms: 1.25x faster                                                        |
| pycparser                | 1.50 sec                                               | 1.22 sec: 1.24x faster                                                      |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                        |
| tornado_http             | 127 ms                                                 | 103 ms: 1.23x faster                                                        |
| mypy2                    | 428 ms                                                 | 349 ms: 1.23x faster                                                        |
| unpack_sequence          | 64.7 ns                                                | 52.8 ns: 1.23x faster                                                       |
| logging_format           | 8.91 us                                                | 7.27 us: 1.23x faster                                                       |
| logging_simple           | 8.07 us                                                | 6.60 us: 1.22x faster                                                       |
| regex_compile            | 177 ms                                                 | 146 ms: 1.22x faster                                                        |
| deepcopy                 | 442 us                                                 | 366 us: 1.21x faster                                                        |
| nqueens                  | 100 ms                                                 | 83.0 ms: 1.20x faster                                                       |
| sqlglot_normalize        | 135 ms                                                 | 114 ms: 1.19x faster                                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.24 us: 1.18x faster                                                       |
| sqlglot_optimize         | 65.3 ms                                                | 55.5 ms: 1.18x faster                                                       |
| scimark_fft              | 424 ms                                                 | 363 ms: 1.17x faster                                                        |
| docutils                 | 3.17 sec                                               | 2.75 sec: 1.15x faster                                                      |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                       |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 831 us: 1.14x faster                                                        |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                                       |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                       |
| dulwich_log              | 75.9 ms                                                | 68.6 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.94 ms: 1.10x faster                                                       |
| xml_etree_generate       | 94.2 ms                                                | 85.3 ms: 1.10x faster                                                       |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| mdp                      | 2.82 sec                                               | 2.63 sec: 1.07x faster                                                      |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                       |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                       |
| xml_etree_iterparse      | 111 ms                                                 | 105 ms: 1.06x faster                                                        |
| pickle_list              | 4.56 us                                                | 4.45 us: 1.02x faster                                                       |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                        |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| unpickle_list            | 4.82 us                                                | 4.97 us: 1.03x slower                                                       |
| telco                    | 6.54 ms                                                | 6.80 ms: 1.04x slower                                                       |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                       |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| async_generators         | 425 ms                                                 | 459 ms: 1.08x slower                                                        |
| regex_effbot             | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| pickle_dict              | 27.3 us                                                | 30.8 us: 1.13x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.81 ms: 1.17x slower                                                       |
| dask                     | 423 ms                                                 | 547 ms: 1.29x slower                                                        |
| coverage                 | 72.8 ms                                                | 96.8 ms: 1.33x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
