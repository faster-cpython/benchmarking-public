
# Results vs. 3.10.4

- fork: faster-cpython
- ref: tweak_ints_monitorin
- machine: linux-x86_64
- commit hash: 0ccd3bb
- commit date: 2023-08-05
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                          |
| tornado_http   | 127 ms                                                 | 95.6 ms: 1.33x faster                                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.7 ms: 1.48x faster                                                           |
| float          | 111 ms                                                 | 81.1 ms: 1.36x faster                                                           |
| pidigits       | 190 ms                                                 | 200 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                            |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                           |
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                            |
| json_dumps           | 13.5 ms                                                | 9.81 ms: 1.38x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 57.8 ms: 1.30x faster                                                           |
| tomli_loads          | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                          |
| xml_etree_generate   | 94.2 ms                                                | 83.6 ms: 1.13x faster                                                           |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                            |
| unpickle_list        | 4.82 us                                                | 4.85 us: 1.01x slower                                                           |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                           |
| pickle_list          | 4.56 us                                                | 4.79 us: 1.05x slower                                                           |
| pickle               | 10.3 us                                                | 10.9 us: 1.06x slower                                                           |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.38 ms: 1.51x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.86 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230805-linux-x86_64-faster%2dcpython-tweak_ints_monitorin-3.13.0a0-0ccd3bb |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 142 us: 3.60x faster                                                            |
| generators               | 76.8 ms                                                | 28.4 ms: 2.70x faster                                                           |
| deltablue                | 7.42 ms                                                | 3.18 ms: 2.33x faster                                                           |
| asyncio_tcp              | 925 ms                                                 | 482 ms: 1.92x faster                                                            |
| chaos                    | 106 ms                                                 | 59.2 ms: 1.80x faster                                                           |
| raytrace                 | 464 ms                                                 | 266 ms: 1.74x faster                                                            |
| crypto_pyaes             | 118 ms                                                 | 70.3 ms: 1.68x faster                                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                          |
| richards_super           | 90.7 ms                                                | 53.9 ms: 1.68x faster                                                           |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                            |
| logging_silent           | 175 ns                                                 | 106 ns: 1.65x faster                                                            |
| scimark_sor              | 197 ms                                                 | 122 ms: 1.61x faster                                                            |
| scimark_monte_carlo      | 108 ms                                                 | 68.2 ms: 1.59x faster                                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                                           |
| hexiom                   | 9.53 ms                                                | 6.07 ms: 1.57x faster                                                           |
| richards                 | 74.9 ms                                                | 48.0 ms: 1.56x faster                                                           |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                                            |
| unpack_sequence          | 64.7 ns                                                | 42.4 ns: 1.53x faster                                                           |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                                            |
| sqlglot_transpile        | 2.45 ms                                                | 1.62 ms: 1.51x faster                                                           |
| python_startup           | 14.2 ms                                                | 9.38 ms: 1.51x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.50x faster                                                          |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.48x faster                                                            |
| nbody                    | 142 ms                                                 | 95.7 ms: 1.48x faster                                                           |
| scimark_lu               | 163 ms                                                 | 111 ms: 1.47x faster                                                            |
| async_tree_memoization   | 854 ms                                                 | 589 ms: 1.45x faster                                                            |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.45x faster                                                           |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                            |
| json_dumps               | 13.5 ms                                                | 9.81 ms: 1.38x faster                                                           |
| spectral_norm            | 150 ms                                                 | 109 ms: 1.37x faster                                                            |
| deepcopy_memo            | 52.3 us                                                | 38.2 us: 1.37x faster                                                           |
| float                    | 111 ms                                                 | 81.1 ms: 1.36x faster                                                           |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                           |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                          |
| logging_simple           | 8.07 us                                                | 6.02 us: 1.34x faster                                                           |
| pprint_safe_repr         | 955 ms                                                 | 715 ms: 1.34x faster                                                            |
| logging_format           | 8.91 us                                                | 6.68 us: 1.33x faster                                                           |
| tornado_http             | 127 ms                                                 | 95.6 ms: 1.33x faster                                                           |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 724 ms: 1.31x faster                                                            |
| xml_etree_process        | 74.9 ms                                                | 57.8 ms: 1.30x faster                                                           |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                          |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                            |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                            |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                            |
| tomli_loads              | 2.92 sec                                               | 2.32 sec: 1.26x faster                                                          |
| nqueens                  | 100 ms                                                 | 79.8 ms: 1.25x faster                                                           |
| fannkuch                 | 486 ms                                                 | 389 ms: 1.25x faster                                                            |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                                            |
| sqlglot_optimize         | 65.3 ms                                                | 52.6 ms: 1.24x faster                                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                           |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.65 ms: 1.17x faster                                                           |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                                           |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                           |
| bench_thread_pool        | 947 us                                                 | 824 us: 1.15x faster                                                            |
| scimark_fft              | 424 ms                                                 | 372 ms: 1.14x faster                                                            |
| xml_etree_generate       | 94.2 ms                                                | 83.6 ms: 1.13x faster                                                           |
| json_loads               | 28.8 us                                                | 25.7 us: 1.12x faster                                                           |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                          |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.10x faster                                                           |
| json                     | 5.42 ms                                                | 4.92 ms: 1.10x faster                                                           |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                            |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.09x faster                                                            |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                           |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                            |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                                           |
| regex_dna                | 222 ms                                                 | 213 ms: 1.04x faster                                                            |
| unpickle_list            | 4.82 us                                                | 4.85 us: 1.01x slower                                                           |
| gc_traversal             | 3.84 ms                                                | 3.94 ms: 1.03x slower                                                           |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                                           |
| pickle_list              | 4.56 us                                                | 4.79 us: 1.05x slower                                                           |
| pidigits                 | 190 ms                                                 | 200 ms: 1.06x slower                                                            |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                                            |
| pickle                   | 10.3 us                                                | 10.9 us: 1.06x slower                                                           |
| regex_effbot             | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                           |
| python_startup_no_site   | 5.82 ms                                                | 6.86 ms: 1.18x slower                                                           |
| pickle_dict              | 27.3 us                                                | 32.3 us: 1.19x slower                                                           |
| telco                    | 6.54 ms                                                | 7.81 ms: 1.19x slower                                                           |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                            |
| coverage                 | 72.8 ms                                                | 94.3 ms: 1.30x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
