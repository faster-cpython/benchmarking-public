
# Results vs. 3.10.4

- fork: brandtbucher
- ref: binary_subscr_str_in
- machine: linux-x86_64
- commit hash: ccddc2b
- commit date: 2023-08-03
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                      |
| tornado_http   | 127 ms                                                 | 95.7 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.3 ms: 1.50x faster                                                       |
| float          | 111 ms                                                 | 80.1 ms: 1.38x faster                                                       |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.29x faster                                                        |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                                       |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 295 us: 1.54x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                       |
| tomli_loads          | 2.92 sec                                               | 2.13 sec: 1.37x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                       |
| json_loads           | 28.8 us                                                | 26.4 us: 1.09x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| unpickle_list        | 4.82 us                                                | 5.11 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230803-linux-x86_64-brandtbucher-binary_subscr_str_in-3.13.0a0-ccddc2b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.56x faster                                                        |
| generators               | 76.8 ms                                                | 29.6 ms: 2.59x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                        |
| chaos                    | 106 ms                                                 | 60.3 ms: 1.76x faster                                                       |
| raytrace                 | 464 ms                                                 | 272 ms: 1.71x faster                                                        |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 70.5 ms: 1.68x faster                                                       |
| richards_super           | 90.7 ms                                                | 54.5 ms: 1.67x faster                                                       |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                                        |
| logging_silent           | 175 ns                                                 | 108 ns: 1.62x faster                                                        |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                       |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                        |
| scimark_monte_carlo      | 108 ms                                                 | 69.3 ms: 1.56x faster                                                       |
| richards                 | 74.9 ms                                                | 48.3 ms: 1.55x faster                                                       |
| pickle_pure_python       | 455 us                                                 | 295 us: 1.54x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.53x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.23 ms: 1.53x faster                                                       |
| python_startup           | 14.2 ms                                                | 9.40 ms: 1.51x faster                                                       |
| nbody                    | 142 ms                                                 | 94.3 ms: 1.50x faster                                                       |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                                        |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                      |
| async_tree_none          | 717 ms                                                 | 484 ms: 1.48x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 587 ms: 1.46x faster                                                        |
| coroutines               | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                        |
| json_dumps               | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                       |
| unpack_sequence          | 64.7 ns                                                | 46.9 ns: 1.38x faster                                                       |
| float                    | 111 ms                                                 | 80.1 ms: 1.38x faster                                                       |
| tomli_loads              | 2.92 sec                                               | 2.13 sec: 1.37x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 38.2 us: 1.37x faster                                                       |
| spectral_norm            | 150 ms                                                 | 110 ms: 1.37x faster                                                        |
| logging_format           | 8.91 us                                                | 6.56 us: 1.36x faster                                                       |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                       |
| logging_simple           | 8.07 us                                                | 5.99 us: 1.35x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                      |
| tornado_http             | 127 ms                                                 | 95.7 ms: 1.33x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 719 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 721 ms: 1.32x faster                                                        |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                                       |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| regex_compile            | 177 ms                                                 | 138 ms: 1.29x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                       |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.29x faster                                                      |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                        |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                        |
| nqueens                  | 100 ms                                                 | 80.7 ms: 1.24x faster                                                       |
| sqlglot_optimize         | 65.3 ms                                                | 52.8 ms: 1.24x faster                                                       |
| fannkuch                 | 486 ms                                                 | 402 ms: 1.21x faster                                                        |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                        |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.22 us: 1.19x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.66 ms: 1.17x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                        |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                                       |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                       |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                                       |
| json                     | 5.42 ms                                                | 4.94 ms: 1.10x faster                                                       |
| json_loads               | 28.8 us                                                | 26.4 us: 1.09x faster                                                       |
| regex_v8                 | 25.0 ms                                                | 23.0 ms: 1.09x faster                                                       |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                        |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                       |
| regex_dna                | 222 ms                                                 | 216 ms: 1.03x faster                                                        |
| pickle_list              | 4.56 us                                                | 4.51 us: 1.01x faster                                                       |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                       |
| gc_traversal             | 3.84 ms                                                | 3.99 ms: 1.04x slower                                                       |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                                        |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                        |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| unpickle_list            | 4.82 us                                                | 5.11 us: 1.06x slower                                                       |
| regex_effbot             | 3.23 ms                                                | 3.55 ms: 1.10x slower                                                       |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.87 ms: 1.18x slower                                                       |
| telco                    | 6.54 ms                                                | 7.77 ms: 1.19x slower                                                       |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                                        |
| coverage                 | 72.8 ms                                                | 93.9 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
