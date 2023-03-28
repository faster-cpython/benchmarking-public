
# Results vs. 3.10.4

- fork: python
- ref: 89e67ada6958cfd8d4ee
- machine: linux-x86_64
- commit hash: 89e67ad
- commit date: 2023-03-27
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                 |
| html5lib       | 86.4 ms                                                             | 62.0 ms: 1.39x faster                                                  |
| tornado_http   | 129 ms                                                              | 91.2 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                               | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.3 ms: 1.67x faster                                                  |
| float          | 110 ms                                                              | 73.4 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.32x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                                  |
| regex_dna      | 213 ms                                                              | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.43 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                               | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 288 us: 1.59x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 200 us: 1.50x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.52 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 56.0 ms: 1.33x faster                                                  |
| json_loads           | 29.3 us                                                             | 24.1 us: 1.22x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 80.9 ms: 1.17x faster                                                  |
| pickle_list          | 4.73 us                                                             | 4.15 us: 1.14x faster                                                  |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 100 ms: 1.11x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                   |
| unpickle_list        | 4.94 us                                                             | 5.08 us: 1.03x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.2 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.80 ms: 1.61x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.50 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                                  |
| django_template | 45.8 ms                                                             | 33.1 ms: 1.39x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 47.4 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 28.9 ms: 2.62x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.20 ms: 2.28x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 502 ms: 1.84x faster                                                   |
| logging_silent          | 169 ns                                                              | 94.5 ns: 1.79x faster                                                  |
| scimark_sor             | 198 ms                                                              | 111 ms: 1.78x faster                                                   |
| richards                | 74.2 ms                                                             | 43.5 ms: 1.70x faster                                                  |
| nbody                   | 146 ms                                                              | 87.3 ms: 1.67x faster                                                  |
| raytrace                | 470 ms                                                              | 282 ms: 1.67x faster                                                   |
| spectral_norm           | 150 ms                                                              | 91.8 ms: 1.63x faster                                                  |
| go                      | 226 ms                                                              | 139 ms: 1.62x faster                                                   |
| python_startup          | 14.1 ms                                                             | 8.80 ms: 1.61x faster                                                  |
| pyflate                 | 671 ms                                                              | 418 ms: 1.61x faster                                                   |
| chaos                   | 106 ms                                                              | 66.7 ms: 1.59x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 288 us: 1.59x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 73.6 ms: 1.58x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 6.02 ms: 1.58x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 41.8 ns: 1.57x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 69.1 ms: 1.57x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 33.6 us: 1.54x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 200 us: 1.50x faster                                                   |
| float                   | 110 ms                                                              | 73.4 ms: 1.50x faster                                                  |
| mako                    | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                                  |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.45x faster                                                   |
| sqlglot_parse           | 2.07 ms                                                             | 1.43 ms: 1.45x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 9.52 ms: 1.44x faster                                                  |
| logging_simple          | 8.21 us                                                             | 5.77 us: 1.42x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.37 us: 1.42x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                  |
| tornado_http            | 129 ms                                                              | 91.2 ms: 1.41x faster                                                  |
| genshi_text             | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                                  |
| html5lib                | 86.4 ms                                                             | 62.0 ms: 1.39x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.39x faster                                                 |
| django_template         | 45.8 ms                                                             | 33.1 ms: 1.39x faster                                                  |
| coroutines              | 31.8 ms                                                             | 22.9 ms: 1.39x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                                 |
| async_tree_io           | 1.78 sec                                                            | 1.29 sec: 1.38x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 696 ms: 1.37x faster                                                   |
| async_tree_none         | 713 ms                                                              | 524 ms: 1.36x faster                                                   |
| scimark_fft             | 425 ms                                                              | 313 ms: 1.36x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 47.4 ms: 1.36x faster                                                  |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                   |
| deepcopy                | 438 us                                                              | 328 us: 1.33x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 56.0 ms: 1.33x faster                                                  |
| thrift                  | 1.04 ms                                                             | 781 us: 1.33x faster                                                   |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.25 ms: 1.32x faster                                                  |
| regex_compile           | 177 ms                                                              | 134 ms: 1.32x faster                                                   |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.31x faster                                                  |
| deepcopy_reduce         | 3.80 us                                                             | 2.92 us: 1.30x faster                                                  |
| mypy2                   | 432 ms                                                              | 332 ms: 1.30x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 656 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 738 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 51.5 ms: 1.27x faster                                                  |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                 |
| sqlglot_normalize       | 135 ms                                                              | 107 ms: 1.26x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 80.4 ms: 1.23x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                                   |
| json_loads              | 29.3 us                                                             | 24.1 us: 1.22x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.5 ms: 1.21x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 788 us: 1.21x faster                                                   |
| dulwich_log             | 76.3 ms                                                             | 63.1 ms: 1.21x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                                  |
| sympy_expand            | 540 ms                                                              | 460 ms: 1.17x faster                                                   |
| xml_etree_generate      | 94.9 ms                                                             | 80.9 ms: 1.17x faster                                                  |
| json                    | 5.41 ms                                                             | 4.64 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                              | 283 ms: 1.16x faster                                                   |
| comprehensions          | 27.3 us                                                             | 23.8 us: 1.15x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 21.8 ms: 1.14x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.60 us: 1.14x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.15 us: 1.14x faster                                                  |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.13x faster                                                  |
| sympy_sum               | 185 ms                                                              | 164 ms: 1.13x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 17.6 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                                  |
| djangocms               | 36.3 us                                                             | 32.6 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 100 ms: 1.11x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.51 sec: 1.10x faster                                                 |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.10x faster                                                   |
| regex_dna               | 213 ms                                                              | 203 ms: 1.05x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.46 ms: 1.03x faster                                                  |
| async_generators        | 420 ms                                                              | 410 ms: 1.02x faster                                                   |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 5.08 us: 1.03x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.67 ms: 1.04x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.43 ms: 1.06x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.50 ms: 1.12x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 31.2 us: 1.12x slower                                                  |
| dask                    | 437 ms                                                              | 510 ms: 1.17x slower                                                   |
| coverage                | 70.6 ms                                                             | 96.7 ms: 1.37x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                           |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
