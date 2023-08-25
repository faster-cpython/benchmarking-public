
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: da98ed0
- commit date: 2023-07-08
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.19x faster                                |
| tornado_http   | 127 ms                                                 | 96.2 ms: 1.32x faster                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.4 ms: 1.60x faster                                 |
| float          | 111 ms                                                 | 78.7 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                 |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 302 us: 1.51x faster                                  |
| unpickle_pure_python | 300 us                                                 | 209 us: 1.43x faster                                  |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                 |
| xml_etree_process    | 74.9 ms                                                | 57.3 ms: 1.31x faster                                 |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| xml_etree_generate   | 94.2 ms                                                | 83.4 ms: 1.13x faster                                 |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| pickle_list          | 4.56 us                                                | 4.49 us: 1.02x faster                                 |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                 |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                 |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| Geometric mean         | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.5 ms: 1.40x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-linux-x86_64-python-main-3.13.0a0-da98ed0 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                  |
| generators               | 76.8 ms                                                | 28.6 ms: 2.69x faster                                 |
| deltablue                | 7.42 ms                                                | 3.23 ms: 2.30x faster                                 |
| asyncio_tcp              | 925 ms                                                 | 507 ms: 1.82x faster                                  |
| chaos                    | 106 ms                                                 | 59.4 ms: 1.79x faster                                 |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                  |
| richards_super           | 90.7 ms                                                | 52.3 ms: 1.74x faster                                 |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                  |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                |
| scimark_sor              | 197 ms                                                 | 117 ms: 1.68x faster                                  |
| richards                 | 74.9 ms                                                | 46.2 ms: 1.62x faster                                 |
| nbody                    | 142 ms                                                 | 88.4 ms: 1.60x faster                                 |
| hexiom                   | 9.53 ms                                                | 5.98 ms: 1.59x faster                                 |
| crypto_pyaes             | 118 ms                                                 | 76.0 ms: 1.56x faster                                 |
| python_startup           | 14.2 ms                                                | 9.18 ms: 1.54x faster                                 |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                 |
| pyflate                  | 673 ms                                                 | 440 ms: 1.53x faster                                  |
| pickle_pure_python       | 455 us                                                 | 302 us: 1.51x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 72.2 ms: 1.50x faster                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                 |
| async_tree_none          | 717 ms                                                 | 485 ms: 1.48x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                  |
| async_tree_memoization   | 854 ms                                                 | 590 ms: 1.45x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 209 us: 1.43x faster                                  |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                 |
| float                    | 111 ms                                                 | 78.7 ms: 1.40x faster                                 |
| mako                     | 14.8 ms                                                | 10.5 ms: 1.40x faster                                 |
| deepcopy_memo            | 52.3 us                                                | 37.3 us: 1.40x faster                                 |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                  |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                 |
| unpack_sequence          | 64.7 ns                                                | 47.1 ns: 1.37x faster                                 |
| logging_format           | 8.91 us                                                | 6.51 us: 1.37x faster                                 |
| pprint_pformat           | 1.99 sec                                               | 1.45 sec: 1.37x faster                                |
| logging_simple           | 8.07 us                                                | 5.92 us: 1.36x faster                                 |
| pprint_safe_repr         | 955 ms                                                 | 709 ms: 1.35x faster                                  |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                 |
| tornado_http             | 127 ms                                                 | 96.2 ms: 1.32x faster                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 721 ms: 1.32x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 57.3 ms: 1.31x faster                                 |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                  |
| deepcopy                 | 442 us                                                 | 346 us: 1.28x faster                                  |
| mypy2                    | 428 ms                                                 | 336 ms: 1.27x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.27x faster                                  |
| pycparser                | 1.50 sec                                               | 1.19 sec: 1.26x faster                                |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                |
| fannkuch                 | 486 ms                                                 | 390 ms: 1.25x faster                                  |
| nqueens                  | 100 ms                                                 | 80.4 ms: 1.24x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.2 ms: 1.23x faster                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.17 us: 1.21x faster                                 |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.19x faster                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.58 ms: 1.19x faster                                 |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                  |
| bench_thread_pool        | 947 us                                                 | 814 us: 1.16x faster                                  |
| dulwich_log              | 75.9 ms                                                | 65.6 ms: 1.16x faster                                 |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                 |
| xml_etree_generate       | 94.2 ms                                                | 83.4 ms: 1.13x faster                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                 |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                 |
| json                     | 5.42 ms                                                | 4.89 ms: 1.11x faster                                 |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.11x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.07x faster                                 |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                 |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                  |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.07x faster                                |
| gc_traversal             | 3.84 ms                                                | 3.65 ms: 1.05x faster                                 |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                  |
| pickle_list              | 4.56 us                                                | 4.49 us: 1.02x faster                                 |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                 |
| unpickle_list            | 4.82 us                                                | 4.96 us: 1.03x slower                                 |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| async_generators         | 425 ms                                                 | 447 ms: 1.05x slower                                  |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                 |
| telco                    | 6.54 ms                                                | 7.13 ms: 1.09x slower                                 |
| regex_effbot             | 3.23 ms                                                | 3.61 ms: 1.12x slower                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                 |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                 |
| dask                     | 423 ms                                                 | 522 ms: 1.23x slower                                  |
| coverage                 | 72.8 ms                                                | 91.1 ms: 1.25x slower                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
