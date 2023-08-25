
# Results vs. 3.10.4

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: a0bd53a
- commit date: 2023-06-20
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| tornado_http   | 127 ms                                                 | 97.3 ms: 1.31x faster                                          |
| Geometric mean | (ref)                                                  | 1.25x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.2 ms: 1.57x faster                                          |
| float          | 111 ms                                                 | 80.1 ms: 1.38x faster                                          |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.28x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                           |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                          |
| regex_dna      | 222 ms                                                 | 202 ms: 1.10x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.44 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                           |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                           |
| json_dumps           | 13.5 ms                                                | 10.2 ms: 1.32x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 58.1 ms: 1.29x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                         |
| json_loads           | 28.8 us                                                | 25.4 us: 1.14x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 84.5 ms: 1.11x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                           |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                          |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.03 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                          |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                          |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.23 ms: 1.53x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230620-linux-x86_64-brandtbucher-to_bool-3.13.0a0-a0bd53a |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.48x faster                                           |
| generators               | 76.8 ms                                                | 29.0 ms: 2.64x faster                                          |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.81x faster                                           |
| chaos                    | 106 ms                                                 | 61.9 ms: 1.72x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                         |
| richards_super           | 90.7 ms                                                | 54.0 ms: 1.68x faster                                          |
| go                       | 229 ms                                                 | 139 ms: 1.65x faster                                           |
| logging_silent           | 175 ns                                                 | 107 ns: 1.64x faster                                           |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                           |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                           |
| nbody                    | 142 ms                                                 | 90.2 ms: 1.57x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.08 ms: 1.57x faster                                          |
| richards                 | 74.9 ms                                                | 47.9 ms: 1.56x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 77.2 ms: 1.53x faster                                          |
| python_startup           | 14.2 ms                                                | 9.23 ms: 1.53x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 71.8 ms: 1.51x faster                                          |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                           |
| pyflate                  | 673 ms                                                 | 454 ms: 1.48x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                          |
| async_tree_none          | 717 ms                                                 | 486 ms: 1.48x faster                                           |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.47x faster                                         |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                          |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 593 ms: 1.44x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 45.2 ns: 1.43x faster                                          |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.38x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                          |
| float                    | 111 ms                                                 | 80.1 ms: 1.38x faster                                          |
| logging_format           | 8.91 us                                                | 6.61 us: 1.35x faster                                          |
| logging_simple           | 8.07 us                                                | 6.01 us: 1.34x faster                                          |
| json_dumps               | 13.5 ms                                                | 10.2 ms: 1.32x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 726 ms: 1.31x faster                                           |
| tornado_http             | 127 ms                                                 | 97.3 ms: 1.31x faster                                          |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                         |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 58.1 ms: 1.29x faster                                          |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                           |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                           |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                         |
| nqueens                  | 100 ms                                                 | 79.1 ms: 1.27x faster                                          |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                           |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 53.4 ms: 1.22x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                          |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                           |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.16x faster                                          |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                          |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.79 ms: 1.14x faster                                          |
| json_loads               | 28.8 us                                                | 25.4 us: 1.14x faster                                          |
| json                     | 5.42 ms                                                | 4.84 ms: 1.12x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 84.5 ms: 1.11x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                          |
| regex_dna                | 222 ms                                                 | 202 ms: 1.10x faster                                           |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.54 ms: 1.08x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.07x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                          |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                         |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                          |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle_list            | 4.82 us                                                | 5.03 us: 1.04x slower                                          |
| telco                    | 6.54 ms                                                | 6.85 ms: 1.05x slower                                          |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                           |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.44 ms: 1.07x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                          |
| pickle_dict              | 27.3 us                                                | 32.4 us: 1.19x slower                                          |
| dask                     | 423 ms                                                 | 527 ms: 1.25x slower                                           |
| coverage                 | 72.8 ms                                                | 93.5 ms: 1.28x slower                                          |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x
