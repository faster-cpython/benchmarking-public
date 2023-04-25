
# Results vs. 3.10.4

- fork: itamaro
- ref: defer_task_name_form
- machine: linux-x86_64
- commit hash: db3b8a6
- commit date: 2023-04-24
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 267 ms: 1.26x faster                                                    |
| chameleon      | 9.13 ms                                                             | 6.82 ms: 1.34x faster                                                   |
| docutils       | 3.19 sec                                                            | 2.69 sec: 1.19x faster                                                  |
| html5lib       | 86.4 ms                                                             | 65.1 ms: 1.33x faster                                                   |
| tornado_http   | 129 ms                                                              | 104 ms: 1.24x faster                                                    |
| Geometric mean | (ref)                                                               | 1.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 89.0 ms: 1.64x faster                                                   |
| float          | 110 ms                                                              | 80.0 ms: 1.37x faster                                                   |
| pidigits       | 190 ms                                                              | 189 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                               | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 142 ms: 1.25x faster                                                    |
| regex_v8       | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                                   |
| regex_dna      | 213 ms                                                              | 203 ms: 1.05x faster                                                    |
| regex_effbot   | 3.22 ms                                                             | 3.66 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                               | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 313 us: 1.46x faster                                                    |
| json_dumps           | 13.7 ms                                                             | 9.68 ms: 1.42x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 218 us: 1.37x faster                                                    |
| xml_etree_process    | 74.8 ms                                                             | 57.9 ms: 1.29x faster                                                   |
| json_loads           | 29.3 us                                                             | 24.8 us: 1.18x faster                                                   |
| xml_etree_generate   | 94.9 ms                                                             | 82.5 ms: 1.15x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                              | 102 ms: 1.09x faster                                                    |
| xml_etree_parse      | 164 ms                                                              | 152 ms: 1.07x faster                                                    |
| pickle_list          | 4.73 us                                                             | 4.41 us: 1.07x faster                                                   |
| unpickle             | 15.0 us                                                             | 14.4 us: 1.04x faster                                                   |
| unpickle_list        | 4.94 us                                                             | 5.11 us: 1.03x slower                                                   |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                   |
| pickle_dict          | 27.8 us                                                             | 31.6 us: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                               | 1.14x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.99 ms: 1.57x faster                                                   |
| python_startup_no_site | 5.80 ms                                                             | 6.60 ms: 1.14x slower                                                   |
| Geometric mean         | (ref)                                                               | 1.18x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                   |
| django_template | 45.8 ms                                                             | 34.3 ms: 1.34x faster                                                   |
| genshi_text     | 30.4 ms                                                             | 23.0 ms: 1.32x faster                                                   |
| genshi_xml      | 64.3 ms                                                             | 50.5 ms: 1.27x faster                                                   |
| Geometric mean  | (ref)                                                               | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 32.2 ms: 2.35x faster                                                   |
| deltablue               | 7.30 ms                                                             | 3.64 ms: 2.01x faster                                                   |
| asyncio_tcp             | 922 ms                                                              | 512 ms: 1.80x faster                                                    |
| richards                | 74.2 ms                                                             | 43.2 ms: 1.72x faster                                                   |
| logging_silent          | 169 ns                                                              | 98.8 ns: 1.71x faster                                                   |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                    |
| nbody                   | 146 ms                                                              | 89.0 ms: 1.64x faster                                                   |
| scimark_sor             | 198 ms                                                              | 122 ms: 1.63x faster                                                    |
| python_startup          | 14.1 ms                                                             | 8.99 ms: 1.57x faster                                                   |
| raytrace                | 470 ms                                                              | 301 ms: 1.56x faster                                                    |
| sqlglot_parse           | 2.07 ms                                                             | 1.32 ms: 1.56x faster                                                   |
| chaos                   | 106 ms                                                              | 68.5 ms: 1.55x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                              | 71.0 ms: 1.53x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 76.9 ms: 1.52x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 6.36 ms: 1.50x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.65 ms: 1.49x faster                                                   |
| pyflate                 | 671 ms                                                              | 459 ms: 1.46x faster                                                    |
| pickle_pure_python      | 457 us                                                              | 313 us: 1.46x faster                                                    |
| scimark_lu              | 160 ms                                                              | 111 ms: 1.44x faster                                                    |
| coroutines              | 31.8 ms                                                             | 22.0 ms: 1.44x faster                                                   |
| spectral_norm           | 150 ms                                                              | 104 ms: 1.44x faster                                                    |
| async_tree_io           | 1.78 sec                                                            | 1.25 sec: 1.43x faster                                                  |
| async_tree_none         | 713 ms                                                              | 500 ms: 1.42x faster                                                    |
| json_dumps              | 13.7 ms                                                             | 9.68 ms: 1.42x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 621 ms: 1.37x faster                                                    |
| float                   | 110 ms                                                              | 80.0 ms: 1.37x faster                                                   |
| unpickle_pure_python    | 300 us                                                              | 218 us: 1.37x faster                                                    |
| mako                    | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                   |
| pycparser               | 1.53 sec                                                            | 1.13 sec: 1.35x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.82 ms: 1.34x faster                                                   |
| django_template         | 45.8 ms                                                             | 34.3 ms: 1.34x faster                                                   |
| pprint_pformat          | 1.98 sec                                                            | 1.48 sec: 1.33x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 39.0 us: 1.33x faster                                                   |
| html5lib                | 86.4 ms                                                             | 65.1 ms: 1.33x faster                                                   |
| unpack_sequence         | 65.6 ns                                                             | 49.5 ns: 1.33x faster                                                   |
| genshi_text             | 30.4 ms                                                             | 23.0 ms: 1.32x faster                                                   |
| logging_format          | 9.07 us                                                             | 6.87 us: 1.32x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.23 us: 1.32x faster                                                   |
| pprint_safe_repr        | 953 ms                                                              | 724 ms: 1.32x faster                                                    |
| async_tree_cpu_io_mixed | 944 ms                                                              | 718 ms: 1.32x faster                                                    |
| thrift                  | 1.04 ms                                                             | 795 us: 1.30x faster                                                    |
| xml_etree_process       | 74.8 ms                                                             | 57.9 ms: 1.29x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 50.5 ms: 1.27x faster                                                   |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                    |
| 2to3                    | 336 ms                                                              | 267 ms: 1.26x faster                                                    |
| regex_compile           | 177 ms                                                              | 142 ms: 1.25x faster                                                    |
| tornado_http            | 129 ms                                                              | 104 ms: 1.24x faster                                                    |
| scimark_fft             | 425 ms                                                              | 348 ms: 1.22x faster                                                    |
| deepcopy                | 438 us                                                              | 360 us: 1.22x faster                                                    |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                    |
| nqueens                 | 98.8 ms                                                             | 82.0 ms: 1.21x faster                                                   |
| mypy2                   | 432 ms                                                              | 359 ms: 1.20x faster                                                    |
| deepcopy_reduce         | 3.80 us                                                             | 3.18 us: 1.19x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 54.7 ms: 1.19x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.69 sec: 1.19x faster                                                  |
| json_loads              | 29.3 us                                                             | 24.8 us: 1.18x faster                                                   |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.78 ms: 1.18x faster                                                   |
| comprehensions          | 27.3 us                                                             | 23.4 us: 1.16x faster                                                   |
| xml_etree_generate      | 94.9 ms                                                             | 82.5 ms: 1.15x faster                                                   |
| bench_thread_pool       | 954 us                                                              | 835 us: 1.14x faster                                                    |
| json                    | 5.41 ms                                                             | 4.75 ms: 1.14x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                    |
| dulwich_log             | 76.3 ms                                                             | 68.0 ms: 1.12x faster                                                   |
| sqlite_synth            | 2.97 us                                                             | 2.67 us: 1.11x faster                                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.11x faster                                                   |
| pylint                  | 521 ms                                                              | 467 ms: 1.11x faster                                                    |
| sympy_integrate         | 24.3 ms                                                             | 21.9 ms: 1.11x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 17.9 ms: 1.11x faster                                                   |
| djangocms               | 36.3 us                                                             | 33.2 us: 1.09x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                              | 102 ms: 1.09x faster                                                    |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.5 ms: 1.08x faster                                                   |
| sympy_expand            | 540 ms                                                              | 500 ms: 1.08x faster                                                    |
| xml_etree_parse         | 164 ms                                                              | 152 ms: 1.07x faster                                                    |
| pickle_list             | 4.73 us                                                             | 4.41 us: 1.07x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.59 sec: 1.06x faster                                                  |
| sympy_str               | 328 ms                                                              | 310 ms: 1.06x faster                                                    |
| regex_dna               | 213 ms                                                              | 203 ms: 1.05x faster                                                    |
| unpickle                | 15.0 us                                                             | 14.4 us: 1.04x faster                                                   |
| sympy_sum               | 185 ms                                                              | 180 ms: 1.03x faster                                                    |
| meteor_contest          | 115 ms                                                              | 114 ms: 1.01x faster                                                    |
| pidigits                | 190 ms                                                              | 189 ms: 1.01x faster                                                    |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                   |
| unpickle_list           | 4.94 us                                                             | 5.11 us: 1.03x slower                                                   |
| async_generators        | 420 ms                                                              | 440 ms: 1.05x slower                                                    |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                   |
| regex_effbot            | 3.22 ms                                                             | 3.66 ms: 1.14x slower                                                   |
| python_startup_no_site  | 5.80 ms                                                             | 6.60 ms: 1.14x slower                                                   |
| pickle_dict             | 27.8 us                                                             | 31.6 us: 1.14x slower                                                   |
| gc_traversal            | 3.53 ms                                                             | 4.08 ms: 1.16x slower                                                   |
| dask                    | 437 ms                                                              | 538 ms: 1.23x slower                                                    |
| coverage                | 70.6 ms                                                             | 99.8 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                            |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
