
# Results vs. 3.10.4

- fork: faster-cpython
- ref: mini_super_ops
- machine: linux-x86_64
- commit hash: 0087a08
- commit date: 2023-05-26
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                    |
| tornado_http   | 127 ms                                                 | 96.1 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.7 ms: 1.60x faster                                                     |
| float          | 111 ms                                                 | 80.0 ms: 1.38x faster                                                     |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                     |
| regex_dna      | 222 ms                                                 | 216 ms: 1.02x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.85 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 306 us: 1.49x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 211 us: 1.42x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.91 ms: 1.37x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                     |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                      |
| unpickle_list        | 4.82 us                                                | 4.88 us: 1.01x slower                                                     |
| pickle_list          | 4.56 us                                                | 4.72 us: 1.04x slower                                                     |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                     |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230526-linux-x86_64-faster%2dcpython-mini_super_ops-3.13.0a0-0087a08 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 139 us: 3.67x faster                                                      |
| generators               | 76.8 ms                                                | 29.8 ms: 2.58x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.22 ms: 2.31x faster                                                     |
| richards_super           | 90.7 ms                                                | 49.6 ms: 1.83x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 511 ms: 1.81x faster                                                      |
| logging_silent           | 175 ns                                                 | 96.8 ns: 1.81x faster                                                     |
| richards                 | 74.9 ms                                                | 43.8 ms: 1.71x faster                                                     |
| chaos                    | 106 ms                                                 | 62.7 ms: 1.70x faster                                                     |
| scimark_sor              | 197 ms                                                 | 116 ms: 1.69x faster                                                      |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| go                       | 229 ms                                                 | 137 ms: 1.68x faster                                                      |
| hexiom                   | 9.53 ms                                                | 5.92 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 88.7 ms: 1.60x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                                     |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.24 ms: 1.53x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 77.7 ms: 1.52x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 71.3 ms: 1.52x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                     |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                      |
| pickle_pure_python       | 455 us                                                 | 306 us: 1.49x faster                                                      |
| coroutines               | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                     |
| async_tree_none          | 717 ms                                                 | 492 ms: 1.46x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                    |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.44x faster                                                      |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 597 ms: 1.43x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 211 us: 1.42x faster                                                      |
| deepcopy_memo            | 52.3 us                                                | 36.8 us: 1.42x faster                                                     |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                     |
| float                    | 111 ms                                                 | 80.0 ms: 1.38x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.91 ms: 1.37x faster                                                     |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                                    |
| logging_simple           | 8.07 us                                                | 6.00 us: 1.35x faster                                                     |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                    |
| unpack_sequence          | 64.7 ns                                                | 48.7 ns: 1.33x faster                                                     |
| comprehensions           | 26.8 us                                                | 20.2 us: 1.33x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 720 ms: 1.33x faster                                                      |
| tornado_http             | 127 ms                                                 | 96.1 ms: 1.33x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                    |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 733 ms: 1.30x faster                                                      |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| xml_etree_process        | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                     |
| deepcopy                 | 442 us                                                 | 345 us: 1.28x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                      |
| mypy2                    | 428 ms                                                 | 336 ms: 1.28x faster                                                      |
| fannkuch                 | 486 ms                                                 | 383 ms: 1.27x faster                                                      |
| nqueens                  | 100 ms                                                 | 78.9 ms: 1.27x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 52.5 ms: 1.24x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.23x faster                                                     |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                                      |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                    |
| dulwich_log              | 75.9 ms                                                | 64.8 ms: 1.17x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 817 us: 1.16x faster                                                      |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                     |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                                     |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                                    |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.90 ms: 1.11x faster                                                     |
| meteor_contest           | 115 ms                                                 | 103 ms: 1.11x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 84.7 ms: 1.11x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                     |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                      |
| regex_dna                | 222 ms                                                 | 216 ms: 1.02x faster                                                      |
| pidigits                 | 190 ms                                                 | 192 ms: 1.01x slower                                                      |
| unpickle_list            | 4.82 us                                                | 4.88 us: 1.01x slower                                                     |
| telco                    | 6.54 ms                                                | 6.77 ms: 1.03x slower                                                     |
| pickle_list              | 4.56 us                                                | 4.72 us: 1.04x slower                                                     |
| gc_traversal             | 3.84 ms                                                | 3.99 ms: 1.04x slower                                                     |
| async_generators         | 425 ms                                                 | 444 ms: 1.05x slower                                                      |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                     |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                     |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.18x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.85 ms: 1.19x slower                                                     |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                                      |
| coverage                 | 72.8 ms                                                | 95.4 ms: 1.31x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
