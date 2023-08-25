
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8571b27
- commit date: 2023-07-02
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                |
| tornado_http   | 127 ms                                                 | 96.5 ms: 1.32x faster                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.57x faster                                 |
| float          | 111 ms                                                 | 80.4 ms: 1.38x faster                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                 |
| regex_dna      | 222 ms                                                 | 214 ms: 1.03x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.68 ms: 1.14x slower                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 301 us: 1.51x faster                                  |
| unpickle_pure_python | 300 us                                                 | 213 us: 1.41x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.71 ms: 1.39x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 58.2 ms: 1.29x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.90 us: 1.02x slower                                 |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                 |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                 |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.16 ms: 1.54x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230702-linux-x86_64-python-main-3.13.0a0-8571b27 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                  |
| generators               | 76.8 ms                                                | 30.0 ms: 2.56x faster                                 |
| deltablue                | 7.42 ms                                                | 3.33 ms: 2.23x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 510 ms: 1.81x faster                                  |
| chaos                    | 106 ms                                                 | 59.6 ms: 1.78x faster                                 |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                  |
| raytrace                 | 464 ms                                                 | 270 ms: 1.72x faster                                  |
| richards_super           | 90.7 ms                                                | 53.2 ms: 1.70x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.62x faster                                  |
| richards                 | 74.9 ms                                                | 47.1 ms: 1.59x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.02 ms: 1.58x faster                                 |
| nbody                    | 142 ms                                                 | 90.5 ms: 1.57x faster                                 |
| python_startup           | 14.2 ms                                                | 9.16 ms: 1.54x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.54x faster                                 |
| crypto_pyaes             | 118 ms                                                 | 76.9 ms: 1.54x faster                                 |
| pickle_pure_python       | 455 us                                                 | 301 us: 1.51x faster                                  |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                  |
| async_tree_none          | 717 ms                                                 | 484 ms: 1.48x faster                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.48x faster                                 |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                |
| scimark_monte_carlo      | 108 ms                                                 | 73.5 ms: 1.47x faster                                 |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 593 ms: 1.44x faster                                  |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 213 us: 1.41x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 46.2 ns: 1.40x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.71 ms: 1.39x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                 |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                 |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.38x faster                                  |
| float                    | 111 ms                                                 | 80.4 ms: 1.38x faster                                 |
| logging_format           | 8.91 us                                                | 6.50 us: 1.37x faster                                 |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.35x faster                                |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                  |
| tornado_http             | 127 ms                                                 | 96.5 ms: 1.32x faster                                 |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 726 ms: 1.31x faster                                  |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.29x faster                                |
| xml_etree_process        | 74.9 ms                                                | 58.2 ms: 1.29x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                  |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| nqueens                  | 100 ms                                                 | 79.9 ms: 1.25x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.3 ms: 1.23x faster                                 |
| fannkuch                 | 486 ms                                                 | 399 ms: 1.22x faster                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                 |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.67 ms: 1.17x faster                                 |
| bench_thread_pool        | 947 us                                                 | 816 us: 1.16x faster                                  |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                 |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.8 ms: 1.12x faster                                 |
| json                     | 5.42 ms                                                | 4.87 ms: 1.11x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.10x faster                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                  |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.06x faster                                |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.06x faster                                 |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.05x faster                                 |
| regex_dna                | 222 ms                                                 | 214 ms: 1.03x faster                                  |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.90 us: 1.02x slower                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                 |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                 |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                 |
| async_generators         | 425 ms                                                 | 453 ms: 1.07x slower                                  |
| telco                    | 6.54 ms                                                | 7.25 ms: 1.11x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.68 ms: 1.14x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.17x slower                                 |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                  |
| coverage                 | 72.8 ms                                                | 93.1 ms: 1.28x slower                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x
