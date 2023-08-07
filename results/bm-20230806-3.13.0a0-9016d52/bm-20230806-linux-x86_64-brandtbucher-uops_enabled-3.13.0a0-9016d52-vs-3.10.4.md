
# Results vs. 3.10.4

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.75 sec: 1.15x faster                                              |
| tornado_http   | 127 ms                                                 | 97.3 ms: 1.31x faster                                               |
| Geometric mean | (ref)                                                  | 1.23x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 96.6 ms: 1.47x faster                                               |
| float          | 111 ms                                                 | 84.5 ms: 1.31x faster                                               |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.22x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 152 ms: 1.17x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                               |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.51 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 300 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.98 ms: 1.36x faster                                               |
| unpickle_pure_python | 300 us                                                 | 224 us: 1.34x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 59.7 ms: 1.26x faster                                               |
| json_loads           | 28.8 us                                                | 25.5 us: 1.13x faster                                               |
| tomli_loads          | 2.92 sec                                               | 2.66 sec: 1.10x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 86.6 ms: 1.09x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                |
| pickle_list          | 4.56 us                                                | 4.60 us: 1.01x slower                                               |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                               |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                               |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                               |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                               |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.42 ms: 1.50x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.0 ms: 1.23x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 150 us: 3.41x faster                                                |
| generators               | 76.8 ms                                                | 29.0 ms: 2.64x faster                                               |
| deltablue                | 7.42 ms                                                | 3.63 ms: 2.04x faster                                               |
| asyncio_tcp              | 925 ms                                                 | 489 ms: 1.89x faster                                                |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                                |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                              |
| raytrace                 | 464 ms                                                 | 283 ms: 1.64x faster                                                |
| richards_super           | 90.7 ms                                                | 55.8 ms: 1.63x faster                                               |
| chaos                    | 106 ms                                                 | 66.3 ms: 1.60x faster                                               |
| crypto_pyaes             | 118 ms                                                 | 74.9 ms: 1.58x faster                                               |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.58x faster                                                |
| scimark_monte_carlo      | 108 ms                                                 | 68.9 ms: 1.57x faster                                               |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                               |
| go                       | 229 ms                                                 | 149 ms: 1.54x faster                                                |
| richards                 | 74.9 ms                                                | 48.9 ms: 1.53x faster                                               |
| pickle_pure_python       | 455 us                                                 | 300 us: 1.52x faster                                                |
| python_startup           | 14.2 ms                                                | 9.42 ms: 1.50x faster                                               |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.48x faster                                               |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                              |
| async_tree_none          | 717 ms                                                 | 489 ms: 1.47x faster                                                |
| nbody                    | 142 ms                                                 | 96.6 ms: 1.47x faster                                               |
| async_tree_memoization   | 854 ms                                                 | 594 ms: 1.44x faster                                                |
| scimark_lu               | 163 ms                                                 | 117 ms: 1.40x faster                                                |
| coroutines               | 31.8 ms                                                | 23.0 ms: 1.38x faster                                               |
| spectral_norm            | 150 ms                                                 | 110 ms: 1.36x faster                                                |
| json_dumps               | 13.5 ms                                                | 9.98 ms: 1.36x faster                                               |
| pyflate                  | 673 ms                                                 | 498 ms: 1.35x faster                                                |
| unpickle_pure_python     | 300 us                                                 | 224 us: 1.34x faster                                                |
| logging_format           | 8.91 us                                                | 6.66 us: 1.34x faster                                               |
| logging_simple           | 8.07 us                                                | 6.06 us: 1.33x faster                                               |
| tornado_http             | 127 ms                                                 | 97.3 ms: 1.31x faster                                               |
| float                    | 111 ms                                                 | 84.5 ms: 1.31x faster                                               |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 729 ms: 1.30x faster                                                |
| unpack_sequence          | 64.7 ns                                                | 49.8 ns: 1.30x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.53 sec: 1.30x faster                                              |
| pprint_safe_repr         | 955 ms                                                 | 744 ms: 1.28x faster                                                |
| xml_etree_process        | 74.9 ms                                                | 59.7 ms: 1.26x faster                                               |
| deepcopy_memo            | 52.3 us                                                | 41.8 us: 1.25x faster                                               |
| hexiom                   | 9.53 ms                                                | 7.60 ms: 1.25x faster                                               |
| mypy2                    | 428 ms                                                 | 346 ms: 1.24x faster                                                |
| pycparser                | 1.50 sec                                               | 1.21 sec: 1.24x faster                                              |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                                |
| deepcopy                 | 442 us                                                 | 360 us: 1.23x faster                                                |
| mako                     | 14.8 ms                                                | 12.0 ms: 1.23x faster                                               |
| deepcopy_reduce          | 3.82 us                                                | 3.20 us: 1.20x faster                                               |
| sqlglot_optimize         | 65.3 ms                                                | 55.2 ms: 1.18x faster                                               |
| regex_compile            | 177 ms                                                 | 152 ms: 1.17x faster                                                |
| docutils                 | 3.17 sec                                               | 2.75 sec: 1.15x faster                                              |
| json_loads               | 28.8 us                                                | 25.5 us: 1.13x faster                                               |
| dulwich_log              | 75.9 ms                                                | 67.6 ms: 1.12x faster                                               |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                               |
| json                     | 5.42 ms                                                | 4.83 ms: 1.12x faster                                               |
| scimark_fft              | 424 ms                                                 | 382 ms: 1.11x faster                                                |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                               |
| bench_thread_pool        | 947 us                                                 | 859 us: 1.10x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.66 sec: 1.10x faster                                              |
| comprehensions           | 26.8 us                                                | 24.6 us: 1.09x faster                                               |
| xml_etree_generate       | 94.2 ms                                                | 86.6 ms: 1.09x faster                                               |
| fannkuch                 | 486 ms                                                 | 455 ms: 1.07x faster                                                |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                                |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                                |
| sqlite_synth             | 2.93 us                                                | 2.81 us: 1.05x faster                                               |
| pathlib                  | 20.0 ms                                                | 19.2 ms: 1.04x faster                                               |
| mdp                      | 2.82 sec                                               | 2.73 sec: 1.04x faster                                              |
| nqueens                  | 100 ms                                                 | 98.8 ms: 1.01x faster                                               |
| pickle_list              | 4.56 us                                                | 4.60 us: 1.01x slower                                               |
| meteor_contest           | 115 ms                                                 | 116 ms: 1.01x slower                                                |
| gc_traversal             | 3.84 ms                                                | 3.93 ms: 1.02x slower                                               |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                               |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                               |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                               |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.84 ms: 1.07x slower                                               |
| regex_effbot             | 3.23 ms                                                | 3.51 ms: 1.09x slower                                               |
| async_generators         | 425 ms                                                 | 462 ms: 1.09x slower                                                |
| pickle_dict              | 27.3 us                                                | 32.1 us: 1.18x slower                                               |
| python_startup_no_site   | 5.82 ms                                                | 6.88 ms: 1.18x slower                                               |
| telco                    | 6.54 ms                                                | 7.93 ms: 1.21x slower                                               |
| dask                     | 423 ms                                                 | 532 ms: 1.26x slower                                                |
| coverage                 | 72.8 ms                                                | 92.3 ms: 1.27x slower                                               |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
