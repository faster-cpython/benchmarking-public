
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: af24cd7
- commit date: 2023-08-12
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark    | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|--------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tornado_http | 127 ms                                                 | 92.9 ms: 1.37x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.59x faster                                                     |
| float          | 111 ms                                                 | 76.8 ms: 1.44x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.73 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.56x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.39x faster                                                      |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                     |
| json_loads           | 28.8 us                                                | 25.4 us: 1.13x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                      |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| pickle_list          | 4.56 us                                                | 4.70 us: 1.03x slower                                                     |
| xml_etree_parse      | 163 ms                                                 | 168 ms: 1.03x slower                                                      |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                     |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.7 us: 1.20x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.29 ms: 1.52x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.51x faster                                                      |
| generators               | 76.8 ms                                                | 28.2 ms: 2.72x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 717 ms: 2.47x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.16 ms: 2.35x faster                                                     |
| async_tree_memoization   | 854 ms                                                 | 406 ms: 2.10x faster                                                      |
| async_tree_none          | 717 ms                                                 | 341 ms: 2.10x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 485 ms: 1.91x faster                                                      |
| chaos                    | 106 ms                                                 | 59.4 ms: 1.79x faster                                                     |
| logging_silent           | 175 ns                                                 | 98.1 ns: 1.78x faster                                                     |
| raytrace                 | 464 ms                                                 | 266 ms: 1.74x faster                                                      |
| richards_super           | 90.7 ms                                                | 53.3 ms: 1.70x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 69.6 ms: 1.70x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 138 ms: 1.67x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 575 ms: 1.66x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 66.1 ms: 1.64x faster                                                     |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 88.8 ms: 1.59x faster                                                     |
| richards                 | 74.9 ms                                                | 47.2 ms: 1.59x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.01 ms: 1.59x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 293 us: 1.56x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.58 ms: 1.54x faster                                                     |
| pyflate                  | 673 ms                                                 | 440 ms: 1.53x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.29 ms: 1.52x faster                                                     |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                                      |
| float                    | 111 ms                                                 | 76.8 ms: 1.44x faster                                                     |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                     |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                      |
| unpack_sequence          | 64.7 ns                                                | 46.0 ns: 1.41x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.39x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.39x faster                                                     |
| logging_format           | 8.91 us                                                | 6.44 us: 1.38x faster                                                     |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                     |
| tornado_http             | 127 ms                                                 | 92.9 ms: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                     |
| json_dumps               | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 716 ms: 1.33x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 57.3 ms: 1.31x faster                                                     |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| nqueens                  | 100 ms                                                 | 79.6 ms: 1.26x faster                                                     |
| deepcopy                 | 442 us                                                 | 356 us: 1.24x faster                                                      |
| fannkuch                 | 486 ms                                                 | 396 ms: 1.23x faster                                                      |
| sqlglot_optimize         | 65.3 ms                                                | 53.4 ms: 1.22x faster                                                     |
| scimark_fft              | 424 ms                                                 | 353 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                                     |
| mypy2                    | 428 ms                                                 | 359 ms: 1.20x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.44 ms: 1.16x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.73 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 66.5 ms: 1.14x faster                                                     |
| json_loads               | 28.8 us                                                | 25.4 us: 1.13x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 83.3 ms: 1.13x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                     |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.60 ms: 1.07x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.65 sec: 1.06x faster                                                    |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 105 ms: 1.06x faster                                                      |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| async_generators         | 425 ms                                                 | 437 ms: 1.03x slower                                                      |
| pickle_list              | 4.56 us                                                | 4.70 us: 1.03x slower                                                     |
| xml_etree_parse          | 163 ms                                                 | 168 ms: 1.03x slower                                                      |
| unpickle_list            | 4.82 us                                                | 5.08 us: 1.05x slower                                                     |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.73 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                     |
| dask                     | 423 ms                                                 | 499 ms: 1.18x slower                                                      |
| pickle_dict              | 27.3 us                                                | 32.7 us: 1.20x slower                                                     |
| telco                    | 6.54 ms                                                | 7.95 ms: 1.21x slower                                                     |
| coverage                 | 72.8 ms                                                | 92.6 ms: 1.27x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, docutils, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pycparser, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x
