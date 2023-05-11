
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 259 ms: 1.30x faster                                   |
| chameleon      | 9.13 ms                                                             | 6.47 ms: 1.41x faster                                  |
| docutils       | 3.19 sec                                                            | 2.63 sec: 1.22x faster                                 |
| html5lib       | 86.4 ms                                                             | 64.5 ms: 1.34x faster                                  |
| tornado_http   | 129 ms                                                              | 96.3 ms: 1.34x faster                                  |
| Geometric mean | (ref)                                                               | 1.32x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.1 ms: 1.57x faster                                  |
| float          | 110 ms                                                              | 77.2 ms: 1.42x faster                                  |
| pidigits       | 190 ms                                                              | 198 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                               | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 138 ms: 1.28x faster                                   |
| regex_v8       | 24.9 ms                                                             | 22.0 ms: 1.13x faster                                  |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                   |
| regex_effbot   | 3.22 ms                                                             | 3.99 ms: 1.24x slower                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 306 us: 1.49x faster                                   |
| xml_etree_process    | 74.8 ms                                                             | 53.9 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                              | 228 us: 1.31x faster                                   |
| xml_etree_generate   | 94.9 ms                                                             | 76.2 ms: 1.24x faster                                  |
| pickle_list          | 4.73 us                                                             | 4.11 us: 1.15x faster                                  |
| json_loads           | 29.3 us                                                             | 26.5 us: 1.11x faster                                  |
| unpickle             | 15.0 us                                                             | 13.7 us: 1.09x faster                                  |
| json_dumps           | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 164 ms                                                              | 158 ms: 1.03x faster                                   |
| pickle               | 10.2 us                                                             | 10.1 us: 1.01x faster                                  |
| unpickle_list        | 4.94 us                                                             | 4.91 us: 1.01x faster                                  |
| pickle_dict          | 27.8 us                                                             | 31.1 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                               | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.52 ms: 1.66x faster                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.01 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                               | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                  |
| genshi_text     | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                  |
| django_template | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                  |
| genshi_xml      | 64.3 ms                                                             | 51.8 ms: 1.24x faster                                  |
| Geometric mean  | (ref)                                                               | 1.38x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.67 ms: 1.99x faster                                  |
| scimark_sor             | 198 ms                                                              | 118 ms: 1.67x faster                                   |
| logging_silent          | 169 ns                                                              | 101 ns: 1.67x faster                                   |
| python_startup          | 14.1 ms                                                             | 8.52 ms: 1.66x faster                                  |
| richards                | 74.2 ms                                                             | 45.7 ms: 1.62x faster                                  |
| go                      | 226 ms                                                              | 140 ms: 1.61x faster                                   |
| pyflate                 | 671 ms                                                              | 418 ms: 1.60x faster                                   |
| scimark_monte_carlo     | 109 ms                                                              | 68.1 ms: 1.59x faster                                  |
| raytrace                | 470 ms                                                              | 297 ms: 1.58x faster                                   |
| nbody                   | 146 ms                                                              | 93.1 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                              | 74.7 ms: 1.56x faster                                  |
| chaos                   | 106 ms                                                              | 69.2 ms: 1.53x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 43.1 ns: 1.52x faster                                  |
| spectral_norm           | 150 ms                                                              | 100 ms: 1.50x faster                                   |
| pickle_pure_python      | 457 us                                                              | 306 us: 1.49x faster                                   |
| hexiom                  | 9.50 ms                                                             | 6.37 ms: 1.49x faster                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.40 ms: 1.48x faster                                  |
| mako                    | 14.7 ms                                                             | 10.1 ms: 1.46x faster                                  |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.46x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.70 ms: 1.44x faster                                  |
| float                   | 110 ms                                                              | 77.2 ms: 1.42x faster                                  |
| chameleon               | 9.13 ms                                                             | 6.47 ms: 1.41x faster                                  |
| genshi_text             | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                  |
| django_template         | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                  |
| deepcopy_memo           | 51.8 us                                                             | 37.0 us: 1.40x faster                                  |
| xml_etree_process       | 74.8 ms                                                             | 53.9 ms: 1.39x faster                                  |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                 |
| thrift                  | 1.04 ms                                                             | 756 us: 1.37x faster                                   |
| logging_simple          | 8.21 us                                                             | 6.03 us: 1.36x faster                                  |
| async_tree_memoization  | 853 ms                                                              | 627 ms: 1.36x faster                                   |
| pprint_safe_repr        | 953 ms                                                              | 701 ms: 1.36x faster                                   |
| pprint_pformat          | 1.98 sec                                                            | 1.46 sec: 1.36x faster                                 |
| logging_format          | 9.07 us                                                             | 6.68 us: 1.36x faster                                  |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.35x faster                                   |
| tornado_http            | 129 ms                                                              | 96.3 ms: 1.34x faster                                  |
| html5lib                | 86.4 ms                                                             | 64.5 ms: 1.34x faster                                  |
| unpickle_pure_python    | 300 us                                                              | 228 us: 1.31x faster                                   |
| pycparser               | 1.53 sec                                                            | 1.18 sec: 1.30x faster                                 |
| 2to3                    | 336 ms                                                              | 259 ms: 1.30x faster                                   |
| scimark_fft             | 425 ms                                                              | 328 ms: 1.30x faster                                   |
| deepcopy_reduce         | 3.80 us                                                             | 2.94 us: 1.29x faster                                  |
| regex_compile           | 177 ms                                                              | 138 ms: 1.28x faster                                   |
| deepcopy                | 438 us                                                              | 342 us: 1.28x faster                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 739 ms: 1.28x faster                                   |
| fannkuch                | 485 ms                                                              | 388 ms: 1.25x faster                                   |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.50 ms: 1.25x faster                                  |
| sqlglot_normalize       | 135 ms                                                              | 108 ms: 1.25x faster                                   |
| coroutines              | 31.8 ms                                                             | 25.5 ms: 1.25x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 76.2 ms: 1.24x faster                                  |
| genshi_xml              | 64.3 ms                                                             | 51.8 ms: 1.24x faster                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 53.1 ms: 1.23x faster                                  |
| aiohttp                 | 1.35 ms                                                             | 1.10 ms: 1.23x faster                                  |
| gunicorn                | 1.43 ms                                                             | 1.18 ms: 1.22x faster                                  |
| docutils                | 3.19 sec                                                            | 2.63 sec: 1.22x faster                                 |
| dask                    | 437 ms                                                              | 360 ms: 1.21x faster                                   |
| comprehensions          | 27.3 us                                                             | 22.4 us: 1.21x faster                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 138 ms: 1.20x faster                                   |
| dulwich_log             | 76.3 ms                                                             | 63.7 ms: 1.20x faster                                  |
| flaskblogging           | 8.48 ms                                                             | 7.12 ms: 1.19x faster                                  |
| nqueens                 | 98.8 ms                                                             | 83.4 ms: 1.19x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                  |
| sqlite_synth            | 2.97 us                                                             | 2.52 us: 1.18x faster                                  |
| bench_thread_pool       | 954 us                                                              | 819 us: 1.16x faster                                   |
| sympy_integrate         | 24.3 ms                                                             | 21.0 ms: 1.16x faster                                  |
| pickle_list             | 4.73 us                                                             | 4.11 us: 1.15x faster                                  |
| async_generators        | 420 ms                                                              | 368 ms: 1.14x faster                                   |
| sympy_expand            | 540 ms                                                              | 475 ms: 1.14x faster                                   |
| regex_v8                | 24.9 ms                                                             | 22.0 ms: 1.13x faster                                  |
| sympy_str               | 328 ms                                                              | 290 ms: 1.13x faster                                   |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                  |
| pylint                  | 521 ms                                                              | 465 ms: 1.12x faster                                   |
| sympy_sum               | 185 ms                                                              | 167 ms: 1.11x faster                                   |
| json_loads              | 29.3 us                                                             | 26.5 us: 1.11x faster                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                  |
| json                    | 5.41 ms                                                             | 4.94 ms: 1.10x faster                                  |
| unpickle                | 15.0 us                                                             | 13.7 us: 1.09x faster                                  |
| json_dumps              | 13.7 ms                                                             | 12.6 ms: 1.09x faster                                  |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                  |
| meteor_contest          | 115 ms                                                              | 107 ms: 1.07x faster                                   |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| mdp                     | 2.75 sec                                                            | 2.62 sec: 1.05x faster                                 |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                   |
| xml_etree_parse         | 164 ms                                                              | 158 ms: 1.03x faster                                   |
| generators              | 75.7 ms                                                             | 73.5 ms: 1.03x faster                                  |
| pickle                  | 10.2 us                                                             | 10.1 us: 1.01x faster                                  |
| telco                   | 6.67 ms                                                             | 6.58 ms: 1.01x faster                                  |
| unpickle_list           | 4.94 us                                                             | 4.91 us: 1.01x faster                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.01 ms: 1.04x slower                                  |
| pidigits                | 190 ms                                                              | 198 ms: 1.04x slower                                   |
| pickle_dict             | 27.8 us                                                             | 31.1 us: 1.12x slower                                  |
| gc_traversal            | 3.53 ms                                                             | 4.02 ms: 1.14x slower                                  |
| regex_effbot            | 3.22 ms                                                             | 3.99 ms: 1.24x slower                                  |
| coverage                | 70.6 ms                                                             | 100 ms: 1.42x slower                                   |
| Geometric mean          | (ref)                                                               | 1.25x faster                                           |

Benchmark hidden because not significant (3): mypy2, asyncio_tcp, bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
