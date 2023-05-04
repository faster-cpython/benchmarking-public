
# Results vs. 3.10.4

- fork: gaogaotiantian
- ref: pep669_cprofile
- machine: linux-x86_64
- commit hash: 20f4663
- commit date: 2023-04-19
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 250 ms: 1.34x faster                                                      |
| chameleon      | 9.13 ms                                                             | 6.26 ms: 1.46x faster                                                     |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                    |
| html5lib       | 86.4 ms                                                             | 60.6 ms: 1.43x faster                                                     |
| tornado_http   | 129 ms                                                              | 92.7 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                               | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 85.1 ms: 1.71x faster                                                     |
| float          | 110 ms                                                              | 73.1 ms: 1.50x faster                                                     |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                               | 1.37x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 131 ms: 1.36x faster                                                      |
| regex_v8       | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                                     |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                      |
| regex_effbot   | 3.22 ms                                                             | 3.53 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                               | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 283 us: 1.61x faster                                                      |
| unpickle_pure_python | 300 us                                                              | 201 us: 1.49x faster                                                      |
| json_dumps           | 13.7 ms                                                             | 9.37 ms: 1.46x faster                                                     |
| xml_etree_process    | 74.8 ms                                                             | 55.8 ms: 1.34x faster                                                     |
| json_loads           | 29.3 us                                                             | 24.1 us: 1.21x faster                                                     |
| xml_etree_generate   | 94.9 ms                                                             | 80.7 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                              | 98.8 ms: 1.13x faster                                                     |
| pickle_list          | 4.73 us                                                             | 4.24 us: 1.12x faster                                                     |
| xml_etree_parse      | 164 ms                                                              | 147 ms: 1.11x faster                                                      |
| unpickle             | 15.0 us                                                             | 13.9 us: 1.08x faster                                                     |
| pickle               | 10.2 us                                                             | 10.9 us: 1.07x slower                                                     |
| pickle_dict          | 27.8 us                                                             | 32.6 us: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.87 ms: 1.59x faster                                                     |
| python_startup_no_site | 5.80 ms                                                             | 6.57 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.94 ms: 1.48x faster                                                     |
| genshi_text     | 30.4 ms                                                             | 21.3 ms: 1.43x faster                                                     |
| django_template | 45.8 ms                                                             | 32.6 ms: 1.40x faster                                                     |
| genshi_xml      | 64.3 ms                                                             | 46.2 ms: 1.39x faster                                                     |
| Geometric mean  | (ref)                                                               | 1.43x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230419-linux-x86_64-gaogaotiantian-pep669_cprofile-3.12.0a7+-20f4663 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 28.3 ms: 2.68x faster                                                     |
| deltablue               | 7.30 ms                                                             | 3.19 ms: 2.29x faster                                                     |
| asyncio_tcp             | 922 ms                                                              | 500 ms: 1.84x faster                                                      |
| scimark_sor             | 198 ms                                                              | 109 ms: 1.82x faster                                                      |
| richards                | 74.2 ms                                                             | 41.3 ms: 1.80x faster                                                     |
| logging_silent          | 169 ns                                                              | 94.2 ns: 1.79x faster                                                     |
| sqlglot_parse           | 2.07 ms                                                             | 1.20 ms: 1.72x faster                                                     |
| nbody                   | 146 ms                                                              | 85.1 ms: 1.71x faster                                                     |
| raytrace                | 470 ms                                                              | 276 ms: 1.70x faster                                                      |
| go                      | 226 ms                                                              | 135 ms: 1.67x faster                                                      |
| spectral_norm           | 150 ms                                                              | 90.9 ms: 1.65x faster                                                     |
| sqlglot_transpile       | 2.45 ms                                                             | 1.49 ms: 1.65x faster                                                     |
| scimark_monte_carlo     | 109 ms                                                              | 66.0 ms: 1.64x faster                                                     |
| chaos                   | 106 ms                                                              | 65.0 ms: 1.63x faster                                                     |
| pyflate                 | 671 ms                                                              | 413 ms: 1.62x faster                                                      |
| pickle_pure_python      | 457 us                                                              | 283 us: 1.61x faster                                                      |
| hexiom                  | 9.50 ms                                                             | 5.96 ms: 1.59x faster                                                     |
| python_startup          | 14.1 ms                                                             | 8.87 ms: 1.59x faster                                                     |
| crypto_pyaes            | 117 ms                                                              | 74.5 ms: 1.57x faster                                                     |
| unpack_sequence         | 65.6 ns                                                             | 42.8 ns: 1.53x faster                                                     |
| deepcopy_memo           | 51.8 us                                                             | 34.2 us: 1.51x faster                                                     |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                                      |
| float                   | 110 ms                                                              | 73.1 ms: 1.50x faster                                                     |
| unpickle_pure_python    | 300 us                                                              | 201 us: 1.49x faster                                                      |
| mako                    | 14.7 ms                                                             | 9.94 ms: 1.48x faster                                                     |
| json_dumps              | 13.7 ms                                                             | 9.37 ms: 1.46x faster                                                     |
| chameleon               | 9.13 ms                                                             | 6.26 ms: 1.46x faster                                                     |
| coroutines              | 31.8 ms                                                             | 22.1 ms: 1.44x faster                                                     |
| genshi_text             | 30.4 ms                                                             | 21.3 ms: 1.43x faster                                                     |
| logging_simple          | 8.21 us                                                             | 5.74 us: 1.43x faster                                                     |
| html5lib                | 86.4 ms                                                             | 60.6 ms: 1.43x faster                                                     |
| scimark_fft             | 425 ms                                                              | 300 ms: 1.42x faster                                                      |
| logging_format          | 9.07 us                                                             | 6.41 us: 1.41x faster                                                     |
| django_template         | 45.8 ms                                                             | 32.6 ms: 1.40x faster                                                     |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.40x faster                                                    |
| pycparser               | 1.53 sec                                                            | 1.10 sec: 1.39x faster                                                    |
| genshi_xml              | 64.3 ms                                                             | 46.2 ms: 1.39x faster                                                     |
| pprint_safe_repr        | 953 ms                                                              | 685 ms: 1.39x faster                                                      |
| tornado_http            | 129 ms                                                              | 92.7 ms: 1.39x faster                                                     |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                    |
| async_tree_none         | 713 ms                                                              | 514 ms: 1.39x faster                                                      |
| async_tree_memoization  | 853 ms                                                              | 616 ms: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                              | 131 ms: 1.36x faster                                                      |
| aiohttp                 | 1.35 ms                                                             | 998 us: 1.35x faster                                                      |
| 2to3                    | 336 ms                                                              | 250 ms: 1.34x faster                                                      |
| xml_etree_process       | 74.8 ms                                                             | 55.8 ms: 1.34x faster                                                     |
| gunicorn                | 1.43 ms                                                             | 1.07 ms: 1.34x faster                                                     |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.25 ms: 1.32x faster                                                     |
| deepcopy                | 438 us                                                              | 332 us: 1.32x faster                                                      |
| async_tree_cpu_io_mixed | 944 ms                                                              | 718 ms: 1.32x faster                                                      |
| sqlglot_normalize       | 135 ms                                                              | 102 ms: 1.31x faster                                                      |
| mypy2                   | 432 ms                                                              | 329 ms: 1.31x faster                                                      |
| thrift                  | 1.04 ms                                                             | 791 us: 1.31x faster                                                      |
| sqlglot_optimize        | 65.3 ms                                                             | 50.8 ms: 1.28x faster                                                     |
| deepcopy_reduce         | 3.80 us                                                             | 2.97 us: 1.28x faster                                                     |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                      |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                    |
| comprehensions          | 27.3 us                                                             | 21.6 us: 1.26x faster                                                     |
| nqueens                 | 98.8 ms                                                             | 79.5 ms: 1.24x faster                                                     |
| sqlalchemy_declarative  | 166 ms                                                              | 135 ms: 1.23x faster                                                      |
| dulwich_log             | 76.3 ms                                                             | 62.0 ms: 1.23x faster                                                     |
| bench_thread_pool       | 954 us                                                              | 781 us: 1.22x faster                                                      |
| json_loads              | 29.3 us                                                             | 24.1 us: 1.21x faster                                                     |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.4 ms: 1.21x faster                                                     |
| sympy_integrate         | 24.3 ms                                                             | 20.3 ms: 1.20x faster                                                     |
| pylint                  | 521 ms                                                              | 435 ms: 1.20x faster                                                      |
| sympy_expand            | 540 ms                                                              | 455 ms: 1.19x faster                                                      |
| xml_etree_generate      | 94.9 ms                                                             | 80.7 ms: 1.18x faster                                                     |
| regex_v8                | 24.9 ms                                                             | 21.3 ms: 1.17x faster                                                     |
| sympy_str               | 328 ms                                                              | 280 ms: 1.17x faster                                                      |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                                     |
| pathlib                 | 19.8 ms                                                             | 17.0 ms: 1.16x faster                                                     |
| sqlite_synth            | 2.97 us                                                             | 2.60 us: 1.14x faster                                                     |
| djangocms               | 36.3 us                                                             | 31.7 us: 1.14x faster                                                     |
| sympy_sum               | 185 ms                                                              | 162 ms: 1.14x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                              | 98.8 ms: 1.13x faster                                                     |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                                     |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.12x faster                                                      |
| pickle_list             | 4.73 us                                                             | 4.24 us: 1.12x faster                                                     |
| xml_etree_parse         | 164 ms                                                              | 147 ms: 1.11x faster                                                      |
| unpickle                | 15.0 us                                                             | 13.9 us: 1.08x faster                                                     |
| mdp                     | 2.75 sec                                                            | 2.60 sec: 1.06x faster                                                    |
| telco                   | 6.67 ms                                                             | 6.44 ms: 1.04x faster                                                     |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                      |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                      |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                     |
| async_generators        | 420 ms                                                              | 431 ms: 1.03x slower                                                      |
| pickle                  | 10.2 us                                                             | 10.9 us: 1.07x slower                                                     |
| regex_effbot            | 3.22 ms                                                             | 3.53 ms: 1.09x slower                                                     |
| dask                    | 437 ms                                                              | 487 ms: 1.11x slower                                                      |
| python_startup_no_site  | 5.80 ms                                                             | 6.57 ms: 1.13x slower                                                     |
| gc_traversal            | 3.53 ms                                                             | 4.06 ms: 1.15x slower                                                     |
| pickle_dict             | 27.8 us                                                             | 32.6 us: 1.17x slower                                                     |
| coverage                | 70.6 ms                                                             | 96.8 ms: 1.37x slower                                                     |
| Geometric mean          | (ref)                                                               | 1.31x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging
