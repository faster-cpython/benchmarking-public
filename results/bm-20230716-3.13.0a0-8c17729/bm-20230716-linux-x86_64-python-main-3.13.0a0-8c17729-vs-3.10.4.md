
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8c17729
- commit date: 2023-07-16
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                |
| tornado_http   | 127 ms                                                 | 96.8 ms: 1.32x faster                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.3 ms: 1.58x faster                                 |
| float          | 111 ms                                                 | 80.7 ms: 1.37x faster                                 |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                 |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.67 ms: 1.14x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 298 us: 1.53x faster                                  |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.40x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.77 ms: 1.38x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 58.5 ms: 1.28x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                 |
| json_loads           | 28.8 us                                                | 26.1 us: 1.10x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| pickle_list          | 4.56 us                                                | 4.70 us: 1.03x slower                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                 |
| unpickle_list        | 4.82 us                                                | 5.14 us: 1.07x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.25 ms: 1.53x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.44x faster                                  |
| generators               | 76.8 ms                                                | 28.7 ms: 2.68x faster                                 |
| deltablue                | 7.42 ms                                                | 3.26 ms: 2.28x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                  |
| chaos                    | 106 ms                                                 | 59.8 ms: 1.78x faster                                 |
| raytrace                 | 464 ms                                                 | 268 ms: 1.73x faster                                  |
| logging_silent           | 175 ns                                                 | 103 ns: 1.71x faster                                  |
| richards_super           | 90.7 ms                                                | 54.0 ms: 1.68x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| crypto_pyaes             | 118 ms                                                 | 71.1 ms: 1.67x faster                                 |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                  |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                 |
| nbody                    | 142 ms                                                 | 89.3 ms: 1.58x faster                                 |
| scimark_monte_carlo      | 108 ms                                                 | 68.5 ms: 1.58x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.11 ms: 1.56x faster                                 |
| richards                 | 74.9 ms                                                | 48.1 ms: 1.56x faster                                 |
| unpack_sequence          | 64.7 ns                                                | 42.3 ns: 1.53x faster                                 |
| python_startup           | 14.2 ms                                                | 9.25 ms: 1.53x faster                                 |
| pickle_pure_python       | 455 us                                                 | 298 us: 1.53x faster                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.51x faster                                |
| pyflate                  | 673 ms                                                 | 449 ms: 1.50x faster                                  |
| async_tree_none          | 717 ms                                                 | 481 ms: 1.49x faster                                  |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 583 ms: 1.46x faster                                  |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.40x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.77 ms: 1.38x faster                                 |
| spectral_norm            | 150 ms                                                 | 109 ms: 1.38x faster                                  |
| float                    | 111 ms                                                 | 80.7 ms: 1.37x faster                                 |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                 |
| logging_format           | 8.91 us                                                | 6.54 us: 1.36x faster                                 |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 721 ms: 1.32x faster                                  |
| tornado_http             | 127 ms                                                 | 96.8 ms: 1.32x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                  |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.29x faster                                |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 58.5 ms: 1.28x faster                                 |
| regex_compile            | 177 ms                                                 | 138 ms: 1.28x faster                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| nqueens                  | 100 ms                                                 | 80.2 ms: 1.25x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.5 ms: 1.24x faster                                 |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                  |
| fannkuch                 | 486 ms                                                 | 397 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.22x faster                                 |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                |
| scimark_fft              | 424 ms                                                 | 360 ms: 1.18x faster                                  |
| bench_thread_pool        | 947 us                                                 | 820 us: 1.15x faster                                  |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                 |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.82 ms: 1.13x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                 |
| json_loads               | 28.8 us                                                | 26.1 us: 1.10x faster                                 |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json                     | 5.42 ms                                                | 4.96 ms: 1.09x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                 |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.06x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                  |
| gc_traversal             | 3.84 ms                                                | 3.94 ms: 1.02x slower                                 |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| pickle_list              | 4.56 us                                                | 4.70 us: 1.03x slower                                 |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                  |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                 |
| unpickle_list            | 4.82 us                                                | 5.14 us: 1.07x slower                                 |
| async_generators         | 425 ms                                                 | 454 ms: 1.07x slower                                  |
| telco                    | 6.54 ms                                                | 7.28 ms: 1.11x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.67 ms: 1.14x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.7 us: 1.16x slower                                 |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                  |
| coverage                 | 72.8 ms                                                | 94.1 ms: 1.29x slower                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
