
# Results vs. 3.10.4

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: e03a937
- commit date: 2023-08-04
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                      |
| tornado_http   | 127 ms                                                 | 95.9 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.2 ms: 1.59x faster                                                       |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                                        |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                       |
| tomli_loads          | 2.92 sec                                               | 2.37 sec: 1.23x faster                                                      |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.45 us: 1.02x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.15 us: 1.07x slower                                                       |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.43 ms: 1.50x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.89 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230804-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-e03a937 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                        |
| generators               | 76.8 ms                                                | 28.3 ms: 2.71x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.19 ms: 2.33x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 483 ms: 1.91x faster                                                        |
| chaos                    | 106 ms                                                 | 59.2 ms: 1.80x faster                                                       |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                                        |
| crypto_pyaes             | 118 ms                                                 | 69.4 ms: 1.71x faster                                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                      |
| richards_super           | 90.7 ms                                                | 54.6 ms: 1.66x faster                                                       |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                                        |
| logging_silent           | 175 ns                                                 | 107 ns: 1.64x faster                                                        |
| sqlglot_parse            | 2.06 ms                                                | 1.26 ms: 1.63x faster                                                       |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                        |
| scimark_monte_carlo      | 108 ms                                                 | 67.5 ms: 1.60x faster                                                       |
| nbody                    | 142 ms                                                 | 89.2 ms: 1.59x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.05 ms: 1.57x faster                                                       |
| sqlglot_transpile        | 2.45 ms                                                | 1.57 ms: 1.56x faster                                                       |
| richards                 | 74.9 ms                                                | 48.2 ms: 1.55x faster                                                       |
| pickle_pure_python       | 455 us                                                 | 294 us: 1.55x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.43 ms: 1.50x faster                                                       |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                      |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.49x faster                                                        |
| pyflate                  | 673 ms                                                 | 455 ms: 1.48x faster                                                        |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                       |
| async_tree_memoization   | 854 ms                                                 | 592 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                                        |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                                        |
| float                    | 111 ms                                                 | 80.0 ms: 1.38x faster                                                       |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                                       |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                       |
| logging_format           | 8.91 us                                                | 6.55 us: 1.36x faster                                                       |
| logging_simple           | 8.07 us                                                | 5.94 us: 1.36x faster                                                       |
| json_dumps               | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                      |
| tornado_http             | 127 ms                                                 | 95.9 ms: 1.33x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 720 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 721 ms: 1.32x faster                                                        |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                       |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                       |
| unpack_sequence          | 64.7 ns                                                | 50.7 ns: 1.28x faster                                                       |
| pycparser                | 1.50 sec                                               | 1.18 sec: 1.27x faster                                                      |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                                        |
| fannkuch                 | 486 ms                                                 | 387 ms: 1.26x faster                                                        |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                                        |
| nqueens                  | 100 ms                                                 | 80.8 ms: 1.24x faster                                                       |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                                       |
| tomli_loads              | 2.92 sec                                               | 2.37 sec: 1.23x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                                      |
| scimark_fft              | 424 ms                                                 | 355 ms: 1.19x faster                                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.26 us: 1.17x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                        |
| dulwich_log              | 75.9 ms                                                | 66.5 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.79 ms: 1.14x faster                                                       |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                       |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                                       |
| json                     | 5.42 ms                                                | 4.81 ms: 1.13x faster                                                       |
| xml_etree_generate       | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                       |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                       |
| regex_dna                | 222 ms                                                 | 202 ms: 1.10x faster                                                        |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                                        |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                                       |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                      |
| pickle_list              | 4.56 us                                                | 4.45 us: 1.02x faster                                                       |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                        |
| gc_traversal             | 3.84 ms                                                | 4.00 ms: 1.04x slower                                                       |
| regex_effbot             | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                       |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                                        |
| unpickle_list            | 4.82 us                                                | 5.15 us: 1.07x slower                                                       |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                       |
| pickle_dict              | 27.3 us                                                | 30.4 us: 1.12x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.89 ms: 1.19x slower                                                       |
| telco                    | 6.54 ms                                                | 7.92 ms: 1.21x slower                                                       |
| dask                     | 423 ms                                                 | 522 ms: 1.24x slower                                                        |
| coverage                 | 72.8 ms                                                | 94.0 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x
