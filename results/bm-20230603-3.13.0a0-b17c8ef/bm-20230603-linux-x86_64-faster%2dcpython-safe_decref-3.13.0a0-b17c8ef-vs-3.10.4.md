
# Results vs. 3.10.4

- fork: faster-cpython
- ref: safe_decref
- machine: linux-x86_64
- commit hash: b17c8ef
- commit date: 2023-06-03
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                 |
| tornado_http   | 127 ms                                                 | 95.5 ms: 1.33x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.7 ms: 1.56x faster                                                  |
| float          | 111 ms                                                 | 76.6 ms: 1.44x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.10x faster                                                  |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.71 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 308 us: 1.48x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.67 ms: 1.40x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                   |
| tomli_loads          | 2.92 sec                                               | 2.15 sec: 1.36x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 57.0 ms: 1.31x faster                                                  |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 83.5 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                   |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.21 ms: 1.54x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.63x faster                                                   |
| generators               | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                  |
| deltablue                | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                  |
| logging_silent           | 175 ns                                                 | 94.9 ns: 1.85x faster                                                  |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                                   |
| richards_super           | 90.7 ms                                                | 50.2 ms: 1.81x faster                                                  |
| chaos                    | 106 ms                                                 | 60.9 ms: 1.74x faster                                                  |
| go                       | 229 ms                                                 | 133 ms: 1.72x faster                                                   |
| richards                 | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                 |
| scimark_sor              | 197 ms                                                 | 117 ms: 1.67x faster                                                   |
| raytrace                 | 464 ms                                                 | 288 ms: 1.61x faster                                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.00 ms: 1.59x faster                                                  |
| nbody                    | 142 ms                                                 | 90.7 ms: 1.56x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 76.8 ms: 1.54x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 70.4 ms: 1.54x faster                                                  |
| python_startup           | 14.2 ms                                                | 9.21 ms: 1.54x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.60 ms: 1.53x faster                                                  |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                                   |
| scimark_lu               | 163 ms                                                 | 108 ms: 1.52x faster                                                   |
| pickle_pure_python       | 455 us                                                 | 308 us: 1.48x faster                                                   |
| async_tree_none          | 717 ms                                                 | 489 ms: 1.47x faster                                                   |
| unpack_sequence          | 64.7 ns                                                | 44.4 ns: 1.46x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                 |
| spectral_norm            | 150 ms                                                 | 103 ms: 1.45x faster                                                   |
| float                    | 111 ms                                                 | 76.6 ms: 1.44x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 594 ms: 1.44x faster                                                   |
| json_dumps               | 13.5 ms                                                | 9.67 ms: 1.40x faster                                                  |
| coroutines               | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                   |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                  |
| deepcopy_memo            | 52.3 us                                                | 37.7 us: 1.39x faster                                                  |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                                  |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                                 |
| tomli_loads              | 2.92 sec                                               | 2.15 sec: 1.36x faster                                                 |
| tornado_http             | 127 ms                                                 | 95.5 ms: 1.33x faster                                                  |
| logging_simple           | 8.07 us                                                | 6.08 us: 1.33x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 720 ms: 1.33x faster                                                   |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                 |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 57.0 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 730 ms: 1.30x faster                                                   |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                                   |
| sqlglot_normalize        | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                                   |
| deepcopy                 | 442 us                                                 | 350 us: 1.26x faster                                                   |
| nqueens                  | 100 ms                                                 | 79.4 ms: 1.26x faster                                                  |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                   |
| sqlglot_optimize         | 65.3 ms                                                | 52.4 ms: 1.25x faster                                                  |
| scimark_fft              | 424 ms                                                 | 348 ms: 1.22x faster                                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.67 sec: 1.19x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 64.7 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.71 ms: 1.16x faster                                                  |
| bench_thread_pool        | 947 us                                                 | 818 us: 1.16x faster                                                   |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 83.5 ms: 1.13x faster                                                  |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 22.9 ms: 1.10x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.3 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| sqlite_synth             | 2.93 us                                                | 2.76 us: 1.06x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                                   |
| mdp                      | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                 |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                                   |
| pidigits                 | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                  |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                                   |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| telco                    | 6.54 ms                                                | 6.96 ms: 1.06x slower                                                  |
| pickle_dict              | 27.3 us                                                | 30.4 us: 1.12x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.71 ms: 1.15x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| dask                     | 423 ms                                                 | 512 ms: 1.21x slower                                                   |
| coverage                 | 72.8 ms                                                | 95.5 ms: 1.31x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (3): gc_traversal, bench_mp_pool, pickle_list
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
