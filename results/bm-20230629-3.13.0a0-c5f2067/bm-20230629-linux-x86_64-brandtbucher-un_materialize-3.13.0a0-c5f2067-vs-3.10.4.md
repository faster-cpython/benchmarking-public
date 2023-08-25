
# Results vs. 3.10.4

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: c5f2067
- commit date: 2023-06-29
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                |
| tornado_http   | 127 ms                                                 | 96.4 ms: 1.32x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.2 ms: 1.57x faster                                                 |
| float          | 111 ms                                                 | 78.8 ms: 1.40x faster                                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                  |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                 |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 306 us: 1.49x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                 |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 57.1 ms: 1.31x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 82.8 ms: 1.14x faster                                                 |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                                 |
| pickle_list          | 4.56 us                                                | 4.75 us: 1.04x slower                                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                 |
| unpickle             | 14.1 us                                                | 15.5 us: 1.10x slower                                                 |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.5 ms: 1.40x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 142 us: 3.58x faster                                                  |
| generators               | 76.8 ms                                                | 28.9 ms: 2.66x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.24 ms: 2.29x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                                  |
| richards_super           | 90.7 ms                                                | 49.9 ms: 1.82x faster                                                 |
| chaos                    | 106 ms                                                 | 59.0 ms: 1.80x faster                                                 |
| logging_silent           | 175 ns                                                 | 97.7 ns: 1.79x faster                                                 |
| richards                 | 74.9 ms                                                | 43.8 ms: 1.71x faster                                                 |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                                  |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.01 ms: 1.59x faster                                                 |
| nbody                    | 142 ms                                                 | 90.2 ms: 1.57x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 76.0 ms: 1.56x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 72.0 ms: 1.50x faster                                                 |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                                  |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                                  |
| async_tree_none          | 717 ms                                                 | 477 ms: 1.50x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 306 us: 1.49x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                |
| async_tree_memoization   | 854 ms                                                 | 585 ms: 1.46x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                 |
| mako                     | 14.8 ms                                                | 10.5 ms: 1.40x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 37.3 us: 1.40x faster                                                 |
| float                    | 111 ms                                                 | 78.8 ms: 1.40x faster                                                 |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                  |
| logging_format           | 8.91 us                                                | 6.39 us: 1.39x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.45 sec: 1.37x faster                                                |
| logging_simple           | 8.07 us                                                | 5.93 us: 1.36x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 47.9 ns: 1.35x faster                                                 |
| pprint_safe_repr         | 955 ms                                                 | 711 ms: 1.34x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 718 ms: 1.32x faster                                                  |
| tornado_http             | 127 ms                                                 | 96.4 ms: 1.32x faster                                                 |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 57.1 ms: 1.31x faster                                                 |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.30x faster                                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                  |
| pycparser                | 1.50 sec                                               | 1.18 sec: 1.27x faster                                                |
| nqueens                  | 100 ms                                                 | 80.1 ms: 1.25x faster                                                 |
| sqlglot_optimize         | 65.3 ms                                                | 52.4 ms: 1.25x faster                                                 |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                                  |
| fannkuch                 | 486 ms                                                 | 393 ms: 1.24x faster                                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                 |
| docutils                 | 3.17 sec                                               | 2.64 sec: 1.20x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.57 ms: 1.19x faster                                                 |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                  |
| bench_thread_pool        | 947 us                                                 | 814 us: 1.16x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 65.4 ms: 1.16x faster                                                 |
| xml_etree_generate       | 94.2 ms                                                | 82.8 ms: 1.14x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                 |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                                 |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                 |
| meteor_contest           | 115 ms                                                 | 103 ms: 1.11x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                                 |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.70 sec: 1.04x faster                                                |
| pathlib                  | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                 |
| gc_traversal             | 3.84 ms                                                | 3.91 ms: 1.02x slower                                                 |
| unpickle_list            | 4.82 us                                                | 4.93 us: 1.02x slower                                                 |
| async_generators         | 425 ms                                                 | 437 ms: 1.03x slower                                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                  |
| pickle_list              | 4.56 us                                                | 4.75 us: 1.04x slower                                                 |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                 |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                                 |
| unpickle                 | 14.1 us                                                | 15.5 us: 1.10x slower                                                 |
| telco                    | 6.54 ms                                                | 7.31 ms: 1.12x slower                                                 |
| pickle_dict              | 27.3 us                                                | 31.0 us: 1.14x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.70 ms: 1.15x slower                                                 |
| dask                     | 423 ms                                                 | 512 ms: 1.21x slower                                                  |
| coverage                 | 72.8 ms                                                | 92.0 ms: 1.26x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
