
# Results vs. 3.10.4

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 6f7c955
- commit date: 2023-05-24
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                         |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                           |
| Geometric mean | (ref)                                                  | 1.20x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                          |
| float          | 111 ms                                                 | 80.4 ms: 1.38x faster                                          |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.28x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                           |
| regex_v8       | 25.0 ms                                                | 22.8 ms: 1.10x faster                                          |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.45x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.78 ms: 1.38x faster                                          |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                           |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 58.9 ms: 1.27x faster                                          |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 85.7 ms: 1.10x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                          |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                          |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                          |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.16x slower                                          |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.4 ms: 1.41x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 140 us: 3.65x faster                                           |
| generators               | 76.8 ms                                                | 31.1 ms: 2.47x faster                                          |
| deltablue                | 7.42 ms                                                | 3.46 ms: 2.15x faster                                          |
| richards_super           | 90.7 ms                                                | 50.0 ms: 1.81x faster                                          |
| logging_silent           | 175 ns                                                 | 97.2 ns: 1.80x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 515 ms: 1.80x faster                                           |
| go                       | 229 ms                                                 | 136 ms: 1.69x faster                                           |
| richards                 | 74.9 ms                                                | 44.6 ms: 1.68x faster                                          |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                         |
| chaos                    | 106 ms                                                 | 65.4 ms: 1.63x faster                                          |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                           |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                          |
| raytrace                 | 464 ms                                                 | 298 ms: 1.55x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                          |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                         |
| pyflate                  | 673 ms                                                 | 441 ms: 1.53x faster                                           |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                           |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                          |
| scimark_monte_carlo      | 108 ms                                                 | 71.5 ms: 1.51x faster                                          |
| async_tree_memoization   | 854 ms                                                 | 574 ms: 1.49x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                          |
| pickle_pure_python       | 455 us                                                 | 315 us: 1.45x faster                                           |
| mako                     | 14.8 ms                                                | 10.4 ms: 1.41x faster                                          |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                          |
| scimark_lu               | 163 ms                                                 | 116 ms: 1.41x faster                                           |
| json_dumps               | 13.5 ms                                                | 9.78 ms: 1.38x faster                                          |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.38x faster                                           |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                           |
| float                    | 111 ms                                                 | 80.4 ms: 1.38x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 38.2 us: 1.37x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 711 ms: 1.34x faster                                           |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 727 ms: 1.31x faster                                           |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                          |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.29x faster                                         |
| unpack_sequence          | 64.7 ns                                                | 50.4 ns: 1.28x faster                                          |
| fannkuch                 | 486 ms                                                 | 380 ms: 1.28x faster                                           |
| xml_etree_process        | 74.9 ms                                                | 58.9 ms: 1.27x faster                                          |
| logging_simple           | 8.07 us                                                | 6.37 us: 1.27x faster                                          |
| logging_format           | 8.91 us                                                | 7.10 us: 1.25x faster                                          |
| tornado_http             | 127 ms                                                 | 102 ms: 1.25x faster                                           |
| mypy2                    | 428 ms                                                 | 344 ms: 1.25x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                           |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                           |
| nqueens                  | 100 ms                                                 | 81.5 ms: 1.23x faster                                          |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                          |
| scimark_fft              | 424 ms                                                 | 351 ms: 1.21x faster                                           |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.16x faster                                         |
| json_loads               | 28.8 us                                                | 25.1 us: 1.15x faster                                          |
| bench_thread_pool        | 947 us                                                 | 831 us: 1.14x faster                                           |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.78 ms: 1.14x faster                                          |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                          |
| dulwich_log              | 75.9 ms                                                | 68.1 ms: 1.11x faster                                          |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.11x faster                                           |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 85.7 ms: 1.10x faster                                          |
| regex_v8                 | 25.0 ms                                                | 22.8 ms: 1.10x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                           |
| mdp                      | 2.82 sec                                               | 2.70 sec: 1.05x faster                                         |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.94 ms: 1.02x slower                                          |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                           |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                           |
| telco                    | 6.54 ms                                                | 6.88 ms: 1.05x slower                                          |
| unpickle_list            | 4.82 us                                                | 5.08 us: 1.05x slower                                          |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.64 ms: 1.13x slower                                          |
| pickle_dict              | 27.3 us                                                | 31.0 us: 1.14x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.16x slower                                          |
| dask                     | 423 ms                                                 | 536 ms: 1.27x slower                                           |
| coverage                 | 72.8 ms                                                | 97.5 ms: 1.34x slower                                          |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                   |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
