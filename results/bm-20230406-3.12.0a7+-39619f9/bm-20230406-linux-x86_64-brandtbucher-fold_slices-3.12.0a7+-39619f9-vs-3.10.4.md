
# Results vs. 3.10.4

- fork: brandtbucher
- ref: fold_slices
- machine: linux-x86_64
- commit hash: 39619f9
- commit date: 2023-04-06
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 250 ms: 1.34x faster                                                |
| chameleon      | 9.13 ms                                                             | 6.49 ms: 1.41x faster                                               |
| docutils       | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                              |
| html5lib       | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                               |
| tornado_http   | 129 ms                                                              | 90.9 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                               | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 86.6 ms: 1.68x faster                                               |
| float          | 110 ms                                                              | 73.6 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                               | 1.36x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.33x faster                                                |
| regex_v8       | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                               |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                |
| regex_effbot   | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                               | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 290 us: 1.58x faster                                                |
| unpickle_pure_python | 300 us                                                              | 202 us: 1.48x faster                                                |
| json_dumps           | 13.7 ms                                                             | 9.53 ms: 1.44x faster                                               |
| xml_etree_process    | 74.8 ms                                                             | 56.2 ms: 1.33x faster                                               |
| json_loads           | 29.3 us                                                             | 24.1 us: 1.22x faster                                               |
| xml_etree_generate   | 94.9 ms                                                             | 80.9 ms: 1.17x faster                                               |
| unpickle             | 15.0 us                                                             | 13.5 us: 1.11x faster                                               |
| xml_etree_parse      | 164 ms                                                              | 150 ms: 1.09x faster                                                |
| pickle_list          | 4.73 us                                                             | 4.35 us: 1.09x faster                                               |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                |
| pickle               | 10.2 us                                                             | 10.9 us: 1.06x slower                                               |
| pickle_dict          | 27.8 us                                                             | 32.6 us: 1.17x slower                                               |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                               |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                               |
| genshi_text     | 30.4 ms                                                             | 21.0 ms: 1.45x faster                                               |
| django_template | 45.8 ms                                                             | 33.4 ms: 1.37x faster                                               |
| genshi_xml      | 64.3 ms                                                             | 47.6 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.2 ms: 2.59x faster                                               |
| deltablue               | 7.30 ms                                                             | 3.30 ms: 2.21x faster                                               |
| asyncio_tcp             | 922 ms                                                              | 500 ms: 1.84x faster                                                |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.76x faster                                                |
| richards                | 74.2 ms                                                             | 42.5 ms: 1.75x faster                                               |
| logging_silent          | 169 ns                                                              | 97.7 ns: 1.73x faster                                               |
| sqlglot_parse           | 2.07 ms                                                             | 1.23 ms: 1.69x faster                                               |
| nbody                   | 146 ms                                                              | 86.6 ms: 1.68x faster                                               |
| go                      | 226 ms                                                              | 134 ms: 1.68x faster                                                |
| raytrace                | 470 ms                                                              | 285 ms: 1.65x faster                                                |
| sqlglot_transpile       | 2.45 ms                                                             | 1.50 ms: 1.63x faster                                               |
| pyflate                 | 671 ms                                                              | 414 ms: 1.62x faster                                                |
| chaos                   | 106 ms                                                              | 65.9 ms: 1.61x faster                                               |
| python_startup          | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                               |
| hexiom                  | 9.50 ms                                                             | 5.98 ms: 1.59x faster                                               |
| scimark_monte_carlo     | 109 ms                                                              | 68.3 ms: 1.59x faster                                               |
| crypto_pyaes            | 117 ms                                                              | 73.5 ms: 1.59x faster                                               |
| pickle_pure_python      | 457 us                                                              | 290 us: 1.58x faster                                                |
| spectral_norm           | 150 ms                                                              | 96.1 ms: 1.56x faster                                               |
| deepcopy_memo           | 51.8 us                                                             | 34.2 us: 1.51x faster                                               |
| unpack_sequence         | 65.6 ns                                                             | 43.9 ns: 1.50x faster                                               |
| float                   | 110 ms                                                              | 73.6 ms: 1.49x faster                                               |
| unpickle_pure_python    | 300 us                                                              | 202 us: 1.48x faster                                                |
| mako                    | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                               |
| genshi_text             | 30.4 ms                                                             | 21.0 ms: 1.45x faster                                               |
| scimark_lu              | 160 ms                                                              | 111 ms: 1.44x faster                                                |
| json_dumps              | 13.7 ms                                                             | 9.53 ms: 1.44x faster                                               |
| logging_simple          | 8.21 us                                                             | 5.74 us: 1.43x faster                                               |
| logging_format          | 9.07 us                                                             | 6.36 us: 1.43x faster                                               |
| tornado_http            | 129 ms                                                              | 90.9 ms: 1.42x faster                                               |
| html5lib                | 86.4 ms                                                             | 61.2 ms: 1.41x faster                                               |
| chameleon               | 9.13 ms                                                             | 6.49 ms: 1.41x faster                                               |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.42 sec: 1.39x faster                                              |
| async_tree_none         | 713 ms                                                              | 515 ms: 1.38x faster                                                |
| pprint_safe_repr        | 953 ms                                                              | 690 ms: 1.38x faster                                                |
| django_template         | 45.8 ms                                                             | 33.4 ms: 1.37x faster                                               |
| scimark_fft             | 425 ms                                                              | 311 ms: 1.37x faster                                                |
| async_tree_memoization  | 853 ms                                                              | 624 ms: 1.37x faster                                                |
| genshi_xml              | 64.3 ms                                                             | 47.6 ms: 1.35x faster                                               |
| 2to3                    | 336 ms                                                              | 250 ms: 1.34x faster                                                |
| deepcopy                | 438 us                                                              | 326 us: 1.34x faster                                                |
| coroutines              | 31.8 ms                                                             | 23.7 ms: 1.34x faster                                               |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                               |
| xml_etree_process       | 74.8 ms                                                             | 56.2 ms: 1.33x faster                                               |
| thrift                  | 1.04 ms                                                             | 780 us: 1.33x faster                                                |
| regex_compile           | 177 ms                                                              | 134 ms: 1.33x faster                                                |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.33x faster                                              |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                               |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.31 ms: 1.30x faster                                               |
| mypy2                   | 432 ms                                                              | 335 ms: 1.29x faster                                                |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.29x faster                                                |
| async_tree_cpu_io_mixed | 944 ms                                                              | 736 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                             | 51.0 ms: 1.28x faster                                               |
| fannkuch                | 485 ms                                                              | 380 ms: 1.28x faster                                                |
| comprehensions          | 27.3 us                                                             | 21.4 us: 1.27x faster                                               |
| deepcopy_reduce         | 3.80 us                                                             | 2.99 us: 1.27x faster                                               |
| docutils                | 3.19 sec                                                            | 2.54 sec: 1.26x faster                                              |
| nqueens                 | 98.8 ms                                                             | 81.0 ms: 1.22x faster                                               |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                |
| json_loads              | 29.3 us                                                             | 24.1 us: 1.22x faster                                               |
| dulwich_log             | 76.3 ms                                                             | 63.3 ms: 1.21x faster                                               |
| bench_thread_pool       | 954 us                                                              | 791 us: 1.21x faster                                                |
| sympy_integrate         | 24.3 ms                                                             | 20.5 ms: 1.19x faster                                               |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                               |
| xml_etree_generate      | 94.9 ms                                                             | 80.9 ms: 1.17x faster                                               |
| json                    | 5.41 ms                                                             | 4.63 ms: 1.17x faster                                               |
| sympy_expand            | 540 ms                                                              | 467 ms: 1.16x faster                                                |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                                |
| sqlite_synth            | 2.97 us                                                             | 2.63 us: 1.13x faster                                               |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.13x faster                                                |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                               |
| regex_v8                | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                               |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                |
| unpickle                | 15.0 us                                                             | 13.5 us: 1.11x faster                                               |
| mdp                     | 2.75 sec                                                            | 2.51 sec: 1.10x faster                                              |
| xml_etree_parse         | 164 ms                                                              | 150 ms: 1.09x faster                                                |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                               |
| pickle_list             | 4.73 us                                                             | 4.35 us: 1.09x faster                                               |
| create_gc_cycles        | 1.64 ms                                                             | 1.51 ms: 1.08x faster                                               |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                |
| telco                   | 6.67 ms                                                             | 6.32 ms: 1.06x faster                                               |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                |
| async_generators        | 420 ms                                                              | 408 ms: 1.03x faster                                                |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                |
| pickle                  | 10.2 us                                                             | 10.9 us: 1.06x slower                                               |
| regex_effbot            | 3.22 ms                                                             | 3.45 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                               |
| dask                    | 437 ms                                                              | 507 ms: 1.16x slower                                                |
| gc_traversal            | 3.53 ms                                                             | 4.10 ms: 1.16x slower                                               |
| pickle_dict             | 27.8 us                                                             | 32.6 us: 1.17x slower                                               |
| coverage                | 70.6 ms                                                             | 96.7 ms: 1.37x slower                                               |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
