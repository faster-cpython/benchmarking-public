
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 58901ff
- commit date: 2023-08-12
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.39 sec: 1.32x faster                                                    |
| tornado_http   | 127 ms                                                 | 93.5 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                                     |
| float          | 111 ms                                                 | 71.9 ms: 1.54x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.11x faster                                                     |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.46 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.28 sec: 1.28x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 93.8 ms: 1.19x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 141 ms: 1.16x faster                                                      |
| json_loads           | 28.8 us                                                | 25.6 us: 1.13x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                                     |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                     |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.28 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.81 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-58901ff |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 561 ms: 3.16x faster                                                      |
| generators               | 76.8 ms                                                | 28.1 ms: 2.73x faster                                                     |
| async_tree_none          | 717 ms                                                 | 276 ms: 2.59x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 342 ms: 2.50x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.12 ms: 2.38x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 503 ms: 1.89x faster                                                      |
| chaos                    | 106 ms                                                 | 59.0 ms: 1.80x faster                                                     |
| logging_silent           | 175 ns                                                 | 101 ns: 1.74x faster                                                      |
| raytrace                 | 464 ms                                                 | 267 ms: 1.74x faster                                                      |
| crypto_pyaes             | 118 ms                                                 | 69.4 ms: 1.71x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                                    |
| richards_super           | 90.7 ms                                                | 53.8 ms: 1.69x faster                                                     |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                      |
| scimark_sor              | 197 ms                                                 | 120 ms: 1.64x faster                                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 67.1 ms: 1.61x faster                                                     |
| hexiom                   | 9.53 ms                                                | 5.93 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                                     |
| richards                 | 74.9 ms                                                | 48.2 ms: 1.55x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 294 us: 1.55x faster                                                      |
| float                    | 111 ms                                                 | 71.9 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.53x faster                                                     |
| python_startup           | 14.2 ms                                                | 9.28 ms: 1.53x faster                                                     |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                      |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 46.2 ns: 1.40x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.75 ms: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.38x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.09 sec: 1.38x faster                                                    |
| logging_simple           | 8.07 us                                                | 5.88 us: 1.37x faster                                                     |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                     |
| tornado_http             | 127 ms                                                 | 93.5 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.1 us: 1.33x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.39 sec: 1.32x faster                                                    |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.30x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.28 sec: 1.28x faster                                                    |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                      |
| nqueens                  | 100 ms                                                 | 79.9 ms: 1.25x faster                                                     |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                     |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 93.8 ms: 1.19x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.22 us: 1.19x faster                                                     |
| scimark_fft              | 424 ms                                                 | 357 ms: 1.19x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.43 ms: 1.17x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 141 ms: 1.16x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.74 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                                      |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.6 us: 1.13x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                                    |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.11x faster                                                     |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.07x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 210 ms: 1.05x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.78 ms: 1.02x faster                                                     |
| pickle_list              | 4.56 us                                                | 4.51 us: 1.01x faster                                                     |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle                   | 10.3 us                                                | 10.4 us: 1.01x slower                                                     |
| unpickle_list            | 4.82 us                                                | 5.08 us: 1.05x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.46 ms: 1.07x slower                                                     |
| pickle_dict              | 27.3 us                                                | 30.9 us: 1.13x slower                                                     |
| dask                     | 423 ms                                                 | 489 ms: 1.16x slower                                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.81 ms: 1.17x slower                                                     |
| telco                    | 6.54 ms                                                | 7.92 ms: 1.21x slower                                                     |
| coverage                 | 72.8 ms                                                | 92.8 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, async_generators
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
