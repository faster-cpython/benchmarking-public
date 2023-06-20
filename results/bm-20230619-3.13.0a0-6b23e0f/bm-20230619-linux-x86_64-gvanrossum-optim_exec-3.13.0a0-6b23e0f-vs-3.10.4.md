
# Results vs. 3.10.4

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 6b23e0f
- commit date: 2023-06-19
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.65 sec: 1.20x faster                                          |
| tornado_http   | 127 ms                                                 | 96.4 ms: 1.32x faster                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.0 ms: 1.59x faster                                           |
| float          | 111 ms                                                 | 80.5 ms: 1.37x faster                                           |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                            |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                           |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                            |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 306 us: 1.49x faster                                            |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.41x faster                                            |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                          |
| xml_etree_process    | 74.9 ms                                                | 58.2 ms: 1.29x faster                                           |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                           |
| xml_etree_generate   | 94.2 ms                                                | 85.3 ms: 1.10x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                            |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                            |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                           |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                           |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                           |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                           |
| pickle_dict          | 27.3 us                                                | 31.5 us: 1.16x slower                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.20 ms: 1.54x faster                                           |
| python_startup_no_site | 5.82 ms                                                | 6.68 ms: 1.15x slower                                           |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.47x faster                                            |
| generators               | 76.8 ms                                                | 29.8 ms: 2.58x faster                                           |
| deltablue                | 7.42 ms                                                | 3.30 ms: 2.25x faster                                           |
| logging_silent           | 175 ns                                                 | 94.3 ns: 1.86x faster                                           |
| asyncio_tcp              | 925 ms                                                 | 506 ms: 1.83x faster                                            |
| richards_super           | 90.7 ms                                                | 50.2 ms: 1.81x faster                                           |
| chaos                    | 106 ms                                                 | 61.4 ms: 1.73x faster                                           |
| go                       | 229 ms                                                 | 135 ms: 1.70x faster                                            |
| richards                 | 74.9 ms                                                | 44.2 ms: 1.69x faster                                           |
| scimark_sor              | 197 ms                                                 | 117 ms: 1.68x faster                                            |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                          |
| raytrace                 | 464 ms                                                 | 290 ms: 1.60x faster                                            |
| nbody                    | 142 ms                                                 | 89.0 ms: 1.59x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 70.0 ms: 1.55x faster                                           |
| python_startup           | 14.2 ms                                                | 9.20 ms: 1.54x faster                                           |
| hexiom                   | 9.53 ms                                                | 6.22 ms: 1.53x faster                                           |
| pyflate                  | 673 ms                                                 | 444 ms: 1.51x faster                                            |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 78.5 ms: 1.51x faster                                           |
| pickle_pure_python       | 455 us                                                 | 306 us: 1.49x faster                                            |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.49x faster                                            |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                          |
| async_tree_none          | 717 ms                                                 | 485 ms: 1.48x faster                                            |
| async_tree_memoization   | 854 ms                                                 | 586 ms: 1.46x faster                                            |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.44x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.41x faster                                            |
| unpack_sequence          | 64.7 ns                                                | 46.8 ns: 1.38x faster                                           |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                           |
| spectral_norm            | 150 ms                                                 | 109 ms: 1.37x faster                                            |
| float                    | 111 ms                                                 | 80.5 ms: 1.37x faster                                           |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                           |
| logging_format           | 8.91 us                                                | 6.50 us: 1.37x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 38.2 us: 1.37x faster                                           |
| logging_simple           | 8.07 us                                                | 5.96 us: 1.35x faster                                           |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 713 ms: 1.34x faster                                            |
| pycparser                | 1.50 sec                                               | 1.13 sec: 1.33x faster                                          |
| tornado_http             | 127 ms                                                 | 96.4 ms: 1.32x faster                                           |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 728 ms: 1.31x faster                                            |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                            |
| xml_etree_process        | 74.9 ms                                                | 58.2 ms: 1.29x faster                                           |
| mypy2                    | 428 ms                                                 | 336 ms: 1.28x faster                                            |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                            |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                            |
| comprehensions           | 26.8 us                                                | 21.4 us: 1.26x faster                                           |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.13 us: 1.22x faster                                           |
| nqueens                  | 100 ms                                                 | 82.5 ms: 1.21x faster                                           |
| fannkuch                 | 486 ms                                                 | 401 ms: 1.21x faster                                            |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                            |
| docutils                 | 3.17 sec                                               | 2.65 sec: 1.20x faster                                          |
| dulwich_log              | 75.9 ms                                                | 64.9 ms: 1.17x faster                                           |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.15x faster                                           |
| bench_thread_pool        | 947 us                                                 | 833 us: 1.14x faster                                            |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                           |
| json                     | 5.42 ms                                                | 4.90 ms: 1.11x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 85.3 ms: 1.10x faster                                           |
| regex_dna                | 222 ms                                                 | 201 ms: 1.10x faster                                            |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.07 ms: 1.08x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                            |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                            |
| meteor_contest           | 115 ms                                                 | 108 ms: 1.06x faster                                            |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.06x faster                                           |
| pathlib                  | 20.0 ms                                                | 19.3 ms: 1.04x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.74 ms: 1.03x faster                                           |
| pickle_list              | 4.56 us                                                | 4.51 us: 1.01x faster                                           |
| unpickle_list            | 4.82 us                                                | 4.87 us: 1.01x slower                                           |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                            |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                           |
| telco                    | 6.54 ms                                                | 6.81 ms: 1.04x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.38 ms: 1.05x slower                                           |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                           |
| async_generators         | 425 ms                                                 | 465 ms: 1.09x slower                                            |
| python_startup_no_site   | 5.82 ms                                                | 6.68 ms: 1.15x slower                                           |
| pickle_dict              | 27.3 us                                                | 31.5 us: 1.16x slower                                           |
| dask                     | 423 ms                                                 | 519 ms: 1.23x slower                                            |
| coverage                 | 72.8 ms                                                | 93.8 ms: 1.29x slower                                           |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
