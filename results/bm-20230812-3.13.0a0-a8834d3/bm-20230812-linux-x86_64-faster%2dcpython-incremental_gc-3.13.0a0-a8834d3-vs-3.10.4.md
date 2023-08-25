
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: a8834d3
- commit date: 2023-08-12
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.37 sec: 1.34x faster                                                    |
| tornado_http   | 127 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.3 ms: 1.60x faster                                                     |
| float          | 111 ms                                                 | 70.9 ms: 1.56x faster                                                     |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                     |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 297 us: 1.53x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 94.1 ms: 1.18x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 139 ms: 1.17x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 80.5 ms: 1.17x faster                                                     |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.52 us: 1.01x faster                                                     |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| unpickle             | 14.1 us                                                | 14.7 us: 1.04x slower                                                     |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.80 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-a8834d3 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 565 ms: 3.14x faster                                                      |
| generators               | 76.8 ms                                                | 28.2 ms: 2.72x faster                                                     |
| async_tree_none          | 717 ms                                                 | 276 ms: 2.60x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 343 ms: 2.49x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.13 ms: 2.37x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 486 ms: 1.90x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 505 ms: 1.88x faster                                                      |
| chaos                    | 106 ms                                                 | 58.7 ms: 1.81x faster                                                     |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                                      |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 69.3 ms: 1.71x faster                                                     |
| richards_super           | 90.7 ms                                                | 53.2 ms: 1.71x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                      |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 66.4 ms: 1.63x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.27 ms: 1.62x faster                                                     |
| nbody                    | 142 ms                                                 | 88.3 ms: 1.60x faster                                                     |
| richards                 | 74.9 ms                                                | 47.4 ms: 1.58x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.02 ms: 1.58x faster                                                     |
| float                    | 111 ms                                                 | 70.9 ms: 1.56x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.54x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 297 us: 1.53x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| pyflate                  | 673 ms                                                 | 453 ms: 1.49x faster                                                      |
| scimark_lu               | 163 ms                                                 | 112 ms: 1.46x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 46.1 ns: 1.40x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 37.4 us: 1.40x faster                                                     |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                      |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.88 us: 1.37x faster                                                     |
| tornado_http             | 127 ms                                                 | 94.0 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| xml_etree_process        | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.37 sec: 1.34x faster                                                    |
| pycparser                | 1.50 sec                                               | 1.12 sec: 1.34x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 722 ms: 1.32x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.31x faster                                                     |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                      |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.31 sec: 1.26x faster                                                    |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.5 ms: 1.24x faster                                                     |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                                      |
| nqueens                  | 100 ms                                                 | 80.7 ms: 1.24x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 94.1 ms: 1.18x faster                                                     |
| scimark_fft              | 424 ms                                                 | 359 ms: 1.18x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.42 ms: 1.17x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 139 ms: 1.17x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 80.5 ms: 1.17x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 65.7 ms: 1.15x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.79 ms: 1.14x faster                                                     |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                     |
| json                     | 5.42 ms                                                | 4.86 ms: 1.11x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                     |
| regex_dna                | 222 ms                                                 | 204 ms: 1.09x faster                                                      |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.80 us: 1.05x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.68 ms: 1.04x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.72 sec: 1.04x faster                                                    |
| pickle_list              | 4.56 us                                                | 4.52 us: 1.01x faster                                                     |
| unpickle_list            | 4.82 us                                                | 4.97 us: 1.03x slower                                                     |
| unpickle                 | 14.1 us                                                | 14.7 us: 1.04x slower                                                     |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                      |
| regex_effbot             | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                     |
| dask                     | 423 ms                                                 | 486 ms: 1.15x slower                                                      |
| pickle_dict              | 27.3 us                                                | 31.6 us: 1.16x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.80 ms: 1.17x slower                                                     |
| telco                    | 6.54 ms                                                | 7.94 ms: 1.21x slower                                                     |
| coverage                 | 72.8 ms                                                | 92.9 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, async_generators
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
