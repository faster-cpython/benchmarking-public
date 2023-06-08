
# Results vs. 3.10.4

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 27bb264
- commit date: 2023-06-07
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                      |
| tornado_http   | 127 ms                                                 | 103 ms: 1.23x faster                                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.56x faster                                                       |
| float          | 111 ms                                                 | 80.9 ms: 1.37x faster                                                       |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.44x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 224 us: 1.34x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.27 sec: 1.28x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                       |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 85.1 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                       |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                       |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.37 ms: 1.51x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-27bb264 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                                        |
| generators               | 76.8 ms                                                | 31.9 ms: 2.41x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.66 ms: 2.02x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                                        |
| richards_super           | 90.7 ms                                                | 51.0 ms: 1.78x faster                                                       |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                                        |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                      |
| richards                 | 74.9 ms                                                | 45.0 ms: 1.67x faster                                                       |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                                        |
| chaos                    | 106 ms                                                 | 65.6 ms: 1.62x faster                                                       |
| nbody                    | 142 ms                                                 | 90.5 ms: 1.56x faster                                                       |
| raytrace                 | 464 ms                                                 | 298 ms: 1.55x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.37 ms: 1.51x faster                                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.36 ms: 1.51x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.42 ms: 1.48x faster                                                       |
| crypto_pyaes             | 118 ms                                                 | 79.9 ms: 1.48x faster                                                       |
| scimark_monte_carlo      | 108 ms                                                 | 73.5 ms: 1.47x faster                                                       |
| pyflate                  | 673 ms                                                 | 465 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                 | 315 us: 1.44x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                       |
| scimark_lu               | 163 ms                                                 | 114 ms: 1.44x faster                                                        |
| scimark_sor              | 197 ms                                                 | 137 ms: 1.43x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.24 sec: 1.43x faster                                                      |
| async_tree_none          | 717 ms                                                 | 500 ms: 1.43x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 607 ms: 1.41x faster                                                        |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                        |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.39x faster                                                       |
| json_dumps               | 13.5 ms                                                | 9.89 ms: 1.37x faster                                                       |
| float                    | 111 ms                                                 | 80.9 ms: 1.37x faster                                                       |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.36x faster                                                       |
| unpickle_pure_python     | 300 us                                                 | 224 us: 1.34x faster                                                        |
| coroutines               | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.53 sec: 1.30x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.27 sec: 1.28x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 744 ms: 1.28x faster                                                        |
| pprint_safe_repr         | 955 ms                                                 | 752 ms: 1.27x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                       |
| comprehensions           | 26.8 us                                                | 21.2 us: 1.26x faster                                                       |
| pycparser                | 1.50 sec                                               | 1.21 sec: 1.24x faster                                                      |
| mypy2                    | 428 ms                                                 | 348 ms: 1.23x faster                                                        |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                                        |
| tornado_http             | 127 ms                                                 | 103 ms: 1.23x faster                                                        |
| logging_simple           | 8.07 us                                                | 6.61 us: 1.22x faster                                                       |
| fannkuch                 | 486 ms                                                 | 400 ms: 1.21x faster                                                        |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| logging_format           | 8.91 us                                                | 7.36 us: 1.21x faster                                                       |
| sqlglot_normalize        | 135 ms                                                 | 113 ms: 1.20x faster                                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                       |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                                        |
| sqlglot_optimize         | 65.3 ms                                                | 55.1 ms: 1.19x faster                                                       |
| unpack_sequence          | 64.7 ns                                                | 54.8 ns: 1.18x faster                                                       |
| nqueens                  | 100 ms                                                 | 84.9 ms: 1.18x faster                                                       |
| docutils                 | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                      |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.77 ms: 1.14x faster                                                       |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 835 us: 1.14x faster                                                        |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                                       |
| dulwich_log              | 75.9 ms                                                | 68.4 ms: 1.11x faster                                                       |
| xml_etree_generate       | 94.2 ms                                                | 85.1 ms: 1.11x faster                                                       |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                       |
| pathlib                  | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                       |
| mdp                      | 2.82 sec                                               | 2.59 sec: 1.09x faster                                                      |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| pickle_list              | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                                       |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                                        |
| gc_traversal             | 3.84 ms                                                | 3.99 ms: 1.04x slower                                                       |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                       |
| telco                    | 6.54 ms                                                | 7.00 ms: 1.07x slower                                                       |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| async_generators         | 425 ms                                                 | 457 ms: 1.08x slower                                                        |
| pickle_dict              | 27.3 us                                                | 30.4 us: 1.12x slower                                                       |
| regex_effbot             | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                       |
| dask                     | 423 ms                                                 | 547 ms: 1.30x slower                                                        |
| coverage                 | 72.8 ms                                                | 96.4 ms: 1.32x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
