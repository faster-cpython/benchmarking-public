
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: a47c13c
- commit date: 2023-08-19
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.62 sec: 1.21x faster                                |
| tornado_http   | 127 ms                                                 | 95.9 ms: 1.33x faster                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.9 ms: 1.56x faster                                 |
| float          | 111 ms                                                 | 79.7 ms: 1.39x faster                                 |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.7 ms: 1.02x faster                                 |
| regex_effbot   | 3.23 ms                                                | 3.55 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 303 us: 1.50x faster                                  |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.10 sec: 1.39x faster                                |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 58.2 ms: 1.29x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 83.2 ms: 1.13x faster                                 |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| unpickle             | 14.1 us                                                | 14.2 us: 1.01x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                 |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                 |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.51x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.85 ms: 1.18x slower                                 |
| Geometric mean         | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230819-linux-x86_64-python-main-3.13.0a0-a47c13c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                  |
| generators               | 76.8 ms                                                | 29.2 ms: 2.63x faster                                 |
| deltablue                | 7.42 ms                                                | 3.32 ms: 2.24x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 487 ms: 1.90x faster                                  |
| chaos                    | 106 ms                                                 | 59.8 ms: 1.78x faster                                 |
| logging_silent           | 175 ns                                                 | 104 ns: 1.69x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 70.1 ms: 1.69x faster                                 |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                |
| raytrace                 | 464 ms                                                 | 275 ms: 1.68x faster                                  |
| richards_super           | 90.7 ms                                                | 54.2 ms: 1.67x faster                                 |
| async_tree_none          | 717 ms                                                 | 439 ms: 1.63x faster                                  |
| go                       | 229 ms                                                 | 142 ms: 1.61x faster                                  |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 67.2 ms: 1.61x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.60x faster                                 |
| richards                 | 74.9 ms                                                | 47.7 ms: 1.57x faster                                 |
| hexiom                   | 9.53 ms                                                | 6.11 ms: 1.56x faster                                 |
| nbody                    | 142 ms                                                 | 90.9 ms: 1.56x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                 |
| async_tree_memoization   | 854 ms                                                 | 560 ms: 1.53x faster                                  |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.51x faster                                 |
| pickle_pure_python       | 455 us                                                 | 303 us: 1.50x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                |
| pyflate                  | 673 ms                                                 | 452 ms: 1.49x faster                                  |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 43.8 ns: 1.48x faster                                 |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                 |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.4 us: 1.40x faster                                 |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.10 sec: 1.39x faster                                |
| float                    | 111 ms                                                 | 79.7 ms: 1.39x faster                                 |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                 |
| logging_simple           | 8.07 us                                                | 5.90 us: 1.37x faster                                 |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                 |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 701 ms: 1.36x faster                                  |
| tornado_http             | 127 ms                                                 | 95.9 ms: 1.33x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 58.2 ms: 1.29x faster                                 |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                 |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                  |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                  |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                  |
| nqueens                  | 100 ms                                                 | 79.5 ms: 1.26x faster                                 |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.25x faster                                |
| sqlglot_optimize         | 65.3 ms                                                | 52.7 ms: 1.24x faster                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.23x faster                                 |
| docutils                 | 3.17 sec                                               | 2.62 sec: 1.21x faster                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.53 ms: 1.20x faster                                 |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                  |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                  |
| dulwich_log              | 75.9 ms                                                | 66.4 ms: 1.14x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.2 ms: 1.13x faster                                 |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| json                     | 5.42 ms                                                | 4.86 ms: 1.11x faster                                 |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                 |
| xml_etree_iterparse      | 111 ms                                                 | 102 ms: 1.09x faster                                  |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                 |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                  |
| regex_v8                 | 25.0 ms                                                | 24.7 ms: 1.02x faster                                 |
| unpickle                 | 14.1 us                                                | 14.2 us: 1.01x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.88 us: 1.01x slower                                 |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                 |
| gc_traversal             | 3.84 ms                                                | 3.93 ms: 1.02x slower                                 |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                 |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                  |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.55 ms: 1.10x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.4 us: 1.15x slower                                 |
| coverage                 | 72.8 ms                                                | 84.7 ms: 1.16x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.85 ms: 1.18x slower                                 |
| telco                    | 6.54 ms                                                | 7.98 ms: 1.22x slower                                 |
| dask                     | 423 ms                                                 | 524 ms: 1.24x slower                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                          |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x
