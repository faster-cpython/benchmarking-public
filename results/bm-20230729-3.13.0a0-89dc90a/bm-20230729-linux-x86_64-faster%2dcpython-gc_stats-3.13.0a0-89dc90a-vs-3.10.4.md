
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 89dc90a
- commit date: 2023-07-29
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                              |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.3 ms: 1.53x faster                                               |
| float          | 111 ms                                                 | 80.7 ms: 1.37x faster                                               |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.30x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.11x faster                                               |
| regex_dna      | 222 ms                                                 | 214 ms: 1.03x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 296 us: 1.54x faster                                                |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.76 ms: 1.39x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 57.8 ms: 1.30x faster                                               |
| tomli_loads          | 2.92 sec                                               | 2.33 sec: 1.25x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 83.9 ms: 1.12x faster                                               |
| json_loads           | 28.8 us                                                | 26.0 us: 1.11x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                |
| pickle_list          | 4.56 us                                                | 4.59 us: 1.01x slower                                               |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                               |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                               |
| unpickle             | 14.1 us                                                | 15.4 us: 1.09x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.36 ms: 1.51x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.84 ms: 1.18x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-89dc90a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.47x faster                                                |
| generators               | 76.8 ms                                                | 27.9 ms: 2.75x faster                                               |
| deltablue                | 7.42 ms                                                | 3.31 ms: 2.24x faster                                               |
| asyncio_tcp              | 925 ms                                                 | 476 ms: 1.94x faster                                                |
| chaos                    | 106 ms                                                 | 59.5 ms: 1.79x faster                                               |
| logging_silent           | 175 ns                                                 | 102 ns: 1.71x faster                                                |
| richards_super           | 90.7 ms                                                | 53.1 ms: 1.71x faster                                               |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                              |
| crypto_pyaes             | 118 ms                                                 | 70.7 ms: 1.68x faster                                               |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.66x faster                                                |
| richards                 | 74.9 ms                                                | 46.4 ms: 1.61x faster                                               |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.60x faster                                               |
| scimark_monte_carlo      | 108 ms                                                 | 67.8 ms: 1.60x faster                                               |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                               |
| pickle_pure_python       | 455 us                                                 | 296 us: 1.54x faster                                                |
| nbody                    | 142 ms                                                 | 92.3 ms: 1.53x faster                                               |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                               |
| python_startup           | 14.2 ms                                                | 9.36 ms: 1.51x faster                                               |
| scimark_lu               | 163 ms                                                 | 108 ms: 1.51x faster                                                |
| pyflate                  | 673 ms                                                 | 446 ms: 1.51x faster                                                |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.51x faster                                              |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.48x faster                                                |
| async_tree_memoization   | 854 ms                                                 | 582 ms: 1.47x faster                                                |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.45x faster                                               |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                |
| json_dumps               | 13.5 ms                                                | 9.76 ms: 1.39x faster                                               |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                               |
| float                    | 111 ms                                                 | 80.7 ms: 1.37x faster                                               |
| logging_format           | 8.91 us                                                | 6.54 us: 1.36x faster                                               |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                               |
| logging_simple           | 8.07 us                                                | 5.97 us: 1.35x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                              |
| tornado_http             | 127 ms                                                 | 95.2 ms: 1.34x faster                                               |
| pprint_safe_repr         | 955 ms                                                 | 721 ms: 1.32x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 720 ms: 1.32x faster                                                |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                               |
| xml_etree_process        | 74.9 ms                                                | 57.8 ms: 1.30x faster                                               |
| regex_compile            | 177 ms                                                 | 137 ms: 1.30x faster                                                |
| pycparser                | 1.50 sec                                               | 1.16 sec: 1.29x faster                                              |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| mypy2                    | 428 ms                                                 | 336 ms: 1.28x faster                                                |
| unpack_sequence          | 64.7 ns                                                | 51.1 ns: 1.27x faster                                               |
| tomli_loads              | 2.92 sec                                               | 2.33 sec: 1.25x faster                                              |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                                |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                               |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                |
| nqueens                  | 100 ms                                                 | 81.9 ms: 1.22x faster                                               |
| scimark_fft              | 424 ms                                                 | 352 ms: 1.20x faster                                                |
| deepcopy_reduce          | 3.82 us                                                | 3.19 us: 1.20x faster                                               |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                              |
| bench_thread_pool        | 947 us                                                 | 815 us: 1.16x faster                                                |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.70 ms: 1.16x faster                                               |
| dulwich_log              | 75.9 ms                                                | 65.8 ms: 1.15x faster                                               |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                               |
| xml_etree_generate       | 94.2 ms                                                | 83.9 ms: 1.12x faster                                               |
| json_loads               | 28.8 us                                                | 26.0 us: 1.11x faster                                               |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                              |
| regex_v8                 | 25.0 ms                                                | 22.7 ms: 1.11x faster                                               |
| json                     | 5.42 ms                                                | 4.95 ms: 1.09x faster                                               |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                               |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                               |
| regex_dna                | 222 ms                                                 | 214 ms: 1.03x faster                                                |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                               |
| pickle_list              | 4.56 us                                                | 4.59 us: 1.01x slower                                               |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                               |
| unpickle_list            | 4.82 us                                                | 4.97 us: 1.03x slower                                               |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| gc_traversal             | 3.84 ms                                                | 4.06 ms: 1.06x slower                                               |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                                |
| unpickle                 | 14.1 us                                                | 15.4 us: 1.09x slower                                               |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                               |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| python_startup_no_site   | 5.82 ms                                                | 6.84 ms: 1.18x slower                                               |
| telco                    | 6.54 ms                                                | 7.79 ms: 1.19x slower                                               |
| dask                     | 423 ms                                                 | 517 ms: 1.22x slower                                                |
| coverage                 | 72.8 ms                                                | 94.6 ms: 1.30x slower                                               |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                        |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x
