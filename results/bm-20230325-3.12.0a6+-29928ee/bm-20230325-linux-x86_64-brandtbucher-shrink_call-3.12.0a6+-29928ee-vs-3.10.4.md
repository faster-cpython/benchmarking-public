
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_call
- machine: linux-x86_64
- commit hash: 29928ee
- commit date: 2023-03-25
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                |
| chameleon      | 9.13 ms                                                             | 6.55 ms: 1.39x faster                                               |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                              |
| html5lib       | 86.4 ms                                                             | 61.5 ms: 1.40x faster                                               |
| tornado_http   | 129 ms                                                              | 91.4 ms: 1.41x faster                                               |
| Geometric mean | (ref)                                                               | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.9 ms: 1.66x faster                                               |
| float          | 110 ms                                                              | 74.7 ms: 1.47x faster                                               |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                               | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.32x faster                                                |
| regex_v8       | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                               |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                |
| regex_effbot   | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                               | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 288 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.49x faster                                                |
| json_dumps           | 13.7 ms                                                             | 9.48 ms: 1.45x faster                                               |
| xml_etree_process    | 74.8 ms                                                             | 55.9 ms: 1.34x faster                                               |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                               |
| xml_etree_generate   | 94.9 ms                                                             | 81.4 ms: 1.17x faster                                               |
| pickle_list          | 4.73 us                                                             | 4.12 us: 1.15x faster                                               |
| unpickle             | 15.0 us                                                             | 13.6 us: 1.10x faster                                               |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 111 ms                                                              | 102 ms: 1.09x faster                                                |
| unpickle_list        | 4.94 us                                                             | 5.23 us: 1.06x slower                                               |
| pickle_dict          | 27.8 us                                                             | 30.7 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                               |
| python_startup_no_site | 5.80 ms                                                             | 6.55 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.98 ms: 1.48x faster                                               |
| genshi_text     | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                               |
| django_template | 45.8 ms                                                             | 33.3 ms: 1.37x faster                                               |
| genshi_xml      | 64.3 ms                                                             | 46.9 ms: 1.37x faster                                               |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230325-linux-x86_64-brandtbucher-shrink_call-3.12.0a6+-29928ee |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.2 ms: 2.50x faster                                               |
| deltablue               | 7.30 ms                                                             | 3.21 ms: 2.28x faster                                               |
| asyncio_tcp             | 922 ms                                                              | 504 ms: 1.83x faster                                                |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.77x faster                                                |
| logging_silent          | 169 ns                                                              | 97.0 ns: 1.74x faster                                               |
| richards                | 74.2 ms                                                             | 44.2 ms: 1.68x faster                                               |
| nbody                   | 146 ms                                                              | 87.9 ms: 1.66x faster                                               |
| raytrace                | 470 ms                                                              | 285 ms: 1.65x faster                                                |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                                |
| scimark_monte_carlo     | 109 ms                                                              | 66.7 ms: 1.63x faster                                               |
| chaos                   | 106 ms                                                              | 65.8 ms: 1.61x faster                                               |
| python_startup          | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                               |
| crypto_pyaes            | 117 ms                                                              | 73.1 ms: 1.59x faster                                               |
| pickle_pure_python      | 457 us                                                              | 288 us: 1.58x faster                                                |
| hexiom                  | 9.50 ms                                                             | 6.03 ms: 1.58x faster                                               |
| pyflate                 | 671 ms                                                              | 431 ms: 1.56x faster                                                |
| spectral_norm           | 150 ms                                                              | 97.3 ms: 1.54x faster                                               |
| deepcopy_memo           | 51.8 us                                                             | 33.7 us: 1.54x faster                                               |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                                |
| unpack_sequence         | 65.6 ns                                                             | 44.0 ns: 1.49x faster                                               |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.49x faster                                                |
| mako                    | 14.7 ms                                                             | 9.98 ms: 1.48x faster                                               |
| float                   | 110 ms                                                              | 74.7 ms: 1.47x faster                                               |
| json_dumps              | 13.7 ms                                                             | 9.48 ms: 1.45x faster                                               |
| sqlglot_parse           | 2.07 ms                                                             | 1.44 ms: 1.44x faster                                               |
| logging_simple          | 8.21 us                                                             | 5.73 us: 1.43x faster                                               |
| genshi_text             | 30.4 ms                                                             | 21.2 ms: 1.43x faster                                               |
| logging_format          | 9.07 us                                                             | 6.36 us: 1.43x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                               |
| tornado_http            | 129 ms                                                              | 91.4 ms: 1.41x faster                                               |
| html5lib                | 86.4 ms                                                             | 61.5 ms: 1.40x faster                                               |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.40x faster                                              |
| chameleon               | 9.13 ms                                                             | 6.55 ms: 1.39x faster                                               |
| pprint_safe_repr        | 953 ms                                                              | 686 ms: 1.39x faster                                                |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                              |
| django_template         | 45.8 ms                                                             | 33.3 ms: 1.37x faster                                               |
| genshi_xml              | 64.3 ms                                                             | 46.9 ms: 1.37x faster                                               |
| scimark_fft             | 425 ms                                                              | 310 ms: 1.37x faster                                                |
| async_tree_none         | 713 ms                                                              | 522 ms: 1.37x faster                                                |
| coroutines              | 31.8 ms                                                             | 23.5 ms: 1.35x faster                                               |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.18 ms: 1.34x faster                                               |
| deepcopy                | 438 us                                                              | 327 us: 1.34x faster                                                |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.34x faster                                              |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                |
| xml_etree_process       | 74.8 ms                                                             | 55.9 ms: 1.34x faster                                               |
| async_tree_memoization  | 853 ms                                                              | 638 ms: 1.34x faster                                                |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                               |
| thrift                  | 1.04 ms                                                             | 783 us: 1.32x faster                                                |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                               |
| regex_compile           | 177 ms                                                              | 135 ms: 1.32x faster                                                |
| mypy2                   | 432 ms                                                              | 333 ms: 1.30x faster                                                |
| deepcopy_reduce         | 3.80 us                                                             | 2.96 us: 1.28x faster                                               |
| async_tree_cpu_io_mixed | 944 ms                                                              | 739 ms: 1.28x faster                                                |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                             | 51.5 ms: 1.27x faster                                               |
| fannkuch                | 485 ms                                                              | 384 ms: 1.26x faster                                                |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                              |
| nqueens                 | 98.8 ms                                                             | 80.6 ms: 1.23x faster                                               |
| bench_thread_pool       | 954 us                                                              | 784 us: 1.22x faster                                                |
| dulwich_log             | 76.3 ms                                                             | 63.5 ms: 1.20x faster                                               |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                               |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                               |
| sqlalchemy_declarative  | 166 ms                                                              | 140 ms: 1.19x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                               |
| sympy_expand            | 540 ms                                                              | 462 ms: 1.17x faster                                                |
| xml_etree_generate      | 94.9 ms                                                             | 81.4 ms: 1.17x faster                                               |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                               |
| regex_v8                | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                               |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                                |
| comprehensions          | 27.3 us                                                             | 23.7 us: 1.15x faster                                               |
| pickle_list             | 4.73 us                                                             | 4.12 us: 1.15x faster                                               |
| sqlite_synth            | 2.97 us                                                             | 2.61 us: 1.14x faster                                               |
| pathlib                 | 19.8 ms                                                             | 17.4 ms: 1.13x faster                                               |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                               |
| sympy_sum               | 185 ms                                                              | 167 ms: 1.11x faster                                                |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                              |
| unpickle                | 15.0 us                                                             | 13.6 us: 1.10x faster                                               |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 111 ms                                                              | 102 ms: 1.09x faster                                                |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.09x faster                                               |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                |
| async_generators        | 420 ms                                                              | 408 ms: 1.03x faster                                                |
| telco                   | 6.67 ms                                                             | 6.55 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| unpickle_list           | 4.94 us                                                             | 5.23 us: 1.06x slower                                               |
| regex_effbot            | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                               |
| gc_traversal            | 3.53 ms                                                             | 3.83 ms: 1.09x slower                                               |
| pickle_dict             | 27.8 us                                                             | 30.7 us: 1.11x slower                                               |
| python_startup_no_site  | 5.80 ms                                                             | 6.55 ms: 1.13x slower                                               |
| dask                    | 437 ms                                                              | 512 ms: 1.17x slower                                                |
| coverage                | 70.6 ms                                                             | 99.1 ms: 1.40x slower                                               |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
