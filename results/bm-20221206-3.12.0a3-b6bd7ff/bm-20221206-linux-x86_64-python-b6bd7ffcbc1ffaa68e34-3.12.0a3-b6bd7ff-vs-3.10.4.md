
# Results vs. 3.10.4

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: linux-x86_64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 246 ms: 1.37x faster                                                  |
| chameleon      | 9.13 ms                                                             | 6.45 ms: 1.42x faster                                                 |
| docutils       | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                                |
| html5lib       | 86.4 ms                                                             | 59.7 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                               | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 94.0 ms: 1.55x faster                                                 |
| float          | 110 ms                                                              | 73.2 ms: 1.50x faster                                                 |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                               | 1.33x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 129 ms: 1.38x faster                                                  |
| regex_v8       | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                 |
| regex_dna      | 213 ms                                                              | 217 ms: 1.02x slower                                                  |
| regex_effbot   | 3.22 ms                                                             | 3.63 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                               | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 282 us: 1.62x faster                                                  |
| unpickle_pure_python | 300 us                                                              | 200 us: 1.50x faster                                                  |
| json_dumps           | 13.7 ms                                                             | 9.52 ms: 1.44x faster                                                 |
| xml_etree_process    | 74.8 ms                                                             | 53.7 ms: 1.39x faster                                                 |
| xml_etree_generate   | 94.9 ms                                                             | 76.9 ms: 1.23x faster                                                 |
| json_loads           | 29.3 us                                                             | 23.8 us: 1.23x faster                                                 |
| pickle_list          | 4.73 us                                                             | 3.95 us: 1.20x faster                                                 |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.12x faster                                                 |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                  |
| pickle               | 10.2 us                                                             | 10.1 us: 1.01x faster                                                 |
| unpickle_list        | 4.94 us                                                             | 4.97 us: 1.01x slower                                                 |
| pickle_dict          | 27.8 us                                                             | 31.5 us: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.52 ms: 1.66x faster                                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.07 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.43 ms: 1.56x faster                                                 |
| genshi_text     | 30.4 ms                                                             | 20.9 ms: 1.46x faster                                                 |
| django_template | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                 |
| genshi_xml      | 64.3 ms                                                             | 48.0 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                               | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221206-linux-x86_64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.22 ms: 2.27x faster                                                 |
| scimark_sor             | 198 ms                                                              | 105 ms: 1.88x faster                                                  |
| logging_silent          | 169 ns                                                              | 90.9 ns: 1.86x faster                                                 |
| richards                | 74.2 ms                                                             | 42.0 ms: 1.77x faster                                                 |
| raytrace                | 470 ms                                                              | 281 ms: 1.68x faster                                                  |
| go                      | 226 ms                                                              | 136 ms: 1.67x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 65.4 ms: 1.66x faster                                                 |
| python_startup          | 14.1 ms                                                             | 8.52 ms: 1.66x faster                                                 |
| pyflate                 | 671 ms                                                              | 405 ms: 1.65x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 282 us: 1.62x faster                                                  |
| chaos                   | 106 ms                                                              | 66.9 ms: 1.58x faster                                                 |
| spectral_norm           | 150 ms                                                              | 96.0 ms: 1.56x faster                                                 |
| hexiom                  | 9.50 ms                                                             | 6.08 ms: 1.56x faster                                                 |
| mako                    | 14.7 ms                                                             | 9.43 ms: 1.56x faster                                                 |
| nbody                   | 146 ms                                                              | 94.0 ms: 1.55x faster                                                 |
| crypto_pyaes            | 117 ms                                                              | 75.3 ms: 1.55x faster                                                 |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                                 |
| unpack_sequence         | 65.6 ns                                                             | 43.1 ns: 1.52x faster                                                 |
| deepcopy_memo           | 51.8 us                                                             | 34.2 us: 1.51x faster                                                 |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.63 ms: 1.50x faster                                                 |
| float                   | 110 ms                                                              | 73.2 ms: 1.50x faster                                                 |
| unpickle_pure_python    | 300 us                                                              | 200 us: 1.50x faster                                                  |
| genshi_text             | 30.4 ms                                                             | 20.9 ms: 1.46x faster                                                 |
| html5lib                | 86.4 ms                                                             | 59.7 ms: 1.45x faster                                                 |
| json_dumps              | 13.7 ms                                                             | 9.52 ms: 1.44x faster                                                 |
| chameleon               | 9.13 ms                                                             | 6.45 ms: 1.42x faster                                                 |
| logging_format          | 9.07 us                                                             | 6.41 us: 1.41x faster                                                 |
| pycparser               | 1.53 sec                                                            | 1.09 sec: 1.40x faster                                                |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.40x faster                                                |
| logging_simple          | 8.21 us                                                             | 5.88 us: 1.40x faster                                                 |
| xml_etree_process       | 74.8 ms                                                             | 53.7 ms: 1.39x faster                                                 |
| django_template         | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 686 ms: 1.39x faster                                                  |
| thrift                  | 1.04 ms                                                             | 751 us: 1.38x faster                                                  |
| regex_compile           | 177 ms                                                              | 129 ms: 1.38x faster                                                  |
| 2to3                    | 336 ms                                                              | 246 ms: 1.37x faster                                                  |
| scimark_fft             | 425 ms                                                              | 314 ms: 1.35x faster                                                  |
| genshi_xml              | 64.3 ms                                                             | 48.0 ms: 1.34x faster                                                 |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.20 ms: 1.34x faster                                                 |
| async_tree_io           | 1.78 sec                                                            | 1.34 sec: 1.33x faster                                                |
| async_tree_none         | 713 ms                                                              | 536 ms: 1.33x faster                                                  |
| deepcopy                | 438 us                                                              | 332 us: 1.32x faster                                                  |
| mypy2                   | 432 ms                                                              | 329 ms: 1.31x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 50.6 ms: 1.29x faster                                                 |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.28x faster                                                  |
| async_tree_memoization  | 853 ms                                                              | 665 ms: 1.28x faster                                                  |
| fannkuch                | 485 ms                                                              | 379 ms: 1.28x faster                                                  |
| deepcopy_reduce         | 3.80 us                                                             | 2.97 us: 1.28x faster                                                 |
| coroutines              | 31.8 ms                                                             | 25.0 ms: 1.27x faster                                                 |
| docutils                | 3.19 sec                                                            | 2.57 sec: 1.24x faster                                                |
| nqueens                 | 98.8 ms                                                             | 80.1 ms: 1.23x faster                                                 |
| xml_etree_generate      | 94.9 ms                                                             | 76.9 ms: 1.23x faster                                                 |
| json_loads              | 29.3 us                                                             | 23.8 us: 1.23x faster                                                 |
| async_tree_cpu_io_mixed | 944 ms                                                              | 769 ms: 1.23x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 778 us: 1.23x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 62.5 ms: 1.22x faster                                                 |
| dask                    | 437 ms                                                              | 360 ms: 1.21x faster                                                  |
| pickle_list             | 4.73 us                                                             | 3.95 us: 1.20x faster                                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                 |
| async_generators        | 420 ms                                                              | 354 ms: 1.19x faster                                                  |
| sympy_expand            | 540 ms                                                              | 458 ms: 1.18x faster                                                  |
| json                    | 5.41 ms                                                             | 4.67 ms: 1.16x faster                                                 |
| sympy_str               | 328 ms                                                              | 283 ms: 1.16x faster                                                  |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                 |
| sqlite_synth            | 2.97 us                                                             | 2.58 us: 1.15x faster                                                 |
| create_gc_cycles        | 1.64 ms                                                             | 1.44 ms: 1.14x faster                                                 |
| sympy_sum               | 185 ms                                                              | 164 ms: 1.13x faster                                                  |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.12x faster                                                 |
| regex_v8                | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                 |
| djangocms               | 36.3 us                                                             | 32.6 us: 1.11x faster                                                 |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.10x faster                                                  |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                                |
| pathlib                 | 19.8 ms                                                             | 18.3 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 890 ms: 1.04x faster                                                  |
| telco                   | 6.67 ms                                                             | 6.46 ms: 1.03x faster                                                 |
| pickle                  | 10.2 us                                                             | 10.1 us: 1.01x faster                                                 |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                  |
| unpickle_list           | 4.94 us                                                             | 4.97 us: 1.01x slower                                                 |
| regex_dna               | 213 ms                                                              | 217 ms: 1.02x slower                                                  |
| generators              | 75.7 ms                                                             | 79.1 ms: 1.05x slower                                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.07 ms: 1.05x slower                                                 |
| gc_traversal            | 3.53 ms                                                             | 3.81 ms: 1.08x slower                                                 |
| regex_effbot            | 3.22 ms                                                             | 3.63 ms: 1.13x slower                                                 |
| pickle_dict             | 27.8 us                                                             | 31.5 us: 1.13x slower                                                 |
| coverage                | 70.6 ms                                                             | 102 ms: 1.45x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.29x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
