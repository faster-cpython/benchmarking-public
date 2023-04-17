
# Results vs. 3.10.4

- fork: thatbirdguythatuknownot
- ref: patch_30
- machine: linux-x86_64
- commit hash: 148c833
- commit date: 2023-04-15
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.13 ms                                                             | 6.48 ms: 1.41x faster                                                       |
| docutils       | 3.19 sec                                                            | 2.52 sec: 1.27x faster                                                      |
| html5lib       | 86.4 ms                                                             | 60.3 ms: 1.43x faster                                                       |
| tornado_http   | 129 ms                                                              | 93.0 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                               | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 83.5 ms: 1.75x faster                                                       |
| float          | 110 ms                                                              | 73.7 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                               | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 129 ms: 1.37x faster                                                        |
| regex_v8       | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                                       |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.22 ms                                                             | 3.52 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                               | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 286 us: 1.60x faster                                                        |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.48x faster                                                        |
| json_dumps           | 13.7 ms                                                             | 9.32 ms: 1.47x faster                                                       |
| xml_etree_process    | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                                       |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                       |
| xml_etree_generate   | 94.9 ms                                                             | 79.8 ms: 1.19x faster                                                       |
| pickle_list          | 4.73 us                                                             | 4.24 us: 1.12x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                              | 99.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 164 ms                                                              | 150 ms: 1.09x faster                                                        |
| unpickle             | 15.0 us                                                             | 14.3 us: 1.05x faster                                                       |
| pickle               | 10.2 us                                                             | 10.7 us: 1.04x slower                                                       |
| unpickle_list        | 4.94 us                                                             | 5.15 us: 1.04x slower                                                       |
| pickle_dict          | 27.8 us                                                             | 31.7 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.90 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.80 ms                                                             | 6.60 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.18x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.96 ms: 1.48x faster                                                       |
| genshi_text     | 30.4 ms                                                             | 21.5 ms: 1.41x faster                                                       |
| django_template | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                                       |
| genshi_xml      | 64.3 ms                                                             | 47.1 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 28.9 ms: 2.62x faster                                                       |
| deltablue               | 7.30 ms                                                             | 3.23 ms: 2.26x faster                                                       |
| asyncio_tcp             | 922 ms                                                              | 500 ms: 1.84x faster                                                        |
| scimark_sor             | 198 ms                                                              | 110 ms: 1.80x faster                                                        |
| logging_silent          | 169 ns                                                              | 95.8 ns: 1.76x faster                                                       |
| richards                | 74.2 ms                                                             | 42.3 ms: 1.75x faster                                                       |
| nbody                   | 146 ms                                                              | 83.5 ms: 1.75x faster                                                       |
| sqlglot_parse           | 2.07 ms                                                             | 1.22 ms: 1.70x faster                                                       |
| raytrace                | 470 ms                                                              | 282 ms: 1.67x faster                                                        |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                        |
| spectral_norm           | 150 ms                                                              | 91.4 ms: 1.64x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                              | 66.2 ms: 1.64x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                             | 1.50 ms: 1.63x faster                                                       |
| chaos                   | 106 ms                                                              | 64.8 ms: 1.63x faster                                                       |
| pyflate                 | 671 ms                                                              | 414 ms: 1.62x faster                                                        |
| pickle_pure_python      | 457 us                                                              | 286 us: 1.60x faster                                                        |
| hexiom                  | 9.50 ms                                                             | 5.96 ms: 1.60x faster                                                       |
| python_startup          | 14.1 ms                                                             | 8.90 ms: 1.59x faster                                                       |
| crypto_pyaes            | 117 ms                                                              | 74.5 ms: 1.57x faster                                                       |
| unpack_sequence         | 65.6 ns                                                             | 42.9 ns: 1.53x faster                                                       |
| scimark_lu              | 160 ms                                                              | 105 ms: 1.52x faster                                                        |
| float                   | 110 ms                                                              | 73.7 ms: 1.49x faster                                                       |
| deepcopy_memo           | 51.8 us                                                             | 34.9 us: 1.48x faster                                                       |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.48x faster                                                        |
| mako                    | 14.7 ms                                                             | 9.96 ms: 1.48x faster                                                       |
| json_dumps              | 13.7 ms                                                             | 9.32 ms: 1.47x faster                                                       |
| coroutines              | 31.8 ms                                                             | 21.7 ms: 1.46x faster                                                       |
| html5lib                | 86.4 ms                                                             | 60.3 ms: 1.43x faster                                                       |
| logging_simple          | 8.21 us                                                             | 5.76 us: 1.43x faster                                                       |
| logging_format          | 9.07 us                                                             | 6.36 us: 1.43x faster                                                       |
| genshi_text             | 30.4 ms                                                             | 21.5 ms: 1.41x faster                                                       |
| chameleon               | 9.13 ms                                                             | 6.48 ms: 1.41x faster                                                       |
| django_template         | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                                       |
| pycparser               | 1.53 sec                                                            | 1.10 sec: 1.40x faster                                                      |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.03 ms: 1.39x faster                                                       |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                      |
| tornado_http            | 129 ms                                                              | 93.0 ms: 1.39x faster                                                       |
| async_tree_memoization  | 853 ms                                                              | 616 ms: 1.38x faster                                                        |
| async_tree_none         | 713 ms                                                              | 517 ms: 1.38x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.44 sec: 1.37x faster                                                      |
| scimark_fft             | 425 ms                                                              | 310 ms: 1.37x faster                                                        |
| regex_compile           | 177 ms                                                              | 129 ms: 1.37x faster                                                        |
| genshi_xml              | 64.3 ms                                                             | 47.1 ms: 1.36x faster                                                       |
| xml_etree_process       | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                                       |
| pprint_safe_repr        | 953 ms                                                              | 704 ms: 1.35x faster                                                        |
| 2to3                    | 336 ms                                                              | 249 ms: 1.35x faster                                                        |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                             | 1.08 ms: 1.33x faster                                                       |
| deepcopy                | 438 us                                                              | 334 us: 1.31x faster                                                        |
| thrift                  | 1.04 ms                                                             | 792 us: 1.31x faster                                                        |
| mypy2                   | 432 ms                                                              | 330 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed | 944 ms                                                              | 724 ms: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                             | 51.2 ms: 1.28x faster                                                       |
| comprehensions          | 27.3 us                                                             | 21.4 us: 1.27x faster                                                       |
| docutils                | 3.19 sec                                                            | 2.52 sec: 1.27x faster                                                      |
| deepcopy_reduce         | 3.80 us                                                             | 3.02 us: 1.26x faster                                                       |
| fannkuch                | 485 ms                                                              | 387 ms: 1.25x faster                                                        |
| sqlalchemy_declarative  | 166 ms                                                              | 135 ms: 1.23x faster                                                        |
| dulwich_log             | 76.3 ms                                                             | 62.3 ms: 1.23x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.3 ms: 1.22x faster                                                       |
| nqueens                 | 98.8 ms                                                             | 81.1 ms: 1.22x faster                                                       |
| bench_thread_pool       | 954 us                                                              | 786 us: 1.21x faster                                                        |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                       |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                       |
| xml_etree_generate      | 94.9 ms                                                             | 79.8 ms: 1.19x faster                                                       |
| pylint                  | 521 ms                                                              | 439 ms: 1.19x faster                                                        |
| sympy_expand            | 540 ms                                                              | 459 ms: 1.18x faster                                                        |
| sympy_str               | 328 ms                                                              | 281 ms: 1.17x faster                                                        |
| json                    | 5.41 ms                                                             | 4.67 ms: 1.16x faster                                                       |
| pathlib                 | 19.8 ms                                                             | 17.2 ms: 1.15x faster                                                       |
| regex_v8                | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                                       |
| sympy_sum               | 185 ms                                                              | 163 ms: 1.13x faster                                                        |
| djangocms               | 36.3 us                                                             | 32.2 us: 1.13x faster                                                       |
| sqlite_synth            | 2.97 us                                                             | 2.64 us: 1.13x faster                                                       |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                                       |
| pickle_list             | 4.73 us                                                             | 4.24 us: 1.12x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                              | 99.8 ms: 1.12x faster                                                       |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.11x faster                                                        |
| xml_etree_parse         | 164 ms                                                              | 150 ms: 1.09x faster                                                        |
| mdp                     | 2.75 sec                                                            | 2.55 sec: 1.08x faster                                                      |
| unpickle                | 15.0 us                                                             | 14.3 us: 1.05x faster                                                       |
| telco                   | 6.67 ms                                                             | 6.48 ms: 1.03x faster                                                       |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                        |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                        |
| async_generators        | 420 ms                                                              | 427 ms: 1.02x slower                                                        |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.04x slower                                                       |
| unpickle_list           | 4.94 us                                                             | 5.15 us: 1.04x slower                                                       |
| regex_effbot            | 3.22 ms                                                             | 3.52 ms: 1.09x slower                                                       |
| dask                    | 437 ms                                                              | 491 ms: 1.12x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.60 ms: 1.14x slower                                                       |
| pickle_dict             | 27.8 us                                                             | 31.7 us: 1.14x slower                                                       |
| gc_traversal            | 3.53 ms                                                             | 4.06 ms: 1.15x slower                                                       |
| coverage                | 70.6 ms                                                             | 96.8 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                               | 1.31x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging
