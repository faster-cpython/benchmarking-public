
# Results vs. 3.10.4

- fork: python
- ref: f73abf8e03fd370c86fb
- machine: linux-x86_64
- commit hash: f73abf8
- commit date: 2023-05-01
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 268 ms: 1.25x faster                                                   |
| docutils       | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                 |
| html5lib       | 86.4 ms                                                             | 65.0 ms: 1.33x faster                                                  |
| tornado_http   | 129 ms                                                              | 98.5 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                               | 1.27x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 89.2 ms: 1.63x faster                                                  |
| float          | 110 ms                                                              | 82.0 ms: 1.34x faster                                                  |
| pidigits       | 190 ms                                                              | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                               | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 144 ms: 1.23x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| regex_dna      | 213 ms                                                              | 210 ms: 1.01x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.44 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 319 us: 1.43x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 217 us: 1.38x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 58.2 ms: 1.29x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.8 us: 1.13x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 84.0 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 152 ms: 1.07x faster                                                   |
| pickle               | 10.2 us                                                             | 10.3 us: 1.01x slower                                                  |
| pickle_list          | 4.73 us                                                             | 4.79 us: 1.01x slower                                                  |
| unpickle_list        | 4.94 us                                                             | 5.19 us: 1.05x slower                                                  |
| unpickle             | 15.0 us                                                             | 15.7 us: 1.05x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 32.3 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.06 ms: 1.56x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.65 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                  |
| genshi_text    | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                  |
| genshi_xml     | 64.3 ms                                                             | 50.5 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                               | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.0 ms: 2.44x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.54 ms: 2.06x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 511 ms: 1.81x faster                                                   |
| richards                | 74.2 ms                                                             | 43.3 ms: 1.71x faster                                                  |
| logging_silent          | 169 ns                                                              | 101 ns: 1.67x faster                                                   |
| go                      | 226 ms                                                              | 136 ms: 1.65x faster                                                   |
| nbody                   | 146 ms                                                              | 89.2 ms: 1.63x faster                                                  |
| scimark_sor             | 198 ms                                                              | 126 ms: 1.56x faster                                                   |
| python_startup          | 14.1 ms                                                             | 9.06 ms: 1.56x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.33 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                              | 68.6 ms: 1.54x faster                                                  |
| raytrace                | 470 ms                                                              | 306 ms: 1.54x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 6.22 ms: 1.53x faster                                                  |
| pyflate                 | 671 ms                                                              | 444 ms: 1.51x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.65 ms: 1.49x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 73.0 ms: 1.49x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 79.5 ms: 1.47x faster                                                  |
| spectral_norm           | 150 ms                                                              | 102 ms: 1.47x faster                                                   |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 319 us: 1.43x faster                                                   |
| async_tree_none         | 713 ms                                                              | 499 ms: 1.43x faster                                                   |
| scimark_lu              | 160 ms                                                              | 114 ms: 1.41x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 614 ms: 1.39x faster                                                   |
| coroutines              | 31.8 ms                                                             | 23.0 ms: 1.38x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 217 us: 1.38x faster                                                   |
| unpack_sequence         | 65.6 ns                                                             | 47.5 ns: 1.38x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 10.1 ms: 1.36x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                  |
| genshi_text             | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                  |
| float                   | 110 ms                                                              | 82.0 ms: 1.34x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.33x faster                                                 |
| html5lib                | 86.4 ms                                                             | 65.0 ms: 1.33x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 39.0 us: 1.33x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.50 sec: 1.32x faster                                                 |
| tornado_http            | 129 ms                                                              | 98.5 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 722 ms: 1.31x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.28 us: 1.31x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.95 us: 1.31x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 733 ms: 1.30x faster                                                   |
| fannkuch                | 485 ms                                                              | 374 ms: 1.30x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 58.2 ms: 1.29x faster                                                  |
| thrift                  | 1.04 ms                                                             | 811 us: 1.28x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 50.5 ms: 1.27x faster                                                  |
| 2to3                    | 336 ms                                                              | 268 ms: 1.25x faster                                                   |
| mypy2                   | 432 ms                                                              | 349 ms: 1.24x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 80.1 ms: 1.23x faster                                                  |
| regex_compile           | 177 ms                                                              | 144 ms: 1.23x faster                                                   |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                   |
| deepcopy                | 438 us                                                              | 363 us: 1.21x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 54.5 ms: 1.20x faster                                                  |
| scimark_fft             | 425 ms                                                              | 356 ms: 1.20x faster                                                   |
| deepcopy_reduce         | 3.80 us                                                             | 3.20 us: 1.19x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                 |
| comprehensions          | 27.3 us                                                             | 23.4 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.83 ms: 1.16x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 834 us: 1.14x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                   |
| json_loads              | 29.3 us                                                             | 25.8 us: 1.13x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.7 ms: 1.13x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 84.0 ms: 1.13x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 22.1 ms: 1.13x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 67.7 ms: 1.13x faster                                                  |
| pathlib                 | 19.8 ms                                                             | 17.7 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.70 us: 1.10x faster                                                  |
| json                    | 5.41 ms                                                             | 4.98 ms: 1.09x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 152 ms: 1.07x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.61 sec: 1.06x faster                                                 |
| meteor_contest          | 115 ms                                                              | 113 ms: 1.01x faster                                                   |
| regex_dna               | 213 ms                                                              | 210 ms: 1.01x faster                                                   |
| pickle                  | 10.2 us                                                             | 10.3 us: 1.01x slower                                                  |
| pickle_list             | 4.73 us                                                             | 4.79 us: 1.01x slower                                                  |
| telco                   | 6.67 ms                                                             | 6.76 ms: 1.01x slower                                                  |
| pidigits                | 190 ms                                                              | 198 ms: 1.04x slower                                                   |
| unpickle_list           | 4.94 us                                                             | 5.19 us: 1.05x slower                                                  |
| unpickle                | 15.0 us                                                             | 15.7 us: 1.05x slower                                                  |
| async_generators        | 420 ms                                                              | 442 ms: 1.05x slower                                                   |
| regex_effbot            | 3.22 ms                                                             | 3.44 ms: 1.07x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.94 ms: 1.12x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.65 ms: 1.15x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 32.3 us: 1.16x slower                                                  |
| dask                    | 437 ms                                                              | 539 ms: 1.23x slower                                                   |
| coverage                | 70.6 ms                                                             | 102 ms: 1.44x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.25x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
