
# Results vs. 3.10.4

- fork: python
- ref: 5d7d86f2fdbbfc23325e
- machine: linux-x86_64
- commit hash: 5d7d86f
- commit date: 2023-04-07
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.47 ms: 1.41x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                 |
| html5lib       | 86.4 ms                                                             | 61.7 ms: 1.40x faster                                                  |
| tornado_http   | 129 ms                                                              | 94.1 ms: 1.37x faster                                                  |
| Geometric mean | (ref)                                                               | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.8 ms: 1.64x faster                                                  |
| float          | 110 ms                                                              | 73.3 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.35x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.32x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                  |
| regex_dna      | 213 ms                                                              | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 286 us: 1.60x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 199 us: 1.50x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.61 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 55.4 ms: 1.35x faster                                                  |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.20x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 80.0 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 99.9 ms: 1.11x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 148 ms: 1.11x faster                                                   |
| unpickle             | 15.0 us                                                             | 13.9 us: 1.08x faster                                                  |
| pickle_list          | 4.73 us                                                             | 4.46 us: 1.06x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| pickle               | 10.2 us                                                             | 10.8 us: 1.06x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 33.0 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                  |
| django_template | 45.8 ms                                                             | 32.6 ms: 1.40x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 48.3 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.3 ms: 2.59x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.22 ms: 2.26x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 503 ms: 1.83x faster                                                   |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.76x faster                                                   |
| logging_silent          | 169 ns                                                              | 96.5 ns: 1.75x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.22 ms: 1.70x faster                                                  |
| richards                | 74.2 ms                                                             | 43.8 ms: 1.70x faster                                                  |
| raytrace                | 470 ms                                                              | 281 ms: 1.67x faster                                                   |
| spectral_norm           | 150 ms                                                              | 91.2 ms: 1.65x faster                                                  |
| nbody                   | 146 ms                                                              | 88.8 ms: 1.64x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.50 ms: 1.63x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 66.5 ms: 1.63x faster                                                  |
| go                      | 226 ms                                                              | 139 ms: 1.63x faster                                                   |
| pyflate                 | 671 ms                                                              | 413 ms: 1.62x faster                                                   |
| python_startup          | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                                  |
| chaos                   | 106 ms                                                              | 66.2 ms: 1.60x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 286 us: 1.60x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 73.3 ms: 1.59x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 5.99 ms: 1.59x faster                                                  |
| scimark_lu              | 160 ms                                                              | 105 ms: 1.52x faster                                                   |
| deepcopy_memo           | 51.8 us                                                             | 34.0 us: 1.52x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 199 us: 1.50x faster                                                   |
| unpack_sequence         | 65.6 ns                                                             | 43.6 ns: 1.50x faster                                                  |
| float                   | 110 ms                                                              | 73.3 ms: 1.50x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                                  |
| logging_simple          | 8.21 us                                                             | 5.63 us: 1.46x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.23 us: 1.46x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.61 ms: 1.43x faster                                                  |
| scimark_fft             | 425 ms                                                              | 301 ms: 1.41x faster                                                   |
| chameleon               | 9.13 ms                                                             | 6.47 ms: 1.41x faster                                                  |
| django_template         | 45.8 ms                                                             | 32.6 ms: 1.40x faster                                                  |
| html5lib                | 86.4 ms                                                             | 61.7 ms: 1.40x faster                                                  |
| async_tree_none         | 713 ms                                                              | 510 ms: 1.40x faster                                                   |
| genshi_text             | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                 |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.39x faster                                                 |
| coroutines              | 31.8 ms                                                             | 22.9 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.05 ms: 1.39x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 692 ms: 1.38x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 619 ms: 1.38x faster                                                   |
| tornado_http            | 129 ms                                                              | 94.1 ms: 1.37x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 55.4 ms: 1.35x faster                                                  |
| deepcopy                | 438 us                                                              | 326 us: 1.34x faster                                                   |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.34x faster                                                 |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                                  |
| genshi_xml              | 64.3 ms                                                             | 48.3 ms: 1.33x faster                                                  |
| thrift                  | 1.04 ms                                                             | 784 us: 1.32x faster                                                   |
| regex_compile           | 177 ms                                                              | 134 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 719 ms: 1.31x faster                                                   |
| gunicorn                | 1.43 ms                                                             | 1.10 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.30x faster                                                   |
| mypy2                   | 432 ms                                                              | 334 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 50.6 ms: 1.29x faster                                                  |
| fannkuch                | 485 ms                                                              | 377 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.80 us                                                             | 2.99 us: 1.27x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                                 |
| comprehensions          | 27.3 us                                                             | 21.8 us: 1.25x faster                                                  |
| nqueens                 | 98.8 ms                                                             | 79.4 ms: 1.25x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 63.0 ms: 1.21x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 138 ms: 1.21x faster                                                   |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 80.0 ms: 1.19x faster                                                  |
| json                    | 5.41 ms                                                             | 4.60 ms: 1.18x faster                                                  |
| sympy_expand            | 540 ms                                                              | 459 ms: 1.17x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                             | 18.0 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                              | 283 ms: 1.16x faster                                                   |
| sqlite_synth            | 2.97 us                                                             | 2.62 us: 1.13x faster                                                  |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                                  |
| sympy_sum               | 185 ms                                                              | 165 ms: 1.12x faster                                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                                  |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 99.9 ms: 1.11x faster                                                  |
| xml_etree_parse         | 164 ms                                                              | 148 ms: 1.11x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.54 sec: 1.09x faster                                                 |
| unpickle                | 15.0 us                                                             | 13.9 us: 1.08x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.46 us: 1.06x faster                                                  |
| regex_dna               | 213 ms                                                              | 203 ms: 1.05x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.51 ms: 1.03x faster                                                  |
| async_generators        | 420 ms                                                              | 415 ms: 1.01x faster                                                   |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| pickle                  | 10.2 us                                                             | 10.8 us: 1.06x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                                  |
| dask                    | 437 ms                                                              | 500 ms: 1.14x slower                                                   |
| gc_traversal            | 3.53 ms                                                             | 4.07 ms: 1.15x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 33.0 us: 1.19x slower                                                  |
| coverage                | 70.6 ms                                                             | 95.9 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
