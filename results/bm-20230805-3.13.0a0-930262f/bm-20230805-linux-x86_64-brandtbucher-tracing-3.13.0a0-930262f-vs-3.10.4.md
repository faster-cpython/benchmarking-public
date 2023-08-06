
# Results vs. 3.10.4

- fork: brandtbucher
- ref: tracing
- machine: linux-x86_64
- commit hash: 930262f
- commit date: 2023-08-05
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.79 sec: 1.14x faster                                         |
| tornado_http   | 127 ms                                                 | 98.2 ms: 1.30x faster                                          |
| Geometric mean | (ref)                                                  | 1.22x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 111 ms                                                 | 85.2 ms: 1.30x faster                                          |
| nbody          | 142 ms                                                 | 112 ms: 1.27x faster                                           |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                          |
| regex_compile  | 177 ms                                                 | 156 ms: 1.13x faster                                           |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 303 us: 1.50x faster                                           |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.35x faster                                          |
| unpickle_pure_python | 300 us                                                 | 225 us: 1.34x faster                                           |
| xml_etree_process    | 74.9 ms                                                | 59.7 ms: 1.25x faster                                          |
| json_loads           | 28.8 us                                                | 25.4 us: 1.14x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.66 sec: 1.10x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 86.1 ms: 1.09x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                           |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                          |
| pickle               | 10.3 us                                                | 10.8 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                          |
| unpickle_list        | 4.82 us                                                | 5.30 us: 1.10x slower                                          |
| pickle_dict          | 27.3 us                                                | 32.8 us: 1.20x slower                                          |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.52x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.83 ms: 1.17x slower                                          |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.4 ms: 1.19x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-brandtbucher-tracing-3.13.0a0-930262f |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 154 us: 3.31x faster                                           |
| generators               | 76.8 ms                                                | 28.9 ms: 2.66x faster                                          |
| deltablue                | 7.42 ms                                                | 3.47 ms: 2.14x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 492 ms: 1.88x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.81 sec: 1.66x faster                                         |
| logging_silent           | 175 ns                                                 | 106 ns: 1.65x faster                                           |
| richards_super           | 90.7 ms                                                | 55.7 ms: 1.63x faster                                          |
| raytrace                 | 464 ms                                                 | 288 ms: 1.61x faster                                           |
| scimark_sor              | 197 ms                                                 | 126 ms: 1.57x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 69.5 ms: 1.56x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                          |
| go                       | 229 ms                                                 | 149 ms: 1.54x faster                                           |
| crypto_pyaes             | 118 ms                                                 | 77.0 ms: 1.54x faster                                          |
| richards                 | 74.9 ms                                                | 49.1 ms: 1.53x faster                                          |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.52x faster                                          |
| pickle_pure_python       | 455 us                                                 | 303 us: 1.50x faster                                           |
| chaos                    | 106 ms                                                 | 71.2 ms: 1.49x faster                                          |
| coroutines               | 31.8 ms                                                | 21.5 ms: 1.48x faster                                          |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                         |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                          |
| async_tree_none          | 717 ms                                                 | 493 ms: 1.45x faster                                           |
| async_tree_memoization   | 854 ms                                                 | 602 ms: 1.42x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 46.1 ns: 1.41x faster                                          |
| scimark_lu               | 163 ms                                                 | 119 ms: 1.37x faster                                           |
| spectral_norm            | 150 ms                                                 | 111 ms: 1.35x faster                                           |
| json_dumps               | 13.5 ms                                                | 10.1 ms: 1.35x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 225 us: 1.34x faster                                           |
| logging_simple           | 8.07 us                                                | 6.18 us: 1.31x faster                                          |
| tornado_http             | 127 ms                                                 | 98.2 ms: 1.30x faster                                          |
| float                    | 111 ms                                                 | 85.2 ms: 1.30x faster                                          |
| logging_format           | 8.91 us                                                | 6.89 us: 1.29x faster                                          |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 736 ms: 1.29x faster                                           |
| nbody                    | 142 ms                                                 | 112 ms: 1.27x faster                                           |
| pyflate                  | 673 ms                                                 | 533 ms: 1.26x faster                                           |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.26x faster                                         |
| pprint_pformat           | 1.99 sec                                               | 1.58 sec: 1.25x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 59.7 ms: 1.25x faster                                          |
| pprint_safe_repr         | 955 ms                                                 | 771 ms: 1.24x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                           |
| deepcopy_memo            | 52.3 us                                                | 42.9 us: 1.22x faster                                          |
| mypy2                    | 428 ms                                                 | 354 ms: 1.21x faster                                           |
| deepcopy                 | 442 us                                                 | 367 us: 1.20x faster                                           |
| hexiom                   | 9.53 ms                                                | 7.93 ms: 1.20x faster                                          |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                          |
| mako                     | 14.8 ms                                                | 12.4 ms: 1.19x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 55.4 ms: 1.18x faster                                          |
| regex_v8                 | 25.0 ms                                                | 21.6 ms: 1.16x faster                                          |
| docutils                 | 3.17 sec                                               | 2.79 sec: 1.14x faster                                         |
| json_loads               | 28.8 us                                                | 25.4 us: 1.14x faster                                          |
| regex_compile            | 177 ms                                                 | 156 ms: 1.13x faster                                           |
| json                     | 5.42 ms                                                | 4.80 ms: 1.13x faster                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                          |
| dulwich_log              | 75.9 ms                                                | 69.0 ms: 1.10x faster                                          |
| tomli_loads              | 2.92 sec                                               | 2.66 sec: 1.10x faster                                         |
| bench_thread_pool        | 947 us                                                 | 866 us: 1.09x faster                                           |
| xml_etree_generate       | 94.2 ms                                                | 86.1 ms: 1.09x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                           |
| regex_dna                | 222 ms                                                 | 208 ms: 1.07x faster                                           |
| comprehensions           | 26.8 us                                                | 25.3 us: 1.06x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.9 ms: 1.06x faster                                          |
| sqlite_synth             | 2.93 us                                                | 2.79 us: 1.05x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                           |
| scimark_fft              | 424 ms                                                 | 404 ms: 1.05x faster                                           |
| mdp                      | 2.82 sec                                               | 2.71 sec: 1.04x faster                                         |
| nqueens                  | 100 ms                                                 | 101 ms: 1.01x slower                                           |
| fannkuch                 | 486 ms                                                 | 490 ms: 1.01x slower                                           |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                          |
| pickle                   | 10.3 us                                                | 10.8 us: 1.04x slower                                          |
| meteor_contest           | 115 ms                                                 | 120 ms: 1.05x slower                                           |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                          |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                           |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.79 ms: 1.06x slower                                          |
| async_generators         | 425 ms                                                 | 466 ms: 1.10x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.54 ms: 1.10x slower                                          |
| unpickle_list            | 4.82 us                                                | 5.30 us: 1.10x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.83 ms: 1.17x slower                                          |
| telco                    | 6.54 ms                                                | 7.80 ms: 1.19x slower                                          |
| pickle_dict              | 27.3 us                                                | 32.8 us: 1.20x slower                                          |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                           |
| coverage                 | 72.8 ms                                                | 94.5 ms: 1.30x slower                                          |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
