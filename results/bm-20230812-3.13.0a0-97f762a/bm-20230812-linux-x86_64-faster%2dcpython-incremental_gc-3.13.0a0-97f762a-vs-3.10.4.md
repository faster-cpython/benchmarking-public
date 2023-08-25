
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 97f762a
- commit date: 2023-08-12
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.44 sec: 1.30x faster                                                    |
| tornado_http   | 127 ms                                                 | 92.7 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.6 ms: 1.58x faster                                                     |
| float          | 111 ms                                                 | 77.8 ms: 1.42x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 294 us: 1.55x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| xml_etree_generate   | 94.2 ms                                                | 83.2 ms: 1.13x faster                                                     |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.62 us: 1.01x slower                                                     |
| xml_etree_parse      | 163 ms                                                 | 166 ms: 1.02x slower                                                      |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| unpickle             | 14.1 us                                                | 14.8 us: 1.04x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-97f762a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.47x faster                                                      |
| generators               | 76.8 ms                                                | 30.9 ms: 2.48x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 730 ms: 2.43x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.13 ms: 2.37x faster                                                     |
| async_tree_memoization   | 854 ms                                                 | 406 ms: 2.10x faster                                                      |
| async_tree_none          | 717 ms                                                 | 342 ms: 2.10x faster                                                      |
| asyncio_tcp              | 925 ms                                                 | 486 ms: 1.90x faster                                                      |
| chaos                    | 106 ms                                                 | 58.7 ms: 1.81x faster                                                     |
| logging_silent           | 175 ns                                                 | 99.7 ns: 1.76x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 68.3 ms: 1.74x faster                                                     |
| richards_super           | 90.7 ms                                                | 52.8 ms: 1.72x faster                                                     |
| raytrace                 | 464 ms                                                 | 271 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 577 ms: 1.65x faster                                                      |
| go                       | 229 ms                                                 | 139 ms: 1.64x faster                                                      |
| richards                 | 74.9 ms                                                | 46.2 ms: 1.62x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 66.9 ms: 1.62x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 89.6 ms: 1.58x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.05 ms: 1.57x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 294 us: 1.55x faster                                                      |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.54x faster                                                     |
| pyflate                  | 673 ms                                                 | 441 ms: 1.53x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 42.7 ns: 1.52x faster                                                     |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                     |
| float                    | 111 ms                                                 | 77.8 ms: 1.42x faster                                                     |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.41x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.40x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                     |
| logging_format           | 8.91 us                                                | 6.47 us: 1.38x faster                                                     |
| tornado_http             | 127 ms                                                 | 92.7 ms: 1.37x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.91 us: 1.37x faster                                                     |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 57.6 ms: 1.30x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.44 sec: 1.30x faster                                                    |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.18 sec: 1.27x faster                                                    |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                                    |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                      |
| fannkuch                 | 486 ms                                                 | 392 ms: 1.24x faster                                                      |
| nqueens                  | 100 ms                                                 | 81.3 ms: 1.23x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 53.3 ms: 1.23x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                                     |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                      |
| mypy2                    | 428 ms                                                 | 359 ms: 1.19x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.45 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.74 ms: 1.15x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 66.0 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 826 us: 1.15x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 83.2 ms: 1.13x faster                                                     |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.12x faster                                                    |
| json                     | 5.42 ms                                                | 4.87 ms: 1.11x faster                                                     |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.61 ms: 1.07x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 105 ms: 1.06x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.05x faster                                                     |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                      |
| pickle_list              | 4.56 us                                                | 4.62 us: 1.01x slower                                                     |
| xml_etree_parse          | 163 ms                                                 | 166 ms: 1.02x slower                                                      |
| async_generators         | 425 ms                                                 | 434 ms: 1.02x slower                                                      |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                     |
| unpickle_list            | 4.82 us                                                | 4.95 us: 1.03x slower                                                     |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.04x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.1 us: 1.14x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                     |
| dask                     | 423 ms                                                 | 495 ms: 1.17x slower                                                      |
| telco                    | 6.54 ms                                                | 7.98 ms: 1.22x slower                                                     |
| coverage                 | 72.8 ms                                                | 92.8 ms: 1.27x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
