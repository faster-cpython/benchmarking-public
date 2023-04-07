
# Results vs. 3.10.4

- fork: iritkatriel
- ref: asyncgen
- machine: linux-x86_64
- commit hash: 4a2152f
- commit date: 2023-04-07
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 252 ms: 1.33x faster                                            |
| chameleon      | 9.13 ms                                                             | 6.54 ms: 1.40x faster                                           |
| docutils       | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                          |
| html5lib       | 86.4 ms                                                             | 62.0 ms: 1.39x faster                                           |
| tornado_http   | 129 ms                                                              | 90.9 ms: 1.42x faster                                           |
| Geometric mean | (ref)                                                               | 1.36x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.4 ms: 1.67x faster                                           |
| float          | 110 ms                                                              | 74.4 ms: 1.48x faster                                           |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                               | 1.35x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.32x faster                                            |
| regex_v8       | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                           |
| regex_effbot   | 3.22 ms                                                             | 3.74 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                               | 1.06x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 287 us: 1.59x faster                                            |
| unpickle_pure_python | 300 us                                                              | 198 us: 1.51x faster                                            |
| json_dumps           | 13.7 ms                                                             | 9.59 ms: 1.43x faster                                           |
| xml_etree_process    | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                           |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.21x faster                                           |
| xml_etree_generate   | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                           |
| xml_etree_iterparse  | 111 ms                                                              | 99.4 ms: 1.12x faster                                           |
| pickle_list          | 4.73 us                                                             | 4.24 us: 1.11x faster                                           |
| unpickle             | 15.0 us                                                             | 13.4 us: 1.11x faster                                           |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                            |
| unpickle_list        | 4.94 us                                                             | 4.98 us: 1.01x slower                                           |
| pickle               | 10.2 us                                                             | 10.4 us: 1.02x slower                                           |
| pickle_dict          | 27.8 us                                                             | 32.2 us: 1.16x slower                                           |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                           |
| python_startup_no_site | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                           |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.97 ms: 1.48x faster                                           |
| genshi_text     | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                           |
| django_template | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                           |
| genshi_xml      | 64.3 ms                                                             | 47.8 ms: 1.34x faster                                           |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.6 ms: 2.56x faster                                           |
| deltablue               | 7.30 ms                                                             | 3.19 ms: 2.29x faster                                           |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                            |
| logging_silent          | 169 ns                                                              | 94.5 ns: 1.79x faster                                           |
| scimark_sor             | 198 ms                                                              | 111 ms: 1.78x faster                                            |
| raytrace                | 470 ms                                                              | 280 ms: 1.68x faster                                            |
| richards                | 74.2 ms                                                             | 44.3 ms: 1.67x faster                                           |
| nbody                   | 146 ms                                                              | 87.4 ms: 1.67x faster                                           |
| go                      | 226 ms                                                              | 140 ms: 1.61x faster                                            |
| python_startup          | 14.1 ms                                                             | 8.84 ms: 1.60x faster                                           |
| chaos                   | 106 ms                                                              | 66.3 ms: 1.60x faster                                           |
| pyflate                 | 671 ms                                                              | 421 ms: 1.59x faster                                            |
| pickle_pure_python      | 457 us                                                              | 287 us: 1.59x faster                                            |
| crypto_pyaes            | 117 ms                                                              | 74.0 ms: 1.58x faster                                           |
| hexiom                  | 9.50 ms                                                             | 6.04 ms: 1.57x faster                                           |
| scimark_monte_carlo     | 109 ms                                                              | 68.9 ms: 1.57x faster                                           |
| spectral_norm           | 150 ms                                                              | 96.2 ms: 1.56x faster                                           |
| unpack_sequence         | 65.6 ns                                                             | 42.7 ns: 1.54x faster                                           |
| deepcopy_memo           | 51.8 us                                                             | 34.0 us: 1.52x faster                                           |
| unpickle_pure_python    | 300 us                                                              | 198 us: 1.51x faster                                            |
| scimark_lu              | 160 ms                                                              | 108 ms: 1.48x faster                                            |
| mako                    | 14.7 ms                                                             | 9.97 ms: 1.48x faster                                           |
| float                   | 110 ms                                                              | 74.4 ms: 1.48x faster                                           |
| logging_format          | 9.07 us                                                             | 6.25 us: 1.45x faster                                           |
| sqlglot_parse           | 2.07 ms                                                             | 1.43 ms: 1.45x faster                                           |
| logging_simple          | 8.21 us                                                             | 5.70 us: 1.44x faster                                           |
| json_dumps              | 13.7 ms                                                             | 9.59 ms: 1.43x faster                                           |
| sqlglot_transpile       | 2.45 ms                                                             | 1.72 ms: 1.43x faster                                           |
| tornado_http            | 129 ms                                                              | 90.9 ms: 1.42x faster                                           |
| genshi_text             | 30.4 ms                                                             | 21.6 ms: 1.41x faster                                           |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.40x faster                                          |
| chameleon               | 9.13 ms                                                             | 6.54 ms: 1.40x faster                                           |
| html5lib                | 86.4 ms                                                             | 62.0 ms: 1.39x faster                                           |
| django_template         | 45.8 ms                                                             | 33.0 ms: 1.39x faster                                           |
| pprint_safe_repr        | 953 ms                                                              | 687 ms: 1.39x faster                                            |
| scimark_fft             | 425 ms                                                              | 307 ms: 1.39x faster                                            |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                          |
| coroutines              | 31.8 ms                                                             | 23.3 ms: 1.37x faster                                           |
| deepcopy                | 438 us                                                              | 322 us: 1.36x faster                                            |
| async_tree_none         | 713 ms                                                              | 524 ms: 1.36x faster                                            |
| xml_etree_process       | 74.8 ms                                                             | 55.0 ms: 1.36x faster                                           |
| genshi_xml              | 64.3 ms                                                             | 47.8 ms: 1.34x faster                                           |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.34x faster                                          |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                           |
| async_tree_memoization  | 853 ms                                                              | 637 ms: 1.34x faster                                            |
| 2to3                    | 336 ms                                                              | 252 ms: 1.33x faster                                            |
| thrift                  | 1.04 ms                                                             | 781 us: 1.33x faster                                            |
| gunicorn                | 1.43 ms                                                             | 1.09 ms: 1.32x faster                                           |
| regex_compile           | 177 ms                                                              | 135 ms: 1.32x faster                                            |
| deepcopy_reduce         | 3.80 us                                                             | 2.90 us: 1.31x faster                                           |
| mypy2                   | 432 ms                                                              | 332 ms: 1.30x faster                                            |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.33 ms: 1.30x faster                                           |
| async_tree_cpu_io_mixed | 944 ms                                                              | 739 ms: 1.28x faster                                            |
| sqlglot_normalize       | 135 ms                                                              | 105 ms: 1.28x faster                                            |
| sqlglot_optimize        | 65.3 ms                                                             | 51.2 ms: 1.27x faster                                           |
| docutils                | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                          |
| nqueens                 | 98.8 ms                                                             | 80.1 ms: 1.23x faster                                           |
| fannkuch                | 485 ms                                                              | 394 ms: 1.23x faster                                            |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.22x faster                                            |
| dulwich_log             | 76.3 ms                                                             | 63.0 ms: 1.21x faster                                           |
| bench_thread_pool       | 954 us                                                              | 790 us: 1.21x faster                                            |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.21x faster                                           |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.7 ms: 1.19x faster                                           |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                           |
| xml_etree_generate      | 94.9 ms                                                             | 80.6 ms: 1.18x faster                                           |
| sympy_expand            | 540 ms                                                              | 460 ms: 1.17x faster                                            |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                           |
| sympy_str               | 328 ms                                                              | 284 ms: 1.15x faster                                            |
| comprehensions          | 27.3 us                                                             | 23.8 us: 1.14x faster                                           |
| sqlite_synth            | 2.97 us                                                             | 2.61 us: 1.14x faster                                           |
| xml_etree_iterparse     | 111 ms                                                              | 99.4 ms: 1.12x faster                                           |
| meteor_contest          | 115 ms                                                              | 103 ms: 1.12x faster                                            |
| djangocms               | 36.3 us                                                             | 32.5 us: 1.12x faster                                           |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.12x faster                                           |
| pickle_list             | 4.73 us                                                             | 4.24 us: 1.11x faster                                           |
| unpickle                | 15.0 us                                                             | 13.4 us: 1.11x faster                                           |
| regex_v8                | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                           |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                            |
| mdp                     | 2.75 sec                                                            | 2.50 sec: 1.10x faster                                          |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                            |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                           |
| telco                   | 6.67 ms                                                             | 6.46 ms: 1.03x faster                                           |
| async_generators        | 420 ms                                                              | 407 ms: 1.03x faster                                            |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                            |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                           |
| unpickle_list           | 4.94 us                                                             | 4.98 us: 1.01x slower                                           |
| pickle                  | 10.2 us                                                             | 10.4 us: 1.02x slower                                           |
| python_startup_no_site  | 5.80 ms                                                             | 6.52 ms: 1.13x slower                                           |
| pickle_dict             | 27.8 us                                                             | 32.2 us: 1.16x slower                                           |
| regex_effbot            | 3.22 ms                                                             | 3.74 ms: 1.16x slower                                           |
| dask                    | 437 ms                                                              | 509 ms: 1.17x slower                                            |
| gc_traversal            | 3.53 ms                                                             | 4.32 ms: 1.22x slower                                           |
| coverage                | 70.6 ms                                                             | 95.4 ms: 1.35x slower                                           |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                    |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
