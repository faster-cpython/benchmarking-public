
# Results vs. 3.10.4

- fork: mdboom
- ref: bolt_experiment
- machine: linux-x86_64
- commit hash: b488f91
- commit date: 2023-05-05
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 270 ms: 1.24x faster                                              |
| docutils       | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                            |
| tornado_http   | 129 ms                                                              | 102 ms: 1.26x faster                                              |
| Geometric mean | (ref)                                                               | 1.22x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.7 ms: 1.66x faster                                             |
| float          | 110 ms                                                              | 81.6 ms: 1.35x faster                                             |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                               | 1.31x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.21x faster                                              |
| regex_v8       | 24.9 ms                                                             | 22.0 ms: 1.13x faster                                             |
| regex_dna      | 213 ms                                                              | 203 ms: 1.05x faster                                              |
| regex_effbot   | 3.22 ms                                                             | 3.81 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                               | 1.05x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 323 us: 1.41x faster                                              |
| json_dumps           | 13.7 ms                                                             | 9.92 ms: 1.38x faster                                             |
| unpickle_pure_python | 300 us                                                              | 220 us: 1.36x faster                                              |
| xml_etree_process    | 74.8 ms                                                             | 59.7 ms: 1.25x faster                                             |
| json_loads           | 29.3 us                                                             | 25.7 us: 1.14x faster                                             |
| xml_etree_generate   | 94.9 ms                                                             | 85.3 ms: 1.11x faster                                             |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                              |
| xml_etree_parse      | 164 ms                                                              | 154 ms: 1.06x faster                                              |
| pickle_list          | 4.73 us                                                             | 4.57 us: 1.04x faster                                             |
| unpickle_list        | 4.94 us                                                             | 4.88 us: 1.01x faster                                             |
| pickle               | 10.2 us                                                             | 10.6 us: 1.04x slower                                             |
| pickle_dict          | 27.8 us                                                             | 31.7 us: 1.14x slower                                             |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                             |
| python_startup_no_site | 5.80 ms                                                             | 6.67 ms: 1.15x slower                                             |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-----------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.9 ms: 1.35x faster                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230505-linux-x86_64-mdboom-bolt_experiment-3.12.0a7+-b488f91 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.7 ms: 2.46x faster                                             |
| deltablue               | 7.30 ms                                                             | 3.56 ms: 2.05x faster                                             |
| asyncio_tcp             | 922 ms                                                              | 510 ms: 1.81x faster                                              |
| richards                | 74.2 ms                                                             | 44.6 ms: 1.66x faster                                             |
| nbody                   | 146 ms                                                              | 87.7 ms: 1.66x faster                                             |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                              |
| logging_silent          | 169 ns                                                              | 104 ns: 1.62x faster                                              |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                              |
| python_startup          | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                             |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                             |
| raytrace                | 470 ms                                                              | 310 ms: 1.52x faster                                              |
| chaos                   | 106 ms                                                              | 69.8 ms: 1.52x faster                                             |
| pyflate                 | 671 ms                                                              | 447 ms: 1.50x faster                                              |
| hexiom                  | 9.50 ms                                                             | 6.41 ms: 1.48x faster                                             |
| scimark_monte_carlo     | 109 ms                                                              | 73.6 ms: 1.47x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                             |
| crypto_pyaes            | 117 ms                                                              | 80.4 ms: 1.45x faster                                             |
| async_tree_io           | 1.78 sec                                                            | 1.24 sec: 1.44x faster                                            |
| coroutines              | 31.8 ms                                                             | 22.2 ms: 1.43x faster                                             |
| async_tree_none         | 713 ms                                                              | 500 ms: 1.43x faster                                              |
| pickle_pure_python      | 457 us                                                              | 323 us: 1.41x faster                                              |
| unpack_sequence         | 65.6 ns                                                             | 46.6 ns: 1.41x faster                                             |
| async_tree_memoization  | 853 ms                                                              | 617 ms: 1.38x faster                                              |
| json_dumps              | 13.7 ms                                                             | 9.92 ms: 1.38x faster                                             |
| scimark_lu              | 160 ms                                                              | 116 ms: 1.38x faster                                              |
| unpickle_pure_python    | 300 us                                                              | 220 us: 1.36x faster                                              |
| spectral_norm           | 150 ms                                                              | 111 ms: 1.36x faster                                              |
| deepcopy_memo           | 51.8 us                                                             | 38.3 us: 1.35x faster                                             |
| mako                    | 14.7 ms                                                             | 10.9 ms: 1.35x faster                                             |
| float                   | 110 ms                                                              | 81.6 ms: 1.35x faster                                             |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.34x faster                                            |
| async_tree_cpu_io_mixed | 944 ms                                                              | 723 ms: 1.31x faster                                              |
| fannkuch                | 485 ms                                                              | 375 ms: 1.29x faster                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.53 sec: 1.29x faster                                            |
| logging_format          | 9.07 us                                                             | 7.12 us: 1.27x faster                                             |
| pprint_safe_repr        | 953 ms                                                              | 750 ms: 1.27x faster                                              |
| logging_simple          | 8.21 us                                                             | 6.47 us: 1.27x faster                                             |
| tornado_http            | 129 ms                                                              | 102 ms: 1.26x faster                                              |
| xml_etree_process       | 74.8 ms                                                             | 59.7 ms: 1.25x faster                                             |
| 2to3                    | 336 ms                                                              | 270 ms: 1.24x faster                                              |
| mypy2                   | 432 ms                                                              | 353 ms: 1.22x faster                                              |
| regex_compile           | 177 ms                                                              | 146 ms: 1.21x faster                                              |
| deepcopy                | 438 us                                                              | 363 us: 1.21x faster                                              |
| nqueens                 | 98.8 ms                                                             | 82.1 ms: 1.20x faster                                             |
| scimark_fft             | 425 ms                                                              | 355 ms: 1.20x faster                                              |
| deepcopy_reduce         | 3.80 us                                                             | 3.19 us: 1.19x faster                                             |
| sqlglot_normalize       | 135 ms                                                              | 113 ms: 1.19x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                             | 55.6 ms: 1.17x faster                                             |
| comprehensions          | 27.3 us                                                             | 23.3 us: 1.17x faster                                             |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.80 ms: 1.17x faster                                             |
| docutils                | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                            |
| json_loads              | 29.3 us                                                             | 25.7 us: 1.14x faster                                             |
| bench_thread_pool       | 954 us                                                              | 837 us: 1.14x faster                                              |
| regex_v8                | 24.9 ms                                                             | 22.0 ms: 1.13x faster                                             |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                              |
| dulwich_log             | 76.3 ms                                                             | 68.3 ms: 1.12x faster                                             |
| xml_etree_generate      | 94.9 ms                                                             | 85.3 ms: 1.11x faster                                             |
| create_gc_cycles        | 1.64 ms                                                             | 1.48 ms: 1.11x faster                                             |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                              |
| json                    | 5.41 ms                                                             | 4.94 ms: 1.10x faster                                             |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.3 ms: 1.09x faster                                             |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                              |
| sqlite_synth            | 2.97 us                                                             | 2.79 us: 1.07x faster                                             |
| xml_etree_parse         | 164 ms                                                              | 154 ms: 1.06x faster                                              |
| mdp                     | 2.75 sec                                                            | 2.61 sec: 1.05x faster                                            |
| pathlib                 | 19.8 ms                                                             | 18.8 ms: 1.05x faster                                             |
| regex_dna               | 213 ms                                                              | 203 ms: 1.05x faster                                              |
| pickle_list             | 4.73 us                                                             | 4.57 us: 1.04x faster                                             |
| unpickle_list           | 4.94 us                                                             | 4.88 us: 1.01x faster                                             |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                              |
| telco                   | 6.67 ms                                                             | 6.82 ms: 1.02x slower                                             |
| pickle                  | 10.2 us                                                             | 10.6 us: 1.04x slower                                             |
| gc_traversal            | 3.53 ms                                                             | 3.68 ms: 1.04x slower                                             |
| async_generators        | 420 ms                                                              | 459 ms: 1.09x slower                                              |
| pickle_dict             | 27.8 us                                                             | 31.7 us: 1.14x slower                                             |
| python_startup_no_site  | 5.80 ms                                                             | 6.67 ms: 1.15x slower                                             |
| regex_effbot            | 3.22 ms                                                             | 3.81 ms: 1.18x slower                                             |
| dask                    | 437 ms                                                              | 542 ms: 1.24x slower                                              |
| coverage                | 70.6 ms                                                             | 103 ms: 1.46x slower                                              |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
