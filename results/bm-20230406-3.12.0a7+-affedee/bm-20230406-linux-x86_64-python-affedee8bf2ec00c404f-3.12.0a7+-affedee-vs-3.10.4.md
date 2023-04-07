
# Results vs. 3.10.4

- fork: python
- ref: affedee8bf2ec00c404f
- machine: linux-x86_64
- commit hash: affedee
- commit date: 2023-04-06
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.27 ms: 1.46x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                 |
| html5lib       | 86.4 ms                                                             | 61.4 ms: 1.41x faster                                                  |
| tornado_http   | 129 ms                                                              | 90.8 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                               | 1.38x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 86.9 ms: 1.68x faster                                                  |
| float          | 110 ms                                                              | 73.5 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 133 ms: 1.34x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.48 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 289 us: 1.58x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 203 us: 1.48x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.47 ms: 1.45x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 55.2 ms: 1.36x faster                                                  |
| json_loads           | 29.3 us                                                             | 24.2 us: 1.21x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                                  |
| xml_etree_parse      | 164 ms                                                              | 146 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                              | 99.3 ms: 1.12x faster                                                  |
| unpickle             | 15.0 us                                                             | 13.7 us: 1.10x faster                                                  |
| pickle_list          | 4.73 us                                                             | 4.35 us: 1.09x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 5.11 us: 1.03x slower                                                  |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 32.6 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.81 ms: 1.61x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.51 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.89 ms: 1.49x faster                                                  |
| django_template | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 21.9 ms: 1.39x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 47.0 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230406-linux-x86_64-python-affedee8bf2ec00c404f-3.12.0a7+-affedee |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.1 ms: 2.60x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.24 ms: 2.25x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                   |
| scimark_sor             | 198 ms                                                              | 110 ms: 1.79x faster                                                   |
| logging_silent          | 169 ns                                                              | 94.9 ns: 1.78x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.22 ms: 1.69x faster                                                  |
| nbody                   | 146 ms                                                              | 86.9 ms: 1.68x faster                                                  |
| richards                | 74.2 ms                                                             | 44.4 ms: 1.67x faster                                                  |
| raytrace                | 470 ms                                                              | 284 ms: 1.65x faster                                                   |
| spectral_norm           | 150 ms                                                              | 91.3 ms: 1.64x faster                                                  |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.51 ms: 1.63x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 66.8 ms: 1.63x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 72.2 ms: 1.62x faster                                                  |
| python_startup          | 14.1 ms                                                             | 8.81 ms: 1.61x faster                                                  |
| pyflate                 | 671 ms                                                              | 422 ms: 1.59x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 5.99 ms: 1.59x faster                                                  |
| chaos                   | 106 ms                                                              | 66.9 ms: 1.58x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 289 us: 1.58x faster                                                   |
| deepcopy_memo           | 51.8 us                                                             | 33.9 us: 1.53x faster                                                  |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.50x faster                                                   |
| float                   | 110 ms                                                              | 73.5 ms: 1.49x faster                                                  |
| mako                    | 14.7 ms                                                             | 9.89 ms: 1.49x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 203 us: 1.48x faster                                                   |
| unpack_sequence         | 65.6 ns                                                             | 44.6 ns: 1.47x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.27 ms: 1.46x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.47 ms: 1.45x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.33 us: 1.43x faster                                                  |
| logging_simple          | 8.21 us                                                             | 5.74 us: 1.43x faster                                                  |
| tornado_http            | 129 ms                                                              | 90.8 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.40 sec: 1.41x faster                                                 |
| html5lib                | 86.4 ms                                                             | 61.4 ms: 1.41x faster                                                  |
| django_template         | 45.8 ms                                                             | 32.7 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 685 ms: 1.39x faster                                                   |
| genshi_text             | 30.4 ms                                                             | 21.9 ms: 1.39x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.38x faster                                                 |
| genshi_xml              | 64.3 ms                                                             | 47.0 ms: 1.37x faster                                                  |
| async_tree_none         | 713 ms                                                              | 522 ms: 1.37x faster                                                   |
| scimark_fft             | 425 ms                                                              | 312 ms: 1.36x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 55.2 ms: 1.36x faster                                                  |
| deepcopy                | 438 us                                                              | 324 us: 1.35x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 633 ms: 1.35x faster                                                   |
| coroutines              | 31.8 ms                                                             | 23.6 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| regex_compile           | 177 ms                                                              | 133 ms: 1.34x faster                                                   |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.33x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                 |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                  |
| fannkuch                | 485 ms                                                              | 374 ms: 1.30x faster                                                   |
| thrift                  | 1.04 ms                                                             | 800 us: 1.30x faster                                                   |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.34 ms: 1.29x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.29x faster                                                   |
| deepcopy_reduce         | 3.80 us                                                             | 2.94 us: 1.29x faster                                                  |
| mypy2                   | 432 ms                                                              | 336 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 736 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 50.9 ms: 1.28x faster                                                  |
| comprehensions          | 27.3 us                                                             | 21.4 us: 1.27x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                 |
| nqueens                 | 98.8 ms                                                             | 79.6 ms: 1.24x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.22x faster                                                   |
| json_loads              | 29.3 us                                                             | 24.2 us: 1.21x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                                   |
| dulwich_log             | 76.3 ms                                                             | 63.3 ms: 1.21x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.6 ms: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.3 ms: 1.20x faster                                                  |
| sympy_expand            | 540 ms                                                              | 456 ms: 1.18x faster                                                   |
| json                    | 5.41 ms                                                             | 4.58 ms: 1.18x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                                  |
| sympy_str               | 328 ms                                                              | 282 ms: 1.16x faster                                                   |
| djangocms               | 36.3 us                                                             | 32.0 us: 1.13x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.64 us: 1.13x faster                                                  |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                                  |
| xml_etree_parse         | 164 ms                                                              | 146 ms: 1.12x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                              | 99.3 ms: 1.12x faster                                                  |
| sympy_sum               | 185 ms                                                              | 165 ms: 1.12x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.51 sec: 1.10x faster                                                 |
| unpickle                | 15.0 us                                                             | 13.7 us: 1.10x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.35 us: 1.09x faster                                                  |
| pathlib                 | 19.8 ms                                                             | 18.3 ms: 1.08x faster                                                  |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.44 ms: 1.04x faster                                                  |
| async_generators        | 420 ms                                                              | 414 ms: 1.01x faster                                                   |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 5.11 us: 1.03x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.65 ms: 1.04x slower                                                  |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.48 ms: 1.08x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.51 ms: 1.12x slower                                                  |
| dask                    | 437 ms                                                              | 502 ms: 1.15x slower                                                   |
| pickle_dict             | 27.8 us                                                             | 32.6 us: 1.18x slower                                                  |
| coverage                | 70.6 ms                                                             | 98.7 ms: 1.40x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
